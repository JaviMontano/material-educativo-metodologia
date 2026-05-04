# Kata · Soltar Legacy · 30 min

> Auditar 1 skill bajo duda · framework 4-D · decidir y documentar. v1.1.0.

| Concepto | Valor |
|---|---|
| Categoría | (R)Evolucionar · auditoría puntual single-skill |
| Tiempo | 30 min |
| Frecuencia | Ad-hoc cuando dudas si una skill aún sirve |
| Output | Score 4-D · decisión MANTENER/ACTUALIZAR/REEMPLAZAR/SOLTAR · plan reskill |
| Distinto del | `ritual-auditoria-mensual.md` (este es single-skill, ad-hoc) |

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §Katas + Framework 4-D + Prompt #5.

## Contrato

| Hace | No hace |
|---|---|
| Aplica framework 4-D con datos de mercado actuales | Decide por ti · te da evidencia · tú decides |
| Detecta Identity Attachment / Sunk Cost en tiempo real | Audita skills cross-cutting (comunicación, liderazgo) · esas son atemporales |
| Genera plan reskill obligatorio si SOLTAR | Reemplaza la conversación con mentor humano para decisiones high-stakes |

`[LÍMITE]` Skills aún en Escala 0-2 (en aprendizaje) NO se auditan con 4-D. Termina Workflow 1-3 antes de evaluar relevancia.
`[LÍMITE]` Skills cross-cutting no se auditan con 4-D directo. Audita la *manifestación específica* (ej. "comunicación ejecutiva bilingüe en mi industria").

## Protocolo · 30 min

### 0:00-0:05 · Declarar la skill bajo duda

```
SKILL: [nombre exacto · sin ambigüedad]
HORAS HISTÓRICAS INVERTIDAS: ~X
ÚLTIMA VEZ EN PROYECTO REAL: [fecha]
RAZÓN DE LA DUDA: [por qué cuestionas · 1 frase]
ESCALA ACTUAL: [3-9 · si <3, NO auditar]
```

`[CRITERIO-ACEPTACIÓN]` Si Escala <3 · interrumpe kata · esta skill aún está en aprendizaje · audítala cuando llegues a Escala 3+.

### 0:05-0:20 · Framework 4-D (Prompt #5 condensado)

Pregunta a Perplexity (datos mercado actuales):

```
Evalúa la skill [SKILL] para mi industria [INDUSTRIA] en
[PAÍS/REGIÓN]. Aplica framework 4-D:

1. Vigencia: ¿es current en job postings 2026?
2. ROI: ¿retorno por hora invertida hoy vs hace 5 años?
3. Obsolescencia: ¿tendencia 5 años? ¿hay sucesor obvio?
4. Demanda: ¿salario, postings, velocidad de cierre?

Cita fuentes. Cifras concretas. Sin endulzar.
```

`[TRADE-OFF]` Perplexity da datos web actuales pero puede sobrerepresentar US/EU · si tu mercado es LatAm/APAC, complementa con LinkedIn jobs locales.

### 0:20-0:25 · Validación cruzada (5 min)

| Cross-check | Fuente | Qué buscar |
|---|---|---|
| LinkedIn jobs · últimos 30 días | linkedin.com/jobs | ¿Cuántos postings mencionan la skill? |
| Stack Overflow Survey 2024-2026 | survey.stackoverflow.co | Trending o declining? (si tech) |
| Conferencias del campo · agenda | sitios oficiales | ¿Sigue en agenda? ¿Tracks dedicados? |
| Tu industria · job boards locales | InfoJobs, Computrabajo, etc. | Confirmación local |

`[CASO-BORDE]` Si Perplexity dice "vigente" pero LinkedIn local muestra 0 postings 30 días · bandera amarilla · skill global pero NO en tu mercado · decide por mercado, no por global.

### 0:25-0:30 · Decisión + documentación

```
Score 4-D consolidado:
- Vigencia:        🟢 / 🟡 / 🔴
- ROI:             🟢 / 🟡 / 🔴
- Obsolescencia:   🟢 / 🟡 / 🔴
- Demanda:         🟢 / 🟡 / 🔴
```

| Patrón | Decisión |
|---|---|
| 3-4 verde | **MANTENER** · profundizar X · tiempo Y |
| 2 verde + 2 amarillo | **ACTUALIZAR** · estudiar versión moderna · 20h Sprint |
| 1 verde + 3 rojo/amarillo | **REEMPLAZAR** · skill sucesora [...] · transición 6 meses |
| 3-4 rojo | **SOLTAR** · stop invertir · plan reskill obligatorio |

```
DOCUMENTAR EN:
- ~/aprender-aprehender/audits/kata-{skill}-{YYYY-MM-DD}.md
- Actualizar `.aprender-state.json` si SOLTAR
- Si público: post LinkedIn como "lección de carrera"
```

## Reglas duras

| Regla | Por qué |
|---|---|
| Aceptar evidencia · no sentimiento | "Aún me gusta" no es decisión profesional |
| Sin "depende" sin condiciones explícitas | "Mantengo X SI [A] · suelto si [B]" · sin condiciones, no decidiste |
| Plan reskill obligatorio si SOLTAR | NO soltar sin sucesora definida |
| MANTENER vence en 3 meses | Re-auditar trimestralmente · el mercado se mueve |

## Anti-patrones top-3 graves

| # | Anti-patrón | Detección | Antídoto |
|---|---|---|---|
| 1 | Identity Attachment | "X es parte de mí" / "soy [Skill] developer" | Tu identidad puede ser "el que sabe soltar" · Diseñador de carrera |
| 2 | Sunk cost fallacy | "Pero invertí 1000h" | Esas horas ya están gastadas · pregunta: las próximas 1000h ¿dónde? |
| 3 | SOLTAR sin sucesora | "Suelto X · ya veré qué hago" | Sucesora definida ANTES de soltar · si no, postpone decisión |

## Casos especiales

### Skill solo usada en proyectos legacy

```
Vigencia: 🔴 (mercado nuevo no la pide)
ROI: 🟡 (proyectos legacy aún pagan)
Obsolescencia: 🔴 (legacy se contrae)
Demanda: 🔴 (mercado nuevo no la lista)

Decisión típica: SOLTAR · pero si tu rol específico depende de
proyectos legacy, MANTENER MÍNIMO VIABLE hasta transición de rol.
```

### Skill que combina partes vigentes con partes obsoletas

```
Ejemplo: SQL (vigente) + procedimientos almacenados de Oracle 9i (obsoleto)

Audita por componentes:
- Core SQL: MANTENER
- Procedimientos Oracle 9i: SOLTAR
- Plan: profundizar SQL moderno · soltar específicamente lo legacy
```

`[CASO-BORDE]` La skill se siente "vigente pero estancada" · síntoma de mercado saturado · ROI cae aunque vigencia se mantenga · revisa: ¿hay sucesora premium emergiendo?

## Output documentado · plantilla

```markdown
# Kata Soltar Legacy · {SKILL} · {YYYY-MM-DD}

## Skill auditada
**Nombre**: [...]
**Horas históricas invertidas**: ~X
**Última vez en proyecto real**: [fecha]
**Escala actual**: [3-9]

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
[síntesis · evidencia-driven]

## Plan de acción
[específico · con fechas · si REEMPLAZAR/SOLTAR: skill sucesora definida]

## Si SOLTAR · narrativa profesional
- LinkedIn: "Decidí soltar [SKILL] cuando vi [evidencia] · ahora invierto en [Y]"
- Próximo Workflow 1: [skill sucesora · fecha]

## Próxima auditoría de esta skill
[+3 meses si MANTENER · N/A si SOLTAR]
```

## Métricas de éxito

```
[ ] Score 4-D con evidencia citada (no opinión)
[ ] Decisión documentada con plan específico
[ ] Si SOLTAR: skill sucesora definida + plan Workflow 1
[ ] .aprender-state.json actualizado
[ ] Re-auditar agendada (+3 meses si MANTENER)
```

## Referencias cruzadas

- `prompts/05-relevance-audit.md`
- `agents/coach-revolucionar.md`
- `rituals/ritual-auditoria-mensual.md`
- `references/04-anti-patrones-y-trampas.md` §Identity Attachment · §Sunk Cost
- `examples/ejemplo-revolucionar-jquery.md`

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · `[FUENTE-PRIMARIA]` Playbook v2.0.0
