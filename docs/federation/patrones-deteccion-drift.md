# Myrmion Federation — Patrones de detección de drift

**Versión 1.0**

*Materializa el §3.4 del manifiesto: convierte la promesa de "una federación que se observa a sí misma" en tres procesos repetibles para detectar el drift federado —la deriva del sistema entero, no la de un agente aislado— a partir de lo que la federación ya registra.*

---

## 1. Qué es el drift federado (y qué no)

El **drift federado** es cualquier patrón sistemático en el comportamiento agregado del sistema de agentes que **no se deriva de la Constitución vigente**. Es la divergencia entre la **conducta efectiva de la federación** —cómo se resuelven realmente las decisiones cuando varios agentes departamentales colaboran— y la **conducta que la Constitución Corporativa prescribe**. Es un fenómeno **de sistema**, no de componente: solo emerge cuando se mira el sistema entero, y por eso ninguno de los participantes puede observarlo por sí solo. Las métricas técnicas habituales (latencia, *error rate*, *throughput*) no lo capturan.

Conviene distinguirlo con precisión de un fenómeno vecino:

- **Drift a nivel agente** (territorio de Adoption). Un agente departamental se aleja de su propio mandato, tono o reglas locales. Se detecta revisando los *outputs* del agente concreto y se corrige dentro de su Capa Departamental, con los mecanismos descritos en Adoption. Es **local y unilateral**: el agente drifta respecto de sí mismo.
- **Drift federado** (este documento). La federación, *como conjunto*, resuelve los casos de forma incompatible con la Constitución, aunque cada agente individual parezca cumplir su mandato local. Es **relacional y emergente**: aparece en las **cadenas de decisión** entre agentes, en la **acumulación de excepciones** que nadie decidió tolerar como política, y en la **incoherencia** entre cómo dos agentes resuelven el mismo dilema.

> El drift a nivel agente es un componente que se sale de su carril. El drift federado es la federación que, sin que nadie lo decida, cambia de criterio.

Detectar drift federado **no es** auditar el contenido de los mensajes, ni medir productividad, ni vigilar a las personas. Es **observar la forma de las decisiones** a lo largo del tiempo y compararla con la Constitución. Trabaja sobre los **metadatos de decisión** que los esquemas del cuerpo ya obligan a emitir —el bloque de contexto cultural y el descriptor de identidad—, nunca sobre el *payload* sensible de los casos.

### 1.1 Por qué tres patrones

Cada patrón mira un **rastro distinto** que la federación deja al operar, y cada rastro revela una **cara distinta** del mismo riesgo:

| Patrón | Rastro que consume | Pregunta que responde |
| --- | --- | --- |
| **A. Análisis de cadenas de decisiones** | Log correlacionado por `correlationId`, sobre la convención `criteriaApplied` | ¿Está cambiando *cómo* se decide a lo largo del corredor entre agentes? |
| **B. Análisis de excepciones** | Registro de excepciones | ¿La excepción se ha vuelto la norma —y eso es una *policy* desfasada o una cultura que drifta? |
| **C. Análisis de coherencia entre agentes** | Banco de escenarios versionado | ¿Resuelven dos agentes el mismo dilema de forma compatible con la Constitución? |

Los tres son **procesos, no productos**. Ninguno prescribe una herramienta. El *dashboard*, las consultas y la retención de los logs los aporta el stack de la organización a través de su plano de observabilidad (ver **CF-05** en [`./criterios-funcionales.md`](./criterios-funcionales.md)). Este documento define **qué entra, cómo se analiza, qué cuenta como señal y quién responde**; la materialización operativa vive en la plantilla y en las recetas sectoriales (§6).

---

## 2. Estructura común de un patrón

Cada uno de los tres patrones se especifica con la **misma rejilla fija**, para que sean comparables, auditables y delegables:

1. **Entradas (qué loggear).** Los campos —siempre metadatos de decisión— que el patrón necesita encontrar en el plano de observabilidad. Si el stack no los emite, el patrón es ciego: por eso esto es un **requisito de CF-05**, no una recomendación.
2. **Método.** El procedimiento de análisis, descrito como proceso reproducible e independiente de cualquier producto.
3. **Señales / Umbrales.** Qué configuración de los datos **constituye drift** (o sospecha de drift) frente a variación normal.
4. **Cadencia.** Cada cuánto se ejecuta el patrón, **modulada por la criticidad del dominio** de los agentes implicados.
5. **Responsable.** Quién ejecuta y quién rinde cuentas. El **cuarto custodio** —la plataforma de federación— es el responsable transversal; la **custodia de la capa** afectada aporta la lectura de su dominio.
6. **Qué dispara revisión.** El evento concreto que escala de "observación" a "revisión formal de la Constitución o de una *policy* derivada".
7. **Qué NO es.** El límite explícito del patrón, para impedir que se convierta en vigilancia o en métrica de rendimiento.

### 2.1 Modulación por criticidad del dominio

La cadencia de los tres patrones se ajusta a la **criticidad del dominio** declarada en el descriptor de identidad del agente (ver [`./esquema-identidad-agente.md`](./esquema-identidad-agente.md)). Se usa una escala de tres niveles, que cada organización ancla a su propio mapa de dominios:

| Criticidad del dominio | Ejemplos de dominio | Modulador de cadencia |
| --- | --- | --- |
| **Alta** | Dominios con impacto regulatorio, contractual o sobre derechos (p. ej. legal, financiero, salud) | Cadencia base **÷ 2** (más frecuente) y revisión obligatoria ante la primera señal fuerte |
| **Media** | Dominios con impacto operativo o comercial relevante | Cadencia base |
| **Baja** | Dominios internos de bajo riesgo | Cadencia base **× 2** (menos frecuente), agregación tolerada |

Cuando una cadena de decisión **cruza** dominios de distinta criticidad, prevalece **la criticidad más alta de la cadena**. Un corredor comercial→legal se gobierna, a efectos de cadencia, con la criticidad del dominio legal.

---

## 3. Patrón A — Análisis de cadenas de decisiones

*Mira la **forma** de las decisiones a lo largo de un corredor entre agentes y detecta cuándo ese patrón empieza a apartarse de la Constitución.*

### 3.1 Entradas (qué loggear)

Por cada salto (`DecisionHop`) de la cadena de decisiones que la federación documenta en su bloque de contexto cultural (ver [`./esquema-bloque-contexto-cultural.md`](./esquema-bloque-contexto-cultural.md)):

- **`correlationId`** — identificador que persiste a lo largo de toda la cadena, desde el primer salto hasta el último, y que nunca se regenera. Es la **columna vertebral** del patrón: es la clave con la que se reconstruye la cadena completa a posteriori.
- **`criteriaApplied`** — la lista de criterios que el agente declaró haber aplicado en ese salto, expresada como `policyId@version` cuando el criterio es una *policy* automatizada o como el literal `"juicio-de-modelo-no-automatizable"` cuando es un juicio fino. Es la **unidad de análisis**: el patrón estudia secuencias de `criteriaApplied`, no contenido.
- **`agentId`** emisor y receptor de cada salto (`urn:myrmion:agent:<org>:<dominio>:<nombre>`), y **`hopCount`** del salto.
- **`businessCaseId`** para agrupar todas las cadenas que sirven a un mismo asunto, y **resultado normalizado** del salto, tomado del vocabulario del bloque, no texto libre.
- **`constitutionHash`** aplicado en el salto, para poder atribuir un cambio de patrón a un cambio de Constitución frente a una deriva genuina.

> Todo son metadatos de decisión. El asunto del lead, el texto de la propuesta o los datos del cliente **no entran**: si fuera necesario referenciarlos, se hace mediante `deidToken`, nunca con el dato en claro.

### 3.2 Método

1. **Reconstruir cadenas.** Agrupar todos los `DecisionHop` por `correlationId` y ordenarlos por `hopCount`. Cada grupo es una **cadena de decisiones** completa.
2. **Construir la firma de la cadena.** Para cada cadena, derivar su *firma*: la secuencia ordenada de `(dominio, criteriaApplied, resultado)` por salto. La firma describe la **forma** de la decisión, no su contenido.
3. **Establecer la línea base.** Para cada tipo de corredor (mismo par de dominios, p. ej. comercial→legal), construir la distribución de firmas observada en una ventana de referencia estable, segmentada por `constitutionHashApplied`.
4. **Comparar contra la base.** En cada ejecución, comparar la distribución de firmas reciente con la línea base, sin mezclar `constitutionHashApplied` distintos, para no confundir *deriva* con *cambio decidido*.
5. **Atribuir.** Donde haya divergencia, separar tres causas posibles: (a) cambio decidido de la Constitución, (b) excepción acumulada (deriva al Patrón B), (c) **drift genuino** —cambio de forma sin cambio de Constitución ni excepción registrada que lo explique.

### 3.3 Señales / Umbrales

Cuenta como **señal de drift** (no como prueba; es disparador de revisión):

- Aparición de **firmas nuevas y persistentes** en un corredor —combinaciones de `criteriaApplied` que antes no se daban— sin cambio de `constitutionHashApplied` que las explique.
- **Desaparición sostenida** de un criterio que la Constitución exige para ese corredor: un `policyId@version` obligatorio que deja de aparecer en `criteriaApplied`.
- **Acortamiento sistemático** de la cadena (saltos que antes existían y desaparecen) sin *policy* que lo respalde —indicio de que un control se está saltando de hecho.
- **Desplazamiento de la distribución de resultados** del corredor (p. ej. "con condiciones" migra a "aceptado" sin paso intermedio) mantenido más allá de la variación estacional esperada.

Cada organización fija el tamaño de "persistente / sostenido" en su receta sectorial; lo normativo aquí es **qué configuración cualifica**, no el número exacto.

### 3.4 Cadencia

Cadencia base **mensual** sobre la ventana móvil de cadenas cerradas, modulada por la criticidad del dominio (§2.1): **quincenal** para corredores que tocan dominios de criticidad alta, **bimestral** para los de criticidad baja. Toda señal fuerte adelanta la siguiente ejecución.

### 3.5 Responsable

Ejecuta el **cuarto custodio (plataforma de federación)**, que es el único actor con vista de extremo a extremo de las cadenas y dueño de la *pipeline* de observabilidad. La **custodia de cada capa** implicada en el corredor interpreta las señales de su dominio (¿es esta firma nueva un riesgo o una mejora?) y co-firma la atribución.

### 3.6 Qué dispara revisión

- Una firma nueva persistente **en un corredor de criticidad alta** dispara revisión formal **inmediata**.
- La desaparición de un criterio obligatorio dispara revisión **siempre**, con independencia de la criticidad.
- El resto de señales se acumulan y disparan revisión al cruzar el umbral fijado en la receta sectorial.

La revisión decide entre: **ratificar** la nueva forma actualizando la Constitución y sus *policy templates*, **corregir** el comportamiento, o **registrar una excepción** explícita (lo que conecta con el Patrón B).

### 3.7 Qué NO es

- **No es** lectura de contenido: opera sobre firmas de `criteriaApplied`, jamás sobre el texto del caso.
- **No es** medición de rendimiento de agentes ni de personas: no produce *rankings* ni tiempos.
- **No es** un control en tiempo real ni un *gate* de ejecución; es análisis a posteriori sobre el log, no la *Validación de compatibilidad* que ocurre en cada llamada.

---

## 4. Patrón B — Análisis de excepciones

*La excepción es legítima. La excepción **silenciosa y repetida** es la forma en que una federación cambia de criterio sin decidirlo.*

### 4.1 Entradas (qué loggear)

Consume el **registro de excepciones** de la federación —el rastro de toda llamada que el *policy engine* bloqueó y que la organización aprobó manualmente. Cada excepción deja rastro en el [registro de excepciones](../../templates/federation/registro-excepciones.md) con justificación, alcance temporal y autorizador. Por cada entrada, el patrón consume:

- **`correlationId`** del caso en que se concedió la excepción (enlaza con el Patrón A).
- **`policyId@version`** de la *policy* bloqueada (referenciada por su identificador, no por descripción libre).
- **`agentId`** y **dominio** origen y destino de la llamada bloqueada, y **autorizador** de la excepción.
- **Motivo normalizado** de la excepción, tomado de un vocabulario cerrado (no texto libre), su **alcance temporal** y la marca temporal.
- **`constitutionHash`** vigente al concederse.

> El registro de excepciones guarda **que** hubo excepción y **contra qué *policy***, no el dato sensible que la motivó. Las referencias a datos del caso se hacen vía `deidToken`. Recuérdese que una "excepción" al Marco Regulatorio **no es una excepción, es una alerta**: el Marco no admite excepciones, y ese rastro escala fuera de este patrón.

### 4.2 Método

1. **Agrupar por *policy* eludida.** Acumular las excepciones por la *policy* contra la que se concedieron (`policyId@version`), no por caso.
2. **Medir la tasa de excepción** de cada *policy*: proporción de llamadas aplicables que terminaron en excepción aprobada, sobre una ventana móvil.
3. **Aplicar la decisión binaria.** Para cada *policy* cuya tasa de excepción supera su umbral, clasificar la causa en una de **dos categorías mutuamente excluyentes**:
   - ***Policy* desfasada** — la *policy* ya no encaja con la realidad del negocio; las excepciones son razonables y consistentes entre sí. La *policy* está equivocada respecto de una cultura que no ha cambiado; la realidad no está mal.
   - **Cultura drifteada** — la *policy* sigue traduciendo correctamente la Constitución, pero la federación la elude de forma sistemática e inconsistente; las excepciones no comparten un motivo legítimo común. La cultura real ha drifteado respecto a la Constitución declarada.
4. **Sustentar la clasificación** con evidencia del registro: homogeneidad de motivos normalizados, distribución de autorizadores y correlación con cambios de `constitutionHash`.

La distinción es deliberadamente **binaria** porque dispara acciones opuestas: la *policy* desfasada se **enmienda** (se cambia la *policy*, y quizá la Constitución); la cultura drifteada se **corrige** (se refuerza la *policy* y se interviene la conducta). Cuál de las dos es, es responsabilidad de la custodia decidir. Confundirlas es el error caro: enmendar una *policy* que era correcta institucionaliza el drift.

### 4.3 Señales / Umbrales

- **Tasa de excepción** de una *policy* por encima de su umbral en la ventana móvil.
- **Tendencia creciente** de excepciones contra una misma *policy*, aunque no haya cruzado todavía el umbral absoluto.
- **Concentración** de excepciones en un mismo `agentId`/dominio (sospecha de drift a nivel agente, que se deriva a Adoption) **frente a** dispersión a través de toda la federación (sospecha de drift federado, que se queda aquí).
- **Excepciones recurrentes con el mismo motivo normalizado**: candidato fuerte a "*policy* desfasada".

### 4.4 Cadencia

Cadencia base **mensual** sobre la acumulación. Para *policies* que protegen **dominios de criticidad alta**, revisión **quincenal** y alerta por umbral en cuanto se cruza, sin esperar a la ventana. Para dominios de criticidad baja, **bimestral**.

### 4.5 Responsable

Ejecuta el **cuarto custodio (plataforma de federación)**, que mantiene la vista agregada del registro de excepciones y los *policy templates* transversales. La **custodia de la capa** dueña de la *policy* eludida emite la **clasificación binaria** (*policy* desfasada vs cultura drifteada), porque es quien conoce si la *policy* "sigue traduciendo bien la Constitución"; el cuarto custodio valida la coherencia transversal de esa clasificación.

### 4.6 Qué dispara revisión

- Cualquier *policy* clasificada como ***policy* desfasada** dispara una **propuesta de enmienda** a la *policy* derivada y, si procede, a la Constitución.
- Cualquier *policy* clasificada como **cultura drifteada** dispara una **revisión de gobernanza** y, si procede, un escenario nuevo para el banco del Patrón C.
- Una excepción concedida contra una *policy* de **criticidad alta** dispara revisión **a la primera ocurrencia**, sin esperar a acumulación.

### 4.7 Qué NO es

- **No es** un veto a las excepciones: la excepción puntual y justificada es legítima y debe seguir siendo barata de conceder.
- **No es** un mecanismo disciplinario contra quien autoriza excepciones; la concentración en un agente se **deriva a Adoption** como drift a nivel agente, no se sanciona aquí.
- **No es** análisis de contenido: trabaja sobre `policyId@version` eludida y motivo normalizado, no sobre el caso.

---

## 5. Patrón C — Análisis de coherencia entre agentes

*Dos agentes que cumplen su mandato local pueden, sin embargo, resolver el mismo dilema de formas incompatibles. La coherencia entre agentes es propiedad de la federación, y hay que probarla.*

### 5.1 Entradas (qué loggear)

- El **banco de escenarios versionado**: un conjunto de **dilemas representativos** del contrato federado, cada uno con su **resolución esperada** según la Constitución vigente. El banco es un **artefacto versionado** y se trata como parte del corpus de gobernanza, no como dato operativo.
- Por cada ejecución del banco: la **resolución efectiva** de cada agente frente a cada escenario, expresada como `criteriaApplied` + resultado normalizado (misma convención que los patrones A y B).
- El **`constitutionHash`** contra el que se evaluó el banco.

> Los escenarios del banco son **sintéticos y deidentificados** por construcción: se redactan para probar el criterio, nunca con datos reales de casos.

### 5.2 Método

1. **Versionar el banco contra la Constitución.** Cada versión del banco declara el `constitutionHash` que valida. Un cambio de Constitución **invalida** el banco hasta que se revisa.
2. **Ejecutar el banco** presentando el mismo escenario hipotético a los agentes relevantes para cada caso (los que participan en el corredor que el escenario modela) y comparando sus respuestas.
3. **Comparar resoluciones** entre agentes y contra la resolución esperada. La unidad de comparación es la coherencia de `criteriaApplied` + resultado, no la redacción.
4. **Localizar incoherencias.** Distinguir: (a) un agente discrepa de la esperada —síntoma de drift en una Capa Departamental, se deriva a Adoption; (b) **varios agentes resuelven el mismo escenario de formas mutuamente incompatibles** —drift federado de coherencia, o drift en la propia Constitución que no se ha propagado bien; esto se queda aquí.
5. **Cerrar el bucle con A y B.** Una incoherencia confirmada genera o actualiza un escenario, y puede explicar firmas nuevas del Patrón A o excepciones del Patrón B.

### 5.3 Señales / Umbrales

- **Cualquier** par de agentes que resuelve un mismo escenario de forma incompatible es señal —la coherencia es binaria por escenario, no estadística.
- **Desviación respecto de la resolución esperada** en un escenario de criticidad alta.
- **Regresión**: un escenario que antes pasaba y ahora falla tras un cambio del entorno (nuevo agente, nuevo bloque, nueva versión de descriptor) sin cambio de Constitución que lo justifique.

### 5.4 Cadencia

Cadencia base **trimestral**, modulada por criticidad (§2.1) — **mensual** para bancos que cubren dominios de criticidad alta. Y, de forma **no negociable**:

> **El Patrón C es obligatorio tras cada cambio de la Constitución.** Toda enmienda constitucional ratificada exige re-ejecutar el banco —y revisar su versión— **antes** de considerar el cambio estabilizado. Una Constitución nueva sin banco re-ejecutado es una Constitución no verificada.

También se ejecuta al **alta de un nuevo agente** en un corredor cubierto —es complementario del *gate de coherencia*, que verifica el descriptor en el registro, no la conducta— y al **cambio de bloque o de descriptor** de un participante.

### 5.5 Responsable

El **cuarto custodio (plataforma de federación)** es **dueño del banco**: lo versiona, lo ejecuta y lo mantiene alineado con la Constitución. La **custodia de cada capa** aporta y revisa los escenarios de su dominio, y firma la resolución esperada de los escenarios que la afectan. La obligatoriedad post-enmienda recae sobre el cuarto custodio como **condición de cierre** del proceso de cambio de Constitución.

### 5.6 Qué dispara revisión

- Una **incoherencia entre agentes** confirmada dispara revisión de gobernanza inmediata: la federación no tiene un criterio único donde debería tenerlo.
- Una **regresión** tras un cambio de Constitución dispara la **reapertura** de esa enmienda hasta restaurar la coherencia.
- Una desviación de un solo agente respecto de la esperada se **deriva a Adoption** como drift a nivel agente.

### 5.7 Qué NO es

- **No es** un banco de pruebas de funcionalidad ni de rendimiento del agente; prueba **criterio compartido**, no capacidad.
- **No es** un sustituto de A y B: A vigila la operación real, B vigila las excepciones reales, C vigila el criterio **en frío**. Los tres son complementarios.
- **No es** un artefacto operativo con datos reales: el banco es sintético y deidentificado por contrato.

---

## 6. Procesos, no productos

Los tres patrones describen **qué observar, cómo y quién responde**. Deliberadamente **no** nombran herramientas: el almacenamiento de los logs correlacionados, la consulta sobre `correlationId`/`criteriaApplied`, el registro de excepciones consultable y el *dashboard* de coherencia los aporta el **stack de la organización** a través de su plano de observabilidad y políticas, conforme a **CF-05** ([`./criterios-funcionales.md`](./criterios-funcionales.md)). Federation no proporciona el *dashboard* que los muestra; lo que normaliza es el **método de detección**, y lo que el stack aporta es la **instrumentación**.

Para llevar estos patrones a la operación:

- La **plantilla operativa** —turnos, responsables nominales, umbrales concretos, plantilla de acta de revisión— se redacta a partir de [`../../templates/federation/playbook-deteccion-drift.md`](../../templates/federation/playbook-deteccion-drift.md).
- Las **recetas sectoriales** —umbrales y cadencias afinados por sector regulado (sanidad, financiero, sector público…) donde la criticidad justifica análisis más finos— viven en [`./appendix/drift-recipes/`](./appendix/drift-recipes/), donde sí pueden citarse productos y dialectos concretos sin contaminar el cuerpo normativo (ver el *test de pertenencia* en [`./regla-anti-acoplamiento.md`](./regla-anti-acoplamiento.md)).

---

## 7. Relación con los tres niveles del corpus

- **Manifiesto** — este documento materializa el §3.4: la federación que se observa a sí misma. El drift es una métrica de primera clase (§2 del manifiesto), no un subproducto de las métricas técnicas.
- **Cuerpo normativo** — los patrones consumen los contratos de [`./esquema-bloque-contexto-cultural.md`](./esquema-bloque-contexto-cultural.md) (`correlationId`, `criteriaApplied`, `DecisionHop`, `deidToken`, `constitutionHash`) y de [`./esquema-identidad-agente.md`](./esquema-identidad-agente.md) (criticidad del dominio, `agentId`), se enmarcan en [`./guia-arquitectura-funcional.md`](./guia-arquitectura-funcional.md) y [`./criterios-funcionales.md`](./criterios-funcionales.md), y usan el vocabulario fijado en [`./glosario-federacion.md`](./glosario-federacion.md).
- **Apéndice (vivo)** — las recetas sectoriales con productos y dialectos van en [`./appendix/drift-recipes/`](./appendix/drift-recipes/).
- **Adoption** — el **drift a nivel agente** se trata fuera de aquí. Este documento solo cubre el **drift federado**.

---

### Enlaces relacionados

- [`../manifesto.md`](../manifesto.md) — manifiesto paraguas del ecosistema Myrmion.
- [`./manifesto.md`](./manifesto.md) — manifiesto de Myrmion Federation (§3.4 detección de drift, §5 gobernanza).
- [`./criterios-funcionales.md`](./criterios-funcionales.md) — CF-01..CF-06 (CF-05: observabilidad agent-aware).
- [`./glosario-federacion.md`](./glosario-federacion.md) — vocabulario normativo (drift federado, patrones A/B/C).
- [`./esquema-bloque-contexto-cultural.md`](./esquema-bloque-contexto-cultural.md) — `correlationId`, `criteriaApplied`, `DecisionHop`, `deidToken`.
- [`./esquema-identidad-agente.md`](./esquema-identidad-agente.md) — descriptor de agente y criticidad del dominio.
- [`./regla-anti-acoplamiento.md`](./regla-anti-acoplamiento.md) — sin marcas en el cuerpo; recetas en el apéndice.
- [`./guia-arquitectura-funcional.md`](./guia-arquitectura-funcional.md) — encaje de las cuatro capas.
- [`../../templates/federation/playbook-deteccion-drift.md`](../../templates/federation/playbook-deteccion-drift.md) — plantilla operativa.
- [`../../templates/federation/registro-excepciones.md`](../../templates/federation/registro-excepciones.md) — registro de excepciones (entrada del Patrón B).
- [`./appendix/drift-recipes/`](./appendix/drift-recipes/) — recetas sectoriales.

---

*Patrones de detección de drift — versión 1.0. Parte del corpus normativo.*
