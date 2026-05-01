# Plantilla · Glosario · 30 términos

> Tabla canónica · ontología del dominio. Mínimo 15 · target 30.

**Tema**: [TU TEMA]
**Generado**: [fecha]
**Última actualización**: [fecha]

---

## Tabla de términos

| # | Término | Definición (1 frase) | Por qué importa | Conexiones | Tag | Fuente |
|---|---|---|---|---|---|---|
| 1 | [Término] | [definición] | [importancia] | [otros términos] | [DOC] | [autor año] |
| 2 | | | | | [DOC] | |
| 3 | | | | | [INFERENCIA] | |
| 4 | | | | | [SUPUESTO] | |
| 5 | | | | | [DOC] | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |
| 13 | | | | | | |
| 14 | | | | | | |
| 15 | | | | | | |
| 16 | | | | | | |
| 17 | | | | | | |
| 18 | | | | | | |
| 19 | | | | | | |
| 20 | | | | | | |
| 21 | | | | | | |
| 22 | | | | | | |
| 23 | | | | | | |
| 24 | | | | | | |
| 25 | | | | | | |
| 26 | | | | | | |
| 27 | | | | | | |
| 28 | | | | | | |
| 29 | | | | | | |
| 30 | | | | | | |

---

## Tags de evidencia

- `[DOC]` · documento verificable identificado (paper, libro, RFC)
- `[INFERENCIA]` · deducción lógica desde fuentes primarias
- `[SUPUESTO]` · asunción no validada · pendiente verificación
- `[FUENTE-PRIMARIA]` · referencia a documento original verificado

**Regla**: cada término debe tener tag. Sin tag = se asume `[SUPUESTO]`.

---

## Validación

```
[ ] Mínimo 15 términos
[ ] Cada término con definición concisa (1 frase)
[ ] Cada término con tag de evidencia
[ ] Términos críticos con [DOC] o [FUENTE-PRIMARIA]
[ ] Conexiones identificadas entre al menos 5 términos
[ ] No términos duplicados o sinónimos sin justificación
```

---

## Ejemplo aplicado · Sistemas Distribuidos (top 5)

| # | Término | Definición | Por qué importa | Conexiones | Tag | Fuente |
|---|---|---|---|---|---|---|
| 1 | CAP Theorem | Trade-off entre Consistency, Availability, Partition tolerance | Define límites fundamentales del diseño | Eventual Consistency, Quorum | [FUENTE-PRIMARIA] | Brewer 2000 |
| 2 | Eventual Consistency | Estado convergerá pero no instantáneamente | Permite alta disponibilidad | CAP, Vector Clock | [FUENTE-PRIMARIA] | DeCandia et al. 2007 |
| 3 | Quorum | Mayoría requerida para decisión válida | Base de Raft, Paxos | Consensus, CAP | [DOC] | Lamport 1998 |
| 4 | Vector Clock | Orden parcial de eventos distribuidos | Detecta causalidad | Happens-before | [FUENTE-PRIMARIA] | Lamport 1978 |
| 5 | Byzantine Fault | Nodos pueden mentir, no solo fallar | Diseño en presencia de adversarios | PBFT, Blockchain | [DOC] | Lamport et al. 1982 |

---

## Plantilla expandida (con relaciones)

Para conceptos avanzados, expande con relaciones:

```
TÉRMINO: Eventual Consistency
- DEFINICIÓN: Estado convergerá pero no instantáneamente
- ANTÓNIMOS: Strong Consistency, Linearizability
- ESPECIALIZACIONES: Causal Consistency, Read-your-writes
- CONTEXTO: aplicar cuando availability > consistency inmediata
- LIMITACIÓN: NO usar en transferencias bancarias
- AUTORIDADES: DeCandia (Dynamo), Helland
```

---

## Cuándo expandir / cuándo simplificar

**Expandir** (Escala 2+):
- Cada controversia del campo amerita 2-3 términos relacionados
- Variantes de un concepto (ej. tipos de Consistency)

**Simplificar** (Escala 0-1):
- 15-20 términos suficiente
- Foco en core, no en edge cases

---

> **Plantilla Glosario** del Playbook Aprender · Aprehender · (R)Evolucionar v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
