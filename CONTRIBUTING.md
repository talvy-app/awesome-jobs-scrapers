# Contribuir

Gracias por el interés. Este listado se mantiene con criterios estrictos y
verificables; léelos antes de proponer nada.

## Solo issues

Este repositorio **no acepta PRs de terceros** (el único PR que se abre aquí
lo genera el CI semestral de verificación). Para proponer un recurso, abre un
issue con la plantilla **«Sugerir recurso»**.

## Criterios de admisión

Un recurso entra en el listado si cumple **todas** estas condiciones:

1. **Barra de mantenimiento**: el repo tiene commits de los **últimos 12
   meses** y **no está archivado** en GitHub. Se comprueba contra la API de
   GitHub en el momento del alta.
2. **Relevancia**: sirve para scrapear, agregar o consumir ofertas de trabajo
   (librerías, conectores ATS, APIs, plataformas, infra anti-bot, datasets o
   guías). No entra scraping genérico sin relación con empleo.
3. **Originalidad**: no forks ni clones sin valor añadido sobre proyectos ya
   listados.
4. **Identifiable**: descripción clara, licencia visible y README que explique
   qué fuentes cubre y con qué estrategia (API, endpoint ATS, HTML o browser
   automation).

## Secciones

La taxonomía completa y el significado de los niveles (⭐ Core / Sólido /
Nicho) están en el [README](README.md#criterios-editoriales). Indica en tu
issue la sección donde crees que encaja; la decisión final es del mantenedor.

## Archivo

Un recurso se mueve a la sección **Archivo** si su repo queda archived en
GitHub o supera los 18 meses sin commits con señales de roto. Cada semestre
(el 1 de enero y el 1 de julio) el CI re-verifica todo el listado y, si hay
candidatos, abre un PR con la evidencia que el mantenedor aprueba o descarta.

Si eres el autor de un recurso archivado y lo reactivas (commits recientes),
abre un issue pidiendo la recuperación: se revisa con los mismos criterios.
