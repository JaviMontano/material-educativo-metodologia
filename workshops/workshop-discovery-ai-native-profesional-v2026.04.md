# Workshop Discovery AI-Native · Variante Profesional · 1 día · v2026.04

> **Para quién:** profesional individual o equipo de 3–6 personas que aplica Discovery AI-Native a un problema real de su trabajo cotidiano. Decide rápido, sin comité ejecutivo.
> **Duración:** 1 día (6 h efectivas) · 4 sesiones de 90 min + 3 breaks · consolidación post-workshop **48 h**.
> **Tono:** pragmático, directo. Asume conocimiento general de IA. "Tú" formal latinoamericano.
> **Versión:** v2026.04 · Profesional · MetodologIA · CC BY-NC-SA 4.0

---

## TL;DR · El método en 60 segundos

Tomas **un problema concreto** de tu trabajo. En **un día** lo conviertes en un **prototipo navegable + spec destilada en 3 lentes (Es / Hace / F-NF) + plan de 30 días** con owner asignado. La spec **emerge del prototipo**, no del papel. La IA es copiloto: tú diriges, ella construye. En **48 h post-workshop** consolidas tres entregables livianos que cualquier compañero puede leer y ejecutar.

No hay comité ejecutivo, no hay matriz RACI completa, no hay 2 días de talleres. Hay **decisión rápida con evidencia**.

---

## Cuándo usar este workshop

| Escenario | Encaja porque… |
|---|---|
| Tienes una idea de automatización con IA y quieres validar si vale la pena antes de pedir presupuesto. | El RAT de 1 mes te da una respuesta binaria sin compromiso largo. |
| Tu equipo (3–6 personas) propone "deberíamos usar IA para X" y nadie sabe por dónde empezar. | El workshop fuerza acotar el qué antes de saltar al cómo. |
| Recibiste un encargo ambiguo de tu jefe ("hagan algo con IA en este proceso") y necesitas convertirlo en algo demostrable. | Sales del día con un prototipo que puedes mostrar. |
| Quieres entrenar al equipo en un método replicable, no en una herramienta. | El framework Es / Hace / F-NF se aplica a cualquier futura iniciativa. |

**No lo uses si:** la iniciativa requiere aprobación de comité corporativo, integra 5+ áreas, o el sponsor no puede dedicar 6 h continuas. Para esos casos, escala a la variante Empresas (2 días + consolidación HITL 5 días).

---

## Pre-workshop · 60 min de preparación

Tres tareas, una sola persona (el conductor), día previo:

| # | Tarea | Salida concreta |
|---|---|---|
| 1 | **Problem statement borrador** — escribe en una frase: *"Quiero ayudar a [usuario] cuando [contexto] para que [resultado] sin [restricción]."* | Un párrafo de máximo 5 líneas, en un doc compartido. |
| 2 | **3 stakeholders confirmados** — identifica 3 personas que sufren o resuelven el problema hoy. Confirma asistencia 6 h. | Calendario aceptado por las 3. |
| 3 | **Evidence pack mínimo** — 3 a 5 artefactos: screenshots, métricas, ticket real, ejemplo de output actual, dataset pequeño. | Carpeta `pre-read/` con archivos numerados. |

**Regla:** si al iniciar el día falta cualquiera de los tres, **se posterga el workshop**. No improvises evidencia — se nota y contamina las decisiones.

---

## Agenda · 4 sesiones de 90 min

| Hora | Sesión | Meta | Artefacto que sale |
|---|---|---|---|
| 09:00–10:30 | **S1 · Acotar el qué** | Pasar de la idea ambigua a un problem statement firmado. | Problem statement v1 + lista *no-hace*. |
| 10:30–10:45 | Break | — | — |
| 10:45–12:15 | **S2 · Mapeo de oportunidades** | Identificar 2–3 hipótesis con evidencia, no con opinión. | Tabla *hipótesis → evidencia → métrica*. |
| 12:15–13:15 | Almuerzo | — | — |
| 13:15–14:45 | **S3 · Vibe coding** | Construir un prototipo navegable con IA como copiloto. | Prototipo demo-able + log de prompts. |
| 14:45–15:00 | Break | — | — |
| 15:00–16:30 | **S4 · Spec destilada + plan 30 días** | Destilar la spec del prototipo y comprometer próximos pasos. | Spec en 3 lentes + plan 30 días + owner. |

> **Reloj duro:** cada sesión termina cuando termina. Si una corre larga, la siguiente se recorta — no se extiende el día.

---

### S1 · Acotar el qué (90 min)

**Objetivo:** alinear qué es éxito y qué **NO** se va a resolver hoy.

| Bloque | Tiempo | Qué hacen |
|---|---|---|
| Lectura del borrador pre-workshop | 15 min | El conductor lee el problem statement v0. Cada asistente subraya en silencio lo que NO entiende. |
| Edición colaborativa en vivo | 35 min | Reescritura en pantalla compartida hasta que las 3 personas firmen verbalmente. |
| Lista *no-hace* | 25 min | Por cada cosa que el problem statement implica, escribir explícitamente lo que NO se va a resolver. Esta lista vale tanto como el statement. |
| Cierre | 15 min | Lectura final + firma digital del statement v1. |

**Cómo sabes que funcionó:** un párrafo firmado + una lista *no-hace* de mínimo 5 ítems. Si al minuto 90 no hay statement firmado, **extiende 15 min y recorta S2**. No avances con ambigüedad.

**Output esperado:**
```
PROBLEM STATEMENT v1
Para [usuario] que sufre [dolor concreto y medible] cuando [contexto],
queremos [resultado deseado] sin [restricción dura].
Éxito se mide como [métrica única, observable, accionable].

NO-HACE (alcance excluido):
- ___
- ___
- ___
```

---

### S2 · Mapeo de oportunidades (90 min)

**Objetivo:** generar 2–3 hipótesis de solución y filtrarlas por evidencia, no por entusiasmo.

| Bloque | Tiempo | Qué hacen |
|---|---|---|
| Brainstorming dirigido | 25 min | Cada persona escribe en silencio 3 ideas de cómo resolver el problema con IA. Sin discutir. |
| Agrupar y descartar | 20 min | Se pegan en pizarra. Se agrupan duplicados. Se descartan las que no superan el filtro de 4 preguntas (abajo). |
| Hipótesis con evidencia | 35 min | Las 2–3 sobrevivientes se escriben como tabla: *hipótesis → evidencia que la respalda → métrica que la valida*. |
| Selección | 10 min | Voto con peso: el sponsor del problema vota último y desempata. |

**Filtro de 4 preguntas (cada hipótesis):**
1. ¿Tenemos datos o podemos conseguirlos en menos de 2 semanas?
2. ¿El problema tiene matices y no se resuelve con una regla determinista?
3. ¿Hay al menos 5 personas/casos por mes que lo sufren?
4. ¿Si la IA se equivoca, hay un paso humano antes de causar daño?

Menos de 3 sí → la hipótesis se descarta o se rebaja a "investigar antes".

**Output esperado:** tabla con 2–3 filas. Cada fila tiene: hipótesis · evidencia · métrica · banda tentativa (RAT / MVP / (R)Evolución).

---

### S3 · Vibe coding (90 min)

**Objetivo:** **construir** el prototipo. No pensar en construirlo. Construirlo.

**Stack permitido (elige UNO):**
- Conversación larga con ChatGPT, Claude o Gemini donde la IA hace lo que tu producto haría (wizard of oz textual).
- Sitio interactivo con v0, bolt, lovable o Replit (sin escribir código a mano).
- Notebook (Colab, Jupyter) con un flujo end-to-end usando un LLM por API.
- Mockup clickeable en Figma + IA generando los outputs reales.

**Reglas del vibe coding (no negociables):**

1. **Empezar feo.** Funcionalidad primero, estética después.
2. **Inicio y fin claros.** Alguien entra con una entrada real, alguien sale con una salida útil.
3. **Datos reales o sintéticos etiquetados.** Si inventas datos, dilo en pantalla.
4. **Snapshot cada 20 min.** Foto, captura, commit. Si rompes algo, hay vuelta atrás.
5. **3 prompts maestros guardados.** Los prompts son parte del entregable.
6. **Cero refactor.** Hoy se construye, no se ordena.
7. **Demo a otro equipo cada 30 min.** Feedback corto: *qué sorprende · qué confunde · qué falta*.
8. **Si te trabas 10 min, cambia de aproximación.** Otro modelo, otro prompt, otra herramienta.

**Cómo sabes que funcionó:** puedes mostrar el flujo completo a alguien externo en menos de 5 minutos y entiende qué hace.

---

### S4 · Spec destilada + plan 30 días (90 min)

**Objetivo:** la spec **emerge del prototipo**. Capturar lo aprendido y comprometer los siguientes 30 días con owner.

| Bloque | Tiempo | Qué hacen |
|---|---|---|
| Demo formal | 15 min | El equipo muestra el prototipo a sí mismo. Recorrido completo, sin saltarse pasos. |
| Destilación 3 lentes | 45 min | Llenar la plantilla *Es / Hace / F-NF* leyendo el prototipo, no la cabeza. Ver template más abajo. |
| Banda y FTE-meses | 15 min | Asignar banda RAT (1m) / MVP (3m) / (R)Evolución (16s) + estimación FTE-meses indicativa. |
| Plan 30 días + owner | 15 min | Cada iniciativa aprobada tiene **un owner explícito** y 3 hitos a 30 días. Sin owner, no se aprueba. |

**Cómo sabes que funcionó:** sales con una spec firmada, una banda asignada, un owner con nombre y apellido, y 3 hitos calendarizados.

---

## Reglas del juego (8, no negociables)

| Regla | Justificación corta |
|---|---|
| **1. La spec emerge del prototipo, no del papel.** | El papel oculta la complejidad real; el prototipo la expone. |
| **2. Evidencia > opinión.** | Cada afirmación se etiqueta `[DATO]`, `[OBSERVADO]`, `[INFERENCIA]` o `[SUPUESTO]`. Si >30% es supuesto, banner de advertencia. |
| **3. Reloj duro.** | Cada sesión termina cuando termina. La presión protege la decisión. |
| **4. NO-hace tiene tanto peso como Hace.** | Sin alcance excluido, la spec se infla durante consolidación. |
| **5. Owner explícito o no se aprueba.** | RACI completa es lujo; owner es mínimo. |
| **6. Snapshot cada 20 min en S3.** | El prototipo es el artefacto central; perderlo es perder el día. |
| **7. Si te trabas 10 min, cambia de aproximación.** | Persistir en una vía rota es la forma más cara de aprender. |
| **8. Parking lot visible.** | Toda idea fuera de scope va a una lista pública. Nada se pierde, nada se discute hoy. |

---

## Anti-patrones del profesional

| Anti-patrón | Señal temprana | Intervención |
|---|---|---|
| **"Deberíamos usar un LLM para…"** antes de tener problem statement. | Alguien menciona la solución en S1. | Conductor redirige al parking lot: *"seguimos en el problema."* |
| **Prototipo bonito antes que funcional.** | Más de 15 min en CSS / colores / layout en S3. | Cronómetro a la vista. Funcionalidad primero. |
| **Hipótesis sin métrica.** | "Vamos a mejorar la experiencia." | Forzar la pregunta: *"¿cómo lo medirías en 30 días?"*. Sin respuesta, no avanza. |
| **Sponsor que no firma.** | El sponsor delega la decisión a "lo vemos después". | Pausa la sesión. Sin firma del sponsor, no hay workshop. |
| **Equipo decide en paralelo sin compartir.** | Dos personas trabajan en cosas distintas y no hablan. | Forzar demo cruzada cada 30 min. |
| **Banda RAT/MVP asignada sin discutir hipótesis crítica.** | "Esto es MVP, claramente." | Pregunta de control: *"¿qué supuesto, si fuera falso, mata esta iniciativa?"*. Eso va al RAT primero. |

---

## Consolidación 48 h post-workshop

Cierra el día, arranca el reloj. **T + 48 h** entregas tres documentos livianos al equipo y al sponsor.

| Entregable | Para qué sirve | Largo máximo |
|---|---|---|
| **1. Spec destilada (limpia)** | La versión editada del template de S4, con los 3 lentes completos y banda asignada. | 1–2 páginas. |
| **2. Plan 30 días** | 3 hitos con fecha, owner por hito, criterio de éxito por hito. Si la banda es RAT, debe haber métrica binaria de la hipótesis crítica. | 1 página. |
| **3. Lista de riesgos** | Top 5 riesgos detectados durante el día, con dueño de seguimiento y acción mitigadora propuesta. | Media página. |

**Regla de oro:** los 3 entregables se publican juntos o no se publican. Documento aislado pierde contexto.

> **Por qué 48 h y no 5 días:** el profesional individual / equipo pequeño no necesita pipeline HITL formal. Necesita un cierre rápido que mantenga la energía del día. Lo que en Empresas toma 5 días con 5 etapas, aquí lo hace una persona en una tarde concentrada.

---

## Bandas RAT / MVP / (R)Evolución

| Banda | Plazo | FTE-meses indicativos | Cuándo se elige | Ejemplo |
|---|---|---|---|---|
| **RAT** (Riskiest Assumption Test) | 1 mes | 1–3 | Hay una hipótesis crítica sin validar. La métrica de éxito es binaria. | "¿Los usuarios prefieren respuesta de IA o humana en el chat de soporte?" |
| **MVP** | 3 meses | 4–10 | Hipótesis ya validada. Se busca **tracción medible** en cohorte real. | Asistente de búsqueda interno con DAU/WAU ≥ 0.4 a 8 semanas. |
| **(R)Evolución** | 16 semanas (4 meses) | 12–25 | MVP probó tracción y se escala a sistema productivo. | Ampliar el asistente a 3 áreas y conectar a fuentes oficiales con guardrails. |

> **Regla simple:** si no sabes en qué banda cae, es porque te falta validar la hipótesis crítica → empieza por **RAT**. La banda no se elige por ambición, se elige por evidencia.

> **Si la iniciativa proyecta más de 16 semanas:** este workshop no la cubre completa. Lo que sí hace es identificar el **primer RAT** que valida o invalida el supuesto más caro. Para conceptualización XL completa (big picture + cascada formal con gates comerciales), escala a la variante Empresas.

---

## KPIs del workshop

Mide tu propio workshop. Si fallan 2 o más, la próxima vez ajusta antes.

| KPI | Meta | Cómo se mide |
|---|---|---|
| Statement firmado al cierre de S1 | 100% | Firma digital o foto de pizarra. |
| Hipótesis con métrica al cierre de S2 | ≥ 2 hipótesis con métrica concreta | Tabla S2 revisada. |
| Prototipo demo-able al cierre de S3 | Sí / No | Demo de 5 min a alguien externo. |
| Spec con owner al cierre de S4 | 100% de iniciativas aprobadas | Tabla S4 sin TBD en columna owner. |
| Entregables 48 h publicados a tiempo | T+48 h | Timestamp del repositorio o doc compartido. |
| Energía del equipo al final | NPS interno ≥ +20 | 1 pregunta al cierre: *"¿recomendarías este formato a un colega?"*. |

---

## Glosario mínimo

- **Spec:** especificación destilada del prototipo en 3 lentes (Es / Hace / F-NF). Es el contrato de qué se construye y qué no.
- **Vibe coding:** construir un prototipo dirigiendo una IA en lenguaje natural, sin escribir código manual línea a línea. La IA hace, tú decides.
- **RAT (Riskiest Assumption Test):** experimento mínimo de 1 mes diseñado para validar o invalidar el supuesto más peligroso de una iniciativa. Resultado binario.
- **MVP:** producto mínimo de 3 meses que demuestra **tracción medible** (uso recurrente, retención) en cohorte real, no en prueba de concepto.
- **HITL (Human-in-the-Loop):** decisión clave revisada por un humano antes de tener efecto. En Profesional es ligero; en Empresas es pipeline formal.

---

## Template de spec destilada (3 lentes)

Llena uno por iniciativa aprobada. Sale del prototipo, no de la cabeza.

```
SPEC DESTILADA — [Nombre de la iniciativa]
Owner: ________________ · Banda: RAT / MVP / (R)Evolución · FTE-meses: ____

────────────────────────────────────────────────────
LENTE 1 · ES / NO ES
ES:        Qué es esta iniciativa, en una línea.
NO ES:     Qué se confunde con esto pero no lo es. Mínimo 3 ítems.

────────────────────────────────────────────────────
LENTE 2 · HACE / NO HACE
HACE:      Bullets de capacidades concretas (verbo + objeto + condición).
NO HACE:   Bullets de capacidades explícitamente excluidas. Mínimo 3 ítems.

────────────────────────────────────────────────────
LENTE 3 · FUNCIONAL / NO FUNCIONAL
FUNCIONAL (F):
- F1 · El sistema hace ___ cuando ___.
- F2 · ...

NO FUNCIONAL (NF) — cada uno con métrica observable:
- NF · Latencia: respuesta ≤ X segundos en P95.
- NF · Costo: ≤ X FTE-meses equivalentes por interacción / por mes.
- NF · Calidad: precisión ≥ X% en golden set de 30 casos.
- NF · Seguridad: log auditable + aprobación humana en acciones de tipo Y.

────────────────────────────────────────────────────
HIPÓTESIS CRÍTICA (solo banda RAT):
"Si [supuesto X] resultara falso, esta iniciativa se detiene o se pivota."
Métrica binaria de validación: __________________
```

**Regla:** ningún `NF` se firma sin métrica concreta. Si no sabes medirlo, va a la lista *requiere benchmark en RAT*.

---

## Cómo escalar a Empresas

Si en S2 detectas que la iniciativa supera 16 semanas, integra 3 o más áreas, o requiere aprobación de comité, **no la metas a la fuerza** en la banda (R)Evolución. Lo que haces:

1. **Acotas el RAT** que valida la hipótesis crítica (sigue siendo 1 mes, sigue siendo viable en formato Profesional).
2. **Documentas el big picture pendiente** en una sección "Para escalar a Empresas" en el plan 30 días.
3. **Recomiendas la variante Empresas** (2 días + consolidación HITL 5 días + ADRs + dimensionamiento P50/P80/P95) para la conceptualización completa, una vez el RAT haya pasado.

> **Principio:** Profesional valida la hipótesis. Empresas conceptualiza el sistema. Cada uno sirve mejor en su tamaño.

---

## Lo que llevas a casa

- **Un método replicable** que funciona la próxima vez con otro problema, sin necesidad de facilitador externo.
- **Una manera de dirigir IA con intención**: prompt + contexto + criterio de aceptación, en vez de "preguntale a ver".
- **Un prototipo, una spec y un plan** que cualquier compañero puede leer y ejecutar.
- **Confianza para decidir rápido con evidencia**, no por intuición ni por presión.

---

## Próximo nivel

Cuando este workshop te quede pequeño — porque ya lideras 5 iniciativas en paralelo, o porque la organización te pide cascadas comerciales formales — el siguiente paso es la **variante Empresas** (2 días workshop + consolidación HITL 5 días hábiles + handover técnico formal). Pídele a tu sponsor el playbook `playbook-workshop-discovery-ai-native-v2026.04.2.html`.

---

*Construido por profesionales · Human First, AI-Next · Por Javier Montaño · metodologia.info · v2026.04 Profesional · CC BY-NC-SA 4.0*
