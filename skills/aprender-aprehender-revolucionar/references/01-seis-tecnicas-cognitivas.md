# 6 Técnicas Cognitivas · Manual operativo

> Las 6 técnicas con mayor evidencia académica para retención duradera, transferencia y dominio. Núcleo de la fase **Aprehender**. v1.1.0.

`[FUENTE-PRIMARIA]` Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 §Aprehender · sustento académico en `06-ciencia-cognitiva-fuentes.md`.

## Mapa rápido

| # | Técnica | Fase | Evidencia | Tiempo | Combina mal con |
|---|---|---|---|---|---|
| 1 | Retrieval Practice | Aprehender | ⭐⭐⭐⭐⭐ Karpicke 2008 | 20–30 min | Sin Spacing → olvido en 48h |
| 2 | Spaced Repetition | Aprehender | ⭐⭐⭐⭐⭐ Cepeda 2008 | 5–15 min/día | Sin Retrieval → recognition, no recall |
| 3 | Feynman | Cross-fase | ⭐⭐⭐⭐⭐ Chi 1989 | 30 min | Audiencia experta neutraliza el reto |
| 4 | Interleaving | Aprehender | ⭐⭐⭐⭐ Rohrer 2010 | 30–45 min | Aplicado prematuramente confunde |
| 5 | Elaboration | Aprender + Aprehender | ⭐⭐⭐⭐ Pressley 1992 | 15 min | Acumulación pasiva sin red de relaciones |
| 6 | Dual Coding | Cross-fase | ⭐⭐⭐⭐ Mayer 2014 | varía | Visual decorativo sin contenido |

> ⭐⭐⭐⭐⭐ = "high utility" en meta-análisis Dunlosky 2013 `[DOC]`. Las 4 estrellas son "moderate utility" con evidencia robusta pero menos consistente entre dominios.

`[NUEVO-APORTE]` Las 6 técnicas **no son aditivas**. Apilar las 6 en una sesión de 1 h satura cognitive load y produce diminishing returns `[DOC: Sweller 1988]`. Distribuir en la semana (§7) supera siempre a "hacerlas todas hoy".

---

## 1 · Retrieval Practice

**Definición**: recuperar de memoria sin pistas externas (notas, libros, slides, IA, web).

**Por qué funciona** `[DOC: Karpicke & Roediger 2008 · Science]`: releer da fluidez ilusoria; recuperar genera *desirable difficulty* que codifica profundo. Estudios muestran +50–80% retención a 1 semana vs releer.

### Protocolo · sesión 20–30 min

1. Cerrar TODO (notas · libros · slides · IA · web)
2. Hoja en blanco
3. Escribir TODO lo que recuerdes sobre [tema] · sin parar
4. Marcar `[?]` donde dudes · NO consultar
5. Abrir fuentes · comparar · marcar cada elemento `[FUERTE/PARCIAL/DÉBIL]`
6. Estudiar SOLO `[DÉBIL]` y `[PARCIAL]`
7. Re-sesión en 3 días (Spaced)

**Anti-patrón** · Recognition vs Recall: ver listado y decir "lo conozco". Reconocer ≠ recuperar. La prueba real es papel en blanco.

`[CASO-BORDE]` Si en hoja blanca escribes >70% pero falla mock interview: el retrieval cubre vocabulario, no estructura argumental. Combinar con Feynman.

**Con IA**: pídele al notebook *"Hazme 5 preguntas abiertas sin respuestas. Yo respondo y tú evalúas con [FUERTE/PARCIAL/DÉBIL]."*

**Cuándo usar** ✅ ritual semanal · pre-presentación · cierre diario.
**Cuándo NO** ❌ en lugar del estudio inicial (necesitas haber estudiado primero).

→ `katas/kata-recuperacion-ciega.md` · `scripts/retrieval_session.py`

---

## 2 · Spaced Repetition

**Definición**: revisar en intervalos crecientes, no consecutivos.

**Por qué funciona** `[DOC: Cepeda et al. 2008]`: la curva del olvido `[DOC: Ebbinghaus 1885]` es exponencial (50% en 1h · 70% en 24h · 90% en 1 sem). Revisar justo antes del olvido aplana la curva. 5 revisiones espaciadas > 50 consecutivas en retención a 6 meses.

### Intervalos canónicos

| Día | Acción |
|---|---|
| 0 | Aprendizaje inicial |
| 0 (PM) | 1ª revisión (final del día) |
| 3 | 2ª revisión |
| 7 | 3ª revisión |
| 14 | 4ª revisión |
| 30 | 5ª revisión |
| 90 | 6ª revisión (consolida ≥6 meses) |

**Regla de ajuste**: si fallas → vuelve al intervalo anterior; si aciertas → avanza al siguiente.

**Anti-patrón** · Cramming: maratón intensivo el día antes. Produce dominio temporal que se evapora en 48–72h. Inútil para horizontes >1 semana.

`[CASO-BORDE]` Si saltaste un intervalo (ej. olvidaste día 7), reanudar en el intervalo más cercano que NO superaste, no "donde ibas". Forzar al intervalo siguiente sin haberlo ganado deja deuda invisible.

**Con IA**: NotebookLM Studio Flashcards aplica spacing automático. Plantilla: `assets/plantilla-fichas-anki.csv`.

**Cuándo usar** ✅ vocabulario técnico · hechos atómicos · datos para presión.
**Cuándo NO** ❌ razonamiento complejo (ahí Feynman + Elaboration).

→ ICS pre-llenados en `assets/calendar-invites/`

---

## 3 · Feynman Technique

**Definición**: explicar un concepto a alguien sin contexto (objetivo: niño de 12 años) sin jerga. Donde te trabes está el gap.

**Atribución correcta** `[DOC: Gleick · Genius · 1992]` y `[DOC: Oakley · A Mind for Numbers · 2014]`: Feynman nunca formalizó la técnica; Gleick y Oakley la operacionalizaron como protocolo de 4 pasos.

**Por qué funciona** `[DOC: Chi · Self-Explanations · 1989]`: la auto-explicación activa procesamiento profundo, expone gaps que la fluidez de IA oculta, y obliga a reorganizar conocimiento desde principios primeros.

### Protocolo · 4 pasos

| Paso | Acción |
|---|---|
| 1 | Concepto en hoja en blanco · 1 línea ("Algoritmo Raft") |
| 2 | Explicar como si la audiencia tuviera 12 años · sin jerga · usar analogías |
| 3 | Marcar con `[?]` cada lugar donde te trabaste o usaste jerga · gap detectado |
| 4 | Volver a la fuente SOLO para los `[?]` · re-escribir desde principios primeros |

**Test final**: si no la cuentas a tu mamá/abuela/hijo en 3 min, no la sabes lo suficiente.

**Anti-patrón** · Refugio en jerga: usar términos técnicos para sentirte que sabes. >5 palabras técnicas en 60 segundos = no entiendes, estás reciclando memoria.

`[CASO-BORDE]` Audiencia experta neutraliza el reto: si "explico a un colega senior" usás abreviaturas que la abuela no entendería pero el colega sí. La audiencia DEBE ser no-experta para que la jerga produzca fricción detectable.

**Con IA**:
- Como audiencia: *"Te explico [TEMA] como si fueras niño de 12. Después dime: ¿qué no entendiste? ¿usé palabras complicadas? ¿falta analogía?"*
- Como pareja: *"Genera un Feynman de [TEMA] · 200 palabras. Comparo con el mío y veo qué se me escapó."*

**Cuándo usar** ✅ pre-defensa pública · post-paper denso · kata semanal.
**Cuándo NO** ❌ hechos memorizables (ahí Spaced).

→ `katas/kata-feynman-novato.md`

---

## 4 · Interleaving

**Definición**: mezclar problemas/subtemas distintos en una sesión, no practicar uno bloqueado.

**Por qué funciona** `[DOC: Rohrer & Pashler 2010]`: práctica bloqueada da 100% durante sesión y olvido en 1 sem; intercalada da 60–70% durante (te sientes peor) y 80% retención a 1 sem. Entrena identificar tipo de problema, no solo resolver tipo conocido.

### Aplicación

| Bloqueado (mal) | Intercalado (bien) |
|---|---|
| 1 h Kubernetes pods | 20 min Kubernetes + 20 min Helm + 20 min Service Mesh |
| 5 quiz seguidos microservicios | Quiz mixto: micro + monolito + serverless |
| Solo casos éxito empresa X | Casos X + Y + Z + contradictorios |

**Anti-patrón** · Bloqueo: "voy a dominar este subtema antes del próximo". Produce *fluencia local* sin transferencia.

`[CASO-BORDE]` Interleaving prematuro confunde si los subtemas no están dominados aislados. Regla: bloqueo hasta Escala 1 por subtema, intercalado de Escala 2 en adelante.

**Con IA**: *"Quiz 15 preguntas mixtas sobre [tema] · no me digas qué subtema es cada una."*

→ `prompts/08-evaluator-certification.md` aplica interleaving en quizes Nivel 2-4

---

## 5 · Elaboration

**Definición**: conectar lo nuevo con lo conocido vía 4 preguntas elaborativas.

**Por qué funciona** `[DOC: Pressley et al. 1992]`: el cerebro recuerda redes, no listas. Cada conexión = punto de acceso adicional. Más conexiones = más rutas para recuperar.

### Las 4 preguntas

```
1 · ¿POR QUÉ es así? (no "qué es" · "por qué existe")
2 · ¿CÓMO se relaciona con [X que ya sé]? (mín 2 conexiones)
3 · ¿QUÉ PASARÍA SI cambiara [variable clave]? (contrafactuales)
4 · ¿DÓNDE NO aplica? (límites del concepto)
```

### Ejemplo · Eventual Consistency

1. **Por qué**: CAP Theorem fuerza elegir entre Consistency y Availability bajo particiones.
2. **Cómo se relaciona con ACID**: opuesto · ACID sacrifica disponibilidad por consistencia inmediata.
3. **Si red nunca se particiona**: CAP no aplica · podrías tener CA. En práctica, particiones SÍ ocurren.
4. **NO aplica**: sistemas financieros (balance bancario antes de retirar requiere consistencia inmediata).

**Anti-patrón** · Acumulación pasiva: subrayar y "saber" sin conectar. Conocimiento sin red es inerte.

`[CASO-BORDE]` Si las 2 conexiones son superficiales ("se relaciona con X" sin explicar cómo), Elaboration está siendo reciclado como Recognition. Cada conexión debe sostener una explicación de 30+ palabras.

**Con IA**: *"Explica [CONCEPTO]. Conecta con 3 conceptos que probablemente conozco. Qué pasaría si [VARIABLE] cambiara. Dónde NO aplica."*

---

## 6 · Dual Coding

**Definición**: combinar texto + visual + audio del mismo material.

**Por qué funciona** `[DOC: Paivio 1971]` `[DOC: Mayer · Multimedia Learning · 2014]`: el cerebro tiene canales separados verbal y visual. Codificar en ambos = 2 rutas de recuperación. +30% retención vs solo texto cuando se siguen los principios de Multimedia Learning (proximidad espacial, modalidad complementaria).

### Protocolo

Para cada concepto importante, generar **3 representaciones**:
1. Texto escrito (definición + ejemplo)
2. Diagrama / mapa conceptual (mermaid · dibujo · infografía)
3. Audio (podcast del notebook · explicación grabada propia)

Rotar entre las 3 en sesiones distintas (no las 3 a la vez).

### NotebookLM Studio · 5 artefactos visuales/auditivos

| Artefacto | Uso |
|---|---|
| Audio Overview | Podcast 5–15 min para escuchar caminando |
| Video Overview | Explainer · útil para conceptos espaciales |
| Infografía | Resumen visual de jerarquías |
| Mind Map | Estructura del campo · navegable |
| Slide Deck | Práctica de presentación |

Plus textuales: Briefing Doc · Study Guide · Quiz · Flashcards · Data Table.

**Recomendación**: para cualquier tema a aprehender, generar **mín 2** representaciones distintas (1 texto + 1 visual o audio).

**Anti-patrón** · Visual decorativo: diagrama bonito sin contenido informativo. Test: ¿el diagrama explica algo que el texto no? Si no, decoración.

`[CASO-BORDE]` Conceptos puramente abstractos (lógica modal, teoría de la medida) resisten Dual Coding visual. En esos, el "visual" puede ser estructura sintáctica (árbol de fórmulas) en lugar de diagrama espacial.

---

## Combinación canónica · loop semanal (1 h × 5 días)

```
LUNES   · 20 min Retrieval ciego (tema sem pasada) + 40 min material nuevo + Elaboration
MARTES  · 60 min material nuevo + Dual Coding (diagrama o mapa)
MIÉRC.  · 60 min Feynman: explicar a niño 12 años · audio · gaps
JUEVES  · 60 min Interleaving: 4 quiz mixtos + flashcards NotebookLM
VIERNES · 60 min Retrieval + cierre de gaps + planificar Spaced sem siguiente
```

Cadencia diaria adicional: 5–15 min spacing por flashcard.

`[FUENTE-PRIMARIA]` Playbook §Aprehender · "Las 6 técnicas no se eligen una por una — se combinan en un loop semanal."

---

## Errores comunes (matriz)

| Error | Falla | Corrección |
|---|---|---|
| Solo Retrieval, sin Spacing | Olvido en 48 h | Combinar con intervalos crecientes |
| Solo Spacing, sin Retrieval | Recognition, no recall | Cada revisión debe ser ciega |
| Feynman con jerga | Refugio en términos | Audiencia: niño de 12 años, sin excepción |
| Interleaving prematuro | Confusión, no transferencia | Bloqueado hasta Escala 1, intercalar después |
| Elaboration superficial | Conexiones sin profundidad | Mín 2 conexiones explicadas, no listadas |
| Dual Coding decorativo | Diagrama bonito sin info | Test: explica algo que texto no |
| 6 técnicas en 1 h | Cognitive overload | Distribuir en la semana |

---

## Validación rápida (auto-test mensual)

- [ ] ≥1 retrieval ciego este mes
- [ ] Revisiones espaciadas agendadas en calendario (no en memoria)
- [ ] ≥1 Feynman a no-experto este mes
- [ ] Última sesión de práctica fue mixta (no bloqueada)
- [ ] Cada concepto nuevo conectado con ≥2 previos
- [ ] ≥2 representaciones (texto + visual o audio) del tema activo

`[CRITERIO-ACEPTACIÓN]` <4/6 marcas → fase Aprehender débil · activar `coach-aprehender`.

---

## Referencias cruzadas

- Sustento académico: `references/06-ciencia-cognitiva-fuentes.md`
- Anti-patrones extendidos: `references/04-anti-patrones-y-trampas.md` §Espejismo Fluidez · §Cramming · §Recognition
- Coach que aplica las 6: `agents/coach-aprehender.md`
- Katas: `katas/kata-recuperacion-ciega.md` · `katas/kata-feynman-novato.md`
- Prompts: `prompts/02-coach-system-prompt.md` · `prompts/08-evaluator-certification.md`

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA
