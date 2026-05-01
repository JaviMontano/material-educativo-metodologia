# Ritual · Auditoría Mensual de Relevancia · 1 hora

> Lo que era vanguardia se vuelve legado. Auditar mensual previene la obsolescencia silenciosa.

**Cadencia**: 1× / mes · primer viernes del mes
**Tiempo**: 60 minutos
**Agente**: `coach-revolucionar`
**Calendar invite**: `assets/calendar-invites/auditoria-mensual.ics`

---

## Por qué este ritual

Tu industria evoluciona. Las skills que eran críticas hace 5 años pueden ser legacy hoy. Sin auditoría mensual, te conviertes en el experto de algo que el mercado dejó de demandar.

**Anti-patrón a evitar**: identity attachment ("X es parte de mi identidad").
**Antídoto**: framework 4-D objetivo · datos > sentimiento.

---

## Protocolo · 60 minutos

### 0:00-0:05 · Identificar las 3 skills

```
PREGUNTA INICIAL:
"¿Cuáles 3 skills usé MÁS este mes?"

Si dudas, mira tu calendar / commits / proyectos del mes.

Las 3 que aparecen más → son las que necesitan auditoría.
```

### 0:05-0:30 · Ejecutar Prompt #5 (4-D framework)

```
TAREA: ejecutar Prompt #5 (Relevance Audit) en Perplexity
       (datos de mercado actualizados)

Para cada una de las 3 skills, evaluar:
- Vigencia (es current?)
- ROI (retorno por hora?)
- Obsolescencia (tendencia 5 años?)
- Demanda (job postings, salarios?)

Output esperado: tabla 4-D + decisión [MANTENER/ACTUALIZAR/
REEMPLAZAR/SOLTAR] por cada una.
```

→ ver `prompts/05-relevance-audit.md`.

### 0:30-0:45 · Validar evidencia

```
Para cada decisión, validar manualmente con cross-check:

1. LinkedIn jobs · cuántos postings mencionan la skill (Colombia/LatAm)?
2. Glassdoor · salario promedio asociado?
3. Stack Overflow Survey (si tech) · trending up or down?
4. Conferencias · sigue en agenda 2026?

Si los datos manuales contradicen la respuesta de Prompt #5,
refinar la decisión.
```

### 0:45-0:55 · Documentar decisiones

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

**Razón** (1 frase):
[síntesis]

**Plan de acción**:
[específico]

**Próxima auditoría**: [+3 meses]

## Skill #2: ...
## Skill #3: ...

## Acciones generadas

- Si REEMPLAZAR/SOLTAR: agendar Workflow 1 con sucesora
- Si ACTUALIZAR: agendar Sprint 20h con versión moderna
- Si MANTENER: continuar inversión actual
```

### 0:55-1:00 · Actualizar narrativa profesional

Genera 3 versiones:
- LinkedIn (200 chars)
- CV (3 bullets)
- Entrevista oral (60s)

Refleja las decisiones tomadas. Si soltaste algo, decláralo conscientemente.

---

## Reglas de oro

### Sé honesto · datos > sentimiento

Si la evidencia dice 🔴 ROJO en 4/4 dimensiones, decisión = [SOLTAR].
"Pero todavía me gusta usarla" no es decisión profesional.

### Documenta SIEMPRE

La auditoría no es solo decidir: es **registrar la decisión** con razón.
Tu yo de 2027 querrá saber: "¿por qué solté X en abril 2026?"

### Si todo queda 🟢, sospecha

Si todas tus skills quedan 🟢 ALTAS, probablemente NO estás auditando con rigor.
Toda industria tiene skills que se mueven · siempre hay algo a actualizar / soltar.

### Sin "depende"

Si la decisión queda *"depende"*, exigir las condiciones:
*"Mantengo X SI [condición] · suelto si [otra condición]."*
Sin condiciones explícitas, no decidiste.

---

## Output esperado · Ejemplo (3 meses consecutivos)

### Auditoría 2026-04
- jQuery: SOLTAR
- System Design: MANTENER
- Python: MANTENER

### Auditoría 2026-05
- React: ACTUALIZAR a v19
- System Design: MANTENER
- Rust: MANTENER (nuevo · resultado de soltar jQuery hace 3 meses · ya en Escala 2)

### Auditoría 2026-06
- React v19: completado · MANTENER
- System Design: MANTENER
- Rust: MANTENER (Escala 3 alcanzada)

Patrón saludable: 1-2 cambios significativos al año, no 0, no 5.

---

## Variantes

### Express · 20 min (mes con poco cambio)

Solo 1 skill auditada en lugar de 3.

### Marathon · 2 horas (mes de cambios estratégicos)

- Auditar 5 skills (no 3)
- Validación humana adicional (preguntar a colega senior)
- Plan de carrera 12 meses revisado

---

## Métricas de éxito

Después de 6 meses con el ritual:

```
✅ Tengo log de 6 auditorías mensuales documentadas
✅ He soltado al menos 1 skill obsoleta consciente
✅ He actualizado al menos 2 skills a versión moderna
✅ Mi LinkedIn refleja las decisiones (no skills fantasma)
✅ Recibo job offers para skills relevantes (no obsoletas)
```

Si NO:
- Estás haciendo auditorías superficiales · profundizar
- Estás aferrado a identidad · Identity Attachment

---

## Calendar Invite

```
Día: primer viernes de cada mes 16:00
Duración: 60 min
Recurrencia: mensual
Bloque "deep work"
```

Archivo: `assets/calendar-invites/auditoria-mensual.ics`

---

## Referencias

- `agents/coach-revolucionar.md`
- `prompts/05-relevance-audit.md`
- `references/02-tres-modelos-fundacionales.md` §Capability/Maturity Models
- `references/04-anti-patrones-y-trampas.md` §Identity Attachment
- `katas/kata-soltar-legacy.md`
- `examples/ejemplo-revolucionar-jquery.md`
- `scripts/relevance_audit.py`

---

> **Ritual Auditoría Mensual** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
