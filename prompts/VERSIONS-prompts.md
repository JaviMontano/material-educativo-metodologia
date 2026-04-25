# Prompts MetodologIA · Registro de versiones

> Bitácora de la biblioteca de prompts ejecutables MetodologIA.
> Cada prompt se publica en dos variantes: **Simple** (no trivial, accesible) y **Metodológicos** (para practicantes con familiaridad en el corpus).
> Naming convention: `prompt-{slug}-{simple|metodologicos}-v{YYYY.MM}.md`

---

## v2026.04 · 24 abr 2026 · Feynman Explicar

**Estado:** Vigente · publicable.

| Variante | Archivo | Tamaño | Audiencia |
|---|---|---|---|
| **Simple** | `prompt-feynman-explicar-simple-v2026.04.md` | ~3 KB | Cualquiera con un asistente de IA, sin contexto previo de MetodologIA. |
| **Metodológicos** | `prompt-feynman-explicar-metodologicos-v2026.04.md` | ~12 KB | Practicantes MetodologIA familiarizados con SPEC, KEY FACTS, tags de evidencia, Protocolo Interpreta-Planifica-Ejecuta. |

### Origen

Refactor del prompt original Feynman publicado en el corpus interno. La revisión identificó que el prompt original tenía buena intención metodológica pero opacidad operativa: usaba tecnicismos (`SPEC`, `VACÍO CRÍTICO`, `KEY FACTS`, `Cláusula Sensorial`) sin definirlos, mezclaba variables sin especificar tipos, y declaraba el Bucle de Excelencia sin rúbrica medible.

### Aportes de la variante Simple

- Estructura mínima funcional: 1 entrada (`[CONCEPTO]`) y 6 pasos.
- Cero scaffolding metodológico explícito.
- Las 3 variaciones opcionales al final cubren los usos más frecuentes.
- Apto para ser pegado en cualquier asistente sin contexto.

### Aportes de la variante Metodológicos respecto al prompt anterior

- **Glosario operativo** de 8 términos al inicio (SPEC, VACÍO CRÍTICO, KEY FACTS, Cláusula Sensorial, Protocolo MetodologIA, Bucle de Excelencia, tags de evidencia, Viaje del Ritual S5).
- **Mapping explícito** de los 3 niveles Feynman (12 años / colega / experto) con el **Viaje del Ritual del playbook S5** (Práctica Personal → Consolidación → Procedimiento Amplificado).
- **Tags de evidencia** `[CÓDIGO][DOC][INFERENCIA][SUPUESTO]` integrados como instrucción operativa.
- **Rúbrica del Bucle de Excelencia** con 10 criterios y definición verificable de "10/10" para cada uno.
- **Insumos opcionales** (`CONTEXTO_USO`, `AUDIENCIA_REAL`) calibran el tono sin obligar al usuario.
- **Output formal de 10 elementos** en orden predecible y auditable.
- **Banner de advertencia** automático si > 30% de las afirmaciones son `[SUPUESTO]`.
- **Checklist de cierre** de 8 ítems verificable por el modelo.
- **Ejemplo de uso** documentado fuera del prompt para acelerar adopción.
- **Sección de anti-patrones** del practicante.
- **Bloque de trazabilidad y créditos** que enlaza explícitamente con el playbook S5 y atribuye Feynman.

---

## Convenciones

- **Versionado:** `vYYYY.MM` para cambios mayores; `vYYYY.MM.PATCH` para correcciones.
- **Brand lock:** todos los prompts en este directorio son MetodologIA. Cero contaminación con otras marcas (regla CLAUDE.md).
- **Bilingüe (futuro):** los próximos prompts se publicarán en ES por defecto y EN como variante separada `-en-`.
- **Doble variante obligatoria:** todo prompt nuevo se publica en Simple + Metodológicos. La variante Simple existe para no excluir a quien aún no domina el lenguaje MetodologIA.
- **Trazabilidad:** cada prompt declara qué playbook MetodologIA u obra externa lo inspira.

---

## Próximos prompts candidatos (no creados aún)

- `prompt-spec-driven-design-{simple|metodologicos}-vX.md` — escribir specs ejecutables para iniciativas técnicas.
- `prompt-pareto-prioritizer-{simple|metodologicos}-vX.md` — encontrar el 20% que entrega el 80% del valor.
- `prompt-five-whys-{simple|metodologicos}-vX.md` — análisis de causa raíz disciplinado.
- `prompt-rat-designer-{simple|metodologicos}-vX.md` — diseñar Riskiest Assumption Tests para validar hipótesis críticas.
- `prompt-mvp-scoper-{simple|metodologicos}-vX.md` — acotar el alcance mínimo viable de una iniciativa.

---

*Construido por profesionales · Human First, AI-Next · Por Javier Montaño · metodologia.info · CC BY-NC-SA 4.0*
