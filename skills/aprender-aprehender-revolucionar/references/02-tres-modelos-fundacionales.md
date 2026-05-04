# 3 Modelos Fundacionales · BoK · Capability · Maturity

> Arquitectura mental de cualquier dominio profesional. Sin los 3, navegas a ciegas. v1.1.0.

`[FUENTE-PRIMARIA]` Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 §Modelos Fundacionales.

## Por qué los 3 son complementarios

| Modelo | Pregunta | Metáfora | Sin él... |
|---|---|---|---|
| **Body of Knowledge (BoK)** | ¿QUÉ EXISTE? | Mapa del territorio | Estudias 3 temas y crees que es el campo |
| **Capability Model** | ¿QUÉ DEBO SABER HACER? | Cinta de karate | Sabes mucho, ejecutas poco |
| **Maturity Model** | ¿DÓNDE ESTOY? | GPS | Plan de viaje sin punto de partida |

`[NUEVO-APORTE]` Los modelos NO son secuenciales rígidos. Si la urgencia es alta (3 días al evento), un Capability incompleto + Maturity diagnosticado supera a un BoK exhaustivo sin Capability. La asimetría es: **Capability + Maturity sin BoK** llega a ejecución; **BoK sin Capability** se queda en biblioteca.

---

## 1 · Body of Knowledge (BoK)

**Definición**: mapa completo del dominio · subtemas · conexiones interdisciplinarias · fuentes 1°/2°/3° · controversias · futuro.

**Por qué importa**: las omisiones invisibles son el peor riesgo. No sabes qué desconoces.

### Estructura canónica

```
[DOMINIO]
├── Definición precisa (1-3 frases)
├── Historia · contexto (cómo llegamos aquí)
├── Subtemas principales (5-10 ramas)
├── Conexiones interdisciplinarias (3+ campos)
├── Fuentes primarias (papers fundacionales · libros canónicos)
├── Fuentes secundarias (autoridades · conferencias)
├── Fuentes terciarias (resúmenes · blogs · cursos derivados)
├── Estado del arte (2024-2026)
├── Controversias / debates abiertos
└── Direcciones futuras
```

### Ejemplo · Sistemas Distribuidos (subset)

```
SUBTEMAS: Consenso (Paxos · Raft · PBFT) · Replicación · Particionamiento · Tolerancia a fallas · Coordinación · Comunicación
CONEXIONES: Redes (TCP/IP · particiones) · Bases de Datos (CAP · consistencia) · OS (concurrencia · locks)
FUENTES PRIMARIAS:
  · Lamport · Time, Clocks · 1978 [FUENTE-PRIMARIA]
  · Brewer · CAP Theorem · 2000 [FUENTE-PRIMARIA]
  · DeCandia et al · Dynamo · 2007 [FUENTE-PRIMARIA]
  · Ongaro & Ousterhout · Raft · 2014 [FUENTE-PRIMARIA]
AUTORIDADES: Lamport · Stonebraker · Dean · Helland · Kleppmann
CONTROVERSIAS: ACID vs BASE · CAP vs PACELC · NewSQL · serverless distribuido
```

### Generación con IA · Prompt #1

→ `prompts/01-research-blueprint.md` instancia este modelo. **Triangulación 3+ IAs es mandatory** (Single-AI BoK es anti-patrón crítico §4-anti-patrones).

### Anti-patrón crítico · Single-AI BoK

| Coincidencia entre IAs | Veredicto |
|---|---|
| 3/3 | Verdad probable · alta confianza |
| 2/3 | Verdad media · validar fuente primaria |
| 1/3 | Sospechoso · investigar manual o descartar |
| Contradicciones | **ORO** · ahí están las áreas de debate del campo |

`[CASO-BORDE]` Si 3 IAs comparten misma omisión (entrenadas con corpus similar), la triangulación falla. Antídoto: agregar 1 fuente humana (paper recent en arXiv, libro canónico publicado >2 años atrás).

### Quality gate del BoK

- [ ] Triangulado en ≥3 IAs distintas
- [ ] ≥5 subtemas mapeados
- [ ] ≥3 fuentes primarias verificables (no terciarias derivadas)
- [ ] Glosario mín 15 términos con tag de evidencia
- [ ] Conexiones interdisciplinarias mapeadas
- [ ] Concept map jerárquico (mermaid) generado

`[CRITERIO-ACEPTACIÓN]` 6/6 · sin esto el BoK es ilusión de completitud.

---

## 2 · Capability Model

**Definición**: lo que necesitas saber **HACER**, organizado en niveles con criterios testables.

**Por qué importa**: el BoK te dice qué hay; el Capability te dice qué subset necesitas para tu rol/objetivo. Backend developer NO necesita Capability completo de UI/UX.

### Estructura canónica

```
[ROL / OBJETIVO]
├── NIVEL 1 · FUNDAMENTOS (0-6 meses)
│   ├── Capability 1.1 · habilidad atómica
│   │   ├── Criterio aceptación: test demostrable
│   │   └── Recurso para aprender
│   └── ...
├── NIVEL 2 · INTERMEDIO (6-18 m)
├── NIVEL 3 · AVANZADO (18+ m)
└── NIVEL 4 · EXPERTO (5+ años)
```

### Ejemplo · Backend Engineer Distribuido (extracto)

| Nivel | Capability | Criterio testable |
|---|---|---|
| 1 · Fund | REST API CRUD completo | API con auth + paginación + tests pasa |
| 1 · Fund | Modelar SQL con índices | Schema normalizado · queries optimizadas con EXPLAIN |
| 1 · Fund | Transacciones ACID | Implementar transferencia bancaria sin race conditions |
| 2 · Inter | APIs idempotentes retry-safe | Idempotency-Key implementado y testeado |
| 2 · Inter | Circuit breaker pattern | Falla graceful con timeout + half-open state |
| 3 · Avan | Sistemas distribuidos con CAP | Diseño con trade-offs CP vs AP justificados |
| 3 · Avan | Consensus básico (Raft/Paxos) | Implementar leader election en Go/Rust |
| 4 · Exp | Arquitecturas 100M+ usuarios | Diseñar y validar con load test real |
| 4 · Exp | Influencia industria (RFCs/OSS) | Contribución mergeada a proyecto referencia |

### Generación

**Manual (recomendado)**: pregunta a un experto del campo. Es **opinión validada**, no consenso de IAs.

**Con IA (validar después)**:
```
Soy [TU ROL ACTUAL] objetivo [TU ROL DESEADO]. Genera Capability Model 4 niveles.
Para cada capability: nombre atómico · criterio testable · recurso.
Cada capability DEBE ser DEMOSTRABLE, no teórica.
```

### Anti-patrón crítico · IA sola para Capability

> *"El Capability Model es la única parte de los 3 modelos donde el experto humano supera a la IA. La IA conoce la teoría, no la realidad de tu mercado."* `[FUENTE-PRIMARIA]` Playbook §Modelos.

Las IAs inventan capabilities que suenan bien pero no son las que tu industria espera. **Validar con experto humano** antes de basar plan de carrera.

### Capability Personal vs Capability Mercado

```
CAPABILITY MERCADO (lo que se espera de tu rol en tu industria)
       ∩
CAPABILITY PERSONAL (lo que TÚ necesitas según tu objetivo único)
       =
GAP ANÁLISIS · qué falta · qué sobra · qué priorizar
```

`[CASO-BORDE]` Capability Mercado y Personal pueden divergir significativamente. Si tu objetivo es nicho (ej. "research scientist en cuántica industrial"), el Capability Mercado puede ser un superset que no necesitas. Documentar la divergencia explícita evita perder tiempo en lo irrelevante.

### Quality gate del Capability Model

- [ ] 4 niveles definidos (Fundamentos → Experto)
- [ ] ≥3 capabilities por nivel
- [ ] Cada capability con criterio testable (no "saber X")
- [ ] Validado con ≥1 experto humano del campo
- [ ] Tu nivel actual identificado por capability
- [ ] Plan de progresión a siguiente nivel definido

---

## 3 · Maturity Model

**Definición**: dónde estás HOY. No es "cuánto sabes" · es "cuán consistentemente operas a tu nivel declarado".

### 5 niveles canónicos

| Nivel | Estado | Fase del playbook |
|---|---|---|
| **0** Inconsciente | No sabes que existe el dominio | — |
| **1** Consciente-incompetente | Sabes que existe · sabes que no sabes | Aprender · Escalas 1-2 |
| **2** Consciente-competente | Sabes hacerlo con esfuerzo · recordando pasos | Aprehender · Escala 3 |
| **3** Inconsciente-competente | Lo haces sin pensar · hábito · natural | Practicante · Escalas 4-5 |
| **4** Maestro | Operas en automático Y enseñas · ves patrones que Nivel 3 no | Versado/Experto · Escalas 6-7 |

### Mapeo a las 10 Escalas del playbook

| Escala | Nombre | Maturity | Horas |
|---|---|---|---|
| 0 | Ignorante | 0 Inconsciente | 0 |
| 1 | Curioso | 1 Cons-Incomp | 1-4 |
| 2 | Explorador | 1 (refinado) | 4-20 |
| 3 | Iniciado | 2 Cons-Comp | 20-64 |
| 4 | Practicante | 3 Incons-Comp | 64-200 |
| 5 | Competente | 3 (refinado) | 200-500 |
| 6 | Versado | 4 (entrada) | 500-1,000 |
| 7 | Experto | 4 (consolidado) | 1,000-10,000 |
| 8 | Maestro | 4+ (cross-disciplina) | 10,000+ |
| 9 | Referente | 4++ (define el campo) | 10,000+ |

→ detalle: `references/03-diez-escalas-maestria.md`.

### Cómo medir madurez sin auto-engaño

Auto-evaluación pura es **peligrosa** por sesgo Dunning-Kruger `[DOC: Dunning & Kruger 1999]`:
- Niveles bajos sobreestiman.
- Niveles altos subestiman.

### Protocolo · auto + IA + humano

| Paso | Fuente | Acción |
|---|---|---|
| 1 | Auto | Para cada capability: ¿Nivel 0/1/2/3/4? |
| 2 | IA | Prompt #8 · 5 preguntas abiertas por nivel · veredicto del nivel |
| 3 | Comparar | Auto vs IA · diferencia ≤1 nivel = confiable · ≥2 = bias |
| 4 | Humano (mensual) | Colega senior: ¿en qué nivel me ves? |

### Reglas de cierre del bias

| Auto vs IA | Diagnóstico |
|---|---|
| Auto > IA por ≥2 | Sobreestimando · Mount Stupid |
| Auto < IA por ≥2 | Subestimando · Valle de la Humildad |
| Diferencia ≤1 | Calibrado · confiable |

`[CASO-BORDE]` Auto-eval Escala 3 + IA-eval Escala 2 NO es Dunning-Kruger crítico (delta=1). Es zona de calibración aceptable. Reservar el flag para delta ≥2.

`[CASO-BORDE]` Si auto < IA (subestimando), no celebrar: típicamente significa Imposter Syndrome, que paraliza tanto como Dunning-Kruger inflado. Ambos extremos requieren feedback humano.

### Quality gate del Maturity Model

- [ ] Auto-eval completa (todos capabilities clasificados 0-4)
- [ ] IA-eval con Prompt #8 ejecutado · resultado guardado
- [ ] Diferencia auto vs IA ≤1 nivel para >80% de capabilities
- [ ] Validación humana ≥1× (colega senior)
- [ ] Plan de progresión: cuáles 3 capabilities con mayor gap

---

## Combinación de los 3 modelos · workflow 1 hora

```
0:00       Definir objetivo (rol · certificación · problema concreto)
0:00-0:15  BoK · 3 IAs · triangular · validar fuentes 1°
0:15-0:30  Capability · subset relevante · validar con experto · priorizar
0:30-0:45  Maturity · auto + IA (Prompt #8)
0:45-1:00  Plan · 3 capabilities con mayor gap · 4/20/64 h según gap · agendar
```

```
        ┌────────────────────────┐
        │  BODY OF KNOWLEDGE     │  Mapa del campo
        └───────────┬────────────┘
                    ▼
        ┌────────────────────────┐
        │  CAPABILITY MODEL      │  Subset que TÚ necesitas
        └───────────┬────────────┘
                    ▼
        ┌────────────────────────┐
        │  MATURITY MODEL        │  Tu ubicación actual
        └───────────┬────────────┘
                    ▼
        ┌────────────────────────┐
        │  PLAN DE PROGRESIÓN    │  Capability gap × tiempo
        └────────────────────────┘
```

→ Workflow 1 enfoca BoK (`workflows/workflow-1-curioso.md`). Workflow 3 cierra ciclo completo (`workflows/workflow-3-iniciado.md`).

---

## Errores comunes (matriz)

| Error | Síntoma | Corrección |
|---|---|---|
| BoK de 1 sola IA | Conoces solo blindspots de tu IA preferida | Triangulación 3+ IAs · validar fuente 1° |
| Capability sin experto | Capabilities que la industria no valora | Validación con senior del campo |
| Maturity sin diagnóstico abierto | Dunning-Kruger oculto | Test abierto con IA + feedback humano |
| BoK sin Capability | Saber mucho, hacer poco | Filtrar BoK por objetivo concreto |
| Capability sin Maturity | Plan irreal sin punto de partida | Diagnosticar nivel actual antes de planear |
| Maturity sin BoK | "Soy experto en X" sin saber qué es X completo | Mapear el campo antes de medir madurez |
| 3 modelos sin priorizar | Análisis-parálisis · 0 ejecución | Aplicar workflow 1 h · cerrar con plan |

---

## Validación rápida (auto-test) para tu tema activo

- [ ] BoK triangulado en ≥3 IAs
- [ ] BoK incluye ≥3 fuentes primarias verificables
- [ ] Capability Model con 4 niveles
- [ ] Capability validado con humano del campo
- [ ] Auto-diagnóstico de madurez por capability
- [ ] IA-diagnóstico con Prompt #8 ejecutado
- [ ] Auto y IA coinciden ±1 nivel
- [ ] Plan de progresión con horas asignadas

`[CRITERIO-ACEPTACIÓN]` <6/8 → fundación incompleta · empezar por BoK.

---

## Referencias cruzadas

- Sustento: `references/06-ciencia-cognitiva-fuentes.md` §Adult Learning + §Dunning-Kruger
- Anti-patrones: `references/04-anti-patrones-y-trampas.md` §Single-AI BoK · §Dunning-Kruger
- Escalas: `references/03-diez-escalas-maestria.md`
- Prompts: `prompts/01-research-blueprint.md` · `prompts/04-cross-fact-check.md` · `prompts/08-evaluator-certification.md`
- Workflows: `workflows/workflow-1-curioso.md` · `workflows/workflow-3-iniciado.md`

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · `[FUENTE-PRIMARIA]` Playbook v2.0.0 §Modelos Fundacionales
