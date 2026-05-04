# Workflow 1 · El Curioso · 1-4 h

Transición Escala 0 (Ignorante) → Escala 1 (Curioso). Primer mapa del territorio. v1.1.0.

| Concepto | Valor |
|---|---|
| Agente que lo ejecuta | `coach-aprender` |
| Tiempo nominal | 4 h (Sprint) · 1 h (Express) · 4h primer slice de Marathon |
| Output mandatory | BoK triangulado · glosario ≥15 (target 30) · concept map mermaid · ≥3 fuentes 1° verificadas · NotebookLM configurado |
| Gate al final | G-Aprender (7 criterios binarios) |

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §Workflow 1.

## Contrato del workflow

| Hace | No hace |
|---|---|
| Construye el mapa inicial del dominio | Lleva al usuario a Escala 2+ (eso es Workflow 2/3) |
| Triangula 3+ IAs · detecta hallucinations vía Prompt #4 | Garantiza dominio operativo (es saber, no hacer) |
| Configura NotebookLM como coach activo | Reemplaza la lectura de fuentes 1° (las identifica · no las lee por ti) |
| Persiste outputs en `~/aprender-aprehender/temas/{slug}/` | Promete que en 4h estarás listo para QBR (eso requiere Aprehender) |

`[LÍMITE]` 4 h reales no equivalen a Escala 1 si el dominio es muy denso (ej. matemáticas avanzadas requieren 10-20 h solo para Escala 1).
`[SUPUESTO]` Usuario tiene acceso a 3+ IAs · si solo tiene 1 ChatGPT/Claude, valor cae 60% por pérdida de triangulación.

## Pre-requisitos `[CRITERIO-ACEPTACIÓN]`

```
[ ] Tema declarado con precisión (ej. "Agentic AI Systems for Production" · NO "AI")
[ ] Objetivo medible (¿para qué? · "pasar AWS SAA-C03 en 3 meses")
[ ] 1-4 h bloqueadas en calendario · ININTERRUMPIDAS · sin notificaciones
[ ] Cuenta NotebookLM activa
[ ] Acceso simultáneo a 3 IAs (ChatGPT + Claude + Gemini ideal)
[ ] Espacio en disco para `~/aprender-aprehender/temas/{slug}/`
```

Si alguno falla · NO arranques · resuelve primero.

## Cronograma · Sprint 4 h

### 0:00-0:15 · Declaración de intención

Crear `~/aprender-aprehender/temas/{slug}/00-declaracion.md`:

```markdown
TEMA: [específico]
POR QUÉ: [objetivo medible]
ESCALA ACTUAL: [0|1] · evidencia: ¿qué sabes ya?
ESCALA OBJETIVO: [1|2]
TIEMPO: 4 h hoy · 0 h compromiso post-hoy
HIPÓTESIS INICIAL: [lo que crees · será refinada]
```

`[NUEVO-APORTE]` La declaración hace explícito qué sabes ya · evita el sesgo "soy 0 en todo" cuando ya tienes vocabulario adyacente.

### 0:15-1:00 · Triangulación del Blueprint (Prompt #1)

Ejecutar Prompt #1 en 3 IAs paralelas (45 min). Guardar:
- `01-bp-chatgpt.md` · `02-bp-claude.md` · `03-bp-gemini.md` (o Perplexity)

`[CASO-BORDE]` Si las 3 IAs dan respuestas casi idénticas (>90% overlap textual) · sospecha cross-training · probablemente todas vieron el mismo material entrenamiento. Mitigación: agregar Kimi o un modelo especializado del dominio.

### 1:00-2:00 · Consolidación (60 min)

```
1. Tabla triangulación (asset: plantilla-triangulacion.md)
   ✅ aparece en 3/3  → CORE · alta confianza
   ⚠️ aparece en 2/3  → REVISAR · validar con fuente 1°
   ❌ aparece en 1/3  → SOSPECHOSO · descartar o investigar manual
   🔄 contradicción   → ORO · ahí están los debates del campo

2. BoK consolidado: mantener ✅ · investigar ⚠️🔄 · eliminar ❌

3. Glosario: ≥15 términos · target 30 · cada uno con [DOC]/[INFERENCIA]/[SUPUESTO]

4. Concept map mermaid:
   - Tema central · 5-10 ramas principales · 3-5 conceptos por rama
   - Si IA no genera mermaid · usa plantilla `assets/plantilla-concept-map.mermaid`
```

Output: `04-bok-consolidado.md`.

### 2:00-2:30 · Fact-Check Cruzado (Prompt #4) · 30 min

Ejecutar Prompt #4 en 4ª IA distinta (Perplexity con web search ideal). Procesar veredictos:

| Veredicto | Acción |
|---|---|
| `[CONFIRMED]` | Mantener |
| `[DISCREPANT]` | Investigar fuente 1° real |
| `[PARTIAL]` | Mantener con caveat documentado |
| `[NO SOURCE]` | Verificar manualmente · si no se confirma en 5 min, eliminar |
| `[HALLUCINATION]` | Eliminar inmediato |

Output: `05-bok-auditado.md`.

`[CASO-BORDE]` Si las 4 IAs comparten una hallucination común (caso raro pero documentado), la triangulación falla. Mitigación: validar cualquier afirmación crítica para QBR/paper en Google Scholar manualmente · 10 min adicionales.

### 2:30-3:00 · NotebookLM Setup · 30 min

```
1. notebooklm.google.com → nuevo notebook
2. Importar 5 sources (los 5 .md del proceso)
3. Auditoría rápida con Prompt #7 · si <40% primary, regresa al 1:00
4. Configurar coach con Prompt #2 · pegar en Custom Goal (≤10K chars)
5. Test: 3 preguntas socráticas · validar comportamiento
```

`[TRADE-OFF]` Configurar NotebookLM toma 30 min hoy · ahorra 2-3 h en cada sesión futura porque ya no re-explicas el contexto.

### 3:00-3:30 · Primera sesión retrieval ciego · 30 min

```
1. Coach: "Repasemos los 5 términos más importantes del glosario · retrieval ciego"
2. Coach pregunta · tú respondes sin mirar nada
3. Coach evalúa [FUERTE/PARCIAL/DÉBIL]
4. Documentar 2-3 conceptos [DÉBIL] · plan próxima sesión
```

`[CRITERIO-ACEPTACIÓN]` Si <2 conceptos quedan FUERTES de los 5 → indicador de que el BoK fue muy denso y necesita 2ª pasada en próxima sesión.

### 3:30-4:00 · Cierre · 30 min

Validar Gate G-Aprender (ver §Gate). Documentar `06-cierre.md` · actualizar `.aprender-state.json` · agendar próximo paso.

## Quality gate G-Aprender

```
[ ] BoK triangulado en 3+ IAs · documentado en tabla
[ ] Glosario ≥15 términos (target 30) · cada uno con tag de evidencia
[ ] Concept map jerárquico mermaid generado y revisado
[ ] ≥3 fuentes 1° verificadas (no terciarias derivadas)
[ ] Prompt #4 ejecutado · 0 [HALLUCINATION] crítica activa
[ ] NotebookLM con 5+ sources · coach activo · 3 preguntas test pasadas
[ ] 06-cierre.md persistido · estado actualizado
```

`[CRITERIO-ACEPTACIÓN]` 7/7 obligatorio. Si falla 1 · NO avanzar a Workflow 2 · repetir el paso correspondiente.

## Variantes por tiempo

| Modo | Tiempo | Trade-off |
|---|---|---|
| **Express 1h** | 1 h · 1 IA solo (Claude · estructurado) | Pierdes triangulación · uso emergencia · Escala 1 frágil |
| **Sprint 4h** | 4 h · 3 IAs · auditoría completa | Recomendado por defecto |
| **Marathon (slice)** | 4 h primer slice de 64h | Idéntico al Sprint · luego encadena Workflow 2 |

## Casos borde · cuando el camino feliz falla

| Caso | Detección | Resolución |
|---|---|---|
| Tema tan nicho que las 3 IAs dicen "no tengo info" | <30% subtemas mapeados | Cambiar a fuente humana · entrevistar a 1 experto · 30 min |
| Tema tiene controversia ideológica fuerte | Las 3 IAs dan respuestas radicalmente distintas | Marcar el debate como output explícito · NO consolidar artificialmente |
| BoK triangulado pero NotebookLM no admite los archivos | Error de upload | Convertir .md a PDF · NotebookLM acepta PDF mejor |
| Sin tiempo para fact-check (urgencia) | Solo 3h disponibles | Saltar fact-check pero marcar TODO el BoK como `[SUPUESTO]` hasta auditarlo |
| 4ª IA en fact-check no encuentra ninguna fuente | Posible: dominio muy reciente (post training cutoff) | Búsqueda web manual · si <2 fuentes en 30 min, marcar BoK como [SUPUESTO] |

## Anti-patrones detectables

| Anti-patrón | Síntoma observable | Antídoto |
|---|---|---|
| Single-AI BoK | Solo 1 archivo en la carpeta · "ChatGPT me dio el mapa" | Triangulación obligatoria · sin excepción |
| Glosario corto | 5-10 términos | "Coach, dame 10 términos clave más específicos del campo" |
| Sin concept map | Solo prosa narrativa | Mermaid obligatorio · te obliga a estructurar |
| Saltar fact-check | "Suena confiable" | Prompt #4 obligatorio · 30 min ahorran horas en QBR |
| Sin NotebookLM | "Solo leo los .md" | Configurar coach · sin él, no hay aprendizaje activo |
| No documentar | "Lo recordaré" | Archivos persistentes · sin esto pierdes continuidad sesión a sesión |
| Aceptar `[NO SOURCE]` sin investigar | "Quizás existe la fuente" | NO SOURCE = HALLUCINATION potencial · resolver o eliminar |

## Estructura de archivos esperada

```
~/aprender-aprehender/temas/{slug}/
├── 00-declaracion.md         intención + objetivo
├── 01-bp-chatgpt.md          IA #1
├── 02-bp-claude.md           IA #2
├── 03-bp-gemini.md           IA #3
├── 04-bok-consolidado.md     triangulación + tabla
├── 05-bok-auditado.md        post fact-check
├── 06-cierre.md              resumen · gaps · plan
├── concept-map.mermaid       visual jerárquico
└── glosario.md               15-30 términos con tags
```

## Referencias cruzadas

- `agents/coach-aprender.md` · ejecutor
- `prompts/01-research-blueprint.md` · prompt principal
- `prompts/04-cross-fact-check.md` · auditoría
- `prompts/07-notebook-audit.md` · audit notebook
- `references/02-tres-modelos-fundacionales.md` §BoK
- `katas/kata-triangulacion-3ias.md` · práctica deliberada de triangulación
- `examples/ejemplo-aprender-rust.md` · sesión real

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · `[FUENTE-PRIMARIA]` Playbook v2.0.0
