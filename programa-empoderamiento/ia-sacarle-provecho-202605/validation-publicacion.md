# Validacion publicacion · IA sacarle provecho 2026-05

Estado: success
Confianza final: 0.96
Fecha: 2026-05-21T13:34:00-05:00
Ruta: `programa-empoderamiento/ia-sacarle-provecho-202605/`

## Resultado

| Check | Estado | Evidencia |
|---|---:|---|
| files_non_empty | PASS | 16 archivos base > 0 bytes |
| json_valid | PASS | 1 JSON validos |
| no_local_or_private_paths | PASS | sin rutas locales privadas, carpetas de descarga ni URLs de archivo |
| no_private_emails | PASS | sin correos privados |
| no_phone_numbers | PASS | sin telefonos visibles ni tel: |
| no_participant_names_configured | PASS | sin nombres privados configurados; autor/facilitador publico permitido |
| local_links_exist | PASS | todos los href/src relativos existen o son artefactos generados |
| workshop_chatgpt_prompt_links | PASS | memoria workshop contiene enlaces ChatGPT con prompt= |
| workshop_gemini_claude_copy_open | PASS | Gemini y Claude abren destino oficial y copian prompt como respaldo |
| assets_present | PASS | logos MetodologIA y Pristino presentes |

## Politica PII-safe

No se publican notas privadas, transcripciones literales, correos, contratos, recibos ni nombres de participantes. El nombre del facilitador/autor se considera identidad publica del repositorio y no participante privado.

## Git y entorno

El worktree local principal presento `short read while indexing` en archivos ajenos al paquete. No se uso para stagear. La publicacion se preparo desde un clon limpio de `origin/main` en una rama nueva.

## GitHub Pages

La API de GitHub Pages respondio 404 para este repositorio durante la validacion, por lo que Pages no se considera activo. Los enlaces relativos quedan listos para activacion posterior.

## Validacion navegador

Servidor local: `http://127.0.0.1:8765/`

| Check navegador | Estado | Evidencia |
|---|---:|---|
| HTML principales | PASS | 12 HTML cargados por navegador. |
| Viewports | PASS | 390 px, 820 px y 1440 px. |
| Consola JS | PASS | 0 errores. |
| Assets locales | PASS | 0 imagenes rotas y 0 respuestas locales 404. |
| Layout | PASS | 0 overflow horizontal detectado. |
| Workshop prompts | PASS | 4 enlaces ChatGPT con `prompt=`, 4 Gemini y 4 Claude. |
| Tema y copia | PASS | Tema claro por defecto; boton copiar devuelve estado visual `Copia manual` en HTTP local. |
