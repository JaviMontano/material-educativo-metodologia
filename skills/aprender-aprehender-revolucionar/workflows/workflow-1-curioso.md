# Workflow 1 · El Curioso · 1-4 horas

> Transición Escala 0 (Ignorante) → Escala 1 (Curioso). El primer mapa del territorio.

**Agente**: `coach-aprender`
**Tiempo**: 1-4 horas
**Output**: BoK triangulado · glosario 30 términos · concept map · NotebookLM configurado

---

## Cuándo ejecutarlo

- Tema nuevo · no sabes nada o casi nada
- Primera vez que escuchas el campo
- Inicio de cualquier deep research
- Modo Express del desatraso (4h)

---

## Pre-requisitos

- [ ] Tema declarado (precisión, no "AI", sino "Agentic AI Systems for Production")
- [ ] Objetivo claro (por qué lo aprendes)
- [ ] Tiempo bloqueado en calendario (1-4h ininterrumpidas)
- [ ] Cuenta NotebookLM activa
- [ ] Acceso a 3 IAs (ChatGPT + Claude + Gemini ideal)

---

## Pasos · Cronograma 4h

### 0:00-0:15 · Declaración de intención

```markdown
TEMA: [específico]
POR QUÉ: [objetivo medible · ej. "Pasar AWS SAA-C03 en 3 meses"]
ESCALA ACTUAL: [0 ignorante · 1 curioso]
ESCALA OBJETIVO: [1 curioso · 2 explorador]
TIEMPO TOTAL: 4 horas hoy
HIPÓTESIS INICIAL: [lo que crees · será refinado al final]
```

Guarda en `~/aprender-aprehender/temas/{slug}/00-declaracion.md`.

### 0:15-1:00 · Triangulación del Blueprint (Prompt #1)

```
TAREA: Ejecutar Prompt #1 en 3 IAs en paralelo

1. ChatGPT (15 min)
   - Tomar `prompts/01-research-blueprint.md`
   - Reemplazar variables
   - Ejecutar
   - Guardar respuesta como `01-bp-chatgpt.md`

2. Claude (15 min)
   - Mismo prompt idéntico
   - Guardar como `02-bp-claude.md`

3. Gemini / Perplexity (15 min)
   - Mismo prompt idéntico
   - Guardar como `03-bp-gemini.md`
```

### 1:00-2:00 · Consolidación

```
TAREA: Compilar las 3 respuestas en 1 documento maestro

PASOS:
1. Tabla de triangulación (asset: plantilla-triangulacion.md)
   Para cada elemento del Blueprint, marcar:
   - ✅ aparece en las 3
   - ⚠️ aparece en 2
   - ❌ aparece en 1 (sospechoso)
   - 🔄 contradicción

2. Generar BoK consolidado:
   - Mantener: items ✅
   - Investigar: items ⚠️ y 🔄
   - Eliminar: items ❌ (sin verificación manual)

3. Validar glosario:
   - Mínimo 15 términos
   - Target 30 términos
   - Marcar [DOC] / [INFERENCIA] / [SUPUESTO]

4. Concept map mermaid:
   - Tema central
   - 5-10 ramas
   - 3-5 conceptos por rama
```

Output: `04-bok-consolidado.md`.

### 2:00-2:30 · Fact-Check Cruzado (Prompt #4)

```
TAREA: Auditar el BoK consolidado con una 4ª IA

1. Tomar `prompts/04-cross-fact-check.md`
2. Usar IA distinta (Perplexity con búsqueda web ideal)
3. Pegar BoK consolidado
4. Procesar veredictos:
   - ELIMINAR items HALLUCINATION
   - VERIFICAR items NO SOURCE críticos
   - MANTENER items CONFIRMED
```

Output: `05-bok-auditado.md`.

### 2:30-3:00 · NotebookLM Setup

```
TAREA: Crear notebook con coach activo

1. notebooklm.google.com → Crear notebook nuevo
2. Importar como sources:
   - 01-bp-chatgpt.md
   - 02-bp-claude.md
   - 03-bp-gemini.md
   - 04-bok-consolidado.md
   - 05-bok-auditado.md
3. Auditoría rápida con Prompt #7 (Notebook Audit)
4. Si recomienda eliminar/consolidar → ejecutar
5. Configurar coach con Prompt #2:
   - [TU TEMA] = [tu tema]
   - [TU NIVEL OBJETIVO] = "Escala 2 Explorador"
   - [TU CONTEXTO] = [...]
6. Guardar
```

### 3:00-3:30 · Primera sesión con coach

```
TAREA: Validar coach + cubrir 2-3 conceptos clave

1. Pregunta 1: "Coach, repasemos los 5 términos más importantes
   del glosario. Hazme retrieval ciego de cada uno."
2. Coach hace 5 preguntas abiertas
3. Tú respondes sin mirar nada
4. Coach evalúa [FUERTE/PARCIAL/DÉBIL]
5. Identifica los 2-3 conceptos [DÉBIL] · plan para próxima sesión
```

### 3:30-4:00 · Cierre y planificación

```
GATE G-APRENDER (validar antes de cerrar):
[ ] BoK triangulado en 3+ IAs · sí
[ ] Glosario ≥15 términos · sí
[ ] Concept map mermaid generado · sí
[ ] ≥3 fuentes primarias verificadas · sí
[ ] Auditor cruzado sin HALLUCINATION crítico · sí
[ ] NotebookLM configurado con coach activo · sí

DOCUMENTAR:
- En `~/aprender-aprehender/temas/{slug}/06-cierre.md`:
  - Logros
  - Gaps detectados
  - Próximo paso (Workflow 2 o pausa)
  - Tiempo total invertido
- Actualizar `.aprender-state.json`
- Agendar próxima sesión

DECIDIR:
- ¿Continuar con Workflow 2 (Explorador)? agendar 4h
- ¿Pausa? guardar estado, retomar cuando aplique
- ¿Suficiente con Escala 1? cerrar el tema activo
```

---

## Variantes

### Express · 1 hora (versión condensada)

Solo si Javier tiene tiempo crítico (atraso urgente):

```
0:00-0:20 · Prompt #1 en 1 IA (Claude · más estructurado)
0:20-0:30 · Glosario rápido · 15 términos clave
0:30-0:40 · Concept map mermaid simple
0:40-0:50 · NotebookLM con 1 source · coach básico
0:50-1:00 · Documentar
```

Trade-off: pierdes triangulación · uso solo en emergencia.

### Sprint · 4 horas (versión recomendada)

Workflow descrito arriba.

### Marathon (parte 1 de 64h)

Este workflow es el primer fragmento de 4h del programa de 64h.

---

## Quality gate G-Aprender

Para avanzar a Workflow 2:

```
✅ BoK con ≥5 subtemas mapeados
✅ Glosario ≥15 términos (target 30)
✅ Concept map jerárquico (mermaid)
✅ Triangulación documentada (3+ IAs)
✅ Fact-check ejecutado (Prompt #4)
✅ NotebookLM con sources cargados + coach activo
✅ Primera sesión con coach exitosa (5 preguntas test)
```

Si falla algún ✅ → repetir el paso correspondiente antes de avanzar.

---

## Anti-patrones

| Error | Síntoma | Corrección |
|---|---|---|
| Solo 1 IA | "Tengo el BoK · ChatGPT lo dio" | Triangular obligatorio |
| Glosario corto | 5-10 términos | Mínimo 15 · si IA da menos, pídele más |
| Sin concept map | Solo prosa | Generar mermaid · obligatorio |
| Saltar fact-check | "Suena confiable" | Prompt #4 obligatorio |
| Sin NotebookLM | Solo lectura | Configurar coach · es activo, no pasivo |
| No documentar | "Lo recordaré" | Archivos persistentes en {slug}/ |

---

## Output esperado · estructura de carpetas

```
~/aprender-aprehender/temas/{slug}/
├── 00-declaracion.md         # Intención + objetivo
├── 01-bp-chatgpt.md          # Respuesta IA #1
├── 02-bp-claude.md           # Respuesta IA #2
├── 03-bp-gemini.md           # Respuesta IA #3
├── 04-bok-consolidado.md     # BoK triangulado
├── 05-bok-auditado.md        # Post-fact-check
├── 06-cierre.md              # Resumen + plan
├── concept-map.mermaid       # Visual jerárquico
└── glosario.md               # 15-30 términos con tags
```

---

## Referencias

- `agents/coach-aprender.md`
- `prompts/01-research-blueprint.md`
- `prompts/02-coach-system-prompt.md`
- `prompts/04-cross-fact-check.md`
- `prompts/07-notebook-audit.md`
- `references/02-tres-modelos-fundacionales.md` §Body of Knowledge
- `katas/kata-triangulacion-3ias.md`
- `examples/ejemplo-aprender-rust.md`

---

> **Workflow 1 · El Curioso** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
