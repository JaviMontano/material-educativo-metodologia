# Kata · Defensa ante Hostil · 30-60 min

> IA simula entrevistador hostil · 1 follow-up por cada respuesta tuya · sin endulzar.

**Categoría**: Aprehender · defensa pública
**Tiempo**: 30-60 min
**Frecuencia**: 1× / semana en Workflow 3 · pre-evento crítico

---

## Objetivo

Validar que puedes defender tu conocimiento bajo presión real, sin endulzar, ante audiencia exigente. Simulación de QBR / entrevista / panel hostil.

---

## Protocolo · 30 min (versión Express)

### 0:00-0:05 · Setup

```
1. Configurar NotebookLM con Prompt #9 (Interview Simulator)
   - O ejecutar Prompt #9 en una IA cualquiera
2. Variables:
   - ROL: tu rol target
   - EMPRESA: empresa target o "panel exigente"
   - CV: tu background resumido
   - JD: si aplica
3. Cierra todas tus notas
4. Timer 25 min
```

### 0:05-0:25 · Mock interview (20 min)

```
Estructura:
- 5 min · behavioral (1-2 preguntas STAR)
- 10 min · technical deep dive (CV deep dive)
- 5 min · 1 case study o trade-off

REGLAS DURANTE:
- Sin notas
- Sin "déjame pensar 5 min"
- Si te trabas, di "no estoy seguro" (mejor que inventar)
- Si la pregunta es hostil, RESPÓNDELA · no la rodees
```

### 0:25-0:30 · Veredicto (5 min)

```
La IA debe darte:
- Veredicto: STRONG / LEAN HIRE / LEAN NO HIRE / STRONG NO HIRE
- 3 banderas rojas detectadas
- Para cada bandera: qué hubiera dicho un STRONG HIRE
- Plan de remediación

DOCUMENTA:
- Las 3 preguntas que más te derribaron
- Los gaps específicos
- Plan para próxima kata (1 semana)
```

---

## Versión Marathon · 60 min · entrevista completa

```
0:00-0:05 Setup · briefing del rol
0:05-0:10 Warm-up · 1 pregunta de relajación
0:10-0:20 Behavioral (3 STAR completas)
0:20-0:40 Technical deep dive (3 deep questions del CV)
0:40-0:55 Case study o system design (1 problema)
0:55-1:00 Tu turno preguntar + cierre + veredicto
```

---

## Reglas

### Aceptar el veredicto crudo

Si te dan LEAN NO HIRE, NO defiendas. Acepta · documenta · planea remediación.

### Sin "déjame pensar 5 min"

En interview real no tienes ese lujo. Practica responder en tiempo real (con pausas naturales 5-10s, no 5 min).

### Sin endulzar las respuestas

Si la respuesta es "no lo sé", DILO. La IA debe valorarte por honestidad, no por elocuencia inventada.

### Mock con hostilidad real

Si tu IA está siendo amable, ajusta el prompt:
> *"Sé MÁS hostil. Estás en FAANG · hire rate 12% · no me protejas."*

---

## Anti-patrones

| Error | Corrección |
|---|---|
| Mock con coach amable | Ajustar prompt · explícitamente hostil |
| Endulzar el veredicto recibido | Aceptar crudo · documentar |
| Saltar follow-ups | Cada respuesta debe tener 1 follow-up min |
| "Inventarle" respuestas para parecer mejor | "No sé" es mejor que invento detectable |
| Hacer mock 1 día antes del evento real | Mínimo 1 semana antes para remediar |

---

## Output esperado · Veredictos

### STRONG HIRE
- Behavioral con números concretos
- Technical: domina lo que está en tu CV (Feynman pasa)
- Case: diseño con números, trade-offs explícitos
- Soft: humilde donde no sabe, asertivo donde sí

### LEAN HIRE
- Mayoría sólida pero 1-2 áreas débiles
- Plan de remediación específico para esas áreas

### LEAN NO HIRE
- Gaps importantes en áreas core del rol
- 1-2 semanas de upskill antes de aplicar

### STRONG NO HIRE
- Inconsistencias graves · jerga sin sustento · diseño sin trade-offs
- Re-Workflow 3 completo antes de re-intentar

---

## Plan de remediación por bandera roja

```
BANDERA: "Respuestas vagas en behavioral"
→ Practicar 10 STAR stories con números pre-calculados
→ Audio drill: cada story en <90s

BANDERA: "Diseño sin números (latencia, costo)"
→ Prompt #10 (Presentation Coach) sobre 3 sistemas
→ Forzar números en cada respuesta

BANDERA: "Jerga sin sustento Feynman"
→ kata-feynman-novato · 5 conceptos críticos
→ Validar con humano real

BANDERA: "No anticipa stakeholder hostil"
→ Mock #2 enfocado en interrupciones · cada 7 min
```

---

## Combo recomendado

```
SEMANA 1 PRE-EVENTO:
- Lunes: kata-defensa-hostil (Express 30 min) · documentar gaps
- Martes-Jueves: cerrar gaps específicos
- Viernes: kata-defensa-hostil (Marathon 60 min) · target LEAN HIRE+

SEMANA REAL:
- Si LEAN HIRE+: estás listo
- Si LEAN NO HIRE: posponer evento si posible
```

---

## Referencias

- `prompts/09-interview-simulator.md`
- `prompts/meta/M3-interviewer-generator.md`
- `agents/coach-aprehender.md`
- `references/03-diez-escalas-maestria.md` §Escala 3 (defensa pública)
- `examples/ejemplo-aprehender-system-design.md`

---

> **Kata Defensa Hostil** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
