# Workshop Discovery AI-Native · Variante Empresas · 2 días + 5 días HITL · v2026.04

> **Para quién:** comité ejecutivo (C-level + sponsors de negocio), equipos técnicos del cliente (backend, frontend, QA, DevOps, seguridad, compliance), PMO, procurement y, en sectores regulados, oficial de cumplimiento.
> **Duración:** 2 días workshop presencial · 5 días hábiles de consolidación HITL · 1 sesión de handover técnico de 90 min.
> **Tono:** corporativo, completo, con governance explícita. Vocabulario enterprise. Anglicismos del dominio en inglés con traducción la primera vez (RFP — Request for Proposal, SoW — Statement of Work, CCB — Change Control Board, etc.).
> **Versión:** v2026.04 · Empresas · MetodologIA · CC BY-NC-SA 4.0

---

## TL;DR · La promesa de la variante Empresas

En **2 días de workshop + 5 días hábiles de consolidación HITL (Human-in-the-Loop — humano-en-el-bucle)** transformamos una iniciativa AI-Native ambigua en un paquete **listo para gobernanza corporativa**: spec destilada de tres lentes por iniciativa, arquitectura TO-BE con ADRs (Architecture Decision Records — registros de decisión arquitectónica), dimensionamiento P50/P80/P95 en FTE-meses con bandas RAT/MVP/(R)Evolución, matriz RACI, risk register, plan de comunicación al Steering Committee y addendum de cumplimiento (ISO 27001, GDPR/leyes locales, sectorial). El paquete se entrega bajo **SLA contractual** y se puede anexar directamente a un RFP existente o convertir en líneas de SoW.

> **Lo que esta variante añade frente al playbook completo:** procurement-readiness, governance multi-stakeholder formal (Steering + CCB + PMO), SLAs contractuales por etapa, addendum de compliance y reporting al board. Para profesional individual o equipo de 3–6, ver variante Profesional (1 día). Para iniciativas de un solo equipo sin gobierno corporativo, usar el playbook completo.

---

## Cuándo usar esta variante

| Escenario | Encaja porque… |
|---|---|
| Hay un RFP en curso o por publicar y se necesita anexo técnico defendible. | El paquete HITL T+5 viene con tabla de mapeo a líneas de SoW y scoring criteria sugeridos. |
| La iniciativa cruza ≥ 3 áreas (ej. negocio + tecnología + riesgos + compliance). | Steering Committee, RACI ampliado y CCB están integrados al método. |
| La organización tiene PMO formal y exige reporting consistente. | Templates de status, EVM (Earned Value Management — gestión de valor ganado) y board report mensual incluidos. |
| Sector regulado (banca, salud, gobierno, seguros, energía). | Addendum compliance con matriz control ↔ etapa ↔ evidencia, mapeado a ISO 27001, GDPR/LFPDPPP/LPDP/LPD, SOX, BCBS 239, HIPAA, HL7. |
| El sponsor necesita defender la iniciativa frente al board en 1 página. | El resumen ejecutivo a C-level es entregable estándar. |

**No la uses si:** la iniciativa la lidera un solo equipo sin gobernanza formal, la decisión la toma una sola persona, o el plazo de respuesta es < 5 días hábiles. Para esos casos usa la variante Profesional o el playbook completo.

---

## Pre-workshop · 10 días hábiles de preparación gobernada

| # | Tarea | Owner | Salida concreta |
|---|---|---|---|
| 1 | **Carta de patrocinio firmada** por sponsor ejecutivo. Define objetivo, restricciones de negocio y autoridad delegada. | Sponsor + Conductor | Documento de 1 página firmado. |
| 2 | **Stakeholder mapping** según método de Mendelow (poder × interés). Mínimo 12 stakeholders mapeados. | PMO + Conductor | Mapa visual + lista priorizada. |
| 3 | **NDA (Non-Disclosure Agreement) y acceso seguro** a evidencia (datasets, sistemas, métricas AS-IS). | Procurement + Seguridad | NDA firmado · accesos provisionados. |
| 4 | **Evidence pack enterprise** — mínimo 12 artefactos clasificados con tags `[CÓDIGO]` `[CONFIG]` `[DOC]` `[DATO]` `[INFERENCIA]` `[SUPUESTO]`. | Domain Lead + Tech Lead | Carpeta `pre-read/` versionada. |
| 5 | **Convocatoria formal** con calendarización doble (workshop + Steering review T+5). | PMO | Invitaciones aceptadas ≥ 90% asistencia confirmada. |
| 6 | **Risk Appetite Statement** — qué riesgos la organización tolera (financiero, reputacional, regulatorio, técnico). | Risk Officer + Sponsor | Documento de 1 página firmado por Risk Officer. |
| 7 | **Briefing al Comité de Cambio (CCB)** — el workshop alimentará su backlog; agendar slot para review post-workshop. | PMO + CCB Chair | Slot agendado en próxima cadencia CCB. |

**Regla de bloqueo:** si al iniciar el día 1 falta cualquiera de los 7, el workshop se posterga sin penalización contractual. La calidad de governance no se improvisa.

---

## Agenda · 2 días, 8 sesiones (heredada del playbook completo)

| Día | Sesión | Hora | Foco enterprise |
|---|---|---|---|
| **D1** | S1 · Alineación de Expectativas | 09:00–10:30 | Sponsor + Steering chair presentan objetivo de negocio; Risk Officer presenta apetito. |
| | S2 · Problem Space Exploration | 10:45–12:15 | Journey AS-IS con métricas operativas; pain points cuantificados con costo organizacional. |
| | S3 · AI Opportunity Mapping | 13:30–15:00 | Filtro AI-native + filtro de cumplimiento (¿esta opción cabe en nuestro apetito de riesgo regulatorio?). |
| | S4 · Priorización & Convergencia · **Gate G1** | 15:15–16:45 | Sponsor firma top-3 hipótesis; CCB queda informado. |
| **D2** | S5 · Vibe Coding Kickoff | 09:00–10:30 | Prototipos en sandbox segregada; logs auditables habilitados desde el primer prompt. |
| | S6 · Demos, Feedback & Iteración | 10:45–12:15 | Stakeholder técnico y oficial de cumplimiento presentes en demos. |
| | S7 · Destilación de Spec · 3 Lentes | 13:30–15:00 | Spec firmada por Sponsor + Tech Lead + Risk Officer en cada lente. |
| | S8 · Validación, Compromisos y Cierre · **Gate G2** | 15:15–16:45 | Acta firmada y enviada a Steering Committee por Conductor. |

> **El detalle bloque-por-bloque de cada sesión vive en el playbook completo (`playbook-workshop-discovery-ai-native-v2026.04.2.html`). Esta variante añade governance, compliance, SLAs y procurement-readiness.**

---

## Procurement / RFP-ready · cómo se conecta con un RFP existente

Esta variante se diseñó para que el paquete HITL T+5 pueda **anexarse directamente a un RFP** o **convertirse en líneas de SoW (Statement of Work — declaración de trabajo)** sin reescritura.

### Mapeo paquete HITL ↔ RFP

| Output del workshop | Sección típica de RFP | Cómo se reutiliza |
|---|---|---|
| Spec destilada (3 lentes) | Bases técnicas / Especificaciones funcionales | Cada fila *HACE / NO HACE / F / NF* es un requisito numerado. |
| Arquitectura TO-BE + ADRs | Anexo arquitectónico | Diagramas C4 nivel 2 + ADRs firmados como anexo defendible ante auditoría. |
| Dimensionamiento P50/P80/P95 | Volumetría / Magnitud del esfuerzo | Tabla FTE-meses por banda; el oferente alinea su propuesta. |
| RACI por iniciativa | Modelo de gobierno | Roles cliente/proveedor preasignados. |
| Risk Register | Análisis de riesgos | Matriz severidad × probabilidad con dueño y mitigación. |
| Compliance addendum | Cumplimiento normativo | Matriz control ↔ etapa ↔ evidencia mapeada al estándar exigido. |
| Plan 30/60/90 | Cronograma macro | Hitos relativos a kickoff con dependencias. |

### Scoring criteria sugeridos (para evaluación de ofertas)

| Criterio | Peso sugerido | Cómo se evalúa |
|---|---|---|
| Comprensión del problema (uso explícito de la spec destilada) | 20% | Mención literal a las 3 lentes en la propuesta. |
| Viabilidad técnica AI-native | 20% | Propuesta arquitectónica alineada con ADRs entregados. |
| Equipo y experiencia (perfiles ↔ FTE-meses dimensionados) | 15% | CV con casos análogos de banda equivalente. |
| Plan de mitigación de riesgos | 15% | Cobertura ≥ 80% del Risk Register entregado. |
| Cumplimiento normativo y compliance addendum | 15% | Mapeo control-por-control. |
| Modelo de gobierno y reporting | 10% | Cadencia, dashboards, integración con PMO cliente. |
| Modelo comercial (firme, separado del workshop) | 5% | Disclaimer respetado; precio en propuesta independiente. |

> **Regla:** el workshop **no fija precio**. Entrega magnitudes (FTE-meses), bandas y scope-cost-time. La oferta firme se construye sobre estos insumos en documento comercial separado bajo NDA.

---

## Multi-stakeholder governance

### Steering Committee

| Atributo | Definición |
|---|---|
| **Composición** | Sponsor ejecutivo (chair), CIO/CTO, COO o líder de área de negocio, CFO o delegado, Risk Officer, Conductor MetodologIA, PMO Lead. 5–7 personas máximo. |
| **Cadencia** | Quincenal durante consolidación; mensual post-handover hasta cierre del primer hito (RAT/MVP). |
| **Agenda tipo (60 min)** | (1) Estado vs plan 5 min · (2) Decisiones requeridas 15 min · (3) Riesgos y bloqueos 15 min · (4) Métricas de adopción 10 min · (5) Próximos hitos y comunicación 10 min · (6) Acuerdos firmados 5 min. |
| **Quórum** | Sponsor + 50% restante. Sin quórum, decisiones se difieren máx 5 días hábiles. |
| **Acta** | Firmada por chair en sesión; distribuida por Scribe en máx 24 h. |
| **Escalation matrix** | Severidad 1 (crítico) → Sponsor en < 4 h · Severidad 2 (alto) → Steering en < 24 h · Severidad 3 (medio) → próxima sesión Steering. |

### Comité de Cambio · CCB · Change Control Board

El workshop **alimenta el backlog del CCB existente del cliente** — no compite con él.

- **Touchpoint pre-workshop:** PMO presenta al CCB la iniciativa propuesta; CCB asigna slot de review post-workshop.
- **Touchpoint post-workshop (T+6):** Conductor presenta al CCB las iniciativas aprobadas (Gate G2) con su scope-cost-time. El CCB aprueba el ingreso al backlog formal de cambios.
- **Outputs que el CCB recibe:** spec destilada, arquitectura TO-BE, risk register, dependencias con sistemas existentes, FTE-meses por banda.
- **Decisiones del CCB sobre el workshop:** aprobación, aprobación condicionada (con condiciones documentadas), rechazo (con razón), o solicitud de información adicional (con plazo de 5 días hábiles).

### Integración con la PMO existente

| Touchpoint | Cuándo | Qué intercambia |
|---|---|---|
| Kickoff PMO | T-10 días | Carta de patrocinio + plan de workshop + RACI preliminar. |
| Daily ligero | Durante consolidación HITL T+1..T+5 | Status diario en formato del cliente. |
| Reporte semanal | T+5 | Dashboard compartido con métricas del paquete. |
| Reporte mensual board | T+30, T+60, T+90 | 1 página ejecutiva (template incluido). |

> **Principio:** la PMO del cliente es la dueña del reporting. MetodologIA entrega en el formato que la PMO usa, no el inverso.

---

## SLAs contractuales por etapa

| Etapa | SLA | Penalización por incumplimiento [INFERENCIA — sujeto a acuerdo comercial] | Exclusiones | Escalation |
|---|---|---|---|---|
| **T+1 · Síntesis** | Entregable disponible en repo seguro antes de 18:00 hora cliente. | Crédito equivalente a 0.5 FTE-día sobre próxima fase. | Demoras causadas por accesos no provisionados por cliente. | Conductor → Sponsor en < 4 h. |
| **T+2 · Modelado** | ADRs firmados por Tech Lead cliente o documentado bloqueo. | Crédito 0.5 FTE-día. | Indisponibilidad de Tech Lead cliente. | Tech Lead → CTO en < 8 h. |
| **T+3 · Dimensionamiento** | P50/P80/P95 entregados con disclaimer comercial textual. | Crédito 1 FTE-día. | Cambios de alcance solicitados por cliente posteriores a Gate G2. | PMO → Sponsor en < 24 h. |
| **T+4 · Ensamblaje + QA** | Paquete con 0 inconsistencias detectadas en checklist cross-deliverable. | Crédito 0.5 FTE-día + iteración de QA. | Evidencia retenida por compliance del cliente. | Risk Controller → Steering. |
| **T+5 · Handover** | Sesión de 90 min con equipos técnicos celebrada · acta firmada. | Crédito 1 FTE-día + reagenda en < 5 días. | Indisponibilidad de equipo técnico cliente. | Sponsor → Steering. |

> **Disclaimer comercial obligatorio:** *"Las penalizaciones aquí descritas son de referencia metodológica y se vuelven exigibles únicamente al ser incorporadas a un contrato comercial firmado por ambas partes. La oferta firme se entrega como documento independiente bajo NDA y firma del responsable comercial."*

---

## Compliance addendum

### Frameworks cubiertos

| Framework | Aplicabilidad típica | Controles tocados por el workshop |
|---|---|---|
| **ISO 27001** | Cualquier organización con SGSI (Sistema de Gestión de Seguridad de la Información). | A.5 (políticas), A.8 (gestión de activos — datos del workshop), A.12 (operación segura de prototipos), A.18 (cumplimiento). |
| **GDPR / LFPDPPP (México) / LPDP (Colombia) / LPD (Argentina)** | Iniciativas que tocan datos personales. | Base legal de tratamiento, minimización, derechos del titular, DPIA (Data Protection Impact Assessment) si aplica. |
| **SOX (Sarbanes-Oxley)** | Servicios financieros listados en EE.UU. o subsidiarias. | Trazabilidad de decisiones, segregación de funciones, controles ITGC (IT General Controls). |
| **BCBS 239** | Banca con riesgos materiales. | Calidad de datos para riesgo, gobernanza de datos, capacidad de agregación. |
| **HIPAA · HL7** | Salud (EE.UU. y proveedores). | PHI (Protected Health Information), interoperabilidad HL7/FHIR si la iniciativa toca historia clínica. |
| **Clasificación de información (gobierno)** | Sector público. | Manejo de información reservada, confidencial, pública conforme a ley nacional. |

### Matriz control ↔ etapa ↔ evidencia generada

| Control representativo | Etapa del workshop | Evidencia generada |
|---|---|---|
| ISO 27001 A.8.2 (clasificación de información) | Pre-workshop · Evidence pack | Cada artefacto del `pre-read/` clasificado: público / interno / confidencial / restringido. |
| ISO 27001 A.12.1 (procedimientos operativos) | S5 · Vibe Coding | Sandbox segregada con logging habilitado · prompts auditables. |
| GDPR Art. 35 (DPIA) | T+1 Síntesis | Si la iniciativa procesa datos personales, se inicia DPIA con Risk Officer firmando. |
| GDPR Art. 5 (minimización) | S7 · Spec lente F/NF | Cada NF de datos declara qué dato se procesa y por qué. |
| SOX 404 (controles internos) | T+2 Modelado · ADRs | ADRs firmados son evidencia auditable de decisiones arquitectónicas. |
| BCBS 239 Principios 3 y 4 | T+3 Dimensionamiento | Trazabilidad de supuestos sobre datos y calidad. |
| HIPAA §164.312 (controles técnicos) | S5 Vibe Coding + T+2 Modelado | Diseño con encriptación en reposo y tránsito si toca PHI. |
| Clasificación gobierno | Pre-workshop + T+4 Ensamblaje | Marca de clasificación en cada documento del paquete. |

> **Regla:** ningún paquete HITL T+5 sale sin la matriz compliance llena para el framework aplicable. El Risk Officer firma la matriz como prerrequisito de Gate G2.

---

## Reporting al comité directivo

### Template de reporte mensual a board · 1 página

```
┌─────────────────────────────────────────────────────────────┐
│ INICIATIVA AI-NATIVE · [Nombre] · Reporte Board · MMM/AAAA  │
├─────────────────────────────────────────────────────────────┤
│ ESTADO: [Verde · Amarillo · Rojo]    BANDA: RAT/MVP/(R)Evol │
│ HITO ACTUAL: [Hito M+X]              FECHA: DD/MM/AAAA      │
├─────────────────────────────────────────────────────────────┤
│ PROGRESO (últimos 30 días)                                  │
│ • [bullet medible 1]                                        │
│ • [bullet medible 2]                                        │
│ • [bullet medible 3]                                        │
├─────────────────────────────────────────────────────────────┤
│ KPIs EJECUTIVOS                                             │
│ • Time-to-traction: X días vs Y plan      [↑ ↓ →]          │
│ • Costo evitado / valor proyectado: X FTE-meses equivalentes│
│ • Riesgo mitigado: X de Y riesgos cerrados                 │
│ • Adopción interna: X% usuarios activos vs cohorte         │
├─────────────────────────────────────────────────────────────┤
│ DECISIÓN REQUERIDA AL BOARD: [Sí · No · Informativo]       │
│ Si Sí: [pregunta concreta de 1 línea]                      │
├─────────────────────────────────────────────────────────────┤
│ PRÓXIMO HITO: [hito + fecha + criterio binario de éxito]   │
└─────────────────────────────────────────────────────────────┘
```

### KPIs ejecutivos · definiciones operativas

| KPI | Definición | Cómo se mide | Frecuencia |
|---|---|---|---|
| **Time-to-traction** | Días desde kickoff hasta el primer evento de uso recurrente por un usuario real (no equipo de proyecto). | Telemetría del prototipo / piloto. | Diaria post-handover. |
| **Costo evitado / valor proyectado** | FTE-meses ahorrados o ingreso atribuible a la iniciativa, declarado y validado. | Modelo de business case actualizado mensualmente con datos reales. | Mensual al board. |
| **Riesgo mitigado** | Número de riesgos del Risk Register inicial cerrados o reducidos en severidad. | Risk Register vivo con auditoría mensual. | Mensual al board. |
| **Adopción interna (DAU/WAU)** | Usuarios activos diarios sobre semanales en cohorte definida. Umbral MVP ≥ 0.4. | Analítica del producto + cohorte registrada. | Semanal al Steering, mensual al board. |

> **Regla de honestidad:** si un KPI no se puede medir aún (porque la iniciativa no lo permite todavía), se reporta como `[NO APLICA AÚN — esperado para hito M+X]`. Nunca se inventa.

---

## Cotización completa con bandas + disclaimer comercial

### Bandas estándar MetodologIA (heredadas del playbook completo)

| Banda | Horizonte | FTE-meses P50 | FTE-meses P80 | FTE-meses P95 | Equipo peak | Cuándo se elige |
|---|---|---|---|---|---|---|
| **S · RAT** (Riskiest Assumption Test) | 1 mes | 2 | 3 | 5 | 2–3 FTE | Hipótesis crítica sin validar; resultado binario. |
| **M · MVP** (Minimum Viable Product) | 3 meses | 8 | 12 | 18 | 4–6 FTE | Hipótesis validada; se busca tracción medible. |
| **L · (R)Evolución** | 16 semanas | 22 | 32 | 48 | 6–10 FTE | MVP probó tracción; se escala a sistema productivo. |
| **XL · Política** | > 16 semanas | Recalculado por fase | Recalculado por fase | Recalculado por fase | Por fase | **Prohibido como bloque único.** Se ejecuta en cascada RAT → MVP → (R)Evolución con gate comercial entre fases. |

[INFERENCIA] Las cifras son rangos de referencia para escenarios típicos AI-Native; cada iniciativa real recalibra con sus supuestos específicos en el dimensionamiento T+3.

### Disclaimer comercial obligatorio (textual)

> **Disclaimer comercial.** Las magnitudes en FTE-meses, las bandas RAT / MVP / (R)Evolución, los percentiles P50 / P80 / P95 y los SLAs descritos en este documento son **estimaciones de dimensionamiento y referencias metodológicas** basadas en los prototipos, specs destiladas y supuestos explícitos del workshop. **No constituyen oferta comercial ni compromiso de precio.** La oferta firme con precio en moneda, términos de pago, garantías, indemnizaciones, propiedad intelectual y SLAs contractuales se entrega como **documento independiente bajo NDA y firma del responsable comercial**, posterior al cierre del Gate G2 del workshop y a la aceptación del paquete HITL T+5.

---

## Quality gates · hard stops

| Gate | Cuándo | Qué se firma | Quién firma | Si no se firma |
|---|---|---|---|---|
| **G1** | Cierre Día 1 | Top-3 hipótesis con scores explícitos | Sponsor + Risk Officer | Día 2 no arranca · se reagenda. |
| **G1.5** | T+2 (consolidación) | ADRs por iniciativa | Tech Lead cliente | Dimensionamiento T+3 se difiere. |
| **G2** | Cierre Día 2 | Spec + RACI + bandas | Sponsor + Tech Lead + Risk Officer | Pipeline HITL no inicia. |
| **G3** | T+5 handover | Aceptación del paquete | Sponsor + CIO/CTO + Risk Officer | Workshop se cierra como parcial; se documenta brecha y se reprograma sesión de cierre. |

---

## Roles ampliados (frente al playbook completo)

Adicional al equipo base (Conductor, Sponsor, Domain Lead, Tech Lead, Data Lead, User Proxy, Scribe, Devil's Advocate), la variante Empresas requiere:

| Rol enterprise | Responsabilidad | Presencia |
|---|---|---|
| **Risk Officer / Compliance Officer** | Firma del Risk Appetite Statement, matriz compliance, mitigaciones del Risk Register. | Pre-workshop · S1 · S7 · T+4 · Gate G2 · Gate G3. |
| **PMO Lead** | Integración con metodología y reporting del cliente; daily ligero durante consolidación. | Pre-workshop · D1 cierre · todo T+1..T+5. |
| **Procurement Lead** | Garantizar trazabilidad workshop → SoW; revisar disclaimer comercial. | Pre-workshop · Gate G3. |
| **CCB Chair (Comité de Cambio)** | Recibir paquete post-workshop; aprobar ingreso al backlog formal. | T+6 (slot agendado). |
| **Steering Chair** | Quincenal durante consolidación; mensual post-handover. | Sesiones de Steering programadas. |

---

## RACI ampliado por decisión clave

R = Responsible (ejecuta) · A = Accountable (rinde cuentas, único) · C = Consulted (consultado antes) · I = Informed (informado después).

| Decisión | Sponsor | Conductor | Tech Lead | Risk Officer | PMO Lead | CCB Chair | Procurement |
|---|---|---|---|---|---|---|---|
| Aprobar carta de patrocinio | A | R | I | C | C | I | I |
| Firmar Risk Appetite Statement | A | C | C | R | I | I | I |
| Firmar NDA y accesos | A | I | C | C | C | I | R |
| Aprobar problem statement v1 (S1) | A | R | C | C | I | I | I |
| Score filtro AI-native + filtro compliance (S3) | I | R | R | A | I | I | I |
| Selección top-3 hipótesis · **Gate G1** | A | R | C | R | I | I | I |
| Stack de vibe coding y sandbox segura (S5) | I | C | A | R | I | I | I |
| Aceptación spec destilada (S7) | A | R | R | R | I | I | I |
| Asignación de banda RAT/MVP/(R)Evolución | A | R | R | C | C | I | I |
| Aceptación · **Gate G2** | A | R | R | R | C | I | I |
| Firma ADRs · **Gate G1.5** (T+2) | C | C | A | C | R | I | I |
| Aceptación dimensionamiento (T+3) | A | R | C | C | R | I | C |
| Aceptación paquete HITL · **Gate G3** (T+5) | A | R | R | R | C | I | C |
| Ingreso al backlog del CCB (T+6) | I | R | C | C | C | A | I |
| Reporte mensual al board (T+30, T+60, T+90) | A | C | C | C | R | I | I |
| Cambio de scope post-Gate G2 (CR formal) | A | R | C | C | R | C | C |

> **Regla:** ningún rol puede figurar como `A` y `R` simultáneamente en la misma decisión. Si ocurre, se reescribe la fila con un rol externo asumiendo Accountable.

---

## Stakeholder communication plan

Mapeo de qué información recibe quién, en qué cadencia, en qué canal y con qué nivel de detalle. Sirve de input directo a la PMO del cliente y al plan de adopción.

| Audiencia | Información que recibe | Cadencia | Canal | Nivel de detalle | Owner del envío |
|---|---|---|---|---|---|
| **Board / Junta Directiva** | Reporte 1 página + decisión requerida + KPIs ejecutivos. | Mensual (T+30, T+60, T+90). | Sesión formal de board + PDF firmado. | Estratégico. | Sponsor. |
| **Steering Committee** | Estado, decisiones requeridas, riesgos, adopción, próximos hitos. | Quincenal durante consolidación; mensual post-handover. | Sesión 60 min + acta. | Táctico-estratégico. | PMO Lead. |
| **CCB · Comité de Cambio** | Iniciativas aprobadas con scope-cost-time + dependencias + risk register. | T+6 puntual; luego según cadencia CCB. | Sesión formal CCB + paquete completo. | Técnico-procesual. | Conductor + PMO. |
| **PMO del cliente** | Status diario, dashboard semanal, reportes mensuales. | Diaria (durante consolidación), semanal, mensual. | Dashboard compartido + daily 15 min. | Operativo. | Conductor → PMO. |
| **Equipos técnicos cliente** (backend, frontend, QA, DevOps, seguridad) | Spec destilada, arquitectura TO-BE, ADRs, prototipos, runbook de onboarding. | T+5 (handover) + iteraciones según hito. | Sesión 90 min handover + repo de paquete. | Técnico detallado. | Tech Lead MetodologIA. |
| **Compliance / Riesgos cliente** | Compliance addendum, matriz control ↔ etapa ↔ evidencia, DPIA si aplica. | T+4 borrador, T+5 final, mensual ongoing. | Sesión cerrada + matriz firmada. | Regulatorio detallado. | Risk Officer cliente + Conductor. |
| **Procurement cliente** | Mapeo paquete ↔ líneas de SoW + scoring criteria + disclaimer comercial. | T+5 + cuando se publique RFP. | Documento formal + reunión 30 min. | Contractual. | Procurement Lead. |
| **Usuarios afectados (cohorte piloto)** | Comunicación de cambios, sesiones de onboarding, canales de soporte y feedback. | Pre-piloto + durante piloto + cierre. | Email + sesión presencial / virtual + canal de soporte. | Práctico-operativo. | Domain Lead + UX. |
| **Sindicatos / representación laboral** (si aplica) | Impacto laboral del cambio, plan de capacitación, garantías de no-sustitución. | Pre-workshop si la iniciativa toca empleos; antes de despliegue. | Sesión formal + acta. | Negociación laboral. | Sponsor + RR.HH. |

> **Regla de transparencia:** ningún canal de comunicación se omite por incomodidad política. Si una audiencia requiere ser informada y no se incluye, eso queda como riesgo en el Risk Register con dueño y mitigación.

---

## Anti-patrones enterprise específicos

| Anti-patrón | Señal temprana | Intervención |
|---|---|---|
| **"Este workshop reemplaza al CCB."** | Alguien sugiere saltar el CCB porque "ya hicimos el workshop". | Conductor recuerda: el workshop alimenta al CCB; no lo sustituye. |
| **Sponsor delega firma a un proxy.** | El sponsor no aparece en Gate G1 o G2. | Pausa: sin firma del sponsor titular, el gate no se cierra. La autoridad delegada debe estar documentada en la carta de patrocinio. |
| **PMO impone formato propio en medio del workshop.** | A mitad de D2, PMO pide rehacer outputs en su template. | Negociar capa de transformación T+4 (ensamblaje); el contenido es el del workshop, el formato se adapta sin perder evidencia. |
| **Compliance llega solo a Gate G3.** | Risk Officer no asistió a S7. | Insistir en presencia desde S1; si no, el paquete sale con `[REQUIERE VALIDACIÓN COMPLIANCE]` y NO se socializa hasta firma. |
| **Procurement quiere precio en T+5.** | Procurement presiona por número en moneda en el handover. | Aplicar disclaimer textual; redirigir a propuesta comercial separada bajo NDA. |
| **Steering pide cambios de scope post-Gate G2.** | Cambio llega T+3 o T+4. | CR (Change Request) formal · scope-cost-time se recalcula · nuevo gate. No hay cambios silenciosos. |

---

## KPIs del workshop (calidad metodológica)

| KPI | Meta | Cómo se mide | Reportado a |
|---|---|---|---|
| Asistencia confirmada de Sponsor + Tech Lead + Risk Officer en ambos días | 100% | Lista de asistencia firmada. | Steering. |
| Gates G1, G2 firmados sin extensión | ≥ 80% de los workshops | Acta firmada en horario. | PMO + Steering. |
| Cobertura compliance addendum sobre framework aplicable | 100% controles relevantes | Matriz control ↔ etapa ↔ evidencia. | Risk Officer. |
| Paquete HITL T+5 entregado en plazo | 100% (o crédito SLA aplicado) | Timestamp + acta de aceptación. | Sponsor + PMO. |
| Iniciativas que pasan a CCB sin observaciones críticas | ≥ 75% | Acta de CCB T+6. | CCB Chair + Steering. |
| Aceptación del Sponsor en Gate G3 | 100% (o documentación de brecha) | Firma digital. | Steering + Board. |

---

## Próximo paso · cómo agendarlo

1. **Carta de intención** firmada por sponsor ejecutivo en plantilla MetodologIA.
2. **Slot Steering pre-workshop** confirmado para Risk Appetite + carta de patrocinio.
3. **Acceso seguro provisionado** y NDA firmado.
4. **Workshop calendarizado** en 2 días consecutivos + slot Steering T+5 + slot CCB T+6.

> **Compromiso MetodologIA:** una vez firmada la carta de intención, T-10 días para arrancar workshop, T+0/+1 workshop, T+1..T+5 consolidación HITL, T+5 handover técnico, T+6 ingreso al CCB. **18 días hábiles del compromiso al backlog formal del cliente.**

---

## Anexos referenciados (entregados en el paquete HITL T+5)

- `01_Spec_destilada_[iniciativa]_{WIP|Aprobado}.md` — una por iniciativa.
- `02_Acta_workshop_{Aprobado}.md` — firmada por sponsor, conductor, tech lead, risk officer.
- `03_RACI_{Aprobado}.md` — por iniciativa y por proceso de gobierno.
- `04_Arquitectura_TOBE_{WIP|Aprobado}.md` + `04a_ADRs/`.
- `05_Dimensionamiento_{WIP|Aprobado}.xlsx` — P50/P80/P95 + bandas.
- `06_Risk_register_{WIP|Aprobado}.md` — severidad × probabilidad × dueño × mitigación.
- `07_Compliance_addendum_{WIP|Aprobado}.md` — matriz control ↔ etapa ↔ evidencia.
- `08_Plan_30_60_90_{Aprobado}.md` — hitos relativos a kickoff.
- `09_SLA_y_governance_{Aprobado}.md` — SLAs por etapa + escalation matrix.
- `10_Reporte_board_template_{Aprobado}.md` — 1 página ejecutiva.
- `11_Mapeo_RFP_SoW_{Aprobado}.md` — cómo el paquete se traduce a líneas de SoW.
- `12_Onboarding_runbook_{Aprobado}.md` — cómo arrancan los equipos técnicos.

> **Naming convention:** `{NN}_{Nombre}_{cliente}_{WIP|Aprobado}.{ext}`. WIP durante consolidación; Aprobado tras Gate G3.

---

*Workshop Discovery AI-Native · Variante Empresas · v2026.04 · Por Javier Montaño · metodologia.info · CC BY-NC-SA 4.0 · Human First, AI-Next.*
