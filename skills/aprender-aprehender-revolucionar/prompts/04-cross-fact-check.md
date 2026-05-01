# Prompt #4 · Cross Fact-Check (Detección de Hallucinations)

> Auditoría cruzada de un research/blueprint usando una IA #4 independiente. Detecta datos inventados, atribuciones erróneas, citas falsas.

**Fase**: cross-fase · post-research
**Cuándo**: después de Prompt #1 o Prompt #3
**IA recomendada**: la **más conservadora** disponible (Claude tiende a ser menos asertiva en datos sin evidencia · GPT-4 + búsqueda web también funciona)

---

## Cuándo usarlo

- ✅ Después de cualquier Deep Research o Blueprint
- ✅ Antes de citar datos en presentación pública (QBR, paper, pitch)
- ✅ Cuando un dato suena "demasiado preciso" o "demasiado conveniente"
- ✅ Como kata regular (`katas/kata-fuente-primaria.md`)

## Cuándo NO usarlo

- ❌ Para opiniones o frameworks (no hay "fuente primaria" para opiniones)
- ❌ Si el material a auditar no tiene afirmaciones factuales (todo conceptual)

---

## Variables

| Variable | Reemplazar con |
|---|---|
| `[CONTENIDO A AUDITAR]` | El research/blueprint completo (pegar al final) |
| `[DOMINIO]` | Tema del contenido (para context) |

---

## El Prompt

```
Eres un fact-checker académico riguroso especializado en [DOMINIO].
Tu único objetivo es detectar afirmaciones FALSAS, INVENTADAS o
INVERIFICABLES en el siguiente contenido. NO añades opiniones.
NO complementas con tu conocimiento. SOLO AUDITAS.

CONTENIDO A AUDITAR:
---
[CONTENIDO A AUDITAR]
---

PROTOCOLO DE AUDITORÍA

Para CADA afirmación factual del contenido (datos, estadísticas,
fechas, citas, autores, títulos de papers, ecuaciones), genera
una entrada con este formato:

CLAIM #N: [transcribir literal la afirmación]
TIPO: [DATO | FECHA | CITA | ATRIBUCIÓN | ECUACIÓN | ESTADÍSTICA]
VEREDICTO:
   [CONFIRMED]   — verifico que es cierto · cito fuente
   [DISCREPANT]  — fuentes contradicen entre sí · explico
   [PARTIAL]     — parcialmente cierto · explico el matiz
   [NO SOURCE]   — plausible pero no encuentro fuente verificable
   [HALLUCINATION] — falso · explico por qué
EVIDENCIA: [fuente primaria si CONFIRMED · explicación si otro]
NIVEL DE CONFIANZA: [ALTO · MEDIO · BAJO]

PRIORIDADES DE AUDITORÍA

Audita primero (riesgo más alto):
1. CITAS con autor + año + título → ¿el paper existe?
2. ESTADÍSTICAS precisas (ej. "73.5% de empresas") → ¿de qué reporte?
3. FECHAS específicas → ¿coinciden con tus fuentes?
4. ATRIBUCIONES (ej. "X propuso Y en Z año") → ¿correcto autor?
5. ECUACIONES → ¿signos, variables correctos?

Después audita (riesgo medio):
6. NOMBRES de personas/empresas/productos
7. RESULTADOS de experimentos citados
8. RANKINGS o comparativas

NO audites:
- Conceptos generales sin cifras
- Opiniones del autor
- Recomendaciones / consejos
- Frameworks (a menos que se atribuyan a alguien específico)

FORMATO DE OUTPUT

Después de auditar todas las claims, genera:

RESUMEN EJECUTIVO
- Total de claims auditadas: N
- CONFIRMED: X (X%)
- DISCREPANT: X (X%)
- PARTIAL: X (X%)
- NO SOURCE: X (X%)
- HALLUCINATION: X (X%)

CLAIMS CRÍTICAS (HALLUCINATION o NO SOURCE de alto impacto)
Lista los items más graves con recomendación:
- "Autor X propuso Y en 1985" → HALLUCINATION · el paper real es de 1995
- "73% de empresas reportan Z" → NO SOURCE · cifra inventada,
  no usar en QBR/paper

RECOMENDACIONES DE REMEDIACIÓN
1. Items que MUST eliminar (HALLUCINATION confirmados)
2. Items que MUST verificar manualmente (NO SOURCE críticos)
3. Items que pueden mantenerse con caveat ("según [fuente]...")

NIVEL GLOBAL DE CONFIANZA DEL CONTENIDO
[ALTO]   — <5% problemas · usar con confianza
[MEDIO]  — 5-15% problemas · revisar antes de citar públicamente
[BAJO]   — 15-30% problemas · re-hacer research crítico
[ROJO]   — >30% problemas · descartar y empezar de nuevo

REGLAS

- Si no puedes verificar algo, di [NO SOURCE], no inventes
- Si tu propio entrenamiento contradice una afirmación, NO la marques
  HALLUCINATION solo por eso · marca [DISCREPANT] y explica
- Para fechas, busca en tu data hasta tu fecha de corte
- Para papers, valida nombre + autor + año + revista
- Sé conservador: ante duda, [NO SOURCE] mejor que falso confirmado
```

---

## Cómo aplicarlo

### Paso 1 · Preparar contenido
Toma el output de Prompt #1 (Blueprint) o Prompt #3 (Deep Research).
Si es muy largo (>10K caracteres), divídelo en secciones y audita por partes.

### Paso 2 · IA distinta a las que generaron
Si usaste ChatGPT + Claude + Gemini para el research, usa una **4ª IA** distinta para fact-check:
- Perplexity (con búsqueda web)
- Kimi (con su corpus)
- O incluso modelo distinto de la misma plataforma (e.g., Claude Opus si usaste Claude Sonnet)

### Paso 3 · Pegar y ejecutar
Reemplaza `[CONTENIDO A AUDITAR]` con tu contenido. `[DOMINIO]` con el tema.

### Paso 4 · Procesar resultado
- Items HALLUCINATION → eliminar
- Items NO SOURCE → verificar manualmente o eliminar
- Items DISCREPANT → investigar y decidir

---

## Output esperado · Ejemplo

```
RESUMEN EJECUTIVO
- Total claims auditadas: 23
- CONFIRMED: 15 (65%)
- DISCREPANT: 2 (9%)
- PARTIAL: 1 (4%)
- NO SOURCE: 4 (17%)
- HALLUCINATION: 1 (4%)

CLAIMS CRÍTICAS

CLAIM #7: "Smith propuso CAP theorem en 1998"
TIPO: ATRIBUCIÓN + FECHA
VEREDICTO: [HALLUCINATION]
EVIDENCIA: CAP fue propuesto por Eric BREWER en 2000 (PODC keynote).
Smith no es el autor. Año correcto: 2000, no 1998.
NIVEL DE CONFIANZA: ALTO
RECOMENDACIÓN: Eliminar y reemplazar:
"Brewer propuso CAP theorem en 2000 (Brewer, 2000)"

CLAIM #14: "73.5% de las empresas adoptan microservicios"
TIPO: ESTADÍSTICA
VEREDICTO: [NO SOURCE]
EVIDENCIA: No encuentro fuente primaria de esta cifra precisa.
Hay reportes (e.g., O'Reilly Microservices Adoption 2020)
con cifras similares pero no exactamente 73.5%.
RECOMENDACIÓN: Reemplazar con:
"Encuestas industriales reportan adopción >70% en empresas
medianas-grandes (O'Reilly, 2020)"

NIVEL GLOBAL DE CONFIANZA: MEDIO
- 1 hallucination + 4 no-source = 22% problemas
- No usar este research en QBR/paper sin remediar primero
- Tras remediación, debería pasar a ALTO
```

---

## Combo recomendado

```
SECUENCIA DE FACT-CHECK ROBUSTA:

DÍA 1 · GENERACIÓN
- Prompt #1 en ChatGPT
- Prompt #1 en Claude
- Prompt #1 en Gemini
- Prompt #3 en Perplexity (con búsqueda)

DÍA 2 · CONSOLIDACIÓN
- Compilar las 4 respuestas en 1 documento

DÍA 3 · FACT-CHECK CRUZADO
- Prompt #4 en una 5ª IA (la más conservadora)
- Identificar HALLUCINATIONS y NO SOURCE críticos

DÍA 4 · REMEDIACIÓN
- Eliminar HALLUCINATIONS
- Verificar NO SOURCE críticos manualmente (Google Scholar, papers originales)
- Refinar el documento consolidado

DÍA 5 · USO
- Material limpio listo para NotebookLM, presentación, paper

TOTAL: 1 semana para Deep Research nivel publication-grade
```

---

## Anti-patrones

| Error | Síntoma | Corrección |
|---|---|---|
| Auditar con la misma IA que generó | Confirmation bias | IA distinta obligatoriamente |
| Saltar fact-check porque "Claude no inventa" | Aún así tiene blindspots | Ningún modelo es 100% libre de hallucination |
| Auditar opiniones | Sin sentido (no hay fuente) | Solo audita afirmaciones factuales |
| Aceptar [PARTIAL] sin investigar | Caveat oculto se convierte en error | Trata [PARTIAL] como [VERIFICAR] manual |
| Confiar 100% en un solo fact-check | Aún la auditora puede equivocarse | Cross-check con fuente primaria si critical |

---

## Validación

Tu fact-check está bien si:

- [ ] Cada claim audita TIENE veredicto explícito
- [ ] HALLUCINATIONS identificadas tienen explicación
- [ ] NO SOURCE separadas de DISCREPANT (semánticamente distintos)
- [ ] Resumen ejecutivo con %
- [ ] Recomendaciones de remediación accionables
- [ ] Nivel global de confianza calibrado

Si la auditora dice "todo está perfecto, 100% CONFIRMED" en un research de 50 claims sobre tema avanzado → sospechoso. **Probablemente la auditora es sycophant**. Cambia de IA.

---

## Sustento académico

→ ver `references/06-ciencia-cognitiva-fuentes.md` §10 (IA Hallucinations).

> *"La hallucination más peligrosa es la que suena académica."*
> Survey of Hallucination in NLG (Ji et al., 2023)

---

## Referencias

- `references/04-anti-patrones-y-trampas.md` §2 (Hallucination), §3 (Sycophancy)
- `katas/kata-fuente-primaria.md`
- `katas/kata-triangulacion-3ias.md`

---

> **Prompt #4** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0
