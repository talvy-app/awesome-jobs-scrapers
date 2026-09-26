# awesome-jobs-scrapers

> Listado curado de recursos **existentes y mantenidos** para scrapear y agregar ofertas de trabajo, con recursos principalmente de GitHub.

![última verificación](https://img.shields.io/badge/%C3%BAltima_verificaci%C3%B3n-2026-09-26-2ea44f)
![entradas activas](https://img.shields.io/badge/entradas_activas-124-0969da)
![licencia](https://img.shields.io/badge/licencia-MIT-green)
[![CI verificación](https://github.com/talvy-app/awesome-jobs-scrapers/actions/workflows/verify.yml/badge.svg)](https://github.com/talvy-app/awesome-jobs-scrapers/actions/workflows/verify.yml)

## Criterios editoriales

- **Barra de mantenimiento**: una entrada solo permanece si su repo tiene commits de los **últimos 12 meses** y **no está archivado** en GitHub. Cada alta se verifica contra la API de GitHub y un CI semestral re-verifica todo el listado.
- **Política de archivo**: un recurso se mueve a la [sección Archivo](#8-archivo) si su repo está archived en GitHub, o supera los **18 meses sin commits** con señales de roto. El CI propone el movimiento en un PR con la evidencia; el mantenedor aprueba. La entrada archivada conserva motivo, fecha y último estado conocido.
- **Jerarquía**: ⭐ **Core** (imprescindibles, con nota ampliada), **Sólido** (proyectos con tracción o arquitectura digna de estudio) y **Nicho** (cubren un hueco concreto: un ATS, un país, un formato).
- **Sin distinción legal**: los scrapers de portales cerrados (LinkedIn, Indeed, Glassdoor) entran igual que los consumidores de APIs públicas. El filtro de esta lista es el mantenimiento, no la legalidad de cada fuente; tú eres responsable de los términos de servicio de cada portal.
- **Badges por entrada**: ⭐ acumuladas y fecha del último commit, servidas en vivo por shields.io.

## Índice

1. [Agregadores multi-job-board](#1-agregadores-multi-job-board)
2. [Conectores ATS y career pages](#2-conectores-ats-y-career-pages)
3. [APIs y feeds públicos](#3-apis-y-feeds-públicos)
4. [Plataformas self-hosted end-to-end](#4-plataformas-self-hosted-end-to-end)
5. [Infra anti-bot y scraping general](#5-infra-anti-bot-y-scraping-general)
6. [Datasets y listas vigiladas](#6-datasets-y-listas-vigiladas)
7. [Tutoriales y guías](#7-tutoriales-y-guías)
8. [Archivo](#8-archivo)

## 1. Agregadores multi-job-board

Para buscar por keyword, ubicación, modalidad y fecha en las grandes bolsas de empleo. Aquí vive lo que la mayoría entiende por «scraper de empleo».

### Librerías y CLIs multi-board

- ⭐ **[JobSpy](https://github.com/speedyapply/JobSpy)** — La librería de referencia. Python; consulta en concurrente LinkedIn, Indeed, Glassdoor, Google Jobs, ZipRecruiter, Bayt, Naukri y bdjobs y devuelve un `pandas.DataFrame`. Ideal para pipelines ETL, notebooks y prototipos. Los conectores de portales cerrados pueden degradarse por cambios de frontend o anti-bot: diseña reintentos y observabilidad por fuente. ![4.354 ★](https://img.shields.io/badge/%E2%98%85-4.354-f5c518) ![last commit](https://img.shields.io/github/last-commit/speedyapply/JobSpy)
- ⭐ **[ever-jobs](https://github.com/ever-jobs/ever-jobs)** — Agregador completo autohospedado (TypeScript) sobre LinkedIn, Indeed, Glassdoor y más. Su valor principal es la documentación de técnicas por fuente — HTML/Cheerio, GraphQL, CSRF —; úsalo como referencia de arquitectura multi-fuente, no solo como librería. ![128 ★](https://img.shields.io/badge/%E2%98%85-128-f5c518) ![last commit](https://img.shields.io/github/last-commit/ever-jobs/ever-jobs)
- **[freehire](https://github.com/strelov1/freehire)** — Motor de búsqueda open-source para buscadores de empleo (Go): indexa boards y career pages en un buscador propio. ![772 ★](https://img.shields.io/badge/%E2%98%85-772-f5c518) ![last commit](https://img.shields.io/github/last-commit/strelov1/freehire)
- **[ts-jobspy](https://github.com/alpharomercoma/ts-jobspy)** — Reescritura en TypeScript de JobSpy: LinkedIn, Indeed, Glassdoor, ZipRecruiter y más. La vía natural para stacks Node.js. ![16 ★](https://img.shields.io/badge/%E2%98%85-16-f5c518) ![last commit](https://img.shields.io/github/last-commit/alpharomercoma/ts-jobspy)
- **[openroles](https://github.com/datascry/openroles)** — Agregador de ofertas abiertas en 52 plataformas de contratación, actualizado a diario y consultable desde el navegador. ![6 ★](https://img.shields.io/badge/%E2%98%85-6-f5c518) ![last commit](https://img.shields.io/github/last-commit/datascry/openroles)
- **[jobspy-node](https://github.com/DaKheera47/jobspy-node)** — Otro port de JobSpy a Node.js/TypeScript con API simple para scrapear varios portales. ![5 ★](https://img.shields.io/badge/%E2%98%85-5-f5c518) ![last commit](https://img.shields.io/github/last-commit/DaKheera47/jobspy-node)
- **[Job-API](https://github.com/sankeer28/Job-API)** — API unificada (Vercel) que compone JobSpy para los portales duros con las APIs públicas de RemoteOK, Arbeitnow, Remotive y Jobicy. Buena lección de arquitectura: scraping solo donde no hay feed. ![3 ★](https://img.shields.io/badge/%E2%98%85-3-f5c518) ![last commit](https://img.shields.io/github/last-commit/sankeer28/Job-API)
- **[php-jobspy](https://github.com/alexseif/php-jobspy)** — Motor en PHP (PSR) para scrapear LinkedIn, Indeed, Glassdoor y ZipRecruiter sin APIs de pago. ![2 ★](https://img.shields.io/badge/%E2%98%85-2-f5c518) ![last commit](https://img.shields.io/github/last-commit/alexseif/php-jobspy)
- **[jobspy-js](https://github.com/borgius/jobspy-js)** — Port a TypeScript de JobSpy con cobertura amplia (LinkedIn, Indeed, Glassdoor, Google, ZipRecruiter, Bayt, Naukri, BDJobs). ![1 ★](https://img.shields.io/badge/%E2%98%85-1-f5c518) ![last commit](https://img.shields.io/github/last-commit/borgius/jobspy-js)
- **[RUSTJobSpy](https://github.com/Liohtml/RUSTJobSpy)** — Port de JobSpy a Rust de alto rendimiento: Indeed, LinkedIn, Glassdoor, Naukri y más. ![0 ★](https://img.shields.io/badge/%E2%98%85-0-f5c518) ![last commit](https://img.shields.io/github/last-commit/Liohtml/RUSTJobSpy)

### Servidores MCP

- **[jobspy-mcp-server](https://github.com/borgius/jobspy-mcp-server)** — Servidor MCP para buscar empleo en múltiples plataformas desde Claude, Cursor o cualquier cliente MCP. ![115 ★](https://img.shields.io/badge/%E2%98%85-115-f5c518) ![last commit](https://img.shields.io/github/last-commit/borgius/jobspy-mcp-server)
- **[openings-mcp](https://github.com/amikai/openings-mcp)** — Servidor MCP (Go) que busca en job boards y career pages de empresas. Diseñado para agentes de código. ![92 ★](https://img.shields.io/badge/%E2%98%85-92-f5c518) ![last commit](https://img.shields.io/github/last-commit/amikai/openings-mcp)

### Scrapers de un solo portal

Los portales con defensas anti-bot agresivas (LinkedIn, Indeed, BOSS直聘…) se rompen a menudo: no construyas nada crítico sobre ellos sin reintentos, observabilidad por fuente y fallback a ATS/APIs.

- **[linkedin_scraper](https://github.com/joeyism/linkedin_scraper)** — Librería Python veterana para scrapear LinkedIn (perfiles, empresas y ofertas). Requiere sesión autenticada. ![4.546 ★](https://img.shields.io/badge/%E2%98%85-4.546-f5c518) ![last commit](https://img.shields.io/github/last-commit/joeyism/linkedin_scraper)
- **[linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server)** — Servidor MCP para LinkedIn: busca perfiles, empresas y ofertas desde cualquier agente de IA. ![3.629 ★](https://img.shields.io/badge/%E2%98%85-3.629-f5c518) ![last commit](https://img.shields.io/github/last-commit/stickerdaniel/linkedin-mcp-server)
- **[boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper)** — Scraper de BOSS直聘 (el portal dominante de China) vía CDP de Chrome reutilizando tu sesión real; evita el anti-bot de fuentes y exporta JSON/CSV con salario. ![1.472 ★](https://img.shields.io/badge/%E2%98%85-1.472-f5c518) ![last commit](https://img.shields.io/github/last-commit/eatmoreduck/boss-zhipin-scraper)
- **[py-linkedin-jobs-scraper](https://github.com/spinlud/py-linkedin-jobs-scraper)** — Scraper de ofertas de LinkedIn en Python con cola de trabajos y deduplicación; el más usado de su nicho. ![497 ★](https://img.shields.io/badge/%E2%98%85-497-f5c518) ![last commit](https://img.shields.io/github/last-commit/spinlud/py-linkedin-jobs-scraper)
- **[linkedin-jobs-scraper](https://github.com/spinlud/linkedin-jobs-scraper)** — Versión TypeScript del scraper de LinkedIn del mismo autor. ![188 ★](https://img.shields.io/badge/%E2%98%85-188-f5c518) ![last commit](https://img.shields.io/github/last-commit/spinlud/linkedin-jobs-scraper)
- **[linkedin-job-scraper](https://github.com/hendrixfreire/linkedin-job-scraper)** — Scraper de la API pública «Guest» de LinkedIn (sin login) con deduplicación y scoring heurístico. ![76 ★](https://img.shields.io/badge/%E2%98%85-76-f5c518) ![last commit](https://img.shields.io/github/last-commit/hendrixfreire/linkedin-job-scraper)
- **[UpworkScraper](https://github.com/roperi/UpworkScraper)** — Scraper de tus matches de Upwork (freelance) con Selenium y almacenamiento en SQLite. ![64 ★](https://img.shields.io/badge/%E2%98%85-64-f5c518) ![last commit](https://img.shields.io/github/last-commit/roperi/UpworkScraper)
- **[Linkedin-Jobs-Api](https://github.com/atharv01h/Linkedin-Jobs-Api)** — API no oficial en TypeScript para buscar ofertas de LinkedIn por keywords, ubicación y filtros. ![27 ★](https://img.shields.io/badge/%E2%98%85-27-f5c518) ![last commit](https://img.shields.io/github/last-commit/atharv01h/Linkedin-Jobs-Api)
- **[Apify-Upwork-Jobs-Scraper](https://github.com/orgupdate/Apify-Upwork-Jobs-Scraper)** — Actor de Apify para Upwork (suite orgupdate). ![19 ★](https://img.shields.io/badge/%E2%98%85-19-f5c518) ![last commit](https://img.shields.io/github/last-commit/orgupdate/Apify-Upwork-Jobs-Scraper)
- **[Apify-Linkedin-Jobs-Scraper](https://github.com/orgupdate/Apify-Linkedin-Jobs-Scraper)** — Actor de Apify para LinkedIn Jobs. orgupdate mantiene una suite de actores por portal con el mismo formato. ![17 ★](https://img.shields.io/badge/%E2%98%85-17-f5c518) ![last commit](https://img.shields.io/github/last-commit/orgupdate/Apify-Linkedin-Jobs-Scraper)
- **[Apify-Google-Jobs-Scraper](https://github.com/orgupdate/Apify-Google-Jobs-Scraper)** — Actor de Apify para Google Jobs (suite orgupdate). ![12 ★](https://img.shields.io/badge/%E2%98%85-12-f5c518) ![last commit](https://img.shields.io/github/last-commit/orgupdate/Apify-Google-Jobs-Scraper)
- **[Apify-Indeed-Jobs-Scraper](https://github.com/orgupdate/Apify-Indeed-Jobs-Scraper)** — Actor de Apify para Indeed (suite orgupdate). ![10 ★](https://img.shields.io/badge/%E2%98%85-10-f5c518) ![last commit](https://img.shields.io/github/last-commit/orgupdate/Apify-Indeed-Jobs-Scraper)
- **[Apify-Wellfound-Jobs-Scraper](https://github.com/orgupdate/Apify-Wellfound-Jobs-Scraper)** — Actor de Apify para Wellfound/AngelList (suite orgupdate). ![5 ★](https://img.shields.io/badge/%E2%98%85-5-f5c518) ![last commit](https://img.shields.io/github/last-commit/orgupdate/Apify-Wellfound-Jobs-Scraper)
- **[Apify-Glassdoor-Jobs-Scraper](https://github.com/orgupdate/Apify-Glassdoor-Jobs-Scraper)** — Actor de Apify para Glassdoor (suite orgupdate). ![4 ★](https://img.shields.io/badge/%E2%98%85-4-f5c518) ![last commit](https://img.shields.io/github/last-commit/orgupdate/Apify-Glassdoor-Jobs-Scraper)
- **[Apify-Welcome-To-The-Jungle-Jobs-Scraper](https://github.com/orgupdate/Apify-Welcome-To-The-Jungle-Jobs-Scraper)** — Actor de Apify para Welcome to the Jungle (suite orgupdate). ![4 ★](https://img.shields.io/badge/%E2%98%85-4-f5c518) ![last commit](https://img.shields.io/github/last-commit/orgupdate/Apify-Welcome-To-The-Jungle-Jobs-Scraper)
- **[Apify-Ziprecruiter-Jobs-Scraper](https://github.com/orgupdate/Apify-Ziprecruiter-Jobs-Scraper)** — Actor de Apify para ZipRecruiter (suite orgupdate). ![3 ★](https://img.shields.io/badge/%E2%98%85-3-f5c518) ![last commit](https://img.shields.io/github/last-commit/orgupdate/Apify-Ziprecruiter-Jobs-Scraper)

## 2. Conectores ATS y career pages

Probablemente la sección más importante de este listado: los ATS públicos (Greenhouse, Lever, Ashby, Workday…) exponen endpoints JSON estables, con mejor relación cobertura/estabilidad que scrapear portales centralizados.

### Librerías multi-ATS

- ⭐ **[ats-scrapers](https://github.com/kalil0321/ats-scrapers)** — Librería open-source unificada para leer los boards públicos de los principales ATS (Greenhouse, Lever, Ashby…). El punto de partida recomendado para monitorizar career pages sin tocar HTML. ![161 ★](https://img.shields.io/badge/%E2%98%85-161-f5c518) ![last commit](https://img.shields.io/github/last-commit/kalil0321/ats-scrapers)
- **[job-board-aggregator](https://github.com/Feashliaa/job-board-aggregator)** — Agregador multi-ATS ambicioso: declara indexar más de 1M de posiciones de 20.000+ empresas sobre Greenhouse, Lever, Ashby, BambooHR, iCIMS, Paylocity y Workday, con paralelismo por plataforma. ![158 ★](https://img.shields.io/badge/%E2%98%85-158-f5c518) ![last commit](https://img.shields.io/github/last-commit/Feashliaa/job-board-aggregator)
- **[job-board-scraper](https://github.com/adgramigna/job-board-scraper)** — Proyecto pequeño y didáctico (Python) para extraer vacantes de Greenhouse, Lever, Ashby y Rippling y normalizarlas. ![46 ★](https://img.shields.io/badge/%E2%98%85-46-f5c518) ![last commit](https://img.shields.io/github/last-commit/adgramigna/job-board-scraper)
- **[ashby-job-scraper](https://github.com/rishilahoti/ashby-job-scraper)** — Scraper (TypeScript) orientado a cientos de empresas sobre los tres ATS principales: Ashby, Lever y Greenhouse. ![41 ★](https://img.shields.io/badge/%E2%98%85-41-f5c518) ![last commit](https://img.shields.io/github/last-commit/rishilahoti/ashby-job-scraper)
- **[ats-jobs](https://github.com/shunsukefuruyama/ats-jobs)** — Lee ofertas de las APIs públicas oficiales de 12 ATS (Greenhouse, Workday, Ashby, Lever…). ![1 ★](https://img.shields.io/badge/%E2%98%85-1-f5c518) ![last commit](https://img.shields.io/github/last-commit/shunsukefuruyama/ats-jobs)
- **[JobHunter](https://github.com/Mister-Raggs/JobHunter)** — Scraper multi-ATS con abstracción unificada sobre Greenhouse, Ashby, Lever y la career page de Apple, con deduplicación en SQLite. ![0 ★](https://img.shields.io/badge/%E2%98%85-0-f5c518) ![last commit](https://img.shields.io/github/last-commit/Mister-Raggs/JobHunter)

### Vigilancia de career pages

- **[jobseek](https://github.com/colophon-group/jobseek)** — Monitoriza career pages de empresas y muestra las nuevas ofertas en un dashboard único (Greenhouse y otros ATS). ![200 ★](https://img.shields.io/badge/%E2%98%85-200-f5c518) ![last commit](https://img.shields.io/github/last-commit/colophon-group/jobseek)
- **[searchsteward](https://github.com/SearchSteward/searchsteward)** — Radar que vigila más de 40.000 career pages y puntúa cada apertura contra tu currículum; detecta también ghost jobs. ![18 ★](https://img.shields.io/badge/%E2%98%85-18-f5c518) ![last commit](https://img.shields.io/github/last-commit/SearchSteward/searchsteward)
- **[Scrapers_Cristi_Olteanu](https://github.com/peviitor-ro/Scrapers_Cristi_Olteanu)** — Más de 100 scripts de scraping ejecutándose a diario en GitHub Actions para el marketplace público de empleo de Rumanía (peviitor.ro). Ejemplo de operación comunitaria con CI. ![11 ★](https://img.shields.io/badge/%E2%98%85-11-f5c518) ![last commit](https://img.shields.io/github/last-commit/peviitor-ro/Scrapers_Cristi_Olteanu)
- **[openhire](https://github.com/gzchenhao/openhire)** — Ofertas con la fecha real de publicación (que los boards suelen ocultar) de Greenhouse, Lever, Ashby, Beisen y Moka. ![7 ★](https://img.shields.io/badge/%E2%98%85-7-f5c518) ![last commit](https://img.shields.io/github/last-commit/gzchenhao/openhire)
- **[ghostbusters-api](https://github.com/balboaid/ghostbusters-api)** — Detecta ofertas fantasma (ghost jobs) antes de que pierdas el tiempo, analizando boards de Greenhouse y Gupy. ![6 ★](https://img.shields.io/badge/%E2%98%85-6-f5c518) ![last commit](https://img.shields.io/github/last-commit/balboaid/ghostbusters-api)
- **[jobwatch-oss](https://github.com/Folabomi/jobwatch-oss)** — Consulta los endpoints JSON de boards de empresas y calcula diffs: Greenhouse, Ashby, Eightfold, Workday… ![3 ★](https://img.shields.io/badge/%E2%98%85-3-f5c518) ![last commit](https://img.shields.io/github/last-commit/Folabomi/jobwatch-oss)

### ATS concretos

- **[workday-scraper](https://github.com/christopherlam888/workday-scraper)** — Scraper Python para las career pages de Workday, el ATS con formatos más variables. ![17 ★](https://img.shields.io/badge/%E2%98%85-17-f5c518) ![last commit](https://img.shields.io/github/last-commit/christopherlam888/workday-scraper)
- **[gatsby-source-greenhouse-job-board](https://github.com/kevinbarnett/gatsby-source-greenhouse-job-board)** — Plugin de Gatsby que trae oficinas, departamentos y ofertas desde la API de Greenhouse. ![5 ★](https://img.shields.io/badge/%E2%98%85-5-f5c518) ![last commit](https://img.shields.io/github/last-commit/kevinbarnett/gatsby-source-greenhouse-job-board)
- **[Apify-Workday-Job-Scraper](https://github.com/orgupdate/Apify-Workday-Job-Scraper)** — Actor de Apify para boards de Workday (suite orgupdate). ![4 ★](https://img.shields.io/badge/%E2%98%85-4-f5c518) ![last commit](https://img.shields.io/github/last-commit/orgupdate/Apify-Workday-Job-Scraper)
- **[personio-jobs](https://github.com/CPS-IT/personio-jobs)** — Extensión TYPO3 (PHP) que integra ofertas de la API de reclutamiento de Personio. ![4 ★](https://img.shields.io/badge/%E2%98%85-4-f5c518) ![last commit](https://img.shields.io/github/last-commit/CPS-IT/personio-jobs)
- **[ashby-job-scraper](https://github.com/d-alleyne/ashby-job-scraper)** — Actor de Apify para boards de Ashby, con esquema normalizado. ![4 ★](https://img.shields.io/badge/%E2%98%85-4-f5c518) ![last commit](https://img.shields.io/github/last-commit/d-alleyne/ashby-job-scraper)
- **[Apify-Workable-Job-Scraper](https://github.com/orgupdate/Apify-Workable-Job-Scraper)** — Actor de Apify para Workable (suite orgupdate). ![3 ★](https://img.shields.io/badge/%E2%98%85-3-f5c518) ![last commit](https://img.shields.io/github/last-commit/orgupdate/Apify-Workable-Job-Scraper)
- **[ekswai-jobs-scraper](https://github.com/danielebarbaro/ekswai-jobs-scraper)** — Sigue ofertas en varios boards (Greenhouse, Ashby, Factorial…) con dashboard y avisos por email; incluye el feed XML de Personio. ![3 ★](https://img.shields.io/badge/%E2%98%85-3-f5c518) ![last commit](https://img.shields.io/github/last-commit/danielebarbaro/ekswai-jobs-scraper)
- **[avature-ats-scraper](https://github.com/ivanlalvarez22/avature-ats-scraper)** — Scraper para Avature, un ATS empresarial poco cubierto por el resto de herramientas. ![1 ★](https://img.shields.io/badge/%E2%98%85-1-f5c518) ![last commit](https://img.shields.io/github/last-commit/ivanlalvarez22/avature-ats-scraper)
- **[job-boards-personio](https://github.com/plin-code/job-boards-personio)** — Cliente PHP (PSR-18) para el feed XML del job board de Personio; funciona en Laravel y Symfony. ![0 ★](https://img.shields.io/badge/%E2%98%85-0-f5c518) ![last commit](https://img.shields.io/github/last-commit/plin-code/job-boards-personio)
- **[job-boards-bamboohr](https://github.com/plin-code/job-boards-bamboohr)** — Cliente PHP (PSR-18) para el job board de BambooHR. ![0 ★](https://img.shields.io/badge/%E2%98%85-0-f5c518) ![last commit](https://img.shields.io/github/last-commit/plin-code/job-boards-bamboohr)
- **[greenhouse-job-scraper](https://github.com/d-alleyne/greenhouse-job-scraper)** — Actor de Apify para Greenhouse: extrae desde el endpoint del board, filtra por departamento y evita navegador y parseo HTML. ![0 ★](https://img.shields.io/badge/%E2%98%85-0-f5c518) ![last commit](https://img.shields.io/github/last-commit/d-alleyne/greenhouse-job-scraper)
- **[lever-job-scraper](https://github.com/d-alleyne/lever-job-scraper)** — Actor de Apify para boards de Lever vía su API JSON, con filtrado por equipo. ![0 ★](https://img.shields.io/badge/%E2%98%85-0-f5c518) ![last commit](https://img.shields.io/github/last-commit/d-alleyne/lever-job-scraper)

### Referencias de endpoints y directorios

- **[Companies-Directory](https://github.com/Clothless/Companies-Directory)** — Directorio de empresas con sus webs y páginas de careers: la lista de objetivos para cualquier monitor de ATS. ![68 ★](https://img.shields.io/badge/%E2%98%85-68-f5c518) ![last commit](https://img.shields.io/github/last-commit/Clothless/Companies-Directory)
- **[hrflow-connectors](https://github.com/Riminder/hrflow-connectors)** — Colección de conectores Python para fuentes de datos de RRHH y boards de empleo (CareerBuilder, Cegid, Ceridian…). ![41 ★](https://img.shields.io/badge/%E2%98%85-41-f5c518) ![last commit](https://img.shields.io/github/last-commit/Riminder/hrflow-connectors)
- **[ats-job-apis](https://github.com/noble-ronin/ats-job-apis)** — Directorio de endpoints JSON/XML públicos de boards ATS: Greenhouse, Lever, Ashby, Workday, SmartRecruiters, BambooHR… ![4 ★](https://img.shields.io/badge/%E2%98%85-4-f5c518) ![last commit](https://img.shields.io/github/last-commit/noble-ronin/ats-job-apis)
- **[ats-boards](https://github.com/msertdev/ats-boards)** — Descubre y lee los boards públicos de los ATS más usados por empresas alemanas (Personio, SmartRecruiters…). ![1 ★](https://img.shields.io/badge/%E2%98%85-1-f5c518) ![last commit](https://img.shields.io/github/last-commit/msertdev/ats-boards)
- **[ats-api-reference](https://github.com/ConorsCode/ats-api-reference)** — Referencia verificada y multiplataforma de las APIs públicas de nueve ATS. Documentación imprescindible antes de escribir tu propio conector. ![0 ★](https://img.shields.io/badge/%E2%98%85-0-f5c518) ![last commit](https://img.shields.io/github/last-commit/ConorsCode/ats-api-reference)

## 3. APIs y feeds públicos

Distingue expresamente «scraping» de «API/feed público»: si existe un feed documentado y estable, debe ser siempre la primera opción. Remote OK, Arbeitnow, Remotive, Adzuna, USAJOBS o Jooble publican APIs sin repo canónico — los clientes y servidores MCP de abajo son su puerta de entrada, y las URLs de cada API están en la web de cada fuente.

### APIs y clientes

- ⭐ **[remote-jobs-api](https://github.com/Jobicy/remote-jobs-api)** — API pública, feeds RSS y widgets oficiales de Jobicy para empleo remoto, sin clave. La vía preferible cuando el portal expone feed documentado: usa la API antes de scrapear. ![8 ★](https://img.shields.io/badge/%E2%98%85-8-f5c518) ![last commit](https://img.shields.io/github/last-commit/Jobicy/remote-jobs-api)
- ⭐ **[remote-jobs-api](https://github.com/Himalayas-App/remote-jobs-api)** — API JSON pública y gratuita de Himalayas (95.000+ ofertas remotas, sin autenticación); el mismo proyecto publica feed RSS y servidor MCP. ![2 ★](https://img.shields.io/badge/%E2%98%85-2-f5c518) ![last commit](https://img.shields.io/github/last-commit/Himalayas-App/remote-jobs-api)
- **[himalayas-mcp](https://github.com/Himalayas-App/himalayas-mcp)** — Servidor MCP oficial de Himalayas: busca 100.000+ ofertas remotas y consulta salarios. ![21 ★](https://img.shields.io/badge/%E2%98%85-21-f5c518) ![last commit](https://img.shields.io/github/last-commit/Himalayas-App/himalayas-mcp)
- **[adzuna-job-search-mcp](https://github.com/folathecoder/adzuna-job-search-mcp)** — Servidor MCP para la API de Adzuna: búsqueda, salarios y empresas en 12 países. ![15 ★](https://img.shields.io/badge/%E2%98%85-15-f5c518) ![last commit](https://img.shields.io/github/last-commit/folathecoder/adzuna-job-search-mcp)
- **[federal-compass-mcp](https://github.com/skivuha/federal-compass-mcp)** — Servidor MCP sobre la API oficial de USAJOBS (empleo público de EE. UU.). ![12 ★](https://img.shields.io/badge/%E2%98%85-12-f5c518) ![last commit](https://img.shields.io/github/last-commit/skivuha/federal-compass-mcp)
- **[remote-jobs-mcp-server](https://github.com/Jobicy/remote-jobs-mcp-server)** — Servidor MCP oficial de Jobicy para buscar ofertas remotas desde agentes de IA. ![2 ★](https://img.shields.io/badge/%E2%98%85-2-f5c518) ![last commit](https://img.shields.io/github/last-commit/Jobicy/remote-jobs-mcp-server)
- **[remote-ok-jobs](https://github.com/go-api-libs/remote-ok-jobs)** — Cliente Go para el feed `/api` de Remote OK. Remote OK no tiene repo oficial; los clientes como este son su puerta de entrada. ![1 ★](https://img.shields.io/badge/%E2%98%85-1-f5c518) ![last commit](https://img.shields.io/github/last-commit/go-api-libs/remote-ok-jobs)
- **[jobs-mcp](https://github.com/0xCybin/jobs-mcp)** — Servidor MCP multi-fuente: RemoteOK, Hacker News (Who's Hiring), Arbeitnow y GitHub Jobs posts. ![1 ★](https://img.shields.io/badge/%E2%98%85-1-f5c518) ![last commit](https://img.shields.io/github/last-commit/0xCybin/jobs-mcp)
- **[usajobs](https://github.com/api-evangelist/usajobs)** — Perfil independiente de la superficie de la API de USAJOBS, mantenido por API Evangelist. Útil como documentación de terceros. ![1 ★](https://img.shields.io/badge/%E2%98%85-1-f5c518) ![last commit](https://img.shields.io/github/last-commit/api-evangelist/usajobs)
- **[jobicy](https://github.com/go-api-libs/jobicy)** — Cliente Go para la API y el feed RSS de Jobicy. ![0 ★](https://img.shields.io/badge/%E2%98%85-0-f5c518) ![last commit](https://img.shields.io/github/last-commit/go-api-libs/jobicy)
- **[adzuna-job-scraper](https://github.com/shriram264/adzuna-job-scraper)** — CLI Python que consulta la API de Adzuna (con credenciales gratuitas, 12 países) y exporta CSV. Buen ejemplo de enfoque API-first. ![0 ★](https://img.shields.io/badge/%E2%98%85-0-f5c518) ![last commit](https://img.shields.io/github/last-commit/shriram264/adzuna-job-scraper)

## 4. Plataformas self-hosted end-to-end

Aplicaciones completas que integran descubrimiento, scraping, scoring y seguimiento de candidaturas. Autonómicas, pesadas y muy útiles.

### Plataformas

- ⭐ **[career-ops](https://github.com/career-ops-hq/career-ops)** — La plataforma de referencia del ecosistema (open-source): escanea portales y career pages, evalúa cada oferta en un informe estructurado A-H con scoring global y genera los materiales de aplicación. Diseñada para operar con agentes de IA. ![72.843 ★](https://img.shields.io/badge/%E2%98%85-72.843-f5c518) ![last commit](https://img.shields.io/github/last-commit/career-ops-hq/career-ops)
- ⭐ **[JobNavigator](https://github.com/vesaias/JobNavigator)** — Solución end-to-end autohospedada: descubrimiento, scraping de ATS (11 plataformas), Playwright, scoring con IA contra tus CVs, alertas y seguimiento de candidaturas. ![129 ★](https://img.shields.io/badge/%E2%98%85-129-f5c518) ![last commit](https://img.shields.io/github/last-commit/vesaias/JobNavigator)
- **[job-ops](https://github.com/DaKheera47/job-ops)** — Aplica principios DevOps a la búsqueda de empleo: pipeline autohospedado para rastrear, analizar y asistir tus candidaturas. ![3.976 ★](https://img.shields.io/badge/%E2%98%85-3.976-f5c518) ![last commit](https://img.shields.io/github/last-commit/DaKheera47/job-ops)
- **[Auto_job_applier_linkedIn](https://github.com/GodsScion/Auto_job_applier_linkedIn)** — El clásico auto-aplicador de LinkedIn (Selenium): configura criterios y aplica en Easy Apply de forma automática. ![2.871 ★](https://img.shields.io/badge/%E2%98%85-2.871-f5c518) ![last commit](https://img.shields.io/github/last-commit/GodsScion/Auto_job_applier_linkedIn)
- **[jobsync](https://github.com/Gsync/jobsync)** — Tracker de candidaturas con asistente de búsqueda potenciado por IA: gestiona el ciclo completo desde el descubrimiento. ![1.316 ★](https://img.shields.io/badge/%E2%98%85-1.316-f5c518) ![last commit](https://img.shields.io/github/last-commit/Gsync/jobsync)
- **[pinloop-cli](https://github.com/pinloop-ai/pinloop-cli)** — CLI de job boards pensada para agentes de código: busca y puntúa millones de ofertas desde el terminal. ![510 ★](https://img.shields.io/badge/%E2%98%85-510-f5c518) ![last commit](https://img.shields.io/github/last-commit/pinloop-ai/pinloop-cli)
- **[job_finder](https://github.com/ATAboukhadra/job_finder)** — Arquitectura limpia por adaptadores (Remotive, Arbeitnow, Himalayas, Adzuna, JSearch) con LLM local vía Ollama para matching y generación de documentos. ![93 ★](https://img.shields.io/badge/%E2%98%85-93-f5c518) ![last commit](https://img.shields.io/github/last-commit/ATAboukhadra/job_finder)
- **[JobHuntBot](https://github.com/DanielPan12/JobHuntBot)** — Flujo de aplicación dirigido por agente con dashboard local de progreso; compatible con cualquier agente de código. ![837 ★](https://img.shields.io/badge/%E2%98%85-837-f5c518) ![last commit](https://img.shields.io/github/last-commit/DanielPan12/JobHuntBot)
- **[EasyApplyJobsBot](https://github.com/wodsuz/EasyApplyJobsBot)** — Bot Python para aplicar automáticamente a ofertas Easy Apply de LinkedIn y Glassdoor según tus preferencias. ![825 ★](https://img.shields.io/badge/%E2%98%85-825-f5c518) ![last commit](https://img.shields.io/github/last-commit/wodsuz/EasyApplyJobsBot)
- **[offerPilot](https://github.com/offercontext/offerPilot)** — Espacio de trabajo local-first para la búsqueda de empleo con IA: CVs, práctica, entrevistas simuladas y comparación de ofertas (en chino). ![734 ★](https://img.shields.io/badge/%E2%98%85-734-f5c518) ![last commit](https://img.shields.io/github/last-commit/offercontext/offerPilot)
- **[job-auto-apply](https://github.com/Anshul439/job-auto-apply)** — Automatiza solicitudes one-click en Wellfound e Instahyre. ![268 ★](https://img.shields.io/badge/%E2%98%85-268-f5c518) ![last commit](https://img.shields.io/github/last-commit/Anshul439/job-auto-apply)
- **[jobseeker-analytics](https://github.com/JustAJobApp/jobseeker-analytics)** — Conecta tu bandeja de Gmail y convierte el caos de la búsqueda en analítica automática de candidaturas. ![202 ★](https://img.shields.io/badge/%E2%98%85-202-f5c518) ![last commit](https://img.shields.io/github/last-commit/JustAJobApp/jobseeker-analytics)
- **[Job-apply-AI-agent](https://github.com/imon333/Job-apply-AI-agent)** — Automatización completa: búsqueda, creación de CV y aplicación automática con IA. ![186 ★](https://img.shields.io/badge/%E2%98%85-186-f5c518) ![last commit](https://img.shields.io/github/last-commit/imon333/Job-apply-AI-agent)
- **[JobFinderOS](https://github.com/matthewprice/JobFinderOS)** — Búsqueda de empleo agéntica sobre Claude Code: reclutador, crawler y analista de mercado escribiendo en Obsidian. ![170 ★](https://img.shields.io/badge/%E2%98%85-170-f5c518) ![last commit](https://img.shields.io/github/last-commit/matthewprice/JobFinderOS)
- **[swiss-job-hunter](https://github.com/Donvink/swiss-job-hunter)** — Pipeline automatizado para Suiza: 7 boards, deduplicación y scoring contra tu CV. ![145 ★](https://img.shields.io/badge/%E2%98%85-145-f5c518) ![last commit](https://img.shields.io/github/last-commit/Donvink/swiss-job-hunter)
- **[geezap](https://github.com/theihasan/geezap)** — Plataforma de agregación con IA construida en Laravel que unifica LinkedIn, Upwork y más. ![131 ★](https://img.shields.io/badge/%E2%98%85-131-f5c518) ![last commit](https://img.shields.io/github/last-commit/theihasan/geezap)
- **[job_search_tool](https://github.com/fedorchenko-juli/job_search_tool)** — Pipeline que obtiene ofertas de APIs de ATS y agregadores, filtra, deduplica y prioriza. ![122 ★](https://img.shields.io/badge/%E2%98%85-122-f5c518) ![last commit](https://img.shields.io/github/last-commit/fedorchenko-juli/job_search_tool)
- **[Argus](https://github.com/mshen1019/Argus)** — Agente de IA que rastrea career pages y te empareja ofertas según tus preferencias. ![114 ★](https://img.shields.io/badge/%E2%98%85-114-f5c518) ![last commit](https://img.shields.io/github/last-commit/mshen1019/Argus)
- **[swissdevjobs-cli](https://github.com/Stupidoodle/swissdevjobs-cli)** — Busca y aplica a ~4.700 ofertas tech con salario transparente en 7 países desde el terminal. ![101 ★](https://img.shields.io/badge/%E2%98%85-101-f5c518) ![last commit](https://img.shields.io/github/last-commit/Stupidoodle/swissdevjobs-cli)
- **[hunter](https://github.com/pedrohlucena/hunter)** — Agente de IA que busca ofertas según tu perfil y exporta resultados puntuados como CSV. ![92 ★](https://img.shields.io/badge/%E2%98%85-92-f5c518) ![last commit](https://img.shields.io/github/last-commit/pedrohlucena/hunter)
- **[JobCtrl](https://github.com/ebarti/JobCtrl)** — App local-first de búsqueda con scoring de encaje basado en evidencia y ajuste de CV trazable. ![82 ★](https://img.shields.io/badge/%E2%98%85-82-f5c518) ![last commit](https://img.shields.io/github/last-commit/ebarti/JobCtrl)
- **[jobpilot](https://github.com/suxrobGM/jobpilot)** — Agente que aplica por ti: busca en boards, adapta el CV, rellena solicitudes y envía mensajes. ![79 ★](https://img.shields.io/badge/%E2%98%85-79-f5c518) ![last commit](https://img.shields.io/github/last-commit/suxrobGM/jobpilot)
- **[career-ops-ui](https://github.com/Fighter90/career-ops-ui)** — UI estilo documentación para ejecutar escaneos unificados de ATS (Greenhouse, Ashby, Lever, Workable…) y fuentes regionales como hh.ru. ![75 ★](https://img.shields.io/badge/%E2%98%85-75-f5c518) ![last commit](https://img.shields.io/github/last-commit/Fighter90/career-ops-ui)
- **[hh.ru-clicker](https://github.com/Vlad9572324/hh.ru-clicker)** — Script de auto-respuesta para hh.ru, el portal dominante en Rusia y CEI. ![62 ★](https://img.shields.io/badge/%E2%98%85-62-f5c518) ![last commit](https://img.shields.io/github/last-commit/Vlad9572324/hh.ru-clicker)
- **[job-seeker](https://github.com/galiprandi/job-seeker)** — Skills, guías y scripts para que tu agente de código (Devin, Claude…) dirija la búsqueda de empleo. ![29 ★](https://img.shields.io/badge/%E2%98%85-29-f5c518) ![last commit](https://img.shields.io/github/last-commit/galiprandi/job-seeker)
- **[JobSentinel](https://github.com/cboyd0319/JobSentinel)** — Búsqueda autohospedada: scrapea varios boards, deduplica, puntúa según tus preferencias y avisa — privado, desplegable en AWS/Azure. ![27 ★](https://img.shields.io/badge/%E2%98%85-27-f5c518) ![last commit](https://img.shields.io/github/last-commit/cboyd0319/JobSentinel)
- **[yc-auto-apply](https://github.com/IndraJeet-09/yc-auto-apply)** — Bot para «Work at a Startup» de Y Combinator: scrapea ofertas remote de engineering y rellena formularios con tu perfil. ![22 ★](https://img.shields.io/badge/%E2%98%85-22-f5c518) ![last commit](https://img.shields.io/github/last-commit/IndraJeet-09/yc-auto-apply)
- **[CareerPulse](https://github.com/tcpsyn/CareerPulse)** — Plataforma de descubrimiento y evaluación de vacantes contra tu CV: 14 job boards con scoring por IA. ![20 ★](https://img.shields.io/badge/%E2%98%85-20-f5c518) ![last commit](https://img.shields.io/github/last-commit/tcpsyn/CareerPulse)
- **[HiringCafe-Scraper](https://github.com/CJ7862/HiringCafe-Scraper)** — Wrapper con CLI, API y Docker sobre hiring.cafe (datos de career pages) con validación de calidad; dependiente de una fuente externa — valida estabilidad antes de apostar a él. ![1 ★](https://img.shields.io/badge/%E2%98%85-1-f5c518) ![last commit](https://img.shields.io/github/last-commit/CJ7862/HiringCafe-Scraper)

## 5. Infra anti-bot y scraping general

La infraestructura transversal que hace viable scrapear en 2026: frameworks, fingerprinting TLS, navegadores indetectables y bypass de Cloudflare.

### Frameworks de scraping

- ⭐ **[scrapy](https://github.com/scrapy/scrapy)** — El framework de crawling y scraping de referencia en Python: spiders, pipelines, middlewares y ecosistema enorme. La base sobre la que construir ingestas serias de ofertas. ![64.487 ★](https://img.shields.io/badge/%E2%98%85-64.487-f5c518) ![last commit](https://img.shields.io/github/last-commit/scrapy/scrapy)
- ⭐ **[crawlee](https://github.com/apify/crawlee)** — Librería de scraping y automatización de navegador para Node.js (Playwright/Puppeteer bajo el capó) con colas, reintentos y proxies integrados. ![25.902 ★](https://img.shields.io/badge/%E2%98%85-25.902-f5c518) ![last commit](https://img.shields.io/github/last-commit/apify/crawlee)
- **[Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai)** — Framework de scraping agéntico: grafos LLM que extraen datos estructurados de webs y docs locales. ![31.314 ★](https://img.shields.io/badge/%E2%98%85-31.314-f5c518) ![last commit](https://img.shields.io/github/last-commit/ScrapeGraphAI/Scrapegraph-ai)

### Fingerprinting TLS / HTTP

- ⭐ **[curl_cffi](https://github.com/lexiforest/curl_cffi)** — Binding Python de curl-impersonate: peticiones HTTP con fingerprint TLS/JA3 de navegadores reales. La herramienta estándar para saltarse bloqueos TLS sin navegador; sucesor activo de curl-impersonate. ![6.563 ★](https://img.shields.io/badge/%E2%98%85-6.563-f5c518) ![last commit](https://img.shields.io/github/last-commit/lexiforest/curl_cffi)
- **[tls-client](https://github.com/bogdanfinn/tls-client)** — Cliente HTTP en Go (con bindings) que permite seleccionar fingerprints TLS específicos; el equivalente de referencia en el mundo Go. ![1.859 ★](https://img.shields.io/badge/%E2%98%85-1.859-f5c518) ![last commit](https://img.shields.io/github/last-commit/bogdanfinn/tls-client)

### Navegadores undetected

- ⭐ **[camoufox](https://github.com/daijro/camoufox)** — Navegador anti-detección basado en Firefox con fingerprinting rotatorio y sin fugas de WebRTC. Cuando Playwright/Selenium puro queda bloqueado. ![12.143 ★](https://img.shields.io/badge/%E2%98%85-12.143-f5c518) ![last commit](https://img.shields.io/github/last-commit/daijro/camoufox)
- **[botasaurus](https://github.com/omkarcloud/botasaurus)** — Framework todo-en-uno (Python) para construir scrapers que sortean anti-bots: navegación, Google caching, scraping masivo y tasks. ![5.725 ★](https://img.shields.io/badge/%E2%98%85-5.725-f5c518) ![last commit](https://img.shields.io/github/last-commit/omkarcloud/botasaurus)
- **[nodriver](https://github.com/ultrafunkamsterdam/nodriver)** — Sucesor de undetected-chromedriver: automatización de Chrome sin los flags que delatan a Selenium. ![4.781 ★](https://img.shields.io/badge/%E2%98%85-4.781-f5c518) ![last commit](https://img.shields.io/github/last-commit/ultrafunkamsterdam/nodriver)
- **[zendriver](https://github.com/cdpdriver/zendriver)** — Fork async-first y mantenido de nodriver, centrado en scraping indetectable. ![1.443 ★](https://img.shields.io/badge/%E2%98%85-1.443-f5c518) ![last commit](https://img.shields.io/github/last-commit/cdpdriver/zendriver)

### Bypass de Cloudflare y proxies

- ⭐ **[FlareSolverr](https://github.com/FlareSolverr/FlareSolverr)** — Servidor proxy que resuelve el desafío de Cloudflare y devuelve las cookies listas para usar; el estándar para autohospedar el bypass. ![15.678 ★](https://img.shields.io/badge/%E2%98%85-15.678-f5c518) ![last commit](https://img.shields.io/github/last-commit/FlareSolverr/FlareSolverr)
- **[PROXY-List](https://github.com/TheSpeedX/PROXY-List)** — Listas de proxies públicas actualizadas a diario (HTTP, SOCKS4, SOCKS5). ![5.828 ★](https://img.shields.io/badge/%E2%98%85-5.828-f5c518) ![last commit](https://img.shields.io/github/last-commit/TheSpeedX/PROXY-List)
- **[proxy-list](https://github.com/monosans/proxy-list)** — Listas de proxies HTTP/SOCKS4/SOCKS5 re-verificadas cada hora, en texto plano y JSON. ![1.519 ★](https://img.shields.io/badge/%E2%98%85-1.519-f5c518) ![last commit](https://img.shields.io/github/last-commit/monosans/proxy-list)

## 6. Datasets y listas vigiladas

Datos ya extraídos y publicados (algunos con licencia abierta) y listas vigiladas que se actualizan solas. Antes de montar tu propio pipeline, comprueba si alguien ya publica lo que necesitas.

### Datasets y trackers

- ⭐ **[open-jobs](https://github.com/elliottdehn/open-jobs)** — ~3M de ofertas activas de 36 ATS con campos enriquecidos por LLM y embeddings, liberadas CC0 e incluyendo tooling para agentes. El dataset abierto más grande del nicho. ![358 ★](https://img.shields.io/badge/%E2%98%85-358-f5c518) ![last commit](https://img.shields.io/github/last-commit/elliottdehn/open-jobs)
- **[Automated-List-Of-Summer-2027-and-Fall-2026-Tech-Internships](https://github.com/zshah101/Automated-List-Of-Summer-2027-and-Fall-2026-Tech-Internships)** — Tracker mantenido de prácticas y puestos CS: 180 prácticas abiertas extraídas de 4.300 boards de empresas. ![858 ★](https://img.shields.io/badge/%E2%98%85-858-f5c518) ![last commit](https://img.shields.io/github/last-commit/zshah101/Automated-List-Of-Summer-2027-and-Fall-2026-Tech-Internships)
- **[job_postings_tracker](https://github.com/hiring-lab/job_postings_tracker)** — El tracker oficial de Hiring Lab (Indeed): serie de variación de ofertas publicadas desde 2020. Dato macro de referencia del mercado. ![216 ★](https://img.shields.io/badge/%E2%98%85-216-f5c518) ![last commit](https://img.shields.io/github/last-commit/hiring-lab/job_postings_tracker)
- **[ai-jobs-net-salaries](https://github.com/foorilla/ai-jobs-net-salaries)** — Dataset de salarios globales en IA/ML y Big Data (de aijobs.net). ![28 ★](https://img.shields.io/badge/%E2%98%85-28-f5c518) ![last commit](https://img.shields.io/github/last-commit/foorilla/ai-jobs-net-salaries)
- **[infosec-jobs-com-salaries](https://github.com/foorilla/infosec-jobs-com-salaries)** — Dataset de salarios globales en ciberseguridad (de infosec-jobs.com). ![21 ★](https://img.shields.io/badge/%E2%98%85-21-f5c518) ![last commit](https://img.shields.io/github/last-commit/foorilla/infosec-jobs-com-salaries)
- **[usajobs_historical](https://github.com/abigailhaddad/usajobs_historical)** — Datos históricos del API de USAJOBS para análisis del empleo público estadounidense. ![18 ★](https://img.shields.io/badge/%E2%98%85-18-f5c518) ![last commit](https://img.shields.io/github/last-commit/abigailhaddad/usajobs_historical)
- **[Open-Tech-Internships-2027](https://github.com/dreamworkhq/Open-Tech-Internships-2027)** — Prácticas tech en EE. UU. verificadas como abiertas y enlazadas directamente a la career page de cada empresa, actualizadas a diario. ![6 ★](https://img.shields.io/badge/%E2%98%85-6-f5c518) ![last commit](https://img.shields.io/github/last-commit/dreamworkhq/Open-Tech-Internships-2027)
- **[linkedin-jobs-scraper](https://github.com/ryq99/linkedin-jobs-scraper)** — Scraper diario de ofertas LinkedIn para roles DS/ML (Playwright + SQLite) que publica un dataset abierto creciente. ![5 ★](https://img.shields.io/badge/%E2%98%85-5-f5c518) ![last commit](https://img.shields.io/github/last-commit/ryq99/linkedin-jobs-scraper)
- **[most-in-demand-skills-2026](https://github.com/dreamjobs-tech/most-in-demand-skills-2026)** — Demanda de habilidades extraída de 360.000+ ofertas (dic 2025–jun 2026), licencia CC BY 4.0. ![2 ★](https://img.shields.io/badge/%E2%98%85-2-f5c518) ![last commit](https://img.shields.io/github/last-commit/dreamjobs-tech/most-in-demand-skills-2026)
- **[ai-jobs-dataset-2026](https://github.com/M0saeed/ai-jobs-dataset-2026)** — Pipeline end-to-end sobre 50.000+ ofertas de IA: scraping, limpieza, EDA y visualización. ![2 ★](https://img.shields.io/badge/%E2%98%85-2-f5c518) ![last commit](https://img.shields.io/github/last-commit/M0saeed/ai-jobs-dataset-2026)

## 7. Tutoriales y guías

Material de aprendizaje y meta-listados. Se marca cuando una guía es contenido de un vendor comercial.

### Guías

- ⭐ **[awesome-web-scraping](https://github.com/lorien/awesome-web-scraping)** — La awesome-list madre de web scraping: librerías, herramientas y APIs por lenguaje. Tu siguiente parada cuando este listado se queda corto en lo genérico. ![8.161 ★](https://img.shields.io/badge/%E2%98%85-8.161-f5c518) ![last commit](https://img.shields.io/github/last-commit/lorien/awesome-web-scraping)
- **[job-data-apis-and-scrapers](https://github.com/cporter202/job-data-apis-and-scrapers)** — Directorio curado específico de APIs y scrapers de datos de empleo: ofertas, señales de contratación, salarios y recruiting. ![81 ★](https://img.shields.io/badge/%E2%98%85-81-f5c518) ![last commit](https://img.shields.io/github/last-commit/cporter202/job-data-apis-and-scrapers)
- **[how-to-scrape-google-jobs](https://github.com/oxylabs/how-to-scrape-google-jobs)** — Guía del vendor Oxylabs para construir un scraper de Google Jobs multi-query (promociona su API comercial, pero el tutorial es completo). ![1.769 ★](https://img.shields.io/badge/%E2%98%85-1.769-f5c518) ![last commit](https://img.shields.io/github/last-commit/oxylabs/how-to-scrape-google-jobs)
- **[awesome-ai-web-scraping](https://github.com/h4ckf0r0day/awesome-ai-web-scraping)** — Lista de herramientas de scraping con IA, crawlers LLM-friendly y servidores MCP. ![106 ★](https://img.shields.io/badge/%E2%98%85-106-f5c518) ![last commit](https://img.shields.io/github/last-commit/h4ckf0r0day/awesome-ai-web-scraping)
- **[best-web-scrapers](https://github.com/ScrapingBee/best-web-scrapers)** — Guía comparativa de herramientas de scraping (contenido de vendor de ScrapingBee). ![27 ★](https://img.shields.io/badge/%E2%98%85-27-f5c518) ![last commit](https://img.shields.io/github/last-commit/ScrapingBee/best-web-scrapers)

## 8. Archivo

Recursos que dejaron de cumplirse los criterios de mantenimiento. Se conservan por valor histórico o documental, con el motivo de su baja.

- **[jobspy-api](https://github.com/rainmanjam/jobspy-api)** — 🪦 Archivado 2026-09: sin commits desde 2025-05 (16 meses). Empaquetado Docker/FastAPI de JobSpy con API key y rate limiting; aún útil como referencia de despliegue self-hosted. Último estado: 379 ⭐, último commit 2025-05-29. ![last commit](https://img.shields.io/github/last-commit/rainmanjam/jobspy-api)
- **[curl-impersonate](https://github.com/lwthiker/curl-impersonate)** — 🪦 Archivado 2026-09: sin commits desde 2024-07 (26 meses). El original del fingerprinting TLS de curl; su sucesor activo es lexiforest/curl_cffi. Último estado: 7.049 ⭐, último commit 2024-07-18. ![last commit](https://img.shields.io/github/last-commit/lwthiker/curl-impersonate)
- **[puppeteer-extra](https://github.com/berstend/puppeteer-extra)** — 🪦 Archivado 2026-09: sin commits desde 2024-07 (26 meses). El ecosistema de plugins de Puppeteer (incl. stealth). Sigue funcionando pero sin mantenimiento activo. Último estado: 7.402 ⭐, último commit 2024-07-18. ![last commit](https://img.shields.io/github/last-commit/berstend/puppeteer-extra)
- **[hrequests](https://github.com/daijro/hrequests)** — 🪦 Archivado 2026-09: sin commits desde 2024-12 (22 meses). Cliente HTTP con fingerprint de navegador del autor de camoufox, que ha movido ahí su esfuerzo. Último estado: 1.023 ⭐, último commit 2024-12-01. ![last commit](https://img.shields.io/github/last-commit/daijro/hrequests)

## Contribuir

Este repositorio acepta sugerencias **solo vía issues** (ver [CONTRIBUTING.md](CONTRIBUTING.md)): propón recursos con la plantilla «Sugerir recurso». El CI semestral es el único que abre PRs.

## Licencia

[MIT](LICENSE)
