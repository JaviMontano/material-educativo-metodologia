# Contrato operativo · v1.2

Este contrato gobierna la ejecución de la skill. Si un ejemplo, workflow o
recurso histórico entra en conflicto, aplicar este archivo.

## Evidencia

- Una salida de IA no es una fuente.
- La coincidencia entre modelos puede revelar patrones o discrepancias, pero no
  constituye corroboración independiente: los modelos pueden compartir datos,
  sesgos y errores.
- Verificar claims materiales contra fuentes primarias o autoridades apropiadas.
- Conservar `coverage_gap` cuando no exista evidencia suficiente.

## Tiempos

Las rutas de 4 h, 20 h y 64 h son presupuestos de práctica. No predicen dominio,
retención, certificación, empleabilidad ni desempeño. Adaptar alcance y criterio
de cierre al dominio, punto de partida, calidad de las fuentes y riesgo.

## Privacidad y derechos

- No solicitar ni persistir secretos, credenciales, PII o información privada.
- No cargar fuentes sin autoridad o derechos verificables.
- Sanitizar ejemplos antes de compartirlos.

## Red y persistencia

- Red desactivada por defecto. Activarla cuando verificar actualidad o localizar
  fuentes sea parte explícita del encargo.
- Estado desactivado por defecto. Persistir únicamente con `--state-file` y una
  ruta escogida por el usuario.
- Escribir estado de forma atómica; nunca sobrescribir un archivo corrupto.
- No sincronizar, publicar ni activar conectores automáticamente.

## Estados honestos

Usar `BORRADOR`, `EVIDENCIA_PARCIAL`, `VERIFICADO` o `coverage_gap` según la
evidencia real. Completar una actividad no equivale a dominar el tema.
