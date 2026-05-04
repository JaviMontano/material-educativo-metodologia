# Ritual · Auditoría Mensual de Relevancia · 60 min

> Lo que era vanguardia se vuelve legado. Auditar mensual previene la obsolescencia silenciosa. v1.1.0.

| Concepto | Valor |
|---|---|
| Cadencia | 1× / mes · primer viernes |
| Tiempo | 60 min Default · 20 min Express · 120 min Marathon |
| Agente | `coach-revolucionar` |
| Output | `~/aprender-aprehender/audits/auditoria-{YYYY-MM}.md` con score 4-D × 3 skills + decisiones |
| Calendar invite | `assets/calendar-invites/auditoria-mensual.ics` |

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §Rituales + Framework 4-D + Prompt #5.
`[DOC]` Tasa de obsolescencia técnica: skill avg life-span se redujo de 30 años (1980s) a 5 años (2020s) (World Economic Forum 2023, *Future of Jobs Report*).

## Contrato

| Hace | No hace |
|---|---|
| Audita 3 skills más usadas con framework 4-D · datos mercado | Reemplaza decisiones con mentor humano · auditoría es input, no veredicto |
| Detecta Identity Attachment / Sunk Cost en tiempo real | Audita TODAS tus skills (eso es el ritual anual) · solo top-3 mensual |
| Genera narrativa profesional actualizada (LinkedIn/CV/oral) | Garantiza que el mercado coincida (es señal, no destino) |

`[LÍMITE]` Skills cross-cutting (comunicación, liderazgo) NO se auditan con 4-D directo. Audita la *manifestación específica*.
`[LÍMITE]` Si tu rol es 100% en proyectos legacy fijos, framework 4-D puede mostrar todo 🔴 sin que sea actionable inmediato. Trade-off: documentar como "consciente · plan transición rol".

## Protocolo · 60 min Default

### 0:00-0:05 · Identificar las 3 skills

```
Pregunta: "¿Cuáles 3 skills usé MÁS este mes?"

Si dudas, mira:
- Calendar (¿en qué temas pasaste tiempo?)
- Commits / proyectos
- Reuniones que dominaste

Las 3 que aparecen más → necesitan auditoría.
```

`[CRITERIO-ACEPTACIÓN]` Si no puedes nombrar las 3 con confianza · señal de que el mes fue disperso · auditar la dispersión es el output del ritual.

### 0:05-0:30 · Ejecutar Prompt #5 · framework 4-D (25 min)

```
TAREA: ejecutar Prompt #5 (Relevance Audit) en Perplexity
       (datos de mercado actualizados)

Para cada una de las 3 skills, evaluar:
- Vigencia (¿es current?)
- ROI (¿retorno por hora?)
- Obsolescencia (¿tendencia 5 años?)
- Demanda (¿job postings, salarios?)

Output: tabla 4-D + decisión [MANTENER/ACTUALIZAR/REEMPLAZAR/SOLTAR]
```

→ ver `prompts/05-relevance-audit.md`.

`[CASO-BORDE]` Si Perplexity dice "vigente global" pero tu mercado local muestra 0 postings 30d · bandera amarilla · decide por mercado, no por global.

### 0:30-0:45 · Validar evidencia (15 min)

| Cross-check | Fuente | Qué buscar |
|---|---|---|
| LinkedIn jobs | linkedin.com/jobs | Postings 30 días en TU región |
| Glassdoor | glassdoor.com | Salario promedio asociado |
| Stack Overflow Survey | survey.stackoverflow.co | Trending up/down (si tech) |
| Conferencias del campo | sitios oficiales | ¿Sigue en agenda 2026? |

Si datos manuales contradicen Prompt #5 · refinar decisión por evidencia local.

### 0:45-0:55 · Documentar decisiones (10 min)

Archivo: `~/aprender-aprehender/audits/auditoria-{YYYY-MM}.md`

```markdown
# Auditoría de Relevancia · {YYYY-MM}

**Fecha**: [hoy]
**Industria**: [...]
**Rol**: [...]

## Skill #1: [NOMBRE]

**Score 4-D**:
- Vigencia: 🟢/🟡/🔴 [evidencia con cifra]
- ROI: 🟢/🟡/🔴 [evidencia]
- Obsolescencia: 🟢/🟡/🔴 [tendencia]
- Demanda: 🟢/🟡/🔴 [job postings + salario]

**Decisión**: [MANTENER / ACTUALIZAR / REEMPLAZAR / SOLTAR]
**Razón** (1 frase): [síntesis evidence-driven]
**Plan de acción**: [específico · con fechas]
**Próxima auditoría**: [+3 meses]

## Skill #2 ... · Skill #3 ...

## Acciones generadas
- Si REEMPLAZAR/SOLTAR: agendar Workflow 1 con sucesora
- Si ACTUALIZAR: agendar Sprint 20h con versión moderna
- Si MANTENER: continuar inversión actual
```

### 0:55-1:00 · Actualizar narrativa profesional (5 min)

Genera 3 versiones reflejando decisiones:
- LinkedIn (200 chars)
- CV (3 bullets)
- Entrevista oral (60s)

Si soltaste algo · decláralo conscientemente · no lo escondas.

## Reglas duras

| Regla | Por qué |
|---|---|
| Datos > sentimiento | "Aún me gusta" no es decisión profesional |
| Documenta SIEMPRE · razón explícita | Tu yo de 2027 querrá saber: "¿por qué solté X en abril 2026?" |
| Si todo queda 🟢, sospecha | Toda industria tiene movimiento · 3/3 verdes en 6 meses = falta rigor |
| Sin "depende" sin condiciones | "Mantengo X SI [A] · suelto si [B]" · sin condiciones, no decidiste |

## Anti-patrones top-3 graves

| # | Anti-patrón | Detección | Antídoto |
|---|---|---|---|
| 1 | Identity Attachment | "X es parte de mí" / "soy [Skill] developer" | Tu identidad puede ser "el Diseñador que sabe soltar" · framework 4-D > ego |
| 2 | Sunk cost fallacy | "Pero invertí 1000h en X" | Esas horas ya están gastadas · pregunta: las próximas 1000h ¿dónde? |
| 3 | Auditorías superficiales | Todo queda 🟢 mes tras mes | Cross-check con LinkedIn local obligatorio · sospecha del 100% verde |

## Patrón saludable · 6 meses

```
Auditoría 2026-04: jQuery SOLTAR · System Design MANTENER · Python MANTENER
Auditoría 2026-05: React ACTUALIZAR a v19 · System Design MANTENER · Rust MANTENER (entró Workflow 1)
Auditoría 2026-06: React v19 completado MANTENER · System Design MANTENER · Rust MANTENER (Escala 3)

→ Patrón saludable: 1-2 cambios significativos al año · no 0 (estancado), no 5 (caos)
```

`[CRITERIO-ACEPTACIÓN]` 6 auditorías sin un solo cambio = estancamiento o auditorías superficiales · revisar rigor.

## Variantes

| Modo | Tiempo | Cuándo |
|---|---|---|
| **Express** | 20 min · 1 skill auditada | Mes con poco cambio |
| **Default** | 60 min · 3 skills | Por defecto · primer viernes |
| **Marathon** | 120 min · 5 skills + validación humana | Mes de cambios estratégicos · inicio de año |

### Marathon · 120 min

```
0:00-0:30 · Identificar 5 skills (no 3)
0:30-1:30 · Prompt #5 + cross-check manual × 5
1:30-1:50 · Validación humana · pregunta a colega senior:
   "¿Coincides con esta evaluación de [skill]?"
1:50-2:00 · Plan de carrera 12 meses revisado
```

## Métricas de éxito (6 meses)

```
[ ] 6 auditorías mensuales documentadas
[ ] ≥1 skill obsoleta soltada conscientemente
[ ] ≥2 skills actualizadas a versión moderna
[ ] LinkedIn refleja decisiones (no skills fantasma)
[ ] Recibes job offers para skills relevantes (no obsoletas)
```

`[CRITERIO-ACEPTACIÓN]` Si tras 6 meses · 0 cambios · 2 escenarios: (a) eres referente del campo y nada se mueve (raro · valida con peer), (b) auditorías superficiales (común · profundizar).

## Calendar invite

```
Día: primer viernes de cada mes 16:00
Duración: 60 min
Recurrencia: mensual
Bloque "deep work"
```

Archivo: `assets/calendar-invites/auditoria-mensual.ics`

## Referencias cruzadas

- `agents/coach-revolucionar.md`
- `prompts/05-relevance-audit.md`
- `references/02-tres-modelos-fundacionales.md` §Capability Models
- `references/04-anti-patrones-y-trampas.md` §Identity Attachment §Sunk Cost
- `katas/kata-soltar-legacy.md`
- `examples/ejemplo-revolucionar-jquery.md`
- `scripts/relevance_audit.py`

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · `[FUENTE-PRIMARIA]` Playbook v2.0.0
