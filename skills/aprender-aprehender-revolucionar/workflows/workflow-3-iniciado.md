# Workflow 3 · El Iniciado · 20-64 horas

> Transición Escala 2 (Explorador) → Escala 3 (Iniciado). Defender sin notas, ante hostil, bajo presión. Esta es la culminación.

**Agente**: `coach-aprehender`
**Tiempo**: 20-64 horas (4-16 semanas)
**Pre-requisito**: Workflow 2 completo · G-Explorador pasado

---

## Cuándo ejecutarlo

- Después de Workflow 2 (BoK profundo + fuentes primarias)
- Vas a presentar QBR / certificación / entrevista en 4-16 semanas
- Quieres genuinamente alcanzar Escala 3 (no solo "saber del tema")
- Modo Sprint (20h) o Marathon (64h)

---

## Output esperado · Quality Gate G-Aprehender

Al cerrar este workflow, debes tener:

```
✅ Explicación Feynman grabada · sin notas · 5 min · audiencia novato
✅ Quiz Nivel 3 aprobado (Prompt #8 · 4/5 mínimo)
✅ Mock interview pasa LEAN HIRE+ (Prompt #9)
✅ 3 conceptos críticos defendidos ante hostil sin trabarse
✅ Self-assessment + AI-assessment coinciden ±1 escala
✅ NotebookLM con coach activo · 6 técnicas integradas
✅ Spaced Repetition agendado para 30/60/90 días post-Workflow
```

---

## Estructura · Sprint 20h (4 semanas)

### Semana 1 · Vocabulario activo

**Objetivo**: dominar el glosario completo en retrieval ciego.

```
LUNES (60 min)
- Coach NotebookLM aplica retrieval a los 50 términos
- Marcar [FUERTE/PARCIAL/DÉBIL]
- Plan: 5 [DÉBIL] focus esta semana

MARTES (60 min)
- Estudiar 5 [DÉBIL] con elaboration ("¿por qué?", "¿cómo se conecta?")
- Cerrar con retrieval ciego (escribir definiciones de memoria)

MIÉRCOLES (60 min)
- Concept map ciego: dibujar de memoria
- Comparar con tu mapa real · identificar gaps mentales

JUEVES (60 min)
- Feynman a 1 concepto · grabar audio 3 min
- Identificar dónde usaste jerga · iterar 1 vez

VIERNES (60 min)
- Mini-quiz Nivel 1 (Prompt #8 Foundations)
- Score esperado: 4/5
- Programar Spaced Repetition de los 5 [DÉBIL]
```

### Semana 2 · Aplicación y trade-offs

```
LUNES · Casos de uso
- 5 casos reales del dominio
- ¿Qué subtema aplica? ¿Qué trade-off?

MARTES · Trade-off principal #1
- Profundizar (paper foundational + opinión)
- Feynman: explicar ambos lados a no-experto

MIÉRCOLES · Trade-off principal #2
[mismo]

JUEVES · Quiz Nivel 2
- Prompt #8 Intermediate
- Score esperado: 4/5

VIERNES · Concept map con trade-offs
- Tu concept map ahora tiene anotaciones de trade-off por nodo
- Audio de 5 min: tu posición en cada trade-off
```

### Semana 3 · Defensa preliminar

```
LUNES · Mock interview hostil (Prompt #9)
- 30 min mock
- Identificar 3 preguntas que te derribaron
- Documentar gaps específicos

MARTES · Cierre de gaps
- Para cada una de las 3 preguntas, prepara respuesta robusta
- Con números, ejemplos concretos, trade-offs explícitos

MIÉRCOLES · Mock #2
- Validar que las 3 preguntas anteriores ya las defiendes
- Identificar 3 nuevas debilidades

JUEVES · Feynman a conceptos críticos
- Los 3 conceptos más importantes para tu defensa
- Audio de 5 min cada uno

VIERNES · Quiz Nivel 3 (Prompt #8 Advanced)
- Score esperado: 4/5
- Si pasas: estás cerca de Escala 3
```

### Semana 4 · Validación final

```
LUNES · Mock final completo (60 min · Prompt #9)
- Veredicto STRONG HIRE / LEAN HIRE / etc.
- Si LEAN HIRE+: estás listo

MARTES · Si necesitas refuerzo
- Workflow extra de 4h en gap principal
- Si paseaste el lunes, sesión de Spaced Repetition

MIÉRCOLES · Feynman a humano real
- Pedir 30 min a colega no-experto
- Explicar el tema · pedir feedback honesto
- Identificar dónde no entendió

JUEVES · Quiz Nivel 4 (opcional · solo si target Escala 4+)
- Prompt #8 Expert level
- No requerido para cerrar Workflow 3

VIERNES · Cierre y celebración
- Documentar en `~/aprender-aprehender/temas/{slug}/cierre-w3.md`
- Plan de Spaced Repetition: días 30, 60, 90
- Actualizar `.aprender-state.json`
- Si aplica: presentación / entrevista / certificación con confianza
```

---

## Marathon · 64 horas (16 semanas)

Versión expandida con:
- 4 sesiones de 1h por semana × 16 semanas = 64h
- Cada técnica cognitiva con 2-3 sesiones dedicadas
- Práctica deliberada con feedback de humano experto
- Dual coding más completo (genera podcast, video, infografía con NotebookLM)
- Validación con 3 humanos distintos (no solo IA)

→ ver `rituals/ritual-practica-deliberada.md` para schedule completo.

---

## Las 6 técnicas en este workflow

| Semana | Retrieval | Spaced | Feynman | Interleaving | Elaboration | Dual Coding |
|---|---|---|---|---|---|---|
| 1 | ✅ glosario | ✅ DEBIL items | ✅ 1 concepto | ❌ | ✅ por qué | ✅ concept map |
| 2 | ✅ casos | ✅ continúa | ✅ trade-offs | ✅ casos mixed | ✅ relaciones | ✅ audio |
| 3 | ✅ preguntas hostiles | ✅ continúa | ✅ 3 conceptos | ✅ mock | ✅ contradicciones | ✅ explicaciones |
| 4 | ✅ mock final | ✅ programado | ✅ a humano | ✅ quiz nivel 4 | ✅ síntesis | ✅ todo modos |

---

## Anti-patrones (tope-3 más graves en este workflow)

### 1 · Saltarse el Feynman

Si Javier dice *"no necesito Feynman, ya lo entiendo"*, NO permitir.
Feynman es el filtro real. Saltarlo = entrar al QBR sin saber qué no sabes.

### 2 · Mock con coach amable

Si el mock interview es soft (no hostil), no entrenas para la realidad.
Prompt #9 es explícitamente hostil. Si tu coach lo está endulzando, ajusta.

### 3 · Pasar Quiz Nivel 3 con 3/5 y avanzar

La regla es 4/5. 3/5 = repaso obligatorio. Si avanzas con 3/5, llegas Escala 2.5, no Escala 3.

---

## Cierre

Al pasar el Quality Gate G-Aprehender:

```markdown
## Workflow 3 · Cerrado · Escala 3 ALCANZADA

**Tema**: [...]
**Tiempo total invertido**: X horas (W1 + W2 + W3)
**Fecha cierre**: [hoy]

**Validaciones pasadas**:
- ✅ Feynman grabado · sin notas · 5 min
- ✅ Quiz Nivel 3 · 4-5/5
- ✅ Mock interview · LEAN HIRE+
- ✅ 3 conceptos defendidos ante hostil
- ✅ Auto + AI alignment ±1 escala
- ✅ Feedback humano positivo

**Próximos pasos**:
- Spaced Repetition · revisión a 30 días: [fecha]
- Spaced Repetition · revisión a 60 días: [fecha]
- Spaced Repetition · revisión a 90 días: [fecha]
- Si aplicó al evento original (QBR/cert/interview): resultado

**Estado**: `.aprender-state.json` actualizado
- escala_actual: 3
- horas_invertidas: X
```

---

## Referencias

- `agents/coach-aprehender.md`
- `references/01-seis-tecnicas-cognitivas.md`
- `references/03-diez-escalas-maestria.md` §Escala 3
- `prompts/02-coach-system-prompt.md`
- `prompts/08-evaluator-certification.md`
- `prompts/09-interview-simulator.md`
- `katas/kata-feynman-novato.md`
- `katas/kata-defensa-hostil.md`
- `katas/kata-recuperacion-ciega.md`
- `rituals/ritual-aprehension-semanal.md`
- `rituals/ritual-practica-deliberada.md`

---

> **Workflow 3 · El Iniciado** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
