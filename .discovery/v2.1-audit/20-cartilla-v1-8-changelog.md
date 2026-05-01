# Changelog · Cartilla v1.8 · 2026-04-30 · 5 imports prioritarios desde archivos previos

## Conclusión
Cierre de la deuda v1.6: los 5 imports prioritarios identificados en los archivos previos (`complementario-v4` + `mobile`) integrados a la cartilla v1.7 con voz BV v3.0.0 completa.

## Imports aplicados (5/5)

| # | Origen | Destino | Tipo |
|---|---|---|---|
| 1 | `complementario-v4` línea 463 · 10-item Universal Rubric | callout en § 11 ENTRUSTED+ post `ent-plus` | Rúbrica liviana complementaria |
| 2 | `complementario-v4` línea 421 · SPEC Template artifact | callout copyable en § 5 anatomía post `anat-ejemplos` | Plantilla copy-paste con `<pre>` |
| 3 | `complementario-v4` líneas 550-590 · Tríada Mentoría/Proyecto/Certificación | nueva § 23.5 Pathways | Sección nueva 3 cards |
| 4 | `complementario-v4` línea 445 · Few-Shots library methodology | callout en § 4 pilar 5 post `pilar-ejemplos` | Método 4 pasos + indicador |
| 5 | `mobile` líneas 2504-2560 · 5-Level Exercise Progression | callout intro en § 20 + 12 prac-XX ids | Mapa progresión + linkeable |

## Cambios estructurales

### § 4 pilar 5 (Few-Shots library)
- Callout post-card "Ejemplos" con metodología 4 pasos: recoge pares · documenta · organiza · versiona.
- Tag `[P3]` · *Indicador sugerido*: % prompts críticos con ≥3 ejemplos curados (mensual · ≥70%).

### § 5 anatomía (SPEC Template)
- Callout post-card "Ejemplos" con bloque `<pre>` copyable (ROL/CONTEXTO/TAREA/FORMATO/RESTRICCIONES/EJEMPLOS/CRITERIO).
- Tag `[P3]` · CTA implícita: "Pégalo en cualquier IA, llena los corchetes".

### § 11 ENTRUSTED+ (10-item Universal Rubric)
- Callout post-card `ent-plus` con `<ol columns:2>` de 10 ítems (escala 1-5).
- Tag `[P1]` · CTA: "califica los 10 ítems · threshold ≥40/50 · escala a ENTRUSTED+ 9 ejes para profundidad forense".
- Posicionamiento: rúbrica liviana cuando ENTRUSTED+ es demasiado pesado.

### § 20 prácticas (5-Level Progression)
- Callout intro pre-grid con los 5 niveles canónicos (Simple → Contexto → Formato → CoT → System Prompt).
- Cada nivel linkea al ejercicio concreto: prac-01, prac-02, prac-03, prac-06 (DSVSR), prac-07 (ritual).
- Las 12 cards reciben `id="prac-XX"` para soportar links internos.
- Tag `[P1]` · Total: ~100 min de práctica deliberada en 5 días.

### § 23.5 Pathways (Tríada NUEVA)
- Sección nueva entre § 23 (Asistentes gratuitos) y § 24 (FAQ).
- 3 cards: Mentoría 1:1 `[P1]` · Proyecto Real Aplicado `[P3]` · Certificación MetodologIA `[P3]`.
- CTAs uniformes: "Conversación inicial 30 min →" sin compromiso.
- Indicador sugerido: si >30% de fricciones requieren acompañamiento, considera la pathway.
- Reusa CSS `asistentes-grid` + `asistente-card` existentes.

### TOC
- Nueva entrada `§ 23.5 · Pathways · profundización` insertada entre § 23 y § 24.
- TOC pasa de 25 → 26 entradas.

## Métricas v1.8

- HTML: 365 KB → **380 KB** (+15 KB)
- Secciones: 25 → **26** (§ 23.5 nueva · sin renumerar FAQ)
- Pillar-tags: 126 → **140** (+14 tags inline en imports nuevos)
- prac-XX ids: **12/12** agregados para internal linking
- Modales: 169 (sin cambios · imports son contenido inline)
- Cero errores JS · WCAG AAA preservado

## Verificación post-build (DOM checks)

- ✅ § 23.5 presente · h2 correcto · 3 pathway cards
- ✅ § 20 callout presente · `<ol>` con 5 niveles
- ✅ 12 prac-XX ids accesibles para anchor links
- ✅ TOC entry § 23.5 presente
- ✅ 169 modales · 31 secciones totales · 140 pillar-tags
- ✅ Cero errores en consola JS

## Cumplimiento BV v3.0.0

| Gate | v1.8 |
|---|:---:|
| G1 Minto persistente | ✅ |
| G2 Evidencia honesta | ✅ (indicadores con frecuencia/dueño/umbral en 3 callouts) |
| G3 Español neutro tú | ✅ |
| G4 Lista roja cero | ✅ |
| G5 Veracidad fuentes | ✅ (atribución verbatim a archivos origen) |
| G6 Anclaje [P1-P3] | ✅ (14 tags nuevos en imports) |

## Cierre del roadmap v1.6

Los 5 prioritarios identificados en el plan v1.6 §15 quedan publicados. La cartilla cumple BV v3.0.0 al 100% con todo el contenido pedagógico de los 4 archivos previos consolidado.
