# MetodologIA Brand Voice · DECISIONS log

Registro de decisiones operativas con trade-offs y justificaciones.

---

## D-001 · Voz panregional `tú` (no voseo) · 2026-04-29

**Decisión:** voz oficial MetodologIA usa `tú` panregional en piezas finales.
**Trade-off:** pierde calidez rioplatense y sabor argentino.
**Justificación:** alcance LATAM+ES requiere neutralidad lingüística. Voseo permitido solo en citas literales o firmas de marca personal.
**Aplicación cartilla v1.6:** 80+ formas de voseo reemplazadas en HTML body + 135 patches en JSON modal data.

## D-002 · Tree of Prompts retirado · 2026-04-29

**Decisión:** eliminar "Tree of Prompts" como técnica recomendada en cartilla.
**Trade-off:** una técnica avanzada menos en § 14.
**Justificación:** era ambigüedad conceptual con Tree of Thought. La frontera intra-prompt (Tree of Thought) vs inter-prompt (Chaining + Stacking) cubre el caso. Tree of Prompts no es estándar industrial.
**Aplicación:** § 14 9 formas → 8 formas · grupo B 3 cards → 2 cards · modal `orch-tree-prompts` eliminado del JSON.

## D-003 · ENTRUSTED+ pasa de 8 a 9 ejes + capa meta · 2026-04-29

**Decisión:** ampliar acrónimo ENTRUSTED+ de 8 ejes a 9 (E·N·T·R·U·S·T·E·D) + capa meta `+` separada.
**Trade-off:** mayor densidad de evaluación · más esfuerzo por output.
**Justificación:** la 9ª letra D = Definition of Done refleja la promoción central de v3.4. El `+` documenta correctamente la capa meta (bucle excelencia + insights proactivos) que antes estaba implícita.
**Aplicación:** § 11 ENTRUSTED+ 10 cards (9 ejes + 1 meta) · CSS `.attr-card.attr-plus` distinguible.

## D-004 · PIVOTE como framework canónico (no pipeline) · 2026-04-29

**Decisión:** P.I.V.O.T.E. es framework de 6 dimensiones · 2 fases (Personas·Interacciones·Valor + Organización·Tecnología·Evolución), no un pipeline operativo.
**Trade-off:** rompe interpretación previa de versiones v1.0-v1.2 que llamaban "pipeline P.I.V.O.T.E." a los 10 pasos /0-/9.
**Justificación:** definición canónica de metodologia.info/vision/. El pipeline operativo /0-/9 es un artefacto distinto que vive dentro de las dimensiones Organización + Evolución.
**Aplicación:** § 9 reescrito con 6 cards en 2 fases + § 9.5 nueva sección con los 10 pasos · cross-link bidireccional.

## D-005 · Anclaje [P1|P2|P3] visible obligatorio · 2026-04-30

**Decisión:** cada soporte / step-title / card de método debe mostrar inline el tag `[P1|P2|P3]`.
**Trade-off:** densidad visual aumenta · diseño compite con la sustancia.
**Justificación:** G6 exige anclaje explícito a pilares MetodologIA. Sin tag visible, queda implícito y no es auditable.
**Aplicación:** CSS `.pillar-tag` añadido (estilo pill compacto) · § 11 ENTRUSTED+ 9 ejes + meta con tags · § 19 Protocolo 7 pasos con tags.

## D-006 · BV separado del HTML como archivos `.md` · 2026-04-30

**Decisión:** Brand Voice OS vive en 3 archivos markdown (`BV_v3.0.0.md` + `CHANGELOG.md` + `DECISIONS.md`), no embebido en el HTML del cartilla.
**Trade-off:** dos artefactos a mantener (cartilla + Vault).
**Justificación:** versionado independiente. La cartilla es contenido pedagógico; el BV es metodología editorial. Ciclos de iteración distintos.
**Aplicación:** vault en `/dist/.discovery/v2.1-audit/MetodologIA_BrandVoice_*.md` · sync a repo `material-educativo-metodologia/.discovery/v2.1-audit/`.

## D-007 · Rúbrica 20/20 obligatoria para marcar `vigente` · 2026-04-30

**Decisión:** ninguna versión BV se marca `vigente` hasta que una muestra mínima de 3 piezas (1 Micro, 1 Completo, 1 Auditoría) apruebe rúbrica 20/20.
**Trade-off:** ciclo de release más largo.
**Justificación:** evita drift entre BV declarado y BV practicado. Si la cartilla v1.6 no aprueba 20/20, el BV v3.0.0 no se marca vigente.
**Aplicación inicial:** auditoría de § 9, § 11, § 19 ejecutada 2026-04-30 → 3/3 aprobadas → BV v3.0.0 vigente.

---

## Plantilla para futuras decisiones

```
## D-XXX · [Título] · YYYY-MM-DD

**Decisión:** …
**Trade-off:** …
**Justificación:** …
**Aplicación:** …
```
