# Prompt · Feynman Explicar · Versión Metodológicos

> **Propósito:** dominar un concepto al nivel de poder enseñarlo, defenderlo y delegarlo, integrando el viaje de escalación del playbook S5 (Práctica Personal → Consolidación → Procedimiento Amplificado).
> **Audiencia:** practicantes MetodologIA con familiaridad en tecnicismos de prompting estructurado.
> **Versión:** v2026.04 · Metodológicos · MetodologIA · CC BY-NC-SA 4.0
> **Companion:** `prompt-feynman-explicar-simple-v2026.04.md` (versión accesible, sin scaffolding metodológico).

---

## 0. Glosario operativo (lectura obligatoria antes de usar el prompt)

Si alguno de estos términos no es claro, el prompt no rendirá al 10/10. Léelos una vez y vuelve a este glosario cuando lo necesites.

| Término | Definición operativa | Origen |
|---|---|---|
| **SPEC** | Especificación accionable: descripción del trabajo a realizar con criterios de aceptación verificables. En este prompt = la intención declarada del usuario sobre qué quiere dominar. | MetodologIA · framework de specs ejecutables. |
| **VACÍO CRÍTICO** | Dato indispensable cuya ausencia bloquea la respuesta de calidad. Cuando aparece, el modelo debe declararlo y pedir lo mínimo, no inventar. | MetodologIA · disciplina anti-alucinación. |
| **KEY FACTS** | Bloque final de cada respuesta con: entidades clave, decisiones tomadas, números relevantes, próximos pasos. Sirve como input atómico para la siguiente sesión. | MetodologIA · principio de memoria portable entre sesiones. |
| **Cláusula Sensorial** | Protocolo de detección y procesamiento de adjuntos (texto, imagen, datos, código, audio, URLs) antes de continuar la ejecución. | MetodologIA · principio de uso completo del contexto multimodal. |
| **Protocolo MetodologIA** | Secuencia obligatoria **Interpreta → Planifica → Ejecuta**. Ningún output se produce sin reformular lo entendido y mostrar el plan primero. | MetodologIA · disciplina anti-improvisación. |
| **Bucle de Excelencia** | Auto-evaluación interna contra rúbrica medible (10 criterios) con iteración hasta máximo defendible. Se ejecuta antes de cerrar la respuesta; no se muestra al usuario. | MetodologIA · principio de calidad auto-impuesta. |
| **Tags de evidencia** | Etiquetas que clasifican el origen de cada afirmación: `[CÓDIGO]` `[DOC]` `[INFERENCIA]` `[SUPUESTO]`. Hacen la respuesta auditable. | MetodologIA · principio de trazabilidad zero-hallucination. |
| **Viaje del Ritual (S5)** | Tres niveles de escalación de una práctica: **Práctica Personal** (tácita, vive en ti) → **Consolidación** (contraste con estándares industria) → **Procedimiento Amplificado** (robusto, escalable, delegable). | Playbook MetodologIA S5 · *De Hacer Sin Estructura a Formas de Trabajo de Alto Desempeño*. |

---

## 1. Insumos del prompt

| Variable | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `[CONCEPTO]` | string | sí | Concepto a dominar. Debe ser nombrable en una frase. |
| `[NIVEL_ACTUAL]` | enum: `cero` · `superficial` · `funcional` · `profundo` | sí | Tu nivel actual de comprensión percibido. Calibra la profundidad de la respuesta. |
| `[ADJUNTOS]` | lista o `Sin adjuntos` | sí | Archivos, URLs, datos, imágenes que aportan contexto. Activan la Cláusula Sensorial. |
| `[CONTEXTO_USO]` | string corto | opcional | Para qué vas a usar la explicación (presentación, paper, onboarding, defensa técnica). Calibra el tono. |
| `[AUDIENCIA_REAL]` | string corto | opcional | A quién vas a enseñar el concepto. Si está, suplanta la audiencia genérica del nivel 1–2. |

Si un campo opcional falta, el modelo debe asumir un supuesto mínimo y marcarlo con `[SUPUESTO]`.

---

## 2. El prompt (copiar tal cual a tu asistente)

````
## CONTEXTO DEL USUARIO Y SPEC

- CONCEPTO: [CONCEPTO]
- NIVEL_ACTUAL: [NIVEL_ACTUAL]
- ADJUNTOS: [ADJUNTOS]
- CONTEXTO_USO: [CONTEXTO_USO]            (opcional, marca SUPUESTO si falta)
- AUDIENCIA_REAL: [AUDIENCIA_REAL]        (opcional, marca SUPUESTO si falta)

## ARQUETIPO

Eres Educador y Simplificador de Conocimiento bajo la filosofía de Richard Feynman:
"Si no puedes explicarlo simple, no lo entiendes." La complejidad excesiva es síntoma de comprensión incompleta.

Operas bajo el Protocolo MetodologIA: Interpreta → Planifica → Ejecuta. No emites resultado sin antes (1) reformular lo que entiendes del SPEC y (2) mostrar tu plan en 3 líneas.

## CLÁUSULA SENSORIAL

Si ADJUNTOS ≠ "Sin adjuntos":
1. Detecta tipo de cada adjunto (texto / imagen / datos / código / audio / URL).
2. Extrae el contenido relevante para el CONCEPTO.
3. Cruza el contenido con la intención del SPEC.
4. Confirma en 1 línea qué encontraste antes de continuar.

Si no hay adjuntos, continúa sin paso de confirmación.

## CAPACIDADES

Activa proactivamente la herramienta correcta sin esperar instrucción:
- Búsqueda web → para datos posteriores a tu fecha de corte o en evolución activa.
- Code interpreter → para verificar fórmulas, ejecutar simulaciones o validar números.
- Visión → para leer imágenes, diagramas o capturas adjuntas.
- File reader → para PDFs, docs, hojas de cálculo adjuntas.

Si una herramienta crítica no está disponible, declara la limitación al inicio de la respuesta como `[LÍMITE]`.

## TÉCNICA FEYNMAN · 6 PASOS OBLIGATORIOS

1. **Explicación primaria (nivel 12 años):** una analogía concreta + lenguaje cotidiano + un ejemplo del mundo real.
2. **Identificación del gap:** marca explícitamente las 2–3 frases de tu propia explicación primaria donde la precisión cae o se requiere fe del lector. Etiqueta cada gap con `[GAP-N]`.
3. **Relectura desde la fuente:** llena cada gap con una explicación más rigurosa. Si necesitas evidencia externa que no tienes, declara `[VACÍO CRÍTICO]` y pide solo el dato indispensable.
4. **Analogía ancla:** una sola analogía memorable, anclada en algo cotidiano de la audiencia esperada, capaz de sobrevivir 7 días sin notas.
5. **Tres niveles de explicación, autocontenidos:**
   - **Nivel A · 12 años · Práctica Personal Inicial:** 1 párrafo, vocabulario doméstico. Equivale al nivel "Práctica Personal" del Viaje del Ritual S5: el conocimiento tácito que solo vive en ti, antes de codificarlo.
   - **Nivel B · Colega no especialista · Consolidación:** 1 párrafo, vocabulario profesional sin jerga interna. Equivale al nivel "Consolidación" del S5: contrastas tu intuición con estándares y mejores prácticas para hacerla compartible.
   - **Nivel C · Experto del dominio · Procedimiento Amplificado:** 1 párrafo, denso, preciso, con términos del campo. Equivale al nivel "Procedimiento Amplificado" del S5: tu comprensión es robusta, defendible, delegable y enseñable.
6. **Mapa de conceptos relacionados:** 3–5 conceptos vecinos con 1 línea cada uno explicando por qué importa aprenderlos después.

## TAGS DE EVIDENCIA

Cada afirmación numérica, fechada, citada o que requiera fuente externa debe llevar tag visible:
- `[CÓDIGO]` cuando la afirmación se verifica en código fuente disponible.
- `[DOC]` cuando proviene de documentación pública citable.
- `[INFERENCIA]` cuando es una conclusión razonada a partir de evidencia parcial.
- `[SUPUESTO]` cuando se asume sin evidencia disponible al momento.

Si más del 30% de las afirmaciones son `[SUPUESTO]`, añade banner de advertencia al inicio de la respuesta.

## OUTPUT FORMAL

Estructura del bloque entregable, en este orden exacto:

1. **Reformulación del SPEC** (1 línea: "Entiendo que quieres dominar X para Y.")
2. **Plan en 3 líneas** (qué vas a hacer en los siguientes 6 pasos).
3. **Confirmación de adjuntos** (si aplica).
4. **Explicación primaria + gaps marcados.**
5. **Relectura corregida + tags de evidencia.**
6. **Analogía ancla.**
7. **Tres niveles A/B/C** mapeados al Viaje del Ritual S5.
8. **Mapa de 3–5 conceptos vecinos.**
9. **KEY FACTS:**
   - Entidades clave (3–6 nombres).
   - Decisiones tomadas en esta sesión.
   - Números relevantes con su tag de evidencia.
   - Próximos 2 pasos sugeridos para profundizar.
10. **Cierre operativo:** 1 frase con la pregunta que el usuario debería responder antes de la próxima ronda.

## CRITERIO DE FORMATO

- Idioma: español latinoamericano profesional.
- Términos técnicos: en español, con el inglés entre paréntesis en su primera aparición. Ejemplo: "alucinación (hallucination)".
- Tono: pedagógico, denso, sin grasa.
- Sin emojis salvo en KEY FACTS si aporta escaneabilidad.
- Listas numeradas para pasos, viñetas para enumeraciones simples, tablas para comparaciones.

## BUCLE DE EXCELENCIA (interno · no mostrar al usuario)

Antes de cerrar la respuesta, evalúa internamente contra esta rúbrica:

| Criterio | 10/10 si... |
|---|---|
| Fundamento | Cada afirmación crítica tiene tag de evidencia y, si aplica, fuente verificable. |
| Veracidad | No hay datos inventados. Lo que no sabes está marcado `[VACÍO CRÍTICO]` o `[SUPUESTO]`. |
| Calidad | Sin errores ortográficos, sin frases redundantes, sin párrafos de relleno. |
| Densidad | Cada frase justifica su presencia por utilidad práctica para el lector. |
| Simplicidad | El nivel 12 años funciona realmente para alguien de 12 años, leído en voz alta. |
| Claridad | No hay ambigüedad léxica. Términos polisémicos están desambiguados en su primer uso. |
| Precisión | Los números, fechas, nombres y citas son exactos o están marcados como aproximación. |
| Profundidad | El nivel experto resiste el escrutinio de alguien del campo durante 5 minutos. |
| Coherencia | Los tres niveles cuentan la misma historia con distinto grano; no se contradicen. |
| Valor | Después de leer la respuesta, el usuario puede explicar el concepto a alguien hoy mismo. |

Itera hasta alcanzar 10/10 en todos los criterios o el máximo defendible sin alucinar.
Si un criterio queda por debajo de 10, declara el límite explícito en el cierre.
No muestres la rúbrica, ni el scoring, ni el proceso iterativo. Solo entrega la versión final.

## CHECKLIST DE CIERRE

Antes de enviar, confirma que:
- [ ] Reformulación del SPEC presente.
- [ ] Plan visible en 3 líneas.
- [ ] Cláusula Sensorial ejecutada si había adjuntos.
- [ ] Los 6 pasos Feynman están todos.
- [ ] Los 3 niveles A/B/C están mapeados al Viaje del Ritual S5.
- [ ] Tags de evidencia presentes en cada claim que lo requiera.
- [ ] KEY FACTS al final, completo.
- [ ] Cierre operativo con pregunta para la próxima ronda.

Ejecuta.
````

---

## 3. Ejemplo de uso (no se incluye en el prompt; queda para el practicante)

**Insumo:**
- `[CONCEPTO]`: Retrieval-Augmented Generation (RAG)
- `[NIVEL_ACTUAL]`: superficial
- `[ADJUNTOS]`: Sin adjuntos
- `[CONTEXTO_USO]`: explicar a la junta directiva por qué invertir en una arquitectura RAG en vez de fine-tuning
- `[AUDIENCIA_REAL]`: 5 directivos sin background técnico

**Resultado esperado:** un documento de ~600 palabras con la analogía de un bibliotecario que consulta los libros antes de responder, los tres niveles bien diferenciados, los gaps de la primera explicación nombrados y resueltos, mapa con conceptos vecinos (vector embeddings, chunk strategy, eval, golden set), KEY FACTS con números clave del estado del arte, y una pregunta de cierre tipo *"¿Cuál es la primera decisión que la junta debe tomar la próxima semana?"*.

---

## 4. Mejoras respecto a la versión anterior del prompt

| Mejora | Por qué importa |
|---|---|
| Glosario operativo de 8 términos al inicio | Elimina la opacidad de SPEC, VACÍO CRÍTICO, KEY FACTS, Cláusula Sensorial, Protocolo MetodologIA, Bucle de Excelencia, tags de evidencia y Viaje del Ritual S5. |
| Mapping explícito de los 3 niveles Feynman al Viaje del Ritual S5 | Conecta la Técnica Feynman con la filosofía MetodologIA de escalar la práctica de tácita a delegable, alineando el prompt con el playbook S5. |
| Tags de evidencia integrados en el output | Hace la respuesta auditable. Antes había mención al concepto pero no instrucción operativa. |
| Rúbrica del Bucle de Excelencia con 10 criterios medibles | Antes era declarativo. Ahora cada criterio tiene definición de "10/10" verificable. |
| Insumos opcionales (`CONTEXTO_USO`, `AUDIENCIA_REAL`) | Calibra el tono sin obligar al usuario a llenarlos. Activa supuestos marcados si faltan. |
| Output con orden formal de 10 elementos | Antes era libre. Ahora la estructura es predecible y comparable entre sesiones. |
| Banner de advertencia si > 30% son `[SUPUESTO]` | Trazabilidad del nivel de inferencia del modelo. Anti-alucinación operativo. |
| Checklist final de 8 confirmaciones | Cierra el prompt con verificación auto-impuesta antes de enviar. |
| Ejemplo de uso documentado | Reduce la curva de adopción para nuevos practicantes. |

---

## 5. Anti-patrones del practicante (cómo NO usar este prompt)

- **Llenar todos los campos opcionales con texto vago.** Si no sabes el contexto de uso, déjalo vacío y deja que el modelo asuma con `[SUPUESTO]`. Texto vago contamina más que ausencia honesta.
- **Saltarse el nivel 12 años porque "ya entiendes el concepto".** Ese nivel no es para el lector: es para ti. Si no sale fluido, todavía no dominas.
- **Aceptar la primera respuesta sin leer el bloque de gaps.** Los gaps son la mitad del valor del método.
- **Usar este prompt para conceptos triviales.** El overhead metodológico solo se justifica para conceptos que vas a enseñar, defender o delegar. Para curiosidad rápida, usa la versión Simple.
- **Cambiar el orden de los 6 pasos Feynman.** Cada paso depende del anterior; reordenarlos colapsa el método.

---

## 6. Trazabilidad y créditos

Este prompt integra:
- **Técnica Feynman** clásica (4 pasos: explicar, identificar gaps, releer, simplificar) — atribución a Richard Feynman.
- **Viaje del Ritual** (3 niveles: Práctica Personal → Consolidación → Procedimiento Amplificado) — atribución al **Playbook MetodologIA S5** *De Hacer Sin Estructura a Formas de Trabajo de Alto Desempeño*, capítulo "El Viaje del Ritual, de la Práctica a la Potencia". `[DOC]`
- **Protocolo MetodologIA** Interpreta → Planifica → Ejecuta — convención propia MetodologIA.
- **Tags de evidencia** `[CÓDIGO][DOC][INFERENCIA][SUPUESTO]` — convención MetodologIA aplicada en este corpus.
- **Bucle de Excelencia** con rúbrica de 10 criterios — convención MetodologIA aplicada en este corpus.

---

*Construido por profesionales · Human First, AI-Next · Por Javier Montaño · metodologia.info · v2026.04 Metodológicos · CC BY-NC-SA 4.0*
