# Framework de Adopción Corporativa de IA

**Manifiesto — versión 1.0**

*Un framework opensource para empresas que adoptan IA mediante productos comerciales y necesitan que esa adopción refleje su cultura, no la del proveedor.*

*Parte de **Myrmion** — el ecosistema opensource que articula el trayecto de adopción corporativa de IA, desde la modelización cultural mediante productos comerciales (este framework, **Myrmion Adoption**) hasta la federación programática de agentes corporativos vía MCP (**Myrmion Federation**).*

---

## Por qué Myrmion

El nombre Myrmion remite a *myrmex* — hormiga en griego — y a los mirmidones, soldados de élite de Aquiles, conocidos por actuar como una sola unidad bajo un mando común sin perder eficacia individual. Las dos imágenes apuntan al mismo problema: **cómo coordinar muchos agentes — humanos, programáticos o productos comerciales asistidos por IA — de forma que actúen como una organización coherente sin ahogar la autonomía local de cada dominio**.

Una colonia de hormigas es la referencia canónica de inteligencia colectiva con gobernanza distribuida. Cada individuo sigue reglas locales, hereda criterios comunes, y emerge un comportamiento coordinado a nivel sistema sin que nadie esté dirigiendo cada decisión. Esa es la condición operativa que la adopción corporativa de IA persigue: cada departamento modela sus propios asistentes para su dominio, todos heredan la cultura de la organización, y el conjunto se comporta como una empresa coherente, no como un agregado de silos automatizados.

La falange de mirmidones añade el otro eje. Cuando los agentes departamentales pasan de operar en paralelo a invocarse mutuamente — propagando contexto, encadenando decisiones, escalando entre dominios sin intermediación humana — el reto deja de ser cultural y se vuelve técnico. Lo que separa a una falange disciplinada de una turba armada es exactamente la gobernanza federada que Myrmion Federation aporta sobre el protocolo MCP.

Myrmion como ecosistema opensource articula el trayecto entre las dos imágenes. **Empiezas por la colonia — Myrmion Adoption — y evolucionas a la falange — Myrmion Federation — cuando tu organización lo necesita.** Las dos fases comparten sustrato: la Constitución Corporativa que articulas en Adoption es la misma que materializas programáticamente en Federation. Lo que cambia es el grado de programaticidad, no la cultura ni el método.

Este manifiesto cubre la primera fase. Describe cómo articular el modelado cultural cuando tu adopción de IA se materializa en productos comerciales — Copilot sobre Microsoft 365, Claude con Cowork, ChatGPT Enterprise, Gemini Enterprise, Custom GPTs, asistentes embebidos en tu CRM o ERP. Es la fase donde la mayoría de organizaciones está hoy, y la fase donde se gana o se pierde la adopción real, mucho antes de que la federación programática entre en la ecuación.

---

## 1. El problema que este framework reconoce

La mayoría de empresas que están adoptando IA hoy no construyen agentes desde cero. Despliegan productos: Copilot sobre Microsoft 365, Claude con Cowork, ChatGPT Enterprise, Gemini Enterprise, Custom GPTs, asistentes embebidos en su CRM o ERP. Eso es razonable. Construir agentes propios desde cero rara vez tiene sentido para una empresa cuya tesis no es la inteligencia artificial.

El problema no es la elección de productos. El problema es lo que pasa después.

Los productos comerciales vienen con valores por defecto que no son neutros. Tienen un tono, un sesgo de respuesta, un criterio para decidir qué recomendar y qué evitar, una forma de redactar, una jerarquía implícita de qué es importante. Esos defaults son el resultado de decisiones de diseño tomadas por el proveedor para servir a su mercado promedio — que casi nunca es el tuyo. Cuando una organización adopta el producto sin más, lo que obtiene no es *su* asistente: obtiene el asistente del proveedor con el logo de su empresa encima.

Durante los primeros meses esto pasa desapercibido. Los empleados están encantados de tener una herramienta que les ahorra tiempo. Los KPIs de adopción suben. La dirección comunica el éxito. Y mientras tanto, sin que nadie lo decida explícitamente, los criterios con los que la organización redacta correos a clientes, califica leads, prepara informes, sintetiza reuniones o resuelve dudas internas se han homogeneizado hacia el promedio de internet con un barniz corporativo encima.

A los seis meses la marca interna se ha vuelto borrosa. A los doce, alguien en el comité de dirección propone migrar de proveedor pensando que el problema es el modelo. No lo es. El problema es que la organización delegó, sin saberlo, una decisión que era suya: cómo piensa, cómo decide, cómo habla.

Este framework existe para que esa delegación deje de ocurrir.

## 2. Tres principios

El framework descansa sobre tres principios que conviene declarar antes de entrar en arquitectura.

**Cultura modelable.** Toda organización tiene una cultura — una forma de decidir, una voz, criterios de calidad, restricciones implícitas y explícitas. Esa cultura es modelable: se puede articular como un artefacto explícito, versionable y auditable, no como sabiduría tácita. Las organizaciones que ya tienen ese trabajo hecho (manuales de marca, código ético, políticas internas escritas) tienen ventaja. Las que no, tienen un trabajo previo que hacer — y descubrirán que ese trabajo es valioso por sí mismo, independientemente de la IA.

**Dominio descentralizado.** Las personas que mejor conocen un dominio son las que viven en él. Quién mejor que el equipo legal para articular cómo debe razonar un asistente legal. Quién mejor que marketing para definir la voz que ellos mismos se exigen. Quién mejor que finanzas para definir qué es un cierre limpio de mes. Centralizar el modelado de todos los dominios en un equipo de IA produce asistentes mediocres que reflejan la idea que el equipo de IA tiene de cómo trabajan los demás, no cómo trabajan de verdad.

**Gobernanza federada.** Si cada departamento modela sus propios asistentes sin más, el resultado no es coherencia distribuida — es fragmentación. Para que la federación funcione hace falta una capa transversal que todos los asistentes hereden por construcción, no por buena voluntad. Esa capa es la **Constitución Corporativa**. La gobernanza federada no es centralización camuflada: es la mínima estructura común que permite la libertad departamental sin que la organización se descomponga.

Estos tres principios no son negociables dentro del framework. Si una empresa rechaza alguno, este framework no es para ella. Hay otros caminos válidos, pero no son éste.

## 3. Arquitectura

La arquitectura del framework es deliberadamente simple. Un **Marco de Modelado** compuesto por tres capas jerárquicas, más una decisión de cómo materializarlas en los productos comerciales que la organización ya usa.

Las tres capas, en orden de precedencia decreciente:

1. **Marco Regulatorio.** Heterónoma. Viene de fuera y la organización no la negocia.
2. **Constitución Corporativa.** Autoritaria. La organización la define y la versiona.
3. **Capas departamentales.** Específicas de dominio. Las modela cada departamento.

En caso de conflicto entre capas, la superior prevalece sin excepciones. Esta jerarquía es el principio arquitectónico más importante del framework y conviene declararlo antes de entrar en el detalle de cada capa: ningún criterio cultural puede contradecir una obligación regulatoria, y ningún criterio departamental puede contradecir un principio cultural transversal.

### 3.1 Marco Regulatorio

El Marco Regulatorio captura las obligaciones legales y normativas que aplican a la organización por su jurisdicción, sector y naturaleza de los datos que maneja. RGPD y EU AI Act para cualquier organización europea que procese datos personales. LOPDGDD y obligaciones AEPD para España específicamente. Marcos sectoriales — financiero, sanitario, sector público — donde aplique. Restricciones contractuales con clientes que se hayan asumido como obligación de cumplimiento.

A nivel internacional, esta capa absorbe también marcos voluntarios pero ampliamente referenciados como base de buenas prácticas: el NIST AI Risk Management Framework, la norma certificable ISO/IEC 42001 sobre sistemas de gestión de IA, y los crosswalks que ambos mantienen con el EU AI Act. El framework no opina sobre cuál de estos marcos seguir como referencia primaria — esa decisión depende de la jurisdicción operativa de la organización, su exposición a clientes en distintos mercados y los requisitos contractuales que haya asumido. La función del Marco Regulatorio dentro del framework es articular el resultado de esa decisión como artefacto operativo que los asistentes deben respetar, sea cual sea la base normativa de origen.

A diferencia de las otras dos capas, el Marco Regulatorio no es algo que la organización elija o defina. Lo recibe. Lo único que la organización decide es cómo lo articula como artefacto explícito que sus asistentes deben respetar. Modificarlo solo es posible cumpliendo más estrictamente, nunca relajándolo.

Esta capa puede ser mínima o casi vacía para algunas organizaciones — una pyme de servicios B2B que no maneja datos personales sensibles ni opera en sectores regulados puede tener un Marco Regulatorio que se reduzca a *"aplica RGPD en su forma básica, sin obligaciones sectoriales adicionales"*. Eso es legítimo y suficiente. El framework no impone complejidad regulatoria donde no existe. Pero cuando existe, manda.

La custodia del Marco Regulatorio es responsabilidad del DPO, del equipo legal o de compliance — no del equipo de transformación digital ni de la función de IA. Esta separación de responsabilidades es deliberada: la capa regulatoria se actualiza cuando aparece nueva normativa, no cuando lo decide el calendario interno de la organización, y la persona o equipo que la custodia debe tener autoridad para imponer cambios sin negociación.

Una observación importante: el Marco Regulatorio articulado como artefacto del framework **no es asesoría legal y no la sustituye**. Es la traducción operativa, escrita por personas con criterio jurídico, de las obligaciones que los asistentes deben respetar. La interpretación jurídica de una norma sigue siendo trabajo del equipo legal; el framework solo proporciona el lugar donde esa interpretación se materializa de forma que los asistentes puedan heredarla.

### 3.2 Constitución Corporativa

La Constitución Corporativa es el documento que captura los elementos culturales de la organización que todo asistente debe heredar, sea cual sea el departamento que lo modele o el proveedor sobre el que corra.

Una Constitución bien construida cubre, como mínimo, cinco capas:

- **Identidad.** Quiénes somos, qué hacemos, a quién servimos, qué nos diferencia. No es la página *Sobre nosotros* de la web — es la versión que un asistente necesita leer para responder coherentemente cuando alguien le pregunta algo que toca la organización.
- **Voz.** Cómo hablamos. Registro, vocabulario que usamos, vocabulario que evitamos, ejemplos concretos de "esto sí" y "esto no". Una Constitución sin ejemplos prácticos de voz envejece mal.
- **Principios de decisión.** Cómo desempatamos cuando dos cosas razonables se contradicen. Si un cliente pide algo que técnicamente está fuera de su contrato pero pequeño, ¿priorizamos servir o cumplir? Si un argumento comercial puede leerse como exagerado, ¿lo matizamos o lo dejamos? Estas son las decisiones que un asistente toma constantemente sin que nadie le diga cómo.
- **Restricciones.** Qué no hacemos nunca. Compromisos contractuales que nadie debe asumir sin pasar por legal. Cifras que nadie debe compartir externamente sin pasar por finanzas. Afirmaciones de producto que nadie debe hacer sin pasar por producto. Formatos prohibidos. Datos vetados.
- **Escalado.** Cuándo el asistente debe parar y devolver el caso a un humano. Esto es probablemente lo más importante y lo que peor se modela por defecto: los asistentes de los proveedores tienden a "ayudar siempre", lo que en contextos corporativos es a veces exactamente el comportamiento equivocado.

La Constitución debe vivir como documento versionado, idealmente en un repositorio que cualquier persona de la organización pueda leer y comentar. No en un Google Doc compartido entre cinco directivos. La trazabilidad de cambios es parte del valor: cuando dentro de tres años alguien pregunta por qué los asistentes empezaron a hacer X en marzo de 2027, debe haber un commit, una pull request y una discusión.

Hay un punto que conviene anticipar: muchas organizaciones descubrirán al intentar escribir su Constitución que no tienen claridad cultural suficiente para hacerlo. Esa incomodidad inicial es información, no un fallo. Si una empresa no puede articular su voz en cinco páginas defendibles, sus asistentes nunca la van a tener — con o sin framework. El proceso de escribir la Constitución es, para muchas organizaciones, el ejercicio más útil de todo el framework.

La Constitución Corporativa hereda y respeta el Marco Regulatorio. En cualquier punto donde la cultura corporativa pueda entrar en tensión con una obligación regulatoria — un asistente que la cultura empuja a ser proactivo y comunicativo pero la regulación obliga a ser cauteloso con cierta información, por ejemplo — la Constitución debe articular explícitamente el límite, no dejarlo al criterio del modelador departamental.

### 3.3 Las capas departamentales

Cada departamento que adopta IA construye su propia capa de modelado sobre la Constitución y, transitivamente, sobre el Marco Regulatorio. Esa capa cubre lo que es específico del dominio: terminología, plantillas, flujos típicos, casos límite, integraciones con sistemas internos, criterios de calidad propios.

Una capa departamental no repite las capas superiores. Las hereda. Las menciona donde haga falta y las extiende donde el dominio lo requiera. Si la Constitución dice "no asumimos compromisos sin pasar por legal", la capa departamental de ventas no necesita repetirlo — necesita explicar qué tipo de compromisos típicos del día a día comercial caen claramente fuera (decir que llamamos a un cliente mañana) o claramente dentro (firmar un descuento del 15%).

La responsabilidad de modelar cada capa departamental es del propio departamento. La función de IA o transformación digital — si existe — actúa como facilitador, revisor de coherencia con las capas superiores y guardián del proceso. No como modelador. Esto es importante: si la función central modela los asistentes departamentales, el framework ha fracasado en su propio principio fundamental.

Un criterio práctico para evitar que la frontera entre capas se desdibuje al escribir: si un principio o regla aplica a más de un departamento, pertenece a la Constitución o al Marco Regulatorio según su naturaleza; si solo aplica a uno, va en la capa departamental. Mantener esta disciplina es responsabilidad de la custodia, y es uno de los puntos donde el framework se gana o se pierde con el tiempo.

La distinción entre una capa supraordenada que define autoridad y permisos para ejecutar y delegar, y capas operativas que aplican procedimientos contextuales durante la ejecución, no es exclusiva de este framework. Aparece formalizada en literatura académica reciente — por ejemplo, en el trabajo sobre *Federated Computing as Code* del campo de la computación federada con conciencia de soberanía, donde se separa explícitamente *governanza constitucional* de *governanza procedural*. El framework comparte ese eje de razonamiento, lo aterriza en un dominio organizativo — no técnico — y lo extiende a la articulación cultural que es el objeto propio de la adopción corporativa de IA.

### 3.4 Materialización en productos

Aquí es donde el framework se vuelve deliberadamente abstracto. La Constitución y las capas departamentales deben materializarse en los productos que la organización ha elegido — y los productos comerciales tienen mecanismos distintos para absorber este modelado.

Algunos productos exponen instrucciones de proyecto o espacio. Otros usan asistentes personalizados con prompts del sistema. Otros tienen Studios o entornos de configuración con interfaces gráficas. Otros permiten conectar fuentes documentales que el asistente consulta antes de responder. Otros combinan varios mecanismos.

El framework no opina sobre qué producto es mejor. Opina sobre dos cosas:

**Primero, la elección del producto debe ser consecuencia del stack tecnológico real, no una decisión de marca.** Una organización con toda su operación en Microsoft 365 + Power BI tiene fricción mucho menor adoptando Copilot que adoptando un producto que requiere conectores y configuración adicional. Una organización heterogénea con flujo de trabajo intensivo en conocimiento (consultoría, legal, investigación, finanzas) probablemente encuentra mejor encaje en productos agnósticos al stack ofimático. Una organización cuyo caso de uso dominante es atención al cliente y necesita orquestar volumen tiene otras necesidades. La pregunta correcta no es *cuál es mejor*, es *cuál encaja con lo que ya tenemos*.

**Segundo, el modelado debe sobrevivir al producto.** Si dentro de dos años la organización decide cambiar de proveedor — y hay razones para que esto pase con frecuencia: cambios de pricing, evolución de capacidades, decisiones regulatorias — el Marco de Modelado completo (regulatorio, cultural y departamental) debe ser portable. Eso significa escribirlo en formato neutro (Markdown, no plantillas propietarias), mantenerlo fuera del producto en sí, y usar los mecanismos del producto solo como *materialización*, nunca como *almacenamiento canónico*.

El apéndice del framework, mantenido como documento vivo separado, recoge cómo se materializa el Marco de Modelado en los productos comerciales más usados a fecha actual, incluyendo los mecanismos que cada producto expone para cubrir obligaciones de la capa regulatoria (residencia de datos, retención, opt-out de entrenamiento, DPA firmable). Ese apéndice es responsabilidad de la comunidad, se actualiza con frecuencia, y se desacopla deliberadamente del cuerpo del framework para que el framework no envejezca con cada release de producto.

Aquí conviene declarar un límite con la misma honestidad con la que el framework reconoce los demás. El Marco Regulatorio declara prohibiciones sobre datos sensibles — seudonimizar antes de exponerlos a un asistente, no tratar datos de salud identificables, minimizar — pero en la fase de Adoption esas prohibiciones se cumplen por **disciplina humana y por los controles que el producto comercial expone** (selección de tier con DPA/BAA, bloqueo y coaching vía DLP/CASB, herramienta de des-identificación sancionada como paso previo), **no por una capa de redacción transparente en la ruta del prompt**. La redacción inline automática — enmascarar el dato sensible antes de que el prompt llegue al modelo, sin intervención humana — exige un intermediario programático en la ruta, y eso es territorio de Myrmion Federation. La protección de datos frente a un LLM vive, de hecho, en dos capas complementarias — una técnica (des-identificación/DLP) y una contractual (licenciamiento: DPA, BAA, residencia, no-entrenamiento) — que ninguna sustituye a la otra. La [Guía de protección de datos](./guia-proteccion-datos.md), documento vivo separado, articula ambas capas, el panorama de herramientas y una matriz de licenciamiento por requisito de cumplimiento. El framework prefiere declarar este límite a fingir que la disciplina humana es enforcement técnico.

## 4. Gobernanza

Un Marco de Modelado sin gobernanza son tres documentos que firma alguien y nadie lee. La gobernanza es lo que hace que el Marco viva.

El framework propone tres mecanismos mínimos.

**Custodia diferenciada por capa.** Cada capa tiene su responsable, y los responsables son distintos por diseño. El Marco Regulatorio lo custodia el DPO, el equipo legal o la función de compliance — quien tenga autoridad para imponer cambios sin negociación cuando aparezca nueva normativa. La Constitución Corporativa la custodia la función de transformación digital, dirección, marca o un equipo equivalente con visibilidad transversal. Las capas departamentales las custodia el propio departamento. Esta separación importa: una sola custodia para las tres capas convierte el framework en proyecto de un equipo, y los proyectos de un equipo mueren cuando ese equipo cambia.

**Revisión de coherencia.** Antes de que una capa departamental entre en producción, alguien — distinto del modelador — verifica que es coherente con las dos capas superiores. Esto no es una auditoría burocrática: es la lectura cruzada que cualquier organización seria aplica a documentos que comprometen su criterio. La revisión puede ser ligera (una persona del equipo central de transformación dedica medio día) o seria (panel formal con representación de legal, marca, dirección), según el riesgo del dominio. Para dominios que tocan datos personales sensibles o decisiones con impacto legal, la revisión debe incluir explícitamente al custodio del Marco Regulatorio.

**Detección de drift.** Con el tiempo, la realidad se aleja de lo declarado. Equipos cambian, criterios evolucionan, el día a día introduce excepciones que se naturalizan. El framework asume que esto va a pasar y propone revisar la concordancia entre las tres capas y el comportamiento real al menos cada seis meses. Para muchas organizaciones, esa revisión es la primera vez que ven con claridad cómo ha evolucionado su cultura sin que nadie lo decidiera.

**Gestión de excepciones.** En la operación real, un departamento legítimamente puede necesitar saltarse algo de la Constitución Corporativa para un caso concreto — un cliente con condiciones contractuales especiales, un canal de comunicación con tono distinto, una excepción justificada por contexto. La respuesta del framework no puede ser nunca *no hay excepciones* (entonces nadie respeta el Marco) ni siempre *sí, lo que haga falta* (entonces el Marco es decorativo). La regla operativa: las excepciones a la Constitución Corporativa son posibles si están documentadas, justificadas y limitadas en alcance temporal o de caso. Las excepciones al Marco Regulatorio no existen — solo cumplimiento o incumplimiento. Esa asimetría debe quedar explícita.

**Proceso de retirada.** Cuando una capa departamental queda obsoleta, un departamento desaparece o se reestructura, sus instrucciones no pueden seguir vivas en sistemas que ya no las representan. El framework propone un proceso explícito de retirada: marcar la capa como deprecated, notificar a los productos donde está materializada, ejecutar el desmaterializado y archivar la capa con su histórico. Sin este proceso, las organizaciones acumulan instrucciones zombi que sus asistentes siguen aplicando años después de que el departamento que las escribió haya cambiado.

Estos mecanismos son ligeros por diseño. El framework no propone comités semanales ni procesos de aprobación de tres semanas. Si se vuelve burocrático, fracasa. La gobernanza tiene que ser proporcional al riesgo del dominio: el asistente que ayuda a finanzas a redactar correos internos necesita menos control que el asistente que prepara propuestas comerciales firmables o que el asistente que toca datos clínicos.

## 5. Interoperabilidad — y su frontera

Los productos comerciales, hoy, no soportan colaboración estructurada entre asistentes de distintos dominios de forma robusta. Hay integraciones puntuales — un Custom GPT puede llamar a una API, Copilot puede invocar Power Automate — pero ninguna constituye un protocolo de colaboración federada entre agentes con gobernanza compartida.

El framework reconoce esta limitación explícitamente y propone, mientras tanto, **patrones manuales de colaboración cruzada**:

- **Plantillas de handover.** Cuando una persona pasa el resultado de un asistente departamental a otro, lo hace usando una plantilla común que incluye contexto, decisiones previas, pendientes y criterios aplicables. La plantilla viaja con la persona, no con el asistente, pero garantiza que la cultura no se pierde en el cruce de dominios.
- **Rituales de coherencia.** Reuniones cortas y periódicas entre los modeladores de capas departamentales para identificar dónde sus asistentes podrían estar dando respuestas contradictorias o incoherentes ante el mismo escenario. Estos rituales se parecen a las communities of practice que ya existen en muchas organizaciones — porque son lo mismo, aplicado a un objeto nuevo.
- **Glosario corporativo compartido.** Un único documento de términos clave que todas las capas departamentales referencian. Sin esto, el agente de marketing entiende "lead cualificado" de una manera y el agente de ventas de otra, y los humanos pasan media reunión averiguando dónde está el desfase.

Estos patrones son suficientes para muchas organizaciones durante mucho tiempo. Hay un punto, sin embargo, en el que se quedan cortos: cuando los asistentes departamentales necesitan invocarse mutuamente sin intermediación humana, propagando contexto cultural y manteniendo la cadena de decisiones auditable. Cuando eso pasa, la organización está saliendo del territorio de este framework y entrando en el de **Myrmion Federation**, la siguiente fase del ecosistema, que cubre federación programática de agentes corporativos extendiendo el protocolo MCP con una capa de gobernanza federada culturalmente consciente.

La frontera entre las dos fases no es ambigua, pero conviene un criterio operativo concreto para no caer en la idealización de ninguna de las dos: **cuando los handovers manuales entre departamentos empiezan a ocupar más tiempo del que ahorra la IA, has cruzado la frontera**. Antes de eso, los patrones manuales son suficientes y este framework te basta. Después, la fricción acumulada justifica adoptar Myrmion Federation.

Si tu adopción de IA se materializa en productos comerciales y los humanos siguen siendo los que mueven contexto entre dominios, este framework te basta. Si necesitas que los agentes hablen entre sí con gobernanza, te toca Myrmion Federation.

## 6. Adopción

El framework se adopta por fases. Cada fase deja la organización en un estado defendible aunque la siguiente no llegue.

**Fase 1 — Marco de Modelado mínimo viable.** Antes de modelar ningún departamento, la organización articula las dos primeras capas: identifica y escribe la versión inicial del Marco Regulatorio aplicable (con apoyo de legal/DPO) y la primera versión de la Constitución Corporativa. Es un ejercicio de cuatro a seis semanas si la cultura está articulada en otros documentos previos y las obligaciones regulatorias ya están claras; mucho más si no lo están. La primera versión puede tener huecos declarados — secciones que dicen explícitamente "esto está pendiente de definición" — pero no puede tener contradicciones. Un Marco incompleto es trabajable; uno incoherente, no.

**Fase 2 — Primera capa departamental.** Se elige un departamento piloto, idealmente uno con voluntad genuina y criterio articulado, no el que la dirección "quiere transformar". Ese departamento, asistido por la función de transformación, modela su capa sobre la Constitución y la materializa en el producto que ya está usando o ha decidido usar. Duración típica: dos a cuatro semanas tras tener Constitución.

**Fase 3 — Segundo y tercer departamento.** Con la lección aprendida del piloto, se modelan dos departamentos más en paralelo. Aquí emergen las primeras tensiones de coherencia entre capas — el momento en el que la Constitución se prueba en serio. Es normal que la Constitución tenga que evolucionar (el Marco Regulatorio raramente, porque no depende de la organización). Lo importante es que esa evolución suceda con trazabilidad, no con parches silenciosos.

**Fase 4 — Gobernanza explícita.** Cuando hay tres o más capas vivas, la gobernanza informal deja de funcionar y hace falta formalizar custodia, revisión y detección de drift. Si esto se intenta antes (en fase 2, por ejemplo), se convierte en burocracia que ahoga la adopción. Si se hace después (en fase 5 o 6), las capas ya están drifteando entre sí y recuperar coherencia cuesta el doble.

**Fase 5 — Madurez y revisión.** A los seis o doce meses de la primera capa en producción, la organización hace su primera revisión sistemática: qué está funcionando, qué ha drifteado, qué hay que actualizar en cada capa, qué patrones manuales se están quedando cortos. De aquí salen las decisiones sobre si la organización tiene suficiente con esta fase del ecosistema o necesita graduarse a Myrmion Federation.

## 7. Cómo saber si funciona

El framework rechaza explícitamente las métricas de adopción superficiales — número de usuarios activos, número de prompts ejecutados, satisfacción declarada. Esas métricas suben con cualquier producto razonable y no dicen nada sobre si la cultura se está reflejando o se está erosionando.

Las métricas que importan son cuatro:

**Reconocibilidad.** Si tomas tres respuestas al azar de un asistente departamental y las muestras a alguien de la empresa que no sabe de dónde vienen, ¿reconoce el estilo, los criterios y el tono como propios de la organización? Si la respuesta es no, el modelado no está funcionando, da igual cuántos usuarios activos haya.

**Coherencia transversal.** Si dos asistentes de departamentos distintos se enfrentan al mismo escenario hipotético, ¿dan respuestas compatibles, aunque cubran ángulos diferentes? La incompatibilidad sistemática es síntoma de drift en alguna capa.

**Tasa de escalado adecuada.** Los asistentes deberían escalar a humano en los casos que la Constitución marca como escalables, y no escalar en los que no. Si escalan demasiado, son inútiles. Si escalan demasiado poco, son peligrosos. Esta métrica es la más infrarrepresentada en la adopción típica y la que más ayuda a calibrar el modelado.

**Trazabilidad de criterio.** Cuando una decisión asistida por IA se cuestiona — internamente, por un cliente o por un regulador — la organización debe poder reconstruir qué criterio se aplicó y desde qué capa del Marco de Modelado venía. Si la respuesta es *"no sabemos, lo dijo el asistente"*, la gobernanza ha fracasado, aunque las otras tres métricas estén bien. Esta métrica adquiere especial peso cuando la decisión cuestionada toca el Marco Regulatorio: ahí la trazabilidad deja de ser higiene y pasa a ser obligación de cumplimiento.

Estas cuatro métricas son evaluables sin tooling complejo. Lo único que requieren es tiempo de revisión humana periódica, que es exactamente lo que la gobernanza descrita en §4 institucionaliza.

## 8. Lo que este framework no es

Conviene declarar con la misma claridad lo que el framework deliberadamente excluye, para evitar malentendidos.

**No es una metodología de transformación digital.** No cubre estrategia tecnológica, hoja de ruta de digitalización, ni rediseño de procesos. Da por hecho que la organización ya ha decidido adoptar IA y se concentra exclusivamente en cómo modelarla.

**No es un manual de productos.** No recomienda Copilot sobre Claude, ni viceversa. La elección es de la organización y depende de su stack. El apéndice ayuda con la materialización, no con la decisión.

**No es asesoría legal.** El Marco Regulatorio articulado dentro del framework es la traducción operativa de obligaciones que los asistentes deben respetar, pero la interpretación jurídica de cada norma sigue siendo trabajo del equipo legal o del DPO. Una organización que use el framework para sustituir a su función jurídica está malentendiendo lo que el framework hace.

**No reemplaza la formación.** Modelar bien los asistentes es necesario pero no suficiente. Las personas que los usan también necesitan formación específica sobre cómo trabajar con ellos sin convertirlos en muleta — pero ese trabajo cae fuera del alcance del framework.

**No resuelve la interoperabilidad estructurada.** Como se ha declarado en §5, eso es territorio de Myrmion Federation. Pretender que esta fase del ecosistema lo cubre sería vender humo.

**No es prescriptivo en cultura.** El framework define la *estructura* del Marco de Modelado, no su *contenido*. Una empresa puede tener una Constitución que define principios opuestos a otra empresa, y el framework no opina. Lo único que exige es coherencia interna entre las tres capas y aplicabilidad a sus asistentes.

**No aplica igual a todas las organizaciones.** Hay dos categorías donde el framework requiere matizaciones importantes. Las organizaciones extremadamente reguladas — sanidad clínica con decisión médica, ciertas áreas de defensa, banca de inversión en activos sensibles — pueden usarlo, pero el peso del Marco Regulatorio domina sobre las otras capas hasta el punto de que el ejercicio cultural queda subordinado al cumplimiento normativo. Y las organizaciones muy pequeñas, por debajo de unas treinta personas, donde la cultura es coherente por proximidad humana directa, probablemente encuentren que formalizar tres capas es burocracia desproporcionada — en su caso, una versión extremadamente ligera (un único documento que mezcle elementos regulatorios, culturales y operativos) puede ser suficiente. El framework reconoce ambas excepciones explícitamente.

## 9. Objeciones anticipadas

Conviene tomar posición sobre los puntos donde un lector crítico va a parar primero. No para clausurar el debate — los frameworks vivos se discuten siempre — sino para que la conversación empiece desde donde corresponde y no desde malentendidos predecibles.

**Las tres capas se ven elegantes en el papel, pero las organizaciones van a colapsarlas al escribir.**

Sí, va a pasar. La tendencia natural cuando una organización empieza a articular el Marco de Modelado es meter en la Constitución cosas que pertenecen a la capa departamental — terminología específica de marketing, criterios de cualificación de leads, plantillas operativas — o al revés, dejar en una capa departamental principios que aplican transversalmente porque allí es donde se han redactado primero. El error no es conceptual, es de disciplina al escribir, y la disciplina se erosiona en el día a día.

La respuesta no es construir mecanismos automáticos para detectar el colapso — sería sobreingeniería para un problema que es humano. La respuesta es la regla práctica que el framework declara explícitamente en §3.3: si una línea aplica a más de un departamento, va arriba; si solo aplica a uno, va abajo. Y aplicarla con disciplina es responsabilidad de la custodia. Las organizaciones que no aceptan esa carga no están preparadas para este framework — lo cual es una respuesta legítima, no un fracaso del framework.

**La frontera con Myrmion Federation es clara, pero hay un escenario intermedio incómodo.**

Sí, lo hay, y conviene reconocerlo. Existen organizaciones cuya colaboración entre dominios es real pero de baja frecuencia: el asistente legal y el comercial cruzan información dos veces por semana, no veinte por hora. Para esas organizaciones, la fricción de adoptar Myrmion Federation con su gateway, su registro federado y su gobernanza programática puede ser desproporcionada respecto al beneficio. Pero los patrones manuales también empiezan a sentirse cortos.

La respuesta del framework a este escenario es operativa, no teórica: el criterio de cruce de frontera es cuándo los handovers manuales empiezan a ocupar más tiempo del que ahorra la IA. Antes de eso, los patrones manuales bastan, aunque rocen. Después, la fricción acumulada justifica la inversión. No hay un punto técnico de cruce; hay un punto económico, y cada organización lo encuentra cuando lo encuentra. El framework prefiere ser honesto sobre esa zona gris en vez de inventar una capa intermedia que probablemente no aguantaría contacto con la realidad operativa.

**Las cuatro métricas suenan razonables, pero una de ellas requiere infraestructura que los productos comerciales no exponen bien.**

Cierto. Reconocibilidad, coherencia transversal y trazabilidad de criterio son evaluables con tiempo de revisión humana periódica — caro, pero factible y de hecho deseable, porque obliga a que personas reales lean lo que sus asistentes están produciendo. La métrica de tasa de escalado adecuada es distinta: idealmente requeriría infraestructura para medir cuántas veces el asistente escaló un caso a humano cuando debía y cuántas no escaló cuando debía. Esa infraestructura no la exponen bien los productos comerciales hoy.

La respuesta del framework es admitirlo y proponer aproximación cualitativa: revisar muestras representativas de interacciones, marcar las que escalaron como correctas o incorrectas, identificar patrones. Es trabajo manual, no es perfecto, pero es lo viable. Y cuando esa aproximación deja de bastar — porque el volumen es demasiado alto o el riesgo regulatorio demasiado serio — esa carencia es uno de los disparadores naturales para graduarse a Myrmion Federation, donde la observabilidad agent-aware permite medir esto con rigor. Es decir: que esta métrica sea difícil en esta fase del ecosistema es una característica del modelo ligero, no un defecto. Comunica al lector cuándo ha excedido el alcance del marco.

**La separación de custodias entre tres responsables distintos no encaja con cómo trabajan muchas empresas hoy.**

Cierto. Muchas organizaciones grandes tienen una función de transformación digital que ha acumulado responsabilidad sobre todo lo que toca IA, incluyendo legal y compliance por defecto cuando estos no están suficientemente involucrados. Y muchas pequeñas no tienen ni siquiera una función formal de transformación, así que tres custodios distintos puede sonar a estructura imposible.

La respuesta del framework es que la separación de custodias no es prescripción organizativa, es prescripción de roles. En una pyme, los tres roles los puede asumir el mismo equipo de tres personas con sombreros distintos: cuando el documento que se actualiza es el Marco Regulatorio, manda el sombrero de compliance; cuando es la Constitución, manda el de dirección; cuando es una capa departamental, manda el del responsable del dominio. Lo que el framework no admite es que los tres sombreros los lleve la misma persona simultáneamente, porque entonces no hay revisión cruzada y la jerarquía de capas se vuelve decorativa. En organizaciones grandes, los tres sombreros suelen estar ya en personas distintas, así que la prescripción solo formaliza algo que existe; el cambio que sí impone es que esos tres roles tienen que coordinarse cuando antes operaban en silos.

Hay una versión más cínica de esta objeción que conviene también reconocer: las organizaciones donde la función de transformación digital ha acumulado poder y no quiere cederlo. En esos casos el framework va a generar fricción real — pero esa fricción es justamente el síntoma de que la organización tiene un problema previo de gobernanza que la IA solo va a amplificar.

**Este framework se parece a NIST AI RMF, ISO/IEC 42001 o EU AI Act. ¿No es redundante con lo que ya existe?**

La pregunta es legítima y conviene responderla con claridad. No es redundante porque opera a otro nivel.

NIST AI RMF describe qué riesgos gestionar y qué funciones (Govern, Map, Measure, Manage) deben existir en una organización que adopta IA. ISO/IEC 42001 es una norma certificable de sistema de gestión de IA: especifica qué políticas, roles y procesos deben existir y cómo se documentan. EU AI Act es regulación que define qué está prohibido, qué requiere transparencia y qué obligaciones tienen los sistemas de alto riesgo. Los tres son marcos sólidos, ampliamente adoptados, y este framework los respeta — de hecho, son el contenido típico de la Capa 1 del Marco de Modelado, no una alternativa a ella.

Lo que ninguno de los tres cubre es **cómo se modela operativamente la cultura corporativa para que los asistentes la hereden**, ni **cómo se descentraliza ese modelado en capas departamentales sin perder coherencia**, ni **cómo se elige y materializa el producto comercial sobre el que esos asistentes corren**. Esos son los huecos que este framework ocupa. La relación correcta no es competitiva — es aditiva. Una organización seria sobre adopción de IA probablemente termina con NIST AI RMF o ISO 42001 como referencia normativa, EU AI Act como obligación legal donde aplique, y un framework operativo como este para articular el cómo del día a día. Los tres niveles coexisten sin solapamiento real.

**El framework declara prohibiciones sobre datos sensibles pero no impide técnicamente que se incumplan.**

Es cierto, y es una limitación de la fase, no un descuido. El Marco Regulatorio puede declarar que no se exponen datos de salud identificables a un asistente, pero mientras una persona pueda pegarlos en la caja de texto de un producto comercial, la prohibición depende de la disciplina y de los controles que el producto expone — el tier contratado, la DLP/CASB que bloquea o avisa, la des-identificación sancionada como paso previo. El enforcement técnico transparente — redactar el dato antes de que llegue al modelo, automáticamente — requiere un intermediario programático en la ruta del prompt, que es precisamente lo que la fase de Adoption no tiene y Myrmion Federation sí. El framework responde de dos maneras: lo reconoce explícitamente en §3.4 en vez de disimularlo, y publica una [Guía de protección de datos](./guia-proteccion-datos.md) que articula las dos capas — técnica y contractual — y las herramientas realistas en cada fase. La asimetría declarada en §4 sigue vigente: las excepciones al Marco Regulatorio no existen, así que la organización que no puede garantizar el cumplimiento de una prohibición por los medios de Adoption debe restringir el caso de uso o graduarse a Federation, nunca relajar la prohibición.

## 10. Horizonte opensource

Este framework se publica como opensource por dos razones. La primera es que el problema que aborda es estructural y compartido — todas las organizaciones que adopten IA en los próximos años se lo van a encontrar — y resolverlo en abierto acelera la madurez del ecosistema. La segunda es que un framework cerrado mantenido por una persona o consultora envejece mal; un framework abierto con contribuciones reales evoluciona con el campo.

El framework se diseña explícitamente para coexistir con los marcos normativos y técnicos ya consolidados: complementa NIST AI RMF, ISO/IEC 42001 y EU AI Act como capa operativa, y se articula como punto de entrada para organizaciones que más adelante necesiten infraestructura programática de gobernanza federada — territorio que cubren proyectos opensource maduros como los gateways MCP y los toolkits de governance de agentes que han emergido durante 2025 y 2026.

Las contribuciones más valiosas serán de tres tipos: actualizaciones del apéndice de mapeo a productos comerciales conforme estos evolucionan; plantillas de Constitución y capas departamentales para sectores específicos (sanidad, financiero, sector público, manufacturing); y casos de uso anonimizados que permitan a otros aprender de implementaciones reales.

La frontera con **Myrmion Federation**, la siguiente fase del ecosistema que cubre federación programática de agentes corporativos vía MCP, se mantendrá explícita y bidireccional: las organizaciones que se gradúan de una fase a otra deben poder hacerlo sin tirar el trabajo previo, y las que se quedan en esta fase deben poder hacerlo sin sentir que están en una versión incompleta de algo más serio. No lo están: están exactamente donde tienen que estar.

---

*Manifiesto del Framework de Adopción Corporativa de IA — versión 1.0.*
