# Ejemplo · Desatraso Express · LLMs en 4 horas

> Catch-up sobre 6 meses de avances en LLMs/Agentic AI · Workflow 2 condensado.

**Persona**: Solutions Architect · 15 años exp · activo en cloud/data, periférico en LLMs.
**Disparador**: cliente pregunta sobre estrategia LLM · necesita ponerse al día YA.
**Tiempo disponible**: 4 horas (sábado mañana antes de meeting el lunes).
**Output esperado**: vocabulario, mapa del campo, opinión informada para presentación lunes.

---

## Contexto antes de la sesión

**Estado conocimiento de Javier (octubre 2025)**:
- Conoce GPT-3, GPT-4 conceptual · usa ChatGPT regular
- Sabe que existe RAG · no ha implementado
- Heard about "agentic AI" · no entiende la arquitectura
- Cero contacto con: Claude Opus 4.7, MCP, evals, prompt caching

**6 meses de gap** (oct 2025 - abril 2026):
- Claude 4 family (Opus 4.5/4.6/4.7)
- MCP standard establecido
- Agentic systems en producción (no solo hype)
- Prompt caching → producción
- Constitutional AI maduro

---

## Cronograma real · 4 horas

### 0:00-0:15 · Declaración Express

Sin mucho overhead · time-boxed:

```markdown
TEMA: LLMs / Agentic AI · estado del arte 2026-Q2
POR QUÉ: cliente meeting lunes · necesito vocabulario + opinión
ESCALA OBJETIVO: 1 (Curioso · puedo conversar con IT lead)
TIEMPO: 4h hoy
HIPÓTESIS: "GPT-4 sigue siendo el referente"
```

(spoiler: la hipótesis es incorrecta · descubrimiento del workflow)

### 0:15-1:00 · Triangulación Blueprint EXPRESS

Tomé Prompt #1 · ejecuté en 3 IAs **rápido** (15 min cada):

#### Perplexity (15 min · con búsqueda web habilitada)

Output (extracto):
- Estado del arte abril 2026: Claude Opus 4.7, GPT-5, Gemini 2.5 Ultra
- MCP (Model Context Protocol) estándar dominante
- Agentic systems en producción: Anthropic Agent SDK, OpenAI Assistants
- Subtemas: tool use, prompt caching, evals, RLHF→constitutional, memory systems

#### Claude (15 min)

Similar pero más estructurado:
- BoK con 7 ramas
- Glosario de 32 términos (incluyó "agent loop", "subagents", "context management")
- Notable: Claude reconoció "no tengo data después de mi cutoff" para algunos items recientes

#### Gemini (15 min)

Diferente énfasis:
- Más detalle en Gemini 2.5 (lógico)
- Listó "Google Search Generative Experience" como avance · cuestionable relevancia para mi caso
- Mencionó "DeepMind Gemini Live" · interesante pero off-topic

### 1:00-2:00 · Consolidación EXPRESS

Tabla rápida (no exhaustiva):

| Item | Perplexity | Claude | Gemini | Veredicto |
|---|---|---|---|---|
| Claude Opus 4.7 | ✅ | ✅ (cutoff) | ✅ | 🟢 CONFIRMED |
| MCP standard | ✅ | ✅ | ❌ | 🟡 REVISAR · Gemini omitió |
| Constitutional AI maduro | ✅ | ✅ | ✅ | 🟢 CONFIRMED |
| Agentic SDK production-ready | ✅ | ✅ | ✅ | 🟢 CONFIRMED |
| Prompt caching estándar | ✅ | ✅ | ❌ | 🟡 REVISAR |
| GPT-5 lanzado | ✅ | ❌ | ✅ | 🟡 REVISAR · Claude no |
| Gemini 2.5 production | ✅ | ✅ | ✅ | 🟢 CONFIRMED |

**Anti-patrón evitado**: NO confiar en Perplexity solo · MCP omitido por Gemini era señal · validar manualmente.

Validación manual rápida · 5 min búsqueda:
- MCP: confirmado (modelcontextprotocol.io existe · adopted by Anthropic, soon OpenAI)
- GPT-5: confirmado (lanzamiento ene 2026)
- Prompt caching: confirmado en Anthropic/OpenAI APIs

### 2:00-2:30 · Concept map mental

Sin tiempo para mermaid bonito · concept map en hoja:

```
                    LLMs 2026
                       |
        ┌──────────────┼───────────────┐
        |              |               |
   CAPACIDADES     INTEGRACIONES   AGENTIC
        |              |               |
   - Multimodal    - MCP (std)     - Agent SDK
   - Long context  - Tool use      - Subagents
   - Reasoning     - APIs          - Memory mgmt
                                    - Tool loops
        |              |               |
   - Caching       - RAG patterns  - Context engineering
   - Streaming     - Embeddings    - Skills/Tools
```

### 2:30-3:00 · Fact-Check cruzado

Pegué top 10 claims en Claude (4ª IA · independent) con Prompt #4:

Veredictos:
- 8/10 CONFIRMED
- 1/10 NO SOURCE (claim de Perplexity sobre adopción MCP en 70% APIs · cifra inventada)
- 1/10 PARTIAL (claim sobre "Claude 4.7 1M context" · cierto pero solo en algunos tier · matiz)

Eliminé el dato 70% · mantuve 1M context con caveat "según tier".

### 3:00-3:30 · Setup mínimo NotebookLM

Sin tiempo para coach completo · setup básico:
1. Notebook "LLMs Q2 2026 catch-up"
2. Sources: las 3 respuestas IA + tabla triangulación
3. Custom Goal con Prompt #2 simplificado · 5K chars (no 10K)
4. Test 3 preguntas · OK

### 3:30-4:00 · Síntesis para meeting lunes

Output ejecutivo (lo que voy a usar el lunes):

```markdown
# LLMs Estado del Arte 2026-Q2 · Brief Ejecutivo

## 3 cambios desde octubre 2025

1. Capacidades subieron significativamente
   - Claude Opus 4.7: 1M context window (algunos tiers)
   - GPT-5 lanzado · benchmarks competitivos
   - Gemini 2.5 production-ready

2. Estandarización
   - MCP (Model Context Protocol) emergió como estándar
   - Agent SDK · construcción de agentes ya no requiere desde-cero
   - Prompt caching estándar en APIs principales (-90% costo)

3. Constitutional AI maduro
   - Sycophancy reducida
   - Hallucination tasas bajaron
   - Pero: STILL HALLUCINATE · Primary Source Rule sigue obligatorio

## Para mi cliente (recomendaciones)

1. Stack: Claude Opus 4.7 (razonamiento premium) +
         GPT-4 turbo (latencia/costo) + 
         Gemini (volumen Google ecosystem)
2. Build vs Buy: Agent SDK madura · evaluar antes de custom
3. Watch: MCP · si su roadmap es 12 meses, MCP será standard antes
4. Riesgo: hallucinations siguen · evaluación humana en loops críticos

## Lo que NO sé (honesto)

- No he construido agente production-grade · solo conceptual
- No tengo benchmarks personales · cito públicos
- Recomendación: PoC pequeño antes de inversion grande
```

---

## Quality Gate G-Aprender · pasado ✅ (Express)

```
[✅] BoK triangulado en 3 IAs (Perplexity + Claude + Gemini)
[✅] Glosario ≥15 términos (consolidé 22 entre las 3)
[✅] Concept map jerárquico (en papel · OK para Express)
[✅] 4 fuentes primarias verificadas (Anthropic docs, OpenAI release notes, MCP spec, papers fundacionales)
[✅] Auditor cruzado · 1 hallucination eliminada (cifra 70% adopción MCP)
[✅] NotebookLM básico configurado
[✅] Síntesis ejecutiva lista para meeting lunes
```

---

## Lunes · meeting con cliente

**Cliente IT Lead**: "¿Qué tal MCP? Hemos visto referencias..."

**Yo** (con confianza basada en 4h de research, no en bluff):
> "MCP emergió como estándar Q1 2026 · adopción inicial en Anthropic, expandiéndose. Para tu caso, recomendaría: si tu roadmap es 12 meses+, considera arquitectura compatible con MCP desde día 1 · si es 3-6 meses, foco en producto, MCP como upgrade futuro. Te puedo profundizar en cualquier aspecto · honesto: no he construido agente production-grade aún, mi expertise es la arquitectura cloud que rodea estos sistemas."

**Cliente**: "Eso suena más calibrado que otros vendors · me gusta. Sigamos."

**Resultado**: meeting exitoso · cliente prefiere honesty + framework structured > overconfidence.

---

## Lecciones aprendidas

### Lo que mejor funcionó

1. **Time-boxed estricto**: cada paso tenía su slot · sin overruns
2. **Concept map en papel**: cuando no hay tiempo, mermaid es overkill · papel sirve
3. **Síntesis ejecutiva al final**: convirtió las 4h en formato accionable para meeting
4. **Honesty sobre lo que NO sé**: no fingir conocimiento profundo que no tengo · gana credibilidad

### Lo que costó

- 4h fueron tight · sin tiempo para Workflow 3 (no era el objetivo · OK)
- 2 hallucinations encontradas en 4h · si era cliente importante, hubiera necesitado 1h más de fact-check
- Concept map a mano se perdió · debería haberlo digitalizado

### Próximos pasos

Si meeting genera engagement:
1. Workflow 2 completo (Sprint 20h en 4 semanas) sobre LLMs
2. PoC de un agente real con Anthropic Agent SDK
3. Workflow 3 si necesito estar Escala 3 (defender técnicamente)

Si NO genera engagement: el catch-up de 4h ya es suficiente · documentar y archivar.

---

## Comandos útiles

```bash
# El plan Express
python scripts/desatraso_planner.py --tema "LLMs Agentic AI 2026" --tiempo 4h \
  --escala-actual 0 --industria "Solutions Architect Cloud"

# Tracking
python scripts/progress_tracker.py --add-tema "LLMs 2026" --objetivo 1 --horas-obj 4
python scripts/progress_tracker.py --update "LLMs 2026" --escala 1 \
  --notas "Meeting lunes exitoso · post-meeting: decidir Workflow 2 o archivar"
```

---

## Tiempo total: 4.0 horas
## Veredicto: ✅ Catch-up exitoso · meeting cliente OK · decisión informada

---

> **Ejemplo Desatraso LLMs Express** del Playbook Aprender · Aprehender · (R)Evolucionar v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
> *Caso ilustrativo del modo Express · cuando tienes deadline real y necesitas ponerte al día sin lujo de tiempo.*
