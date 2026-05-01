# 3 Modelos Fundacionales · Body of Knowledge · Capability · Maturity

> Los 3 modelos que estructuran cualquier dominio profesional. Son la **arquitectura mental** de cualquier disciplina que quieras dominar.

**Fuente canónica**: Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · §Modelos Fundacionales.

---

## Por qué estos 3 modelos

Cualquier dominio profesional puede mapearse en estas tres preguntas:

| Modelo | Pregunta que responde | Metáfora |
|---|---|---|
| **Body of Knowledge (BoK)** | ¿QUÉ EXISTE en este campo? | Mapa del territorio |
| **Capability Model** | ¿QUÉ NECESITO SABER HACER? | Cinta de karate (niveles) |
| **Maturity Model** | ¿DÓNDE ESTOY HOY? | GPS / termómetro |

Los 3 son complementarios. El BoK te dice qué hay (territorio). El Capability te dice qué necesitas (objetivo). El Maturity te dice dónde estás (posición). **Sin los 3, navegas a ciegas.**

---

## 1 · Body of Knowledge (BoK)

### Definición
**El mapa completo del dominio**: subtemas, conexiones interdisciplinarias, fuentes primarias, secundarias y terciarias, controversias abiertas, futuro del campo.

### Por qué importa
Sin BoK, no sabes qué desconoces. Te quedas estudiando los 3 temas que viste en redes sociales y crees que es todo el campo. **Las omisiones invisibles son el peor riesgo.**

### Estructura canónica de un BoK

```
[DOMINIO]
├── Definición precisa (1-3 frases)
├── Historia / contexto (cómo llegamos aquí)
├── Subtemas principales (ramas del campo)
│   ├── Sub-rama A
│   ├── Sub-rama B
│   └── Sub-rama C
├── Conexiones interdisciplinarias
│   ├── Con [otro campo]
│   └── Con [otra disciplina]
├── Fuentes primarias (papers fundacionales, libros canónicos)
├── Fuentes secundarias (autoridades del campo, conferencias)
├── Fuentes terciarias (resúmenes, blogs, cursos derivados)
├── Estado del arte actual
├── Controversias / debates abiertos
└── Direcciones futuras
```

### Ejemplo · BoK de "Sistemas Distribuidos"

```
SISTEMAS DISTRIBUIDOS
├── Definición: arquitecturas que coordinan múltiples nodos
│   computacionales para servir una función unificada
├── Historia:
│   ├── 1970s: ARPANET, primeros protocolos
│   ├── 1980s: NFS, RPC
│   ├── 1990s: CORBA, web
│   ├── 2000s: BigTable, MapReduce, Dynamo
│   └── 2010s+: Kubernetes, microservicios, service mesh
├── Subtemas:
│   ├── Consenso (Paxos, Raft, PBFT)
│   ├── Replicación (master-slave, multi-master, eventual)
│   ├── Particionamiento (sharding, consistent hashing)
│   ├── Tolerancia a fallas (failover, retry, circuit breaker)
│   ├── Coordinación (Zookeeper, etcd)
│   └── Comunicación (RPC, message queues, event sourcing)
├── Conexiones:
│   ├── Con Redes (TCP/IP, latencia, particiones)
│   ├── Con Bases de Datos (CAP theorem, consistencia)
│   └── Con Sistemas Operativos (concurrencia, locks)
├── Fuentes primarias:
│   ├── Lamport · Time, Clocks, and the Ordering of Events · 1978
│   ├── Brewer · CAP Theorem · 2000
│   ├── DeCandia et al. · Dynamo · 2007
│   └── Ongaro & Ousterhout · Raft · 2014
├── Autoridades: Lamport, Stonebraker, Dean, Helland, Kleppmann
├── Controversias: ACID vs BASE, CAP vs PACELC, NewSQL
└── Futuro: serverless distribuido, edge computing, CRDTs
```

### Cómo generar un BoK con IA (Prompt #1)

```
Eres experto con 15+ años en [DOMINIO]. Genera el Body of Knowledge
completo de [DOMINIO] estructurado así:
1. Definición precisa (2-3 frases)
2. Subtemas principales (5-10 ramas)
3. Conexiones interdisciplinarias (3+ campos)
4. Fuentes primarias (papers fundacionales o libros canónicos)
5. Glosario mínimo (15-20 términos clave)
6. Estado del arte actual
7. Controversias abiertas
8. Direcciones futuras

Importante: cita autores y años para fuentes primarias.
Sé exhaustivo, no superficial.
```

→ ver `prompts/01-research-blueprint.md`.

### Anti-patrón crítico: BoK de 1 sola IA

> *"Las omisiones de una IA aparecen en otra. Triangular es mandatory."*
> `[FUENTE-PRIMARIA: Playbook §Aprender · Triangulación Protocol]`

Genera el BoK en **3 IAs distintas** (e.g., ChatGPT + Claude + Gemini), luego:

```
COINCIDENCIAS ENTRE LAS 3 → verdad probable, alta confianza
COINCIDENCIAS ENTRE 2     → verdad media, validar con fuente primaria
APARECE EN 1 SOLA         → sospechoso, investigar manual o descartar
CONTRADICCIONES           → ORO · ahí están las áreas de debate
```

→ ver `katas/kata-triangulacion-3ias.md`, `prompts/04-cross-fact-check.md`.

### Quality gate del BoK

```
[ ] Triangulado en ≥3 IAs
[ ] ≥5 subtemas mapeados
[ ] ≥3 fuentes primarias verificables (no terciarias)
[ ] Glosario mínimo de 15 términos
[ ] Conexiones interdisciplinarias mapeadas
[ ] Concept map jerárquico generado (mermaid)
```

---

## 2 · Capability Model (Modelo de Capacidades)

### Definición
**Lo que necesitas saber HACER, organizado en niveles de progresión**, tipo cintas de karate. Cada nivel tiene criterios de aceptación claros y demostraciones prácticas.

### Por qué importa
El BoK te dice qué hay; el Capability te dice **qué subset DEBES manejar para tu rol/objetivo**. No todos necesitan todo el BoK. Un backend developer no necesita el subset completo de UI/UX.

### Estructura canónica

```
[ROL / OBJETIVO]
├── NIVEL 1 · FUNDAMENTOS
│   ├── Capability 1.1: [habilidad atómica]
│   │   ├── Criterio aceptación: [test demostrable]
│   │   └── Recurso: [referencia para aprender]
│   ├── Capability 1.2: ...
│   └── ...
├── NIVEL 2 · INTERMEDIO
│   ├── Capability 2.1
│   └── ...
├── NIVEL 3 · AVANZADO
│   ├── Capability 3.1
│   └── ...
└── NIVEL 4 · EXPERTO
    └── ...
```

### Ejemplo · Capability Model · "Backend Engineer Distribuido"

```
NIVEL 1 · FUNDAMENTOS (0-6 meses)
├── 1.1 Implementar REST API con CRUD completo
│       Test: API funcional con auth + paginación + tests
├── 1.2 Modelar relaciones en SQL con índices apropiados
│       Test: schema normalizado + queries optimizadas
├── 1.3 Manejar transacciones ACID
│       Test: implementar transferencia bancaria sin race conditions
└── 1.4 Configurar logging estructurado
        Test: trazas de request end-to-end

NIVEL 2 · INTERMEDIO (6-18 meses)
├── 2.1 Diseñar APIs idempotentes con retry-safe
├── 2.2 Implementar circuit breaker pattern
├── 2.3 Cachear con invalidación correcta
├── 2.4 Diagnosticar performance con profiling
└── 2.5 Diseñar para failure (chaos engineering básico)

NIVEL 3 · AVANZADO (18+ meses)
├── 3.1 Diseñar sistemas distribuidos con CAP en mente
├── 3.2 Implementar consensus (Raft/Paxos básico)
├── 3.3 Diseñar event sourcing + CQRS
├── 3.4 Optimizar costos cloud (FinOps)
└── 3.5 Mentorizar Nivel 1 sin micro-management

NIVEL 4 · EXPERTO (5+ años)
├── 4.1 Definir arquitecturas para 100M+ usuarios
├── 4.2 Hacer trade-offs cross-cutting (security/perf/cost)
├── 4.3 Influir en estándares de industria (RFCs, OSS)
└── 4.4 Formar siguiente generación de Nivel 3
```

### Cómo generar un Capability Model

**Manual (recomendado)**: pregunta a un experto del campo en quien confíes. Esto es **opinión validada**, no consenso de IAs.

**Con IA (validar después)**:
```
Soy [TU ROL ACTUAL] objetivo: [TU ROL DESEADO].
Genera un Capability Model con 4 niveles (Fundamentos / Intermedio /
Avanzado / Experto). Para cada capability:
1. Nombre atómico (1 frase)
2. Criterio de aceptación testable
3. Recurso para aprenderla
Importante: cada capability debe ser DEMOSTRABLE, no teórica.
```

### Anti-patrón crítico

**Confiar 100% en IA para Capability Model**: la IA puede inventar capabilities que suenan bien pero no son las que tu industria realmente espera. **Valida con un experto humano** antes de basar tu plan de carrera en él.

> *"El Capability Model es la única parte de los 3 modelos donde el experto humano supera a la IA. Las IAs pueden conocer la teoría, pero no la realidad de tu mercado."* `[FUENTE-PRIMARIA: Playbook §Modelos]`

### Tu Capability Personal vs el del Mercado

```
CAPABILITY MERCADO    ← lo que se espera de tu rol en tu industria
        ∩
CAPABILITY PERSONAL   ← lo que TÚ necesitas según tu objetivo único
        =
GAP ANÁLISIS          ← qué te falta · qué te sobra · qué priorizar
```

### Quality gate del Capability Model

```
[ ] 4 niveles definidos (Fundamentos → Experto)
[ ] ≥3 capabilities por nivel
[ ] Cada capability tiene criterio testable
[ ] Validado con ≥1 experto humano del campo
[ ] Tu nivel actual identificado
[ ] Plan de progresión a siguiente nivel definido
```

---

## 3 · Maturity Model (Modelo de Madurez)

### Definición
**Escala que mide DÓNDE ESTÁS HOY** respecto al dominio. No es "cuánto sabes"; es "cuán consistentemente operas a tu nivel declarado".

### Metáfora · GPS

- **BoK** = el mapa
- **Capability** = el destino al que quieres llegar
- **Maturity** = tu ubicación actual GPS

Sin Maturity, planeas un viaje sin saber el punto de partida → destino imposible de calcular.

### Estructura canónica · 5 niveles de madurez

```
NIVEL 0 · INCONSCIENTE
   No sabes que existe el dominio. No tienes opinión.

NIVEL 1 · CONSCIENTE-INCOMPETENTE
   Sabes que existe. Sabes que no sabes. Eres consciente de los gaps.
   (Esta es la fase Aprender en el playbook)

NIVEL 2 · CONSCIENTE-COMPETENTE
   Sabes hacerlo, pero requiere esfuerzo, atención, recordar pasos.
   (Iniciado · Escala 3 del playbook)

NIVEL 3 · INCONSCIENTE-COMPETENTE
   Lo haces sin pensar. Hábito. Te sale natural.
   (Practicante · Escala 4-5)

NIVEL 4 · MAESTRO
   Operas en automático Y enseñas a otros a operar bien.
   Ves patrones que los Nivel 3 no ven.
   (Experto · Escala 6-7)
```

### Conexión con las 10 Escalas del playbook

| Escala (playbook) | Maturity Level | Horas |
|---|---|---|
| 0 Ignorante | Nivel 0 Inconsciente | 0 |
| 1 Curioso | Nivel 1 Consciente-incompetente | 1-4 |
| 2 Explorador | Nivel 1 (refinado) | 4-20 |
| 3 Iniciado | Nivel 2 Consciente-competente | 20-64 |
| 4 Practicante | Nivel 3 Inconsciente-competente | 64-200 |
| 5 Competente | Nivel 3 (refinado) | 200-500 |
| 6 Versado | Nivel 4 Maestro (entrada) | 500-1,000 |
| 7 Experto | Nivel 4 Maestro (consolidado) | 1,000-10,000 |
| 8 Maestro | Nivel 4+ (cross-disciplina) | 10,000+ |
| 9 Referente | Nivel 4++ (define el campo) | 10,000+ |

→ detalle completo: `references/03-diez-escalas-maestria.md`.

### Cómo medir tu madurez (sin auto-engaño)

**Auto-evaluación es peligrosa** por sesgo Dunning-Kruger:
- Niveles bajos sobreestiman su nivel.
- Niveles altos subestiman su nivel.

**Protocolo recomendado** (combinación auto + IA + humano):

```
PASO 1 · AUTO-DIAGNÓSTICO
   Para cada capability del Capability Model:
   - ¿Lo hago en automático (Nivel 3)?
   - ¿Lo hago con esfuerzo (Nivel 2)?
   - ¿Sé que existe pero no lo manejo (Nivel 1)?
   - ¿No sabía que existía (Nivel 0)?

PASO 2 · IA DIAGNÓSTICO
   Pide a NotebookLM con Prompt #8:
   *"Hazme un examen de [DOMINIO] con preguntas abiertas (NO multiple
    choice). 5 preguntas por nivel (Fundamentos → Experto). Evalúa
    mis respuestas y dame veredicto del nivel."*

PASO 3 · COMPARAR
   Si auto-eval coincide con IA-eval ±1 nivel → confiable.
   Si difiere ≥2 niveles → BIAS DETECTADO.
   - Si auto-eval > IA-eval → estás sobreestimando.
   - Si auto-eval < IA-eval → estás subestimando.

PASO 4 · VALIDACIÓN HUMANA (mensual)
   Pide feedback a colega senior: ¿en qué nivel me ves?
   Compara con auto-eval e IA-eval.
```

### Anti-patrón · Dunning-Kruger

> *"Los que más saben dudan. Los que menos saben afirman."* `[DOC: Dunning & Kruger · 1999]`

Síntoma típico: alguien con 3 meses de experiencia se autoidentifica como "senior". Alguien con 10 años se autoidentifica como "intermedio". El primero está en la cima del Mount Stupid; el segundo en el Valle de la Humildad.

**Antídoto**: pruebas abiertas (no multiple choice), feedback de pares senior, defensa pública del conocimiento.

→ ver `references/04-anti-patrones-y-trampas.md`.

### Quality gate del Maturity Model

```
[ ] Auto-evaluación completa (todos los capabilities clasificados)
[ ] IA-evaluación completa (Prompt #8 ejecutado, resultado guardado)
[ ] Diferencia auto vs IA ≤1 nivel para >80% de capabilities
[ ] Validación humana al menos 1× (colega senior)
[ ] Plan de progresión: qué hago para avanzar 1 nivel en X capabilities
```

---

## Cómo se combinan los 3 modelos

```
                     BODY OF KNOWLEDGE
                     (Mapa del campo)
                            │
                            ▼
                    CAPABILITY MODEL
                  (Subset que tú necesitas)
                            │
                            ▼
                    MATURITY MODEL
                  (Tu ubicación actual)
                            │
                            ▼
                    PLAN DE PROGRESIÓN
              (Capability gap × tiempo invertido)
```

### Workflow completo (1 hora)

```
0:00 · Definir tu objetivo (rol, certificación, problema a resolver)

0:00-0:15 · BoK
    Genera con 3 IAs · triangula · valida fuentes primarias

0:15-0:30 · Capability Model
    Define el subset relevante · valida con experto · prioriza

0:30-0:45 · Maturity Self-Assessment
    Para cada capability priorizada: ¿en qué nivel estoy?
    Auto + IA (Prompt #8)

0:45-1:00 · Plan de progresión
    Identifica los 3 capabilities con mayor gap
    Asigna 4 / 20 / 64 horas según tamaño del gap
    Agenda en calendario
```

→ ver `workflows/workflow-1-curioso.md` (BoK) y `workflows/workflow-3-iniciado.md` (progresión completa).

---

## Errores comunes al aplicar los 3 modelos

| Error | Síntoma | Corrección |
|---|---|---|
| BoK de 1 sola IA | Conoces solo lo que tu IA preferida menciona | Triangulación 3+ IAs |
| Capability sin experto | Capabilities que la industria no valora | Validación con senior del campo |
| Maturity sin diagnóstico | Auto-engaño Dunning-Kruger | Test abierto con IA + feedback humano |
| BoK sin Capability | Saber mucho, hacer poco | Filtrar BoK por tu objetivo concreto |
| Capability sin Maturity | Plan irreal sin punto de partida | Diagnosticar nivel actual antes de planear |
| Maturity sin BoK | "Soy experto en X" sin saber qué es X completo | Mapear el campo antes de medir madurez |

---

## Validación rápida (auto-test)

Para tu tema activo:

- [ ] ¿Tengo BoK triangulado en ≥3 IAs?
- [ ] ¿El BoK incluye ≥3 fuentes primarias verificables?
- [ ] ¿Tengo Capability Model con 4 niveles?
- [ ] ¿Validé el Capability Model con un humano del campo?
- [ ] ¿Hice auto-diagnóstico de madurez?
- [ ] ¿Hice IA-diagnóstico (Prompt #8)?
- [ ] ¿Auto y IA coinciden ±1 nivel?
- [ ] ¿Tengo plan de progresión con horas asignadas?

Si tienes <6 marcas → tu fundación está incompleta. Empieza por BoK.

---

> **Atribución**: Modelos extraídos del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 §Modelos Fundacionales.
> *MetodologIA · CC BY-NC-SA 4.0*
