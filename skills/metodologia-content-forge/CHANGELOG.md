# Changelog · metodologia-content-forge

Formato: [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) · Versionado: [SemVer](https://semver.org/lang/es/).

---

## [1.0.0] · 2026-05-04 · Inaugural

**Tipo**: skill nueva · MetodologIA Content Forge.
**Misión**: forjar contenido brand-compliant MetodologIA con la robustez de `sofka-ui-pro-max` adaptada a la marca propia.

### Added

#### Estructura raíz
- `SKILL.md` (orquestador 5 fases: INTAKE → REASON → COMPOSE → GENERATE → DELIVER)
- `README.md` con quick start
- `CHANGELOG.md` (este archivo)
- `LICENSE.md` (CC BY-NC-SA 4.0)

#### 4 References (fuente de verdad)
- `01-brand-voice-v4.md` — Brand Voice v4.0 con **prohibición de `gratis`/`gratuito`/`regalo`** y nueva jerarquía "sin fricción" → "sin inversión económica inicial" → "sin costo"
- `02-aesthetic-neo-swiss-v1.md` — Aesthetic Neo-Swiss Clean and Soft Explainer · paleta 6 colores · Poppins + Montserrat + Trebuchet · 10 componentes M1-M10
- `03-nudge-phrases.md` — 8 nudges canónicos (N1-N8) + combos por contexto
- `04-prompt-templates.md` — 8 templates copy-paste (T1-T8) por tipo de pieza

#### Scripts
- `validate_voice.py` — verifica lista roja + estructura Minto + footer + neutralidad

#### Assets
- `color-tokens.json` — single source of truth · paleta · tipografía · escala · spacing · radius · motion · validation thresholds · voice redlist + greenlist

#### Outputs (HTML brand-ready)
- `outputs/metodologia-brand-voice-v4.html` — pieza brand-compliant que documenta la voz v4.0 con estética Neo-Swiss aplicada
- `outputs/metodologia-aesthetic-neo-swiss-v1.html` — pieza brand-compliant que documenta la estética visual con paleta + tipografías + componentes

### Cambios v3.0 → v4.0 de la voz

- **Lista roja agregada**: `gratis`, `gratuito`, `gratuita`, `regalo`, `free`, `freemium`
- **Lista verde agregada**: `sin fricción`, `sin inversión económica inicial`, `sin costo`
- **Regla nueva**: jerarquía de "free" — (1) sin fricción [default] → (2) sin inversión económica inicial → (3) sin costo [literal] → nunca "gratis"
- **Razón**: "gratis" devalúa el método · MetodologIA es premium pero accesible · diferencia entre "regalado" y "sin barrera de entrada"

### Pilares confirmados

- **P1** (R)Evolución
- **P2** Intención antes que intensidad
- **P3** Tecnología como aliada

### Roadmap v1.1+

- [ ] `build_html.py` · `build_md.py` · `build_image_prompt.py` (generadores desde spec.json)
- [ ] data/ CSVs poblados (content-types · voice-modes · audiences · components)
- [ ] templates/html-shell.html.j2 + components/M1-M10.html.j2
- [ ] prompts/intake-system.md · compose-system.md · critique-system.md
- [ ] examples/ con walkthroughs end-to-end
- [ ] tests/ pytest smoke tests
- [ ] DOCX/PPTX exporters (vía python-docx / python-pptx)

---

> CC BY-NC-SA 4.0 · MetodologIA · Javier Montaño · 2026
