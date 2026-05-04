# metodologia-content-forge

> **Forja de contenido brand-compliant MetodologIA.** Voz Minto-First v4.0 (con prohibición de "gratis"/"gratuito") + Estética Neo-Swiss Clean and Soft Explainer v1.0.

[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE.md) [![Brand](https://img.shields.io/badge/Brand-MetodologIA-122562)](https://metodologia.info) [![Version](https://img.shields.io/badge/version-1.0.0-FFD700)](CHANGELOG.md)

---

## Qué es

Una **skill de Claude Code** que convierte lenguaje natural en piezas brand-compliant MetodologIA · Markdown, HTML self-contained, slides, posts, emails, prompts para imagen.

Inspirada en `sofka-ui-pro-max` pero adaptada a marca **MetodologIA-only**.

### Capas del sistema

1. **Voz** (qué decir y cómo) — Brand Voice v4.0 · Minto-First + lista roja con prohibición de `gratis`/`gratuito` + jerarquía "sin fricción"
2. **Estética** (cómo se ve) — Neo-Swiss Clean · 6 colores · 3 tipografías · 10 componentes M1-M10
3. **Nudges** (cómo activar voz/estética en cualquier IA) — 8 frases-ancla canónicas
4. **Templates** (prompts copy-paste) — 8 templates por tipo de pieza

---

## Quick start

```bash
cd ~/.claude/skills/metodologia-content-forge

# Validar voz de una pieza
python scripts/validate_voice.py archivo.md

# Ver outputs canónicos
open outputs/metodologia-brand-voice-v4.html
open outputs/metodologia-aesthetic-neo-swiss-v1.html
```

### Activar desde Claude Code

```
"genera post LinkedIn sobre cadencia con voz MetodologIA"
"audita esta pieza con rúbrica /20"
"genera HTML brand-ready Neo-Swiss para playbook de aprendizaje"
"reescribe esto con voz MetodologIA (sin gratis)"
"prompt Midjourney para hero MetodologIA sobre IA y método"
```

---

## Lista roja v4 · 0 tolerancia

| Categoría | Palabras | Reemplazo |
|---|---|---|
| Hype | hack · truco · secreto · resultados instantáneos | (eliminar) |
| **Nuevo v4** | **gratis · gratuito · gratuita · regalo · free · freemium** | "sin fricción" / "sin inversión económica inicial" / "sin costo" |
| Brand off | arquitecto / arquitectura | Diseñador / Diseño |
| Brand off | transformación | (R)Evolución |
| Hueco | sinergia · leverage · holístico · bandwidth | (eliminar) |

---

## Tokens canónicos

| Token | HEX | Uso |
|---|---|---|
| `--navy` | `#122562` | Headings · CTAs · brand signal |
| `--gold` | `#FFD700` | Highlight · KPI · accent |
| `--blue` | `#137DC5` | Links · CTAs secondary |
| `--dark` | `#1F2833` | Body · footer |
| `--lilac` | `#BBA0CC` | Accent humano · soft sections |
| `--gray` | `#808080` | Tertiary · hints |

**Tipografía**: Poppins (head) + Montserrat (body) + Trebuchet MS (notes).

> Single source of truth: `assets/color-tokens.json` · NUNCA hardcodear hex.

---

## Estructura

```
metodologia-content-forge/
├── SKILL.md (orquestador 5 fases)
├── README.md (este archivo)
├── CHANGELOG.md
├── LICENSE.md
├── references/
│   ├── 01-brand-voice-v4.md       ← VOZ canónica (con prohibición "gratis")
│   ├── 02-aesthetic-neo-swiss-v1.md ← ESTÉTICA canónica
│   ├── 03-nudge-phrases.md        ← 8 nudges + combos
│   └── 04-prompt-templates.md     ← T1-T8 templates
├── data/                          ← CSVs (futuro)
├── scripts/
│   └── validate_voice.py          ← validación automática voz
├── assets/
│   └── color-tokens.json          ← single source of truth
├── prompts/                       ← system prompts (futuro)
├── outputs/
│   ├── metodologia-brand-voice-v4.html        ← BRAND-READY voz
│   └── metodologia-aesthetic-neo-swiss-v1.html ← BRAND-READY estética
└── examples/                      ← walkthroughs (futuro)
```

---

## Filosofía

> *Si una frase no ayuda a decidir, comprender o actuar, sobra.*
> *Cadencia > intensidad.*
> *Método primero, IA después.*

---

## Atribución y licencia

- **Autor**: Javier Montaño · Founder/CEO MetodologIA
- **License**: CC BY-NC-SA 4.0 (Atribución · NoComercial · CompartirIgual)
- **Año**: 2026
- **Inspiración estructural**: `sofka-ui-pro-max` (BM25 reasoning + 5 fases)

---

> v1.0.0 · CC BY-NC-SA 4.0 · MetodologIA · Javier Montaño · 2026
