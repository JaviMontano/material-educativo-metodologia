---
name: metodologia-content-forge
description: >
  Forja contenido brand-compliant MetodologIA desde lenguaje natural. Combina
  Brand Voice v4.0 (Minto-First + lista roja con prohibición de "gratis"/
  "gratuito") con estética Neo-Swiss Clean and Soft Explainer (paleta exclusiva
  navy #122562 / gold #FFD700 / blue #137DC5 / dark #1F2833 / lilac #BBA0CC /
  gray #808080 + Poppins/Montserrat/Trebuchet). Genera Markdown, HTML
  self-contained, slide decks, posts LinkedIn, emails, playbooks. Activa para
  frases como "post MetodologIA", "playbook MetodologIA", "audita esta pieza
  con voz MetodologIA", "genera HTML brand-ready MetodologIA", "crea contenido
  con voz Minto", "reescribe esto con voz MetodologIA". Use proactively cuando
  el usuario pida contenido educativo o de marca MetodologIA.
argument-hint: "<descripción NL del contenido a generar>"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion
license: CC BY-NC-SA 4.0
version: 1.0.0
author: Javier Montaño · MetodologIA
model: opus
---

# `metodologia-content-forge` v1.0.0

> **Misión**: convertir lenguaje natural en piezas brand-compliant MetodologIA · voz Minto-First v4.0 + estética Neo-Swiss Clean and Soft Explainer · genera Markdown + HTML + briefs para imagen/slide.

---

## Cuándo activar

| Trigger | Acción |
|---|---|
| "post / playbook / email / slide / página MetodologIA" | Activar generación |
| "voz MetodologIA" / "voz Minto" / "voz brand" | Activar voz como filtro |
| "audita / revisa esta pieza" | Activar modo Auditoría |
| "reescribe con voz MetodologIA" | Activar modo Reescritura |
| "HTML brand-ready" / "estética Neo-Swiss" | Activar generación HTML |
| "imagen MetodologIA" / "ilustración brand" | Devolver prompt para Midjourney/DALL-E con paleta |

**NO activar** cuando:
- Pieza es para otra marca (Sofka, JM Labs, etc.) → otra skill
- Pieza es código pesado (React app) → usar `frontend-design`
- DOCX/XLSX/PPTX directo → usar `brand-docx` / `brand-xlsx` / `brand-pptx`

---

## Workflow · 5 fases

```
NL → [INTAKE] → [REASON] → [COMPOSE] → [GENERATE] → [DELIVER]
```

### Fase 1 · INTAKE

Parsear NL y extraer:

| Campo | Valores |
|---|---|
| `surface` | post-linkedin / email / playbook / slide-deck / one-pager / landing / cartilla |
| `audience` | b2c / b2b / ejecutivo / mixto |
| `density` | micro (Minto Micro) / completo (Minto Completo) / ultracorto |
| `tone` | editorial / corporate / explainer / pedagogical / executive |
| `length` | chars / words / slides count |
| `language` | es-latam (default) / es-eu / en |
| `output_format` | md / html / both / image-prompt / slide-md |
| `include_visual` | true / false (si requiere ilustración) |
| `pillar_focus` | P1 (R)Evolución / P2 Intención / P3 Tecnología / mixto |

Si falta info crítica · preguntar con `AskUserQuestion` · máximo 3 preguntas.

### Fase 2 · REASON

Aplicar reglas de `references/01-brand-voice-v4.md` + `02-aesthetic-neo-swiss-v1.md`:

1. Determinar **modo Minto** (Micro/Completo/Ultracorto) según `density` + `surface`
2. Elegir **MECE** según audiencia (B2C: Claridad/Sistema/Continuidad · B2B: Gobernanza/Capacidades/Tecnología · Ejec: Riesgo/Retorno/Implementación)
3. Anclar **pilares** [P1/P2/P3] por soporte
4. Si `include_visual`: aplicar tokens de `assets/color-tokens.json` + componentes M1-M10
5. Generar `reason.json`

### Fase 3 · COMPOSE

Sintetizar `spec.json`:

```json
{
  "meta": { "surface": "...", "audience": "...", "density": "...", "lang": "es-latam" },
  "voice": { "mode": "minto-completo", "pillars": ["P1","P2","P3"] },
  "structure": {
    "conclusion": "...",
    "supports": [
      { "text": "...", "pillar": "P1", "evidence": { "type": "DATO", "value": "..." } },
      { "text": "...", "pillar": "P2", "evidence": { "type": "INDICADOR-SUGERIDO", "value": "..." } }
    ],
    "cta": { "verb": "...", "object": "...", "context": "..." }
  },
  "aesthetic": {
    "palette": "neo-swiss-default",
    "components": ["M1","M2","M5","M10"],
    "dark_mode": false
  },
  "footer": "MetodologIA · Javier Montaño · CC BY-NC-SA 4.0 · 2026"
}
```

**Self-critique** (`prompts/critique-system.md`): valida lista roja · MECE · evidencia · CTA · paleta · tipografía. Si falla, regenera (max 1 intento).

### Fase 4 · GENERATE

| Output | Comando | Resultado |
|---|---|---|
| `md` | `python scripts/build_md.py spec.json --out pieza.md` | Markdown estructurado |
| `html` | `python scripts/build_html.py spec.json --out pieza.html` | HTML self-contained |
| `slide-md` | `python scripts/build_slides.py spec.json --out deck.md` | Slides en MD con frontmatter |
| `image-prompt` | `python scripts/build_image_prompt.py spec.json` | Prompt para Midjourney/DALL-E |

### Fase 5 · DELIVER

1. `python scripts/validate_voice.py <output>` → reporte voz
2. Si HTML: `python scripts/validate_brand.py <output>` → reporte estética
3. Si HTML: `python scripts/preview.py <output>` (abre browser)
4. Imprime ghost menu con próximos pasos

---

## Decision tree NL → output

| Frase NL | Surface | Density | Output |
|---|---|---|---|
| "post LinkedIn sobre X" | post-linkedin | micro | md (≤1300 chars) |
| "email a clientes B2B" | email | ultracorto | md (≤150 palabras) |
| "playbook educativo de Y" | playbook | completo | md + html |
| "slide deck de N slides" | slide-deck | micro por slide | slide-md |
| "landing page para Z" | landing | completo | html self-contained |
| "cartilla pedagógica" | cartilla | completo | html con secciones expandidas |
| "imagen para post" | image | n/a | image-prompt |
| "audita esta pieza: [...]" | audit-mode | n/a | reporte rúbrica /20 |

---

## Architecture

```
metodologia-content-forge/
├── SKILL.md (este archivo)
├── README.md (quick start)
├── CHANGELOG.md
├── LICENSE.md
├── references/
│   ├── 01-brand-voice-v4.md (fuente única voz · ROJA + JERARQUÍA "sin fricción")
│   ├── 02-aesthetic-neo-swiss-v1.md (paleta · tipografía · componentes M1-M10)
│   ├── 03-nudge-phrases.md (8 nudges canónicos · combos)
│   ├── 04-prompt-templates.md (T1-T8 templates copy-paste)
│   ├── 05-anti-patterns.md (lo que NUNCA hacer)
│   └── 06-decision-tree.md (NL → spec)
├── data/
│   ├── content-types.csv (post · email · playbook · slide · landing · cartilla)
│   ├── voice-modes.csv (minto-completo · minto-micro · ultracorto · auditoria)
│   ├── audiences.csv (b2c · b2b · ejecutivo · mixto + MECE preferido)
│   └── components.csv (M1-M10 con uso · props · anti-patrones)
├── scripts/
│   ├── validate_voice.py (verifica lista roja · "gratis" · gates Minto)
│   ├── validate_brand.py (verifica paleta · tipografía · WCAG · estructura HTML)
│   ├── build_md.py (genera Markdown desde spec)
│   ├── build_html.py (genera HTML self-contained desde spec)
│   ├── build_image_prompt.py (genera prompt para Midjourney/DALL-E)
│   ├── preview.py (abre browser)
│   └── tests/ (smoke tests)
├── templates/
│   ├── html-shell.html.j2 (shell brand-ready Neo-Swiss)
│   └── components/ (M1-M10 snippets)
├── assets/
│   ├── color-tokens.json (single source of truth · 6 colores + derivados)
│   └── examples/ (specs JSON pre-llenados)
├── prompts/
│   ├── intake-system.md
│   ├── compose-system.md
│   └── critique-system.md
├── outputs/ (HTMLs brand-ready: voice-v4 + aesthetic-v1)
└── examples/ (walkthroughs)
```

---

## Lista roja · 0 tolerancia (verificada por script)

| Categoría | Palabras | Reemplazo |
|---|---|---|
| Hype | hack · truco · secreto · resultados instantáneos · milagroso | (eliminar · reformular) |
| **NUEVO v4** | **gratis · gratuito · gratuita · regalo · free · freemium** | "sin fricción" / "sin inversión económica inicial" / "sin costo" |
| Brand off | arquitecto · arquitectura | Diseñador · Diseño |
| Brand off | transformación | (R)Evolución |
| Hueco | sinergia · leverage · holístico · bandwidth · circle back | (eliminar) |
| Vago | mejorar · alinear · optimizar (sin contexto) | + verbo concreto + objeto + contexto |

---

## Tokens canónicos (referencia rápida)

| Token | HEX | Uso |
|---|---|---|
| `--navy` | `#122562` | Headings · CTAs primary · brand signal |
| `--gold` | `#FFD700` | Highlight · KPI big-numbers · accent |
| `--blue` | `#137DC5` | Links · CTAs secondary · gradients |
| `--dark` | `#1F2833` | Body text · footer · separadores |
| `--lilac` | `#BBA0CC` | Accent humano · soft sections · personas |
| `--gray` | `#808080` | Tertiary · hints · disabled |

**Tipografía**: Poppins (head) + Montserrat (body) + Trebuchet MS (notes).

> Fuente única: `assets/color-tokens.json`. **NUNCA hardcodear hex en otro lado.**

---

## Validación obligatoria · checklist

### Voz (validate_voice.py)

```
[ ] 0 lista roja (incluye "gratis"/"gratuito")
[ ] Estructura Minto presente (Conclusión + Soportes + Evidencia + CTA)
[ ] Cada soporte ancla a [P?]
[ ] CTA con verbo + objeto + contexto
[ ] Español latino neutro · trato tú
```

### Brand visual (validate_brand.py · solo HTML)

```
[ ] Solo 6 colores canónicos + neutrales/derivados
[ ] Tipografías: Poppins + Montserrat + Trebuchet (presentes)
[ ] WCAG AA mínimo · contraste 4.5:1 / 7:1
[ ] Footer con MetodologIA · Javier Montaño · CC BY-NC-SA 4.0
[ ] Footer NO contiene "gratis" ni derivados
```

---

## Quick start

```bash
cd ~/.claude/skills/metodologia-content-forge

# Validar voz de una pieza existente
python scripts/validate_voice.py archivo.md

# Validar brand visual de un HTML
python scripts/validate_brand.py archivo.html

# Ver outputs canónicos pre-generados
open outputs/metodologia-brand-voice-v4.html
open outputs/metodologia-aesthetic-neo-swiss-v1.html
```

---

## Ghost menu post-generación

Tras generar pieza · ofrecer:

```
Generado: pieza.md (1234 chars · voz validated · 0 lista roja)

Próximos pasos:
1) Validar voz: python scripts/validate_voice.py pieza.md
2) Convertir a HTML: python scripts/build_html.py spec.json --out pieza.html
3) Generar imagen: python scripts/build_image_prompt.py spec.json
4) Auditoría rigurosa: aplicar T2 con rúbrica /20
5) Compartir: copy a clipboard (pbcopy < pieza.md)
```

---

## Out of scope (v1.0)

- Otras marcas (Sofka, JM Labs, AAD, etc.) · esta skill es **MetodologIA-only**
- Generación de DOCX/PPTX/XLSX nativo (usar skills dedicadas downstream)
- Generación de imagen real (devuelve prompts para Midjourney/DALL-E)
- React/Vue components (usar `frontend-design` o `sofka-ui-pro-max`)
- Multi-idioma simultáneo (es default · en bajo demanda)

---

## Referencias cruzadas

- Brand Voice fuente: `references/01-brand-voice-v4.md`
- Estética fuente: `references/02-aesthetic-neo-swiss-v1.md`
- Nudges atómicos: `references/03-nudge-phrases.md`
- Templates de prompts: `references/04-prompt-templates.md`
- Skill compañera: `aprender-aprehender-revolucionar` (contenido educativo)

> v1.0.0 · CC BY-NC-SA 4.0 · MetodologIA · Javier Montaño · 2026
