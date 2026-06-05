# Derivado B — Migración ligera

Monolito legacy 38MB → **shell + JSON externo**.

- `biblioteca-universal-prompting-2026.html` — shell (~25KB) que reusa `estilos/doc.css`.
- `biblioteca-data.json` — 2026 prompts extraídos de `window.promptsUniversales` y **normalizados** (campos `invoke`/`keywords`/`strategy` pasaron de repr Python → JSON; `desc` derivado de `strategy.how_to_use`/`example_output`).
- `estilos/`, `favicon.svg` — copiados de la live.

Features: render incremental (lotes 60 + IntersectionObserver), debounce + índice, búsqueda en cuerpo, filtros categoría/rail, orden q/A-Z/categoría, command palette (⌘K / `/`), slash-invoke por `invoke`, deep-link `?q=&rail=&cat=&sort=#id` + Compartir, skip-link, aria-live, no-results.

Servir: `python3 -m http.server` (usa `fetch`, no `file://`).
Re-extraer: `window.promptsUniversales` está en el monolito de `../originals/`.

## Capa de invocación parametrizada (propagada de la live)

77 registros (/0–/9 + verbos + /a–/z; legacy conflaciona /s=/sintetiza) con
`params:[{key,label,opts,def}]` y `content` tokenizado `[[key]]`. El modal renderiza
selectores que reescriben el prompt al vuelo + toggle «Anteponer parámetros»;
defaults = comportamiento previo. Parámetros, NO inputs.
Generador: `tools/propagar-params.py` (reusa la tabla de specs de la live;
backup en `biblioteca-data.json.bak`).
