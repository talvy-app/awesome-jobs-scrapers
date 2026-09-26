#!/usr/bin/env python3
"""Mueve a la sección Archivo los recursos marcados en data/to-archive.json.

Lo ejecuta el CI semestral tras `verify.py check`. Para cada candidato:
elimina su línea de la sección activa del README y añade una línea de baja
al final de la sección Archivo con motivo, fecha y último estado conocido.
También actualiza el badge de entradas activas. Idempotente.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone

README = "README.md"
ARCHIVE_JSON = "data/to-archive.json"
ARCHIVE_HEADING = re.compile(r"^##\s+8\.\s+Archivo\s*$", re.MULTILINE)
BADGE = re.compile(r"entradas_activas-(\d+)-")


def main() -> None:
    with open(ARCHIVE_JSON, encoding="utf-8") as f:
        candidates = json.load(f)
    if not candidates:
        print("sin candidatos; nada que hacer")
        return

    with open(README, encoding="utf-8") as f:
        content = f.read()

    split = ARCHIVE_HEADING.search(content)
    if not split:
        sys.exit("no encuentro la sección 8. Archivo en el README")
    active, archivo = content[: split.start()], content[split.start():]
    today = datetime.now(timezone.utc).strftime("%Y-%m")

    moved = 0
    for c in candidates:
        slug = c["repo"]
        pattern = re.compile(
            rf"^- [^\n]*github\.com/{re.escape(slug)}[)\"][^\n]*\n?",
            re.MULTILINE,
        )
        match = pattern.search(active)
        if not match:
            print(f"  = {slug}: no está en las secciones activas (¿ya archivado?)")
            continue
        active = pattern.sub("", active, count=1)
        stars = f"{c['stars']:,} ⭐".replace(",", ".") if c.get("stars") is not None else "n/d"
        pushed = c.get("pushed_at") or "desconocido"
        name = slug.split("/")[1]
        baja = (
            f"- **[{name}](https://github.com/{slug})** — 🪦 Archivado {today}: "
            f"{c['reason']}. Último estado: {stars}, último commit {pushed}.\n"
        )
        archivo = archivo.rstrip("\n") + "\n" + baja
        moved += 1
        print(f"  → {slug}: archivado ({c['reason']})")

    if moved == 0:
        print("nada movido; README sin cambios")
        return

    m = BADGE.search(active)
    if m:
        new = int(m.group(1)) - moved
        active = BADGE.sub(f"entradas_activas-{new}-", active, count=1)
        print(f"badge de entradas activas: {m.group(1)} → {new}")

    active = re.sub(r"\n{3,}", "\n\n", active)
    with open(README, "w", encoding="utf-8") as f:
        f.write(active + archivo)
    print(f"{moved} entradas movidas al Archivo")


if __name__ == "__main__":
    main()
