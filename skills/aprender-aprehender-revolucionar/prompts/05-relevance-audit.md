# Prompt #5 · Auditoría de Relevancia Profesional

> Framework 4-D para evaluar tus skills mensual y decidir [MANTENER/ACTUALIZAR/REEMPLAZAR/SOLTAR]. Núcleo de la fase (R)Evolucionar.

**Fase**: (R)Evolucionar
**Cadencia**: 1× / mes (1 hora)
**IA recomendada**: cualquiera con datos de mercado actualizados (Perplexity ideal)

---

## Cuándo usarlo

- ✅ Auditoría mensual de relevancia profesional
- ✅ Antes de aceptar un proyecto que requiere skill antiguo (¿vale la pena?)
- ✅ Antes de pedir aumento (cuál es el ROI real de tus skills)
- ✅ Como parte del ritual `rituals/ritual-auditoria-mensual.md`

## Cuándo NO usarlo

- ❌ Sobre temas conceptuales atemporales (matemáticas, comunicación, liderazgo · no se evalúan por "vigencia")
- ❌ Sobre skills muy nicho sin datos de mercado (la IA inventará)

---

## Variables

| Variable | Reemplazar con |
|---|---|
| `[TU INDUSTRIA]` | Industria · ej. "Banca digital", "SaaS B2B", "Retail" |
| `[TU PAÍS / REGIÓN]` | Geografía relevante · ej. "Colombia", "LatAm", "EU" |
| `[TU ROL]` | Rol actual · ej. "Backend Senior · 8 años exp" |
| `[SKILL #1, #2, #3]` | Las 3 skills usadas más este mes |

---

## El Prompt

```
Eres un consultor de carrera senior especializado en [TU INDUSTRIA]
con foco en [TU PAÍS / REGIÓN]. Tienes acceso a tendencias de
contratación, salarios, demanda de skills, y trayectorias profesionales
hasta [FECHA ACTUAL].

Mi rol: [TU ROL]
Industria: [TU INDUSTRIA]
Región: [TU PAÍS / REGIÓN]

SKILLS A AUDITAR (las 3 que más usé este mes):
1. [SKILL #1]
2. [SKILL #2]
3. [SKILL #3]

PROTOCOLO DE AUDITORÍA · FRAMEWORK 4-D

Para CADA skill, evalúa en estas 4 dimensiones:

DIMENSIÓN 1 · VIGENCIA (Currency)
   ¿Es current en mi industria HOY?
   - Aparece en job descriptions de [INDUSTRIA] en 2025-2026?
   - Las conferencias del campo lo mencionan?
   - Los rankings de tools/tech lo incluyen?
   Score: 🟢 ALTA · 🟡 MEDIA · 🔴 BAJA

DIMENSIÓN 2 · ROI (Return on Investment)
   ¿Cuánto retorno por hora invertida en mantener esta skill?
   - Cuántas oportunidades de proyecto/job se desbloquean?
   - Diferencial de salario que aporta?
   - Hace mi trabajo significativamente mejor / más rápido?
   Score: 🟢 ALTO · 🟡 MEDIO · 🔴 BAJO

DIMENSIÓN 3 · OBSOLESCENCIA RISK
   ¿Está en proceso de fading?
   - Tendencia de menciones últimos 5 años: ascendente / estable / descendente?
   - Hay sucesor obvio que la reemplaza?
   - Cuándo predicen los analistas que llegará a EOL?
   Score: 🟢 BAJO RIESGO · 🟡 RIESGO MEDIO · 🔴 ALTO RIESGO

DIMENSIÓN 4 · DEMANDA DE MERCADO
   ¿Qué tan demandada es en mi región?
   - Job postings en [PAÍS] últimos 90 días?
   - Salario promedio asociado?
   - Velocidad de cierre de vacancies?
   Score: 🟢 ALTA · 🟡 MEDIA · 🔴 BAJA

DECISIÓN POR SKILL

Basado en los 4 scores, recomienda UNA decisión:

[MANTENER]
   3-4 verde · skill core que vale la pena profundizar
   Acción: continúa invirtiendo · sube de Escala

[ACTUALIZAR]
   2-3 verde + 1-2 amarillo · skill aún relevante pero con riesgo
   Acción: estudia versión moderna · cierra gaps específicos

[REEMPLAZAR]
   1-2 verde + amarillos/rojos · skill en declive
   Acción: identifica sucesor · transición planeada en 6 meses

[SOLTAR]
   3-4 rojo · skill obsoleta
   Acción: deja de invertir · usa solo si proyecto legacy lo requiere
   Trade-off: tiempo recuperado para una skill emergente

PARA CADA DECISIÓN, INCLUYE:

1. SCORE 4-D explícito (Vigencia | ROI | Obsolescencia | Demanda)
2. EVIDENCIA (datos, no opinión):
   - Job postings count si aplica
   - Salario rango si aplica
   - Trend last 5 years
   - Fuentes citadas
3. PLAN DE ACCIÓN concreto:
   - Si MANTENER: qué profundizar / qué Escala objetivo
   - Si ACTUALIZAR: qué versión moderna estudiar
   - Si REEMPLAZAR: cuál skill sucesora · plan de transición 6 meses
   - Si SOLTAR: cómo justificarlo profesionalmente · qué viene en su lugar

DESPUÉS DE LAS 3 SKILLS:

NARRATIVA PROFESIONAL ACTUALIZADA

Genera 3 versiones de "elevator pitch" basado en las decisiones:
1. Versión LinkedIn (200 chars)
2. Versión CV (3 bullets)
3. Versión entrevista oral (60 segundos)

Refleja las decisiones tomadas:
- Si solté X, no lo menciono o lo declaro consciente: "Decidí dejar
  X cuando vi que [evidencia]; ahora invierto en Y"
- Si reemplacé X→Y, narra la transición como decisión informada
- Si mantengo X, profundizo en por qué (señales de relevancia continuada)

REGLAS

- Cada afirmación con evidencia · cita fuentes
- No reciclar mi narrativa actual · cuestionar honestamente
- Si dato no disponible, marca [NO DATA · estimado conservador]
- Tono: directo, sin endulzar · honestidad > comodidad
```

---

## Cómo procesar el output

### Paso 1 · Documentar
Crea archivo en `~/aprender-aprehender/audits/auditoria-{YYYY-MM}.md` con la salida completa.

### Paso 2 · Decisiones formales
Para cada skill, escribe decisión + razón:
```
Skill: jQuery
Score: V🔴 ROI🔴 Obs🔴 Dem🔴
Decisión: [SOLTAR]
Razón: 4/4 rojo · job postings -90% en 5 años · sucesores claros (React/Vue)
Plan: dejar de invertir · plan reskill React Escala 0→3 en 64h (Workflow 3)
Fecha decisión: 2026-04-30
Próxima auditoría: 2026-05-30
```

### Paso 3 · Calendar action
Si hay [REEMPLAZAR] o [SOLTAR] → agendar Workflow 1 con la nueva skill.

### Paso 4 · Actualizar perfiles
Cada 3 meses, actualiza LinkedIn / CV / Notion / etc. con narrativa nueva.

---

## Output esperado · Ejemplo

```
SKILL #1: jQuery
SCORE 4-D: V🔴 ROI🔴 Obs🔴 Dem🔴
EVIDENCIA:
- Vigencia: <5% job postings en 2026 mencionan jQuery [LinkedIn 2026 Q1]
- ROI: salario promedio asociado -25% vs hace 5 años [Glassdoor]
- Obsolescencia: tendencia -90% en 5 años [Stack Overflow Survey]
- Demanda: <50 vacancies/mes en Colombia [Computrabajo]

DECISIÓN: [SOLTAR]
PLAN:
- Stop invertir tiempo en mantener jQuery skills
- Si proyecto legacy lo requiere: usar pero no profundizar
- Reemplazo: React (target Escala 3 en 64h · 16 semanas)
- Narrativa: "Solté jQuery cuando vi tendencia a -90%. Hoy invierto
  en React + ecosystem moderno"

---

SKILL #2: System Design
SCORE 4-D: V🟢 ROI🟢 Obs🟢 Dem🟢
EVIDENCIA:
- Vigencia: presente en 95% job postings senior [LinkedIn 2026 Q1]
- ROI: salario senior +40% vs intermedio [Glassdoor LatAm]
- Obsolescencia: tendencia estable · core skill perpetua
- Demanda: alta · cierra vacancies en <30 días [LinkedIn]

DECISIÓN: [MANTENER]
PLAN:
- Continúa invirtiendo · objetivo: Escala 5 → Escala 6 en 12 meses
- Profundización: distributed systems · CAP advanced · CRDT
- Diferencial: contribuir a OSS o paper técnico

---

NARRATIVA PROFESIONAL ACTUALIZADA

LinkedIn (200 chars):
"Senior Backend (Escala 5) · Sistemas Distribuidos · Diseño de
sistemas para escala. Solté jQuery, invierto en React + Rust.
Mentor de equipos junior."

CV (3 bullets):
- 8 años en ingeniería backend, especializado en sistemas distribuidos
- Decisión 2026: pivot estratégico React/Rust · transición documentada
- Mentoría activa: 3 ingenieros junior alcanzando Escala 4 en 12 meses

Entrevista oral (60s):
"Soy ingeniero backend con 8 años, especializado en sistemas
distribuidos. En el último año tomé una decisión consciente: solté
jQuery cuando vi que el mercado lo descartaba, y reinvertí ese
tiempo en React y Rust. Esa disciplina de auditar mis skills
mensualmente es lo que me distingue: no acumulo, decido."
```

---

## Anti-patrones

| Error | Síntoma | Corrección |
|---|---|---|
| Auditar opiniones, no skills medibles | "Mi liderazgo es relevante" | Solo skills técnicas o medibles |
| Defender skill que perdió mercado | "jQuery todavía sirve, hay legacy" | Identity attachment · acepta el dato |
| Saltar mes de auditoría | Stealth obsolescence | Agendar como ritual fijo |
| No documentar decisiones | Olvidas qué decidiste y por qué | Audit log persistente |
| Solo IA, sin verificación humana | Sesgo de IA en datos de mercado | Cross-check con LinkedIn manual |

---

## Validación

Tu auditoría está bien si:

- [ ] 3 skills auditadas (no 1, no 10)
- [ ] Cada una tiene 4 scores explícitos
- [ ] Cada score tiene evidencia citada (no opinión)
- [ ] Cada skill tiene 1 decisión clara (no "depende")
- [ ] Cada decisión tiene plan accionable
- [ ] Narrativa profesional refleja las decisiones
- [ ] Documentado en archivo persistente con fecha
- [ ] Próxima auditoría agendada

---

## Combo recomendado

```
RITUAL MENSUAL · 1 hora · primer viernes del mes:

08:00 · Identificar las 3 skills más usadas el mes pasado
08:05 · Ejecutar Prompt #5 en Perplexity (datos de mercado)
08:30 · Procesar respuesta · documentar decisiones
08:45 · Si REEMPLAZAR/SOLTAR · agendar Workflow 1 nueva skill
08:55 · Actualizar narrativa profesional
09:00 · Programar próxima auditoría 2026-06-XX

CADA TRIMESTRE:
- Actualizar LinkedIn / CV con narrativa nueva
- Compartir publicly al menos 1 decisión [SOLTAR] como caso de
  liderazgo (tu marca personal se beneficia de la honestidad)
```

---

## Referencias

- `references/02-tres-modelos-fundacionales.md` §Maturity Model
- `references/04-anti-patrones-y-trampas.md` §Identity Attachment
- `agents/coach-revolucionar.md`
- `rituals/ritual-auditoria-mensual.md`
- `scripts/relevance_audit.py`

---

> **Prompt #5** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
