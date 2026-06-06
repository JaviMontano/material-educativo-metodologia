# Estándar general para crear prompts
> Cómo diseñar un prompt MetodologIA que rinda con cero fricción y se pueda auditar.

## Guidelines
- Empieza por la intención: define el resultado que quieres y para quién, en una frase.
- Defaults primero: el prompt funciona tal cual; los parámetros viven en el texto con su valor por defecto.
- Demuestra, no describas: el cuerpo ejecuta el comportamiento; no se autodescribe ("este prompt es una macro que…").
- Una intención por prompt; si hay dos, son dos prompts.
- Voz MetodologIA: directa, profesional, densa; cada palabra se gana su lugar.

## Guardrails
- No inventes: marca {SUPUESTO} o {VACIO_CRITICO} ante falta de datos; no afirmes acceso a memoria, adjuntos o herramientas ausentes.
- Evidencia: toda afirmación factual con fuente o etiqueta de procedencia; cero citas inventadas.
- Privacidad: detecta y anonimiza PII por defecto.
- Separa hecho de inferencia y declara confianza (0.0–1.0).
- Sin metadiscurso ni trazas del proceso en la salida.

## Workflow
1. Intención — resultado, audiencia y criterio de éxito en 1 frase.
2. Estructura — elige el formato (natural · parámetros · SPEC · dupla) según el uso.
3. Defaults — fija los valores por defecto en el texto (cero fricción) y marca qué es ajustable.
4. Prueba en blanco — ejecútalo sin llenar nada: debe rendir solo.
5. Bucle de Excelencia — autoevalúa con la rúbrica de 10, itera hasta 10/10, entrega solo la versión final.

## Criterios de aceptación
- Fundamento — toda afirmación con base o marcada como supuesto.
- Veracidad — nada inventado ni sobrevendido.
- Calidad — anatomía sólida (rol, tarea, formato, criterio).
- Densidad — cero relleno; no se puede borrar nada sin pérdida.
- Simplicidad — lo más simple que funcione.
- Claridad — comprensible en una lectura.
- Precisión — términos exactos; criterios y números concretos.
- Profundidad — cubre lo esencial + casos borde.
- Coherencia — las 4 versiones alineadas entre sí y con título/desc.
- Valor — utilidad práctica directa; usable con los defaults.

## Definition of Done
- Rinde con defaults sin pedir nada al usuario.
- Ajustable editando texto (sin widgets ni campos vacíos).
- Pasa la rúbrica de 10; sin metadiscurso; guardrails aplicados.
- Trazabilidad: cada afirmación con procedencia o supuesto marcado.
