# Workflow 2 · El Explorador · 4-20 horas

> Transición Escala 1 (Curioso) → Escala 2 (Explorador). Triangulación de fuentes · profundidad · primeras opiniones.

**Agente**: `coach-aprender` (continuación) · `auditor-cruzado` (post-research)
**Tiempo**: 4-20 horas (4 semanas, 1h × 5 días/semana)
**Pre-requisito**: Workflow 1 completo · BoK triangulado.

---

## Cuándo ejecutarlo

- Después de Workflow 1 con G-Aprender pasado
- Quieres ir más allá de "vocabulario" hacia "puedo distinguir fuentes"
- Modo Sprint del desatraso (20h en 4 semanas)
- Pre-requisito para Workflow 3

---

## Output esperado

- BoK profundizado (subtemas con casos de uso)
- Fuentes primarias verificadas (mínimo 5 papers/libros canónicos)
- Glosario expandido (50+ términos con relaciones)
- 2-3 controversias del campo identificadas con argumentos
- Concept map refinado con flujos/relaciones (no solo jerarquía)
- NotebookLM con 10-15 sources auditadas

---

## Estructura · 4 semanas (1h × 5 días)

### Semana 1 · Profundidad por subtema

**Objetivo**: cubrir cada uno de los 5 subtemas del BoK con mínimo 1h cada uno.

```
LUNES (60 min) · Subtema 1
- Prompt #3 (Deep Research) sobre Subtema 1 · 30 min
- Lectura activa de la respuesta + notas · 20 min
- Conectar con concept map · 10 min

MARTES (60 min) · Subtema 2
[mismo patrón]

MIÉRCOLES (60 min) · Subtema 3
[mismo patrón]

JUEVES (60 min) · Subtema 4
[mismo patrón]

VIERNES (60 min) · Subtema 5
[mismo patrón]
```

### Semana 2 · Fuentes primarias

**Objetivo**: leer las fuentes primarias canónicas del campo.

```
LUNES (60 min) · Paper #1 (foundational)
- Lectura de abstract + introduction + conclusion (no full paper)
- Extracción de 5 ideas clave
- Conectar con tu BoK

MARTES (60 min) · Paper #2
[mismo]

MIÉRCOLES (60 min) · Paper #3
[mismo]

JUEVES (60 min) · Libro canónico (parte 1)
- Skim del índice
- Lectura profunda de 2 capítulos clave

VIERNES (60 min) · Libro canónico (parte 2)
- Lectura profunda de 2 capítulos más
- Extraer 10 conceptos nuevos para glosario
```

### Semana 3 · Triangulación de controversias

**Objetivo**: identificar y entender los debates del campo.

```
LUNES (60 min) · Controversia #1
- Prompt #1 modificado: "Dame las 3 controversias principales en
  [DOMINIO]. Para cada una, presenta los 2 lados con sus mejores
  argumentos."
- En 2 IAs distintas

MARTES (60 min) · Controversia #1 - profundización
- Para cada lado del debate, busca 1 paper que lo defienda
- Lee abstract + conclusion
- Tu opinión preliminar (con caveat de que estás Escala 1-2)

MIÉRCOLES (60 min) · Controversia #2
[mismo patrón]

JUEVES (60 min) · Controversia #3
[mismo patrón]

VIERNES (60 min) · Síntesis
- Tabla de las 3 controversias
- Tu posición preliminar en cada una
- Qué te falta saber para decidir con confianza
```

### Semana 4 · Consolidación

**Objetivo**: actualizar todo lo producido + auditoría completa.

```
LUNES (60 min) · BoK refinado
- Tomar BoK original
- Agregar lo aprendido en semanas 1-3
- Concept map ahora con flujos (no solo jerarquía)

MARTES (60 min) · Glosario expandido
- De 30 → 50 términos
- Cada término con [DOC] tag (ya tienes fuentes)
- Relaciones entre términos (ej. "X requiere Y", "X conflicta con Z")

MIÉRCOLES (60 min) · Auditoría de sources NotebookLM
- Aplicar Prompt #7 (Notebook Audit)
- Eliminar / consolidar / añadir según recomendaciones
- Re-configurar coach (Prompt #2 actualizado)

JUEVES (60 min) · Mini-quiz Nivel 2
- Prompt #8 con dificultad Intermediate
- Score esperado: 4/5
- Si <4/5: identificar gaps · plan refuerzo

VIERNES (60 min) · Cierre
- Documentar todo en {slug}/
- Decidir: avanzar a Workflow 3 (Iniciado) o pausar
- Actualizar estado
```

---

## Quality gate G-Explorador (pre-Workflow 3)

```
✅ BoK refinado con casos de uso reales
✅ Glosario ≥40 términos con [DOC] tags
✅ Concept map con flujos y relaciones (no solo jerarquía)
✅ ≥3 papers fundacionales leídos (abstract+conclusion mínimo)
✅ ≥1 libro canónico (4 capítulos clave)
✅ 3 controversias del campo identificadas con argumentos
✅ NotebookLM con 10-15 sources auditadas
✅ Quiz Nivel 2 aprobado (4/5 mínimo)
✅ Tu posición preliminar en cada controversia documentada
```

---

## Variante Express · 4 horas (4 sesiones de 1h)

Si solo tienes 4h totales:

```
SESIÓN 1 (60 min) · Subtemas más críticos
- Prompt #3 sobre los 2 subtemas más relevantes para tu objetivo

SESIÓN 2 (60 min) · 1 paper fundacional
- Lectura activa abstract+conclusion+1 sección detallada

SESIÓN 3 (60 min) · 1 controversia principal
- Triangulación de los 2 lados

SESIÓN 4 (60 min) · Consolidación + audit
- Concept map refinado · glosario expandido · NotebookLM audit
```

Output: BoK más profundo que Workflow 1, pero menos completo que el Sprint 20h.

---

## Anti-patrones

| Error | Síntoma | Corrección |
|---|---|---|
| Skim de papers | "Lo leí en 5 min" | Lectura activa: abstract + conclusion + 1 sección detallada |
| Solo 1 lado de controversia | Sesgo confirmation | Cubrir AMBOS lados con sus mejores argumentos |
| No expandir glosario | Sigue con 15 términos | Target 50 al final de Workflow 2 |
| Concept map idéntico al de W1 | Sin profundidad | Agregar flujos, relaciones, dependencias |
| Saltar quiz | "Ya entendí" | Quiz Nivel 2 obligatorio · valida real |

---

## Referencias

- `agents/coach-aprender.md`
- `prompts/03-deep-research.md`
- `prompts/07-notebook-audit.md`
- `prompts/08-evaluator-certification.md`
- `references/02-tres-modelos-fundacionales.md`
- `workflows/workflow-1-curioso.md` (pre-requisito)
- `workflows/workflow-3-iniciado.md` (siguiente)

---

> **Workflow 2 · El Explorador** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
