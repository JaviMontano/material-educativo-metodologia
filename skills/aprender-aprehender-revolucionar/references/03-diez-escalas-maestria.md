# 10 Escalas de Maestría · Mastery Scales

> Rúbrica completa Ignorante (0) → Referente (9) con horas, criterios testables, retos verificables y recompensas. v1.1.0.

`[FUENTE-PRIMARIA]` Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 §10 Escalas.

`[LÍMITE]` **Esta skill cubre Escalas 0–3** (primeras 64 h con método sistemático). Para Escalas 4+ se requiere práctica en mundo real con feedback humano · la skill ayuda a planear y mantener afilado, no a generar la práctica.

## Tabla maestra

| # | ES / EN | Horas | Criterio aceptación binario | Reto verificable | Recompensa |
|---|---|---|---|---|---|
| **0** | Ignorante / Unaware | — | No diferencia el dominio | Descríbelo en 1 frase | Conciencia |
| **1** | Curioso / Curious | 1–4 | BoK triangulado · glosario ≥15 (W1) | Enseña a Escala 0 sin trabarte | Vocabulario |
| **2** | Explorador / Explorer | 4–20 | Triangulación + auditoría fuentes (W2) | Enseña a Escala 1 sobre controversias del campo | Discernimiento |
| **3** | Iniciado / Initiate | 20–64 | Feynman sin notas + Quiz N3 4/5 + Mock LEAN HIRE+ (W3) | Mentoriza a Escala 1-2 · 30 min · alumno avanza | Defensa pública |
| **4** | Practicante / Practitioner | 64–200 | ≥1 proyecto en producción · time-to-solve estable | Mejora proceso medible (antes/después) | Productividad |
| **5** | Competente / Competent | 200–500 | Maneja casos novel · trade-offs explícitos | Entrena Escala 3→4 con plan reproducible | Liderazgo técnico |
| **6** | Versado / Versed | 500–1,000 | Contribución original (paper · talk · OSS) | Tus mentees alcanzan Escala 5+ | Reconocimiento |
| **7** | Experto / Expert | 1,000–10,000 | Cambia prácticas del campo · reconocimiento institucional | Contribuye al avance documentable | Autoridad |
| **8** | Maestro / Master | 10,000+ | Aporte cross-disciplina · funda categorías | Forma dirección de industria | Visión |
| **9** | Referente / Referent | 10,000+ | Tú ERES el estándar (externo · no auto-declarable) | Sucesor define escala nueva | Legado |

> **10,000 h**: regla popularizada por Gladwell `[DOC: Outliers · 2008]`, refinada por Ericsson `[DOC: Peak · 2016]`. NO es magia: son 10,000 h de **práctica deliberada con feedback** — no horas de oficina pasivas.

`[NUEVO-APORTE]` Las Escalas son no-lineales en horas: pasar de Escala 1 a Escala 3 toma ~64 h con método; pasar de Escala 6 a Escala 7 puede tomar **5+ años** porque depende de circunstancias externas (publicación, reconocimiento de pares, oportunidades). El esfuerzo no escala linealmente con la escala.

---

## Escalas 0–3 · cobertura directa de la skill

### 0 · Ignorante

- **Síntomas**: sonríes amablemente cuando se menciona el tema · no diferencias del campo adyacente · no reconoces autoridades.
- **Salir**: 1 frase definitoria *"X es el campo que estudia/diseña/optimiza Y"*.
- **Cómo avanzar**: Workflow 1 con Prompt #1 · 1-4 h.

### 1 · Curioso

- **Definición**: vocabulario básico ≥15 términos · sabes qué no sabes.
- **Síntomas positivos**: identificas subtemas · reconoces autoridades · formulas preguntas inteligentes.
- **Criterio**: BoK triangulado (3+ IAs) · glosario 15-30 términos · concept map mermaid · 3 fuentes primarias verificadas (no terciarias).
- **Reto**: enseñar a Escala 0 durante 5 min sin tropezarse.
- **Tiempo**: 1-4 h Express o spread en 1 sem.
- **Workflow**: `workflows/workflow-1-curioso.md`.

### 2 · Explorador

- **Definición**: cruzaste fuentes · identificas contradicciones · distingues 1°/2°/3° · opinión rudimentaria sobre debates.
- **Síntomas**: reconoces contradicciones entre fuentes · distingues paper de blog · detectas señales de hallucination IA · 1-2 controversias identificadas.
- **Criterio**: triangulación documentada (Prompts #4 + #7) · auditoría de sources · glosario 30-50 términos · BoK refinado con conexiones interdisciplinarias.
- **Reto**: enseñar a Escala 1 sobre las controversias del campo durante 15 min.
- **Tiempo**: 4-20 h (Sprint 4 sem).
- **Workflow**: `workflows/workflow-2-explorador.md`.

### 3 · Iniciado · GATE CRÍTICO

- **Definición**: explicas sin notas · te defiendes de preguntas hostiles · puedes mentorizar Escala 1-2.
- **Síntomas**: pasas Feynman a niño 12 años · apruebas quiz Nivel 3 · sobrevives mock interview hostil · tienes opinión propia (no solo recitar autores).

#### Quality gate G-Iniciado · `[CRITERIO-ACEPTACIÓN]` 5/5

- [ ] Feynman sin notas grabado (audio/video · 3-5 min)
- [ ] Quiz Nivel 3 aprobado: ≥4/5 (`prompts/08-evaluator-certification.md`)
- [ ] Mock interview LEAN HIRE+ (`prompts/09-interview-simulator.md`)
- [ ] Self-assessment ↔ AI-assessment coinciden ±1 escala
- [ ] Mentoría real a Escala 1-2 · 30 min · alumno avanza demostrablemente

- **Reto**: mentorizar a alguien Escala 1-2 durante 1 sesión completa de 30 min. Si el alumno avanza visiblemente, eres Escala 3.
- **Tiempo**: 20-64 h (Sprint 4 sem o Marathon 16 sem).
- **Workflow**: `workflows/workflow-3-iniciado.md` + todos los katas.

`[LÍMITE]` Última escala que la skill cubre directamente con método sistemático. De aquí en adelante: práctica real con feedback de pares.

---

## Escalas 4–9 · cobertura indirecta (mantenimiento + planeación)

### 4 · Practicante

- **Definición**: ejecutas en producción confiable · output predecible.
- **Síntomas**: ≥1 proyecto shipped · time-to-solve estable (varianza <2× entre problemas similares) · estimas costos/tiempos con error <30%.
- **Criterio**: ≥1 proyecto en producción con responsabilidad propia · métricas documentadas (velocidad · calidad · costo) · Capability Nivel 1 completo · Nivel 2 en progreso.
- **Reto**: mejorar proceso existente · medir antes/después.
- **Tiempo**: 64-200 h práctica real (3-6 meses).
- **Cómo te ayuda la skill**: auditoría mensual de relevancia + retrieval para no perder lo aprehendido.

### 5 · Competente

- **Definición**: manejas casos novel · sabes cuándo NO aplicar las técnicas estándar.
- **Síntomas**: te llaman para problemas raros · trade-offs explícitos (no por defecto) · sabes cuándo violar "best practices" · mentorizas Escala 3-4 sin micro-management.
- **Criterio**: Capability Nivel 2 completo · Nivel 3 en progreso · ≥3 casos novel resueltos con trade-offs documentados · ≥1 mentee llegando a Escala 4.
- **Reto**: entrenar a alguien Escala 3 hasta Escala 4 con plan reproducible.
- **Tiempo**: 200-500 h.

### 6 · Versado

- **Definición**: innovas dentro de los límites del campo.
- **Síntomas**: publicaste / diste talks · tienes patrones/técnicas tuyas · mentees alcanzan Escala 5+ · invitado a comités técnicos.
- **Criterio**: contribución original documentada (paper · talk · OSS · patente) · Capability Nivel 3 completo · Nivel 4 en progreso · mentees alcanzando Escala 5.
- **Reto**: tus alumnos llegan a Escala 5+ (indicador externo de impacto).
- **Tiempo**: 500-1,000 h + actividad pública sostenida.

### 7 · Experto

- **Definición**: defines los límites del campo.
- **Síntomas**: tu nombre en bibliografías · co-autoría con autoridades · tu trabajo influye decisiones empresa/gobierno · consultado en crisis del dominio.
- **Criterio**: contribuciones que cambiaron prácticas · Capability Nivel 4 completo · reconocimiento institucional (premios · fellowships · cátedras).
- **Reto**: contribución al avance documentable.
- **Tiempo**: 1,000-10,000 h (5-15 años).

### 8 · Maestro

- **Definición**: ves cross-disciplina · creas categorías nuevas.
- **Síntomas**: obra abarca disciplinas · fundaste o transformaste campos · libros/papers citados décadas · formas dirección de industria.
- **Reto**: forma dirección de industria por influencia, no autoridad formal.
- **Tiempo**: 10,000+ h + carrera completa.

### 9 · Referente

- **Definición**: TÚ eres el estándar.
- **Síntomas**: tu nombre = el campo (Knuth = algoritmos · Lamport = sistemas distribuidos) · premios mayores reciben tu nombre · generaciones de practicantes te citan como punto de partida.
- **Criterio**: externo · validado por la comunidad · NO auto-declarable.
- **Reto**: sucesor define escala nueva (señal de que agotaste la tuya).
- **Tiempo**: carrera completa + circunstancias históricas favorables. **No es solo trabajo duro** · requiere condiciones del campo + timing.

---

## Cómo usar las escalas en la práctica

### Para tu skill activa hoy

```
1. ¿En qué escala estoy? (auto + Prompt #8 · diferencia ≤1 · §03-diagnóstico)
2. ¿Escala objetivo en 6 meses?
3. ¿Horas que faltan? (objetivo × diferencia × 1.5 buffer Dunning-Kruger)
4. Workflow + ritual:
   · 0→1: Workflow 1 + ritual diario
   · 1→2: Workflow 2 + ritual semanal
   · 2→3: Workflow 3 + ritual semanal + katas
   · 3→4: práctica producción + ritual auditoría
   · 4+: skill se vuelve mantenimiento, no progresión metodológica
```

### Para auditoría de relevancia (mensual)

| Skill | Tu Escala | Escala mercado | Decisión |
|---|---|---|---|
| jQuery | 6 (Versado) | 1 (Curioso · mercado dejó de demandar) | [SOLTAR] · plan reskill React 0→3 en 64 h |
| System Design | 5 (Competente) | 4-5 (alta demanda) | [MANTENER] · profundizar hacia 6 |

→ `prompts/05-relevance-audit.md` · `agents/coach-revolucionar.md`.

### Para narrativa profesional

```
✅ "10 años exp · Escala 6-7 en Sistemas Distribuidos"
✅ "Versado en X · iniciando aprehensión en Y"
❌ "Senior" (vacío sin referencia)
❌ "Experto en todo" (Dunning-Kruger evidence)
```

`[NUEVO-APORTE]` Declarar Escala explícitamente en LinkedIn/CV es **diferenciador** porque la mayoría usa "Senior/Mid/Junior" sin método. La rúbrica concreta (con criterios y horas) genera credibilidad inmediata en entrevistas porque demuestra meta-conciencia.

---

## Anti-patrones por escala

| Escala | Anti-patrón típico | Antídoto |
|---|---|---|
| 0 | "No me interesa" sin investigar mín si debería | Auto-eval honesta · 5 min en Wikipedia / paper foundational |
| 1 | Confundir vocabulario con comprensión ("conozco términos = sé") | Reto explícito: enseñar a Escala 0 |
| 2 | Confundir cantidad con calidad ("leí 50 papers = experto") | Filtro: cuántas controversias puedes argumentar AMBOS lados |
| 3 | Dunning-Kruger pico ("ya domino, puedo enseñar") sin mentoría real | Reto verificable: mentoría real, alumno debe avanzar |
| 4 | Estancamiento por confort ("ya soy productivo, ¿para qué más?") | Auditoría 4-D · ¿qué viene en 3 años? |
| 5 | Sobrevalorar trade-off favorito ("siempre debe ser X" sin contexto) | Buscar 3 casos donde NO funciona tu favorito |
| 6 | Identidad excesiva con el campo · no soltar lo obsoleto | Auditoría mensual implacable |
| 7 | Defender statu quo del campo contra disrupciones | Mentorizar a Escala 6 que cuestiona tu base |
| 8 | Hablar fuera de disciplina sin humildad | Cross-disciplina debe ir con experto del otro campo |
| 9 | Convertirse en culto · suprimir voces alternativas | Promover sucesor que te supere · no clonar |

---

## Casos borde (transiciones)

| Caso | Detección | Resolución |
|---|---|---|
| **Skill que llegaste a Escala 3 hace 5 años, no tocaste desde** | Skill marcada Escala 3 sin práctica reciente | Auditar: ¿conservas defensa pública sin notas? Si no, eres Escala 2 con vocabulario residual |
| **Escala alta en sub-tema, Escala baja en el campo macro** | "Soy Escala 6 en Raft pero Escala 3 en Sistemas Distribuidos" | Válido y común · escala se mide por sub-dominio acotado · no inflar al macro |
| **Escala personal vs escala mercado divergen** | Escala 6 en jQuery, mercado Escala 1 | Activar `coach-revolucionar` · framework 4-D · probable [SOLTAR] |
| **Self-eval Escala 5 pero 0 mentees llegando a 4** | Criterio externo no se cumple | Bandera: probable Escala 4 con auto-inflación. Validar con mock training real |
| **Escala 7+ sin reconocimiento institucional** | "Soy experto pero nadie me cita" | Ambiguo: o eres pre-experto (5-6) o el campo no tiene mecanismo de reconocimiento (raro). Investigar |

---

## Validación rápida (auto-test) para tu skill principal

- [ ] Sé en qué Escala estoy · con evidencia (no auto-declaración)
- [ ] IA-eval reciente (Prompt #8) coincide ±1
- [ ] Sé qué necesito para avanzar 1 escala (criterio + reto)
- [ ] Plan de horas concreto (con buffer 1.5×)
- [ ] Sé en qué Escala está mi mercado (no solo yo)
- [ ] Si soy Escala ≥4: hago auditoría mensual de relevancia
- [ ] Si soy Escala ≥6: identifico cómo contribuyo al campo
- [ ] Mi narrativa profesional usa Escala explícita, no "Senior"

`[CRITERIO-ACEPTACIÓN]` <5/8 → empieza por auto-diagnóstico con Prompt #8 antes de planear progresión.

---

## Referencias cruzadas

- Modelo conceptual: `references/02-tres-modelos-fundacionales.md` §Maturity Model
- Anti-patrones extendidos: `references/04-anti-patrones-y-trampas.md` §Dunning-Kruger
- Diagnóstico: `prompts/08-evaluator-certification.md`
- Auditoría mensual: `prompts/05-relevance-audit.md` · `agents/coach-revolucionar.md`
- Workflows por escala: `workflows/workflow-1-curioso.md` · `workflow-2-explorador.md` · `workflow-3-iniciado.md`

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · `[FUENTE-PRIMARIA]` Playbook v2.0.0 §10 Escalas
