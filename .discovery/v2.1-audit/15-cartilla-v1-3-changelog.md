# Changelog · Cartilla v1.3 · 2026-04-29

> **Trigger:** `/ui-ux-pro-max` audit identifies 4 conceptual errors + 11 functional title rewrites + 1 missing free-resources section.

## Issues fijos

### Errores conceptuales (P0)

1. **PIVOTE was wrongly modeled as a 10-step pipeline** → reframed as the canonical 6-dimension / 2-phase framework from `metodologia.info/vision/`:
   - **P** = Personas · **I** = Interacciones · **V** = Valor (Fase A · Fundamentar)
   - **O** = Organización · **T** = Tecnología · **E** = Evolución (Fase B · Amplificar)
   - Anchor `Human First, IA Next` visible at section opening.
   - Verbatim attribution to metodologia.info/vision linked.
2. **The 10 numerical steps `/0`-`/9`** moved to a new dedicated § 9.5 "Pipeline operativo /0-/9" (lives within Organización + Evolución).
3. **ENTRUSTED+ was listed with only 8 axes** despite the 9-letter acronym → added 9th axis `D = Definition of Done` + meta-layer card explaining the `+` (active excellence loop + proactive insights).
4. **DSV title cut from full DSVSR acronym** → restored across § 13 title, TOC, and cross-references in § 8 (Metacognitivo attribute), § 14 (chains of thought intro), § 20 (12 practices exercise).

### Bugs fijados (P1)

- **TOC line 340 bug**: ES dijo `§ 24 · Rubricario` y EN dijo `§ 11 · ENTRUSTED+ rubric` → uniformado a `§ 11 · ENTRUSTED+ · 9 ejes + meta` en ambos idiomas.
- **Hero CTA bug**: botón "Saltar al pipeline" apuntaba a `#atributos` (§ 8) en vez de `#pipeline-pivote` (§ 9) → corregido.
- **Meta description**: actualizada para reflejar framework + pipeline operativo + 9 ejes (no más "pipeline P.I.V.O.T.E. de 10 pasos").
- **Section IDs**: `#pipeline` mantenido como compat anchor + nuevo `#pipeline-pivote` (framework) + nuevo `#pipeline-operativo` (10 pasos).

## Reescrituras editoriales (P1 · 11 títulos insightful)

| § | Antes | Después |
|---|---|---|
| § 8 | "Los 8 atributos del prompting profesional" | **"Los 8 atributos que separan al usuario del operador"** |
| § 9 | "El pipeline P.I.V.O.T.E. · 10 pasos" | **"Framework P.I.V.O.T.E. · 6 dimensiones · 2 fases"** |
| § 9.5 | (nueva) | **"El pipeline operativo /0-/9 · de pedido difuso a entregable defendible"** |
| § 10 | "Las 12 cláusulas paramétricas (ajustables al vuelo)" | **"Los 12 contratos invisibles que llevan tu output al estándar profesional"** |
| § 11 | "Rubricario ENTRUSTED+ · 8 ejes" | **"Rubricario ENTRUSTED+ · 9 ejes auditables + capa meta"** |
| § 12 | "10 etiquetas de procedencia" | **"Las 10 etiquetas que separan 'creo que' de 'sé que'"** |
| § 13 | "Flujo DSV · 5 pasos" | **"Metacognición DSVSR · el cerebro detrás de los outputs defendibles"** |
| § 14 | "Cadenas de pensamiento y razonamiento" | **"Las 6 formas de hacer pensar a la IA antes de responder"** |
| § 15 | "Las 6 técnicas élite del prompting profesional" | **"Las 6 técnicas que el 5% domina (y nadie te enseña)"** |
| § 19 | "Protocolo de prompting paso a paso" | **"El protocolo que ejecutás cada vez que escribís un prompt"** |
| § 20 | "12 ejercicios · de 3 min a sesión completa" | **"12 prácticas para que el método se grabe en músculo"** |
| § 22 | "Tres ritmos · diaria · semanal · mensual" | **"Tres ritmos de práctica · cuándo se vuelve hábito"** |

## Sección nueva (P1 · § 23 Asistentes gratuitos)

`#asistentes-free` con **6 cards** (Pristino · Pristino OSS · GPT Prompting · GPT Investigaciones · 5 Gems destacados · Catálogo completo) + badge "sin costo · sin fricción · sin riesgo" + ancla a la visión.

CSS añadido (~2 KB): `.asistentes-grid` · `.asistente-card[.pristino|.pristino-oss|.gem|.catalogo]` · `.badge` · `.cta` · `.anchor-vision` con dark mode + `prefers-reduced-motion` respetado.

## Footer ampliado (P2)

- Versión bumped: `v1.0 · 2026` → `v1.3 · 2026-04-29`
- Score nota: `score 100/100 sobre 9 ejes ponderados`
- Atribución framework: `Framework P.I.V.O.T.E. © MetodologIA · Visión · CC BY-SA 4.0 · uso libre con atribución`
- Visión + comunidad: `metodologia.info`

## Modales actualizados

- **8 nuevos**: `piv-p`, `piv-i`, `piv-v`, `piv-o`, `piv-t`, `piv-e`, `ent-d`, `ent-plus`
- **5 renombrados**: `dsv-d`, `dsv-s1`, `dsv-v`, `dsv-s2`, `dsv-r` ahora dicen `(DSVSR · paso N)` en lugar de plain DSV
- **Total entradas**: 153 → 161
- **JSON file**: 107 KB → 116 KB
- **Embed inline**: sincronizado en `window.modalCardData`

## Verificación post-build

- [x] HTTP 200 + sin errores JS
- [x] 6 cards PIVOTE en 2 fases con `Human First, IA Next` visible y atribución a metodologia.info/vision/
- [x] 10 cards ENTRUSTED+ (9 ejes + plus) renderizadas
- [x] DSVSR íntegro en título § 13
- [x] § 23 Asistentes con 6 cards
- [x] Numeración § 1 → § 24 sin saltos
- [x] Modales `ent-d`, `ent-plus`, `piv-t` abren con título correcto
- [x] Dark mode preserva gold border + contraste WCAG
- [x] `prefers-reduced-motion` apaga hover-translate de pivote-card y asistente-card

## Tamaño

- HTML: 293 KB → **324 KB** (+31 KB · +10%) — dentro del rango planificado
- JSON modales: 107 KB → **116 KB**
- 0 archivos nuevos en runtime (single-file self-contained mantiene)
