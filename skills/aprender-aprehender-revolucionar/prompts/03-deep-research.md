# Prompt #3 · Deep Research

> Investigación exhaustiva sobre un tema · genera material para cargar en NotebookLM como sources · diseñado para Workflow 2 (Explorador).

**Fase**: Aprender · refinamiento del Blueprint
**Workflow**: 2 (Explorador) · 4-20 horas
**IA recomendada**: Perplexity, Kimi, ChatGPT Plus, Claude · idealmente con búsqueda web

---

## Cuándo usarlo

- ✅ Después del Blueprint (Prompt #1), para profundizar
- ✅ Cuando necesitas material denso para cargar como source en NotebookLM
- ✅ Para temas donde la búsqueda web es valiosa (avances recientes)
- ✅ Modo Express del desatraso (4 horas para ponerse al día)

## Cuándo NO usarlo

- ❌ Si todavía no tienes Blueprint (Prompt #1 primero)
- ❌ Si solo quieres una definición rápida (sobre-ingeniería)

---

## Variables

| Variable | Reemplazar con |
|---|---|
| `[TU TEMA]` | Tema específico de research |
| `[SUBTEMA ESPECÍFICO]` | Aspecto particular a profundizar |
| `[CONTEXTO]` | Por qué necesitas saber esto |
| `[FECHA CORTE]` | Hasta qué fecha buscar (ej. "2026-04") |

---

## El Prompt

```
Eres un investigador con 20+ años en [TU TEMA].

Necesito un Deep Research sobre [SUBTEMA ESPECÍFICO] dentro de [TU TEMA].
Contexto: [CONTEXTO].
Cubre desde sus fundamentos hasta el estado del arte a [FECHA CORTE].

ESTRUCTURA REQUERIDA:

1. RESUMEN EJECUTIVO (250 palabras)
   - Qué es
   - Por qué importa hoy
   - Cuál es el debate principal

2. HISTORIA Y CONTEXTO
   - Cómo surgió (años, autores fundacionales, problema que resolvía)
   - Hitos clave en la evolución (5-7 con año + autor)
   - Estado actual: maduración o disrupción

3. FUNDAMENTOS CONCEPTUALES
   - Modelos teóricos centrales (con fórmulas/diagramas si aplica)
   - Vocabulario crítico (10-15 términos)
   - Premisas que asume el campo

4. ESTADO DEL ARTE 2024-2026
   - Avances de los últimos 24 meses
   - Papers seminales recientes (autor + año + enlace)
   - Productos / herramientas líderes
   - Capítulos abiertos sin consenso

5. APLICACIONES PRÁCTICAS
   - Casos de uso reales documentados (3-5)
   - Empresas que lo usan en producción
   - Métricas de éxito típicas
   - Trampas comunes en implementación

6. TRADE-OFFS Y DEBATES
   - Las 3 controversias más importantes
   - Argumentos de cada lado con evidencia
   - Tu evaluación: dónde está el consenso vs dónde no

7. RIESGOS Y LIMITACIONES
   - Qué NO resuelve este enfoque
   - Casos donde falla
   - Costos ocultos (técnicos, organizacionales, financieros)

8. FUTURO PROBABLE
   - Tendencias emergentes (3-5)
   - Disruptores potenciales
   - Skills que se volverán críticos / obsoletos

9. CHECKLIST DE LECTURA RECOMENDADA
   ORDEN DE PRIORIDAD para alguien con [CONTEXTO]:
   - 3 papers must-read (con razón por qué)
   - 2 libros must-read
   - 5 blogs / canales con autores expertos

REGLAS DE EXACTITUD:

- Cada cifra tiene fuente: [DOC: autor año] o [WEB: organización año]
- Si no estás 100% seguro de un dato, marca [VERIFICAR]
- Si una afirmación viene solo de tu entrenamiento (no de búsqueda
  reciente), marca [TRAINING DATA]
- Para cada autor mencionado, cita SU trabajo más relevante
- NO inventes papers · si no encuentras fuente verificable, dilo
- Para fechas precisas (ej. "publicado en marzo 2024"), valida
  contra tu búsqueda

ESTILO:

- Profesional pero accesible (no academia hermético)
- Sin marketing ni superlativos sin sustento
- Tablas comparativas cuando aplique (>2 alternativas)
- Diagramas mermaid si la relación lo amerita
- Idioma: español, citas en idioma original

LARGO ESPERADO: 3,000-5,000 palabras.
NO seas más breve. NO seas innecesariamente más largo.
```

---

## Workflow recomendado · Deep Research en 4 horas

```
HORA 1 · GENERACIÓN
- 0:00 Ejecutar Prompt #3 en Perplexity (con web search activo)
- 0:30 Ejecutar Prompt #3 en Claude
- 0:60 Ejecutar Prompt #3 en ChatGPT Plus

HORA 2 · CONSOLIDACIÓN
- 1:00 Comparar las 3 respuestas
- 1:30 Identificar discrepancias en hechos clave
- 1:45 Marcar áreas que necesitan validación

HORA 3 · FACT-CHECK
- 2:00 Ejecutar Prompt #4 en una 4ª IA (la más conservadora)
- 2:30 Verificar manualmente los items [VERIFICAR]
- 2:45 Crear tabla de triangulación

HORA 4 · NOTEBOOKLM
- 3:00 Crear notebook
- 3:15 Importar las 3 respuestas + tabla triangulación como sources
- 3:30 Configurar coach con Prompt #2
- 3:45 Primer test de 5 preguntas
```

Output: Notebook con 4-6 sources validadas + coach activo + base para Workflow 3.

---

## Variantes

### Express · 30 min
Solo ejecuta en 1 IA (la mejor para tu tema · Perplexity para temas con búsqueda web; Claude para análisis profundo).
Trade-off: pierdes triangulación. Solo si tiempo es crítico.

### Sprint · 4 horas (recomendado)
Workflow descrito arriba.

### Marathon · 20 horas
- Día 1: Deep Research en 3 IAs + consolidación
- Día 2: Fact-check + lectura de 3 papers fundacionales
- Día 3: 1 libro canónico (lectura activa, no skim)
- Día 4: Workflow 2 completo (concept map + glosario expandido)
- Día 5: Aprehensión inicial con NotebookLM

---

## Anti-patrones

| Error | Síntoma | Corrección |
|---|---|---|
| Solo 1 IA | Sesgo no detectado | Triangular siempre |
| Aceptar [TRAINING DATA] como current | Info de hace 2 años | Búsqueda web obligatoria si aplica |
| No verificar [VERIFICAR] | Citas inexistentes | Validar manualmente cada flag |
| Skim sin profundizar | "Leí el research" sin entender | Aplicar Feynman después |
| 1 sola fuente como source NotebookLM | Coach solo cita esa fuente | Mínimo 3 sources para diversidad |

---

## Validación

Después de un Deep Research bien ejecutado:

- [ ] 9 secciones completas, no resumidas
- [ ] Cifras con tag [DOC] / [WEB] / [VERIFICAR] / [TRAINING DATA]
- [ ] ≥3 papers con autor + año
- [ ] ≥2 libros recomendados
- [ ] Tabla de trade-offs si hay alternativas
- [ ] Diagrama mermaid si hay relaciones jerárquicas
- [ ] 3,000-5,000 palabras (no más, no menos)
- [ ] Triangulado en 3+ IAs (versión Sprint+)
- [ ] Fact-check con Prompt #4 ejecutado

Si tienes <6 marcas → vuelve a iterar.

---

## Combo con otros prompts

```
1. Prompt #1 (Blueprint)        → vista panorámica
2. Prompt #3 (Deep Research)    → profundidad
3. Prompt #4 (Fact-Check)       → verificación
4. Prompt #7 (Notebook Audit)   → calidad de sources
5. Prompt #2 (Coach)            → tutor activo
```

---

## Referencias

- `references/02-tres-modelos-fundacionales.md` §Body of Knowledge
- `prompts/04-cross-fact-check.md`
- `prompts/07-notebook-audit.md`
- `workflows/workflow-2-explorador.md`

---

> **Prompt #3** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
