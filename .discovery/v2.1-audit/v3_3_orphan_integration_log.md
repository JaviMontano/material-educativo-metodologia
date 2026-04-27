# Orphan integration log v3.3 — 2026-04-26

Para cada prompt con tokens declarados-pero-no-usados, se insertó un paso explícito en EJECUCIÓN que integra cada token con su propósito derivado.

| Prompt ID | Tokens integrados | Heurística |
|---|---|---|
| `/demo_combinar_imagenes_publicitaria` | `fondo`(A), `mensaje`(A), `producto`(A) | A |
| `/demo_crear_imagen_desde_input` | `descripcion`(A), `estilo`(A), `formato`(A) | A |
| `/demo_imagen_a_video` | `accion`(A), `duracion`(A), `imagen_descripcion`(B) | B,A |
| `/demo_juego_culebrita` | `estilo`(A), `logica`(A), `tipo_app`(A) | A |
| `/demo_presentacion_tema_actualidad` | `audiencia`(A), `enfoque`(A), `tema`(A) | A |
| `/COP_AUT_01` | `disparador`(A), `nombre`(A) | A |
| `/COP_AUT_02` | `aprobador`(A), `tema`(A) | A |
| `/COP_AUT_03` | `estructura`(A), `schema`(A) | A |
| `/COP_AUT_04` | `accion`(A), `politica`(A) | A |
| `/COP_AUT_05` | `coleccion`(A), `proceso`(A) | A |
| `/COP_AUT_06` | `archivo`(B), `destinatario`(B) | B |
| `/COP_AUT_07` | `accion`(A), `lista`(A) | A |
| `/COP_AUT_08` | `adaptive_card`(B), `channel`(B) | B |
| `/COP_AUT_09` | `nombre`(A), `valor`(B) | B,A |
| `/COP_AUT_10` | `recurrencia`(B), `tarea`(A) | A,B |
| `/COP_AUT_11` | `nombre`(A), `pantalla`(B) | B,A |
| `/COP_AUT_12` | `diseno`(B), `fuente`(B) | B |
| `/COP_AUT_13` | `data_source`(B), `modo`(B) | B |
| `/COP_AUT_14` | `datos`(A), `record`(B) | B,A |
| `/COP_AUT_15` | `datos`(A), `nombre_coll`(B) | B,A |
| `/COP_AUT_16` | `params`(B), `target`(B) | B |
| `/COP_AUT_17` | `colores`(B), `componente`(B) | B |
| `/COP_AUT_18` | `conector`(B), `tipo`(A) | A,B |
| `/COP_AUT_19` | `query`(B), `termino`(B) | B |
| `/COP_AUT_20` | `captura`(B), `storage`(B) | B |
| `/COP_AUT_21` | `desktop_task`(B), `ui_elemento`(B) | B |
| `/COP_AUT_22` | `lenguaje`(B), `pasos`(B) | B |
| `/COP_AUT_23` | `documento`(A), `modelo`(B) | B,A |
| `/COP_AUT_24` | `tabla`(B), `tipo_col`(B) | B |
| `/COP_AUT_25` | `dlp`(B), `env`(B) | B |
| `/COP_EXC_01` | `kpi`(A), `tabla`(B) | B,A |
| `/COP_EXC_02` | `criterio`(A), `rango`(B) | B,A |
| `/COP_EXC_03` | `datos`(A), `ventana`(B) | B,A |
| `/COP_EXC_04` | `matriz`(B), `variable`(B) | B |
| `/COP_EXC_05` | `formato`(A), `query`(B) | B,A |
| `/COP_EXC_06` | `segmento`(B), `valores`(B) | B |
| `/COP_EXC_07` | `busqueda`(B), `codigo`(B) | B |
| `/COP_EXC_08` | `escenario`(B), `sensibilidad`(B) | B |
| `/COP_EXC_09` | `estilo`(A), `regla`(B) | B,A |
| `/COP_EXC_10` | `error`(B), `formula`(B) | B |
| `/COP_EXC_11` | `dashboard`(B), `fuente`(B) | B |
| `/COP_EXC_12` | `filtro`(B), `tabla`(B) | B |
| `/COP_EXC_13` | `proteccion`(B), `usuario`(B) | B |
| `/COP_EXC_14` | `macro`(B), `trigger`(A) | A,B |
| `/COP_EXC_15` | `insights`(B), `tipo`(A) | A,B |
| `/COP_EXC_16` | `logica`(A), `rango`(B) | B,A |
| `/COP_EXC_17` | `anio`(B), `variacion`(B) | B |
| `/COP_EXC_18` | `punto_reorden`(B), `stock`(B) | B |
| `/COP_EXC_19` | `form`(B), `tipo`(A) | A,B |
| `/COP_EXC_20` | `archivos`(B), `master`(B) | B |
| `/COP_EXC_21` | `hitos`(B), `mes`(B) | B |
| `/COP_EXC_22` | `empleados`(B), `novedades`(B) | B |
| `/COP_EXC_23` | `data`(B), `perfil`(B) | B |
| `/COP_EXC_24` | `calculo`(B), `digitos`(B) | B |
| `/COP_EXC_25` | `formato`(A), `tema`(A) | A |
| `/COP_PBI_01` | `granularidad`(C), `metrica`(B), `modelo`(B) | B,C |
| `/COP_PBI_02` | `dominio`(B), `tablas`(B), `volumen`(A) | A,B |
| `/COP_PBI_03` | `audiencia`(A), `decision`(A), `marca`(A) | A |
| `/COP_PBI_04` | `dimensiones`(B), `metricas`(A), `visuales`(B) | A,B |
| `/COP_PBI_05` | `modo`(B), `reglas`(B), `roles`(B) | B |
| `/COP_PBI_06` | `origen`(B), `query`(B), `tamano`(A) | A,B |
| `/COP_PBI_07` | `origen`(B), `politica`(A), `tabla`(B) | A,B |
| `/COP_PBI_08` | `logica`(A), `origen_dim`(B), `uso`(B) | B,A |
| `/COP_PBI_09` | `audiencia`(A), `jerarquia`(B), `visual_base`(B) | B,A |
| `/COP_PBI_10` | `contexto`(A), `estilo`(A), `visual`(B) | B,A |
| `/COP_PBI_11` | `marca`(A), `modo`(B), `visuales`(B) | B,A |
| `/COP_PBI_12` | `audiencia`(A), `sla`(B), `workspace`(B) | B,A |
| `/COP_PBI_13` | `historia`(B), `trigger`(A), `visuales`(B) | A,B |
| `/COP_PBI_14` | `modelo`(B), `preguntas`(A), `sinonimos`(B) | A,B |
| `/COP_PBI_15` | `cadencia`(B), `estrategia`(B), `perspectivas`(B) | B |
| `/COP_PBI_16` | `dataset`(B), `pregunta`(B), `tipo`(A) | A,B |
| `/COP_PBI_17` | `analisis`(B), `geo_data`(B), `plataforma`(B) | B |
| `/COP_PBI_18` | `fuentes`(A), `modo`(B), `restricciones`(A) | B,A |
| `/COP_PBI_19` | `hero`(B), `marca`(A), `plataformas`(B) | A,B |
| `/COP_PBI_20` | `dataset_master`(B), `politica`(A), `reportes`(B) | A,B |
| `/COP_PRD_01` | `audiencia`(A), `extension`(B), `tipo`(A), `tono`(A) | B,A |
| `/COP_PRD_02` | `formato`(A), `fuentes`(A), `pregunta`(B) | B,A |
| `/COP_PRD_03` | `marca`(A), `secciones`(B), `tipo`(A) | B,A |
| `/COP_PRD_04` | `nivel`(B), `texto`(B), `variante`(B) | B |
| `/COP_PRD_05` | `datos`(A), `formato`(A), `objetivo`(A) | A |
| `/COP_PRD_06` | `hilo`(B), `objetivo`(A), `tono`(A) | A,B |
| `/COP_PRD_07` | `foco`(B), `hilo`(B) | B |
| `/COP_PRD_08` | `duracion`(A), `participantes`(B), `restricciones`(A) | B,A |
| `/COP_PRD_09` | `audiencia`(A), `borrador`(A), `objetivo`(A) | A |
| `/COP_PRD_10` | `compromisos`(B), `periodicidad`(B), `proyecto`(A) | A,B |
| `/COP_PRD_11` | `audiencia`(A), `estructura`(A), `transcripcion`(B) | B,A |
| `/COP_PRD_12` | `minuta`(B), `sistema`(B) | B |
| `/COP_PRD_13` | `canal`(B), `foco`(B), `periodo`(B) | B |
| `/COP_PRD_14` | `alcance`(A), `filtros`(B), `pregunta`(B) | B,A |
| `/COP_PRD_15` | `duracion`(A), `objetivo`(A), `participantes`(B) | B,A |
| `/COP_PRD_16` | `audiencia`(A), `duracion`(A), `tema`(A) | A |
| `/COP_PRD_17` | `cantidad`(B), `estilo`(A), `word_doc`(B) | A,B |
| `/COP_PRD_18` | `concepto`(A), `estilo`(A), `marca`(A) | A |
| `/COP_PRD_19` | `audiencia`(A), `mensaje`(A), `tiempo`(B) | B,A |
| `/COP_PRD_20` | `duracion`(A), `estilo`(A), `slides`(B) | B,A |
| `/COP_PRD_21` | `cuaderno`(B), `estructura`(A) | A,B |
| `/COP_PRD_22` | `cadencia`(B), `plantilla`(B), `proyecto`(A) | A,B |
| `/COP_PRD_23` | `horizonte`(B), `marco`(A), `tareas`(B) | A,B |
| `/COP_PRD_24` | `audiencia`(A), `objetivo`(A), `preguntas`(A) | A |
| `/COP_PRD_25` | `caso`(A), `componentes`(B), `equipo`(A) | B,A |
| `/COP_STU_01` | `caso`(A), `intenciones`(B), `tono`(A) | B,A |
| `/COP_STU_02` | `datos`(A), `topico`(B), `validaciones`(B) | B,A |
| `/COP_STU_03` | `persona`(A), `tono`(A), `vetados`(B) | B,A |
| `/COP_STU_04` | `logica`(A), `topico`(B), `variables`(B) | B,A |
| `/COP_STU_05` | `actualizacion`(B), `casos`(B), `fuentes`(A) | A,B |
| `/COP_STU_06` | `caso`(A), `modelo`(B), `plugin`(B) | B,A |
| `/COP_STU_07` | `canal`(B), `fallos`(B), `topico`(B) | B |
| `/COP_STU_08` | `agente`(A), `casos`(B), `metricas`(A) | B,A |
| `/COP_STU_09` | `agente`(A), `metricas`(A), `objetivo`(A) | A |
| `/COP_STU_10` | `agente`(A), `idiomas`(B), `politica`(A) | B,A |
| `/COP_STU_11` | `agente`(A), `canales`(B), `publico`(A) | B,A |
| `/COP_STU_12` | `fuentes`(A), `restricciones`(A), `topico`(B) | B,A |
| `/COP_STU_13` | `iteraciones`(B), `salida`(B), `topico`(B) | B |
| `/COP_STU_14` | `api`(B), `auth`(B), `caso`(A) | A,B |
| `/COP_STU_15` | `agente`(A), `objetivo`(A), `sintomas`(B) | B,A |
| `/COP_MGT_01` | `proyecto`(A), `restricciones`(A), `stakeholders`(A) | A |
| `/COP_MGT_02` | `apetito`(B), `proyecto`(A), `riesgos`(A) | A,B |
| `/COP_MGT_03` | `audiencia`(A), `cadencia`(B), `proyecto`(A) | B,A |
| `/COP_MGT_04` | `estrategia`(B), `proyecto`(A), `stakeholders`(A) | A,B |
| `/COP_MGT_05` | `granularidad`(B), `niveles`(B), `proyecto`(A) | A,B |
| `/COP_MGT_06` | `recursos`(B), `restricciones`(A), `wbs`(B) | A,B |
| `/COP_MGT_07` | `proyecto`(A), `recursos`(B), `sobreasignaciones`(B) | B,A |
| `/COP_MGT_08` | `datos`(A), `periodo`(B), `proyecto`(A) | B,A |
| `/COP_MGT_09` | `estandares`(B), `procesos`(B), `proyecto`(A) | A,B |
| `/COP_MGT_10` | `equipo`(A), `foco`(B), `proyecto`(A) | B,A |
| `/COP_MGT_11` | `dolor`(B), `equipo`(A), `framework`(A) | A,B |
| `/COP_MGT_12` | `areas`(B), `cambio`(B), `proyecto`(A) | A,B |
| `/COP_MGT_13` | `cadencia`(B), `equipo`(A), `modalidad`(B) | A,B |
| `/COP_MGT_14` | `criterios`(A), `modelo`(B), `necesidad`(B) | B,A |
| `/COP_MGT_15` | `audiencia`(A), `kpis`(A), `proyecto`(A) | A |
| `/v11_0` | `ADJUNTOS`(A), `PROBLEMA`(A) | A |
| `/v11_1` | `CRITERIO_DE_EXITO`(C), `PARA_QUE`(C), `PARA_QUIEN`(C), `RETO_O_TAREA`(A) | A,C |
| `/v11_2` | `CONTEXTO`(A), `ENTREGABLE`(B), `RESTRICCIONES`(A), `RETO_O_TAREA`(A) | B,A |
| `/v11_3` | `DEPENDENCIAS`(B), `RETO_O_TAREA`(A), `RIESGOS`(A), `SPEC_APROBADO`(C) | A,B,C |
| `/v11_4` | `INSUMOS`(C), `PENDIENTE`(A), `PLAN_APROBADO`(C), `RETO_O_TAREA`(A), `SPEC_APROBADO`(C), `VERIFICAR`(A) | A,C |
| `/v11_5` | `BORRADOR_ACTUAL`(A), `FUENTES_DISPONIBLES`(A), `PENDIENTE`(A), `RETO_O_TAREA`(A), `VACIOS_CRITICOS`(A), `VERIFICAR`(A) | A |
| `/v11_6` | `AUDIENCIA_DESTINO`(C), `LONGITUD_OBJETIVO`(C), `RETO_O_TAREA`(A), `VERSION_ROBUSTA`(C) | A,C |
| `/v11_7` | `CHECKLIST`(C), `CRITERIO_DE_ACEPTACION`(C), `ENTREGABLE`(B), `RETO_O_TAREA`(A) | A,B,C |
| `/v11_8` | `AUDIENCIA`(A), `ENTREGABLE_VALIDADO`(C), `FORMATO_FINAL`(C), `RETO_O_TAREA`(A) | A,C |
| `/v11_9` | `FORMATO_DESTINO`(C), `HISTORIAL_DE_SESION`(C), `REGLAS_REUSABLES`(C), `RETO_O_TAREA`(A) | A,C |
| `/v11_a` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_b` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_c` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_d` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_e` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_f` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_g` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_h` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_i` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_j` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_k` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_l` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_m` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_n` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_o` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_p` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_q` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_r` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_s` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_t` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_u` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_v` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_w` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_x` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_y` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_z` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_ñ` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v11_compara` | `OPCIONES`(B) | B |
| `/v11_prioriza` | `ITEMS`(A) | A |
| `/v11_reformula` | `AUDIENCIA`(A) | A |
| `/v11_debate` | `TEMA`(A) | A |
| `/v11_investiga` | `FUENTE`(B), `TEMA`(A) | A,B |
| `/v11_documenta` | `CONTENIDO`(B) | B |
| `/v11_diagrama` | `CONCEPTO`(A) | A |
| `/v11_evalua` | `OBJETO`(B) | B |
| `/v11_optimiza` | `PROCESO`(A) | A |
| `/v11_automatiza` | `PROCESO`(A) | A |
| `/v11_desafia` | `PROPUESTA`(B) | B |
| `/v11_calibra` | `AUDIENCIA`(A) | A |
| `/v11_resume` | `CONTENIDO`(B) | B |
| `/v11_traduce` | `IDIOMA`(A) | A |
| `/v11_profundiza` | `TEMA`(A) | A |
| `/v11_simplifica` | `CONTENIDO`(B) | B |
| `/v11_contextualiza` | `TEMA`(A) | A |
| `/v11_cuantifica` | `TEMA`(A) | A |
| `/v11_visualiza` | `DATOS`(A) | A |
| `/v11_personaliza` | `ROL`(A), `SECTOR`(A) | A |
| `/v11_estructura` | `CONTENIDO`(B) | B |
| `/v11_argumenta` | `TESIS`(B) | B |
| `/v11_predice` | `SITUACION`(A) | A |
| `/v11_mapea` | `CONCEPTO`(A) | A |
| `/v11_pareto` | `LISTA`(A) | A |
| `/v11_verifica` | `TEMA`(A) | A |
| `/v11_operacionaliza` | `PLAN`(B) | B |
| `/v11_sintetiza` | `TEMA`(A) | A |
| `/v11_segmenta` | `PROYECTO`(A) | A |
| `/v11_escenarios` | `SITUACION`(A) | A |
| `/v11_prototipa` | `IDEA`(B) | B |
| `/v11_escala` | `SOLUCION`(B) | B |
| `/v11_aterriza` | `TEMA`(A) | A |
| `/v11_conecta` | `CONCEPTO_A`(B), `CONCEPTO_B`(B) | B |
| `/v11_auditoria` | `OBJETO`(B) | B |
| `/v11_narrativa` | `DATOS`(A) | A |
| `/v11_benchmark` | `METRICA`(B), `SECTOR`(A) | A,B |
| `/v11_diagnostica` | `SITUACION`(A) | A |
| `/v11_estrategia` | `OBJETIVO`(A) | A |
| `/v11_feedback` | `COMPORTAMIENTO`(B) | B |
| `/v11_reversa` | `TEMA_SESION`(B) | B |
| `/v11_defiende` | `POSICION`(B) | B |
| `/v11_empatiza` | `PERSONA`(A) | A |
| `/v11_productividad_disenar_ritual_matutino` | `ADJUNTOS`(A), `ENERGIA_ACTUAL`(C), `HORA_DESPERTAR`(C), `PROFESION`(C) | A,C |
| `/v11_productividad_auditar_tiempo_semanal` | `ACTIVIDADES`(C), `ADJUNTOS`(A), `HORAS_TRABAJO`(C), `OBJETIVO`(A) | A,C |
| `/v11_productividad_sistema_captura_inbox_cero` | `ADJUNTOS`(A), `HERRAMIENTAS`(A), `VOLUMEN`(A) | A |
| `/v11_productividad_calcular_roi_personal` | `ADJUNTOS`(A), `HORAS_SEMANALES`(C), `INICIATIVA`(C), `VALOR_HORA`(C) | A,C |
| `/v11_productividad_disenar_sistema_habitos` | `ADJUNTOS`(A), `HABITOS_ACTUALES`(C), `OBJETIVO`(A), `TIEMPO_DIARIO`(C) | A,C |
| `/v11_productividad_optimizar_entorno_digital` | `ADJUNTOS`(A), `DISPOSITIVO`(C), `FRUSTRACIONES`(C), `HERRAMIENTAS`(A) | A,C |
| `/v11_productividad_energia_no_tiempo` | `ADJUNTOS`(A), `AGENDA_ACTUAL`(C), `CRONOTIPO`(C), `TAREAS_CRITICAS`(C) | A,C |
| `/v11_productividad_weekly_review_sistema` | `ADJUNTOS`(A), `HERRAMIENTAS`(A), `OBJETIVOS_TRIMESTRE`(C) | A,C |
| `/v11_productividad_deep_work_protocolo` | `ADJUNTOS`(A), `CONTEXTO`(A), `HORAS_DW_ACTUAL`(C), `INTERRUPCIONES`(C) | A,C |
| `/v11_productividad_decision_rapida_framework` | `ADJUNTOS`(A), `CONTEXTO`(A), `DECISION_EJEMPLO`(C) | A,C |
| `/v11_productividad_delegar_tarea_efectivamente` | `ADJUNTOS`(A), `EXPERIENCIA`(C), `RECEPTOR`(C), `TAREA`(A) | A,C |
| `/v11_productividad_reducir_reuniones_50` | `ADJUNTOS`(A), `REUNIONES`(B), `ROL`(A) | B,A |
| `/v11_productividad_email_cero_friccion` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `RESPUESTAS_COMUNES`(C), `VOLUMEN`(A) | A,C |
| `/v11_productividad_shutdown_ritual_cierre` | `ADJUNTOS`(A), `HERRAMIENTAS`(A), `HORA_CIERRE`(C) | A,C |
| `/v11_productividad_sprint_personal_semanal` | `ADJUNTOS`(A), `CONTEXTO`(A), `OBJETIVO_SEMANA`(C) | A,C |
| `/v11_productividad_batch_processing_tareas` | `ADJUNTOS`(A), `HORARIO`(C), `TAREAS_RECURRENTES`(C) | A,C |
| `/v11_productividad_brain_dump_estructurado` | `ADJUNTOS`(A), `CONTEXTO`(A), `HERRAMIENTAS`(A) | A |
| `/v11_productividad_kanban_personal_flujo` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `ROL`(A) | A |
| `/v11_productividad_friction_audit_eliminar` | `ADJUNTOS`(A), `CONTEXTO`(A), `FRUSTRACIONES`(C) | A,C |
| `/v11_productividad_template_system_entregables` | `ADJUNTOS`(A), `ENTREGABLES`(B), `HERRAMIENTAS`(A) | B,A |
| `/v11_productividad_accountability_system` | `ADJUNTOS`(A), `HORIZONTE`(C), `OBJETIVOS`(A) | A,C |
| `/v11_productividad_context_switching_minimizar` | `ADJUNTOS`(A), `ENTORNO`(C), `HERRAMIENTAS`(A), `INTERRUPCIONES`(C) | A,C |
| `/v11_productividad_procrastinacion_protocolo` | `ADJUNTOS`(A), `TAREA`(A), `TIEMPO_BLOQUEADO`(C) | A,C |
| `/v11_productividad_meeting_note_to_action` | `ADJUNTOS`(A), `NOTAS`(C), `PARTICIPANTES`(C) | A,C |
| `/v11_productividad_pomodoro_avanzado_personalizado` | `ADJUNTOS`(A), `ATENCION_ACTUAL`(C), `TIPO_TRABAJO`(C) | A,C |
| `/v11_productividad_morning_planning_5min` | `ADJUNTOS`(A), `HERRAMIENTAS`(A), `HORA`(C) | A,C |
| `/v11_productividad_async_communication_protocol` | `ADJUNTOS`(A), `EQUIPO`(A), `HERRAMIENTAS`(A), `ZONA_HORARIA`(C) | A,C |
| `/v11_productividad_energia_mapping_semanal` | `ADJUNTOS`(A), `HORARIO`(C), `TIPO_TRABAJO`(C) | A,C |
| `/v11_pensamiento_piramide_minto_estructura` | `ADJUNTOS`(A), `AUDIENCIA`(A), `FORMATO`(A), `TEMA`(A) | A |
| `/v11_pensamiento_issue_tree_problema` | `ADJUNTOS`(A), `CONTEXTO`(A), `PROBLEMA`(A), `PROFUNDIDAD`(C) | A,C |
| `/v11_pensamiento_primeros_principios` | `ADJUNTOS`(A), `INDUSTRIA`(A), `SUPOSICION`(C) | A,C |
| `/v11_pensamiento_modelos_mentales_latticework` | `ADJUNTOS`(A), `DOMINIO`(C), `SITUACION`(A) | A,C |
| `/v11_pensamiento_socratico_examinar` | `ADJUNTOS`(A), `IDEA`(C), `OBJETIVO`(A) | A,C |
| `/v11_pensamiento_segundo_orden_consecuencias` | `ADJUNTOS`(A), `DECISION`(A), `HORIZONTE`(C) | A,C |
| `/v11_pensamiento_pre_mortem_proyecto` | `ADJUNTOS`(A), `PLAZO`(A), `PROYECTO`(A) | A |
| `/v11_pensamiento_analisis_causal_fishbone` | `ADJUNTOS`(A), `CONTEXTO`(A), `PROBLEMA`(A) | A |
| `/v11_pensamiento_analogia_transferir_solucion` | `ADJUNTOS`(A), `DOMINIO`(B), `PROBLEMA`(A) | B,A |
| `/v11_pensamiento_inversion_pensar_al_reves` | `ADJUNTOS`(A), `CONTEXTO`(A), `OBJETIVO`(A) | A |
| `/v11_pensamiento_steel_man_fortalecer_argumento` | `ADJUNTOS`(A), `CONTEXTO`(A), `POSICION`(C) | A,C |
| `/v11_pensamiento_red_team_atacar_plan` | `ADJUNTOS`(A), `ADVERSARIO`(C), `PLAN`(B) | B,A,C |
| `/v11_pensamiento_design_thinking_problema` | `ADJUNTOS`(A), `PROBLEMA`(A), `USUARIO`(B) | B,A |
| `/v11_pensamiento_systems_thinking_mapa` | `ADJUNTOS`(A), `PROBLEMA`(A), `SISTEMA`(C) | A,C |
| `/v11_pensamiento_six_hats_perspectivas` | `ADJUNTOS`(A), `TEMA`(A) | A |
| `/v11_pensamiento_ooda_loop_decision_rapida` | `ADJUNTOS`(A), `PRESION`(C), `SITUACION`(A) | A,C |
| `/v11_pensamiento_bayesiano_actualizar_creencias` | `ADJUNTOS`(A), `CREENCIA`(C), `EVIDENCIA`(A) | A,C |
| `/v11_pensamiento_occam_razor_solucion_simple` | `ADJUNTOS`(A), `OPCIONES`(C), `PROBLEMA`(A) | A,C |
| `/v11_pensamiento_dialectico_tesis_antitesis` | `ADJUNTOS`(A), `POSICION_A`(C), `POSICION_B`(C) | A,C |
| `/v11_pensamiento_lateral_provocacion` | `ADJUNTOS`(A), `PATRON_ACTUAL`(C), `PROBLEMA`(A) | A,C |
| `/v11_pensamiento_abstraction_laddering` | `ADJUNTOS`(A), `PROBLEMA`(A) | A |
| `/v11_pensamiento_assumption_mapping` | `ADJUNTOS`(A), `PLAN`(C) | A,C |
| `/v11_pensamiento_decision_journal_registro` | `ADJUNTOS`(A), `TIPO_DECISIONES`(C) | A,C |
| `/v11_pensamiento_cognitive_bias_audit` | `ADJUNTOS`(A), `CONTEXTO`(A), `DECISION`(A) | A |
| `/v11_pensamiento_reframing_cambiar_perspectiva` | `ADJUNTOS`(A), `SITUACION`(A) | A |
| `/v11_investigacion_protocolo_3_fases` | `ADJUNTOS`(A), `FUENTES`(A), `OBJETIVO`(A), `TEMA`(A) | A |
| `/v11_investigacion_factcheck_afirmacion` | `ADJUNTOS`(A), `AFIRMACION`(B), `CONTEXTO`(A) | B,A |
| `/v11_investigacion_tendencias_sector` | `ADJUNTOS`(A), `HORIZONTE`(C), `SECTOR`(A) | A,C |
| `/v11_investigacion_dossier_empresa` | `ADJUNTOS`(A), `EMPRESA`(A), `OBJETIVO`(A) | A |
| `/v11_investigacion_sintesis_multiples_fuentes` | `ADJUNTOS`(A), `FUENTES`(A), `TEMA`(A) | A |
| `/v11_investigacion_benchmark_competitivo` | `ADJUNTOS`(A), `COMPETIDORES`(C), `METRICAS`(A), `SECTOR`(A) | A,C |
| `/v11_investigacion_due_diligence_rapida` | `ADJUNTOS`(A), `ENTIDAD`(C), `TIPO`(A) | A,C |
| `/v11_investigacion_mapa_stakeholders` | `ADJUNTOS`(A), `CONTEXTO`(A), `INICIATIVA`(C) | A,C |
| `/v11_investigacion_analisis_competitivo_5_fuerzas` | `ADJUNTOS`(A), `EMPRESA`(A), `SECTOR`(A) | A |
| `/v11_investigacion_pestel_entorno_macro` | `ADJUNTOS`(A), `ORGANIZACION`(C), `PAIS`(C) | A,C |
| `/v11_investigacion_voice_of_customer` | `ADJUNTOS`(A), `PRODUCTO`(A), `SEGMENTOS`(C) | A,C |
| `/v11_investigacion_analisis_swot_estrategico` | `ADJUNTOS`(A), `ORGANIZACION`(C), `SECTOR`(A) | A,C |
| `/v11_investigacion_analisis_sentimiento_marca` | `ADJUNTOS`(A), `MARCA`(A), `PERIODO`(C) | A,C |
| `/v11_investigacion_market_sizing_tam_sam_som` | `ADJUNTOS`(A), `GEOGRAFIA`(A), `OPORTUNIDAD`(C) | A,C |
| `/v11_investigacion_patent_landscape` | `ADJUNTOS`(A), `EMPRESA`(A), `TECNOLOGIA`(C) | A,C |
| `/v11_investigacion_caso_estudio_analisis` | `ADJUNTOS`(A), `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_investigacion_regulatory_scan` | `ADJUNTOS`(A), `INICIATIVA`(C), `JURISDICCION`(C) | A,C |
| `/v11_investigacion_literature_review` | `ADJUNTOS`(A), `ALCANCE`(A), `TEMA`(A) | A |
| `/v11_investigacion_analisis_redes_influencia` | `ADJUNTOS`(A), `ECOSISTEMA`(C), `OBJETIVO`(A) | A,C |
| `/v11_investigacion_scenario_planning_futuros` | `ADJUNTOS`(A), `HORIZONTE`(C), `PREGUNTA`(B) | B,A,C |
| `/v11_investigacion_data_collection_plan` | `ADJUNTOS`(A), `PREGUNTA`(B), `RECURSOS`(C) | B,A,C |
| `/v11_investigacion_media_monitoring_alertas` | `ADJUNTOS`(A), `COMPETIDORES`(C), `TEMA`(A) | A,C |
| `/v11_investigacion_expert_interview_guide` | `ADJUNTOS`(A), `EXPERTO`(C), `OBJETIVO`(A), `TEMA`(A) | A,C |
| `/v11_investigacion_competitive_intelligence_continua` | `ADJUNTOS`(A), `COMPETIDORES`(C), `EMPRESA`(A), `SECTOR`(A) | A,C |
| `/v11_escritura_brand_voice_document` | `ADJUNTOS`(A), `AUDIENCIA`(A), `MARCA`(A), `REFERENCIAS`(C), `VALORES`(C) | A,C |
| `/v11_escritura_reescribir_profesional` | `ADJUNTOS`(A), `AUDIENCIA`(A), `TEXTO`(C), `TONO`(A) | A,C |
| `/v11_escritura_storytelling_datos` | `ACCION`(A), `ADJUNTOS`(A), `AUDIENCIA`(A), `DATOS`(A) | A |
| `/v11_escritura_email_alto_impacto` | `ADJUNTOS`(A), `CONTEXTO`(A), `DESTINATARIO`(C), `OBJETIVO`(A), `TONO`(A) | A,C |
| `/v11_escritura_linkedin_thought_leadership` | `ADJUNTOS`(A), `EXPERIENCIA`(C), `TEMA`(A) | A,C |
| `/v11_escritura_secuencia_email_nurturing` | `ADJUNTOS`(A), `AUDIENCIA`(A), `OBJECION`(C), `PRODUCTO`(A), `TONO`(A) | A,C |
| `/v11_escritura_copy_landing_page` | `ADJUNTOS`(A), `AUDIENCIA`(A), `PRODUCTO`(A), `PROPUESTA_VALOR`(C) | A,C |
| `/v11_escritura_caso_exito_cliente` | `ADJUNTOS`(A), `CLIENTE`(A), `DETALLES`(C), `RESULTADO`(B) | B,A,C |
| `/v11_escritura_propuesta_comercial` | `ADJUNTOS`(A), `CLIENTE`(A), `PROBLEMA`(A), `SOLUCION`(C) | A,C |
| `/v11_escritura_newsletter_engagement` | `ADJUNTOS`(A), `AUDIENCIA`(A), `NEWSLETTER`(B), `TEMA`(A) | B,A |
| `/v11_escritura_presentacion_ejecutiva_script` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DURACION`(A), `TEMA`(A) | A |
| `/v11_escritura_informe_ejecutivo` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DATOS`(A), `TEMA`(A) | A |
| `/v11_escritura_comunicado_interno` | `ADJUNTOS`(A), `AUDIENCIA`(A), `CAMBIO`(C), `TIMELINE`(C) | A,C |
| `/v11_escritura_articulo_blog_seo` | `ADJUNTOS`(A), `AUDIENCIA`(A), `KEYWORD`(C), `LONGITUD`(A) | A,C |
| `/v11_escritura_speech_motivacional` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DURACION`(A), `TEMA`(A) | A |
| `/v11_escritura_white_paper_autoridad` | `ADJUNTOS`(A), `FRAMEWORK`(A), `SECTOR`(A), `TEMA`(A) | A |
| `/v11_escritura_thread_twitter_viral` | `ADJUNTOS`(A), `INSIGHTS`(C), `TEMA`(A) | A,C |
| `/v11_escritura_copy_producto_features` | `ADJUNTOS`(A), `CLIENTE`(A), `FEATURES`(B), `PRODUCTO`(A) | B,A |
| `/v11_escritura_guion_podcast` | `ADJUNTOS`(A), `DURACION`(A), `PODCAST`(B), `TEMA_EPISODIO`(C) | B,A,C |
| `/v11_escritura_micro_contenido_redes` | `ADJUNTOS`(A), `PERFIL`(C), `PLATAFORMA`(C), `TEMA`(A) | A,C |
| `/v11_escritura_resumen_libro_accionable` | `ADJUNTOS`(A), `CONTEXTO`(A), `LIBRO`(B) | B,A |
| `/v11_escritura_faq_completa_producto` | `ADJUNTOS`(A), `PREGUNTAS_COMUNES`(C), `PRODUCTO`(A) | A,C |
| `/v11_escritura_elevator_pitch` | `ADJUNTOS`(A), `AUDIENCIA`(A), `EMPRESA`(A), `PROPUESTA`(C) | A,C |
| `/v11_escritura_contenido_onboarding` | `ADJUNTOS`(A), `AHA_MOMENT`(C), `AUDIENCIA`(A), `PRODUCTO`(A) | A,C |
| `/v11_data_analisis_exploratorio_dataset` | `ADJUNTOS`(A), `DATASET`(B), `HERRAMIENTA`(A), `PREGUNTA`(B) | B,A |
| `/v11_data_dashboard_metricas_disenar` | `ADJUNTOS`(A), `AUDIENCIA`(A), `HERRAMIENTA`(A), `PROCESO`(A) | A |
| `/v11_data_limpiar_transformar_datos` | `ADJUNTOS`(A), `DATOS`(A), `FORMATO_DESTINO`(C) | A,C |
| `/v11_data_kpi_framework_definir` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `NEGOCIO`(C), `OBJETIVO`(A) | A,C |
| `/v11_data_encuesta_disenar_analizar` | `ADJUNTOS`(A), `OBJETIVO`(A), `POBLACION`(C) | A,C |
| `/v11_data_ab_test_disenar` | `ADJUNTOS`(A), `CAMBIO`(C), `METRICA`(C), `TRAFICO`(C) | A,C |
| `/v11_data_cohort_analysis` | `ADJUNTOS`(A), `DATOS`(A), `METRICA`(C), `PRODUCTO`(A) | A,C |
| `/v11_data_forecast_proyeccion` | `ADJUNTOS`(A), `DATOS_HISTORICOS`(C), `HORIZONTE`(C), `METRICA`(C) | A,C |
| `/v11_data_regression_analysis_simple` | `ADJUNTOS`(A), `DATOS`(A), `PREGUNTA`(B), `VARIABLES`(C) | B,A,C |
| `/v11_data_sql_query_compleja` | `ADJUNTOS`(A), `BASE_DATOS`(C), `PREGUNTA`(B), `TABLAS`(C) | B,A,C |
| `/v11_data_excel_modelo_financiero` | `ADJUNTOS`(A), `HORIZONTE`(C), `METRICAS`(A), `NEGOCIO`(C) | A,C |
| `/v11_data_customer_segmentation` | `ADJUNTOS`(A), `CLIENTES`(C), `OBJETIVO`(A), `VARIABLES`(C) | A,C |
| `/v11_data_roi_calculo_proyecto` | `ADJUNTOS`(A), `HORIZONTE`(C), `INVERSION`(C), `PROYECTO`(A) | A,C |
| `/v11_data_funnel_conversion_analisis` | `ADJUNTOS`(A), `DATOS`(A), `ETAPAS`(C), `PRODUCTO`(A) | A,C |
| `/v11_data_pricing_analysis` | `ADJUNTOS`(A), `COMPETIDORES`(C), `PRICING_ACTUAL`(C), `PRODUCTO`(A) | A,C |
| `/v11_data_churn_diagnostico` | `ADJUNTOS`(A), `CHURN_ACTUAL`(C), `DATOS`(A), `PRODUCTO`(A) | A,C |
| `/v11_data_visualization_best_practice` | `ADJUNTOS`(A), `TIPO_DATOS`(C) | A,C |
| `/v11_data_automated_report_disenar` | `ADJUNTOS`(A), `FUENTE`(C), `HERRAMIENTA`(A), `REPORTE`(C) | A,C |
| `/v11_visual_brief_creativo_imagen_ia` | `ADJUNTOS`(A), `CONCEPTO`(A), `ESTILO`(A), `USO`(C) | A,C |
| `/v11_visual_guion_video_corto` | `ADJUNTOS`(A), `DURACION`(A), `PLATAFORMA`(C), `TEMA`(A) | A,C |
| `/v11_visual_infografia_ejecutiva` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DATOS`(A), `FORMATO`(A) | A |
| `/v11_visual_presentacion_slide_deck` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DURACION`(A), `SLIDES`(C), `TEMA`(A) | A,C |
| `/v11_visual_moodboard_direccion_arte` | `ADJUNTOS`(A), `CONTEXTO`(A), `PROYECTO`(A) | A |
| `/v11_visual_diagrama_arquitectura` | `ADJUNTOS`(A), `AUDIENCIA`(A), `NIVEL`(C), `SISTEMA`(B) | B,A,C |
| `/v11_visual_brand_kit_personal` | `ADJUNTOS`(A), `CANALES`(C), `NOMBRE`(A), `VALORES`(C) | A,C |
| `/v11_visual_storyboard_campana` | `ADJUNTOS`(A), `CAMPANA`(B), `CANALES`(C), `DURACION`(A) | B,A,C |
| `/v11_visual_thumbnail_redes_sociales` | `ADJUNTOS`(A), `CONTENIDO`(C), `PLATAFORMA`(C) | A,C |
| `/v11_visual_data_viz_interactiva` | `ADJUNTOS`(A), `DATOS`(A), `HERRAMIENTA`(A), `HISTORIA`(C) | A,C |
| `/v11_visual_contenido_educativo_visual` | `ADJUNTOS`(A), `AUDIENCIA`(A), `TEMA`(A) | A |
| `/v11_visual_motion_graphics_spec` | `ADJUNTOS`(A), `DURACION`(A), `ESTILO`(A), `MENSAJE`(A) | A |
| `/v11_visual_ui_wireframe_spec` | `ADJUNTOS`(A), `PANTALLAS`(C), `PLATAFORMA`(C), `PRODUCTO`(A) | A,C |
| `/v11_agentes_disenar_custom_gpt` | `ADJUNTOS`(A), `AUDIENCIA`(A), `TAREA`(A), `TONO`(A) | A |
| `/v11_agentes_comite_operativo_artificial` | `ADJUNTOS`(A), `ENTREGABLE`(C), `ESTANDAR`(C) | A,C |
| `/v11_agentes_system_prompt_gem_nlm` | `ADJUNTOS`(A), `AUDIENCIA`(A), `FUNCION`(C), `PERSONALIDAD`(C) | A,C |
| `/v11_agentes_chain_prompts_workflow` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `TAREA`(A) | A |
| `/v11_agentes_knowledge_base_privada` | `ADJUNTOS`(A), `DOMINIO`(B), `FUENTES`(A), `USUARIOS`(C) | B,A,C |
| `/v11_agentes_evaluacion_asistente_qa` | `ADJUNTOS`(A), `ASISTENTE`(B), `SCOPE`(C) | B,A,C |
| `/v11_agentes_automatizar_proceso_recurrente` | `ADJUNTOS`(A), `FRECUENCIA`(C), `HERRAMIENTAS`(A), `PROCESO`(A) | A,C |
| `/v11_agentes_prompt_library_personal` | `ADJUNTOS`(A), `HERRAMIENTAS`(A), `TEMAS`(C), `variables`(C) | A,C |
| `/v11_agentes_escalera_agentica_roadmap` | `ADJUNTOS`(A), `NIVEL_ACTUAL`(C), `OBJETIVO`(A) | A,C |
| `/v11_automatizacion_workflow_nocode` | `ADJUNTOS`(A), `FRECUENCIA`(C), `HERRAMIENTAS`(A), `PROCESO`(A) | A,C |
| `/v11_meta_crear_spec_alto_rendimiento` | `ADJUNTOS`(A), `COMPLEJIDAD`(A), `CONTEXTO`(A), `DOBLE_LLAVE`(C), `OBJETIVO`(A), `placeholders`(C) | A,C |
| `/v11_meta_optimizar_spec_existente` | `ADJUNTOS`(A), `PROBLEMA`(A), `SPEC_ACTUAL`(C) | A,C |
| `/v11_visual_paleta_colores_profesional` | `ADJUNTOS`(A), `MARCA`(A), `PERSONALIDAD`(C), `SECTOR`(A) | A,C |
| `/v11_visual_diseno_social_media_kit` | `ADJUNTOS`(A), `MARCA`(A), `PALETA`(C), `PLATAFORMAS`(C) | A,C |
| `/v11_visual_presentacion_minimalista` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DURACION`(A), `TEMA`(A) | A |
| `/v11_visual_html_autocontenido_dashboard` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DATOS`(A), `MARCA`(A) | A |
| `/v11_visual_before_after_transformacion` | `ADJUNTOS`(A), `AFTER`(B), `BEFORE`(B), `METRICA`(C) | B,A,C |
| `/v11_visual_mapa_mental_concepto` | `ADJUNTOS`(A), `CONCEPTO`(A), `PROPOSITO`(C) | A,C |
| `/v11_visual_icon_system_coherente` | `ADJUNTOS`(A), `ESTILO`(A), `PROYECTO`(A) | A |
| `/v11_agentes_gemini_gem_especializado` | `ADJUNTOS`(A), `AUDIENCIA`(A), `FUNCION`(C), `SOURCES`(C) | A,C |
| `/v11_agentes_notebooklm_cuaderno` | `ADJUNTOS`(A), `FUENTES`(A), `OUTPUTS`(A), `TEMA`(A) | A |
| `/v11_agentes_text_expander_biblioteca` | `ADJUNTOS`(A), `DISPOSITIVOS`(C), `HERRAMIENTA`(A), `campos`(C) | A,C |
| `/v11_agentes_priming_contexto_sesion` | `ADJUNTOS`(A), `PREFERENCIAS`(C), `ROL`(A), `SECTOR`(A) | A,C |
| `/v11_agentes_workflow_multimodelo` | `ADJUNTOS`(A), `MODELOS`(C), `PRESUPUESTO`(A), `TAREAS`(C) | A,C |
| `/v11_agentes_quality_rubric_outputs` | `ADJUNTOS`(A), `ESTANDAR`(C), `TIPO_OUTPUT`(C) | A,C |
| `/v11_stack_auditar_herramientas_personal` | `ADJUNTOS`(A), `HERRAMIENTAS`(A), `PRESUPUESTO`(A) | A |
| `/v11_stack_seleccionar_herramienta` | `ADJUNTOS`(A), `CANDIDATAS`(C), `NECESIDAD`(C), `PRESUPUESTO`(A) | A,C |
| `/v11_stack_integraciones_mapa` | `ADJUNTOS`(A), `FLUJOS`(C), `HERRAMIENTAS`(A) | A,C |
| `/v11_automatizacion_ritual_productivo_semiautomatico` | `ADJUNTOS`(A), `FRICCIONES`(C), `RITUAL`(B) | B,A,C |
| `/v11_automatizacion_zapier_make_receta` | `ADJUNTOS`(A), `APPS`(C), `PLATAFORMA`(C), `PROCESO`(A) | A,C |
| `/v11_engine_asistente_corporativo_privado` | `ADJUNTOS`(A), `FUENTES`(A), `ORGANIZACION`(C), `SCOPE`(C) | A,C |
| `/v11_engine_chatbot_ventas_calificacion` | `ADJUNTOS`(A), `CRM`(C), `ICP`(C), `PRODUCTO`(A) | A,C |
| `/v11_presentacion_deck_inversores` | `ADJUNTOS`(A), `METRICAS`(A), `RONDA`(C), `STARTUP`(C) | A,C |
| `/v11_comunicacion_escalacion_profesional` | `ADJUNTOS`(A), `DESTINATARIO`(C), `ESCALACION`(B), `IMPACTO`(C), `PROBLEMA`(A) | B,A,C |
| `/v11_comunicacion_feedback_positivo_refuerzo` | `ADJUNTOS`(A), `COMPORTAMIENTO`(C), `IMPACTO`(B), `PERSONA`(A) | B,A,C |
| `/v11_decision_framework_rapido_5min` | `ADJUNTOS`(A), `CONTEXTO`(A), `DECISION`(A) | A |
| `/v11_decision_matriz_ponderada` | `ADJUNTOS`(A), `CRITERIOS`(A), `OPCIONES`(C) | A,C |
| `/v11_liderazgo_conversacion_dificil` | `ADJUNTOS`(A), `OBJETIVO`(A), `PERSONA`(A), `SITUACION`(A) | A |
| `/v11_liderazgo_one_on_one_efectivo` | `ADJUNTOS`(A), `EQUIPO`(A), `FRECUENCIA`(C) | A,C |
| `/v11_aprendizaje_feynman_explicar` | `ADJUNTOS`(A), `CONCEPTO`(A), `NIVEL_ACTUAL`(C) | A,C |
| `/v11_aprendizaje_plan_90_dias_competencia` | `ADJUNTOS`(A), `COMPETENCIA`(B), `HORAS_SEMANALES`(C), `NIVEL_ACTUAL`(C) | B,A,C |
| `/v11_negociacion_preparar_conversacion` | `ADJUNTOS`(A), `CONTEXTO`(A), `CONTRAPARTE`(C), `OBJETIVO`(A) | A,C |
| `/v11_creatividad_scamper_innovar` | `ADJUNTOS`(A), `OBJETO`(C), `RESTRICCIONES`(A) | A,C |
| `/v11_bienestar_protocolo_anti_burnout` | `ADJUNTOS`(A), `DRAINS`(C), `ROL`(A) | A,C |
| `/v11_estrategia_vision_3_horizontes` | `ADJUNTOS`(A), `CONTEXTO`(A), `HORIZONTE`(C) | A,C |
| `/v11_estrategia_okr_personal_trimestral` | `ADJUNTOS`(A), `TRIMESTRE`(C), `VISION`(B) | B,A,C |
| `/v11_meta_reverse_engineer_conversacion` | `ADJUNTOS`(A), `SESION`(C) | A,C |
| `/v11_meta_auditar_mis_prompts` | `ADJUNTOS`(A), `PROMPTS`(B) | B,A |
| `/v11_meta_crear_system_prompt_agente` | `ADJUNTOS`(A), `AGENTE`(A), `AUDIENCIA`(A), `AUTONOMIA`(C) | A,C |
| `/v11_meta_taxonomia_prompts_organizar` | `ADJUNTOS`(A), `BIBLIOTECA`(C), `TAMANO`(A) | A,C |
| `/v11_investigacion_analisis_bibliometrico` | `ADJUNTOS`(A), `CAMPO`(C), `PERIODO`(C) | A,C |
| `/v11_escritura_manual_procedimientos` | `ADJUNTOS`(A), `AUDIENCIA`(A), `PROCEDIMIENTO`(C) | A,C |
| `/v11_data_pivot_table_analisis` | `ADJUNTOS`(A), `DATOS`(A), `PREGUNTA`(B) | B,A |
| `/v11_data_anomaly_detection_manual` | `ADJUNTOS`(A), `DATASET`(C), `VARIABLES`(C) | A,C |
| `/v11_data_storytelling_presentation` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DATOS`(A), `DECISION`(A) | A |
| `/v11_data_sql_basico_consulta` | `ADJUNTOS`(A), `PREGUNTA`(B), `TABLAS`(C) | B,A,C |
| `/v11_agentes_prompt_testing_framework` | `ADJUNTOS`(A), `PROMPT`(B), `SCOPE`(C) | B,A,C |
| `/v11_agentes_migrar_gpt_a_gem` | `ADJUNTOS`(A), `AGENTE_ORIGINAL`(C), `PLATAFORMA_DESTINO`(C) | A,C |
| `/v11_agentes_monitorear_rendimiento` | `ADJUNTOS`(A), `AGENTE`(A), `METRICAS`(A) | A |
| `/v11_agentes_documentar_asistente` | `ADJUNTOS`(A), `AGENTE`(A), `AUDIENCIA`(A) | A |
| `/v11_agentes_curar_knowledge_sources` | `ADJUNTOS`(A), `AGENTE`(A), `DOMINIO`(B) | B,A |
| `/v11_agentes_conversational_ux_disenar` | `ADJUNTOS`(A), `AGENTE`(A), `AUDIENCIA`(A) | A |
| `/v11_agentes_security_guardrails` | `ADJUNTOS`(A), `AGENTE`(A), `DATOS`(A) | A |
| `/v11_agentes_roi_calcular_asistente` | `ADJUNTOS`(A), `AGENTE`(A), `COSTO`(C), `PROCESO`(A) | A,C |
| `/v11_agentes_onboarding_equipo_ia` | `ADJUNTOS`(A), `AGENTE`(A), `EQUIPO`(A) | A |
| `/v11_agentes_iterative_improvement_cycle` | `ADJUNTOS`(A), `AGENTE`(A), `METRICAS_ACTUALES`(C) | A,C |
| `/v11_automatizacion_email_filtros_reglas` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `VOLUMEN`(A) | A |
| `/v11_automatizacion_reportes_automaticos` | `ADJUNTOS`(A), `FRECUENCIA`(C), `HERRAMIENTA`(A), `REPORTE`(B) | B,A,C |
| `/v11_automatizacion_onboarding_empleado` | `ADJUNTOS`(A), `EMPRESA`(A), `HERRAMIENTAS`(A), `ROL`(A) | A |
| `/v11_automatizacion_social_media_scheduling` | `ADJUNTOS`(A), `CANALES`(C), `FRECUENCIA`(C), `HERRAMIENTA`(A) | A,C |
| `/v11_automatizacion_crm_pipeline_flujo` | `ADJUNTOS`(A), `CRM`(B), `EQUIPO`(A), `PROCESO_VENTAS`(C) | B,A,C |
| `/v11_automatizacion_notificaciones_inteligentes` | `ADJUNTOS`(A), `APPS`(C), `DISPOSITIVOS`(C) | A,C |
| `/v11_automatizacion_backup_datos_personal` | `ADJUNTOS`(A), `DATOS`(A), `HERRAMIENTAS`(A) | A |
| `/v11_automatizacion_meeting_prep_auto` | `ADJUNTOS`(A), `CALENDARIO`(C), `REUNIONES_SEMANA`(C) | A,C |
| `/v11_automatizacion_invoice_tracking` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `VOLUMEN`(A) | A |
| `/v11_automatizacion_content_repurposing` | `ADJUNTOS`(A), `CANALES`(C), `CONTENIDO`(C) | A,C |
| `/v11_automatizacion_password_security` | `ACTUAL`(B), `ADJUNTOS`(A), `VOLUMEN`(A) | A,B |
| `/v11_engine_faq_bot_automatico` | `ADJUNTOS`(A), `FUENTE`(C), `PLATAFORMA`(C) | A,C |
| `/v11_engine_content_generator_marca` | `ADJUNTOS`(A), `BRAND_VOICE`(C), `CONTENIDO`(B), `MARCA`(A) | B,A,C |
| `/v11_engine_analisis_automatizado_datos` | `ADJUNTOS`(A), `DATOS`(A), `FRECUENCIA`(C), `METRICAS`(A) | A,C |
| `/v11_engine_lead_scoring_modelo` | `ADJUNTOS`(A), `CRM`(C), `ICP`(C), `PRODUCTO`(A) | A,C |
| `/v11_engine_workflow_aprobaciones` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `PROCESO`(A) | A |
| `/v11_presentacion_pitch_cliente` | `ADJUNTOS`(A), `CLIENTE`(A), `PRODUCTO`(A) | A |
| `/v11_presentacion_quarterly_review` | `ADJUNTOS`(A), `EQUIPO`(A), `PERIODO`(C) | A,C |
| `/v11_presentacion_ted_style_talk` | `ADJUNTOS`(A), `DURACION`(A), `IDEA`(C) | A,C |
| `/v11_comunicacion_mensaje_dificil_escrito` | `ADJUNTOS`(A), `CANAL`(C), `RECEPTOR`(B), `TEMA`(A) | B,A,C |
| `/v11_comunicacion_update_stakeholders` | `ADJUNTOS`(A), `PROYECTO`(A), `STAKEHOLDERS`(A) | A |
| `/v11_decision_analizar_trade_offs` | `ADJUNTOS`(A), `CONTEXTO`(A), `OPCIONES`(C) | A,C |
| `/v11_decision_kill_project` | `ADJUNTOS`(A), `METRICAS`(A), `PROYECTO`(A) | A |
| `/v11_liderazgo_vision_equipo` | `ADJUNTOS`(A), `CONTEXTO`(A), `EQUIPO`(A) | A |
| `/v11_liderazgo_desarrollar_talento` | `ADJUNTOS`(A), `ASPIRACION`(C), `PERSONA`(A), `ROL_ACTUAL`(C) | A,C |
| `/v11_aprendizaje_skill_stack_personal` | `ADJUNTOS`(A), `INDUSTRIA`(A), `SKILLS_ACTUALES`(C) | A,C |
| `/v11_aprendizaje_zettelkasten_sistema` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `OBJETIVO`(A) | A |
| `/v11_negociacion_contrato_revisar` | `ADJUNTOS`(A), `CONTRATO`(B), `ROL`(A) | B,A |
| `/v11_creatividad_brainstorm_100_ideas` | `ADJUNTOS`(A), `DESAFIO`(C), `RESTRICCIONES`(A) | A,C |
| `/v11_bienestar_gestion_estres_agudo` | `ADJUNTOS`(A), `CONTEXTO`(A) | A |
| `/v11_estrategia_north_star_metric` | `ADJUNTOS`(A), `PRODUCTO`(A), `VALOR`(B) | B,A |
| `/v11_estrategia_competitive_moat` | `ADJUNTOS`(A), `COMPETIDORES`(C), `EMPRESA`(A) | A,C |
| `/v11_meta_prompt_chain_disenar` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `OUTPUT`(A) | A |
| `/v11_meta_excellence_rubric_crear` | `ADJUNTOS`(A), `ESTANDAR`(C), `TIPO_OUTPUT`(C) | A,C |
| `/v11_automatizacion_google_sheets_formulas` | `ADJUNTOS`(A), `DATOS`(A), `PROCESO`(A) | A |
| `/v11_automatizacion_notion_database_workflow` | `ADJUNTOS`(A), `EQUIPO`(A), `PROCESOS`(C) | A,C |
| `/v11_automatizacion_calendar_blocking_auto` | `ADJUNTOS`(A), `HORARIO`(C), `PRIORIDADES`(C) | A,C |
| `/v11_automatizacion_ai_daily_briefing` | `ADJUNTOS`(A), `FUENTES`(A), `SECTOR`(A) | A |
| `/v11_stack_migrar_herramienta` | `ADJUNTOS`(A), `DATOS`(A), `HERRAMIENTA_NUEVA`(C), `HERRAMIENTA_VIEJA`(C) | A,C |
| `/v11_stack_evaluar_ia_herramienta` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `PROBLEMA`(A) | A |
| `/v11_stack_keyboard_shortcuts_mapear` | `ADJUNTOS`(A), `DISPOSITIVO`(C), `HERRAMIENTAS`(A) | A,C |
| `/v11_stack_digital_minimalism_plan` | `ADJUNTOS`(A), `HERRAMIENTAS`(A) | A |
| `/v11_engine_email_responder_automatico` | `ADJUNTOS`(A), `TIPOS`(C), `TONO`(A), `VOLUMEN`(A) | A,C |
| `/v11_engine_propuesta_generator` | `ADJUNTOS`(A), `CLIENTE_TIPO`(C), `SERVICIO`(C) | A,C |
| `/v11_engine_meeting_summarizer` | `ADJUNTOS`(A), `FRECUENCIA`(C), `HERRAMIENTA`(A) | A,C |
| `/v11_engine_data_storytelling_auto` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DATOS`(A) | A |
| `/v11_solucion_proyecto_integrador_plan` | `ADJUNTOS`(A), `COMPETENCIAS`(C), `CONTEXTO`(A) | A,C |
| `/v11_solucion_portafolio_evidencia` | `ADJUNTOS`(A), `OBJETIVO`(A), `ROL`(A) | A |
| `/v11_solucion_caso_real_resolver` | `ADJUNTOS`(A), `COMPETENCIAS`(C), `PROBLEMA`(A) | A,C |
| `/v11_decision_eisenhower_priorizar` | `ADJUNTOS`(A), `TAREAS`(C) | A,C |
| `/v11_decision_cost_benefit_rapido` | `ADJUNTOS`(A), `DECISION`(A) | A |
| `/v11_decision_6_sombreros_rapido` | `ADJUNTOS`(A), `DECISION`(A) | A |
| `/v11_decision_regret_minimization` | `ADJUNTOS`(A), `DECISION`(A), `OPCIONES`(C) | A,C |
| `/v11_liderazgo_retrospectiva_equipo` | `ADJUNTOS`(A), `EQUIPO`(A), `PERIODO`(B) | B,A |
| `/v11_liderazgo_hiring_scorecard` | `ADJUNTOS`(A), `EQUIPO`(A), `ROL`(A) | A |
| `/v11_liderazgo_cultura_equipo_disenar` | `ADJUNTOS`(A), `EQUIPO`(A), `ESTADO_ACTUAL`(C) | A,C |
| `/v11_aprendizaje_spaced_repetition` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `MATERIAL`(B) | B,A |
| `/v11_aprendizaje_teach_to_learn` | `ADJUNTOS`(A), `AUDIENCIA`(A), `CONCEPTO`(A) | A |
| `/v11_negociacion_salary_raise` | `ADJUNTOS`(A), `EXPERIENCIA`(C), `LOGROS`(C), `ROL`(A) | A,C |
| `/v11_negociacion_precio_servicio` | `ADJUNTOS`(A), `PRESUPUESTO`(A), `PROVEEDOR`(C), `SERVICIO`(B) | B,A,C |
| `/v11_creatividad_constraint_driven_design` | `ADJUNTOS`(A), `PROBLEMA`(A), `RESTRICCIONES`(A) | A |
| `/v11_creatividad_random_input_technique` | `ADJUNTOS`(A), `PROBLEMA`(A) | A |
| `/v11_bienestar_digital_detox_plan` | `ADJUNTOS`(A), `APPS_PROBLEMA`(C), `SCREEN_TIME`(C) | A,C |
| `/v11_bienestar_energy_management_daily` | `ADJUNTOS`(A), `ENERGIA_ACTUAL`(C), `HORARIO`(C) | A,C |
| `/v11_estrategia_personal_roadmap` | `ADJUNTOS`(A), `ESTADO_ACTUAL`(C), `VISION`(B) | B,A,C |
| `/v11_estrategia_pivot_evaluar` | `ADJUNTOS`(A), `MODELO_ACTUAL`(C), `SIGNALS`(C) | A,C |
| `/v11_presentacion_demo_producto` | `ADJUNTOS`(A), `PAIN_POINTS`(C), `PRODUCTO`(A), `PROSPECTO`(C) | A,C |
| `/v11_presentacion_workshop_facilitar` | `ADJUNTOS`(A), `DURACION`(A), `OBJETIVO`(A), `PARTICIPANTES`(C) | A,C |
| `/v11_comunicacion_storytelling_personal` | `ADJUNTOS`(A), `AUDIENCIA`(A), `CONTEXTO`(A) | A |
| `/v11_comunicacion_bad_news_delivery` | `ADJUNTOS`(A), `NOTICIA`(C), `RECEPTOR`(B) | B,A,C |
| `/v11_meta_prompt_audit_personal` | `ADJUNTOS`(A), `PROMPTS`(C) | A,C |
| `/v11_meta_system_prompt_personal_ia` | `ADJUNTOS`(A), `ESTILO`(A), `REGLAS`(C), `ROL`(A) | A,C |
| `/v11_decision_reversible_vs_irreversible` | `ADJUNTOS`(A), `CONTEXTO`(A), `DECISION`(A) | A |
| `/v11_decision_10_10_10_perspectiva` | `ADJUNTOS`(A), `DECISION`(A) | A |
| `/v11_decision_opportunity_cost_calcular` | `ADJUNTOS`(A), `OPCIONES`(C), `RECURSOS`(C) | A,C |
| `/v11_decision_consensus_vs_consent` | `ADJUNTOS`(A), `DECISION`(A), `GRUPO`(C) | A,C |
| `/v11_decision_analisis_sensibilidad` | `ADJUNTOS`(A), `DECISION`(A), `SUPUESTOS`(A) | A |
| `/v11_decision_devil_advocate_protocolo` | `ADJUNTOS`(A), `CONTEXTO`(A), `PROPUESTA`(C) | A,C |
| `/v11_liderazgo_onboarding_30_60_90` | `ADJUNTOS`(A), `EQUIPO`(A), `ROL`(A) | A |
| `/v11_liderazgo_dar_autonomia_calibrada` | `ADJUNTOS`(A), `PERSONA`(A), `TAREA`(A) | A |
| `/v11_liderazgo_remote_team_engagement` | `ADJUNTOS`(A), `EQUIPO`(A), `HERRAMIENTAS`(A) | A |
| `/v11_liderazgo_mentorar_junior` | `ADJUNTOS`(A), `MENTEE`(C), `OBJETIVO`(A) | A,C |
| `/v11_liderazgo_conflict_resolution` | `ADJUNTOS`(A), `CONFLICTO`(C), `PARTES`(C) | A,C |
| `/v11_aprendizaje_curacion_recursos` | `ADJUNTOS`(A), `NIVEL`(C), `TEMA`(A), `TIEMPO`(C) | A,C |
| `/v11_aprendizaje_deliberate_practice` | `ADJUNTOS`(A), `HABILIDAD`(C), `NIVEL`(C) | A,C |
| `/v11_aprendizaje_portfolio_learning` | `ADJUNTOS`(A), `AUDIENCIA`(A), `COMPETENCIAS`(C) | A,C |
| `/v11_aprendizaje_retrospectiva_personal` | `ADJUNTOS`(A), `PERIODO`(B) | B,A |
| `/v11_estrategia_swot_personal` | `ADJUNTOS`(A), `ASPIRACION`(C), `ROL`(A) | A,C |
| `/v11_estrategia_blue_ocean_oportunidad` | `ADJUNTOS`(A), `PRODUCTO`(A), `SECTOR`(A) | A |
| `/v11_estrategia_flywheel_diseno` | `ADJUNTOS`(A), `CRECIMIENTO`(C), `NEGOCIO`(C) | A,C |
| `/v11_estrategia_jobs_to_be_done` | `ADJUNTOS`(A), `CLIENTES`(C), `PRODUCTO`(A), `motivacion`(C), `resultado`(B), `situacion`(A) | B,A,C |
| `/v11_meta_priming_universal_crear` | `ADJUNTOS`(A), `ESTILO`(A), `ROL`(A) | A |
| `/v11_meta_evaluar_output_ia_rubric` | `ADJUNTOS`(A), `TIPO_OUTPUT`(C) | A,C |
| `/v11_presentacion_board_meeting` | `ADJUNTOS`(A), `EMPRESA`(A), `PERIODO`(C) | A,C |
| `/v11_presentacion_training_session` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DURACION`(A), `HABILIDAD`(C) | A,C |
| `/v11_presentacion_webinar_engagement` | `ADJUNTOS`(A), `AUDIENCIA`(A), `TEMA`(A) | A |
| `/v11_comunicacion_thank_you_profesional` | `ADJUNTOS`(A), `CANAL`(C), `PERSONA`(A), `RAZON`(C) | A,C |
| `/v11_comunicacion_presentar_personas` | `ADJUNTOS`(A), `PERSONA_A`(C), `PERSONA_B`(C), `RAZON`(C) | A,C |
| `/v11_negociacion_deadline_extensiones` | `ADJUNTOS`(A), `DEADLINE`(A), `PROYECTO`(A), `RAZON`(C) | A,C |
| `/v11_negociacion_scope_creep_defender` | `ADJUNTOS`(A), `CAMBIO`(C), `SCOPE_ORIGINAL`(C) | A,C |
| `/v11_creatividad_reverse_brainstorm` | `ADJUNTOS`(A), `PROBLEMA`(A) | A |
| `/v11_creatividad_mashup_ideas` | `ADJUNTOS`(A), `DOMINIO_A`(C), `DOMINIO_B`(C) | A,C |
| `/v11_bienestar_boundaries_profesionales` | `ADJUNTOS`(A), `ROL`(A), `VIOLACIONES`(C) | A,C |
| `/v11_bienestar_mindfulness_2min` | `ADJUNTOS`(A), `CONTEXTO`(A) | A |
| `/v11_stack_browser_productividad` | `ADJUNTOS`(A), `BROWSER`(B), `USO`(C) | B,A,C |
| `/v11_stack_note_taking_system` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `VOLUMEN`(A) | A |
| `/v11_stack_ai_tools_portfolio` | `ADJUNTOS`(A), `HERRAMIENTAS_IA`(C), `TAREAS`(C) | A,C |
| `/v11_stack_second_brain_disenar` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `VOLUMEN`(A) | A |
| `/v11_engine_report_generator_automatico` | `ADJUNTOS`(A), `DATOS`(A), `FRECUENCIA`(C), `REPORTE`(C) | A,C |
| `/v11_engine_onboarding_personalizado` | `ADJUNTOS`(A), `PRODUCTO`(A), `USUARIOS`(C) | A,C |
| `/v11_solucion_mvp_disenar` | `ADJUNTOS`(A), `HIPOTESIS`(A), `IDEA`(C) | A,C |
| `/v11_solucion_business_case_crear` | `ADJUNTOS`(A), `INVERSION`(C), `PROYECTO`(A) | A,C |
| `/v11_solucion_pitch_interno_idea` | `ADJUNTOS`(A), `ASK`(C), `AUDIENCIA`(A), `IDEA`(B) | B,A,C |
| `/v11_solucion_forma_trabajo_documentar` | `ADJUNTOS`(A), `PROCESOS`(C), `ROL`(A) | A,C |
| `/v11_decision_go_nogo_checklist` | `ADJUNTOS`(A), `CRITERIOS`(A), `LANZAMIENTO`(C) | A,C |
| `/v11_decision_stakeholder_alignment` | `ADJUNTOS`(A), `DECISION`(A), `STAKEHOLDERS`(A) | A |
| `/v11_decision_sunk_cost_detector` | `ADJUNTOS`(A), `INVERTIDO`(C), `PROYECTO`(A) | A,C |
| `/v11_decision_minimum_viable_decision` | `ADJUNTOS`(A), `DECISION`(A) | A |
| `/v11_liderazgo_empowerment_framework` | `ADJUNTOS`(A), `EQUIPO`(A), `NIVEL`(C) | A,C |
| `/v11_liderazgo_succession_planning` | `ADJUNTOS`(A), `EQUIPO`(A), `POSICION`(C) | A,C |
| `/v11_liderazgo_town_hall_preparar` | `ADJUNTOS`(A), `EMPRESA`(A), `ESTADO`(C), `PERIODO`(C) | A,C |
| `/v11_aprendizaje_active_recall_practice` | `ADJUNTOS`(A), `MATERIAL`(B), `OBJETIVO`(A) | B,A |
| `/v11_aprendizaje_interleaving_practice` | `ADJUNTOS`(A), `HABILIDADES`(C), `TIEMPO`(C) | A,C |
| `/v11_aprendizaje_elaboration_tecnica` | `ADJUNTOS`(A), `CONCEPTO`(A), `CONOCIMIENTO_PREVIO`(C) | A,C |
| `/v11_aprendizaje_community_learning` | `ADJUNTOS`(A), `NIVEL`(C), `TEMA`(A) | A,C |
| `/v11_aprendizaje_learning_from_failure` | `ADJUNTOS`(A), `EVENTO`(C) | A,C |
| `/v11_estrategia_resource_allocation` | `ADJUNTOS`(A), `INICIATIVAS`(C), `RECURSOS`(C) | A,C |
| `/v11_estrategia_competitive_positioning` | `ADJUNTOS`(A), `AUDIENCIA`(A), `COMPETIDORES`(C), `PRODUCTO`(A), `diferenciador`(C), `quien`(C) | A,C |
| `/v11_estrategia_antifragil_plan` | `ADJUNTOS`(A), `PLAN`(B) | B,A |
| `/v11_estrategia_moat_personal_carrera` | `ADJUNTOS`(A), `ASPIRACION`(C), `ROL`(A) | A,C |
| `/v11_estrategia_value_chain_personal` | `ADJUNTOS`(A), `OUTPUTS`(A), `ROL`(A) | A |
| `/v11_presentacion_project_kickoff` | `ADJUNTOS`(A), `EQUIPO`(A), `PROYECTO`(A) | A |
| `/v11_presentacion_report_mensual` | `ADJUNTOS`(A), `AREA`(C), `PERIODO`(C) | A,C |
| `/v11_presentacion_case_competition` | `ADJUNTOS`(A), `CASO`(A), `DURACION`(A) | A |
| `/v11_presentacion_internal_proposal` | `ADJUNTOS`(A), `AUDIENCIA`(A), `PROPUESTA`(C) | A,C |
| `/v11_comunicacion_resumen_reuniones_async` | `ADJUNTOS`(A), `ASISTENTES`(C), `REUNION`(C) | A,C |
| `/v11_comunicacion_cold_outreach` | `ADJUNTOS`(A), `OBJETIVO`(A), `PERSONA`(A) | A |
| `/v11_negociacion_partnership_propuesta` | `ADJUNTOS`(A), `OBJETIVO`(A), `PARTNER`(C) | A,C |
| `/v11_negociacion_objecion_handling` | `ADJUNTOS`(A), `OBJECIONES`(C), `PRODUCTO`(A) | A,C |
| `/v11_creatividad_provocative_questions` | `ADJUNTOS`(A), `TEMA`(A) | A |
| `/v11_creatividad_six_word_story` | `ADJUNTOS`(A), `CONCEPTO`(A) | A |
| `/v11_creatividad_world_building` | `ADJUNTOS`(A), `AUDIENCIA`(A), `MARCA`(A), `VALORES`(C) | A,C |
| `/v11_bienestar_sleep_hygiene_protocol` | `ADJUNTOS`(A), `HORARIO_ACTUAL`(C), `PROBLEMAS`(C) | A,C |
| `/v11_bienestar_micro_recovery_workday` | `ADJUNTOS`(A), `ENTORNO`(C), `HORARIO`(C) | A,C |
| `/v11_solucion_demo_day_preparar` | `ADJUNTOS`(A), `AUDIENCIA`(A), `PROYECTO`(A), `RESULTADOS`(C) | A,C |
| `/v11_solucion_retrospectiva_proyecto` | `ADJUNTOS`(A), `DURACION`(A), `PROYECTO`(A) | A |
| `/v11_solucion_certificacion_portafolio` | `ADJUNTOS`(A), `CERTIFICACION`(B), `HITOS`(C) | B,A,C |
| `/v11_stack_api_keys_organizar` | `ADJUNTOS`(A), `SERVICIOS`(C) | A,C |
| `/v11_stack_file_organization_system` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `VOLUMEN`(A) | A |
| `/v11_stack_automation_personal_stack` | `ADJUNTOS`(A), `HERRAMIENTAS`(A), `PROCESOS`(C) | A,C |
| `/v11_stack_learning_environment` | `ADJUNTOS`(A), `HERRAMIENTAS`(A), `INTERESES`(C) | A,C |
| `/v11_meta_conversation_design_ia` | `ADJUNTOS`(A), `COMPLEJIDAD`(A), `TAREA`(A) | A |
| `/v11_meta_prompt_portfolio_review` | `ADJUNTOS`(A), `PORTFOLIO`(B) | B,A |
| `/v11_meta_ai_collaboration_protocol` | `ADJUNTOS`(A), `FRECUENCIA`(C), `USO`(C) | A,C |
| `/v11_engine_template_generator` | `ADJUNTOS`(A), `DATOS`(A), `TIPO_DOC`(C) | A,C |
| `/v11_engine_feedback_collector` | `ADJUNTOS`(A), `CANALES`(C), `PRODUCTO`(A) | A,C |
| `/v11_presentacion_retrospective_showcase` | `ADJUNTOS`(A), `EQUIPO`(A), `PERIODO`(B) | B,A |
| `/v11_presentacion_elevator_visual` | `ADJUNTOS`(A), `METRICA`(C), `PROPUESTA`(C) | A,C |
| `/v11_comunicacion_weekly_team_update` | `ADJUNTOS`(A), `EQUIPO`(A), `PERIODO`(C) | A,C |
| `/v11_comunicacion_apology_profesional` | `ADJUNTOS`(A), `PERSONA`(A), `SITUACION`(A) | A |
| `/v11_creatividad_metaphor_generator` | `ADJUNTOS`(A), `CONCEPTO`(A) | A |
| `/v11_creatividad_idea_incubator` | `ADJUNTOS`(A), `IDEA`(B) | B,A |
| `/v11_creatividad_lateral_connection` | `ADJUNTOS`(A), `CONCEPTO_A`(C), `CONCEPTO_B`(C) | A,C |
| `/v11_negociacion_win_win_crear` | `ADJUNTOS`(A), `CONTEXTO`(A), `INTERESES`(C) | A,C |
| `/v11_negociacion_email_followup` | `ADJUNTOS`(A), `CONTEXTO`(A), `OBJETIVO`(A) | A |
| `/v11_bienestar_focus_music_protocol` | `ADJUNTOS`(A), `PREFERENCIAS`(C), `TIPO_TRABAJO`(C) | A,C |
| `/v11_bienestar_gratitude_journal_protocol` | `ADJUNTOS`(A), `MOMENTO`(C) | A,C |
| `/v11_meta_spec_generator` | `AUDIENCIA`(A), `RESTRICCION`(B), `TAREA_VAGA`(B), `TU_ROL`(B) | B,A |
| `/v11_eng_constitutional_guardrail` | `MODELO`(B), `PRODUCTO_O_FLUJO`(B), `principio_fallido`(C) | B,C |
| `/v11_eng_self_consistency_voting` | `DOMINIO`(B), `N`(B), `PROBLEMA`(A) | A,B |
| `/v11_eng_injection_defense` | `TAREA`(A), `categoria`(A) | A |
| `/v11_eng_rag_wrapper` | `DOMINIO`(B), `PREGUNTA`(B), `aspecto_faltante`(C) | B,C |
| `/v11_eng_multimodal_audit` | `ILEGIBLE`(C), `TIPO_DE_ARTEFACTO`(B) | B,C |
| `/v11_agt_orchestrator_pwc` | `N`(C), `TAREA`(A) | A,C |
| `/v11_vert_legal_contract_review` | `CLAUSULAS_CLAVE`(B), `JURISDICCION`(B), `PARTE_A`(B), `PARTE_B`(B) | B |
| `/v11_vert_legal_compliance_gap` | `MARCO_REGULATORIO`(B), `SECTOR`(A) | A,B |
| `/v11_vert_legal_privacy_dpia` | `MARCO_PROTECCION_DATOS`(B), `PRODUCTO_O_PROCESO`(B) | B |
| `/v11_vert_salud_clinical_summary` | `CUADRO`(B), `PENDIENTE`(A), `ROL_CLINICO`(B) | A,B |
| `/v11_vert_salud_triage_protocol` | `PROTOCOLO`(B) | B |
| `/v11_vert_salud_patient_education` | `CONDICION`(B), `NIVEL_LECTURA`(B) | B |
| `/v11_vert_rpa_process_discovery` | `AREA`(B), `FRECUENCIA`(B), `PROCESO`(A) | A,B |
| `/v11_vert_rpa_exception_catalog` | `PROCESO`(A) | A |
| `/v11_vert_rpa_roi_framework` | `MEDIDO`(C), `PROCESO`(A) | A,C |
| `/v11_vert_educacion_rubrica_dua` | `MATERIA`(B), `NIVEL_EDUCATIVO`(B) | B |
| `/v11_vert_educacion_plan_clase` | `MINUTOS`(B), `NIVEL`(B), `TEMA`(A) | A,B |
| `/v11_vert_educacion_feedback_student` | `ASIGNATURA`(B) | B |
| `/v11_vert_gobierno_asis_mapping` | `PROCESO`(A), `UNIDAD`(B) | B,A |
| `/v11_vert_gobierno_stakeholder_map` | `PROYECTO`(A) | A |
| `/v11_vert_gobierno_governance_framework` | `TAREA`(A) | A |
| `/v11_artefacto_5_fuerzas_porter` | `adjuntos`(A), `empresa`(A), `industria`(A) | A |
| `/v11_artefacto_accessibility_audit` | `adjuntos`(A), `nivel_wcag`(C), `producto`(A) | A,C |
| `/v11_artefacto_analisis_campo_fuerzas` | `adjuntos`(A), `cambio_propuesto`(B), `contexto`(A) | B,A |
| `/v11_artefacto_analisis_gap` | `adjuntos`(A), `area`(C), `estado_actual`(C), `estado_deseado`(C) | A,C |
| `/v11_artefacto_analisis_pareto` | `adjuntos`(A), `categorias`(A), `datos`(A), `problema`(A) | A |
| `/v11_artefacto_analisis_pestel` | `adjuntos`(A), `contexto`(A), `tema`(A) | A |
| `/v11_artefacto_analisis_vrio` | `adjuntos`(A), `empresa`(A), `recurso`(B) | B,A |
| `/v11_artefacto_balanced_scorecard` | `adjuntos`(A), `estrategia`(C), `organizacion`(C) | A,C |
| `/v11_artefacto_benchmarking` | `adjuntos`(A), `competidores`(C), `dimensiones`(B), `empresa`(A) | B,A,C |
| `/v11_artefacto_business_case` | `adjuntos`(A), `horizonte`(C), `iniciativa`(C), `inversion`(C) | A,C |
| `/v11_artefacto_cadena_valor_porter` | `adjuntos`(A), `empresa`(A), `industria`(A) | A |
| `/v11_artefacto_canvas_modelo_negocio` | `adjuntos`(A), `empresa`(A), `mercado`(C), `producto`(A), `ref_previa`(C) | A,C |
| `/v11_artefacto_canvas_propuesta_valor` | `adjuntos`(A), `audiencia`(A), `beneficio`(C), `producto`(A), `ref_previa`(C) | A,C |
| `/v11_artefacto_cronograma_proyecto_gantt` | `adjuntos`(A), `dependencias`(B), `duracion`(A), `proyecto`(A), `ref_previa`(C), `tareas`(C) | B,A,C |
| `/v11_artefacto_customer_journey_map` | `adjuntos`(A), `etapas`(B), `persona`(A), `servicio`(C) | B,A,C |
| `/v11_artefacto_decision_matrix` | `adjuntos`(A), `criterios`(A), `decision`(A), `opciones`(C) | A,C |
| `/v11_artefacto_design_system` | `adjuntos`(A), `alcance`(A), `producto`(A) | A |
| `/v11_artefacto_diagrama_ishikawa` | `adjuntos`(A), `contexto`(A), `problema`(A) | A |
| `/v11_artefacto_experience_map` | `adjuntos`(A), `contexto`(A), `experiencia`(B) | B,A |
| `/v11_artefacto_impact_effort_matrix` | `adjuntos`(A), `criterio_impacto`(C), `iniciativas`(B) | B,A,C |
| `/v11_artefacto_information_architecture` | `adjuntos`(A), `contenido`(B), `producto`(A) | B,A |
| `/v11_artefacto_kano_model` | `adjuntos`(A), `caracteristicas`(B), `producto`(A) | B,A |
| `/v11_artefacto_lean_canvas` | `adjuntos`(A), `idea`(B), `problema`(A) | B,A |
| `/v11_artefacto_mapa_empatia` | `adjuntos`(A), `situacion`(A), `usuario`(B) | B,A |
| `/v11_artefacto_mapa_procesos_bpmn` | `adjuntos`(A), `alcance`(A), `proceso`(A) | A |
| `/v11_artefacto_matriz_ansoff` | `adjuntos`(A), `mercado`(B), `objetivo_crecimiento`(B), `producto`(A) | B,A |
| `/v11_artefacto_matriz_bcg` | `adjuntos`(A), `empresa`(A), `unidades`(C) | A,C |
| `/v11_artefacto_matriz_eisenhower` | `adjuntos`(A), `objetivo`(A), `tareas`(C) | A,C |
| `/v11_artefacto_matriz_raci` | `actividades`(C), `adjuntos`(A), `proyecto`(A) | A,C |
| `/v11_artefacto_matriz_swot_completa` | `adjuntos`(A), `contexto`(A), `entidad`(B), `horizonte`(C), `ref_previa`(C) | B,A,C |
| `/v11_artefacto_north_star_metric` | `adjuntos`(A), `contexto`(A), `producto`(A) | A |
| `/v11_artefacto_okr` | `adjuntos`(A), `objetivo`(A), `resultados_clave`(C) | A,C |
| `/v11_artefacto_priorizacion_moscow` | `adjuntos`(A), `contexto`(A), `requerimientos`(B) | B,A |
| `/v11_artefacto_risk_matrix` | `adjuntos`(A), `proyecto`(A), `riesgos`(A) | A |
| `/v11_artefacto_root_cause_5_whys` | `adjuntos`(A), `contexto`(A), `problema`(A) | A |
| `/v11_artefacto_service_blueprint` | `adjuntos`(A), `escenario`(B), `servicio`(B) | B,A |
| `/v11_artefacto_sesion_lluvia_ideas` | `adjuntos`(A), `cantidad`(C), `criterio_priorizacion`(C), `ref_previa`(C), `semilla`(C) | A,C |
| `/v11_artefacto_stakeholder_map` | `adjuntos`(A), `proyecto`(A), `stakeholders`(A) | A |
| `/v11_artefacto_strategic_roadmap` | `adjuntos`(A), `objetivos`(A), `vision`(B) | B,A |
| `/v11_artefacto_strategy_canvas` | `adjuntos`(A), `competidores`(C), `industria`(A), `mi_propuesta`(C) | A,C |
| `/v11_artefacto_usability_heuristics` | `adjuntos`(A), `flujo`(C), `producto`(A) | A,C |
| `/v11_artefacto_user_persona` | `adjuntos`(A), `contexto`(A), `producto`(A) | A |
| `/v11_artefacto_value_stream_map` | `adjuntos`(A), `proceso`(A), `producto`(A) | A |
| `/v11_artefacto_voice_of_customer` | `adjuntos`(A), `fuentes`(A), `producto`(A) | A |
| `/v11_artefacto_wireframe_specification` | `adjuntos`(A), `pantalla`(B), `plataforma`(B) | B,A |
| `/v11_artefacto_assumption_map` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_evidence_hierarchy` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_issue_tree` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_mece_tree` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_minto_pyramid_memo` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_premortem_canvas` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_postmortem_review` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_cynefin_context_map` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_probabilistic_decision_table` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_expected_value_sheet` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_literature_review_matrix` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_fact_check_memo` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_competitive_teardown` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_interview_discussion_guide` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_problem_framing_brief` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_jtbd_forces_map` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_double_diamond_brief` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_user_story_map` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_persona_matrix` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_opportunity_solution_tree` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_accessibility_backlog` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_feature_prioritization_scorecard` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_release_scope_board` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_experiment_backlog` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_sipoc` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_sop` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_pdca_sheet` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_dmaic_charter` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_a3_problem_solving` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_constraints_tree` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_fmea_worksheet` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_raid_log` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_kanban_board` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_delegation_board` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_one_on_one_agenda` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_decision_log` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_rapid_decision_matrix` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_sbi_feedback_note` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_change_readiness_assessment` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_communication_plan` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_executive_memo` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_faq_architecture` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_objection_handling_matrix` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_negotiation_prep_sheet` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_batna_worksheet` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_hypothesis_sheet` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_kpi_tree` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_funnel_analysis_canvas` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_cohort_analysis_table` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_monte_carlo_scenario_sheet` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_data_quality_scorecard` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_rag_architecture_canvas` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_agent_workflow_map` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_prompt_chain_map` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_hitl_review_matrix` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_artefacto_ai_governance_charter` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m001` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m002` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m003` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m004` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m005` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m006` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m007` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m008` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m009` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m010` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m011` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m012` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m013` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m014` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m015` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m016` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m017` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m018` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m019` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m020` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m021` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m022` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m023` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m024` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m025` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m026` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m027` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m028` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m029` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m030` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m031` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m032` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m033` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m034` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m035` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m036` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m037` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m038` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m039` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m040` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m041` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m042` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m043` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m044` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m045` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m046` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m047` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m048` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m049` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m050` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m051` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m052` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m053` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m054` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m055` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m056` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m057` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m058` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m059` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m060` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m061` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m062` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m063` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m064` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m065` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m066` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m067` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m068` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m069` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m070` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m071` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m072` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m073` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m074` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m075` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m076` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m077` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m078` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m079` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m080` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m081` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m082` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m083` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m084` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m085` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m086` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m087` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m088` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m089` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m090` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m091` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m092` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m093` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m094` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m095` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m096` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m097` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m098` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m099` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m100` | `CASO`(A), `CONTEXTO`(A) | A |
| `/v11_m101` | `CASO`(A), `CONTEXTO`(A) | A |
| `/0` | `adjuntos`(A), `sensibilidad`(C), `tipo_sesion`(C) | A,C |
| `/1` | `fuente_contexto`(C), `pedido_recibido`(C), `sospecha_inicial`(C) | C |
| `/2` | `entregable`(B), `necesidad`(B), `restricciones`(A) | A,B |
| `/3` | `recursos`(B), `riesgos`(A), `spec`(B) | A,B |
| `/4` | `energia`(B), `insumos_crudos`(B), `spec_plan`(B) | B |
| `/5` | `areas_debiles`(B), `borrador`(A), `tipo_evidencia`(B) | A,B |
| `/6` | `audiencia`(A), `longitud`(A), `version_robusta`(B) | B,A |
| `/7` | `criterio`(A), `entregable`(B), `tolerancia`(B) | B,A |
| `/8` | `audiencia`(A), `canal`(B), `entregable`(B) | B,A |
| `/9` | `frecuencia`(B), `proceso`(A), `proximo_usuario`(B) | A,B |
| `/argumenta` | `TESIS`(B) | B |
| `/aterriza` | `TEMA`(A) | A |
| `/auditoria` | `OBJETO`(B) | B |
| `/automatiza` | `PROCESO`(A) | A |
| `/b` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/benchmark` | `METRICA`(B), `SECTOR`(A) | A,B |
| `/c` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/calibra` | `AUDIENCIA`(A) | A |
| `/compara` | `OPCIONES`(B) | B |
| `/conecta` | `CONCEPTO_A`(B), `CONCEPTO_B`(B) | B |
| `/contextualiza` | `TEMA`(A) | A |
| `/cuantifica` | `TEMA`(A) | A |
| `/d` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/debate` | `TEMA`(A) | A |
| `/defiende` | `POSICION`(B) | B |
| `/desafia` | `PROPUESTA`(B) | B |
| `/diagnostica` | `SITUACION`(A) | A |
| `/diagrama` | `CONCEPTO`(A) | A |
| `/documenta` | `CONTENIDO`(B) | B |
| `/empatiza` | `PERSONA`(A) | A |
| `/escala` | `SOLUCION`(B) | B |
| `/escenarios` | `SITUACION`(A) | A |
| `/estrategia` | `OBJETIVO`(A) | A |
| `/estructura` | `CONTENIDO`(B) | B |
| `/evalua` | `OBJETO`(B) | B |
| `/f` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/feedback` | `COMPORTAMIENTO`(B) | B |
| `/g` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/h` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/i` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/investiga` | `FUENTE`(B), `TEMA`(A) | A,B |
| `/j` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/k` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/l` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/m` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/mapea` | `CONCEPTO`(A) | A |
| `/n` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/narrativa` | `DATOS`(A) | A |
| `/o` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/operacionaliza` | `PLAN`(B) | B |
| `/optimiza` | `PROCESO`(A) | A |
| `/p` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/pareto` | `LISTA`(A) | A |
| `/personaliza` | `ROL`(A), `SECTOR`(A) | A |
| `/predice` | `SITUACION`(A) | A |
| `/prioriza` | `ITEMS`(A) | A |
| `/profundiza` | `TEMA`(A) | A |
| `/prototipa` | `IDEA`(B) | B |
| `/q` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/r` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/reformula` | `AUDIENCIA`(A) | A |
| `/resume` | `CONTENIDO`(B) | B |
| `/reversa` | `TEMA_SESION`(B) | B |
| `/segmenta` | `PROYECTO`(A) | A |
| `/simplifica` | `CONTENIDO`(B) | B |
| `/sintetiza` | `TEMA`(A) | A |
| `/t` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/u` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/v` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/verifica` | `TEMA`(A) | A |
| `/visualiza` | `DATOS`(A) | A |
| `/w` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/x` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/y` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/z` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/ñ` | `DIRECCION`(C), `IDIOMA_DESTINO`(C), `IDIOMA_INSUMO`(C), `MODO_TRADUCCION`(C), `REGISTRO_OBJETIVO`(C), `TONO_OBJETIVO`(C) | C |
| `/10-10-10-perspectiva` | `ADJUNTOS`(A), `DECISION`(A) | A |
| `/5-whys` | `CASO`(A), `CONTEXTO`(A) | A |
| `/6-sombreros-rapido` | `ADJUNTOS`(A), `DECISION`(A) | A |
| `/a-b-testing` | `CASO`(A), `CONTEXTO`(A) | A |
| `/a3-problem-solving` | `CASO`(A), `CONTEXTO`(A) | A |
| `/a3-problem-solving-artefactos` | `CASO`(A), `CONTEXTO`(A) | A |
| `/ab-test-disenar` | `ADJUNTOS`(A), `CAMBIO`(B), `METRICA`(B), `TRAFICO`(C) | B,A,C |
| `/abstraction-laddering` | `ADJUNTOS`(A), `PROBLEMA`(A) | A |
| `/accessibility-backlog` | `CASO`(A), `CONTEXTO`(A) | A |
| `/accountability-system` | `ADJUNTOS`(A), `HORIZONTE`(C), `OBJETIVOS`(A) | A,C |
| `/active-recall-practice` | `ADJUNTOS`(A), `MATERIAL`(B), `OBJETIVO`(A) | B,A |
| `/adkar` | `CASO`(A), `CONTEXTO`(A) | A |
| `/agent-workflow-design` | `CASO`(A), `CONTEXTO`(A) | A |
| `/agent-workflow-map` | `CASO`(A), `CONTEXTO`(A) | A |
| `/ai-collaboration-protocol` | `ADJUNTOS`(A), `FRECUENCIA`(C), `USO`(C) | A,C |
| `/ai-daily-briefing` | `ADJUNTOS`(A), `FUENTES`(A), `SECTOR`(A) | A |
| `/ai-governance-charter` | `CASO`(A), `CONTEXTO`(A) | A |
| `/ai-governance-framework` | `CASO`(A), `CONTEXTO`(A) | A |
| `/ai-tools-portfolio` | `ADJUNTOS`(A), `HERRAMIENTAS_IA`(C), `TAREAS`(B) | B,A,C |
| `/aida` | `CASO`(A), `CONTEXTO`(A) | A |
| `/analisis-automatizado-datos` | `ADJUNTOS`(A), `DATOS`(A), `FRECUENCIA`(B), `METRICAS`(A) | B,A |
| `/analisis-bibliometrico` | `ADJUNTOS`(A), `CAMPO`(B), `PERIODO`(B) | B,A |
| `/analisis-causal-fishbone` | `ADJUNTOS`(A), `CONTEXTO`(A), `PROBLEMA`(A) | A |
| `/analisis-competitivo-5-fuerzas` | `ADJUNTOS`(A), `EMPRESA`(A), `SECTOR`(A) | A |
| `/analisis-exploratorio-dataset` | `ADJUNTOS`(A), `DATASET`(B), `HERRAMIENTA`(A), `PREGUNTA`(C) | B,A,C |
| `/analisis-redes-influencia` | `ADJUNTOS`(A), `ECOSISTEMA`(B), `OBJETIVO`(A) | B,A |
| `/analisis-sensibilidad` | `ADJUNTOS`(A), `DECISION`(A), `SUPUESTOS`(A) | A |
| `/analisis-sentimiento-marca` | `ADJUNTOS`(A), `MARCA`(A), `PERIODO`(C) | A,C |
| `/analisis-swot-estrategico` | `ADJUNTOS`(A), `ORGANIZACION`(C), `SECTOR`(A) | A,C |
| `/analizar-trade-offs` | `ADJUNTOS`(A), `CONTEXTO`(A), `OPCIONES`(B) | B,A |
| `/analogia-transferir-solucion` | `ADJUNTOS`(A), `DOMINIO`(B), `PROBLEMA`(A) | B,A |
| `/anomaly-detection-manual` | `ADJUNTOS`(A), `DATASET`(B), `VARIABLES`(C) | B,A,C |
| `/antifragil-plan` | `ADJUNTOS`(A), `PLAN`(B) | B,A |
| `/api-keys-organizar` | `ADJUNTOS`(A), `SERVICIOS`(C) | A,C |
| `/apology-profesional` | `ADJUNTOS`(A), `PERSONA`(A), `SITUACION`(A) | A |
| `/articulo-blog-seo` | `ADJUNTOS`(A), `AUDIENCIA`(A), `KEYWORD`(B), `LONGITUD`(A) | B,A |
| `/asistente-corporativo-privado` | `ADJUNTOS`(A), `FUENTES`(A), `ORGANIZACION`(B), `SCOPE`(B) | B,A |
| `/assumption-map` | `CASO`(A), `CONTEXTO`(A) | A |
| `/assumption-mapping` | `ADJUNTOS`(A), `PLAN`(B) | B,A |
| `/assumption-mapping-metodos` | `CASO`(A), `CONTEXTO`(A) | A |
| `/async-communication-protocol` | `ADJUNTOS`(A), `EQUIPO`(A), `HERRAMIENTAS`(A), `ZONA_HORARIA`(C) | A,C |
| `/auditar-herramientas-personal` | `ADJUNTOS`(A), `HERRAMIENTAS`(A), `PRESUPUESTO`(A) | A |
| `/auditar-mis-prompts` | `ADJUNTOS`(A), `PROMPTS`(B) | B,A |
| `/auditar-tiempo-semanal` | `ACTIVIDADES`(B), `ADJUNTOS`(A), `HORAS_TRABAJO`(C), `OBJETIVO`(A) | A,B,C |
| `/automated-report-disenar` | `ADJUNTOS`(A), `FUENTE`(B), `HERRAMIENTA`(A), `REPORTE`(B) | B,A |
| `/automation-personal-stack` | `ADJUNTOS`(A), `HERRAMIENTAS`(A), `PROCESOS`(B) | B,A |
| `/automatizar-proceso-recurrente` | `ADJUNTOS`(A), `FRECUENCIA`(B), `HERRAMIENTAS`(A), `PROCESO`(A) | B,A |
| `/backup-datos-personal` | `ADJUNTOS`(A), `DATOS`(A), `HERRAMIENTAS`(A) | A |
| `/bad-news-delivery` | `ADJUNTOS`(A), `NOTICIA`(C), `RECEPTOR`(B) | B,A,C |
| `/balanced-scorecard` | `CASO`(A), `CONTEXTO`(A) | A |
| `/batch-processing-tareas` | `ADJUNTOS`(A), `HORARIO`(C), `TAREAS_RECURRENTES`(C) | A,C |
| `/batna-prep` | `CASO`(A), `CONTEXTO`(A) | A |
| `/batna-worksheet` | `CASO`(A), `CONTEXTO`(A) | A |
| `/bayesiano-actualizar-creencias` | `ADJUNTOS`(A), `CREENCIA`(B), `EVIDENCIA`(A) | B,A |
| `/bcg-matrix` | `CASO`(A), `CONTEXTO`(A) | A |
| `/before-after-transformacion` | `ADJUNTOS`(A), `AFTER`(B), `BEFORE`(B), `METRICA`(B) | B,A |
| `/benchmark-competitivo` | `ADJUNTOS`(A), `COMPETIDORES`(B), `METRICAS`(A), `SECTOR`(A) | B,A |
| `/benchmarking` | `CASO`(A), `CONTEXTO`(A) | A |
| `/blue-ocean-errc-strategy-canvas` | `CASO`(A), `CONTEXTO`(A) | A |
| `/blue-ocean-oportunidad` | `ADJUNTOS`(A), `PRODUCTO`(A), `SECTOR`(A) | A |
| `/bluf` | `CASO`(A), `CONTEXTO`(A) | A |
| `/board-meeting` | `ADJUNTOS`(A), `EMPRESA`(A), `PERIODO`(C) | A,C |
| `/boundaries-profesionales` | `ADJUNTOS`(A), `ROL`(A), `VIOLACIONES`(C) | A,C |
| `/bpmn-process-mapping` | `CASO`(A), `CONTEXTO`(A) | A |
| `/brain-dump-estructurado` | `ADJUNTOS`(A), `CONTEXTO`(A), `HERRAMIENTAS`(A) | A |
| `/brainstorm-100-ideas` | `ADJUNTOS`(A), `DESAFIO`(B), `RESTRICCIONES`(A) | B,A |
| `/brand-kit-personal` | `ADJUNTOS`(A), `CANALES`(B), `NOMBRE`(A), `VALORES`(C) | B,A,C |
| `/brand-voice-document` | `ADJUNTOS`(A), `AUDIENCIA`(A), `MARCA`(A), `REFERENCIAS`(C), `VALORES`(C) | A,C |
| `/brief-creativo-imagen-ia` | `ADJUNTOS`(A), `CONCEPTO`(A), `ESTILO`(A), `USO`(C) | A,C |
| `/browser-productividad` | `ADJUNTOS`(A), `BROWSER`(B), `USO`(C) | B,A,C |
| `/business-case-crear` | `ADJUNTOS`(A), `INVERSION`(B), `PROYECTO`(A) | B,A |
| `/business-model-canvas` | `CASO`(A), `CONTEXTO`(A) | A |
| `/calcular-roi-personal` | `ADJUNTOS`(A), `HORAS_SEMANALES`(C), `INICIATIVA`(B), `VALOR_HORA`(C) | B,A,C |
| `/calendar-blocking-auto` | `ADJUNTOS`(A), `HORARIO`(C), `PRIORIDADES`(B) | B,A,C |
| `/case-competition` | `ADJUNTOS`(A), `CASO`(A), `DURACION`(A) | A |
| `/caso-estudio-analisis` | `ADJUNTOS`(A), `CASO`(A), `CONTEXTO`(A) | A |
| `/caso-exito-cliente` | `ADJUNTOS`(A), `CLIENTE`(A), `DETALLES`(C), `RESULTADO`(B) | B,A,C |
| `/caso-real-resolver` | `ADJUNTOS`(A), `COMPETENCIAS`(B), `PROBLEMA`(A) | B,A |
| `/causal-impact-reasoning` | `CASO`(A), `CONTEXTO`(A) | A |
| `/certificacion-portafolio` | `ADJUNTOS`(A), `CERTIFICACION`(B), `HITOS`(B) | B,A |
| `/chain-prompts-workflow` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `TAREA`(A) | A |
| `/change-readiness-assessment` | `CASO`(A), `CONTEXTO`(A) | A |
| `/change-readiness-assessment-artefactos` | `CASO`(A), `CONTEXTO`(A) | A |
| `/chatbot-ventas-calificacion` | `ADJUNTOS`(A), `CRM`(B), `ICP`(C), `PRODUCTO`(A) | B,A,C |
| `/churn-diagnostico` | `ADJUNTOS`(A), `CHURN_ACTUAL`(C), `DATOS`(A), `PRODUCTO`(A) | A,C |
| `/cognitive-bias-audit` | `ADJUNTOS`(A), `CONTEXTO`(A), `DECISION`(A) | A |
| `/cohort-analysis` | `ADJUNTOS`(A), `DATOS`(A), `METRICA`(B), `PRODUCTO`(A) | B,A |
| `/cohort-analysis-metodos` | `CASO`(A), `CONTEXTO`(A) | A |
| `/cohort-analysis-table` | `CASO`(A), `CONTEXTO`(A) | A |
| `/cold-outreach` | `ADJUNTOS`(A), `OBJETIVO`(A), `PERSONA`(A) | A |
| `/comite-operativo-artificial` | `ADJUNTOS`(A), `ENTREGABLE`(B), `ESTANDAR`(C) | B,A,C |
| `/communication-plan` | `CASO`(A), `CONTEXTO`(A) | A |
| `/community-learning` | `ADJUNTOS`(A), `NIVEL`(B), `TEMA`(A) | B,A |
| `/competitive-intelligence-continua` | `ADJUNTOS`(A), `COMPETIDORES`(B), `EMPRESA`(A), `SECTOR`(A) | B,A |
| `/competitive-moat` | `ADJUNTOS`(A), `COMPETIDORES`(C), `EMPRESA`(A) | A,C |
| `/competitive-positioning` | `ADJUNTOS`(A), `AUDIENCIA`(A), `COMPETIDORES`(C), `PRODUCTO`(A) | A,C |
| `/competitive-teardown` | `CASO`(A), `CONTEXTO`(A) | A |
| `/competitive-teardown-artefactos` | `CASO`(A), `CONTEXTO`(A) | A |
| `/comunicacion-no-violenta` | `CASO`(A), `CONTEXTO`(A) | A |
| `/comunicado-interno` | `ADJUNTOS`(A), `AUDIENCIA`(A), `CAMBIO`(C), `TIMELINE`(B) | B,A,C |
| `/conflict-resolution` | `ADJUNTOS`(A), `CONFLICTO`(B), `PARTES`(B) | B,A |
| `/consensus-vs-consent` | `ADJUNTOS`(A), `DECISION`(A), `GRUPO`(B) | B,A |
| `/constitutional-guardrail` | `MODELO`(B), `PRODUCTO_O_FLUJO`(B) | B |
| `/constraint-driven-design` | `ADJUNTOS`(A), `PROBLEMA`(A), `RESTRICCIONES`(A) | A |
| `/constraints-tree` | `CASO`(A), `CONTEXTO`(A) | A |
| `/contenido-educativo-visual` | `ADJUNTOS`(A), `AUDIENCIA`(A), `TEMA`(A) | A |
| `/contenido-onboarding` | `ADJUNTOS`(A), `AHA_MOMENT`(C), `AUDIENCIA`(A), `PRODUCTO`(A) | A,C |
| `/content-generator-marca` | `ADJUNTOS`(A), `BRAND_VOICE`(C), `CONTENIDO`(B), `MARCA`(A) | B,A,C |
| `/content-repurposing` | `ADJUNTOS`(A), `CANALES`(B), `CONTENIDO`(B) | B,A |
| `/context-switching-minimizar` | `ADJUNTOS`(A), `ENTORNO`(C), `HERRAMIENTAS`(A), `INTERRUPCIONES`(B) | B,A,C |
| `/contrato-revisar` | `ADJUNTOS`(A), `CONTRATO`(B), `ROL`(A) | B,A |
| `/conversacion-dificil` | `ADJUNTOS`(A), `OBJETIVO`(A), `PERSONA`(A), `SITUACION`(A) | A |
| `/conversation-design-ia` | `ADJUNTOS`(A), `COMPLEJIDAD`(A), `TAREA`(A) | A |
| `/conversational-ux-disenar` | `ADJUNTOS`(A), `AGENTE`(A), `AUDIENCIA`(A) | A |
| `/copy-landing-page` | `ADJUNTOS`(A), `AUDIENCIA`(A), `PRODUCTO`(A), `PROPUESTA_VALOR`(C) | A,C |
| `/copy-producto-features` | `ADJUNTOS`(A), `CLIENTE`(A), `FEATURES`(B), `PRODUCTO`(A) | B,A |
| `/cost-benefit-rapido` | `ADJUNTOS`(A), `DECISION`(A) | A |
| `/crear-spec-alto-rendimiento` | `ADJUNTOS`(A), `COMPLEJIDAD`(A), `CONTEXTO`(A), `OBJETIVO`(A) | A |
| `/crear-system-prompt-agente` | `ADJUNTOS`(A), `AGENTE`(A), `AUDIENCIA`(A), `AUTONOMIA`(B) | B,A |
| `/crm-pipeline-flujo` | `ADJUNTOS`(A), `CRM`(B), `EQUIPO`(A), `PROCESO_VENTAS`(C) | B,A,C |
| `/cultura-equipo-disenar` | `ADJUNTOS`(A), `EQUIPO`(A), `ESTADO_ACTUAL`(C) | A,C |
| `/curacion-recursos` | `ADJUNTOS`(A), `NIVEL`(C), `TEMA`(A), `TIEMPO`(C) | A,C |
| `/curar-knowledge-sources` | `ADJUNTOS`(A), `AGENTE`(A), `DOMINIO`(C) | A,C |
| `/customer-journey-map` | `CASO`(A), `CONTEXTO`(A) | A |
| `/customer-segmentation` | `ADJUNTOS`(A), `CLIENTES`(B), `OBJETIVO`(A), `VARIABLES`(B) | B,A |
| `/cynefin` | `CASO`(A), `CONTEXTO`(A) | A |
| `/cynefin-context-map` | `CASO`(A), `CONTEXTO`(A) | A |
| `/dar-autonomia-calibrada` | `ADJUNTOS`(A), `PERSONA`(A), `TAREA`(A) | A |
| `/dashboard-metricas-disenar` | `ADJUNTOS`(A), `AUDIENCIA`(A), `HERRAMIENTA`(A), `PROCESO`(A) | A |
| `/data-collection-plan` | `ADJUNTOS`(A), `PREGUNTA`(B), `RECURSOS`(C) | B,A,C |
| `/data-quality-scorecard` | `CASO`(A), `CONTEXTO`(A) | A |
| `/data-quality-scorecard-artefactos` | `CASO`(A), `CONTEXTO`(A) | A |
| `/data-storytelling-auto` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DATOS`(A) | A |
| `/data-viz-interactiva` | `ADJUNTOS`(A), `DATOS`(A), `HERRAMIENTA`(A), `HISTORIA`(B) | B,A |
| `/deadline-extensiones` | `ADJUNTOS`(A), `DEADLINE`(A), `PROYECTO`(A), `RAZON`(B) | B,A |
| `/decision-journal-registro` | `ADJUNTOS`(A), `TIPO_DECISIONES`(C) | A,C |
| `/decision-log` | `CASO`(A), `CONTEXTO`(A) | A |
| `/decision-log-governance` | `CASO`(A), `CONTEXTO`(A) | A |
| `/decision-rapida-framework` | `ADJUNTOS`(A), `CONTEXTO`(A), `DECISION_EJEMPLO`(C) | A,C |
| `/deck-inversores` | `ADJUNTOS`(A), `METRICAS`(A), `RONDA`(C), `STARTUP`(B) | B,A,C |
| `/deep-work-protocolo` | `ADJUNTOS`(A), `CONTEXTO`(A), `HORAS_DW_ACTUAL`(C), `INTERRUPCIONES`(B) | B,A,C |
| `/delegar-tarea-efectivamente` | `ADJUNTOS`(A), `EXPERIENCIA`(B), `RECEPTOR`(B), `TAREA`(A) | B,A |
| `/delegation-board` | `CASO`(A), `CONTEXTO`(A) | A |
| `/delegation-levels` | `CASO`(A), `CONTEXTO`(A) | A |
| `/deliberate-practice` | `ADJUNTOS`(A), `HABILIDAD`(B), `NIVEL`(C) | B,A,C |
| `/demo-day-preparar` | `ADJUNTOS`(A), `AUDIENCIA`(A), `PROYECTO`(A), `RESULTADOS`(B) | B,A |
| `/demo-producto` | `ADJUNTOS`(A), `PAIN_POINTS`(C), `PRODUCTO`(A), `PROSPECTO`(B) | B,A,C |
| `/desarrollar-talento` | `ADJUNTOS`(A), `ASPIRACION`(C), `PERSONA`(A), `ROL_ACTUAL`(C) | A,C |
| `/design-thinking` | `CASO`(A), `CONTEXTO`(A) | A |
| `/design-thinking-problema` | `ADJUNTOS`(A), `PROBLEMA`(A), `USUARIO`(B) | B,A |
| `/devil-advocate-protocolo` | `ADJUNTOS`(A), `CONTEXTO`(A), `PROPUESTA`(B) | B,A |
| `/diagrama-arquitectura` | `ADJUNTOS`(A), `AUDIENCIA`(A), `NIVEL`(B), `SISTEMA`(B) | B,A |
| `/dialectico-tesis-antitesis` | `ADJUNTOS`(A), `POSICION_A`(C), `POSICION_B`(C) | A,C |
| `/digital-detox-plan` | `ADJUNTOS`(A), `APPS_PROBLEMA`(C), `SCREEN_TIME`(C) | A,C |
| `/digital-minimalism-plan` | `ADJUNTOS`(A), `HERRAMIENTAS`(A) | A |
| `/disenar-custom-gpt` | `ADJUNTOS`(A), `AUDIENCIA`(A), `TAREA`(A), `TONO`(A) | A |
| `/disenar-ritual-matutino` | `ADJUNTOS`(A), `ENERGIA_ACTUAL`(C), `HORA_DESPERTAR`(B), `PROFESION`(B) | B,A,C |
| `/disenar-sistema-habitos` | `ADJUNTOS`(A), `HABITOS_ACTUALES`(C), `OBJETIVO`(A), `TIEMPO_DIARIO`(C) | A,C |
| `/diseno-social-media-kit` | `ADJUNTOS`(A), `MARCA`(A), `PALETA`(B), `PLATAFORMAS`(C) | B,A,C |
| `/dmaic` | `CASO`(A), `CONTEXTO`(A) | A |
| `/dmaic-charter` | `CASO`(A), `CONTEXTO`(A) | A |
| `/documentar-asistente` | `ADJUNTOS`(A), `AGENTE`(A), `AUDIENCIA`(A) | A |
| `/dossier-empresa` | `ADJUNTOS`(A), `EMPRESA`(A), `OBJETIVO`(A) | A |
| `/double-diamond` | `CASO`(A), `CONTEXTO`(A) | A |
| `/double-diamond-brief` | `CASO`(A), `CONTEXTO`(A) | A |
| `/due-diligence-rapida` | `ADJUNTOS`(A), `ENTIDAD`(B), `TIPO`(A) | B,A |
| `/educacion-feedback-student` | `ASIGNATURA`(B) | B |
| `/educacion-plan-clase` | `MINUTOS`(B), `NIVEL`(B), `TEMA`(A) | A,B |
| `/educacion-rubrica-dua` | `MATERIA`(B), `NIVEL_EDUCATIVO`(B) | B |
| `/eisenhower-priorizar` | `ADJUNTOS`(A), `TAREAS`(B) | B,A |
| `/elaboration-tecnica` | `ADJUNTOS`(A), `CONCEPTO`(A), `CONOCIMIENTO_PREVIO`(C) | A,C |
| `/elevator-pitch` | `ADJUNTOS`(A), `AUDIENCIA`(A), `EMPRESA`(A), `PROPUESTA`(B) | B,A |
| `/elevator-visual` | `ADJUNTOS`(A), `METRICA`(C), `PROPUESTA`(B) | B,A,C |
| `/email-alto-impacto` | `ADJUNTOS`(A), `CONTEXTO`(A), `DESTINATARIO`(C), `OBJETIVO`(A), `TONO`(A) | A,C |
| `/email-cero-friccion` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `RESPUESTAS_COMUNES`(C), `VOLUMEN`(A) | A,C |
| `/email-filtros-reglas` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `VOLUMEN`(A) | A |
| `/email-followup` | `ADJUNTOS`(A), `CONTEXTO`(A), `OBJETIVO`(A) | A |
| `/email-responder-automatico` | `ADJUNTOS`(A), `TIPOS`(C), `TONO`(A), `VOLUMEN`(A) | A,C |
| `/empowerment-framework` | `ADJUNTOS`(A), `EQUIPO`(A), `NIVEL`(B) | B,A |
| `/encuesta-disenar-analizar` | `ADJUNTOS`(A), `OBJETIVO`(A), `POBLACION`(B) | B,A |
| `/energia-mapping-semanal` | `ADJUNTOS`(A), `HORARIO`(C), `TIPO_TRABAJO`(C) | A,C |
| `/energia-no-tiempo` | `ADJUNTOS`(A), `AGENDA_ACTUAL`(C), `CRONOTIPO`(C), `TAREAS_CRITICAS`(C) | A,C |
| `/energy-management-daily` | `ADJUNTOS`(A), `ENERGIA_ACTUAL`(C), `HORARIO`(C) | A,C |
| `/escalacion-profesional` | `ADJUNTOS`(A), `DESTINATARIO`(B), `IMPACTO`(B), `PROBLEMA`(A) | B,A |
| `/escalera-agentica-roadmap` | `ADJUNTOS`(A), `NIVEL_ACTUAL`(C), `OBJETIVO`(A) | A,C |
| `/evaluacion-asistente-qa` | `ADJUNTOS`(A), `ASISTENTE`(B), `SCOPE`(C) | B,A,C |
| `/evaluar-ia-herramienta` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `PROBLEMA`(A) | A |
| `/evaluar-output-ia-rubric` | `ADJUNTOS`(A), `TIPO_OUTPUT`(C) | A,C |
| `/evidence-hierarchy` | `CASO`(A), `CONTEXTO`(A) | A |
| `/evidence-hierarchy-artefactos` | `CASO`(A), `CONTEXTO`(A) | A |
| `/excel-modelo-financiero` | `ADJUNTOS`(A), `HORIZONTE`(C), `METRICAS`(A), `NEGOCIO`(C) | A,C |
| `/excellence-rubric-crear` | `ADJUNTOS`(A), `ESTANDAR`(B), `TIPO_OUTPUT`(C) | B,A,C |
| `/executive-memo` | `CASO`(A), `CONTEXTO`(A) | A |
| `/executive-memo-artefactos` | `CASO`(A), `CONTEXTO`(A) | A |
| `/expected-value-sheet` | `CASO`(A), `CONTEXTO`(A) | A |
| `/experiment-backlog` | `CASO`(A), `CONTEXTO`(A) | A |
| `/expert-interview-guide` | `ADJUNTOS`(A), `EXPERTO`(B), `OBJETIVO`(A), `TEMA`(A) | B,A |
| `/fact-check-memo` | `CASO`(A), `CONTEXTO`(A) | A |
| `/fact-check-protocol` | `CASO`(A), `CONTEXTO`(A) | A |
| `/factcheck-afirmacion` | `ADJUNTOS`(A), `AFIRMACION`(B), `CONTEXTO`(A) | B,A |
| `/faq-architecture` | `CASO`(A), `CONTEXTO`(A) | A |
| `/faq-bot-automatico` | `ADJUNTOS`(A), `FUENTE`(B), `PLATAFORMA`(C) | B,A,C |
| `/faq-completa-producto` | `ADJUNTOS`(A), `PREGUNTAS_COMUNES`(C), `PRODUCTO`(A) | A,C |
| `/faq-design` | `CASO`(A), `CONTEXTO`(A) | A |
| `/feature-prioritization-scorecard` | `CASO`(A), `CONTEXTO`(A) | A |
| `/feedback-collector` | `ADJUNTOS`(A), `CANALES`(C), `PRODUCTO`(A) | A,C |
| `/feedback-positivo-refuerzo` | `ADJUNTOS`(A), `COMPORTAMIENTO`(B), `IMPACTO`(B), `PERSONA`(A) | B,A |
| `/feynman-explicar` | `ADJUNTOS`(A), `CONCEPTO`(A), `NIVEL_ACTUAL`(C) | A,C |
| `/file-organization-system` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `VOLUMEN`(A) | A |
| `/five-forces` | `CASO`(A), `CONTEXTO`(A) | A |
| `/flywheel-diseno` | `ADJUNTOS`(A), `CRECIMIENTO`(B), `NEGOCIO`(C) | B,A,C |
| `/fmea` | `CASO`(A), `CONTEXTO`(A) | A |
| `/fmea-worksheet` | `CASO`(A), `CONTEXTO`(A) | A |
| `/focus-music-protocol` | `ADJUNTOS`(A), `PREFERENCIAS`(C), `TIPO_TRABAJO`(C) | A,C |
| `/forecast-proyeccion` | `ADJUNTOS`(A), `DATOS_HISTORICOS`(C), `HORIZONTE`(C), `METRICA`(C) | A,C |
| `/forma-trabajo-documentar` | `ADJUNTOS`(A), `PROCESOS`(B), `ROL`(A) | B,A |
| `/framework-rapido-5min` | `ADJUNTOS`(A), `CONTEXTO`(A), `DECISION`(A) | A |
| `/friction-audit-eliminar` | `ADJUNTOS`(A), `CONTEXTO`(A), `FRUSTRACIONES`(C) | A,C |
| `/funnel-analysis` | `CASO`(A), `CONTEXTO`(A) | A |
| `/funnel-analysis-canvas` | `CASO`(A), `CONTEXTO`(A) | A |
| `/funnel-conversion-analisis` | `ADJUNTOS`(A), `DATOS`(A), `ETAPAS`(B), `PRODUCTO`(A) | B,A |
| `/gemini-gem-especializado` | `ADJUNTOS`(A), `AUDIENCIA`(A), `FUNCION`(C), `SOURCES`(B) | B,A,C |
| `/gestion-estres-agudo` | `ADJUNTOS`(A), `CONTEXTO`(A) | A |
| `/go-nogo-checklist` | `ADJUNTOS`(A), `CRITERIOS`(A), `LANZAMIENTO`(B) | B,A |
| `/gobierno-asis-mapping` | `PROCESO`(A), `UNIDAD`(B) | B,A |
| `/gobierno-stakeholder-map` | `PROYECTO`(A) | A |
| `/google-sheets-formulas` | `ADJUNTOS`(A), `DATOS`(A), `PROCESO`(A) | A |
| `/gratitude-journal-protocol` | `ADJUNTOS`(A), `MOMENTO`(B) | B,A |
| `/guion-podcast` | `ADJUNTOS`(A), `DURACION`(A), `PODCAST`(B), `TEMA_EPISODIO`(C) | B,A,C |
| `/guion-video-corto` | `ADJUNTOS`(A), `DURACION`(A), `PLATAFORMA`(C), `TEMA`(A) | A,C |
| `/heuristic-evaluation` | `CASO`(A), `CONTEXTO`(A) | A |
| `/hiring-scorecard` | `ADJUNTOS`(A), `EQUIPO`(A), `ROL`(A) | A |
| `/hitl-review-matrix` | `CASO`(A), `CONTEXTO`(A) | A |
| `/html-autocontenido-dashboard` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DATOS`(A), `MARCA`(A) | A |
| `/human-in-the-loop-review` | `CASO`(A), `CONTEXTO`(A) | A |
| `/hypothesis-driven-analysis` | `CASO`(A), `CONTEXTO`(A) | A |
| `/hypothesis-sheet` | `CASO`(A), `CONTEXTO`(A) | A |
| `/icon-system-coherente` | `ADJUNTOS`(A), `ESTILO`(A), `PROYECTO`(A) | A |
| `/idea-incubator` | `ADJUNTOS`(A), `IDEA`(B) | B,A |
| `/infografia-ejecutiva` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DATOS`(A), `FORMATO`(A) | A |
| `/informe-ejecutivo` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DATOS`(A), `TEMA`(A) | A |
| `/integraciones-mapa` | `ADJUNTOS`(A), `FLUJOS`(C), `HERRAMIENTAS`(A) | A,C |
| `/interleaving-practice` | `ADJUNTOS`(A), `HABILIDADES`(B), `TIEMPO`(C) | B,A,C |
| `/internal-proposal` | `ADJUNTOS`(A), `AUDIENCIA`(A), `PROPUESTA`(B) | B,A |
| `/interview-discussion-guide` | `CASO`(A), `CONTEXTO`(A) | A |
| `/inversion` | `CASO`(A), `CONTEXTO`(A) | A |
| `/inversion-pensar-al-reves` | `ADJUNTOS`(A), `CONTEXTO`(A), `OBJETIVO`(A) | A |
| `/invoice-tracking` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `VOLUMEN`(A) | A |
| `/ishikawa-fishbone` | `CASO`(A), `CONTEXTO`(A) | A |
| `/issue-tree` | `CASO`(A), `CONTEXTO`(A) | A |
| `/issue-tree-artefactos` | `CASO`(A), `CONTEXTO`(A) | A |
| `/issue-tree-problema` | `ADJUNTOS`(A), `CONTEXTO`(A), `PROBLEMA`(A), `PROFUNDIDAD`(C) | A,C |
| `/iterative-improvement-cycle` | `ADJUNTOS`(A), `AGENTE`(A), `METRICAS_ACTUALES`(C) | A,C |
| `/jobs-to-be-done` | `ADJUNTOS`(A), `CLIENTES`(C), `PRODUCTO`(A) | A,C |
| `/jobs-to-be-done-metodos` | `CASO`(A), `CONTEXTO`(A) | A |
| `/jtbd-forces-map` | `CASO`(A), `CONTEXTO`(A) | A |
| `/kanban-board` | `CASO`(A), `CONTEXTO`(A) | A |
| `/kanban-flow-design` | `CASO`(A), `CONTEXTO`(A) | A |
| `/kanban-personal-flujo` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `ROL`(A) | A |
| `/kano-model` | `CASO`(A), `CONTEXTO`(A) | A |
| `/keyboard-shortcuts-mapear` | `ADJUNTOS`(A), `DISPOSITIVO`(C), `HERRAMIENTAS`(A) | A,C |
| `/kill-project` | `ADJUNTOS`(A), `METRICAS`(A), `PROYECTO`(A) | A |
| `/knowledge-base-privada` | `ADJUNTOS`(A), `DOMINIO`(C), `FUENTES`(A), `USUARIOS`(C) | A,C |
| `/kotter-8-steps` | `CASO`(A), `CONTEXTO`(A) | A |
| `/kpi-framework-definir` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `NEGOCIO`(B), `OBJETIVO`(A) | B,A |
| `/kpi-tree` | `CASO`(A), `CONTEXTO`(A) | A |
| `/kpi-tree-artefactos` | `CASO`(A), `CONTEXTO`(A) | A |
| `/lateral-connection` | `ADJUNTOS`(A), `CONCEPTO_A`(C), `CONCEPTO_B`(C) | A,C |
| `/lateral-provocacion` | `ADJUNTOS`(A), `PATRON_ACTUAL`(C), `PROBLEMA`(A) | A,C |
| `/lead-scoring-modelo` | `ADJUNTOS`(A), `CRM`(B), `ICP`(C), `PRODUCTO`(A) | B,A,C |
| `/lean-canvas` | `CASO`(A), `CONTEXTO`(A) | A |
| `/learning-environment` | `ADJUNTOS`(A), `HERRAMIENTAS`(A), `INTERESES`(C) | A,C |
| `/learning-from-failure` | `ADJUNTOS`(A), `EVENTO`(C) | A,C |
| `/legal-compliance-gap` | `MARCO_REGULATORIO`(B), `SECTOR`(A) | A,B |
| `/legal-contract-review` | `CLAUSULAS_CLAVE`(B), `JURISDICCION`(B), `PARTE_A`(B), `PARTE_B`(B) | B |
| `/legal-privacy-dpia` | `MARCO_PROTECCION_DATOS`(B), `PRODUCTO_O_PROCESO`(B) | B |
| `/limpiar-transformar-datos` | `ADJUNTOS`(A), `DATOS`(A), `FORMATO_DESTINO`(C) | A,C |
| `/linkedin-thought-leadership` | `ADJUNTOS`(A), `EXPERIENCIA`(B), `TEMA`(A) | B,A |
| `/literature-review` | `ADJUNTOS`(A), `ALCANCE`(A), `TEMA`(A) | A |
| `/literature-review-matrix` | `CASO`(A), `CONTEXTO`(A) | A |
| `/literature-review-practica` | `CASO`(A), `CONTEXTO`(A) | A |
| `/manual-procedimientos` | `ADJUNTOS`(A), `AUDIENCIA`(A), `PROCEDIMIENTO`(B) | B,A |
| `/mapa-mental-concepto` | `ADJUNTOS`(A), `CONCEPTO`(A), `PROPOSITO`(C) | A,C |
| `/mapa-stakeholders` | `ADJUNTOS`(A), `CONTEXTO`(A), `INICIATIVA`(B) | B,A |
| `/market-sizing-tam-sam-som` | `ADJUNTOS`(A), `GEOGRAFIA`(A), `OPORTUNIDAD`(B) | B,A |
| `/mashup-ideas` | `ADJUNTOS`(A), `DOMINIO_A`(C), `DOMINIO_B`(C) | A,C |
| `/matriz-de-ansoff` | `CASO`(A), `CONTEXTO`(A) | A |
| `/matriz-ponderada` | `ADJUNTOS`(A), `CRITERIOS`(A), `OPCIONES`(B) | B,A |
| `/mece` | `CASO`(A), `CONTEXTO`(A) | A |
| `/mece-tree` | `CASO`(A), `CONTEXTO`(A) | A |
| `/media-monitoring-alertas` | `ADJUNTOS`(A), `COMPETIDORES`(B), `TEMA`(A) | B,A |
| `/meeting-note-to-action` | `ADJUNTOS`(A), `NOTAS`(B), `PARTICIPANTES`(C) | B,A,C |
| `/meeting-prep-auto` | `ADJUNTOS`(A), `CALENDARIO`(B), `REUNIONES_SEMANA`(C) | B,A,C |
| `/meeting-summarizer` | `ADJUNTOS`(A), `FRECUENCIA`(C), `HERRAMIENTA`(A) | A,C |
| `/mensaje-dificil-escrito` | `ADJUNTOS`(A), `CANAL`(C), `RECEPTOR`(B), `TEMA`(A) | B,A,C |
| `/mentorar-junior` | `ADJUNTOS`(A), `MENTEE`(B), `OBJETIVO`(A) | B,A |
| `/metaphor-generator` | `ADJUNTOS`(A), `CONCEPTO`(A) | A |
| `/metodo-socratico` | `CASO`(A), `CONTEXTO`(A) | A |
| `/micro-contenido-redes` | `ADJUNTOS`(A), `PERFIL`(C), `PLATAFORMA`(B), `TEMA`(A) | B,A,C |
| `/micro-recovery-workday` | `ADJUNTOS`(A), `ENTORNO`(C), `HORARIO`(C) | A,C |
| `/migrar-gpt-a-gem` | `ADJUNTOS`(A), `AGENTE_ORIGINAL`(C), `PLATAFORMA_DESTINO`(C) | A,C |
| `/migrar-herramienta` | `ADJUNTOS`(A), `DATOS`(A), `HERRAMIENTA_NUEVA`(C), `HERRAMIENTA_VIEJA`(C) | A,C |
| `/mindfulness-2min` | `ADJUNTOS`(A), `CONTEXTO`(A) | A |
| `/minimum-viable-decision` | `ADJUNTOS`(A), `DECISION`(A) | A |
| `/minto-pyramid-memo` | `CASO`(A), `CONTEXTO`(A) | A |
| `/moat-personal-carrera` | `ADJUNTOS`(A), `ASPIRACION`(C), `ROL`(A) | A,C |
| `/modelos-mentales-latticework` | `ADJUNTOS`(A), `DOMINIO`(B), `SITUACION`(A) | B,A |
| `/monitorear-rendimiento` | `ADJUNTOS`(A), `AGENTE`(A), `METRICAS`(A) | A |
| `/monte-carlo-scenario-sheet` | `CASO`(A), `CONTEXTO`(A) | A |
| `/monte-carlo-scenarioing` | `CASO`(A), `CONTEXTO`(A) | A |
| `/moodboard-direccion-arte` | `ADJUNTOS`(A), `CONTEXTO`(A), `PROYECTO`(A) | A |
| `/morning-planning-5min` | `ADJUNTOS`(A), `HERRAMIENTAS`(A), `HORA`(C) | A,C |
| `/moscow` | `CASO`(A), `CONTEXTO`(A) | A |
| `/motion-graphics-spec` | `ADJUNTOS`(A), `DURACION`(A), `ESTILO`(A), `MENSAJE`(A) | A |
| `/multimodal-audit` | `ILEGIBLE`(C), `TIPO_DE_ARTEFACTO`(B) | B,C |
| `/mvp-disenar` | `ADJUNTOS`(A), `HIPOTESIS`(A), `IDEA`(C) | A,C |
| `/n-2` | `CONTEXTO`(A), `FORMATO`(A), `MATERIAL_BASE`(A), `OBJETIVO`(A), `RESTRICCIONES`(A) | A |
| `/negotiation-prep-sheet` | `CASO`(A), `CONTEXTO`(A) | A |
| `/newsletter-engagement` | `ADJUNTOS`(A), `AUDIENCIA`(A), `NEWSLETTER`(B), `TEMA`(A) | B,A |
| `/north-star-metric` | `ADJUNTOS`(A), `PRODUCTO`(A), `VALOR`(B) | B,A |
| `/north-star-metric-metodos` | `CASO`(A), `CONTEXTO`(A) | A |
| `/note-taking-system` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `VOLUMEN`(A) | A |
| `/notebooklm-cuaderno` | `ADJUNTOS`(A), `FUENTES`(A), `OUTPUTS`(A), `TEMA`(A) | A |
| `/notificaciones-inteligentes` | `ADJUNTOS`(A), `APPS`(C), `DISPOSITIVOS`(C) | A,C |
| `/notion-database-workflow` | `ADJUNTOS`(A), `EQUIPO`(A), `PROCESOS`(C) | A,C |
| `/objecion-handling` | `ADJUNTOS`(A), `OBJECIONES`(B), `PRODUCTO`(A) | B,A |
| `/objection-handling-matrix` | `CASO`(A), `CONTEXTO`(A) | A |
| `/objection-handling-matrix-artefactos` | `CASO`(A), `CONTEXTO`(A) | A |
| `/occam-razor-solucion-simple` | `ADJUNTOS`(A), `OPCIONES`(B), `PROBLEMA`(A) | B,A |
| `/okr-design` | `CASO`(A), `CONTEXTO`(A) | A |
| `/okr-personal-trimestral` | `ADJUNTOS`(A), `TRIMESTRE`(B), `VISION`(B) | B,A |
| `/onboarding-30-60-90` | `ADJUNTOS`(A), `EQUIPO`(A), `ROL`(A) | A |
| `/onboarding-empleado` | `ADJUNTOS`(A), `EMPRESA`(A), `HERRAMIENTAS`(A), `ROL`(A) | A |
| `/onboarding-equipo-ia` | `ADJUNTOS`(A), `AGENTE`(A), `EQUIPO`(A) | A |
| `/onboarding-personalizado` | `ADJUNTOS`(A), `PRODUCTO`(A), `USUARIOS`(C) | A,C |
| `/one-on-one-agenda` | `CASO`(A), `CONTEXTO`(A) | A |
| `/one-on-one-efectivo` | `ADJUNTOS`(A), `EQUIPO`(A), `FRECUENCIA`(B) | B,A |
| `/one-on-one-framework` | `CASO`(A), `CONTEXTO`(A) | A |
| `/ooda-loop` | `CASO`(A), `CONTEXTO`(A) | A |
| `/ooda-loop-decision-rapida` | `ADJUNTOS`(A), `PRESION`(B), `SITUACION`(A) | B,A |
| `/opportunity-cost-calcular` | `ADJUNTOS`(A), `OPCIONES`(C), `RECURSOS`(B) | B,A,C |
| `/opportunity-solution-tree` | `CASO`(A), `CONTEXTO`(A) | A |
| `/optimizar-entorno-digital` | `ADJUNTOS`(A), `DISPOSITIVO`(C), `FRUSTRACIONES`(C), `HERRAMIENTAS`(A) | A,C |
| `/optimizar-spec-existente` | `ADJUNTOS`(A), `PROBLEMA`(A), `SPEC_ACTUAL`(C) | A,C |
| `/orchestrator-pwc` | `N`(C), `TAREA`(A) | A,C |
| `/paleta-colores-profesional` | `ADJUNTOS`(A), `MARCA`(A), `PERSONALIDAD`(B), `SECTOR`(A) | B,A |
| `/pareto-80-20` | `CASO`(A), `CONTEXTO`(A) | A |
| `/partnership-propuesta` | `ADJUNTOS`(A), `OBJETIVO`(A), `PARTNER`(C) | A,C |
| `/pas` | `CASO`(A), `CONTEXTO`(A) | A |
| `/password-security` | `ACTUAL`(C), `ADJUNTOS`(A), `VOLUMEN`(A) | A,C |
| `/patent-landscape` | `ADJUNTOS`(A), `EMPRESA`(A), `TECNOLOGIA`(B) | B,A |
| `/pdca` | `CASO`(A), `CONTEXTO`(A) | A |
| `/pdca-sheet` | `CASO`(A), `CONTEXTO`(A) | A |
| `/pensamiento-de-segundo-orden` | `CASO`(A), `CONTEXTO`(A) | A |
| `/pensamiento-probabilistico` | `CASO`(A), `CONTEXTO`(A) | A |
| `/persona-matrix` | `CASO`(A), `CONTEXTO`(A) | A |
| `/persona-synthesis` | `CASO`(A), `CONTEXTO`(A) | A |
| `/personal-roadmap` | `ADJUNTOS`(A), `ESTADO_ACTUAL`(C), `VISION`(B) | B,A,C |
| `/pestel` | `CASO`(A), `CONTEXTO`(A) | A |
| `/pestel-entorno-macro` | `ADJUNTOS`(A), `ORGANIZACION`(B), `PAIS`(C) | B,A,C |
| `/piramide-de-minto` | `CASO`(A), `CONTEXTO`(A) | A |
| `/piramide-minto-estructura` | `ADJUNTOS`(A), `AUDIENCIA`(A), `FORMATO`(A), `TEMA`(A) | A |
| `/pitch-cliente` | `ADJUNTOS`(A), `CLIENTE`(A), `PRODUCTO`(A) | A |
| `/pitch-interno-idea` | `ADJUNTOS`(A), `ASK`(B), `AUDIENCIA`(A), `IDEA`(B) | B,A |
| `/pivot-evaluar` | `ADJUNTOS`(A), `MODELO_ACTUAL`(C), `SIGNALS`(C) | A,C |
| `/pivot-table-analisis` | `ADJUNTOS`(A), `DATOS`(A), `PREGUNTA`(B) | B,A |
| `/plan-90-dias-competencia` | `ADJUNTOS`(A), `COMPETENCIA`(B), `HORAS_SEMANALES`(C), `NIVEL_ACTUAL`(C) | B,A,C |
| `/pomodoro-avanzado-personalizado` | `ADJUNTOS`(A), `ATENCION_ACTUAL`(C), `TIPO_TRABAJO`(C) | A,C |
| `/portafolio-evidencia` | `ADJUNTOS`(A), `OBJETIVO`(A), `ROL`(A) | A |
| `/portfolio-learning` | `ADJUNTOS`(A), `AUDIENCIA`(A), `COMPETENCIAS`(B) | B,A |
| `/postmortem-review` | `CASO`(A), `CONTEXTO`(A) | A |
| `/postmortem-sin-culpa` | `CASO`(A), `CONTEXTO`(A) | A |
| `/pre-mortem-proyecto` | `ADJUNTOS`(A), `PLAZO`(A), `PROYECTO`(A) | A |
| `/precio-servicio` | `ADJUNTOS`(A), `PRESUPUESTO`(A), `PROVEEDOR`(C), `SERVICIO`(B) | B,A,C |
| `/premortem` | `CASO`(A), `CONTEXTO`(A) | A |
| `/premortem-canvas` | `CASO`(A), `CONTEXTO`(A) | A |
| `/preparar-conversacion` | `ADJUNTOS`(A), `CONTEXTO`(A), `CONTRAPARTE`(B), `OBJETIVO`(A) | B,A |
| `/presentacion-ejecutiva-script` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DURACION`(A), `TEMA`(A) | A |
| `/presentacion-minimalista` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DURACION`(A), `TEMA`(A) | A |
| `/presentacion-slide-deck` | `ADJUNTOS`(A), `AUDIENCIA`(A), `DURACION`(A), `SLIDES`(C), `TEMA`(A) | A,C |
| `/presentar-personas` | `ADJUNTOS`(A), `PERSONA_A`(C), `PERSONA_B`(C), `RAZON`(C) | A,C |
| `/pricing-analysis` | `ADJUNTOS`(A), `COMPETIDORES`(B), `PRICING_ACTUAL`(C), `PRODUCTO`(A) | B,A,C |
| `/primeros-principios` | `ADJUNTOS`(A), `INDUSTRIA`(A), `SUPOSICION`(B) | B,A |
| `/primeros-principios-metodos` | `CASO`(A), `CONTEXTO`(A) | A |
| `/priming-contexto-sesion` | `ADJUNTOS`(A), `PREFERENCIAS`(B), `ROL`(A), `SECTOR`(A) | B,A |
| `/priming-universal-crear` | `ADJUNTOS`(A), `ESTILO`(A), `ROL`(A) | A |
| `/probabilistic-decision-table` | `CASO`(A), `CONTEXTO`(A) | A |
| `/problem-framing-brief` | `CASO`(A), `CONTEXTO`(A) | A |
| `/procrastinacion-protocolo` | `ADJUNTOS`(A), `TAREA`(A), `TIEMPO_BLOQUEADO`(C) | A,C |
| `/project-kickoff` | `ADJUNTOS`(A), `EQUIPO`(A), `PROYECTO`(A) | A |
| `/prompt-audit-personal` | `ADJUNTOS`(A), `PROMPTS`(B) | B,A |
| `/prompt-chain-disenar` | `ADJUNTOS`(A), `HERRAMIENTA`(A), `OUTPUT`(A) | A |
| `/prompt-chain-map` | `CASO`(A), `CONTEXTO`(A) | A |
| `/prompt-chaining` | `CASO`(A), `CONTEXTO`(A) | A |
| `/prompt-injection-defense` | `CASO`(A), `CONTEXTO`(A) | A |
| `/prompt-library-personal` | `ADJUNTOS`(A), `HERRAMIENTAS`(A), `TEMAS`(C) | A,C |
| `/prompt-portfolio-review` | `ADJUNTOS`(A), `PORTFOLIO`(B) | B,A |
| `/prompt-testing-framework` | `ADJUNTOS`(A), `PROMPT`(B), `SCOPE`(C) | B,A,C |
