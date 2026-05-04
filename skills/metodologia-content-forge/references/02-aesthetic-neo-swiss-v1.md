# MetodologIA · Aesthetic v1.0 · Neo-Swiss Clean and Soft Explainer

> Sistema visual canónico · CC BY-NC-SA 4.0 · Javier Montaño · MetodologIA · 2026.

`[FUENTE-PRIMARIA]` Brand voice v3.0 + dirección visual usuario · 2026-05.

---

## Identidad de la estética

**Nombre completo**: Neo-Swiss Clean and Soft Explainer (Corporate Clean and Premium).

**Categoría**: editorial corporate-explainer · ilustración vectorial flat · grid suizo.

**Tono visual**: orden + calma + claridad · evita ruido · respeta el silencio del espacio en blanco.

**Tagline**: *Diseño editorial · ilustración suave · explicación honesta.*

---

## Pilares visuales (analogía con voz)

| Pilar | En voz | En estética |
|---|---|---|
| **P1** (R)Evolución | Brecha → método | Composición que muestra antes/después con claridad |
| **P2** Intención > intensidad | Diseño antes que fuerza | Mucho espacio en blanco · pocas decoraciones · jerarquía clara |
| **P3** Tecnología aliada | Automatiza repetible | Grid + tokens · sistema replicable · 0 hardcoded |

**Regla**: si un elemento visual no comunica decisión / comprensión / acción · sobra.

---

## Paleta canónica · 6 colores

> Fuente única de verdad: `assets/color-tokens.json`. **Nunca hardcodear hex en otro lado.**

### Primarios

| Token | HEX | RGB | Uso primario | Uso secundario |
|---|---|---|---|---|
| `--navy` | `#122562` | rgb(18,37,98) | Headings · CTAs · brand signal | Borders fuertes · backgrounds dark mode |
| `--gold` | `#FFD700` | rgb(255,215,0) | Highlight · KPI big-numbers · accent en hero | Underline emphasis · iconos críticos |
| `--blue` | `#137DC5` | rgb(19,125,197) | Links · CTAs secundarios · gradientes con navy | Hover states · datos en charts |
| `--dark` | `#1F2833` | rgb(31,40,51) | Body text · captions sobre claro · footer | Iconos sólidos · separadores |
| `--lilac` | `#BBA0CC` | rgb(187,160,204) | Accent humano · soft sections · personas | Tags categoría · hover backgrounds |
| `--gray` | `#808080` | rgb(128,128,128) | Tertiary text · hints · disabled | Borders sutiles · skeleton loaders |

### Derivados oficiales (computados, NO inventes)

| Token | HEX | Función |
|---|---|---|
| `--bg` | `#F9FAFB` | Canvas claro principal |
| `--bg-soft` | `#F0F0EC` | Canvas suave alternativo (off-white cálido) |
| `--bg-card` | `rgba(255,255,255,.88)` | Cards sobre canvas claro |
| `--text` | `#1F2833` | (= `--dark`) body |
| `--text-sec` | `#4A5568` | Secondary body |
| `--text-muted` | `#808080` | (= `--gray`) hints |
| `--border` | `rgba(18,37,98,.08)` | Divisores sutiles |
| `--shadow-card` | `0 1px 3px rgba(0,0,0,.04), 0 6px 16px rgba(0,0,0,.06)` | Sombra suave estándar |

### Dark mode

| Token | HEX | Función |
|---|---|---|
| `--bg` | `#0B2545` | Canvas dark (navy profundo) |
| `--bg-soft` | `#071A33` | Canvas dark alterno |
| `--bg-card` | `rgba(11,37,69,.6)` | Cards dark |
| `--text` | `#F0F4F8` | Body dark |
| `--text-sec` | `#CBD5E1` | Secondary dark |

`[CRITERIO-ACEPTACIÓN]` Contraste WCAG AA mínimo (AAA preferido): 7:1 body · 4.5:1 large text. Verificado computacionalmente.

---

## Tipografía · 3 familias canónicas

| Familia | Uso | Pesos | Reglas |
|---|---|---|---|
| **Poppins** | Titulares (h1-h3) · CTAs grandes | 600 / 700 | Sentence case · flush left · 3 sizes máx por layout |
| **Montserrat** | Cuerpo · subheaders · UI | 400 / 500 / 600 | Line-height ≥1.5 · max-width 65ch |
| **Trebuchet MS** | Notas · footnotes · callouts · popups | 400 italic | Solo elementos secundarios · jamás body |

### Fallbacks

```css
font-family: 'Poppins', 'Inter', system-ui, sans-serif;       /* head */
font-family: 'Montserrat', 'Inter', system-ui, sans-serif;    /* body */
font-family: 'Trebuchet MS', 'Lucida Sans Unicode', sans-serif; /* notes */
```

### Escala tipográfica · 5 sizes (max usados por pieza: 3)

| Token | Size desktop | Size mobile | Uso |
|---|---|---|---|
| `--fs-hero` | `48px` (3rem) | `32px` (2rem) | Hero h1 only |
| `--fs-h1` | `36px` (2.25rem) | `28px` (1.75rem) | Section titles |
| `--fs-h2` | `24px` (1.5rem) | `22px` | Subsections |
| `--fs-body` | `16px` (1rem) | `16px` | Body default |
| `--fs-note` | `14px` (.875rem) | `14px` | Captions · footnotes |

---

## Composición · grid suizo

### Anatomía base

```
┌─────────────────────────────────────────────────────┐
│ [HEADER · sticky · navy on white]                   │
├─────────────────────────────────────────────────────┤
│                                                     │
│  [HERO]                                             │
│   ├─ Eyebrow chip (navy soft / lilac)               │
│   ├─ H1 Poppins 48px (left flush)                   │
│   ├─ Lead Montserrat 18px (max 65ch)                │
│   └─ CTA primary (navy bg · white) + secondary      │
│                                                     │
├─────────────────────────────────────────────────────┤
│  [12-COL GRID · gap 24px · padding 64px desktop]    │
│   ┌─────────┬─────────┐                             │
│   │ TEXT    │ VISUAL  │  ← columnas pareadas         │
│   │ 6 cols  │ 6 cols  │                             │
│   └─────────┴─────────┘                             │
│                                                     │
├─────────────────────────────────────────────────────┤
│  [STATBAR · 4 KPIs · gold big-numbers]              │
├─────────────────────────────────────────────────────┤
│  [FOOTER · 3-col · gray-muted]                      │
└─────────────────────────────────────────────────────┘
```

### Reglas de composición

| Regla | Detalle |
|---|---|
| Grid | 12 columnas · gap 24px · max-width 1200px (1440 large) |
| Spacing | Múltiplos de 8px (8 / 16 / 24 / 32 / 48 / 64 / 96) |
| Padding sección | 64px desktop · 32px tablet · 24px mobile |
| Cards | radius 12px (md) o 20px (lg) · shadow suave |
| Borders | 1px solid `--border` · 0 borders pesados |
| Iconos | Tamaño 24px (inline) o 48px (feature) · stroke 2px |

---

## Ilustración · estilo

### Características

- **Vectorial flat**: sin texturas raster · sin fotorealismo
- **Vibrante pero sobria**: usa paleta canónica · 0 colores fuera de tokens
- **Figuras humanas sin rostro**: siluetas con tonos de piel neutrales o monocromas en `--lilac`/`--navy`
- **Formas geométricas suaves**: rectángulos con radius 12-20 · círculos · arcos · líneas onduladas suaves
- **Elementos UI integrados**: chips · checklists · timers · progress bars · badges como parte de la ilustración
- **Sombras suaves**: micro-gradientes discretos `gold→gold-light` o `navy→blue` · NO sombras realistas
- **Iconografía consistente**: pictogramas line (stroke 2px) o solid · jamás mezclar estilos

### Lista roja visual

| ❌ NO hacer | ✅ Sí hacer |
|---|---|
| Fotos stock realistas | Ilustración vectorial flat |
| Texturas raster (papel arrugado, grunge) | Geometría limpia · radius suaves |
| Colores fuera de paleta | Solo 6 colores canónicos + neutrales |
| Sombras profundas (drop-shadow ≥10px) | Micro-shadow suave (≤6px blur) |
| Mezcla de estilos icono (line + solid + 3D) | Un solo estilo por pieza |
| Texto sobre fondo ruidoso | Texto sobre canvas plano + alto contraste |
| Verde dominante (#42D36F, #00FF00) | Solo paleta · lilac para humano |
| Gradientes saturados | Micro-gradientes discretos brand |

---

## Componentes canónicos · M1-M10

> Análogo a C1-C10 de Sofka · adaptado a estética MetodologIA.

### M1 · Sticky nav minimal

- Background `--bg-card` con backdrop-blur
- Border-bottom 1px `--border`
- Logo (text + dot gold) izquierda · sections derecha (Montserrat 14px uppercase)
- Height 64px desktop · 56px mobile

### M2 · Hero con eyebrow + KPI row

```
┌─────────────────────────────────┐
│ [eyebrow chip lilac]            │
│ H1 Poppins 48px navy            │
│ Lead Montserrat 18px            │
│ [CTA primary] [CTA secondary]   │
├─────────────────────────────────┤
│ KPI1   KPI2   KPI3   KPI4       │  ← gold big-numbers
└─────────────────────────────────┘
```

### M3 · Section badge (chip + chapter)

- Chip `--lilac` background + ink texto
- Chapter title Poppins 24px navy
- Lead Montserrat 16px

### M4 · 2-column text + visual

- 6/6 desktop · stack mobile
- Texto izquierda · ilustración derecha (o invertido)
- Card con shadow suave si la columna texto es densa

### M5 · Statbar 4-col

```
┌──────┬──────┬──────┬──────┐
│ 47   │ 12   │ 4.7  │ 92%  │  ← Poppins 36px gold
│ días │ pers │ /5   │ adop │  ← Montserrat 14px gray
└──────┴──────┴──────┴──────┘
```

### M6 · Process diagram (orbit / steps)

- Core central (círculo navy con número)
- 4 satélites en cardinal points
- Líneas suaves conectoras (`--border` 2px)
- Mobile: stack vertical con conectores → o ↓

### M7 · Mermaid card

- Mermaid wrapped en card `--bg-card`
- Theme variables: primary navy · secondary gold · lines blue
- Border-radius 12px · padding 32px

### M8 · Modal explainer

- Overlay `rgba(31,40,51,.6)` (navy ink)
- Card centrada · max-width 640px · radius 20px
- Focus-trap · ESC close · slide-up animation 250ms

### M9 · Quote pull (testimonial)

```
   ❝ [quote en Poppins italic 24px navy]
       — [autor] · [rol]
```

- Border-left 4px `--gold` (no fill, solo línea)
- Mark "❝" en `--gold` 48px

### M10 · Footer 3-col

- Col 1: brand + tagline + dot gold
- Col 2: links (Montserrat 14px)
- Col 3: meta (license · contact · year)
- Background `--bg-soft` o `--dark` (dark mode)

---

## Elementos UI específicos

### Chips

```css
.chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: 999px;
  background: var(--lilac);
  color: var(--navy);
  font: 500 12px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

### Checklists

```html
<ul class="checklist">
  <li><span class="check">✓</span> Item con check gold</li>
  <li><span class="check">✓</span> Otro item</li>
</ul>
```

```css
.check {
  color: var(--gold);
  font-weight: 700;
  margin-right: 8px;
}
```

### Timers / progress

- Bar 4px height · radius 999px
- Background `--border` · fill `--blue` o `--gold`
- Label arriba (Montserrat 14px) + percent derecha

### Botones

| Tipo | Background | Color | Border |
|---|---|---|---|
| Primary | `--navy` | white | none |
| Secondary | white | `--navy` | 1px `--navy` |
| Tertiary | transparent | `--blue` | none (subraya hover) |
| Destructive | `--bg-card` | red-600 | 1px red-300 |

Hover: opacity 0.9 + transform `translateY(-1px)` + shadow más fuerte.

---

## Animación · motion budget

| Tipo | Duración | Easing | Cuándo |
|---|---|---|---|
| Hover micro | 150ms | `cubic-bezier(0.4,0,0.2,1)` | Cards · buttons · links |
| Modal slide | 250ms | `cubic-bezier(0.4,0,0.2,1)` | Modales · sheets |
| Page transition | 400ms max | smooth | Solo si hay narrativa |
| Loading skeleton | 1500ms loop | linear | Solo en data-heavy |

`[LÍMITE]` `prefers-reduced-motion: reduce` desactiva todo excepto opacity.

---

## Validación brand visual · checklist

```
[ ] Solo 6 colores canónicos + neutrales/derivados oficiales
[ ] Tipografías: Poppins (head) + Montserrat (body) + Trebuchet (notes)
[ ] Max 3 sizes tipográficos por pieza
[ ] WCAG AA mínimo (AAA preferido): contrast 4.5:1 / 7:1
[ ] Spacing en múltiplos de 8px
[ ] Cards con shadow suave (≤6px blur)
[ ] Iconos consistentes (un solo estilo por pieza)
[ ] 0 imágenes raster realistas en hero
[ ] 0 colores fuera de paleta
[ ] 0 verde dominante
[ ] Footer presente con MetodologIA · year · license
[ ] Footer NO usa "gratis" ni derivados (NUEVO v4)
```

---

## Anti-patrones visuales (top-5 graves)

| # | Anti-patrón | Detección | Antídoto |
|---|---|---|---|
| 1 | Colores fuera de paleta | Hex ≠ tokens canónicos | Solo `--navy/gold/blue/dark/lilac/gray` |
| 2 | >3 sizes tipográficos | Hero + h1 + h2 + h3 + body + note | Reducir a 3 jerarquías clave |
| 3 | Sombras profundas / glows | drop-shadow ≥10px / glow neon | shadow-card suave (`6px 16px`) |
| 4 | Texto sobre imagen ruidosa | Hero con foto detrás del título | Canvas plano con micro-gradient |
| 5 | Mezcla estilos icono | line + solid + 3D + emoji | Un solo estilo por pieza |

---

## Referencias cruzadas

- `01-brand-voice-v4.md` (sistema de voz complementario)
- `03-nudge-phrases.md` (frases visuales · descripciones para IA)
- `assets/color-tokens.json` (single source of truth de paleta)
- `templates/html-shell.html.j2` (shell brand-ready)
- `scripts/validate_brand.py` (verificación automática)

> v1.0 · CC BY-NC-SA 4.0 · MetodologIA · Javier Montaño · 2026
