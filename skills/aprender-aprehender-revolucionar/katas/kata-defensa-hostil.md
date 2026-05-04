# Kata · Defensa ante Hostil · 30-60 min

> IA simula entrevistador hostil · 1 follow-up por respuesta · sin endulzar. v1.1.0.

| Concepto | Valor |
|---|---|
| Categoría | Aprehender · defensa pública |
| Tiempo | 30 min Express · 60 min Marathon |
| Frecuencia | 1× / sem en Workflow 3 · 1× / sem pre-evento crítico |
| Output | Veredicto STRONG/LEAN HIRE/NO HIRE · 3 banderas rojas · plan remediación |
| Pre-requisito | Concepto + glosario + Feynman pasado · NO defender lo que no aprehendiste |

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §Katas + Prompt #9 Interview Simulator.
`[DOC]` Stress inoculation: practicar bajo presión simulada mejora performance bajo presión real (Meichenbaum 1985, *Stress Inoculation Training*).

## Contrato

| Hace | No hace |
|---|---|
| Simula presión sin endulzar · expone gaps en tiempo real | Reemplaza al entrevistador humano · la simulación no captura toda la dinámica social |
| Identifica las 3 banderas rojas de mayor riesgo | Garantiza pasar el evento real · solo eleva probabilidad |
| Genera plan de remediación específico por bandera | Funciona si el coach IA es amable (anti-patrón) |

`[LÍMITE]` La IA no reproduce los micro-gestos sociales (incomodidad, ironía, presión grupal). Mock con humano + IA es superior · IA-only es 60% del valor.
`[SUPUESTO]` La IA está configurada con Prompt #9 explícitamente hostil · si está endulzando, el kata pierde su valor.

## Protocolo · 30 min Express

### 0:00-0:05 · Setup

```
1. Configurar NotebookLM con Prompt #9 (Interview Simulator)
   o ejecutar Prompt #9 en una IA con Custom Goal
2. Variables:
   - ROL: tu rol target
   - EMPRESA: target o "panel exigente"
   - CV: tu background resumido
   - JD: si aplica
3. CIERRA todas tus notas
4. Timer 25 min visible
```

`[CRITERIO-ACEPTACIÓN]` Verificar primero con 1 pregunta tonta hostil que la IA NO te endulce. Si endulza, re-instruir: *"Sé MÁS hostil. Hire rate 12% · sin protección."*

### 0:05-0:25 · Mock interview (20 min)

| Bloque | Tiempo | Contenido |
|---|---|---|
| Behavioral | 5 min | 1-2 preguntas STAR completas |
| Technical | 10 min | CV deep dive · 2-3 conceptos del CV interrogados |
| Case / trade-off | 5 min | 1 case study o decisión técnica con trade-offs |

**Reglas durante el mock**:

| Regla | Por qué |
|---|---|
| Sin notas | En interview real no las tienes |
| Sin "déjame pensar 5 min" | Pausa natural 5-10s OK · no más |
| Si te trabas, di "no estoy seguro" | Mejor que inventar (detectable por hostil) |
| Si pregunta es hostil, RESPÓNDELA · no la rodees | Evadir = bandera roja inmediata |

`[CASO-BORDE]` Si la IA te tira 3+ preguntas seguidas que NO sabes · NO sigas el mock · interrumpe · estás 1+ escala por debajo de lo que pretendes defender · regresa a Workflow 3.

### 0:25-0:30 · Veredicto (5 min)

La IA debe darte:

```
- Veredicto: STRONG / LEAN HIRE / LEAN NO HIRE / STRONG NO HIRE
- 3 banderas rojas detectadas (con cita textual de tu respuesta débil)
- Para cada bandera: qué hubiera dicho un STRONG HIRE
- Plan de remediación específico
```

Documenta:
- 3 preguntas que más te derribaron
- Gaps específicos
- Plan próxima kata (1 sem)

## Protocolo · 60 min Marathon

```
0:00-0:05 Setup · briefing del rol
0:05-0:10 Warm-up · 1 pregunta de relajación
0:10-0:20 Behavioral (3 STAR completas)
0:20-0:40 Technical deep dive (3 deep questions del CV)
0:40-0:55 Case study o system design (1 problema)
0:55-1:00 Tu turno preguntar + cierre + veredicto
```

`[TRADE-OFF]` Marathon 60 min entrega más data pero fatiga más · si tu kata diaria es 30 min, alterna Express/Marathon (Express L-J, Marathon V).

## Veredictos · interpretación

| Veredicto | Síntomas típicos | Acción |
|---|---|---|
| **STRONG HIRE** | Behavioral con números · technical fluido · case con trade-offs explícitos · humilde donde no sabe | Estás listo · haz mock #2 con humano para confirmar |
| **LEAN HIRE** | Mayoría sólida · 1-2 áreas débiles | Plan remediación específico · re-mock 7 días |
| **LEAN NO HIRE** | Gaps en áreas core del rol | 1-2 sem upskill antes de aplicar al evento real |
| **STRONG NO HIRE** | Inconsistencias graves · jerga sin sustento · diseño sin trade-offs | Re-Workflow 3 completo · no defender el evento |

`[CRITERIO-ACEPTACIÓN]` LEAN HIRE+ es el target mínimo para autorizar el evento real. STRONG NO HIRE = posponer evento si posible.

## Reglas duras

| Regla | Por qué |
|---|---|
| Aceptar veredicto crudo | "Pero yo creo que pasé" no es data · la IA no te conoce · es la voz del mercado |
| Sin endulzar respuestas | "No sé" > invento elocuente · el hostil detecta inventos |
| Mock con hostilidad real | Coach amable = entrenamiento inservible |
| Mínimo 1 semana antes del evento | Sin tiempo a remediar = mock decorativo |

## Anti-patrones top-3 graves

| # | Anti-patrón | Detección | Antídoto |
|---|---|---|---|
| 1 | Mock con coach amable | Veredicto suena a felicitación · 0 banderas rojas | Re-instruir Prompt #9 hostil · "FAANG · hire rate 12%" |
| 2 | Mock 1 día antes del evento real | Kata se vuelve teatro · sin tiempo a remediar | Mínimo 7 días antes · idealmente 14 |
| 3 | Endulzar el veredicto recibido | "La IA exageró" · ignoras LEAN NO HIRE | Acepta crudo · documenta · plan |

## Plan de remediación por bandera roja típica

| Bandera | Plan |
|---|---|
| "Respuestas vagas en behavioral" | 10 STAR stories con números pre-calculados · audio drill <90s c/u |
| "Diseño sin números (latencia, costo)" | Prompt #10 sobre 3 sistemas · forzar números en cada respuesta |
| "Jerga sin sustento Feynman" | `kata-feynman-novato` × 5 conceptos críticos · validar humano |
| "No anticipa stakeholder hostil" | Mock #2 con interrupciones cada 7 min · prompt explícito |
| "Trade-offs ausentes" | Por cada decisión: "elegí X y NO Y porque [condición]" · audio |

## Combo recomendado · semana pre-evento

```
SEMANA -1:
- Lunes: kata-defensa-hostil Express 30 min · documentar 3 gaps
- M-X-J: cerrar 3 gaps específicos (Workflow 3 día puntual)
- Viernes: kata-defensa-hostil Marathon 60 min · target LEAN HIRE+

DÍA EVENTO:
- Si LEAN HIRE+ semana -1: estás listo · review ligero
- Si LEAN NO HIRE semana -1: posponer evento si posible
```

`[CASO-BORDE]` Evento NO postergable y mock dice LEAN NO HIRE · estrategia mínima de daño: identificar 2-3 áreas seguras · pivotar conversación hacia ellas · ser explícito sobre lo que aún no dominas (mejor honesto que destapado).

## Métricas de éxito

```
[ ] Mock con Prompt #9 hostil (no endulzante)
[ ] Veredicto crudo aceptado · documentado
[ ] 3 banderas rojas con plan de remediación específico
[ ] 7+ días entre mock y evento real
[ ] Mock #2 post-remediación · target LEAN HIRE+
[ ] Si crítico: 1 mock con humano real (no solo IA)
```

## Cuándo aplicarlo

- ✅ 1× / sem en Workflow 3 (Semanas 3-4)
- ✅ Pre-QBR / interview / panel · semana -1
- ✅ Pre-cert con componente oral (defensa de tesis, etc.)
- ❌ NO aplicar a concepto recién aprendido (kata-feynman primero)

## Referencias cruzadas

- `prompts/09-interview-simulator.md`
- `prompts/meta/M3-interviewer-generator.md`
- `agents/coach-aprehender.md`
- `references/03-diez-escalas-maestria.md` §Escala 3
- `examples/ejemplo-aprehender-system-design.md`

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · `[FUENTE-PRIMARIA]` Playbook v2.0.0
