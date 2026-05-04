# Changelog · Cartilla v2.0 · 2026-05-04 · Look-and-feel migration to biblioteca-2026

## Conclusión
Migración visual del playbook al sistema canónico de la biblioteca-2026 (`biblioteca-universal-prompting-2026 (7).html`): tokens, glass-morphism, hero kinetic, buttons polish, footer dark navy, callout variants, sticky h2, easing tokens. **Zero regresión funcional · zero contenido modificado**.

## Decisiones tomadas (autónomas · "total")

| Feature biblioteca | Decisión | Razón |
|---|---|---|
| Scroll-snap paginado e-book | ❌ NO | Playbook = lectura continua pedagógica · 26 secciones densas |
| Sidebar fijo (mobile bottom 56px) | ❌ NO | Mantener TOC drawer (ya funciona · 26 entradas con jerarquía 4 niveles) |
| Page counter + ebook indicator dots | ❌ NO | Ruido visual fuera del modelo paginado |
| Tokens canónicos (glass, shadows, easing, radius scale) | ✅ SÍ | Base para todo lo demás |
| Hero kinetic + scroll hint bounce | ✅ SÍ | Identidad de marca instantánea |
| Glass-morphism topnav + modal | ✅ SÍ | Look biblioteca · backdrop-filter blur(12px) |
| Buttons polish (spring easing + shadow elevation) | ✅ SÍ | Microinteracciones de calidad |
| Footer dark navy + border-top gold | ✅ SÍ | Cierre visual fuerte de marca |
| Callout variants gold/navy/blue | ✅ SÍ | Más expresividad sin romper contenido existente |
| Sticky h2 mobile | ✅ SÍ | Lectura paginada en pantallas pequeñas |
| Reading bar CSS-only `animation-timeline` | ✅ SÍ | Progressive enhancement (fallback JS conservado) |

## Cambios técnicos

### Tokens (`:root` + `html.dark`)
- **Colores**: `--navy-dark:#1F2833`, `--gold-dark:#B8860B` (de #D4A017), `--lilac:#BBA0CC` (de #BAA0CC)
- **Backgrounds**: `--bg:#F9FAFB` (de #FAF9F6), `--bg-soft:#F0F0EC`, `--bg-card` valor exacto
- **Glass**: `--glass-bg:rgba(255,255,255,.82)`, `--glass-blur:blur(12px)`
- **Texto AAA**: `--text:#0F172A`, `--text-sec:#334155`, `--text-muted:#475569`
- **Sombras**: `--shadow-glow`, `--shadow-card` (multilayer), `--shadow-lg:0 12px 32px`
- **Radius scale**: `--radius-sm:6px`, `--radius-md:12px`, `--radius-lg:20px`, `--radius-xl:32px`
- **Easing**: `--ease-spring`, `--ease-smooth` (además del `--transition` original)
- **Layout**: `--max-w:1100px`, `--sidebar-w:56px`
- **Compat aliases**: `--text-soft`, `--shadow`, `--radius` apuntan a los nuevos tokens

### Bloque CSS v2.0 unificado (~5 KB)
- Spring/smooth easing aplicado a todos los componentes interactivos
- Hover translateY(-4px) + shadow-lg en cards
- `.btn-primary` con padding 0.95em/2em + shadow elevation
- Topnav `backdrop-filter:blur(12px)` + glass-bg
- Modal con glass effect
- Hero ::before blob radial gradient (gold)
- `.hero .eyebrow` con dot glow animado (`pmDotGlow` 2s infinite)
- `pmFadeUp` staggered en hero h1/promesa/ctas (0s/0.15s/0.3s delays)
- `.hero-scroll-hint` con `pmBounce` 2s infinite (link a #storytelling)
- Callout variants `.callout-navy` y `.callout-blue`
- Sticky h2 mobile `position:sticky; top:56px; z-index:5`
- Reading bar CSS-only con `@supports (animation-timeline:scroll())`
- Footer dark `var(--navy-dark)` con border-top `6px solid var(--gold)`
- Reveal con `--ease-smooth` 0.7s
- Card glow on hover (`::after` radial gradient)
- Pillar-tags con biblioteca chip style (rgba gold)
- `prefers-reduced-motion` cubre todas las animaciones nuevas

### HTML
- Hero recibe `<a class="hero-scroll-hint">` después de `.ctas` (link a #storytelling)
- Cero secciones movidas · cero contenido modificado · 169 modales intactos · 140 pillar-tags intactos

## Métricas v2.0

- HTML: 380 KB → **396 KB** (+16 KB · CSS unificado v2.0)
- Secciones: 31 (sin cambios)
- Modales: 169 (sin cambios)
- Pillar-tags: 140 (sin cambios · estilo refinado)
- Cero errores JS · `prefers-reduced-motion` respetado · WCAG AAA preservado
- Backup: `playbook-prompting-universal-2026.html.bak-pre-v2-0-20260504`

## Verificación post-build

- ✅ Tokens canónicos accesibles vía `getComputedStyle(:root)`
- ✅ Hero eyebrow con dot glow renderiza
- ✅ Scroll hint bounce visible al final del hero
- ✅ Topnav `backdrop-filter:blur(12px)` activo
- ✅ Footer `background-color:rgb(31,40,51)` + `border-top:6px`
- ✅ Easing tokens (`cubic-bezier(0.175,0.885,0.32,1.275)` y `cubic-bezier(0.16,1,0.3,1)`) aplicados a hover

## Identidad visual unificada

Playbook v2.0 ahora comparte con biblioteca-2026:
- Misma paleta navy/gold/blue/lilac (gold-dark ajustado)
- Misma tipografía Poppins (heads) + Montserrat (body) + Trebuchet MS (notes/labels)
- Mismo glass-morphism en navegación
- Mismo lenguaje de microinteracciones (spring/smooth)
- Mismo footer dark con border gold
- Mismo radius scale (6/12/20/32)
- Mismas variables de easing

**Diferencia intencional**: el playbook mantiene scroll continuo + TOC drawer (no e-book paginado) porque el contenido pedagógico requiere lectura lineal, no navegación tipo catálogo.
