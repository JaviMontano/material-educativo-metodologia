# Prompt #1 · Research Blueprint

> Plan metodológico de investigación para cualquier tema nuevo. Genera Body of Knowledge inicial, glosario y concept map.

**Fase**: Aprender (Escala 0→1)
**Workflow**: 1 (Curioso) · 1-4 horas
**IA recomendada**: ChatGPT, Claude, Gemini · **úsalo en 3 IAs distintas para triangulación**.

---

## Cuándo usarlo

- ✅ Cualquier tema profesional/técnico nuevo donde estás Escala 0-1
- ✅ Antes de invertir 20+ horas en aprender algo
- ✅ Cuando alguien te pide "investigar X" y no sabes por dónde empezar
- ✅ Como kickoff de un sprint de catch-up (`scripts/desatraso_planner.py`)

## Cuándo NO usarlo

- ❌ Si ya estás Escala 3+ del tema (este es para empezar)
- ❌ Si solo necesitas un dato puntual (sobre-ingeniería)
- ❌ Si no tienes tiempo para triangular en 3 IAs (usa Prompt #3 más rápido)

---

## Variables a personalizar

| Variable | Reemplazar con |
|---|---|
| `[TU TEMA]` | Dominio específico · ej. "Sistemas Distribuidos", "Rust", "Diseño de APIs REST" |
| `[TU OBJETIVO]` | Qué quieres lograr · ej. "pasar AWS SAA-C03 en 2 meses" |
| `[TU NIVEL ACTUAL]` | Escala 0-9 honesta · ej. "Escala 1 Curioso · sé que existe pero no defino" |

---

## El Prompt

```
Eres un experto con 15+ años en [TU TEMA].

Mi objetivo: [TU OBJETIVO]
Mi nivel actual: [TU NIVEL ACTUAL]

Genera un Research Blueprint completo estructurado así:

1. DEFINICIÓN PRECISA (2-3 frases)
   Qué es exactamente [TU TEMA]. Sin marketing.

2. BODY OF KNOWLEDGE (BoK)
   - Subtemas principales (5-10 ramas)
   - Conexiones interdisciplinarias (con qué otros campos se relaciona)
   - Estado del arte actual (2024-2026)

3. GLOSARIO MÍNIMO (15-30 términos clave)
   Para cada término: definición de 1 frase + por qué importa.
   Ordenados por importancia (los 5 primeros son los críticos).

4. CONCEPT MAP JERÁRQUICO
   Genera en formato Mermaid mindmap:
   ```mermaid
   mindmap
     root([TU TEMA])
       Rama 1
         Concepto 1.1
         Concepto 1.2
       Rama 2
         ...
   ```

5. FUENTES PRIMARIAS RECOMENDADAS
   - Papers fundacionales (autor + año + por qué importa)
   - Libros canónicos (autor + título + edición)
   - Cursos / certificaciones (sólo si son canónicas)
   IMPORTANTE: solo cita fuentes que existen. Si no estás seguro, marca [VERIFICAR].

6. AUTORIDADES DEL CAMPO
   3-5 nombres + por qué son referentes (no opinión, hechos: papers, premios, contribuciones).

7. CONTROVERSIAS / DEBATES ABIERTOS
   2-3 áreas donde no hay consenso. Cuál es cada lado del debate.

8. DIRECCIONES FUTURAS
   Hacia dónde va el campo en los próximos 3-5 años.

9. RUTA DE APRENDIZAJE PARA MI OBJETIVO
   Dado mi nivel ([TU NIVEL ACTUAL]) y objetivo ([TU OBJETIVO]):
   - Qué subset del BoK debo priorizar
   - Tiempo estimado en horas (con rangos: optimista / realista / pesimista)
   - Hitos verificables a las 4h, 20h, 64h

REGLAS:
- Cita autores y años para fuentes primarias
- Sé exhaustivo, no superficial
- Si NO sabes algo con certeza, dilo: "No tengo certeza sobre X"
- Para cada afirmación factual, marca tu nivel de confianza: [ALTA] [MEDIA] [BAJA]
- Si una fuente puede ser hallucination, marca [VERIFICAR]
```

---

## Cómo usar la respuesta

### Paso 1 · Triangulación
Ejecuta este mismo prompt en **3 IAs distintas** (e.g., ChatGPT + Claude + Gemini).

### Paso 2 · Comparación
Crea una tabla:

| Elemento | ChatGPT | Claude | Gemini | Veredicto |
|---|---|---|---|---|
| Subtema 1 | ✅ | ✅ | ✅ | CONFIRMED |
| Autor X | ✅ | ❌ | ✅ | REVISAR |
| Paper Y · 2018 | ✅ | ❌ | ❌ | SOSPECHOSO · validar fuente |

→ ver `assets/plantilla-triangulacion.md`.

### Paso 3 · Fact-check
Toma el resultado consolidado y pásalo por **Prompt #4** en una 4ª IA independiente.

### Paso 4 · Cargar en NotebookLM
- Crea un nuevo Notebook
- Importa cada respuesta como source
- Configura el chat con Prompt #2 (Coach) usando `[TU TEMA]`
- Empieza a interactuar como tutor 24/7

### Paso 5 · Validar gates
```
[ ] BoK triangulado en 3+ IAs
[ ] Glosario con ≥15 términos consolidado
[ ] ≥3 fuentes primarias verificadas (no terciarias)
[ ] Concept map mermaid generado
[ ] Auditor cruzado (Prompt #4) sin [NO SOURCE] crítico
```

---

## Output esperado (estructura)

Una respuesta bien ejecutada tiene estas características:

✅ **2-3 páginas** (no 1 párrafo, no 20 páginas)
✅ **15-30 términos** en glosario, no 5 ni 100
✅ **Citas con año** en autoridades y fuentes
✅ **Marcas de confianza** [ALTA/MEDIA/BAJA] visibles
✅ **Concept map mermaid** ejecutable
✅ **Tiempo estimado** con rangos, no número único

---

## Ejemplo · Aplicado a "Sistemas Distribuidos"

> Variables:
> - TU TEMA: "Sistemas Distribuidos"
> - TU OBJETIVO: "Diseñar arquitecturas escalables para 10M+ usuarios"
> - TU NIVEL ACTUAL: "Escala 2 Explorador · entiendo CAP, Raft a nivel conceptual"

**Respuesta esperada incluiría**:

```
1. DEFINICIÓN: Arquitecturas que coordinan múltiples nodos computacionales
   geográficamente o lógicamente separados para servir una función unificada,
   manteniendo consistencia, disponibilidad y tolerancia a fallas.

2. BoK SUBTEMAS:
   - Consenso (Paxos, Raft, PBFT)
   - Replicación (master-slave, multi-master, eventual)
   - Particionamiento (sharding, consistent hashing)
   - Tolerancia a fallas
   - Coordinación (Zookeeper, etcd)
   - Comunicación (RPC, message queues, event sourcing)

3. GLOSARIO (top 5):
   - CAP Theorem [ALTA]: trade-off Consistency/Availability/Partition tolerance
   - Eventual Consistency [ALTA]: estado convergerá, no inmediato
   - Quorum [ALTA]: mayoría requerida para decisión válida
   - Vector Clock [MEDIA]: orden parcial de eventos distribuidos
   - Byzantine Fault [MEDIA]: nodos pueden mentir, no solo fallar

4. CONCEPT MAP (mermaid)... [genera el diagrama]

5. FUENTES PRIMARIAS:
   - Lamport · Time, Clocks, and Ordering · 1978 [ALTA]
   - Brewer · CAP Theorem · 2000 [ALTA]
   - DeCandia et al. · Dynamo · 2007 [ALTA]
   - Ongaro & Ousterhout · Raft · 2014 [ALTA]

6. AUTORIDADES: Lamport, Stonebraker, Dean, Helland, Kleppmann

7. CONTROVERSIAS:
   - ACID vs BASE (cuándo cada uno)
   - CAP vs PACELC (refinamiento moderno)
   - Microservicios vs Monolitos (péndulo de moda)

8. DIRECCIONES FUTURAS:
   - CRDTs (Conflict-Free Replicated Data Types)
   - Serverless distribuido
   - Edge computing

9. RUTA PARA TU OBJETIVO (Escala 2 → Escala 4 · 6 meses):
   - 4h: Refinar CAP, Quorum, Vector Clocks (Workflow 1)
   - 20h: Profundizar Raft + ejercicios prácticos (Workflow 2)
   - 64h: Diseñar 3 sistemas reales con trade-offs documentados (Workflow 3)
   - 200h: Implementar uno en producción
```

---

## Errores comunes al usar este prompt

| Error | Síntoma | Corrección |
|---|---|---|
| No reemplazar variables | Respuesta genérica sobre "Tu Tema" | Reemplaza siempre |
| Solo 1 IA | Conoces solo el sesgo de esa IA | Triangulación obligatoria |
| Ignorar [VERIFICAR] | Citas hallucinations | Verifica cada fuente primaria |
| Saltar Concept Map | Solo texto, no jerarquía visual | Pide explícitamente mermaid |
| No iterar | Aceptar primera respuesta | Pregunta seguimientos |

---

## Combo recomendado

```
DÍA 1:
- 09:00 Prompt #1 en ChatGPT (15 min)
- 09:15 Prompt #1 en Claude (15 min)
- 09:30 Prompt #1 en Gemini (15 min)
- 09:45 Consolidación + tabla triangulación (30 min)
- 10:15 Prompt #4 (Fact-Check) en 4ª IA (15 min)
- 10:30 Prompt #7 (Audit) sobre BoK consolidado (15 min)
- 10:45 Crear NotebookLM con sources (15 min)
- 11:00 Configurar Coach con Prompt #2 (15 min)

TOTAL: 2 horas · sales con BoK validado y NotebookLM listo.
```

---

## Validación rápida (auto-test)

¿Tu Blueprint está bien? Marca:

- [ ] Tiene 9 secciones completas (no me saltó ninguna)
- [ ] Glosario tiene ≥15 términos
- [ ] Cada autor tiene año de referencia
- [ ] Concept map en mermaid (ejecuta visualmente)
- [ ] Triangulado en 3 IAs distintas
- [ ] Fact-check en 4ª IA hecho
- [ ] ≥3 fuentes primarias verificadas
- [ ] Tiempo estimado con rangos (no número único)

Si tienes <6 marcas → tu Blueprint está incompleto. Itera antes de avanzar a Workflow 2.

---

## Referencias

- `references/02-tres-modelos-fundacionales.md` §Body of Knowledge
- `references/04-anti-patrones-y-trampas.md` §Single-AI BoK
- `katas/kata-triangulacion-3ias.md`
- `workflows/workflow-1-curioso.md`

---

> **Prompt #1** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
