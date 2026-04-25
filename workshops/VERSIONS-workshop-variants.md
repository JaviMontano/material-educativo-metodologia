# Workshop Discovery AI-Native · Variantes por audiencia · Bitácora

> Tres variantes del mismo workshop adaptadas a tres audiencias del framework Feynman re-mapeado.
> Naming: `workshop-discovery-ai-native-{audiencia}-v{YYYY.MM}.{md|html}`

---

## v2026.04 · 24 abr 2026 · Tres variantes Feynman

**Estado:** Vigente · publicable.

### Origen

Aplicación del prompt `prompts/prompt-feynman-explicar-metodologicos-v2026.04.md` como heurística de diseño. Los tres niveles del framework Feynman (12 años · colega · experto) fueron re-mapeados por instrucción del usuario a tres audiencias enterprise-real:

| Nivel Feynman | Audiencia MetodologIA | Mapeo al Viaje del Ritual S5 |
|---|---|---|
| 12 años · Simple | **Llano · 13 años** | Práctica Personal (tácita, vive en ti) |
| Colega · Intermedio | **Profesional** | Consolidación (contraste con estándares) |
| Experto · Profundo | **Empresas** | Procedimiento Amplificado (escalable, delegable) |

### Entregables de esta versión

| Audiencia | Markdown | HTML | Resumen ejecutivo | Total |
|---|---|---|---|---|
| **Llano · 13 años** | 179 líneas · 8 KB | 590 líneas · 33 KB | — | 2 archivos |
| **Profesional** | 302 líneas · 18 KB | 747 líneas · 45 KB | — | 2 archivos |
| **Empresas** | 365 líneas · 30 KB | 665 líneas · 87 KB | 116 líneas · 5 KB | 3 archivos |
| **Total** | — | — | — | **7 archivos** |

### Diferenciación por variante

#### Llano · 13 años
- **Quién:** estudiantes secundaria, talleres extracurriculares, clubes innovación.
- **Duración:** media jornada (4 h).
- **Sesiones:** 4 × 45 min.
- **Tono:** juguetón rioplatense ("vos"), sin jerga corporativa.
- **Idioma:** sólo ES.
- **Sin:** RACI, cotización, disclaimer comercial, Política XL, bandas FTE-meses.
- **Con:** tarjetón imprimible, errores típicos en lenguaje cotidiano, próximo nivel = Profesional.

#### Profesional
- **Quién:** profesional individual o equipo de 3–6 que aplica en su trabajo cotidiano.
- **Duración:** 1 día (6 h efectivas).
- **Sesiones:** 4 × 90 min + 3 breaks.
- **Tono:** pragmático directo, "tú" formal latinoamericano.
- **Idioma:** sólo ES (mantenerlo compacto).
- **Consolidación:** **48 h** post-workshop (vs 5 días de Empresas).
- **Sin:** RACI completo (sólo owner explícito), Política XL completa, percentiles P50/P80/P95, ADRs formales.
- **Con:** bandas RAT/MVP/(R)Evolución con FTE-meses indicativos (1–3 / 4–10 / 12–25), template de spec destilada, sección "cómo escalar a Empresas".

#### Empresas
- **Quién:** comité ejecutivo + equipos técnicos + PMO + procurement + (sectores regulados) compliance officer.
- **Duración:** 2 días + 5 días HITL.
- **Tono:** corporativo completo, vocabulario enterprise, anglicismos con traducción primer uso.
- **Idioma:** **bilingüe ES/EN** con toggle (211 spans).
- **Énfasis enterprise-only (vs playbook completo):**
  1. **Procurement / RFP-ready:** mapeo HITL ↔ RFP, 7 scoring criteria con pesos.
  2. **Multi-stakeholder governance:** Steering Committee (5–7 miembros), CCB integrado como T+6, integración con PMO existente.
  3. **SLAs contractuales** por etapa T+1..T+5 con penalizaciones, exclusiones, escalation matrix de 3 severidades.
  4. **Compliance addendum:** 6 frameworks (ISO 27001, GDPR/LFPDPPP/LPDP/LPD, SOX, BCBS 239, HIPAA/HL7, clasificación gobierno) + matriz control ↔ etapa ↔ evidencia.
  5. **Reporting al board:** template ASCII de 1 página, KPIs ejecutivos (time-to-traction, costo evitado, riesgo mitigado, adopción interna).
  6. **Cotización completa:** bandas con percentiles P50/P80/P95, disclaimer comercial textual obligatorio repetido en MD y HTML.
  7. **RACI ampliado** por 16 decisiones clave × 7 roles enterprise.
  8. **Stakeholder communication plan** con 9 audiencias (incluyendo representación laboral si aplica).
- **Resumen ejecutivo de 1 página** para enviar a C-level antes del workshop.

### Verificaciones aplicadas

```
Brand-lock (sofka/IRIS/ATLAS/CRONOS/SKAI/BFSI/SAGE/SDF):  0 hits en todos los 7 archivos ✅
Conteo de líneas dentro de rangos esperados:               7/7 ✅
Cobertura bilingüe en Empresas HTML:                       211 spans (target > 200) ✅
Wordmark MetodologIA presente:                             7/7 ✅
Footer con badges + atribución:                            7/7 ✅
Cero precios en moneda:                                    7/7 ✅ (sólo FTE-meses + disclaimers)
```

### Producción

Spawneados 3 agentes general-purpose secuenciales (paralelo bloqueado por rate limit temporal del API):
- Agente A · Llano HTML (590 líneas, 33 KB)
- Agente B · Profesional MD+HTML (302 + 747 líneas)
- Agente C · Empresas MD+HTML+Resumen (365 + 665 + 116 líneas, 211 spans bilingües)

---

## Convenciones

- **Versionado:** `vYYYY.MM` mayor; `vYYYY.MM.PATCH` correcciones.
- **Brand lock:** todos los archivos en este directorio son MetodologIA. Cero contaminación con otras marcas (regla CLAUDE.md).
- **Trazabilidad:** cada variante debe declarar su audiencia, duración, tono, y qué deja explícitamente fuera respecto a la variante mayor inmediata.
- **Cross-links obligatorios:** Llano enlaza a Profesional como "próximo nivel"; Profesional enlaza a Empresas como escalamiento.
- **MD y HTML deben tener paridad de contenido del cuerpo principal.** El HTML es la visualización del MD, no una destilación.

## Próximos candidatos (no creados aún)

- `workshop-discovery-ai-native-llano-13anos-onepager-vX.html` — tarjetón único A5 imprimible para repartir en aulas.
- `workshop-discovery-ai-native-profesional-onepager-vX.html` — hoja A4 para llevar a la oficina.
- `workshop-discovery-ai-native-empresas-rfp-anexo-vX.md` — anexo RFP-ready listo para incluir en bases técnicas de procurement.
- `workshop-discovery-ai-native-empresas-board-deck-vX.html` — slideshow para sesión con board.

---

*Construido por profesionales · Human First, AI-Next · Por Javier Montaño · metodologia.info · CC BY-NC-SA 4.0*
