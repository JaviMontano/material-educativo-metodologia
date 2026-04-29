# Cartilla universal de prompting v1.0 · 2026-04-29

## Decisión de diseño
- Single-file HTML self-contained · 126.4 KB
- Branding heredado de biblioteca-universal-prompting-2026.html
- Bilingual ES/EN · profesional adulto
- Storytelling-first híbrido (decisión Javier)

## Arquitectura · 11 secciones (+ Hero)

| § | Sección | Bloque |
|---:|---|---|
| 0 | Hero + CTAs | promesa concreta |
| 1 | Storytelling | dolores → motivadores → soberanía digital y de IA |
| 2 | 8 atributos | sistemático · sin fricción · replicable · portable · metacognitivo · auditable · orquestado · insight-oriented |
| 3 | Pipeline P.I.V.O.T.E. | 10 capítulos colapsables /0-/9 |
| 4 | 12 cláusulas | 9 v3.3 + 3 nuevas v3.4 (EVIDENCIA_CITAS · NO_ALUCINACIÓN · INFERENCIA_VS_HECHO) |
| 5 | Rubricario ENTRUSTED+ | 8 ejes auditables |
| 6 | 10 etiquetas | sistema de procedencia |
| 7 | DSV | DECOMPOSE → SOLVE → VERIFY → SYNTHESIZE → REFLECT |
| 8 | 12 prácticas | 3 min · 30 min · 60 min · sesión completa |
| 9 | 30 prompts curados | gallery clickeable + modal · embed JSON |
| 10 | 3 espacios práctica | ritual matutino · semanal · mensual |
| 11 | Footer 2 salidas | estudiante · receptor |

## Branding inline (CSS variables canónicas v3.4)

```css
--navy:#122562 · --gold:#FFD700 · --blue:#137DC5 · --lilac:#BAA0CC
Poppins (heads) · Montserrat (body) · Trebuchet (labels) · Courier (mono)
```

## Funcionalidad

- Toggle ES/EN persistente (localStorage)
- Toggle theme light/dark persistente
- Reading bar gold gradient
- Reveal stagger por sección (IntersectionObserver)
- Back-to-top
- Modal con SPEC compacto de cualquier prompt curado
- Accordions <details> nativos en pipeline
- prefers-reduced-motion respetado

## 30 prompts curados embebidos

- Pipeline /0-/9 (10)
- Frameworks: SWOT · Porter · Lean Canvas · OKR · BCG (5)
- Aceleradores: a · e · s · simplifica · estructura (5)
- Macros: documenta · empatiza · investiga · prioriza · compara (5)
- COP: AUT_01 · EXC_01 · PBI_01 · PRD_01 · STU_01 (5)

## Definition of Done v1.0
- [x] Single-file HTML self-contained
- [x] Tamaño 126.4 KB (target 1.5-3 MB · cumple con margen)
- [x] Toggle ES/EN funcional
- [x] Light/dark mode
- [x] Reading bar + back-to-top
- [x] 11 secciones completas
- [x] Branding canónico v3.4 heredado
- [x] 30 prompts curados con modal
- [x] Footer 2 salidas (estudiante / receptor)
- [x] prefers-reduced-motion respetado
- [x] Brand voice: cero "arquitecto" / cero "hack" / informa-inspira
- [ ] Push al repo `material-educativo-metodologia` (siguiente paso)
