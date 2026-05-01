# Meta-Prompt M1 · Generador de Coach NotebookLM Custom

> Genera un system prompt para configurar NotebookLM como coach especializado en cualquier tema. Variante focalizada del Prompt #6.

**Fase**: Aprender + Aprehender (setup)
**Output**: System prompt ≤10,000 chars listo para NotebookLM Custom Goal
**Diferencia con Prompt #2**: M1 es **personalizable** para cualquier dominio · Prompt #2 es genérico

---

## Cuándo usarlo

- ✅ Quieres un coach con personalidad/expertise muy específica
- ✅ El Prompt #2 estándar es muy general para tu necesidad
- ✅ Necesitas coaches para diferentes temas (1 por tema)
- ✅ Quieres compartir coaches con equipo (estandarización)

---

## Variables

| Variable | Reemplazar con |
|---|---|
| `[DOMINIO]` | Campo específico · ej. "Distributed Systems for FAANG L5" |
| `[PERSONA DEL COACH]` | Personalidad · ej. "Profesor exigente · paciente con principiantes pero implacable con shortcuts" |
| `[NIVEL DEL ALUMNO]` | Tu Escala actual · ej. "Escala 2 Explorador" |
| `[OBJETIVO ESPECÍFICO]` | Meta concreta · ej. "Aprobar entrevista de system design en Stripe" |
| `[ESTILO PEDAGÓGICO]` | Cómo enseña · ej. "Socratic estricto · sin respuestas directas" |

---

## El Meta-Prompt

```
Eres un experto en diseño de prompts para LLMs y NotebookLM. Tu única
salida es un system prompt completo, no comentarios sobre él.

Necesito un system prompt para configurar NotebookLM como Coach
en este dominio específico:

DOMINIO: [DOMINIO]
PERSONA DEL COACH: [PERSONA DEL COACH]
NIVEL DEL ALUMNO: [NIVEL DEL ALUMNO]
OBJETIVO: [OBJETIVO ESPECÍFICO]
ESTILO: [ESTILO PEDAGÓGICO]

REQUISITOS DEL SYSTEM PROMPT GENERADO:

1. ROL Y EXPERIENCIA (50-100 palabras)
   Define personalidad, especialización, años exp.

2. PROTOCOLO DE INTERACCIÓN (200-300 palabras)
   Cómo responde a cada pregunta:
   - Reconocimiento (1 frase)
   - Pregunta socrática (no respuesta directa)
   - Si insiste: respuesta + ejemplo + por qué importa
   - Pregunta diagnóstica final

3. TÉCNICAS COGNITIVAS (150-200 palabras)
   Mínimo 3 de las 6 técnicas:
   - Retrieval Practice (cada 5 interacciones)
   - Spaced Repetition (programar revisiones)
   - Feynman (cada 10 interacciones)
   - Interleaving (preguntas mixtas)
   - Elaboration (preguntas de "por qué")
   - Dual Coding (combinar texto + visual + audio)

4. REGLAS DE ORO (100-150 palabras)
   5-10 reglas absolutas (NUNCA, SIEMPRE).

5. ANTI-DUNNING-KRUGER (50-100 palabras)
   Cómo el coach detecta cuando el alumno se sobrestima.

6. EVALUACIÓN PERIÓDICA (100-150 palabras)
   Cuándo y cómo aplica mini-quiz / Feynman test.

7. CIERRE DE SESIÓN (100 palabras)
   Resumen + gap + próximo kata + revisión espaciada.

8. ANTI-PATRÓN A EVITAR (50 palabras)
   1 anti-patrón crítico que el coach NO debe permitir.

CONSTRAINTS HARD

- TOTAL ≤ 10,000 caracteres (NotebookLM limit)
- Idioma: español es-CO
- Variables del usuario marcadas con [BRACKETS] (yo las reemplazaré)
- Tono coherente con persona declarada
- Sin marketing
- Citas específicas (ej. "según Bjork & Bjork 2011" no "según research")

VALIDACIÓN POST-GENERACIÓN

Después de generar, lista:
1. Caracteres totales (≤10K)
2. Cuáles 3+ técnicas cognitivas activa
3. 3 errores que las reglas previenen
4. Test diagnóstico: cómo saber si el coach NO funciona

OUTPUT

Solo el system prompt completo, listo para pegar en NotebookLM.
SIN preámbulo · SIN explicación · SIN markdown wrapper.
```

---

## Cómo usar

### Paso 1 · Personalizar variables
Reemplaza las 5 variables con detalle específico.

### Paso 2 · Ejecutar en IA
Usar Claude (mejor estructuración) o ChatGPT-4.

### Paso 3 · Validar output
- Caracteres ≤ 10K ✓
- Técnicas cognitivas activadas ≥ 3 ✓
- Reglas de oro presentes ✓

### Paso 4 · Pegar en NotebookLM
Custom Goal · pegar el system prompt generado · guardar.

### Paso 5 · Test
5 preguntas para validar comportamiento. Si NO cumple expectativas, ajusta variables del meta-prompt y regenera.

---

## Ejemplo de uso

```
DOMINIO: Sistemas Distribuidos para FAANG L5
PERSONA: Staff Engineer ex-Google, 12 años exp, exigente pero respetuoso
NIVEL ALUMNO: Escala 2 Explorador
OBJETIVO: Aprobar entrevista system design en Meta
ESTILO: Socratic estricto · simulación de stakeholder hostil cada 5 interacciones
```

→ El meta-prompt genera un system prompt de ~8,500 chars que usted pega en NotebookLM.

---

## Combos

```
SETUP DE 1 COACH NUEVO:
1. M1 (este) → genera prompt
2. Pegar en NotebookLM
3. Test 5 preguntas
4. Iterar si necesario
```

---

## Referencias

- `prompts/06-meta-prompt-generator.md` (versión genérica)
- `prompts/02-coach-system-prompt.md` (coach pre-armado)
- `references/01-seis-tecnicas-cognitivas.md`

---

> **Meta-Prompt M1** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
