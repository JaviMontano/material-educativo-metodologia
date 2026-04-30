# MetodologIA Brand Voice · CHANGELOG

## v3.0.0 · 2026-04-30 · vigente

**Motivo:** primera edición Premium/Deluxe + anticipación + definiciones con tests + Vault v2.0 anclado a cartilla v1.6.

### Añadido
- 6 gates no negociables (G1-G6) con anclaje explícito a [P1|P2|P3].
- Rúbrica /20 con 10 criterios y escala 0/1/2.
- Modos operativos: Producción, Auditoría, Chat.
- Plantillas listas para copiar (Minto Completo, Minto Micro, Ultracorto, Transaccional urgente).
- Plantilla de *Indicador sugerido* (métrica + definición + frecuencia + dueño + umbral).
- Lista roja de palabras prohibidas en piezas finales.
- Lista verde de léxico preferido.
- Vault v2.0 con CHANGELOG, DECISIONS, registro de versiones, protocolo de publicación, pruebas de compatibilidad.
- Anexo A · prueba de compatibilidad cartilla v1.6 (3 secciones auditadas: § 9, § 11, § 19, todas 20/20).

### Cambiado
- Voz consolidada: español latino neutro · trato `tú` por defecto · voseo solo en citas literales.
- Pilares P1-P3 elevados a anclaje obligatorio (G6) — antes implícito.
- Score requerido: rúbrica 20/20 para marcar `vigente`.

### Eliminado
- "Tree of Prompts" como técnica recomendada (era error conceptual; reemplazada por Tree of Thought intra-prompt + Chaining/Stacking inter-prompt).
- Voseo regional ("vos", "tenés", "podés", imperativos en -á / -í) en la cartilla v1.6.
- Palabra "arquitectura" en descripciones de marca (Pristino card, etc.).
- Palabra "Transformacional" como categoría de prompts (renombrado a "Conversor").

### Corregido
- Drift `8 ejes ENTRUSTED+ → 9 ejes + capa meta` resuelto en § 19, § 20.
- Drift `DSV → DSVSR` íntegro en títulos, TOC, cross-refs.
- Drift `PIVOTE como pipeline 10-pasos → framework 6 dimensiones · 2 fases` con pipeline /0-/9 separado en § 9.5.
- Bug TOC § 24/§ 11 desincronía ES/EN.
- Bug hero CTA apuntaba a `#atributos` en lugar de `#pipeline-pivote`.
- Cross-refs § 5 (SPEC), § 22 (esp-semanal), footer (2 salidas) repuntados a sus secciones correctas.
- Paridad ES/EN completa en pipeline /0-/9, 12 cláusulas, 9 ejes ENTRUSTED+, 10 etiquetas, 12 prácticas.

### Decisiones y trade-offs
- **Decisión:** Vault separado del HTML como archivos `.md`. **Trade-off:** dos artefactos en lugar de uno · **Justificación:** versionado independiente del Brand Voice y del cartilla.
- **Decisión:** `[P1|P2|P3]` visibles inline en step-titles y cards. **Trade-off:** densidad visual aumenta · **Justificación:** G6 exige anclaje explícito (no implícito).
- **Decisión:** Tree of Prompts retirado completamente en lugar de re-explicado. **Trade-off:** una técnica menos · **Justificación:** Tree of Thought (intra-prompt) + Stacking ya cubren el caso de uso.

### Notas de compatibilidad
- **Qué se mantiene igual:** estructura de 25 secciones (§ 1 a § 24 + § 9.5 + § 17.5), 169 modales, branding visual (navy/gold/lilac), toggle ES/EN, dark/light mode.
- **Qué requiere ajuste en futuras piezas:** toda nueva sección debe pasar G1-G6 + rúbrica 20/20 antes de marcarse vigente.

---

## v2.9.1 · histórico (no anclado a cartilla)

**Motivo:** robustez operativa + rúbrica /20 + trazabilidad. Sin anclaje a cartilla específica.
**Estado:** anterior · superseded por v3.0.0.

## v2.9.0 · histórico

**Motivo:** Micro + control rápido opcional + modo chat.
**Estado:** anterior.

## v2.8.0 · histórico

**Motivo:** base Minto-First OS.
**Estado:** anterior.
