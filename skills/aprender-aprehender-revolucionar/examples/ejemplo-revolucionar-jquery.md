# Ejemplo · (R)Evolucionar · Soltar jQuery

> Auditoría 4-D · decisión [SOLTAR] · plan reskill · narrativa profesional actualizada.

**Persona**: Frontend Senior · 12 años exp · skill jQuery desde 2014.
**Disparador**: postulación a jobs no recibe respuesta · sospecha que stack está obsoleto.
**Tiempo invertido**: 1 hora (auditoría mensual) + 64h (reskill posterior · separado).

---

## Contexto antes de la sesión

**Skills históricos** (12 años):
- jQuery: 8 años intensivo (2014-2022) · 3 años mantenimiento (2022-2025) · ~3000h totales
- Identity attachment: "Soy 'el de jQuery' en mi círculo profesional"
- Última vez en proyecto nuevo con jQuery: 2022

**Disparador**:
- Aplicó a 15 jobs frontend en 3 meses
- 2 entrevistas, 0 ofertas
- Feedback recurrente: "Buscamos React · jQuery es legacy"

---

## Sesión Auditoría · 1 hora · primer viernes del mes

### 0:00-0:05 · Identificar 3 skills

Las usadas más este mes:
1. **jQuery** · todavía mantengo 1 sistema legacy
2. **HTML/CSS** · base · todos los proyectos
3. **JavaScript ES6+** · he aprendido lo nuevo, pero no React/Vue

### 0:05-0:30 · Ejecutar Prompt #5 (framework 4-D) en Perplexity

Variables:
- INDUSTRIA: Frontend Web
- PAÍS / REGIÓN: Colombia + LatAm remote
- ROL: Frontend Senior

#### Skill #1: jQuery

| Dimensión | Score | Evidencia |
|---|---|---|
| Vigencia | 🔴 BAJA | <5% de job postings 2026 lo mencionan [LinkedIn 2026 Q1] |
| ROI | 🔴 BAJO | Salario asociado -25% vs 2018 · oportunidades nuevas: solo legacy [Glassdoor LatAm] |
| Obsolescencia | 🔴 ALTA | Stack Overflow Survey 2024-2026: declive -90% en 5 años · jQuery removido de Bootstrap 5 |
| Demanda | 🔴 BAJA | <50 vacancies/mes en Colombia mencionan jQuery [Computrabajo] · vs React: 800+ |

**Decisión**: **[SOLTAR]**
**Razón**: 4/4 rojo · evidencia abrumadora · sucesor obvio (React/Vue)
**Plan**: stop invertir tiempo · usar solo si proyecto legacy lo requiere · plan reskill React 64h

#### Skill #2: HTML/CSS

| Dimensión | Score | Evidencia |
|---|---|---|
| Vigencia | 🟢 ALTA | 100% job postings frontend lo asumen [LinkedIn] |
| ROI | 🟢 ALTO | Sin esto, no eres frontend |
| Obsolescencia | 🟢 BAJO | Tendencia estable · CSS evoluciona pero no se reemplaza |
| Demanda | 🟢 ALTA | Universal en frontend |

**Decisión**: **[MANTENER]**
**Plan**: profundizar en CSS Grid moderno + accessibility (siempre relevante)

#### Skill #3: JavaScript ES6+

| Dimensión | Score | Evidencia |
|---|---|---|
| Vigencia | 🟢 ALTA | Foundation de todos los frameworks |
| ROI | 🟢 ALTO | Crítico para cualquier rol frontend serio |
| Obsolescencia | 🟢 BAJO | TC39 evoluciona el lenguaje continuamente |
| Demanda | 🟢 ALTA | Universal |

**Decisión**: **[MANTENER]**
**Plan**: profundizar en async patterns + módulos modernos · prep React

### 0:30-0:45 · Validación cruzada manual

Verifiqué la cifra "<5% jobs mencionan jQuery":
- Búsqueda LinkedIn "jQuery" en Colombia: 23 resultados
- Búsqueda LinkedIn "React" en Colombia: 847 resultados
- Ratio: jQuery es <3% · confirmando la cifra

Verifiqué Stack Overflow Survey:
- 2018: 50% developers usaban jQuery
- 2024: 17% (declive sostenido)
- 2026: estimado <10%

**Conclusión**: data confirma el veredicto · NO es bias de la IA.

### 0:45-0:55 · Documentar decisión

Creé `~/aprender-aprehender/audits/auditoria-2026-04.md`:

```markdown
# Auditoría de Relevancia · 2026-04

## Skill: jQuery

Score 4-D: V🔴 ROI🔴 Obs🔴 Dem🔴

DECISIÓN: [SOLTAR]

Razón: 4/4 rojo · -90% en 5 años · sucesor obvio (React/Vue)

Plan:
- Stop invertir tiempo en mantener jQuery skills
- Si proyecto legacy lo requiere: usar pero no profundizar
- Reemplazo: React (target Escala 3 en 64h · 16 semanas)

Narrativa actualizada:
- LinkedIn: "Solté jQuery cuando vi tendencia -90%. Hoy invierto en React + ecosystem moderno"
- CV: actualizar inmediatamente

Fecha decisión: 2026-04-30
Próxima auditoría: skill no aplicable (soltada) · próxima auditoría general: 2026-05-30
```

### 0:55-1:00 · Actualizar narrativa profesional

#### LinkedIn (200 chars)
> Frontend Senior 12y · solté jQuery en 2026 cuando vi tendencia -90% · hoy invierto en React + ecosystem moderno · disciplina: auditar relevancia mensual · (R)Evolución continua

#### CV (3 bullets)

```
- 12 años de experiencia frontend · transición consciente legacy → moderno
- Decisión 2026-04: solté jQuery basado en data de mercado · pivot a React
- Disciplina de auditoría mensual de relevancia · método > comodidad
```

#### Entrevista oral (60s)

> "Mi último cambio importante fue en abril 2026, cuando audité mis skills con framework 4-D. jQuery, que dominé 8 años, salió 4/4 rojo: vigencia, ROI, obsolescencia, demanda. Tomé la decisión consciente de soltarlo y reskillearme en React. Eso me distingue: no acumulo skills por nostalgia · audito y decido. La disciplina es mensual. El que no audita, se vuelve legado sin saberlo."

---

## Plan de reskill posterior (separado · 64h Marathon)

```bash
python scripts/desatraso_planner.py --tema "React + ecosystem moderno" \
  --tiempo 64h --escala-actual 0 \
  --industria "Frontend Web LatAm"
```

Output: programa 16 semanas (1h × 4 días/semana).

Inicio agendado: lunes siguiente.

---

## Resultado · 6 meses después

**Setpoints**:
- Mes 1: Workflow 1 React (Escala 1)
- Mes 2-3: Workflow 2 + 3 (Escala 3)
- Mes 4: PoC React en proyecto real (mi propio sistema legacy)
- Mes 5-6: aplicar a jobs · 5 entrevistas, 2 ofertas (vs 2/0 anteriormente)

**Salario**: +25% vs anterior (no porque "soltar jQuery" me hizo merecer más · sino porque ahora aplico a un mercado 28× más grande)

---

## Lecciones aprendidas

### Lo que más costó · emocionalmente

- Identity Attachment fue el bloqueador real · no la dificultad técnica
- 3 días de "pero todavía hay proyectos legacy..." antes de aceptar evidencia
- Empezar React de cero a los 12 años de carrera · sentí "desvalorización"

### Lo que más sirvió

- **Datos objetivos > sentimiento**: el framework 4-D me dio razón externa para soltar
- **Narrativa "decisión consciente"**: soltar jQuery públicamente se volvió diferenciador en entrevistas
- **Plan reskill inmediato**: no soltar al vacío · siempre con sucesor agendado

### Lo que cambió en mi proceso

- Auditoría mensual obligatoria · calendar invite locked
- Cada año reviso framework 4-D para mis 5 skills core
- Mi LinkedIn ahora muestra evolución consciente, no skills fantasma de hace 5 años

---

## Tiempo total: 1h auditoría + 64h reskill = 65h
## Veredicto: ✅ Decisión correcta · ROI: +25% salario · 28× mercado accesible

---

## Comandos útiles que ejecuté

```bash
# Auditoría
python scripts/relevance_audit.py \
  --skills "jQuery,HTML/CSS,JavaScript ES6+" \
  --industria "Frontend Web" \
  --pais "Colombia · LatAm" \
  --rol "Frontend Senior 12y" \
  --save ~/aprender-aprehender/audits/auditoria-2026-04.md

# Plan reskill
python scripts/desatraso_planner.py --tema "React" --tiempo 64h --escala-actual 0

# Track
python scripts/progress_tracker.py --add-tema "React" --objetivo 3 --horas-obj 64
```

---

> **Ejemplo (R)Evolucionar jQuery** del Playbook Aprender · Aprehender · (R)Evolucionar v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
> *Caso ilustrativo · refleja patrones comunes de transición legacy → moderno.*
