# Kata · Recuperación Ciega · 15 min

> Cierra todo · escribe de memoria · marca tus gaps. v1.1.0.

| Concepto | Valor |
|---|---|
| Categoría | Aprehender · técnica Retrieval Practice |
| Tiempo | 15 min Sprint · 5 min Express · 60 min Marathon |
| Frecuencia | Diaria en Workflow 3 · ≥1× / sem en mantenimiento |
| Output | Auto-eval con ratio FUERTE/PARCIAL/DÉBIL · 2-3 gaps documentados |
| Distingue | Recall productivo (lo sabes) vs Recognition (lo identificas) |

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §Katas + Retrieval Practice (Roediger & Karpicke 2006, *Psychological Science* 17).
`[DOC]` Testing effect: el acto de recuperar fortalece el aprendizaje más que la re-exposición pasiva. Bjork (2011, *Make It Stick* cap.3).

## Contrato

| Hace | No hace |
|---|---|
| Distingue lo que SABES (recall) de lo que RECONOCES (recognition) | Reemplaza el estudio inicial · si nunca lo viste, no recuperas |
| Detecta el "Espejismo de Fluidez" antes del QBR/cert | Garantiza retención largo plazo · eso requiere Spaced Repetition |
| Genera gaps específicos para el plan de estudio siguiente | Evalúa profundidad de comprensión (eso es Feynman) |

`[LÍMITE]` Conceptos puramente procedurales (ej. tocar piano, soldar) NO se recuperan en hoja en blanco. Esos requieren práctica kinestésica.
`[SUPUESTO]` Tienes ya el concepto en glosario · al menos 1 sesión de estudio previa.

## Protocolo · 15 min Sprint

### 0:00-0:01 · Setup brutal

```
1. CIERRA TODO sin excepción:
   - Notas · libros · tabs del navegador
   - NotebookLM · IAs paralelas
   - Notion · Obsidian · Roam
2. Hoja en blanco / documento nuevo
3. Decide UN concepto a recuperar
4. Timer 10 min visible
```

`[CRITERIO-ACEPTACIÓN]` 1 tab del tema abierta = kata fallido. Reset · cerrar todo · empezar.

### 0:01-0:11 · Recuperación (10 min)

Escribe TODO lo que recuerdes:

| Aspecto | Pregunta |
|---|---|
| Definición | ¿Qué es? |
| Importancia | ¿Por qué importa? |
| Relaciones | ¿Cómo se conecta con conceptos vecinos? |
| Ejemplos | 2-3 casos concretos |
| Trade-offs | Costos del concepto |
| Límites | ¿Cuándo NO aplica? |
| Atribución | Autor / fuente que asocias |

**Sin parar · sin volver atrás · sin abrir nada.** Si te trabas, escribe `[?]` y sigue.

`[CASO-BORDE]` Si escribes >10 `[?]` en los primeros 5 min · el concepto NO está en estado recuperable · interrumpe · plan: re-estudiar antes de re-kata.

### 0:11-0:14 · Auto-evaluación rápida (3 min)

Lee lo que escribiste · marca cada elemento:

| Tag | Significado | Frecuencia esperada |
|---|---|---|
| ✅ FUERTE | 90%+ seguro · de memoria | Target ≥60% |
| 🟡 PARCIAL | Concepto OK · faltan detalles | Aceptable ≤30% |
| ❌ DÉBIL | `[?]` o probablemente mal | Bandera roja >10% |

### 0:14-0:15 · Comparación (1 min)

Abre la fuente original (notas / paper / NotebookLM):

```
Para cada elemento:
- ¿Lo que escribiste coincide?
- ¿Faltó algo crítico?

Documenta los 2-3 gaps más importantes.
```

`[TRADE-OFF]` La tentación de "verificar a la mitad" es alta · NO lo hagas. La sorpresa de comparar al final es el dato más valioso del kata.

## Reglas duras

| Regla | Por qué |
|---|---|
| Cierra TODO sin excepciones | Si tienes 1 tab abierta, ya no es recall · es recognition disfrazado |
| Sin parar 10 min | La presión continua es el ejercicio |
| No mires hasta minuto 14 | La sorpresa final = dato más valioso |
| Comprometete · `[?]` si dudas | "Yo creo que es..." sin commitment = no recall |

## Anti-patrones top-3 graves

| # | Anti-patrón | Detección | Antídoto |
|---|---|---|---|
| 1 | Mirar notas durante recuperación | "Solo verificar 1 cosita" | Cierra TODO · si miraste, kata fallido · reset |
| 2 | Saltar comparación final | "Total, ya escribí lo que sé" | Comparación es donde APRENDES · paso obligatorio |
| 3 | No documentar gaps | "Lo recordaré" | Bitácora obligatoria · sin esto pierdes el dato |

## Output esperado por caso

| Caso | Ratio FUERTE | Diagnóstico | Acción |
|---|---|---|---|
| A · fuerte | ≥60% FUERTE · pocos `[?]` | APREHENDIDO · gaps son detalles | Spaced Repetition · día 7 |
| B · parcial | 30-60% FUERTE · varios `[?]` | Conceptual sin profundidad | Estudiar gaps específicos · re-kata 3 días |
| C · débil | <30% FUERTE · muchos `[?]` | Recognition disfrazado · Espejismo de Fluidez | Re-Workflow 2 sobre concepto · NO pasar a Workflow 3 |

`[CASO-BORDE]` Si tras 3 katas en 3 semanas el ratio FUERTE no sube · cambia técnica · prueba Elaboration o Feynman · puede ser que retrieval solo no fija para ese tipo de concepto.

## Variantes

| Modo | Tiempo | Trade-off |
|---|---|---|
| **Express** | 5 min · 1 concepto · 3 min recall + 2 min comparar | Útil daily · NO suficiente diagnóstico profundo |
| **Sprint** | 15 min · default | Balance recuperación + auto-eval + comparación |
| **Marathon** | 60 min · subtema completo (5+ conceptos) | 30 min recall · 15 min auto-eval · 15 min comparar + plan |

## Métricas de éxito (4 semanas)

```
[ ] Ratio FUERTE mejora semana a semana
[ ] Tiempo entre kata y "recall fluido" se reduce
[ ] Detectas Espejismo de Fluidez antes de QBR/cert
[ ] Bitácora con gaps específicos por sesión
[ ] Plan reparación derivado de gaps · ejecutado
```

`[CRITERIO-ACEPTACIÓN]` Si ratio FUERTE cae 2 sesiones consecutivas · alerta · revisar dieta de estudio (probablemente recognition pasivo en exceso).

## Cuándo aplicarlo

- ✅ Cada día durante Workflow 3 intensivo
- ✅ Como inicio de `ritual-aprehension-semanal.md`
- ✅ Pre-presentación / cert / interview · 7 días antes
- ✅ Cada vez que sientas "ya entendí" (validar · no creer)
- ❌ NO en concepto recién leído (necesita 24h antes para ser recall, no echo memory)

## Referencias cruzadas

- `references/01-seis-tecnicas-cognitivas.md` §Retrieval Practice
- `references/04-anti-patrones-y-trampas.md` §Recognition vs Recall
- `references/06-ciencia-cognitiva-fuentes.md` §1 (testing effect)
- `rituals/ritual-aprehension-semanal.md`
- `rituals/ritual-curiosidad-diaria.md`

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · `[FUENTE-PRIMARIA]` Playbook v2.0.0
