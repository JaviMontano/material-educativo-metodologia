# Version Vault — Masterclass S2 · Del Automatismo a estar En Presencia

**ID:** `MC-S2`
**Patrón de versionado:** basado en MetodologIA Version Vault v2.0 · Brand Voice v3.0 §Entregable 2
**Archivo principal:** `SPEC-Masterclass-S2-AutomatismoPresencia-v2.0.md`
**Este archivo:** registro de cambios, decisiones, trade-offs, reglas de publicación

---

## 1 · Convención de nombres
- **ID del asset:** `MC-S2`
- **Versión:** `vMAJOR.MINOR.PATCH` (ej.: `v2.0.0`)
- **Spec:** `SPEC-Masterclass-S2-AutomatismoPresencia-v{VERSION}.md`
- **Vault:** `VAULT-Masterclass-S2-AutomatismoPresencia.md` (único, acumulativo)
- **Descartados:** `ARCHIVED-{originalName}.md`

## 2 · Reglas de versionado
- **PATCH** (vX.Y.Z+1): correcciones de texto, claridad, consistencia. No cambia estructura, número de slides, ni contratos brand.
- **MINOR** (vX.Y+1.0): agrega capacidades compatibles (slides adicionales, plantillas nuevas, actividades opcionales, rúbricas).
- **MAJOR** (vX+1.0.0): rompe compatibilidad (cambia tesis, elimina slides canónicas, cambia brand, redefine estructura Minto).

## 3 · Registro de versiones

### v3.0.1 · 2026-04-18 · vigente canónica (PATCH transversal sobre v3.0)
**Motivo:** corrección transversal de coherencia interna en la SPEC v3.0 para eliminar inconsistencias que filtrarían jerga o cifras imposibles al render.

**Correcciones transversales aplicadas**

| # | Dónde | Problema detectado en v3.0 | Corrección v3.0.1 |
|---|---|---|---|
| 1 | Slide 6 | Ejemplos usaban nombres de los arquetipos (Verónica, Daniel, Mateo) mezclados con los 3 momentos, colisionando con slides 10/11/12 que son los casos definitivos de cada uno | Slide 6 pasa a ejemplos genéricos (sin nombres); cada arquetipo conserva UNA escena definitoria en su slide profundo |
| 2 | Slide 8 | Título "Cómo funciona el método" usa "método" como término abstracto genérico | Cambiado a "Cómo se conecta todo" |
| 3 | Slide 9 | Regla decía "pasar del 1 al 3" usando numeración, contradiciendo la regla dura de nombres humanos | Cambiado a "pasar de Piloto útil a Atención plena" |
| 4 | Slide 11 | Cifra "70% de 3 decisiones salieron mejor" = 2.1 decisiones (imposible); base demasiado pequeña para porcentaje | Reformulado: "Verónica tomó 12 decisiones irreversibles con el ritual en 4 semanas; 8 salieron mejor, 4 iguales, ninguna peor" |
| 5 | Slide 12 | "Calidad (reporte en 1-10)" confuso sobre quién reporta | Precisado: "cada día anotó 3 números del 1 al 10: su cabeza al despertar, la calidad de sus decisiones, el cansancio acumulado" |
| 6 | Slide 14 | "Bucle de Excelencia" como concepto visible | Baja a nota al pie Trebuchet 10pt; front usa "las 10 preguntas" |
| 7 | Slide 15 | Título "El Plan de Activación" suena corporativo | Cambiado a "Cómo sigues esta semana: tres horas en tres encuentros" |
| 8 | Slide 15 | "Workshop" es anglicismo | Cambiado a "Taller" consistente con regla de español latino neutro |
| 9 | Slide 15 | Etiqueta "Experiencia No Cost / No Risk" mezcla inglés | Cambiado a "Gratis · Sin riesgo" |
| 10 | Apéndice A | Criterio "puede explicar el método" era abstracto | Precisado: "puede explicar la idea central a su pareja o amigo no técnico en menos de 2 minutos, sin usar las palabras de la lista prohibida" |
| 11 | Apéndice A criterio 5 | Confusión entre nombre comercial y discurso del asistente | Clarificado: las palabras prohibidas pueden aparecer como nombres comerciales en materiales, pero no en el discurso del asistente al explicar el método con sus propias palabras |
| 12 | Reglas duras | Faltaba prohibir "plan de activación" y "bucle de excelencia" como titulares visibles | Añadidos a la lista de palabras vacías de cliente |
| 13 | Reglas duras | Faltaba regla explícita sobre consistencia de arquetipos | Añadida: "los 3 arquetipos tienen una única escena cada uno; no colisionan entre slides" |
| 14 | Reglas duras | Faltaba regla sobre cifras pequeñas | Añadida: "cifras con ancla a personaje específico; sin porcentajes aplicados a bases pequeñas que generen cifras imposibles" |
| 15 | Mapa de conceptos (Apéndice F) | Mencionaba "Soberanía Cognitiva" como nodo del mapa | Reemplazado por "Ser dueño de tu día" (consistente con el front) |
| 16 | Prompts NotebookLM | Faltaban reglas explícitas contra cifras imposibles y contra anglicismos | Reescritos con 16 reglas duras numeradas |

**Sin cambios en**
- Paleta, tipografía, logo, header/footer, brand voice v3.0, 3 niveles Feynman, analogía del coche, 5 hábitos, 10 preguntas, 3 arquetipos (siguen siendo Daniel/Verónica/Mateo).

**Decisiones y trade-offs del patch**

| Decisión | Trade-off | Por qué |
|---|---|---|
| PATCH en vez de MINOR | Conserva número v3.0.x | Cambios no rompen compatibilidad narrativa; solo limpian coherencia interna |
| Nueva source en NotebookLM | Duplica archivo cargado | La source previa (v3.0) ya está asociada a artefactos en curso; mantenerla permite A/B entre v3.0 y v3.0.1 |
| Apéndice E crece con tabla explícita de trade-offs del patch | Spec más larga | Trazabilidad de cada corrección queda documentada |

**Notas de compatibilidad**
- La SPEC v3.0 original queda como snapshot histórico inmediatamente anterior; artefactos generados con ella (Deck E `71829d4a`, Video D `132da2f1`) se mantienen en el notebook para comparación.
- v3.0.1 es la versión canónica para nuevas generaciones.

---

### v3.0.0 · 2026-04-18 · snapshot inmediatamente previo (corregido transversalmente en v3.0.1)
**Motivo:** El cliente real no conecta con la jerga interna ("portafolio atencional", "dual operativo", "orquestar"). Reescritura radical en lenguaje cotidiano usando técnica Feynman, con analogías memorables, hábitos adoptables concretos, supuestos declarados, límites honestos, casos borde respondidos y criterios de aceptación medibles.

**MAJOR (rompe compatibilidad narrativa)**
- Tesis expresada en 3 niveles (niño 12 años · colega · experto) en vez de uno solo técnico.
- Ecuación matemática retirada del front-end; baja a nota al pie para nivel experto.
- Jerga interna prohibida en el deck visible al cliente.
- "Modos A/B/C/D" renombrados a "Piloto útil · Piloto con un ojo abierto · Atención plena · Presencia sin meta".
- "Soberanía Cognitiva" reemplazada en titulares por "Ser dueño de tu día".
- Ilustración central cambia de fórmula a analogía del coche (caja automática vs manual).

**Añadido**
- 3 arquetipos humanizados con nombres propios: Daniel, Verónica, Mateo.
- Slide 5 sobre constante biológica 4 horas de calidad real.
- Slide 13 con 5 hábitos concretos (regla "elige UNO solo").
- Slide 14 con rúbrica traducida a 10 preguntas directas.
- Apéndice A · criterios de aceptación medibles (80% nombra los 3 momentos, 80% elige 1 hábito, 0% usa jerga interna).
- Apéndice B · supuestos declarados (≥30h/sem cognitivas, autonomía parcial, voluntad de cambio).
- Apéndice C · límites honestos (no reemplaza terapia, cifras self-reported, requiere 2-4 semanas).
- Apéndice D · 5 casos borde respondidos (100% creativo, 100% operativo, ya agotado, jefe impone plantilla, ya hizo mindfulness).
- Apéndice E · tabla de decisiones y trade-offs justificados.
- Apéndice F · mapa de conceptos conectados (Feynman, Newport, Clear, Kahneman, Ericsson).

**Cambiado**
- Estructura de 15 slides (v2.4) a 16 slides (v3.0): +1 slide para los 5 hábitos concretos.
- El título técnico original de la masterclass se conserva; pero el contenido se traduce a lenguaje humano.
- Cifras de los casos se mantienen pero se anclan a nombres propios para ganar memoria.

**Eliminado**
- Referencias al "Portafolio Atencional" como concepto visible al cliente.
- Uso explícito de "Dual Operativo" y "(R)Evolución Dual" en slides visibles.
- Ecuación matemática como visual central de slide.
- Letras A/B/C/D en front del modo operativo.

**Corregido**
- Lenguaje: pasa de técnico-interno a neutral-cotidiano sin perder precisión.
- Trazabilidad: cada cifra queda anclada a un arquetipo específico (Daniel 2h, Verónica 40, Mateo 40%).
- Feynman: cada concepto se presenta en 3 niveles progresivos de profundidad.

**Decisiones y trade-offs principales**

| Decisión | Trade-off aceptado | Por qué |
|---|---|---|
| Retirar jerga del front-end | Pierde densidad técnica en slide | Cliente real no conecta con "portafolio atencional"; mantener como término interno para niveles 3 y equipo |
| Cambiar ecuación por analogía del coche | Pierde elegancia técnica | Analogía concreta genera recuerdo; ecuación técnica se queda en pie de nivel experto |
| Nombres propios Daniel/Verónica/Mateo | Carga regional ligera | Neutral en LatAm; personas se identifican con humanos, no con roles abstractos |
| 5 hábitos con regla "elige UNO" | Parece poco ambicioso | Elegir 5 casi garantiza abandono en semana 2; elegir 1 casi garantiza instalación sostenida |
| 10 preguntas humanas antes de rúbrica técnica | Menos "Bucle de Excelencia puro" | La rúbrica técnica asusta al cliente no técnico; las 10 preguntas son puerta de entrada |
| Apéndices A-F visibles al facilitador, no al cliente | Spec más larga | El deck queda limpio (16 slides); el manual queda completo (6 apéndices) |

**Artefactos nuevos en notebook `faf4416f`**
- Deck E · 16 slides v3.0 Versión Humana · `71829d4a-d816-45d7-b6c0-ae8984ec1a83` · 🔄 generando
- Video D · explainer Feynman + analogía coche + 3 casos humanos · `132da2f1-8349-4418-9b95-4c44c3e9db7b` · 🔄 generando

**Notas de compatibilidad**
- **Se mantiene igual:** paleta, tipografía, logo, header/footer, brand voice v3.0, rúbrica de 10 criterios (traducida a preguntas humanas), Ciclo 1-1-1.
- **Se refuerza:** reglas duras de idioma (sin voseo, sin modismos) y reglas duras de anti-jerga (sin portafolio/dual/orquestar).
- **Canonización:** v3.0 es ahora la versión canónica para la masterclass pública. v2.1, v2.2, v2.3, v2.4 quedan como variantes para A/B testing interno.

---

### v2.4.0 · 2026-04-18 · reemplazada por v3.0 como canónica (Deck D · 15 slides · estudio de caso · sin voseo)
**Motivo:** Alternativa narrativa adicional para A/B/C/D testing. Usa 3 arquetipos profesionales (El Consultor Senior · La Líder de Producto · El Fundador de Startup) como estudios de caso que atraviesan el deck. Refuerzo explícito de español latino neutro SIN voseo y SIN modismos regionales.

**Añadido**
- Archivo `SPEC-Masterclass-S2-AutomatismoPresencia-v2.4.md` · 15 slides con formato de casos.
- Sección "⚠️ Reglas duras de idioma" con 7 reglas explícitas: prohibición de voseo (vos, sos, tenés, querés, andá, decime, mirá, etc.) y modismos regionales (che, dale, boludo, güey, parce, chavo, tío, posta, etc.).
- 3 slides nuevas con casos aplicados (slides 6, 8, 11).
- Deck D artifact · `a4cf37f9-d55d-4dcc-8011-5a6a08acba92` · 🔄 generando.
- Video C artifact · `98e487cd-ba63-4659-a8d7-73a4841de25c` · 🔄 generando.

**Cambiado**
- Conteo de slides: 15 (vs 11 de C2, 13 de A, 22 de B).
- Estructura narrativa: lineal → entrelazada con 3 recorridos de caso.
- Cada concepto teórico se presenta acompañado por su aplicación concreta en un arquetipo.

**Eliminado**
- Nada. Adición compatible, A/B/C/D testing opera con todos los decks en paralelo.

**Corregido**
- Refuerzo preventivo: si en renders anteriores apareció voseo no detectado (NotebookLM ocasionalmente mezcla registros), esta versión bloquea explícitamente con reglas duras y lista de verbos esperados.

**Decisiones y trade-offs**

| Decisión | Trade-off | Justificación |
|---|---|---|
| 3 arquetipos con rol, no con nombre propio | Pierde calidez de nombres | Nombres propios (María, Luis, Ana) cargan connotación regional; el rol ("El Consultor Senior") es neutro para toda LatAm |
| 15 slides en lugar de 11 o 13 | Mayor duración de masterclass | Los casos requieren espacio narrativo; comprimir los dejaría sin poder explicativo |
| Cifras específicas en cada caso (2h, 40, 35%, 4h) | Más difícil de defender si alguien cuestiona | Las cifras van ancladas a un personaje ficticio, no son afirmaciones generales; el riesgo de inventiva queda contenido en el marco de "caso ilustrativo" |
| Reglas duras de idioma visibles al inicio | Alarga la spec | La instrucción al modelo es más efectiva cuando las reglas están al tope y repetidas en el prompt |
| Video C narrativa de 3 arquetipos | Video más largo (exige duración extendida) | Complementa Video A (dolor cotidiano) y Video B (deseo de calidad) sin repetir enfoque |

**Notas de compatibilidad**
- **Se mantiene igual:** paleta, tipografía, logo, Brand Voice v3.0 gates, rúbrica Bucle de Excelencia, lista roja.
- **Refuerzo nuevo:** reglas duras anti-voseo y anti-modismos disponibles para futuras versiones.

---

### v2.3.0 · 2026-04-18 · vigente (Deck C2 · reparación post-auditoría render)
**Motivo:** Auditoría del render del Deck C (título autogenerado "Soberanía Cognitiva") detectó 3 fallos críticos y 2 menores. Además, Video B falló silenciosamente en generación. Esta versión repara con reglas duras anti-ambigüedad.

**Fallos corregidos en v2.3**

| Fallo | Severidad | Origen | Solución v2.3 |
|---|---|---|---|
| Slide 2 · "Presencia Performativa" duplicada (4 tarjetas en lugar de 3) | 🔴 crítico | NotebookLM rellenó una 4ª tarjeta | Regla dura: "EXACTAMENTE 3 tarjetas con contenido distinto; NO duplicar" + iconos sugeridos explícitos |
| Slide 2 · cifra "120 minutos" inventada sin evidencia | 🟡 brand | NotebookLM llenó con dato propio | Regla dura: "NO inventes cifras. Si la spec no tiene número, no lo uses" + pie literal sin número |
| Slide 4 · ecuación inconsistente (subtítulo "Soberanía" vs diagrama "Maestría") | 🟡 coherencia | Spec v2.2 presentaba ambas formulaciones | UNA SOLA ecuación: `Piloto + Atención + Método = Soberanía Cognitiva`. Prohibido introducir "Maestría" o "Empoderamiento" |
| Slide 4 · Método no visible como multiplicador en diagrama | 🟡 completitud | Spec v2.2 no lo especificó | Diagrama literal con signo `×` antes de Método |
| Slide 9 · rúbrica con celdas vacías (líneas en blanco) | 🔴 crítico | NotebookLM interpretó tabla como formulario | Tabla 10×3 (#, Criterio, Test) con TODAS las celdas llenas con texto literal |

**Añadido**
- Sección superior "⚠️ Instrucciones críticas para NotebookLM" con 6 reglas duras anti-ambigüedad.
- Iconos sugeridos explícitos en slide 2 para forzar diferenciación visual.
- Prompt de generación reforzado con 11 reglas numeradas explícitas.
- Relanzamiento de ambos videos (A y B) con video_style_prompts consolidados.

**Artefactos nuevos en notebook `faf4416f`**
- Deck C2 · 11 slides v2.3 · `4c68efac-cbd3-440a-b6be-674826fbfa92` · 🔄 generando
- Video A2 · explainer dolor cotidiano · `839fcc36-26d1-423b-ab31-be6a11dcef2f` · 🔄 generando
- Video B2 · explainer deseo de calidad · `1ce757dc-a60c-4a50-814d-f88c60decab1` · 🔄 generando

**Decisiones y trade-offs**

| Decisión | Trade-off | Justificación |
|---|---|---|
| Regenerar Deck C en vez de reeditar PDF | Pierde el render ya producido | Reeditar PDF requiere diseñador; regenerar aprovecha el pipeline y cuesta ~5 min |
| Relanzar Video A aunque estaba "completed" | Duplica artefacto | Usuario reporta que no carga → URL puede haber expirado en su sesión; nueva URL resuelve |
| Relanzar Video B desde cero | Consume tiempo de generación | No apareció en el listado de artefactos: falló silenciosamente en generación previa |
| No modificar Deck A (v2.1) ni Deck B (v2.0) | A/B/C testing sigue siendo comparable | Solo Deck C tenía fallos; los demás siguen válidos |

**Notas de compatibilidad**
- **Se mantiene igual:** estructura de 11 slides homóloga S1, paleta, tipografía, logo, brand voice v3.0, lista roja = 0.
- **Se refuerza:** instrucciones anti-ambigüedad explícitas por slide.
- **Limitación estructural aceptada:** watermark "NotebookLM" en footer-der (plan free/pro sin enterprise no permite reemplazar logo).

---

### v2.2.0 · 2026-04-18 · reemplazada por v2.3.0 (Deck C original con fallos de render)
**Motivo:** Producir variante de 11 slides homóloga al molde canónico de la masterclass S1 "De Ocupado a Productivo", aplicada al tema Automatismo y Presencia. Objetivo: 3 decks comparables (A=13, B=22, C=11) para A/B/C testing en `faf4416f`. Además, generar un segundo video (Video B) con ángulo narrativo distinto al Video A, también para testing.

**Añadido**
- Archivo `SPEC-Masterclass-S2-AutomatismoPresencia-v2.2.md` con las 11 slides del Deck C, mapeadas 1:1 con la S1 canónica.
- Artefacto Deck C en notebook `faf4416f` · `2eba0492-7c1f-481a-b376-b6c53b396e4a`.
- Artefacto Video B en notebook `faf4416f` · `7d6eb79c-37ba-4bd1-a046-ce02af2e3337`.
- Video B con ángulo de entrada distinto a Video A: dolor → deseo de calidad y frustración de la auto-crítica vaga.

**Cambiado**
- Pirámide canónica de S1 slide 6 (Architect/Engineer/Mason) reemplazada por **Diseñador/Ingeniero/Ejecutor** en Deck C para compliance con lista roja Brand Voice v3.0.
- Título de slide 6 "De Operador a Arquitecto" reformulado como **"De Ejecutor a Diseñador"**.
- "Las 3 Capas de una Buena Instrucción" de S1 slide 6 reemplazadas por **"Las 3 Señales que exigen Presencia"** (decisión irreversible, vínculo de confianza, creatividad original) — más fit con el tema de S2.
- "Comité Operativo Artificial" de S1 slide 9 reformulado como **"Orquestador Dual"** (Director / Diseñador del Piloto / Guardián de Atención / Árbitro con Rúbrica) e integrada la rúbrica de 10 criterios del Bucle de Excelencia.
- Cifras canónicas de S1 (40% calidad + 30% productividad) reemplazadas por **10–15h + 30% menos fatiga** en Deck C, con nota metodológica honesta.

**Eliminado**
- Nada. Este changelog es adición compatible (MINOR). Deck A (v2.1) y Deck B (v2.0 archived) continúan vigentes y corriendo.

**Corregido**
- Cero apariciones de `arquitecto/arquitectura` en Deck C a pesar de homologar una slide que en S1 sí usaba el término.

**Decisiones y trade-offs**

| Decisión | Trade-off asumido | Justificación |
|---|---|---|
| Crear Deck C además de A y B (no reemplazar) | 3 decks en paralelo en un mismo notebook · carga visual | A/B/C testing requiere 3 variantes comparables; el usuario elegirá cuál canoniza tras medir conversión/retención |
| Sustituir "Arquitecto" por "Diseñador" en la pirámide homóloga | Pierde la aliteración del original S1 | Regla G4 Brand Voice v3.0: lista roja = 0 tolerancia. "Diseñador" conserva la función (top of pyramid = humano con juicio) sin romper brand |
| Sustituir "3 Capas de Instrucción" por "3 Señales que exigen Presencia" | Homología textual imperfecta | Las 3 capas eran específicas del tema S1 (prompting); las 3 señales son específicas del tema S2 (presencia). Mantener las capas habría forzado contenido fuera de tesis |
| Integrar rúbrica Bucle de Excelencia dentro del slide 9 "Comité → Orquestador" en vez de slide aparte | Densidad alta en slide 9 | Preserva conteo de 11 slides fiel al molde S1. Alternativa (slide dedicada) rompe homología |
| Video B con ángulo "deseo de calidad" vs Video A "dolor automatismo heredado" | Dos videos requieren más tiempo de procesamiento | Cobertura narrativa completa: pesimismo (dolor) + optimismo (deseo). Ambos cierran con el mismo CTA para medir cuál puerta de entrada convierte mejor |

**Notas de compatibilidad**
- **Se mantiene igual:** paleta, tipografía, logo, estética Neo-Swiss, header/footer, Brand Voice v3.0, rúbrica Bucle de Excelencia.
- **Nuevo en paralelo:** 3 decks activos + 2 videos activos. El usuario opera el A/B/C testing y decide cuál promover a canónica.

---

### v2.1.0 · 2026-04-18 · vigente (Deck A)
**Motivo:** Compactación de 22 → 13 slides por decisión del usuario. Preserva tesis, pilares, rúbrica y entregables; fusiona slides adyacentes para aumentar densidad útil y reducir tiempo total de la masterclass sin perder valor.

**Añadido**
- Banda inferior con constante biológica (90–120 min · 4h · ≥8h) integrada en slide 5 "Dos estrategias conviven".
- Protocolo Notar→Pausar→Elegir integrado en slide 10 junto al prompt del Bucle (antes slides 17 y 19 separadas).
- Auditoría interna 20/20 visible dentro de la misma spec (antes solo en Vault).

**Cambiado**
- Slide 5 v2.0 "Dos estrategias conviven" + slide 6 v2.0 "Constante biológica" → fusionadas en slide 5 v2.1.
- Slide 8 v2.0 "¿Qué es la presencia?" + slide 9 v2.0 "Los 3 disparadores" + slide 10 v2.0 "Los 4 modos" → fusionadas en slide 7 v2.1 (3 secciones apiladas).
- Slide 14 v2.0 "Ecuación Dual con Método" absorbida como parte del marco de slide 5 v2.1.
- Slide 16 v2.0 "Rúbrica" + slide 17 v2.0 "Cómo aplicar el Bucle" → slide 9 + slide 10 v2.1 (la rúbrica queda sola por importancia; la aplicación se fusiona con Notar→Pausar→Elegir).
- Slide 20 v2.0 "Manifiesto" + slide 21 v2.0 "Plan de Activación" → fusionadas en slide 12 v2.1.
- Ciclo narrativo de 5 bloques a 4 bloques (Apertura · Diagnóstico+Pivote · Marco · Instrumento+Práctica · Cierre → Apertura · Diagnóstico+Pivote · Marco · Instrumento+Práctica+Cierre).

**Eliminado**
- Slide 11 v2.0 "Actividad Observar lo que volvemos paisaje" · conservada como slide 11 v2.1 (única actividad contemplativa retenida).
- Slide 12 v2.0 "Actividad Johari" · sacrificada por densidad útil (contenido accesible en workshop).
- Slide 15 v2.0 "Los 4 niveles de (R)Evolución dual" · sacrificada por simplicidad; se reintroduce en workshop del Ciclo 1-1-1.
- Slide 18 v2.0 "Práctica demo Orquestador Dual" · sacrificada; la práctica queda en Auditoría Dual (slide 8 v2.1) y en el Bucle aplicado (slide 10 v2.1).

**Corregido**
- Sin cambios: lista roja sigue en 0 apariciones en contenido operativo.

**Decisiones y trade-offs**

| Decisión | Trade-off asumido | Justificación |
|---|---|---|
| Fusionar definición de presencia + 3 disparadores + 4 modos en 1 slide | Densidad informativa alta en slide 7; mayor exigencia al presentador | Criterio #5 Simplicidad y #4 Densidad útil; separados consumían 3 slides con fragmentación narrativa. |
| Sacrificar actividad Johari | Reduce auto-observación contemplativa | Actividad 11 (Observar paisaje) cubre el mismo propósito con menor tiempo. Johari se mueve a workshop. |
| Sacrificar slide de 4 niveles evolutivos | El marco de progresión a 12 semanas no visible en masterclass | Masterclass debe caber en 60 min; los 4 niveles son activo de workshop y clínica. |
| Fusionar manifiesto + Ciclo 1-1-1 | Slide 12 visualmente más densa | Preserva el cierre emocional y el CTA en un solo momento; evita que la sesión termine sin CTA tangible por falta de tiempo. |
| Mantener Auditoría Dual (slide 8) como único entregable vivo | Único ejercicio práctico en la sesión | Criterio #10 Valor: sin entregable tangible, la masterclass no tiene cierre medible. |
| Incluir rúbrica 20/20 dentro del .md visible | Incrementa longitud del archivo | Transparencia editorial + instrumenta al lector para auditar sus propias piezas con la misma rúbrica. |

**Notas de compatibilidad**
- **Se mantiene igual:** título, header/footer, paleta, tipografía, logo, slide 1 cover, slide 2 metas, slide 3 y 4 ecuaciones canónicas, slide 6 automatismo, slide 13 canales, CTAs escalonados.
- **Requiere ajuste:** guion de facilitación del presentador (tiempos por slide recalculados); workshop y clínica absorben los 4 niveles y la actividad Johari.
- **Próxima revisión:** post-ejecución del primer grupo con v2.1 → evaluar si la carga cognitiva de slide 7 requiere volver a 3 slides (v2.1.1 patch o v2.2.0 minor).

---

### v2.0.0 · 2026-04-18 · reemplazada por v2.1.0
**Motivo:** Iteración sobre S2 existente (25 slides publicadas) para integrar el pivote del usuario (no todo automatismo es malo, no toda presencia es sostenible >8h), aplicar Brand Voice v3.0 completo y añadir el Bucle de Excelencia como instrumento operativo.

**Añadido**
- Slide 5 nueva · "Dos estrategias conviven en ti" (marco dual explícito desde el inicio).
- Slide 6 nueva · "Constante biológica: nadie sostiene foco pleno más de 8 horas" (evidencia honesta con indicador instrumentable).
- Matriz 2×2 del automatismo en slide 7 (deseable/tóxico × diseñado/heredado).
- Distinción presencia estratégica vs performativa en slide 8.
- Slide 9 nueva · "Los 3 disparadores que exigen presencia".
- Slide 10 nueva · "Los 4 modos operativos A/B/C/D".
- Slide 13 nueva · "Auditoría Dual" (primer entregable tangible en vivo).
- Slide 14 nueva · "La Ecuación Dual con Método".
- Slide 15 nueva · "Los 4 niveles de (R)Evolución dual".
- Slides 16 y 17 nuevas · Bucle de Excelencia (rúbrica 10 criterios + prompt operativo 3 pasos).
- Slide 18 nueva · Práctica demo en vivo con 4 roles (Director, Diseñador, Guardián, Árbitro).
- Slide 19 nueva · Protocolo Notar → Pausar → Elegir.
- Slide 21 rediseñada · Ciclo 1-1-1 con entregable certificable y 3 CTAs escalonados.

**Cambiado**
- Slide 1 cover: sub-CTAs duales mantenidos tal cual (continuidad de serie).
- Slide 2 metas: sin cambio de contenido, reforzada con ancla P1.
- Slide 3 y 4 ecuaciones: sin cambio (base canónica de la serie).
- Slide 7 "¿Qué es el automatismo?": reemplaza el párrafo por matriz 2×2; frase honesta original usada como callout lateral.
- Slide 8 "¿Qué es la presencia?": bullets 4-frase + chips estratégica/performativa.
- Slide 11 y 12 actividades: conservadas con estructura explícita de tiempo.
- Slide 20 manifiesto: texto canónico conservado.
- Slide 22 canales: sin cambio.

**Eliminado**
- Slides de relleno visual del original que no aportaban densidad útil (reducción de 25 a 22 slides, Criterio 4 y 5 de la rúbrica: densidad útil + simplicidad).
- Sesiones de introducción larga previas a la ecuación (compactadas en slides 1-2).

**Corregido**
- Cero apariciones de `arquitecto/arquitectura` (auditado).
- Cero apariciones de `transformación`; sustituido por `(R)Evolución`.
- Cero `hack/truco/secreto/magia/resultados instantáneos` (auditado).
- Cifras con evidencia tipada [E:Dato/Indicador/Señal/Dato requerido] en todas las slides de contenido.

**Decisiones y trade-offs**

| Decisión | Trade-off asumido | Justificación |
|---|---|---|
| Mantener título canónico "Del Automatismo a estar En Presencia" en vez de adoptar el título alternativo del usuario "Automatismo y Presencia. (R)Evoluciona…" | Pierde modernidad del nuevo pivote en título | Continuidad de serie (S1-S2-S3); el pivote se comunica en sub-CTAs y slide 5. Menor costo de re-branding de página de aterrizaje. |
| Reducir a 22 slides (desde 25) | Menos respiración visual | Criterio "Densidad útil" (rúbrica #4) y "Simplicidad" (#5). Cada slide eliminada no aportaba decisión/comprensión/acción. |
| Rúbrica Bucle de Excelencia en 2 slides (16 criterio + 17 aplicación) | 1 slide extra | La rúbrica es el diferenciador operativo; mostrarla sin explicar cómo aplicarla reduce su valor a conocimiento inerte. |
| Constante biológica ≥8h marcada como [E:Indicador sugerido] y [E:Dato requerido] | No afirma como hecho absoluto | Regla G2 de Brand Voice v3.0 (evidencia honesta). Literatura exacta a citar en materiales complementarios, no en slide. |
| Mantener actividades 11 y 12 del original | Alarga el centro del deck | Alta participación y valor contemplativo reportado en Ciclo 1; eliminar restaría ADN de la serie. |
| Auditoría Dual (slide 13) como entregable en vivo | Requiere 3 min de actividad | Garantiza que el alumno salga con un artefacto tangible (Criterio #10 Valor). |

**Notas de compatibilidad**
- **Se mantiene igual:** título oficial, header/footer, paleta, tipografía, logo, slide 1 cover, slide 20 manifiesto, slide 22 canales.
- **Requiere ajuste:** landing page del programa debe añadir mención al Bucle de Excelencia como entregable certificable.
- **Próxima revisión:** post-ejecución del primer grupo con v2.0 → evaluar incorporar métricas reales a slide 6 y 7.

---

### v1.0.0 · fecha desconocida · publicada (25 slides) · reemplazada por v2.0.0
Spec canónica original de S2, disponible como PDF de referencia:
`/Users/deonto/Downloads/pristino_ide_agent/inputs/masterclasses-metodologia/S2MasterclassDelAutomatismoaestarEnPresencia (1).pdf`

### v0.9.0 · 2026-04-18 · descartada
Borrador preliminar con título alternativo *"De Autómata a Artesano"*. Descartado por ruptura de continuidad de serie y por centrar la narrativa en conversión del sujeto en vez de (r)evolución dual de estrategias.
Archivo: `ARCHIVED-SPEC-Masterclass-Automatismo-y-Presencia-v1.md`

---

## 4 · Protocolo de publicación (sin fricción)

1. Incrementa versión en la spec y actualiza encabezado.
2. Registra entrada nueva en este Vault (Añadido / Cambiado / Eliminado / Corregido / Decisiones / Notas).
3. Ejecuta pruebas de compatibilidad (sección 5).
4. Marca la versión anterior como "reemplazada"; la nueva como "vigente".
5. Renombra el archivo de la spec reemplazada a `ARCHIVED-{nombre}.md`.
6. Opcional: publica changelog público en `metodologia.info/changelog`.

---

## 5 · Pruebas de compatibilidad (antes de marcar vigente)

### Gates no negociables Brand Voice v3.0
- [x] Minto Completo por slide (conclusión + soportes + evidencia + CTA de bloque)
- [x] Lista roja = 0 (verificado por grep)
- [x] Español latino neutro, trato "tú"
- [x] CTA ejecutable en 1 acción
- [x] Pilares P1/P2/P3 anclados por soporte

### Rúbrica /20 sobre la propia spec
La spec v2.0.0 fue auditada contra los 10 criterios de su propia rúbrica antes de publicación:

| # | Criterio | Puntaje | Notas |
|---|---|---|---|
| 1 | Fundamento | 2/2 | Cada slide deriva de la tesis central |
| 2 | Veracidad | 2/2 | Cifras con [E] tipado o dato requerido |
| 3 | Calidad | 2/2 | Sin contradicciones internas |
| 4 | Densidad útil | 2/2 | 22 slides, 0 decoración |
| 5 | Simplicidad | 2/2 | 1 idea nuclear por slide |
| 6 | Claridad | 2/2 | Automatismo, presencia, bucle definidos |
| 7 | Precisión | 2/2 | Condiciones (≥8h, 3 disparadores) explícitas |
| 8 | Profundidad | 2/2 | Trade-offs (deseable/tóxico, estratégica/performativa) |
| 9 | Coherencia | 2/2 | Estructura Minto consistente |
| 10 | Valor | 2/2 | Auditoría Dual entregable en vivo |

**Total:** 20/20 · **Aprobada para publicación**

### Consistencia de insumos
- Mismo prompt a NotebookLM sobre esta spec debería producir variaciones solo estilísticas, nunca de decisión.

---

## 6 · Roadmap de versiones futuras

- **v2.1.0** (MINOR, planeada): añadir 1 slide con métricas reales post-primer grupo v2.0.0.
- **v2.2.0** (MINOR, planeada): integrar ejercicio de Habit Portfolio Audit del notebook FAM-B N01 como actividad 4.
- **v3.0.0** (MAJOR, posible): si la evidencia muestra que la rúbrica debe reducirse a 7 criterios en vivo (los 10 para entregables asíncronos), se reformulan slides 16 y 17.

---

**Fin del Vault v2.0.0.**
