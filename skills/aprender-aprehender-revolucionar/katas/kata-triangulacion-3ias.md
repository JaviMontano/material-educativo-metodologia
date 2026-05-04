# Kata · Triangulación 3 IAs · 30 min

> Misma pregunta · 3 IAs distintas · contradicciones = oro. v1.1.0.

| Concepto | Valor |
|---|---|
| Categoría | Aprender · validación de fuentes |
| Tiempo | 30 min |
| Frecuencia | Cada Workflow 1 · cada research crítico |
| Output | Tabla triangulación con veredicto por item · 0 hallucinations confirmadas |
| Pre-requisito | Acceso a 3+ IAs distintas en paralelo |

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §Triangulation Protocol + Prompt #1.
`[DOC]` Cross-validation reduce sesgos individuales · principio de inter-rater reliability (Cohen 1960).

## Contrato

| Hace | No hace |
|---|---|
| Detecta omisiones, sesgos y hallucinations al cruzar 3 IAs | Garantiza verdad · solo aumenta confianza · 4ª capa (Prompt #4) sigue siendo obligatoria |
| Identifica controversias del campo (3 respuestas distintas = oro) | Resuelve la controversia · solo la expone |
| Funciona con 3 IAs entrenadas con datasets diferentes | Funciona si las 3 IAs comparten cross-training (caso raro pero documentado) |

`[LÍMITE]` Si las 3 IAs son derivadas de la misma familia (ej. 3 modelos de OpenAI) · valor cae 70% por sesgo compartido. Mitigación: usa IAs de proveedores distintos (Anthropic + OpenAI + Google + Perplexity).
`[SUPUESTO]` Las 3 IAs tienen información válida sobre el dominio · si el tema es post training cutoff de todas, fallan en común.

## Protocolo · 30 min

### 0:00-0:05 · Preparar pregunta única

Define UNA pregunta clara · idéntica para las 3 IAs:

| Tipo | Ejemplo |
|---|---|
| Mapeo | "¿Cuáles son los N conceptos/autores/papers más importantes en [DOMINIO]? Cita fuentes primarias." |
| Definición | "Define [CONCEPTO] · 2 ejemplos reales de aplicación · trade-offs principales." |
| Controversia | "¿Cuáles son las 3 controversias actuales en [CAMPO]? Argumentos de ambos lados." |

`[CRITERIO-ACEPTACIÓN]` Si la pregunta tiene >3 cláusulas o pide >10 items · divide en sub-preguntas. Triangulación falla con preguntas amplias.

### 0:05-0:20 · Ejecutar en 3 IAs (15 min)

```
- IA #1 (5 min · pegar pregunta · guardar respuesta completa)
- IA #2 (5 min · misma pregunta exacta · guardar)
- IA #3 (5 min · misma · guardar)
```

`[CASO-BORDE]` NO modifiques la pregunta entre IAs · NO refines · NO copies-pegas la respuesta de IA #1 a IA #2. La triangulación válida exige independencia total entre las 3 ejecuciones.

`[TRADE-OFF]` 15 min en paralelo es eficiente · pero si pegas la respuesta #1 al pedirle a IA #2, contaminas. Mejor: 3 ventanas/tabs separadas · sin cross-pollination.

### 0:20-0:30 · Tabla de triangulación

Plantilla en `assets/plantilla-triangulacion.md`:

| Item | IA #1 | IA #2 | IA #3 | Veredicto |
|---|---|---|---|---|
| Concepto A | ✅ | ✅ | ✅ | CONFIRMED · 3/3 |
| Autor X · 2018 | ✅ | ❌ | ✅ | REVISAR · 2/3 |
| Paper Y | ✅ | ❌ | ❌ | SOSPECHOSO · 1/3 |
| Controversia Z | ❌ | ✅ | ✅ | CONFIRMED · 2/3 |

| Veredicto | Frecuencia | Acción |
|---|---|---|
| CONFIRMED | 3/3 | Alta confianza · usar |
| CONFIRMED | 2/3 | Validar fuente primaria antes de uso público |
| SOSPECHOSO | 1/3 | Alta probabilidad hallucination o nicho · validar manual |
| CONTRADICCIÓN | 0/3 acuerdan · cada una dice algo distinto | ORO · debate del campo · documenta como tal |

## Reglas duras

| Regla | Por qué |
|---|---|
| Pregunta IDÉNTICA en las 3 | Sin esto, no es triangulación |
| Captura respuestas COMPLETAS | Las omisiones son los datos · no resumas antes de comparar |
| Contradicciones son ORO | No las descartes · son señales del campo |
| 3+ IAs · NO 2 | Con 2, los empates 1-1 no resuelven |

## Anti-patrones top-3 graves

| # | Anti-patrón | Detección | Antídoto |
|---|---|---|---|
| 1 | "Solo Claude/GPT es confiable" | 1 archivo en la carpeta · BoK monoamarillo | Triangular obligatorio · sin excepción |
| 2 | Modificar pregunta entre IAs | "Refiné la pregunta para IA #2" | Pregunta congelada · IDÉNTICA × 3 |
| 3 | Aceptar 2/3 como verdad final | "2 IAs dicen sí · debe ser cierto" | 2/3 = REVISAR · validar fuente primaria antes de uso público |

## Output esperado por caso

| Caso | Coincidencia | Diagnóstico |
|---|---|---|
| A · alta | 80%+ items 3/3 | BoK confiable · proceder · Prompt #4 confirmatorio |
| B · media | 50-80% items | BoK útil · áreas REVISAR documentadas · Prompt #4 obligatorio |
| C · baja | <50% acuerdo | Tema controversial (oro) O nicho (hallucinations probables) · investigar manual |

`[CASO-BORDE]` Si los 3 dan respuestas casi idénticas (>90% overlap textual) · sospecha cross-training · mitigación: 4ª IA de familia distinta (Kimi, Mistral, especializado de dominio).

## Combo obligatorio · Prompt #4

Después de triangular · ejecuta Prompt #4 (Cross Fact-Check) en 4ª IA:
- Pegar las 3 respuestas
- Pedir veredicto por claim
- Eliminar HALLUCINATIONS confirmados

`[CRITERIO-ACEPTACIÓN]` Triangulación SIN Prompt #4 = trabajo a la mitad. Las 3 IAs pueden compartir hallucination · solo la 4ª capa lo detecta.

## Métricas de éxito

```
[ ] 3 IAs distintas (idealmente proveedores distintos)
[ ] Pregunta idéntica · capturas completas
[ ] Tabla triangulación con veredicto por item
[ ] CONTRADICCIONES marcadas como oro (no descartadas)
[ ] Prompt #4 ejecutado sobre el output consolidado
[ ] 0 HALLUCINATIONS críticas en el BoK final
```

## Cuándo aplicarlo

- ✅ Cada Workflow 1 (paso 1:00-2:00)
- ✅ Cada research crítico (>2h impacto downstream)
- ✅ Pre-cita pública en QBR/paper
- ❌ NO para chat trivial (sobreuso = fricción innecesaria)

## Referencias cruzadas

- `prompts/01-research-blueprint.md`
- `prompts/04-cross-fact-check.md`
- `references/04-anti-patrones-y-trampas.md` §Single-AI BoK
- `agents/auditor-cruzado.md`
- `assets/plantilla-triangulacion.md`

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · `[FUENTE-PRIMARIA]` Playbook v2.0.0
