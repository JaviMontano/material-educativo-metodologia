# Prompt #7 · Auditoría de Sources de NotebookLM

> Clasifica las sources de tu notebook en 1°/2°/3° y recomienda eliminar redundantes, consolidar similares, investigar contradicciones.

**Fase**: cross-fase · gestión de notebook
**Cuándo**: cada 5+ sources nuevas, antes de configurar coach
**IA recomendada**: Claude (estructurado) o ChatGPT-4

---

## Cuándo usarlo

- ✅ Después de cargar 5+ sources nuevas en NotebookLM
- ✅ Antes de configurar el coach final con Prompt #2
- ✅ Cuando el coach está dando respuestas inconsistentes (probable: sources contradictorios)
- ✅ Al cerrar Workflow 2 antes de Workflow 3

## Cuándo NO usarlo

- ❌ Notebook con <5 sources (no hay material para auditar)
- ❌ Notebook con sources de un solo tipo (todos papers · audit innecesario)

---

## Variables

| Variable | Reemplazar con |
|---|---|
| `[TU TEMA]` | Tema central del notebook |
| `[LISTA DE SOURCES]` | Pegar lista con título + autor + tipo (paper/blog/video/curso) |

---

## El Prompt

```
Eres un bibliotecario académico especializado en [TU TEMA].

Mi notebook NotebookLM contiene las siguientes sources:

[LISTA DE SOURCES]

Quiero que auditer la calidad y composición de mi notebook.

PROTOCOLO DE AUDITORÍA

Para CADA source, clasifica:

NIVEL DE FUENTE
- 1° PRIMARY: documento original donde se publicó por primera vez
  (papers académicos, reportes oficiales, datasets, RFC, patentes,
  libros canónicos del campo)
- 2° SECONDARY: autoridad reconocida que cita y comenta primarias
  (libros de texto reconocidos, reviews académicos, charlas de
  autoridades del campo)
- 3° TERTIARY: material derivado · resumen · divulgación
  (blog posts, artículos de medios, cursos resumidos, videos
  YouTube de no-autoridades)

CALIDAD INDIVIDUAL
Para cada source, evalúa:
- ✅ ÚTIL: aporta info no presente en otras sources del notebook
- 🔄 REDUNDANTE: cubre lo mismo que otra source mejor
- ❓ CUESTIONABLE: contradice otras o tiene problemas (autor sin
  expertise verificable, sin fecha, sin fuentes)
- ❌ ELIMINAR: tertiary cuando ya tienes primary; o low-quality

COMPOSICIÓN DEL NOTEBOOK

Después de evaluar individualmente, evalúa el conjunto:

DIVERSIDAD DE FUENTES
- ¿Cuántas primary vs secondary vs tertiary?
- ¿Diversidad de autores (no solo 1 escuela de pensamiento)?
- ¿Diversidad temporal (no solo papers de 1 año)?

GAPS TEMÁTICOS
Mapea las sources contra los subtemas del campo:
- ¿Qué subtema tiene cobertura completa? ✅
- ¿Qué subtema tiene cobertura parcial? 🟡
- ¿Qué subtema NO está cubierto? ❌

CONTRADICCIONES
Identifica claims donde sources se contradicen:
- "Source A dice X. Source B dice contrario X."
- Recomienda: investigar manualmente, marcar como debate abierto.

RECOMENDACIONES DE ACCIÓN

1. SOURCES A ELIMINAR
   Lista específica + razón (ej. "Source #4 es tertiary derivada
   del paper de Source #2 · redundante").

2. SOURCES A CONSOLIDAR
   Pares/grupos que dicen lo mismo · mantener la mejor.

3. SOURCES A AÑADIR
   Para llenar gaps temáticos · primary preferentemente.
   Sugerencias específicas: "Falta Lamport 1978 sobre orden de
   eventos · esencial para tu BoK".

4. CONTRADICCIONES A INVESTIGAR
   Lista los pares contradictorios · recomienda 1 fuente terciaria
   neutral para arbitraje.

VEREDICTO GLOBAL

Score del notebook como conjunto:
- 🟢 EXCELENTE: ≥60% primary · gaps mínimos · sin contradicciones críticas
- 🟡 BUENO: 40-60% primary · 1-2 gaps · pocas contradicciones
- 🟠 REGULAR: 20-40% primary · gaps importantes · varias contradicciones
- 🔴 POBRE: <20% primary · muchos gaps · contradicciones sin resolver

Si 🔴 o 🟠: NO configurar coach todavía · primero remediar.
Si 🟡: configurar coach con caveats explícitos.
Si 🟢: listo para coach + uso intensivo.

REGLAS

- Sé honesto · no decir "el notebook está bien" si no lo está
- Cita evidence: "El autor X no aparece en Google Scholar como
  autoridad de [TEMA]" antes que "esta source es cuestionable"
- No descartar tertiary automáticamente · puede ser útil para
  intro · solo descartar si redundante con primary
- Idioma: español
```

---

## Cómo aplicarlo

### Paso 1 · Listar sources
En NotebookLM, copia los títulos de tus sources. Para cada uno, identifica:
- Autor
- Tipo (paper / libro / blog / video / curso)
- Año

### Paso 2 · Pegar y ejecutar
Reemplaza `[TU TEMA]` y `[LISTA DE SOURCES]` con tus datos.

### Paso 3 · Procesar resultado
- ELIMINAR: borra de NotebookLM
- CONSOLIDAR: mantén una, elimina la otra
- AÑADIR: busca y agrega los sugeridos
- INVESTIGAR contradicciones: lee ambas sources, decide cuál tiene más peso

### Paso 4 · Re-auditar después de cambios
Si añadiste 5+ sources nuevas, re-ejecuta este prompt.

---

## Output esperado · Ejemplo

```
AUDITORÍA NOTEBOOK · "Sistemas Distribuidos"

SOURCE-BY-SOURCE

#1 "Time, Clocks, and the Ordering of Events" · Lamport · 1978
   Nivel: 1° PRIMARY (paper canónico)
   Calidad: ✅ ÚTIL · fundacional, irreemplazable
   Acción: MANTENER

#2 "Designing Data-Intensive Applications" · Kleppmann · 2017
   Nivel: 2° SECONDARY (autoridad cita primarias)
   Calidad: ✅ ÚTIL · síntesis del campo
   Acción: MANTENER

#3 "5 Distributed Systems Patterns You MUST Know" · Medium blog
   Nivel: 3° TERTIARY (blog divulgativo)
   Calidad: 🔄 REDUNDANTE · cubre lo mismo que Kleppmann pero superficial
   Acción: ELIMINAR

#4 "What is CAP Theorem?" · Random YouTube channel · 2022
   Nivel: 3° TERTIARY (video sin autor verificable)
   Calidad: ❓ CUESTIONABLE · autor sin expertise claro
   Acción: ELIMINAR · reemplazar con Brewer 2000 (primary)

#5 "Dynamo: Amazon's Highly Available Key-Value Store" · DeCandia 2007
   Nivel: 1° PRIMARY (paper Amazon)
   Calidad: ✅ ÚTIL · foundational para eventual consistency
   Acción: MANTENER

COMPOSICIÓN GLOBAL

Distribución actual:
- 1° Primary: 2/5 (40%)
- 2° Secondary: 1/5 (20%)
- 3° Tertiary: 2/5 (40%) ← demasiado tertiary

GAPS TEMÁTICOS:
✅ Time/ordering (Lamport)
✅ Eventual consistency (Dynamo)
❌ FALTA: Consensus (Raft/Paxos) — paper Ongaro & Ousterhout 2014
❌ FALTA: CAP theorem original — Brewer 2000
🟡 PARCIAL: Replicación (cubierta superficialmente en Kleppmann)

CONTRADICCIONES:
- Ninguna detectada con sources actuales

RECOMENDACIONES

1. ELIMINAR: #3 (redundante), #4 (cuestionable)
2. AÑADIR (primary obligatorio):
   - Ongaro & Ousterhout · Raft · 2014
   - Brewer · CAP Theorem · 2000 (PODC keynote)
   - Gilbert & Lynch · CAP formalization · 2002
3. INVESTIGAR: ninguna contradicción crítica

VEREDICTO: 🟠 REGULAR (antes de remediación)
   Después de remediación: 🟢 EXCELENTE
   Acción inmediata: NO configurar coach todavía · primero añadir
   3 papers primary recomendados.
```

---

## Anti-patrones

| Error | Síntoma | Corrección |
|---|---|---|
| Notebook 100% blogs | Coach cita info de baja calidad | Mínimo 50% primary/secondary |
| 1 solo autor | Coach tiene sesgo | Diversifica autores |
| Sources sin fecha | No detectas obsolescencia | Solo sources con fecha clara |
| Saltar audit | Notebook caótico · coach inconsistente | Audit cada 5 sources nuevos |
| Ignorar contradicciones | Coach da respuestas inconsistentes | Investiga y resuelve |

---

## Combo recomendado

```
WORKFLOW 2 · CONSOLIDACIÓN DE NOTEBOOK:

Día 1: Generar Blueprint (Prompt #1) en 3 IAs
Día 2: Deep Research (Prompt #3) sobre subtemas críticos
Día 3: Buscar manualmente papers primary citados
Día 4: Cargar todo en NotebookLM como sources (10-15 items)
Día 5: Prompt #4 (Fact-Check) · eliminar info hallucinada
Día 6: Prompt #7 (este) · auditar composición
Día 7: Remediar según recomendaciones
Día 8: Configurar coach con Prompt #2

Notebook listo para Workflow 3 · 1 semana de setup.
```

---

## Referencias

- `references/02-tres-modelos-fundacionales.md` §Body of Knowledge
- `references/04-anti-patrones-y-trampas.md` §Single-AI BoK
- `prompts/01-research-blueprint.md`
- `prompts/04-cross-fact-check.md`
- `prompts/02-coach-system-prompt.md`

---

> **Prompt #7** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
