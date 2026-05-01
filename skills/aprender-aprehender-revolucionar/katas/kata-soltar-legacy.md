# Kata · Soltar Legacy · 30 min

> Auditar 1 skill · decidir [MANTENER/RELEASE] · documentar.

**Categoría**: (R)Evolucionar · auditoría puntual
**Tiempo**: 30 min
**Frecuencia**: ad-hoc cuando dudas si una skill aún sirve

---

## Objetivo

Tomar una skill específica que **dudas si vale la pena seguir manteniendo** · evaluarla con framework 4-D · decidir y documentar.

Distinto del Ritual Auditoría Mensual: este kata es **single-skill, ad-hoc**.

---

## Protocolo · 30 min

### 0:00-0:05 · Declarar la skill bajo duda

```
SKILL: [nombre exacto]
HORAS INVERTIDAS HISTÓRICAS: [estimado]
ÚLTIMA VEZ QUE LA USÉ EN PROYECTO REAL: [fecha]
RAZÓN DE LA DUDA: [por qué la cuestionas]
```

### 0:05-0:20 · Framework 4-D (Prompt #5 condensado)

```
Pregunta a Perplexity (con datos de mercado actualizados):

"Evalúa la skill [SKILL] para mi industria [INDUSTRIA] en
[PAÍS / REGIÓN]. Aplica framework 4-D:

1. Vigencia: ¿es current en job postings 2026?
2. ROI: ¿retorno por hora invertida hoy vs hace 5 años?
3. Obsolescencia: ¿tendencia 5 años? ¿hay sucesor obvio?
4. Demanda: ¿salario, postings, velocidad de cierre?

Cita fuentes. Cifras concretas. Sin endulzar."
```

### 0:20-0:25 · Validación cruzada (5 min)

```
Cross-check manualmente:
1. LinkedIn jobs · cuántos en últimos 30 días mencionan la skill?
2. Stack Overflow Survey 2024-2026 (si tech) · trending?
3. Conferencias del campo · sigue en agenda?

Si cifras coinciden con Prompt #5 → confiable
Si difieren mucho → re-validar manual
```

### 0:25-0:30 · Decisión + documentación

```
Score 4-D consolidado:
- Vigencia:        🟢 / 🟡 / 🔴
- ROI:             🟢 / 🟡 / 🔴
- Obsolescencia:   🟢 / 🟡 / 🔴
- Demanda:         🟢 / 🟡 / 🔴

DECISIÓN (basada en regla):
- 3-4 verde     → [MANTENER]
- 2 verde + 2 amarillo → [ACTUALIZAR]
- 1 verde + 3 rojo/amarillo → [REEMPLAZAR]
- 3-4 rojo     → [SOLTAR]

PLAN DE ACCIÓN:
- Si MANTENER: profundizar X · tiempo Y
- Si ACTUALIZAR: estudiar versión moderna · 20h Sprint
- Si REEMPLAZAR: skill sucesora [...] · plan transición 6 meses
- Si SOLTAR: stop invertir · plan reskill [Y]

DOCUMENTAR EN:
- ~/aprender-aprehender/audits/kata-{skill}-{YYYY-MM-DD}.md
- Actualizar `.aprender-state.json` si SOLTAR
- Si público amerita: post LinkedIn como "lección de carrera"
```

---

## Reglas

### Aceptar evidencia · no sentimiento

Si la data dice 4/4 rojo, decisión = [SOLTAR]. "Pero todavía me gusta" no es decisión profesional.

### Sin "depende"

Define las condiciones explícitas. *"Mantengo X SI [condición A] · suelto si [B]."* Sin condiciones, no decidiste.

### Plan reskill obligatorio si [SOLTAR]

No suelto sin reemplazo. Define skill sucesora · agenda Workflow 1.

### Si decides MANTENER · revisar próximo trimestre

Las decisiones MANTENER tienen vencimiento · 3 meses · re-auditar.

---

## Anti-patrones

| Error | Síntoma | Corrección |
|---|---|---|
| Identity Attachment | "X es parte de mí" | Tu identidad puede ser "el que sabe soltar" |
| Sunk cost | "Pero invertí 1000h" | Ya están gastadas · pregunta: ¿próximas 1000h dónde? |
| Defender por confort | "X es lo que mejor manejo" | Eso no es razón profesional |
| [SOLTAR] sin sucesor | Vacío peligroso | Define sucesora antes de soltar |
| Auditar opiniones | "¿Es buena la opinión Y?" | Solo skills medibles |

---

## Casos especiales

### Skill aún Escala 0-2 (en aprendizaje)

NO auditar todavía con 4-D. Está en fase Aprender. Termina Workflow 1-3 antes de evaluar relevancia.

### Skill cross-cutting (comunicación, liderazgo)

NO se evalúa con 4-D directo. Esas son atemporales. Lo que SÍ evalúas: la **manifestación específica** (ej. "comunicación ejecutiva bilingüe en mi industria").

### Skill que solo usas en proyectos legacy

```
Si tu única exposición es proyectos legacy:
- Vigencia: 🔴 (mercado nuevo no la pide)
- ROI: 🟡 (los proyectos legacy aún pagan)
- Obsolescencia: 🔴 (en declive · proyectos legacy se contraen)
- Demanda: 🔴 (mercado nuevo no la lista)

Decisión típica: [SOLTAR] · pero si tu rol específico depende
de proyectos legacy, [MANTENER mínimo viable] hasta transición.
```

---

## Output documentado · plantilla

```markdown
# Kata Soltar Legacy · {SKILL} · {YYYY-MM-DD}

## Skill auditada
**Nombre**: [...]
**Horas históricas invertidas**: ~X
**Última vez en proyecto real**: [fecha]

## Score 4-D
| Dimensión | Score | Evidencia |
|---|---|---|
| Vigencia | 🟢/🟡/🔴 | [cifra + fuente] |
| ROI | 🟢/🟡/🔴 | [cifra + fuente] |
| Obsolescencia | 🟢/🟡/🔴 | [tendencia + fuente] |
| Demanda | 🟢/🟡/🔴 | [job postings + salario] |

## Decisión
[MANTENER / ACTUALIZAR / REEMPLAZAR / SOLTAR]

## Razón (1 frase)
[síntesis]

## Plan de acción
[específico · con fechas]

## Si SOLTAR · narrativa profesional
- LinkedIn: "Decidí soltar [SKILL] cuando vi [evidencia] · ahora invierto en [Y]"
- Próximo Workflow 1: [skill sucesora · fecha]

## Próxima auditoría de esta skill
[+3 meses si MANTENER · N/A si SOLTAR]
```

---

## Referencias

- `prompts/05-relevance-audit.md`
- `agents/coach-revolucionar.md`
- `rituals/ritual-auditoria-mensual.md`
- `references/04-anti-patrones-y-trampas.md` §Identity Attachment
- `examples/ejemplo-revolucionar-jquery.md`

---

> **Kata Soltar Legacy** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
