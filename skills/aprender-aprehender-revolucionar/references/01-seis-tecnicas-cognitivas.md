# 6 Técnicas Cognitivas · Ciencia del Aprendizaje

> Las 6 técnicas con mayor evidencia académica para retención duradera, transferencia y dominio. Base de la fase **Aprehender**.

**Fuente canónica**: Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · §Aprehender.
**Sustento académico**: ver `06-ciencia-cognitiva-fuentes.md`.

---

## Mapa de las 6 técnicas

| # | Técnica | Fase principal | Ranking evidencia | Tiempo/sesión |
|---|---|---|---|---|
| 1 | Retrieval Practice | Aprehender | ⭐⭐⭐⭐⭐ | 20–30 min |
| 2 | Spaced Repetition | Aprehender | ⭐⭐⭐⭐⭐ | 5–15 min/día |
| 3 | Feynman Technique | Cross-fase | ⭐⭐⭐⭐⭐ | 30 min |
| 4 | Interleaving | Aprehender | ⭐⭐⭐⭐ | 30–45 min |
| 5 | Elaboration | Aprehender + Aprender | ⭐⭐⭐⭐ | 15 min |
| 6 | Dual Coding | Aprender + Aprehender | ⭐⭐⭐⭐ | varía |

> Las 5 estrellas = "high utility" en el meta-análisis Dunlosky et al. 2013 `[DOC: Dunlosky · Improving Students' Learning · 2013]`.

---

## 1 · Retrieval Practice (Recuperación activa)

### Definición
Recuperar información de la memoria **sin pistas externas** (notas, libros, slides). Fuerza el cerebro a reconstruir el conocimiento, lo cual fortalece las conexiones neuronales más que releer.

### Por qué funciona `[DOC: Karpicke & Roediger · 2008 · Science]`
- Releer da **fluidez ilusoria** (reconoces el material → crees que lo sabes).
- Recuperar genera **desirable difficulty** (esfuerzo productivo) que codifica el conocimiento profundamente.
- Los estudios muestran 50–80% más retención a 1 semana vs releer.

### Protocolo (sesión de 20–30 min)

```
1. Cierra TODOS los materiales (notas, libros, slides, IA, navegador).
2. Toma una hoja en blanco.
3. Escribe TODO lo que recuerdes sobre [TEMA].
4. Sin volver a las notas: marca con [?] lo que dudas.
5. Ahora abre las fuentes y compara.
6. Marca cada elemento como:
   [FUERTE]   — recuperaste correctamente sin pista
   [PARCIAL]  — recuperaste pero con errores
   [DÉBIL]    — no recuperaste o estaba mal
7. Estudia SOLO lo [DÉBIL] y [PARCIAL].
8. Repite la sesión en 3 días (ver Spaced Repetition).
```

### Anti-patrón
**Recognition vs Recall**: ver el listado y decir "sí, lo conozco". *Reconocer ≠ recuperar*. La prueba real es papel en blanco.

### Con IA (NotebookLM)
- Pide al notebook: *"Hazme 5 preguntas abiertas sobre [TEMA]. No me des las respuestas. Yo respondo, tú evalúas con [FUERTE/PARCIAL/DÉBIL]."*
- Ver Prompt #2 (`prompts/02-coach-system-prompt.md`) y Prompt #8 (`prompts/08-evaluator-certification.md`).

### Cuándo usar
- ✅ Ritual semanal de aprehensión (`rituals/ritual-aprehension-semanal.md`).
- ✅ Antes de presentación o certificación.
- ✅ Después de cada bloque de estudio (al terminar el día).
- ❌ NO usar en lugar del estudio inicial (necesitas haber estudiado primero).

### Kata asociado
`katas/kata-recuperacion-ciega.md` (15 min · ejercicio dirigido).

---

## 2 · Spaced Repetition (Repetición espaciada)

### Definición
Revisar información en **intervalos crecientes**: mismo día → 3 días → 1 semana → 2 semanas → 1 mes → 3 meses → 6 meses.

### Por qué funciona `[DOC: Cepeda et al. · 2008 · Psychological Science]`
- La curva del olvido (Ebbinghaus 1885) muestra que olvidamos exponencialmente: 50% en 1 hora, 70% en 24h, 90% en 1 semana.
- Cada revisión justo antes del olvido **resetea** la curva y la hace más plana.
- 5 revisiones espaciadas > 50 revisiones consecutivas (cramming) en retención a 6 meses.

### Protocolo (intervalos canónicos del playbook)

```
DÍA  0: aprendizaje inicial
DÍA  0: primera revisión (al final del día) ─── retrieval session
DÍA  3: segunda revisión             ────────── retrieval session
DÍA  7: tercera revisión             ────────── retrieval session
DÍA 14: cuarta revisión              ────────── retrieval session
DÍA 30: quinta revisión              ────────── retrieval session
DÍA 90: sexta revisión               ────────── retrieval session
```

Si fallas en una revisión → vuelve al intervalo anterior. Si aciertas → avanza al siguiente intervalo.

### Anti-patrón
**Cramming** (maratón intensivo el día antes): produce ilusión de dominio que se evapora en 48h. *No funciona para nada que necesites retener más de 1 semana.*

### Con IA (NotebookLM Flashcards)
- NotebookLM tiene **Studio Artifact: Flashcards** que aplica spacing automático.
- Pídelo así: *"Genera 20 flashcards de [TEMA] con dificultad creciente. Front = pregunta, Back = respuesta + por qué."*
- Plantilla: `assets/plantilla-fichas-anki.csv`.

### Cuándo usar
- ✅ Vocabulario técnico (terminología, comandos, sintaxis).
- ✅ Hechos atómicos (fechas, fórmulas, nombres).
- ✅ Conceptos que necesitas recuperar bajo presión.
- ❌ NO usar para conceptos que requieren razonamiento complejo (ahí va Feynman).

### Calendario sugerido
Después de aprender un tema, agenda automáticamente las 6 revisiones en Google Calendar (15 min cada una). Plantilla ICS: `assets/calendar-invites/`.

---

## 3 · Feynman Technique (Técnica Feynman)

### Definición
**Explicar un concepto a alguien que no sabe del tema, usando lenguaje simple, sin jerga.** Donde uses jerga o te trabes, ahí están tus gaps de comprensión.

Atribuida a Richard Feynman (Nobel Física 1965), aunque él nunca la formalizó así. La formalización la popularizó James Gleick en *Genius* (1992) y la operacionalizó la comunidad de aprendizaje moderna.

### Por qué funciona `[DOC: Chi · Self-Explanations · 1989]`
- **Auto-explicación** activa el procesamiento profundo (deep processing).
- Detecta gaps que la fluidez de IA oculta.
- Te obliga a reorganizar el conocimiento desde principios primeros, no desde memorización.

### Protocolo (4 pasos clásicos)

```
PASO 1 · ELIGE EL CONCEPTO
   Toma una hoja. Escribe el nombre del concepto en el tope.
   Ejemplo: "Algoritmo de Consenso Raft"

PASO 2 · EXPLICA COMO SI FUERA NIÑO DE 12 AÑOS
   Sin jerga. Sin referencias a otros conceptos avanzados.
   Si necesitas decir "log replication", reemplaza con
   "una lista que se copia en muchas computadoras".
   Si necesitas analogías, úsalas.

PASO 3 · IDENTIFICA GAPS
   Donde te trabes, donde uses jerga, donde la explicación
   suene complicada → ahí está el gap.
   Marca cada uno con [?].

PASO 4 · CIERRA GAPS Y SIMPLIFICA
   Vuelve a la fuente original SOLO para los [?].
   Reescribe la explicación 100% desde principios primeros.
   Si todavía suena académica, simplifica más.
```

### Test final
**Si no la puedes contar a tu mamá / abuela / hijo en 3 minutos, no la sabes lo suficiente.**

### Anti-patrón
**Refugio en jerga**: usar términos técnicos para sentir que sabes. Si tu explicación tiene >5 palabras técnicas, no entiendes (estás reciclando memoria).

### Con IA
- **IA como audiencia**: *"Voy a explicarte [TEMA] como si fueras un niño de 12 años. Después tú me dices: ¿hay algo que no entendiste? ¿Usé palabras complicadas? ¿Falta una analogía?"*
- **IA como pareja**: *"Genera una explicación tipo Feynman de [TEMA] de 200 palabras. Yo voy a comparar con la mía y ver qué se me escapó."*
- Ver Prompt #2 (`prompts/02-coach-system-prompt.md`).

### Cuándo usar
- ✅ Cualquier concepto que vayas a defender públicamente.
- ✅ Antes de QBR / presentación / entrevista.
- ✅ Después de leer un paper denso.
- ✅ Como kata semanal (`katas/kata-feynman-novato.md`).
- ❌ NO usar para hechos memorizables (eso es Spaced Repetition).

### Kata asociado
`katas/kata-feynman-novato.md` · 30 min · audiencia: niño de 12 años.

---

## 4 · Interleaving (Intercalado)

### Definición
**Mezclar problemas o subtemas distintos en una misma sesión** en lugar de practicar un solo tipo bloqueado (blocked practice).

### Por qué funciona `[DOC: Rohrer & Pashler · 2010 · Psychological Science]`
- Bloqueado: 100% acertados durante práctica, pero olvidas en 1 semana.
- Intercalado: 60–70% acertados durante práctica (sientes que estás peor), pero retienes 80% a 1 semana.
- Te entrena a **identificar qué tipo de problema es**, no solo cómo resolver un tipo conocido.

### Protocolo

```
EN VEZ DE:
Sesión: 50 problemas de derivadas seguidas.
Resultado: dominas mecánica de derivadas, fallas en el examen mixto.

HAZ:
Sesión: 5 derivadas, 5 integrales, 5 límites, 5 series, repetir.
Resultado: peor durante práctica, mejor en examen y mundo real.
```

### Aplicado a aprendizaje técnico

| Bloqueado (mal) | Intercalado (bien) |
|---|---|
| 1 hora de leer sobre Kubernetes pods | 20 min Kubernetes, 20 min Helm, 20 min Service Mesh |
| 5 quiz seguidos sobre microservicios | Quiz mixto: microservicios + monolitos + serverless |
| Solo casos de éxito de empresa X | Casos de X · Y · Z · contradictorios |

### Anti-patrón
**Bloqueo**: estudiar un solo subtema durante toda la sesión "para dominarlo". Crea **fluencia local** sin **transferencia**.

### Con IA
- *"Hazme un quiz de 15 preguntas sobre [TEMA] que mezcle conceptos de subtemas distintos. No me digas qué subtema es cada pregunta."*
- *"Dame 5 casos de uso reales que combinen [SUBTEMA-A] y [SUBTEMA-B]."*

### Cuándo usar
- ✅ Práctica antes de examen o certificación con preguntas mixtas.
- ✅ Cuando ya manejas cada subtema en aislamiento.
- ❌ NO usar al inicio (primero domina cada subtema en bloqueo, después intercala).

---

## 5 · Elaboration (Elaboración)

### Definición
**Conectar lo que estás aprendiendo con lo que ya sabes**, preguntando *por qué*, *cómo*, *qué pasaría si*. Construir relaciones, no acumular hechos.

### Por qué funciona `[DOC: Pressley et al. · 1992 · Educational Psychology Review]`
- El cerebro recuerda redes, no listas.
- Cada conexión es un punto de acceso adicional al conocimiento.
- Más conexiones = más rutas para recuperar.

### Protocolo (las 4 preguntas elaborativas)

Después de aprender cualquier concepto, pregunta:

```
1 · ¿POR QUÉ es así?
    No "qué es" sino "por qué existe esta solución/concepto/regla".

2 · ¿CÓMO se relaciona con [X que ya sé]?
    Encuentra al menos 2 conexiones con conceptos previos.

3 · ¿QUÉ PASARÍA SI cambiara [variable clave]?
    Imagina escenarios contrafactuales. Esto revela el rango del concepto.

4 · ¿DÓNDE NO aplica?
    Los límites del concepto son tan importantes como el concepto.
```

### Ejemplo aplicado · concepto: "Eventual Consistency"

```
1 · ¿Por qué? Porque CAP theorem nos obliga a elegir entre Consistency
    y Availability cuando hay particiones de red.

2 · ¿Cómo se relaciona con [ACID que conozco]? Es el opuesto: ACID
    sacrifica disponibilidad por consistencia inmediata; Eventual
    sacrifica consistencia inmediata por disponibilidad.

3 · ¿Qué pasaría si la red nunca se particiona? CAP no aplica;
    podrías tener CA. Pero en práctica, las particiones SÍ ocurren.

4 · ¿Dónde NO aplica? En sistemas financieros donde necesitas
    consistencia inmediata (e.g., balance bancario antes de retirar).
```

### Anti-patrón
**Acumulación pasiva**: subrayar y "saber" sin conectar. El conocimiento sin red es inerte.

### Con IA
- *"Explica [CONCEPTO]. Luego conecta con 3 conceptos que probablemente ya conozco. Luego dime qué pasaría si [VARIABLE] cambiara. Luego dime dónde NO aplica."*

### Cuándo usar
- ✅ Después de cada concepto nuevo, antes de pasar al siguiente.
- ✅ En el ritual semanal de aprehensión.
- ❌ NO saltar este paso, aunque sientas que "ya entendiste".

---

## 6 · Dual Coding (Codificación dual)

### Definición
**Combinar texto con imagen / diagrama / audio.** El cerebro tiene canales separados para verbal y visual. Usar ambos = doble codificación = mejor retención.

### Por qué funciona `[DOC: Paivio · Mental Representations · 1986]`
- Modelo de codificación dual de Paivio (1971): información codificada en ambos canales tiene 2 rutas de recuperación.
- Estudios muestran +30% retención cuando combinas texto + diagrama vs solo texto `[DOC: Mayer · Multimedia Learning · 2001]`.
- Funciona especialmente bien para conceptos espaciales, procesos, jerarquías.

### Protocolo

```
PARA CADA CONCEPTO IMPORTANTE, GENERA 3 REPRESENTACIONES:

1 · TEXTO ESCRITO (definición + ejemplo)
2 · DIAGRAMA / MAPA CONCEPTUAL (mermaid, dibujo a mano, infografía)
3 · AUDIO (escucha podcast / explicación en voz alta / tu propia explicación grabada)

REVISAS ROTANDO ENTRE LOS 3 EN SESIONES DISTINTAS.
```

### Con IA (NotebookLM Studio)

NotebookLM produce 5 artefactos visuales/auditivos del mismo material:
1. **Audio Overview** (podcast 5–15 min)
2. **Video Overview** (explainer)
3. **Infografía**
4. **Mind Map** (jerarquía visual)
5. **Slide Deck** (presentación)

Plus textuales: Briefing Doc, Study Guide, Quiz, Flashcards, Data Table.

> **Recomendación**: para cualquier tema que vas a aprehender, genera **al menos 2** representaciones distintas en NotebookLM y consume las dos.

### Anti-patrón
- **Solo texto**: leer y releer libros sin diagramas → bajo retention.
- **Solo visual**: ver infografías sin leer la fuente → conocimiento superficial.

### Cuándo usar
- ✅ Conceptos espaciales (arquitecturas, redes, topologías).
- ✅ Procesos secuenciales (workflows, pipelines).
- ✅ Jerarquías (taxonomías, herencia, dependencias).
- ✅ Preparación para presentación (los slides + audio te entrenan a explicar).

---

## Combinación canónica del playbook

> *"Las 6 técnicas no se eligen una por una — se combinan en un loop semanal."* `[FUENTE-PRIMARIA: Playbook §Aprehender]`

### Loop semanal recomendado (1h, lunes a viernes)

```
LUNES   · 20 min Retrieval ciego del tema de la semana pasada
        + 40 min material nuevo + Elaboration

MARTES  · 60 min material nuevo + Dual Coding
        (genera diagrama o mapa conceptual)

MIÉRCOLES · 60 min Feynman: explica lo nuevo a un niño de 12 años
          (graba en audio, transcribe, identifica gaps)

JUEVES  · 60 min Interleaving: 4 quiz cortos mezclando subtemas
        + flashcards en NotebookLM

VIERNES · 60 min Retrieval + revisión de los gaps detectados
        + planificar Spaced Repetition de la próxima semana
```

Cadencia diaria de revisiones espaciadas: 5–15 min adicionales.

---

## Errores comunes al aplicar las 6 técnicas

| Error | Por qué falla | Corrección |
|---|---|---|
| Solo Retrieval, sin Spacing | Olvidas en 48h | Combina con intervalos crecientes |
| Solo Spacing, sin Retrieval | Reconoces, no recuperas | Cada revisión debe ser ciega |
| Feynman con jerga | Refugio en términos técnicos | Audiencia: niño de 12 años, sin excepciones |
| Interleaving prematuro | Confusión, no transferencia | Domina cada subtema primero, intercala después |
| Elaboration superficial | "Sí, se relaciona con X" sin profundizar | Mínimo 2 conexiones explicadas, no listadas |
| Dual Coding decorativo | Diagrama bonito sin contenido | Diagrama debe explicar, no decorar |

---

## Validación rápida (auto-test)

¿Estás aplicando bien las 6 técnicas? Marca:

- [ ] Has hecho **al menos 1 retrieval ciego** este mes
- [ ] Tienes **revisiones espaciadas agendadas** (no las dejas a la memoria)
- [ ] Has explicado **al menos 1 concepto a un no-experto** este mes
- [ ] Tu **última sesión de práctica** mezcló subtemas (no fue blocked)
- [ ] Para cada concepto nuevo, **conectaste con ≥2 conceptos previos**
- [ ] Tienes **al menos 2 representaciones** (texto + visual o audio) del tema activo

Si tienes <4 marcas → tu fase Aprehender es débil. Activa `coach-aprehender`.

---

> **Atribución**: Técnicas extraídas y operacionalizadas del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 §Aprehender.
> Sustento académico completo: `06-ciencia-cognitiva-fuentes.md`.
> *MetodologIA · CC BY-NC-SA 4.0*
