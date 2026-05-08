<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Capa Departamental — Operaciones — Consultora Modelo S.L.

**Ejemplo orientativo**

*Este documento es un ejemplo completamente rellenado de la plantilla de capa departamental, aplicado a la función Operaciones — entrega de proyectos — de la misma organización ficticia que articula su [Constitución Corporativa](./constitucion-corporativa-ejemplo.md) y su [Marco Regulatorio](./marco-regulatorio-ejemplo.md). Sirve como referencia para entender cómo se modela una capa departamental cuando el dominio es donde la organización realmente vive: la entrega real al cliente.*

*Las decisiones articuladas aquí ilustran especialmente la tensión cultural más característica de la función de Operaciones: cómo equilibrar disciplina metodológica con la respuesta a una realidad que cambia durante la ejecución del proyecto.*

*Consultora Modelo S.L. es una organización ficticia.*

</td>
</tr>
</table>

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Departamento al que aplica esta capa | Operaciones — Entrega de Proyectos |
| Versión del documento | 1.0 |
| Fecha de aprobación | 2026-04-15 |
| Próxima revisión programada | 2026-10-15 |
| Custodio principal | Pilar Méndez, Directora de Operaciones |
| Co-firmante | Director General (validación de coherencia con Constitución, dado que Operaciones es el departamento más numeroso y central de la organización) |
| Aprobación formal | Comité de Dirección, acta nº 2026-04 |
| Versión de la Constitución Corporativa de la que hereda | 1.0, aprobada 2026-04-15 |
| Versión del Marco Regulatorio del que hereda | 1.0, aprobado 2026-04-15 |

---

## 1. Identidad del departamento

### 1.1 Misión del departamento

Entregamos los proyectos que el departamento Comercial ha cerrado, en plazo y forma comprometidos, manteniendo la calidad que la organización promete y la rentabilidad por consultor por encima del umbral acordado. Nuestra eficacia se mide por la combinación de tres criterios: proyectos entregados que terminan en relación duradera con el cliente, satisfacción interna del equipo de proyecto, y disciplina metodológica sostenida — no por velocidad de cierre formal de proyectos ni por facturación bruta.

### 1.2 Quién compone el departamento

Operaciones es el departamento más numeroso de la organización, dimensionado para que cada proyecto tenga la dedicación que necesita:

- **Pilar Méndez** — Directora de Operaciones. Responsable del departamento.
- **Cinco Practice Leads** — responsables de las cinco prácticas de la consultora (Estrategia Tecnológica, Transformación Digital, Gobernanza de Datos, Adopción de IA, Modernización de Aplicaciones). Cada Practice Lead supervisa los proyectos de su práctica y desarrolla las metodologías propias.
- **Treinta consultores senior** — responsables de proyectos individuales como Project Leads. Cada uno gestiona típicamente entre uno y tres proyectos concurrentes.
- **Veinticinco consultores en niveles intermedios** — ejecutan dentro de los equipos de proyecto, con responsabilidades de subentrega.
- **Doce consultores junior** — apoyan en proyectos, integrados en equipos liderados por consultores senior, con planes de desarrollo formal.

Total del departamento: 73 personas de los 80 totales de la organización. Distribución geográfica alineada con las jurisdicciones operativas: predominio Madrid (50 personas), oficina Lisboa (10), distribución móvil para Francia e Italia (13).

### 1.3 Con qué otros departamentos colabora más estrechamente

- **Comercial** (custodio: Andrés Fonseca): colaboración estructural y constante. Cada propuesta requiere validación de Operaciones antes de envío al cliente, con reuniones semanales conjuntas. La frontera Comercial-Operaciones es probablemente la más crítica de la organización — el desajuste aquí genera proyectos que se cierran y luego no se pueden entregar bien.
- **Capital Humano y Talento** (custodio: Cristina Vega): asignación de consultores a proyectos, planificación de capacidad por jurisdicción y por especialidad, gestión de necesidades de formación específica, identificación de necesidades de incorporación.
- **Legal y Compliance** (custodio: Manuel Riera): consultas durante ejecución de proyecto sobre tratamiento de datos del cliente, cumplimiento de cláusulas DPA, gestión de incidentes con implicaciones regulatorias.
- **Dirección General**: validación de decisiones que afectan a posicionamiento de la organización en proyectos críticos, gestión de conflictos de cliente significativos, decisiones sobre modelos metodológicos que afectan a más de una práctica.

### 1.4 Qué nos hace específicos como departamento

Tres particularidades operativas:

**Primero**, la realidad de proyecto cambia constantemente. Lo que se planifica al inicio de un proyecto rara vez coincide al detalle con lo que se ejecuta — emergen variables, cambian prioridades del cliente, aparecen restricciones no anticipadas. La disciplina metodológica de la organización está en mantener la rigurosidad de planificación y revisión sin volverse inflexibles ante la realidad que cambia. Esta tensión es el ángulo cultural protagonista de esta capa.

**Segundo**, el departamento opera en cinco prácticas con metodologías parcialmente compartidas y parcialmente específicas. Lo común — gestión de proyecto, gobernanza, comunicación al cliente, calidad — es transversal y se modela aquí. Lo específico — metodologías técnicas de cada práctica — vive en cada Practice Lead y excede esta capa departamental.

**Tercero**, los proyectos de Consultora Modelo cierran en plazos significativamente más cortos que la media del sector. Esto es promesa cultural articulada en la Constitución y argumento comercial diferenciador. El departamento tiene la responsabilidad operativa de sostener esa promesa sin que se traduzca en infrahumanización del equipo. Cómo se equilibra velocidad con humanidad del trabajo es decisión de modelado constante.

### 1.5 Custodio operativo de la sub-capa

Pilar Méndez, Directora de Operaciones.

---

## 2. Voz del departamento

### 2.1 Particularidades de tono dentro del departamento

La voz general de Consultora Modelo se aplica plenamente. El departamento Operaciones añade dos matices:

**Más operativo en lo procedimental.** Las comunicaciones de gestión de proyecto (estados, planes, decisiones operativas) son sucintas, claras, orientadas a acción. La calidez se reserva para comunicaciones sobre personas, no sobre tareas. Un correo de actualización de plan de proyecto puede prescindir de fórmulas de cortesía elaboradas; un correo sobre el desarrollo profesional de un consultor del equipo, no.

**Más matizado al comunicar al cliente.** Cuando emerge una desviación, una mala noticia, o un cambio significativo en el plan, la comunicación al cliente requiere matiz especial. No es lo mismo *"se ha producido un retraso de dos semanas"* (informativo neutro) que *"hemos identificado un riesgo de retraso de dos semanas que estamos gestionando con las siguientes acciones"* (transparente, con contexto, orientado a solución). El segundo es la voz del departamento.

### 2.2 Vocabulario técnico específico del dominio

**Vocabulario propio del departamento:**

- *"Proyecto"* en lugar de *"engagement"*, *"work"* o *"matter"*.
- *"Equipo de proyecto"* en lugar de *"team"* genérico.
- *"Hito"* en lugar de *"milestone"* en comunicaciones en español.
- *"Comité de seguimiento"* en lugar de *"steering committee"* (anglicismo aceptado solo cuando el cliente lo usa).
- *"Punto de control"* o *"check-point"* (anglicismo aceptado por uso) para revisiones intermedias.
- *"Desviación"* en lugar de *"variance"* o *"deviation"*.
- *"Plan de proyecto"* y *"replanificación"* — la replanificación es práctica habitual y articulada, no excepción.
- *"Cierre de proyecto"* como hito formal con sus propios entregables.
- *"Lecciones aprendidas"* — proceso formal al final de cada proyecto, no opcional.

**Acrónimos y abreviaciones recurrentes:**

- *PL* — Project Lead (en notas internas; en comunicación externa decimos *responsable de proyecto*).
- *PMO* — Project Management Office (anglicismo aceptado por uso universal sectorial).
- *RAG* — Red/Amber/Green (estado de proyecto en informes; anglicismo aceptado).
- *KPI* — anglicismo aceptado, sin equivalente español usable.
- *EVM* — Earned Value Management cuando se aplica formalmente.
- *RACI* — matriz de responsabilidades.

### 2.3 Cómo nos referimos a los interlocutores externos del departamento

- **Sponsor del cliente** (típicamente un director o un C-level del cliente que firma el proyecto): tratamiento de usted en comunicaciones formales, tuteo cuando la relación lo permite y la otra parte lo facilita.
- **Equipo del cliente** (consultores del cliente que trabajan codo a codo con nuestro equipo de proyecto): tuteo desde el inicio de la colaboración. La cercanía operativa cotidiana hace que el tratamiento de usted sea distancia artificial.
- **Comité de dirección del cliente** (en presentaciones formales): tratamiento de usted, formalidad alta, comunicación cuidada.
- **Auditores externos del cliente** (cuando intervienen en nuestros proyectos): tratamiento de usted siempre, formalidad sostenida.
- **Subcontratistas en nuestros proyectos**: relación profesional clara entre pares, cordial sin familiaridad.

### 2.4 Custodio operativo de la sub-capa

Pilar Méndez, en colaboración con Practice Leads para vocabulario específico de cada práctica.

---

## 3. Tipos de tarea del departamento

### 3.1 Tabla de tipos de tarea

| Tipo de tarea | Qué aporta el asistente | Qué decide siempre el humano | Revisión humana antes de externalizar |
|---|---|---|---|
| Generación de planes de proyecto detallados | Primera versión basada en metodología de la práctica y briefing de la propuesta, identificación de dependencias, generación de cronograma | Decisiones sobre asignación de recursos específicos, hitos contractuales, márgenes de plan | Revisión obligatoria por Project Lead + Practice Lead correspondiente |
| Reportes semanales de avance de proyecto | Compilación automática de avance contra plan, identificación de desviaciones, generación de borradores de informe | Interpretación de desviaciones, decisiones sobre acciones correctivas, narrativa para el cliente | Revisión obligatoria por Project Lead antes de envío al cliente |
| Análisis de desviaciones de proyecto | Identificación cuantitativa de desviaciones (plazo, alcance, recursos), análisis de impacto en hitos contractuales | Decisión sobre acciones correctivas, comunicación al cliente, replanificación | Revisión por Project Lead + Practice Lead |
| Preparación de comités de seguimiento con cliente | Compilación de información para presentación, generación de borradores de slides, preparación de respuestas a preguntas anticipadas | Mensaje principal a transmitir, posicionamiento ante decisiones del cliente, contenido sustantivo | Revisión obligatoria por Project Lead |
| Análisis agregado de portfolio de proyectos | Identificación de patrones cruzados (uso de recursos, tipos de desviación, áreas de mejora metodológica), generación de informes de tendencias | Interpretación, decisiones sobre cambios metodológicos | Revisión por Pilar + Practice Leads |
| Gestión de planificación de capacidad de plantilla | Análisis de disponibilidad de consultores por proyecto, alertas sobre conflictos de planificación, sugerencias de optimización | Decisiones sobre asignación específica de personas, gestión de conflictos | Revisión por Pilar + Cristina (Capital Humano) |
| Documentación de proyecto durante ejecución | Generación de borradores de documentación entregable basados en plantillas de la práctica, integración de inputs del equipo | Validación técnica de contenido, decisiones sobre estructura específica del entregable | Revisión obligatoria por Project Lead + Practice Lead |
| Generación de informes ejecutivos para Comité de Dirección interno | Compilación de información de portfolio, identificación de proyectos en estado de riesgo, generación de borradores | Interpretación, decisiones sobre escalado, mensaje principal | Revisión por Pilar antes de presentación |
| Preparación de procesos de cierre de proyecto | Compilación de entregables finales, generación de checklist de cierre, borradores de informe de lecciones aprendidas | Validación de completitud, gestión de expectativas finales con cliente | Revisión obligatoria por Project Lead + Practice Lead |
| Soporte a procesos de calidad de entregables | Verificación contra checklist de calidad de la práctica, identificación de gaps, sugerencias de mejora | Validación técnica de calidad, decisiones sobre aceptación o reescritura | Revisión por Project Lead + Practice Lead |

### 3.2 Tareas que el departamento NO delega a asistentes de IA

Cinco categorías deliberadamente excluidas:

**Decisiones sobre escalado de incidentes en proyecto.** Cuando emerge un incidente significativo en un proyecto activo, la decisión de cómo escalar (a quién, en qué momento, con qué nivel de alarma) la toma siempre el Project Lead con apoyo del Practice Lead correspondiente. Los asistentes pueden compilar información, pero no calibran ni proponen escalado.

**Comunicación al cliente sobre desviaciones significativas.** Cuando una desviación de proyecto requiere comunicación al cliente, la redacción final y el envío son siempre humanos. Los asistentes pueden generar borradores estructurados, pero el matiz de cómo se comunica una mala noticia es exclusivo del Project Lead.

**Decisiones sobre replanificación de proyecto.** Cualquier replanificación que afecta a hitos contractuales o al cronograma original requiere decisión humana del Project Lead + Practice Lead. Los asistentes pueden modelar escenarios, pero no eligen.

**Evaluación de calidad de entregables al cliente.** La validación de que un entregable cumple los estándares de calidad de la organización es siempre humana. El asistente puede verificar contra checklist objetivo, pero la decisión de calidad cualitativa es del Project Lead + Practice Lead.

**Cierre formal de proyecto y declaración de lecciones aprendidas.** El proceso de cierre y la articulación de lecciones aprendidas requiere reflexión humana. Los asistentes pueden generar borradores, pero la lección aprendida significativa la articula la persona que la ha vivido.

### 3.3 Custodio operativo de la sub-capa

Pilar Méndez, en coordinación con los cinco Practice Leads para validación de tareas específicas de cada práctica.

---

## 4. Restricciones específicas del departamento

### 4.1 Restricciones de uso adicionales

Más allá de las restricciones generales aplicables a toda la organización, el departamento Operaciones aplica las siguientes:

**Aislamiento entre proyectos.** La información de cada proyecto se mantiene aislada de los demás proyectos. Los asistentes no establecen referencias cruzadas entre proyectos sin autorización explícita, incluso cuando metodológicamente sería útil. Las lecciones aprendidas de un proyecto se incorporan a la metodología de la práctica solo tras anonimización por humano.

**Restricción reforzada sobre datos del cliente recibidos durante proyecto.** Toda información que el equipo de proyecto recibe del cliente durante la ejecución es confidencial estricta. Los asistentes pueden procesarla solo dentro del contexto del proyecto activo y no la cruzan con otros proyectos del mismo cliente ni con otros clientes.

**Trazabilidad de decisiones de proyecto.** Cualquier output generado por asistente que vaya a usarse para tomar una decisión de proyecto debe ser trazable — debe quedar registrado qué prompt generó qué output, qué versión del asistente, qué fuentes consultó. La razón es que las decisiones de proyecto son auditables y la trazabilidad es condición para que la auditabilidad sea real.

**Verificabilidad obligatoria de afirmaciones técnicas.** Cualquier afirmación técnica que aparezca en un entregable al cliente debe ser verificable contra fuente. Los asistentes pueden generar afirmaciones plausibles pero no necesariamente verificadas; el responsable del entregable verifica antes de incorporar.

### 4.2 Datos del dominio que requieren cuidado especial

- **Información estratégica del cliente compartida en confianza durante proyecto.** Confidencialidad absoluta. Solo accesible al equipo del proyecto específico.
- **Datos operativos confidenciales del cliente** (estructura interna, decisiones internas, conflictos internos, datos económicos no públicos): tratamiento restringido al equipo del proyecto.
- **Outputs de proyecto en estado borrador**: no compartibles fuera del equipo de proyecto sin autorización del Project Lead.
- **Información sobre desempeño de subcontratistas en proyectos**: confidencial. Influye en decisiones de subcontratación futura pero no se comparte con el subcontratista ni con clientes.
- **Lecciones aprendidas de proyectos cerrados**: anonimizables tras cierre, pero solo con autorización formal y nunca cuando puedan identificar al cliente o al consultor responsable.

### 4.3 Materias del departamento sometidas a aprobación previa

| Tipo de acción | Aprobador requerido | Mecanismo de aprobación |
|---|---|---|
| Replanificación de proyecto que afecta a hito contractual | Project Lead + Practice Lead + Director Comercial | Email previo a comunicar al cliente |
| Subcontratación de cualquier parte de un proyecto | Project Lead + Pilar + Director General | Justificación escrita del por qué de la subcontratación |
| Aceptación de cambio de alcance significativo (>15% del valor del proyecto) | Project Lead + Director Comercial + Pilar | Validación escrita previa a comunicar al cliente |
| Comunicación de incidente serio al cliente | Project Lead + Practice Lead + Director Comercial + Pilar | Reunión de validación documentada antes de comunicar |
| Asignación de consultor a proyecto fuera del plan de capacidad inicial | Pilar + Cristina | Email de validación |
| Aplicación de metodología no estándar en un proyecto | Project Lead + Practice Lead + Pilar | Aprobación escrita |
| Cierre formal de proyecto sin haber alcanzado todos los hitos comprometidos | Project Lead + Practice Lead + Pilar + Director Comercial | Reunión de cierre documentada |
| Comunicación pública sobre proyecto (caso de éxito, ponencia, blog) | Project Lead + Cliente + Directora de Comunicación | Aprobación escrita explícita del cliente |

### 4.4 Custodio operativo de la sub-capa

Pilar Méndez, con escalado a Director General para validación de restricciones que afectan a posicionamiento estratégico de la organización.

---

## 5. Escalado dentro del departamento

### 5.1 Tabla operativa de escalado del departamento

| Situación específica del dominio | Agente que escala | Agente humano que recibe | Plazo de respuesta esperado |
|---|---|---|---|
| Detección de desviación de proyecto que excede umbral de tolerancia | Asistente de proyecto | Project Lead | Mismo día hábil |
| Detección de patrón de desviación cruzado entre proyectos de la misma práctica | Asistente de proyecto | Practice Lead + Pilar | 48 horas |
| Cliente comunica insatisfacción en comité de seguimiento | Asistente de proyecto | Project Lead + Director Comercial | Inmediato — el asistente no responde, solo registra y escala |
| Detección de posible incidente de seguridad o cumplimiento durante proyecto | Asistente de proyecto | Project Lead + DPO + Practice Lead | Inmediato |
| Necesidad de incorporación urgente de consultor al equipo de proyecto | Asistente de proyecto | Project Lead + Cristina + Pilar | 24 horas |
| Solicitud de cliente fuera de horario o canal habitual | Asistente de proyecto | Project Lead | Mismo día hábil |
| Conflicto detectado entre miembros del equipo de proyecto | Asistente de proyecto | Project Lead + Cristina | 24 horas |
| Petición de cliente que excede alcance contractual | Asistente de proyecto | Project Lead + Director Comercial | 24 horas |
| Detección de subentregable que no cumple checklist de calidad | Asistente de proyecto | Project Lead + Practice Lead | Mismo día hábil |
| Cualquier situación que el asistente perciba como fuera de patrón habitual | Asistente de proyecto | Project Lead | Mismo día hábil |

### 5.2 Escalado fuera del departamento

Situaciones que típicamente escalan fuera del departamento Operaciones:

- **A Comercial**: cualquier asunto que afecta a la relación contractual con cliente (cambios de alcance, conflictos contractuales, oportunidades de extensión que emergen durante el proyecto).
- **A Capital Humano y Talento**: cualquier asunto relacionado con personas del equipo de proyecto (necesidad de incorporación, conflictos interpersonales, situaciones personales que afectan al trabajo, desarrollo profesional emergente durante el proyecto).
- **A Legal y Compliance / DPO**: cualquier consulta sobre cumplimiento durante ejecución de proyecto, gestión de incidentes con implicaciones regulatorias, dudas sobre cláusulas DPA aplicables.
- **A Dirección General**: cualquier asunto con implicación estratégica, gestión de conflictos significativos con cliente, decisiones que afectan al posicionamiento de la organización.

### 5.3 Custodio operativo de la sub-capa

Pilar Méndez.

---

## 6. Métricas e indicadores específicos

### 6.1 Indicadores de que los asistentes están aportando valor en el departamento

Tres indicadores monitorizados trimestralmente:

**Tiempo dedicado a actividades de gestión de proyecto vs. actividades de aporte de valor técnico.** El objetivo no es eliminar la gestión sino reducir el tiempo dedicado a tareas administrativas (compilación de reportes, generación de slides estándar, tracking de horas) para liberar al equipo a actividades de mayor valor (análisis técnico, conversaciones con cliente, mentoring intra-equipo). Si tras adopción de asistentes el ratio mejora sin pérdida de calidad de gestión, los asistentes están funcionando bien.

**Calidad de reportes y comunicaciones al cliente.** Medida cualitativamente mediante feedback periódico de clientes sobre claridad, oportunidad y valor de los reportes recibidos. Si la calidad sube tras adopción, los asistentes están bien calibrados. Si baja, hay que recalibrar.

**Velocidad de cierre de proyectos sin pérdida de calidad ni satisfacción del equipo.** El objetivo cultural es mantener la diferencia con la media del sector (proyectos en 14 semanas vs. 24 del mercado) sin que se traduzca en infrahumanización. Indicador cruzado siempre con satisfacción del equipo de proyecto medida en feedback interno post-cierre.

### 6.2 Indicadores de que los asistentes NO están funcionando bien en el departamento

Señales de alarma que disparan revisión inmediata:

- Reportes a cliente percibidos como genéricos, sin matiz específico del proyecto — síntoma de que los asistentes están templating y no calibrando.
- Filtración inadvertida de información de un proyecto en outputs relacionados con otro — incidente crítico que dispara revisión de seguridad.
- Project Leads reescribiendo desde cero los outputs en lugar de usarlos como base — síntoma de calibración inadecuada o de falta de integración con el conocimiento específico del proyecto.
- Aumento de desviaciones de proyecto no detectadas a tiempo — síntoma de que los asistentes están reportando lo planificado sin analizar la realidad ejecutada.
- Tono complaciente o adulador en comunicaciones al cliente — síntoma de que los asistentes están suavizando comunicaciones que deberían ser firmes.
- Reducción de la disciplina metodológica articulada (no se cumplen plantillas de cierre, no se documentan lecciones aprendidas, no se completan checklist) — síntoma de que la facilidad de generación con IA está erosionando los procesos.

### 6.3 Custodio operativo de la sub-capa

Pilar Méndez, con apoyo de los cinco Practice Leads para indicadores cualitativos específicos de cada práctica.

---

## 7. Coherencia y mantenimiento

### 7.1 Mecanismo de actualización

Pilar recibe notificaciones de necesidad de actualización desde tres fuentes:

- Lecciones aprendidas formales al cierre de cada proyecto, donde Project Leads identifican gaps en la capa departamental que han notado durante la ejecución.
- Practice Leads, conforme las metodologías propias evolucionan en cada práctica.
- Feedback de clientes recurrentes sobre dimensiones operativas del trabajo de la organización.

Pilar evalúa mensualmente las notificaciones, propone actualizaciones cuando aplique, y las eleva a aprobación conjunta con el Director General (co-firmante) antes de incorporar.

### 7.2 Mecanismo de excepciones documentadas

Las excepciones a la aplicación literal de esta capa departamental son habituales en proyectos atípicos — esa es precisamente la naturaleza de la entrega de proyectos, que combina rigor metodológico con respuesta a la realidad. Cuando se solicitan, requieren aprobación del Project Lead + Practice Lead + Pilar, con justificación escrita específica, alcance limitado al proyecto en cuestión, y revisión obligatoria al cierre del proyecto para evaluar si la excepción debe convertirse en práctica metodológica nueva.

Las excepciones quedan registradas en repositorio interno con: motivo, alcance, aprobadores, fecha de revisión obligatoria. Las excepciones recurrentes en la misma dimensión disparan revisión específica de la capa departamental — son señal de que la capa no está reflejando bien la realidad operativa.

### 7.3 Indicadores de drift cultural en el departamento

Señales que indicarían que el departamento Operaciones está drifteando culturalmente respecto a la Constitución:

- Proyectos cerrando con compromisos prometidos pero no cumplidos — síntoma estructural del peor tipo, donde la promesa de "cumplir lo prometido" del Marco Regulatorio y de la Constitución se está erosionando.
- Aumento de horas extras del equipo de proyecto como patrón sostenido — síntoma de que la velocidad se está consiguiendo a costa de la humanidad del trabajo.
- Reportes a cliente que ocultan problemas en lugar de comunicarlos transparentemente — síntoma de que la honestidad analítica se está perdiendo.
- Lecciones aprendidas que dejan de articularse o que se vuelven formularias — síntoma de que la disciplina metodológica está erosionándose.
- Tono adulador o complaciente en comunicaciones a cliente — síntoma del mismo tipo que en otros departamentos: la firmeza propia se está perdiendo.
- Conflictos crecientes entre Operaciones y Comercial sobre lo que se ha vendido vs. lo que se puede entregar — síntoma de que la frontera entre departamentos se está rompiendo.

---

*Capa Departamental Operaciones de Consultora Modelo S.L. — versión 1.0, aprobada el 2026-04-15. Documento ficticio orientativo.*

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Para la plantilla en blanco, consultar [capa-departamental.md](./capa-departamental.md). Para ver otras capas departamentales rellenadas, consultar los ejemplos para [Comercial](./capa-departamental-ejemplo-comercial.md), [Legal y Compliance](./capa-departamental-ejemplo-legal.md), y [Capital Humano y Talento](./capa-departamental-ejemplo-personas.md).*
