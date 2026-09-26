#!/usr/bin/env python3
"""Verificación de recursos para awesome-jobs-scrapers.

Modos:
  lookup <slugs.json> [--out data/verified.json]
      Consulta la API de GitHub para cada repo (lista de slugs "owner/repo")
      y guarda el snapshot: archived, pushed_at, stars, license, descripción.
  check [--readme README.md] [--out data/to-archive.json] [--report data/verify-report.md]
      Extrae los repos de las secciones activas del README (todo lo anterior
      a la sección Archivo) y audita la barra de mantenimiento:
        OK       → no archived y último commit <= 12 meses
        WARN     -> último commit entre 12 y 18 meses
        ARCHIVE  → repo archived en GitHub, o sin commits > 18 meses
      Escribe los candidatos a archivo en JSON y un informe markdown.

Token: $GITHUB_TOKEN / $GH_TOKEN, o el de `gh auth token`.
Solo librería estándar.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

API = "https://api.github.com"
MONTHS_ARCHIVO = 18
MONTHS_WARN = 12


def get_token() -> str:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token.strip()
    try:
        out = subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, timeout=15
        )
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
    except (OSError, subprocess.TimeoutExpired):
        pass
    return ""


class GitHub:
    def __init__(self) -> None:
        self.token = get_token()
        self.reset_at = 0.0

    def _sleep_until_reset(self, headers: dict[str, str]) -> None:
        reset = headers.get("x-ratelimit-reset")
        if reset:
            wait = float(reset) - time.time() + 2
            if 0 < wait < 3600:
                print(f"rate limit agotado; esperando {int(wait)}s", file=sys.stderr)
                time.sleep(wait)

    def request(self, path: str) -> dict | list | None:
        url = path if path.startswith("http") else API + path
        for attempt in range(4):
            req = urllib.request.Request(url)
            req.add_header("Accept", "application/vnd.github+json")
            req.add_header("User-Agent", "awesome-jobs-scrapers-verify")
            if self.token:
                req.add_header("Authorization", f"Bearer {self.token}")
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    return json.load(resp)
            except urllib.error.HTTPError as e:
                if e.code in (403, 429) and e.headers.get("x-ratelimit-remaining") == "0":
                    self._sleep_until_reset(dict(e.headers))
                    continue
                if e.code == 404:
                    return None
                if e.code >= 500 and attempt < 3:
                    time.sleep(2 * (attempt + 1))
                    continue
                raise
            except urllib.error.URLError:
                if attempt < 3:
                    time.sleep(2 * (attempt + 1))
                    continue
                raise
        return None


def repo_snapshot(gh: GitHub, slug: str) -> dict | None:
    data = gh.request(f"/repos/{slug}")
    if data is None:
        return None
    lic = data.get("license") or {}
    return {
        "repo": data["full_name"],
        "url": data["html_url"],
        "description": (data.get("description") or "").strip(),
        "archived": bool(data.get("archived")),
        "pushed_at": (data.get("pushed_at") or "")[:10],
        "stars": data.get("stargazers_count", 0),
        "language": data.get("language"),
        "license": lic.get("spdx_id"),
        "topics": data.get("topics") or [],
        "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }


def cmd_lookup(args: argparse.Namespace) -> None:
    gh = GitHub()
    with open(args.slugs, encoding="utf-8") as f:
        slugs = json.load(f)
    result: dict[str, dict | None] = {}
    for i, slug in enumerate(slugs, 1):
        result[slug] = repo_snapshot(gh, slug)
        status = "404" if result[slug] is None else result[slug]["pushed_at"]  # type: ignore[index]
        print(f"[{i}/{len(slugs)}] {slug}: {status}", file=sys.stderr)
    out = args.out or "data/verified.json"
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    print(f"escrito {out} ({len(slugs)} repos)")


REPO_LINK = re.compile(r"github\.com/([\w.-]+/[\w.-]+)/?(?:[?#)].*)?$")


def parse_readme(path: str) -> tuple[list[tuple[str, str, int]], str]:
    """Devuelve [(slug, linea, num_linea)] de las secciones activas y el contenido."""
    with open(path, encoding="utf-8") as f:
        content = f.read()
    marker = re.search(r"^##\s.*[Aa]rchivo.*$", content, re.MULTILINE)
    active = content[: marker.start()] if marker else content
    entries = []
    for lineno, line in enumerate(active.splitlines(), 1):
        m = REPO_LINK.search(line)
        if m and line.lstrip().startswith("-"):
            entries.append((m.group(1).rstrip("."), line, lineno))
    return entries, content


def classify(snap: dict, now: datetime) -> tuple[str, str]:
    cutoff_warn = now - timedelta(days=MONTHS_WARN * 30.44)
    cutoff_arch = now - timedelta(days=MONTHS_ARCHIVO * 30.44)
    pushed = datetime.strptime(snap["pushed_at"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    if snap["archived"]:
        return "ARCHIVE", "repo archivado en GitHub"
    if pushed < cutoff_arch:
        return "ARCHIVE", f"sin commits desde {pushed:%Y-%m} (más de {MONTHS_ARCHIVO} meses)"
    if pushed < cutoff_warn:
        return "WARN", f"último commit {snap['pushed_at']} (más de {MONTHS_WARN} meses)"
    return "OK", ""


def cmd_check(args: argparse.Namespace) -> None:
    gh = GitHub()
    entries, _ = parse_readme(args.readme)
    seen: set[str] = set()
    now = datetime.now(timezone.utc)
    report: list[str] = ["# Informe de verificación", "", f"Fecha: {now:%Y-%m-%d}", ""]
    to_archive: list[dict] = []
    n_ok = n_warn = 0
    for i, (slug, _line, lineno) in enumerate(entries, 1):
        if slug in seen:
            continue
        seen.add(slug)
        snap = repo_snapshot(gh, slug)
        if snap is None:
            to_archive.append({"repo": slug, "reason": "repo inaccesible (404)", "pushed_at": None, "stars": None})
            report += [f"- ❌ `{slug}` (README línea {lineno}): inaccesible (404 o renombrado)"]
            continue
        status, reason = classify(snap, now)
        if status == "OK":
            n_ok += 1
        elif status == "WARN":
            n_warn += 1
            report += [f"- ⚠️ `{slug}` (README línea {lineno}): {reason}"]
        else:
            to_archive.append({"repo": slug, "reason": reason, "pushed_at": snap["pushed_at"], "stars": snap["stars"]})
            report += [f"- 🪦 `{slug}` (README línea {lineno}): {reason}"]
        print(f"[{i}/{len(entries)}] {slug}: {status}", file=sys.stderr)
        time.sleep(0.3)
    report += ["", f"**Resumen:** {n_ok} OK · {n_warn} en aviso · {len(to_archive)} candidatos a archivo", ""]
    for out, text in ((args.out, json.dumps(to_archive, ensure_ascii=False, indent=1)), (args.report, "\n".join(report))):
        if out:
            os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
            with open(out, "w", encoding="utf-8") as f:
                f.write(text)
    print(f"OK {n_ok} · WARN {n_warn} · ARCHIVE {len(to_archive)}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    lk = sub.add_parser("lookup", help="snapshot de repos desde una lista de slugs")
    lk.add_argument("slugs")
    lk.add_argument("--out", default="data/verified.json")
    ck = sub.add_parser("check", help="auditar la barra de mantenimiento del README")
    ck.add_argument("--readme", default="README.md")
    ck.add_argument("--out", default="data/to-archive.json")
    ck.add_argument("--report", default="data/verify-report.md")
    args = p.parse_args()
    {"lookup": cmd_lookup, "check": cmd_check}[args.cmd](args)


if __name__ == "__main__":
    main()
