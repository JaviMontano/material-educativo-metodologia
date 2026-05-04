# Kata · Feynman a Novato · 30 min

> Explica a niño de 12 años. Donde uses jerga, ahí está el gap. v1.1.0.

| Concepto | Valor |
|---|---|
| Categoría | Aprehender · técnica Feynman |
| Tiempo | 30 min Sprint · 10 min Express · 60 min con humano real |
| Frecuencia | ≥1× / semana en Workflow 3 · pre-evento crítico |
| Output | Audio 2-3 min sin jerga · veredicto APREHENDIDO/PARCIAL/NO |
| Pre-requisito | Concepto está en tu glosario activo (no concepto nuevo) |

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §Katas + Feynman (1985, *Surely You're Joking, Mr. Feynman!*).
`[DOC]` Eficacia confirmada en self-explanation studies (Chi et al. 1989, *Cognitive Science* 13).

## Contrato

| Hace | No hace |
|---|---|
| Detecta jerga residual sin sustento conceptual | Garantiza que la audiencia REAL entienda (eso requiere humano · §Marathon) |
| Distingue fluidez (recognition) de comprensión (recall productivo) | Reemplaza el estudio del concepto · si no lo sabes, Feynman expone, no enseña |
| Genera analogías que sirven luego en QBR/cert | Funciona para conceptos kinestésicos / muy formales (matemática avanzada) |

`[LÍMITE]` Conceptos formalizados con notación matemática densa (ej. lambda calculus, teoremas de Gödel) NO se simplifican a niño 12. La jerga es el concepto. Variante: explicar la *intuición* del concepto, no el formalismo.
`[LÍMITE]` La validación última requiere un humano real · no la IA. Si solo iteras con IA, puedes auto-engañarte.

## Protocolo · 30 min Sprint

### 0:00-0:05 · Setup

```
1. Elige 1 concepto que crees dominar (ya está en glosario)
2. Audiencia: niño 12 años · inteligente · sin jerga técnica
3. Hoja en blanco / grabadora · CIERRA todas notas / IA / Notebook
4. Timer 25 min visible
```

`[CRITERIO-ACEPTACIÓN]` Si el concepto NO está en tu glosario · NO es Feynman · es estudio inicial. Cierra el kata · pasa a Workflow 1.

### 0:05-0:15 · Primer intento (10 min)

Escribe la explicación · 3 minutos sin parar · audiencia niño 12 · sin jerga · con analogías cotidianas. Si te trabas, marca `[?]` y sigue.

`[CASO-BORDE]` Si te trabas en los primeros 30 segundos y escribes >5 [?] en 3 min · DETÉN el kata · concepto no está en glosario activo · regresa a Workflow 2 (técnica Elaboration sobre ese concepto).

### 0:15-0:20 · Auto-revisión (5 min)

Marca cada palabra/frase con tag:

| Tag | Significado | Acción |
|---|---|---|
| `[JERGA]` | Palabra técnica sin definir | Reemplaza con analogía |
| `[VAGO]` | Concepto superficial | Concretiza con número/ejemplo |
| `[FLUIDO]` | Claro y accesible | Mantener |
| `[ANALOGÍA]` | Metáfora cotidiana exitosa | Reforzar (más así) |

### 0:20-0:25 · Iteración (5 min)

Para cada `[JERGA]` y `[VAGO]` · reescribe con analogía cotidiana. Si la jerga es inevitable (ej. "API"), defínela ANTES de usarla con metáfora.

### 0:25-0:30 · Test final · audio (5 min)

Lee en voz alta · graba · escucha. Verdict:

| Síntoma | Veredicto |
|---|---|
| Fluye natural · 0 jerga residual · 2-3 min | ✅ APREHENDIDO |
| Fluye pero 1-2 jergas residuales | 🟡 PARCIAL · iterar 1× más |
| Tropiezos / incoherencia / >5 min | ❌ NO APREHENDIDO · re-Workflow 2 |

`[CRITERIO-ACEPTACIÓN]` APREHENDIDO requiere los 3: fluidez audio + 0 jerga + duración 2-3 min. Falla 1 → no APREHENDIDO.

## Reglas duras

| Regla | Antídoto |
|---|---|
| Audiencia es **niño 12 años** | NO "junior técnico" · NO "estudiante pregrado". Si necesita más sofisticación, NO es Feynman. |
| Analogías de **vida cotidiana** | "Caché es la mesa de tu cocina" ✅ vs "caché optimiza access pattern locality" ❌ |
| Si jerga es inevitable, **definir ANTES** | "Una API es una puerta · ahora voy a usar la palabra API..." ✅ |
| Si dura **>3 min** · simplifica | Niños 12 no escuchan 10 min · sobrecarga indica gap |

`[TRADE-OFF]` Insistir en niño 12 puede dolerle al ego del experto · esa es la señal. La incomodidad de simplificar es exactamente lo que te muestra la jerga vacía.

## Anti-patrones top-3 graves

| # | Anti-patrón | Detección | Antídoto |
|---|---|---|---|
| 1 | Audiencia "junior técnico" | Permite jerga · sigue sintiéndote experto | Niño 12 no negociable · jerga prohibida |
| 2 | Sin grabar audio | Crees que fluye · no detectas tropiezos | Audio obligatorio · escuchar 24h después |
| 3 | Iterar solo con IA · saltar humano real | Pasas el kata pero fallas en QBR real | §Marathon con humano · mínimo 1× pre-evento crítico |

## Variantes

| Modo | Tiempo | Trade-off |
|---|---|---|
| **Express** | 10 min | 1 sola iteración · útil para validación rápida · NO suficiente pre-QBR |
| **Sprint** | 30 min | Default · auto-evaluación + 1 iteración + audio |
| **Marathon humano** | 60 min | Feedback humano real · detecta lo que IA no detecta · obligatorio pre-evento crítico |

### Marathon · 60 min con humano real

```
0:00-0:30 · Sprint completo (audio)
0:30-0:45 · Explicar en vivo a colega que NO conoce el tema
0:45-0:55 · Feedback honesto · 3 preguntas:
   - "¿En qué punto te perdí?"
   - "¿Qué término no entendiste?"
   - "¿Cuál analogía funcionó · cuál no?"
0:55-1:00 · Iterar basado en feedback · 2da pasada con humano distinto si tiempo
```

`[CASO-BORDE]` Si humano real dice "todo claro" pero NO te repreguntó nada · bandera amarilla · pidió ser amable · pídele preguntas hostiles explícitamente.

## Métricas de éxito

```
[ ] Audio fluye sin tropiezos (0 "ehm" más de 3×)
[ ] 0 jerga residual sin definir antes de usar
[ ] ≥2 analogías cotidianas exitosas
[ ] Duración 2-3 min (no más, no menos)
[ ] Si Marathon: humano entiende sin pedir aclaración
```

`[CRITERIO-ACEPTACIÓN]` 5/5 obligatorio para declarar APREHENDIDO. 4/5 = PARCIAL · iterar 1×.

## Cuándo aplicarlo

- ✅ Cada semana en `ritual-aprehension-semanal.md`
- ✅ Antes de QBR / cert / interview · mínimo 7 días antes
- ✅ Después de Workflow 1 · validar que conceptos del glosario son recall, no recognition
- ❌ NO aplicar a concepto recién aprendido (no está en glosario activo)

## Output esperado · ejemplo

**Concepto**: Eventual Consistency.

**Intento 1 (con jerga)**: "Eventual consistency es un modelo donde los nodos del sistema convergen al mismo estado eventualmente, después de un período de propagación. Es trade-off del CAP theorem que sacrifica strong consistency por availability."
→ `[JERGA]` × 7: modelo, nodos, convergen, trade-off, CAP, strong consistency, availability.

**Iteración 1 (con analogías)**: "Imagina 3 amigos en distintas ciudades · todos llevan el mismo cuaderno con tus notas. Cuando agregas algo en una ciudad, los 3 cuadernos no se actualizan al instante. Hay un momentito donde uno tiene la nota nueva y los otros 2 no. Pero después de unos segundos, los 3 quedan iguales otra vez. Eso es 'eventual consistency': eventualmente todos se ponen al día, pero no al instante."
→ `[ANALOGÍA]` × 3: amigos en ciudades, cuadernos, "momentito" · 0 jerga sin definir.

**Iteración 2 (audio)**: graba · si fluye natural · 2:30 min · APREHENDIDO.

## Referencias cruzadas

- `references/01-seis-tecnicas-cognitivas.md` §Feynman
- `references/06-ciencia-cognitiva-fuentes.md` §3 (self-explanation)
- `agents/coach-aprehender.md`
- `prompts/02-coach-system-prompt.md`
- `rituals/ritual-aprehension-semanal.md`

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · `[FUENTE-PRIMARIA]` Playbook v2.0.0
