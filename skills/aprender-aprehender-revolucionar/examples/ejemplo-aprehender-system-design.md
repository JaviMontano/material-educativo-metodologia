# Ejemplo · Aprehender System Design en 20 horas

> Sesión real Workflow 3 · Escala 2 → Escala 3 · 4 semanas pre-entrevista FAANG.

**Persona**: Backend Senior · 8 años exp · ya en Escala 2 (sabe del tema, no defiende bajo presión).
**Objetivo**: aprobar entrevista de System Design en empresa target en 4 semanas.
**Tiempo invertido**: 20 horas (1h × 5 días/sem × 4 sem).
**Output esperado**: defender 60 min de mock interview con LEAN HIRE+ veredicto.

---

## Estado inicial (lunes semana 1)

**Auto-eval**: "Sé los conceptos · pero cuando me preguntan en mock me trabo."

**IA-eval con Prompt #8 Nivel 2** (lunes mañana):
- Score: 3/5
- Veredicto: REFUERZO antes de avanzar a Nivel 3

**Diagnóstico**: clásica Escala 2 con espejismo de fluidez. Sabe el vocabulario, no domina trade-offs.

---

## Semana 1 · Vocabulario activo (5h)

### Lunes: retrieval ciego del glosario

```bash
python scripts/retrieval_session.py --concepto "CAP theorem" --tiempo 15
```

Resultado: 3 FUERTE · 2 PARCIAL · 1 DÉBIL

**Gap detectado**: confundía Eventual Consistency con Weak Consistency.

### Martes-Miércoles: estudiar gaps

- 2h estudiar diferencias Eventual vs Weak vs Causal
- Crear 5 flashcards en NotebookLM
- Spaced Repetition agendado

### Jueves: Feynman a un trade-off

Concepto: "Strong vs Eventual Consistency"

Audio grabado · 3 min · audiencia: hermana 11 años (no técnica).

Auto-revisión:
- 2 jergas usadas: "node", "consistency model" → reemplazar con analogías
- Iteración 2: "computadoras que se mandan mensajes", "estilo de ponerse de acuerdo"
- Audio fluyó natural en iteración 2 ✅

### Viernes: Quiz Nivel 1

Score: 5/5 ✅ · avanzar a Nivel 2 la próxima semana.

---

## Semana 2 · Aplicación + trade-offs (5h)

### Lunes-Martes: 5 casos de uso reales

Cada caso · 30 min:
1. Diseñar URL shortener (10M usuarios)
2. Diseñar Twitter feed
3. Diseñar Uber matching
4. Diseñar Netflix CDN
5. Diseñar Slack messaging

Para cada caso:
- ¿Qué subtema aplica? (CAP, sharding, replication, etc.)
- ¿Trade-off principal? (con números: latencia, costo, complejidad)

### Miércoles: trade-off principal · sharding

Profundización 60 min:
- Range vs hash sharding · cuándo cada uno
- Ejemplo concreto · si tu key es timestamp, hash sharding distribuye mejor que range
- Caso edge: hot keys (e.g., celebrity tweets en Twitter)

### Jueves: Quiz Nivel 2

Score: 4/5 ✅ · 1 pregunta sobre quorum me derribó (no recordaba la fórmula N/2+1)

### Viernes: concept map con trade-offs

Mi concept map ahora tiene anotaciones por nodo:
- "Strong Consistency · ↑ correctness · ↓ availability"
- "Eventual Consistency · ↑ availability · ↓ correctness inmediata"

Audio de 5 min: mi posición en cada trade-off principal.

---

## Semana 3 · Defensa preliminar (5h)

### Lunes: Mock #1 (60 min · Prompt #9)

Configuré entrevistador hostil:
- ROL: Staff Engineer
- EMPRESA: Stripe
- PERSONA: Marcos · 12 años exp · ex-Square

Mock real:
- Behavioral: STAR sobre incidente reciente (race condition Java) · OK pero faltaron números
- Technical: profundización en mi CV · me preguntó "¿cómo escalaste de 1M a 10M usuarios?" · respondí general · él presionó por números → me trabé al dar latencia exacta
- Case study: "Diseña URL shortener para 10M users" · diseñé sin números · él interrumpió con "¿costo? ¿latencia p99?" · trabazón

**Veredicto**: 🟡 LEAN HIRE
**Banderas rojas**:
1. Behavioral sin números
2. Diseños sin métricas (latencia, costo, throughput)
3. No anticipo stakeholder hostil en case study

### Martes: cierre de gap #1 (números behavioral)

- Preparé 10 STAR stories con números pre-calculados
- Cada una en <90 segundos
- Audio drill 5 veces

### Miércoles: cierre de gap #2 (números en diseño)

- Practiqué 3 case studies escribiendo SIEMPRE números:
  - 10M users → ¿100 RPS? ¿1000 RPS? Calcular asumiendo 10 reqs/usuario/día
  - URL shortener → 100 chars/URL · 10M URLs → 1 GB · pero con metadata 5-10 GB
  - Latencia p99 target · ¿100ms? ¿200ms? Trade-off con costo

### Jueves: Mock #2 (60 min)

Mismo entrevistador hostil. Ahora:
- Behavioral: cada STAR con números · OK
- Technical: respondo "Latencia p99 era 500ms · bajamos a 50ms con cache · cache hit ratio 87.3%"
- Case study: diseño con números · interrumpe pero ahora respondo "asumiendo X% growth, recalcularíamos a Y"

**Veredicto**: 🟢 STRONG HIRE para Behavioral + Technical · 🟡 LEAN HIRE en Case Study

### Viernes: Quiz Nivel 3

Score: 4/5 ✅ (1 trampa me derribó · diferencia entre 2PC y Saga · falta nuance)

---

## Semana 4 · Validación final (5h)

### Lunes: Mock #3 final (60 min)

Veredicto: 🟢 STRONG HIRE (mejorado en case study desde Mock #2)

Banderas residuales:
- 1 follow-up sobre Byzantine faults me agarró fuera de zona

### Martes: cierre del último gap

- 1h estudiar Byzantine faults a profundidad
- Feynman a hermana: "imagina nodos que mienten, no solo se caen"

### Miércoles: Feynman a humano real

Pedí 30 min a colega Senior (no experto en distribuido).
Le expliqué CAP, Consistency, Sharding · 25 min.

Feedback de él:
- ✅ "Entendí 80% sin pedir aclaración"
- 🟡 "Te trabaste 1 vez en lifetimes... digo, lifetimes? eso era Rust"
- ✅ "Las analogías de carteros y cajas funcionaron"

### Jueves: Quiz Nivel 4 (opcional)

Score: 3/5 · NO necesario para entrevista (target era L4 nivel)

### Viernes: cierre y celebración

```bash
python scripts/progress_tracker.py --update "System Design" --escala 3 \
  --notas "Quality Gate G-Aprehender pasado · listo para entrevista lunes"
```

**Documentación final** en `~/aprender-aprehender/temas/system-design/cierre-w3.md`.

---

## Quality Gate G-Aprehender · pasado ✅

```
[✅] Feynman grabado · sin notas · 5 min (a hermana 11 años · entendió 80%)
[✅] Quiz Nivel 3 aprobado: 4/5 (Prompt #8)
[✅] Mock interview LEAN HIRE+ (3 mocks · trayectoria: LEAN HIRE → STRONG HIRE)
[✅] Self vs AI alignment ±1 escala (auto: 3 / IA: 3)
[✅] 3 conceptos críticos defendidos: CAP, Sharding, Quorum
[✅] Spaced Repetition agendado: días 30, 60, 90
[✅] Plan próxima sesión: revisión a 30 días con Quiz Nivel 3 ciego
```

---

## Lunes siguiente · Entrevista real

**Resultado** (caso ficticio para ejemplo): aprobado con score 8.5/10 en system design round. Oferta recibida 2 semanas después.

---

## Lecciones aprendidas

### Lo que mejor funcionó

1. **Mock progresivo**: Mock #1 doloroso pero útil · Mock #2 mostró progreso · Mock #3 confirmó readiness
2. **Números como obsesión**: cambió mi profile de "interview pasable" a "interview convincente"
3. **Feynman con humano real**: detectó 1 gap que la IA no detectó (lifetimes confusion · era Rust en mi cabeza)

### Lo que costó

- Semana 3 · primer mock fue duro emocionalmente (LEAN HIRE = cerca de NO HIRE)
- Tendencia de subir a "explicación abstracta" sin números · costó 2 semanas corregir
- Spaced Repetition de viernes a domingo se me olvidó 2 veces (calendar invite ayudó la 3a)

### Cambios para futuras aprehensiones

1. Empezar con Mock #1 al inicio de Semana 2 (no Semana 3) · más tiempo para corregir
2. Pre-calcular 10 STAR stories ANTES de empezar Workflow 3
3. Spaced Repetition con calendar invite obligatorio desde día 0

---

## Tiempo total: 20.5 horas
## Veredicto: ✅ Escala 3 alcanzada · listo para entrevista FAANG

---

> **Ejemplo Aprehender System Design** del Playbook Aprender · Aprehender · (R)Evolucionar v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
> *Este es un ejemplo ilustrativo · combina patrones reales en una narrativa pedagógica.*
