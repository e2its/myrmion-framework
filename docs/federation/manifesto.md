# Myrmion Federation

**Manifiesto — versión 1.0**

*Una capa de gobernanza federada culturalmente consciente para sistemas de agentes corporativos sobre el protocolo MCP.*

*Segunda fase del ecosistema **Myrmion**. La primera fase, **Myrmion Adoption**, articula el modelado cultural de IA en organizaciones que adoptan productos comerciales. Esta fase aborda el problema técnico que emerge cuando esos asistentes departamentales necesitan invocarse mutuamente sin intermediación humana, propagando contexto y manteniendo la cadena de decisiones auditable.*

---

## De la colonia a la falange

Myrmion Adoption se apoya en la imagen de la colonia: muchos individuos siguiendo reglas locales, heredando criterios comunes, comportándose como un sistema coherente sin coordinación central directa. Esa imagen funciona mientras los handovers entre dominios los hacen humanos.

Cuando los agentes empiezan a invocarse entre sí, la colonia ya no basta. Lo que se necesita es una falange: agentes coordinados con disciplina técnica bajo mando común, propagando contexto en cada movimiento, manteniendo formación bajo presión. La diferencia entre una falange y una turba armada es exactamente la gobernanza — y esa gobernanza, aplicada a sistemas de agentes corporativos sobre MCP, es lo que articula este manifiesto.

Federation no es una versión avanzada de Adoption ni la sustituye. Es la fase del ecosistema que se activa cuando el modelado cultural ya está hecho y la fricción de los handovers manuales empieza a costar más que la propia adopción. La Constitución Corporativa que articulaste en Adoption es la misma que aquí se materializa programáticamente. Lo que cambia es el grado de programaticidad, no la cultura ni el método.

---

## 1. El problema que esta fase reconoce

A medida que las organizaciones avanzan en la adopción de IA, los productos comerciales que usaban como contenedores de asistentes departamentales se van quedando cortos. Aparecen tres síntomas concretos:

**Los handovers entre dominios consumen más tiempo del que ahorra la IA.** El asistente legal produce un dictamen que el comercial necesita interpretar para responder a un cliente. Hoy, una persona toma el output de uno, lo resume, y se lo pasa al otro como input contextualizado. Ese trabajo de bisagra, que parecía marginal cuando había un solo asistente activo, se convierte en cuello de botella cuando hay siete.

**El contexto cultural no viaja con las llamadas.** Cuando dos asistentes departamentales se comunican vía integraciones puntuales — un Custom GPT que llama a una API, un Copilot que invoca Power Automate — lo que viaja es la información operativa: el dato, la pregunta, el resultado. Lo que no viaja es la versión de la Constitución Corporativa que cada lado está aplicando, ni el caso de negocio, ni los criterios que el dominio de origen ya había aplicado. El segundo asistente recibe un input descontextualizado y vuelve a aplicar criterios desde cero, a veces contradiciendo decisiones que ya se habían tomado upstream.

**La trazabilidad se rompe en la frontera entre dominios.** Cuando una decisión asistida por IA cruza varios departamentos — lead generado por marketing, calificado por ventas, validado por legal, materializado en propuesta comercial — y alguien la cuestiona después, reconstruir qué criterios se aplicaron, en qué orden y por qué, requiere un trabajo forense que ningún producto comercial soporta nativamente. La cadena de decisiones se vuelve opaca exactamente en el momento en que más importa: cuando hay que defender la decisión.

Estos tres síntomas no son patologías que se resuelvan con mejor formación o más asistentes. Son consecuencia estructural de adoptar IA sin una capa de federación. Resolverlos requiere infraestructura y método, no más prompts.

Esta fase del ecosistema existe para que la organización pueda dar ese salto sin perder la cultura que articuló en Adoption ni someterse a la cultura del proveedor que le venda el gateway.

## 2. Tres principios

Federation descansa sobre tres principios que conviene declarar antes de entrar en arquitectura.

**Compositividad sobre infraestructura existente.** El ecosistema opensource de gobernanza programática para sistemas de agentes ha madurado durante 2025 y 2026 más rápido de lo que cualquier framework propietario podía absorber. Hay implementaciones serias y mantenidas de policy enforcement, identity zero-trust, audit, service registry y observabilidad agent-aware sobre MCP. Federation no reimplementa nada de eso — se monta encima como capa de opinión cultural, contribuyendo lo que ningún proyecto técnico está cosiendo: el puente entre la Constitución Corporativa y la gobernanza programática.

**Cultura propagable.** En un sistema de agentes federados, el contexto que viaja en cada llamada inter-agente debe incluir la versión de la Constitución que el agente origen está aplicando, el caso de negocio, los criterios ya aplicados y la cadena de decisiones previas. Esto no es un detalle de implementación: es lo que distingue una falange de un grupo de mercenarios. Federation define cómo se materializa esa propagación sobre los mecanismos que MCP ya provee, sin requerir extensiones del protocolo base.

**Drift como métrica de primera clase.** En sistemas con muchos agentes coordinándose, el drift cultural — el momento en que las decisiones colectivas dejan de reflejar la Constitución que la organización articuló — es invisible si nadie lo mide específicamente. Las métricas técnicas habituales (latencia, error rate, throughput) no lo capturan. Federation eleva la detección de drift a métrica de primera clase, con patrones operativos para detectarlo a nivel federación, no solo agente por agente.

Estos tres principios no son negociables dentro del framework. Si una organización rechaza alguno — quiere construir su propio gateway, no propagar contexto cultural en las llamadas, o no medir drift — Federation no es para ella. Hay otros caminos válidos, pero no son éste.

## 3. Arquitectura

La arquitectura de Federation se articula en cuatro capas funcionales que se montan sobre la infraestructura opensource elegida. Las capas son funcionales, no físicas: cada una puede materializarse en uno o varios componentes del stack subyacente.

### 3.1 Capa de identidad y autorización

Cada agente departamental se materializa como un servidor MCP con identidad criptográfica propia, registrado en el service registry de la organización. Las llamadas inter-agente se autentican mutuamente vía mTLS o un equivalente del stack elegido, y cada tool invocada pasa por un policy engine que decide si la llamada está permitida antes de ejecutarse.

Esta capa la cubre la infraestructura opensource existente. Lo que Federation aporta encima es **un esquema corporativo común** para la identidad y los descriptores de capacidades: cómo se nombra cada agente, qué dominio cubre, qué nivel de criticidad tiene, qué clase de datos maneja, a qué versión de la Constitución Corporativa se adhiere. Sin este esquema común, el agente legal y el de marketing pueden registrarse y autenticarse correctamente y aun así ser incapaces de descubrirse y entenderse mutuamente sin coordinación humana previa.

El esquema corporativo es responsabilidad de la organización pero Federation publica una plantilla mínima que cubre los campos imprescindibles para el descubrimiento federado.

### 3.2 Capa de propagación de contexto cultural

Es la pieza técnicamente más original del framework y la que ningún gateway opensource cubre por defecto.

Cuando el agente A invoca al agente B vía MCP, además de los argumentos de la tool viaja un bloque de metadatos culturales que incluye, como mínimo: hash de la versión de la Constitución Corporativa aplicada por A, identificador del caso de negocio, hash de la capa departamental de la que deriva A, identificador del usuario originante (cuando aplique), cadena de decisiones previas relevantes (si la cadena tiene más de un salto), y un correlation id que persiste a lo largo de toda la cadena.

B recibe ese bloque, valida que la versión de Constitución que A aplicó es compatible con la suya, decide si aplica criterios adicionales propios de su dominio que A no podía conocer, y propaga el bloque actualizado en cualquier llamada subsiguiente que él mismo haga. La cadena de decisiones se reconstruye trivialmente desde el correlation id.

Esta propagación se materializa sobre los headers o metadata fields que MCP expone, sin requerir extensiones del protocolo. Federation define el esquema del bloque, no la transporte. La transporte la resuelve el gateway opensource elegido.

Hay un caso límite que conviene declarar explícitamente: cuando el agente B detecta que la versión de Constitución que A aplicó es incompatible con la suya — porque alguno de los dos no se ha actualizado tras un cambio normativo, por ejemplo — la llamada no procede. La política por defecto es escalado a humano con el bloque de contexto completo como evidencia. Permitir la llamada con criterios desfasados sería la antítesis del framework.

### 3.3 Capa de mapping Constitución → policy

La Constitución Corporativa que la organización articuló en Adoption es un documento en lenguaje natural, deliberadamente legible por humanos. Para que se aplique automáticamente en cada llamada inter-agente, hace falta materializarla en políticas que un policy engine — Cedar, OPA/Rego, equivalente del stack elegido — pueda evaluar en runtime.

Federation define convenciones para ese mapping, no las políticas concretas. Cada principio cultural traducible a policy tiene un patrón conocido — *"no asumimos compromisos sin pasar por legal"* se traduce típicamente a un policy template que evalúa si la tool invocada puede generar un compromiso contractual y, si es así, exige que la cadena de decisiones incluya un paso por el agente legal con resultado positivo. *"Cifras financieras no se exteriorizan sin pasar por finanzas"* se traduce a un policy template que detecta tools de comunicación externa y bloquea si los argumentos contienen patrones financieros sin endorsement de finanzas.

La des-identificación de datos sensibles es otro patrón canónico de este mapping, y el que cierra el hueco de enforcement técnico que la fase de Adoption no podía cubrir. *"No exponemos datos de salud identificables al modelo"* o *"los datos personales de cliente se seudonimizan antes de salir del dominio"* se traducen a un policy template que inspecciona los argumentos de la tool antes de la llamada inter-agente y redacta, tokeniza o bloquea según la categoría detectada — la redacción transparente en la ruta del prompt que en Adoption exigía un intermediario inexistente y que aquí es nativa (ver manifiesto de [Myrmion Adoption](../adoption/manifesto.md) §3.4 y la [Guía de protección de datos](../adoption/guia-proteccion-datos.md)). Cuando la redacción es reversible, el bloque de contexto cultural (§3.2) puede transportar los tokens necesarios para re-identificar la respuesta final en el agente de origen.

Estos policy templates son responsabilidad de la organización, pero Federation publica un catálogo mínimo de patrones recurrentes, con sus implementaciones de referencia para los stacks más usados. El catálogo es comunidad, no manifiesto: vive en el repo, se actualiza con frecuencia, y se desacopla deliberadamente del cuerpo del framework para que el framework no envejezca con cada release de Cedar o OPA.

No todo principio cultural es traducible a policy. Las restricciones operativas — cifras vetadas, dominios prohibidos, palabras clave, detección y redacción de categorías de datos sensibles — sí lo son. Los criterios de decisión finos — *"matizamos los argumentos comerciales que pueden leerse como exagerados"* — no lo son, y el manifiesto lo declara explícitamente: Federation no pretende automatizar la cultura completa, solo lo que es automatizable sin pérdida de fidelidad. El resto sigue siendo trabajo de modelado en cada agente, igual que en Adoption.

### 3.4 Capa de detección de drift cultural

A nivel federación, drift es cualquier patrón sistemático en el comportamiento agregado del sistema que no se deriva de la Constitución vigente. Esto es distinto del drift a nivel agente individual, que se detecta revisando outputs del agente concreto. El drift federado solo emerge cuando se mira el sistema entero.

Federation propone tres patrones operativos para detectarlo:

**Análisis de cadenas de decisiones.** Sobre el log de correlation ids, identificar cadenas que terminaron en outputs cuestionados internamente, externamente o por reguladores. Para cada cadena cuestionada, reconstruir qué criterios se aplicaron en qué punto y comparar contra lo que la Constitución dice que debería haberse aplicado. Si emergen patrones — el mismo tipo de cadena fallando consistentemente — hay drift.

**Análisis de excepciones.** Cuando una llamada inter-agente se bloquea por policy y la organización decide aprobarla manualmente, eso es una excepción. Las excepciones son legítimas (lo articulamos en Adoption §4) pero deben dejar rastro. Si las excepciones a la misma policy se acumulan sistemáticamente, no es la realidad la que está mal: es la policy la que ha quedado desfasada respecto a la cultura real, o la cultura real la que ha drifteado respecto a la Constitución declarada. Cuál de las dos es responsabilidad de la custodia decidir.

**Análisis de coherencia entre agentes.** Periódicamente, presentar el mismo escenario hipotético a varios agentes departamentales y comparar sus respuestas. Las incompatibilidades sistemáticas son síntoma de drift en alguna capa departamental respecto a la Constitución, o de drift en la propia Constitución que no se ha propagado bien.

Estos tres análisis son procesos, no productos. Federation no proporciona el dashboard que los muestra — eso lo proporcionan las herramientas de observabilidad del stack elegido. Lo que Federation aporta es la articulación de qué hay que medir, cómo, y con qué frecuencia.

## 4. Stack opensource: criterios, no marcas

El manifiesto se mantiene deliberadamente agnóstico al stack opensource concreto. Las decisiones de qué gateway, qué policy engine, qué service registry o qué pipeline de observabilidad usar son decisiones técnicas que dependen del entorno de la organización, su volumen de tráfico inter-agente, su exposición regulatoria y su stack pre-existente.

Lo que Federation declara son los **criterios funcionales que el stack elegido debe cubrir**:

- **Gateway MCP** que intermedie todas las llamadas inter-agente, soporte mTLS o equivalente, exponga puntos de extensión para policy enforcement, y propague metadatos arbitrarios en headers.
- **Service registry** federado que permita el descubrimiento de agentes con descriptores de capacidades extendidos (no solo nombre y endpoint, sino dominio, criticidad, versión de Constitución aplicada).
- **Policy engine** con lenguaje declarativo, latencia sub-milisegundo en evaluación, y capacidad de versionar políticas con auditoría de cambios.
- **Identity provider** que soporte identidades de servicio criptográficas y emisión de credenciales con TTL corto.
- **Observabilidad agent-aware**, idealmente OpenTelemetry, con capacidad de tracear cadenas de llamadas completas vía correlation id y exportar a backends estándar.
- **Des-identificación / DLP en la ruta**, capaz de detectar y redactar o tokenizar PII y PHI en los argumentos de las llamadas inter-agente antes de que alcancen el modelo, idealmente sobre un motor vendor-neutral (p. ej. Microsoft Presidio) para no acoplar la política de datos a un gateway concreto.

El apéndice del framework, mantenido como documento vivo separado, recoge stacks de referencia con sus pros y contras a fecha actual: combinaciones de Microsoft Agent Governance Toolkit, IBM ContextForge, Agentgateway, Lunar.dev MCPX, MCP Mesh, MCP Gateway Registry, OPA, Cedar, Casbin y similares. Varios de esos componentes — IBM ContextForge entre ellos — integran un plugin de des-identificación, típicamente sobre Microsoft Presidio, que cubre a la vez el criterio de gateway MCP y el de DLP en la ruta. Ese apéndice es responsabilidad de la comunidad, se actualiza conforme el ecosistema evoluciona, y se desacopla deliberadamente del manifiesto para que éste no envejezca con cada release.

## 5. Gobernanza federada

La gobernanza descrita en Adoption — custodia diferenciada por capa, revisión de coherencia, detección de drift, gestión de excepciones, proceso de retirada — sigue aplicando en Federation. Lo que cambia es que algunas piezas que en Adoption se ejecutan manualmente, aquí se ejecutan programáticamente.

**Custodia.** Igual que en Adoption: Marco Regulatorio en legal/DPO, Constitución Corporativa en transformación digital o equivalente, capas departamentales en cada departamento. Federation añade un cuarto custodio: la **plataforma de federación**, responsable del stack opensource subyacente, los policy templates corporativos transversales y la pipeline de observabilidad. Este custodio típicamente es el equipo de plataforma o de SRE, no el equipo de transformación.

**Revisión de coherencia.** En Adoption se hace en lectura cruzada antes de subir a producción. En Federation se complementa con verificación programática: los policy templates traducidos desde la Constitución se evalúan automáticamente contra los descriptores de capacidades de cada agente nuevo antes de que se registre en el service registry. Si un agente declara capacidades que entran en conflicto con la Constitución, la registración falla.

**Detección de drift.** En Adoption es revisión humana periódica. En Federation se ejecuta sobre los tres patrones del §3.4, con la frecuencia que la criticidad del dominio exija.

**Gestión de excepciones.** En Adoption es trabajo manual de la custodia. En Federation cada excepción aprobada manualmente queda registrada en el log de policy con justificación, alcance temporal y autorizador. El análisis periódico de excepciones (§3.4) es uno de los disparadores de revisión de la Constitución o de las policies derivadas.

**Proceso de retirada.** En Adoption es marcar como deprecated y desmaterializar manualmente. En Federation, retirar un agente significa: deregistrarlo del service registry, revocar sus credenciales, archivar su histórico de capacidades y cadenas de decisión, y notificar a otros agentes que dependían de él. Sin este proceso, las organizaciones acumulan agentes zombi que el sistema sigue invocando años después de que el departamento que los modeló haya desaparecido.

## 6. Adopción

Federation se adopta por fases. Cada fase deja la organización en un estado defendible aunque la siguiente no llegue.

**Fase 0 — Verificación de prerrequisitos.** Federation no tiene sentido si Adoption no está madura. Antes de plantearse Federation, la organización debe tener al menos tres capas departamentales vivas en producción, una Constitución Corporativa estable durante al menos seis meses, gobernanza formal de las tres capas, y experiencia documentada de fricción real en handovers manuales que justifica la inversión. Si alguno de estos prerrequisitos falta, Federation va a generar más coste que valor.

**Fase 1 — Selección de stack y prueba de concepto.** El equipo de plataforma evalúa los stacks opensource disponibles según los criterios del §4 y selecciona el que mejor encaje con la infraestructura existente. Sobre ese stack se monta una prueba de concepto con dos agentes departamentales — los dos cuya colaboración manual genera más fricción — propagando contexto cultural en sus llamadas. Duración típica: cuatro a ocho semanas, dependiendo del stack y del equipo.

**Fase 2 — Mapping de la Constitución a policy templates.** En paralelo a la prueba de concepto, transformación digital y plataforma colaboran para traducir los principios automatizables de la Constitución Corporativa a policy templates ejecutables sobre el policy engine elegido. No se pretende cubrir el 100% de la Constitución — solo la parte automatizable sin pérdida de fidelidad. Duración típica: dos a cuatro semanas para una Constitución bien articulada.

**Fase 3 — Migración del primer corredor real.** Cuando la prueba de concepto demuestra que la propagación de contexto y el policy enforcement funcionan, los dos agentes piloto se migran a producción reemplazando los handovers manuales que existían entre ellos. Aquí emerge la primera realidad operativa: latencia, errores, casos límite no anticipados. La duración depende mucho del dominio.

**Fase 4 — Federación progresiva del resto.** Con la lección aprendida del primer corredor, los siguientes agentes departamentales se federan progresivamente, no en bloque. Cada nuevo agente que entra en la federación pasa por verificación de coherencia programática (§5) antes de registrarse en el service registry. Es habitual que en esta fase emerjan revisiones a la Constitución o a las policies derivadas, porque la realidad operativa estresa los principios articulados sobre papel.

**Fase 5 — Madurez y observabilidad de drift.** A los seis o doce meses con federación parcial en producción, los tres patrones de detección de drift (§3.4) se ejecutan por primera vez con datos suficientes. Las primeras revisiones suelen producir ajustes significativos a las policies y, ocasionalmente, a la Constitución misma. Esa actualización de la Constitución debe propagarse al ecosistema Adoption — recordatorio explícito de que las dos fases son del mismo ecosistema, no frameworks paralelos.

## 7. Cómo saber si funciona

Federation hereda de Adoption las cuatro métricas que importan — reconocibilidad, coherencia transversal, tasa de escalado adecuada, trazabilidad de criterio — y añade dos métricas técnicas propias.

**Reducción de fricción en handovers.** Antes de Federation, cada handover entre dominios consumía tiempo humano de bisagra. Después, esa fricción se ha reducido o eliminado. La métrica concreta es tiempo medio de resolución de casos que cruzan más de un dominio, comparado contra una baseline pre-federación. Si Federation no reduce esta métrica de forma observable, la inversión no se justifica.

**Tasa de bloqueo y excepción.** El policy engine bloquea llamadas que violan policies derivadas de la Constitución. Esa tasa de bloqueo, descompuesta por agente origen, agente destino y policy violada, es información operativa de primer orden. Si la tasa es muy baja, las policies son demasiado permisivas o la cultura no se está aplicando. Si es muy alta, las policies son demasiado estrictas y van a generar excepciones manuales sistemáticas que socavan el sistema. El rango sano depende del dominio, pero la métrica debe vigilarse.

Las cuatro métricas heredadas de Adoption se pueden ahora medir con rigor que antes no era posible. La métrica de tasa de escalado adecuada — declarada como métrica difícil en Adoption §7 — aquí es trivial: cada escalado a humano queda registrado con su contexto completo y se puede analizar cuántos eran apropiados y cuántos no. Eso es exactamente uno de los argumentos para graduarse a Federation.

## 8. Lo que esta fase no es

**No es una alternativa a Adoption.** Si la organización no ha hecho el trabajo cultural de Adoption, Federation no lo va a sustituir. Va a federar agentes sin Constitución común y a producir un sistema más rápido en hacer mal lo que ya hacía mal antes.

**No es un gateway nuevo.** El ecosistema opensource ya tiene gateways MCP serios. Reimplementar uno sería derroche y, peor, condenaría al framework a competir con Microsoft, IBM y compañía en su propio terreno.

**No automatiza la Constitución completa.** Solo la parte automatizable sin pérdida de fidelidad — restricciones operativas concretas, principios traducibles a reglas booleanas. El resto sigue siendo trabajo de modelado en cada agente, igual que en Adoption.

**No reemplaza el modelado departamental.** Cada agente sigue siendo modelado por su departamento. Federation aporta la capa de coordinación e interoperabilidad, no el contenido cultural de cada agente.

**No es un protocolo nuevo.** MCP es el protocolo. Federation se monta sobre MCP usando los mecanismos que el protocolo ya provee — headers, metadata, descriptors — sin requerir extensiones del estándar. Si MCP evoluciona, Federation se adapta.

**No es prescriptiva en stack.** Como se declaró en §4, los criterios funcionales son obligatorios; la elección de stack concreto, no.

## 9. Objeciones anticipadas

**Microsoft Agent Governance Toolkit ya cubre esto. ¿Qué aporta Federation?**

AGT cubre policy enforcement, identity zero-trust, sandboxing y SRE para agentes autónomos sobre múltiples frameworks. Es excelente en lo que hace y Federation se apoya en él como uno de los stacks de referencia recomendados. Lo que AGT no cubre — porque no es su problema — es el puente entre la Constitución Corporativa de la organización y los policy templates que el toolkit ejecuta. Esa traducción es responsabilidad de la organización; AGT proporciona el motor, no las reglas. Federation aporta el método para escribir esas reglas con coherencia cultural y propagar contexto cultural en cada llamada, que es donde AGT — deliberadamente — no opina. La relación es complementaria, no competitiva.

**¿Por qué MCP y no A2A o un protocolo propietario?**

MCP es el estándar de facto para integración de tools y agentes que han adoptado Anthropic, OpenAI, Google y Microsoft, y sobre el que ya hay un ecosistema opensource maduro. A2A cubre comunicación inter-agente con énfasis distinto y muchos gateways modernos lo soportan en paralelo. Federation se construye sobre MCP por pragmatismo — donde está la masa crítica del ecosistema — pero los principios del manifiesto (propagación de contexto cultural, mapping de Constitución a policy, detección de drift) son aplicables sobre cualquier protocolo de comunicación inter-agente. Si A2A se vuelve dominante en el futuro, Federation portará a A2A los mismos principios sin reescribirse.

**¿Cómo escala el policy engine cuando hay muchos agentes y mucho tráfico?**

Los policy engines opensource recomendados — Cedar, OPA, los integrados en AGT — están diseñados para evaluación sub-milisegundo y throughput de decenas de miles de evaluaciones por segundo. La latencia agregada introducida por la capa de gobernanza es típicamente del orden de unos pocos milisegundos por hop, dominada por la verificación criptográfica de identidad, no por la evaluación de policy. Para las organizaciones donde Federation tiene sentido — agentes departamentales que se invocan decenas o cientos de veces por hora, no millones — esto está muy lejos de ser un problema técnico. El cuello de botella habitual es humano (gestión de excepciones, revisión de drift), no técnico.

**¿Qué pasa con la latencia de la propagación de contexto cultural?**

El bloque de metadatos cultural que viaja en cada llamada es de orden de cientos de bytes a unos pocos kilobytes — hashes, identificadores, cadena de decisiones. La sobrecarga de transporte es despreciable. La sobrecarga real es la verificación, en el agente receptor, de que la versión de Constitución del emisor es compatible con la suya — una comparación de hashes y, en el caso de incompatibilidad, una decisión de escalado. Esto añade microsegundos en el caso normal y bloquea (correctamente) en el caso de incompatibilidad real.

**¿Cómo se reconcilia Federation con la observabilidad existente de la organización?**

OpenTelemetry es el estándar y todos los stacks opensource recomendados lo soportan nativamente. Las cadenas de llamadas inter-agente se trazan con correlation ids estándar, los bloques de metadatos cultural se exportan como atributos del span, y los backends de observabilidad existentes (Datadog, Honeycomb, Grafana, Jaeger) los ingesta sin modificación. Lo que sí requiere trabajo es enriquecer los dashboards existentes con vistas agent-aware — pero ese trabajo lo hace el equipo de plataforma una sola vez al adoptar el stack, no en cada incorporación de agente.

**Federation parece útil solo para organizaciones grandes con muchos agentes. ¿Y los demás?**

Cierto, y conviene declararlo. Federation tiene sentido cuando la organización tiene al menos cinco o seis agentes departamentales activos y al menos tres pares que colaboran con frecuencia significativa (varias veces al día). Por debajo de ese umbral, los patrones manuales de Adoption §5 son suficientes y la sobrecarga operativa de Federation no se justifica. El framework es honesto sobre esto: no es para todo el mundo ni se vende como horizonte aspiracional para organizaciones que no llegarán nunca al volumen que lo justifica.

## 10. Horizonte opensource

Federation se publica como opensource bajo licencia MIT, igual que el resto del ecosistema Myrmion. La razón estratégica es la misma: el problema es estructural y compartido, resolverlo en abierto acelera la madurez del ecosistema, y un framework abierto evoluciona con el campo de forma que ninguno cerrado puede.

Las contribuciones más valiosas serán de tres tipos: actualizaciones del apéndice de stacks de referencia conforme los proyectos opensource subyacentes evolucionan; catálogos de policy templates derivables de Constituciones Corporativas reales, anonimizados, para acelerar la curva de aprendizaje del mapping; y patrones de detección de drift específicos de sectores regulados (sanidad, financiero, sector público) donde la criticidad justifica análisis más finos que los del §3.4.

Federation se diseña explícitamente para no envejecer con el ecosistema sobre el que se monta. Si Microsoft AGT, ContextForge, Agentgateway o cualquier otro proyecto evoluciona, se fusiona o desaparece, Federation se adapta sin reescribirse — porque el manifiesto opina sobre criterios funcionales y método, no sobre marcas. Esa portabilidad es deliberada y es la principal protección contra el riesgo de que un actor grande absorba el espacio: el manifiesto sigue siendo válido aunque el stack debajo cambie completamente.

La frontera con **Myrmion Adoption**, la fase del ecosistema que articula el modelado cultural sin programaticidad, se mantiene explícita y bidireccional. Las organizaciones que vienen desde Adoption traen consigo la Constitución Corporativa que aquí se materializa programáticamente. Las que en algún momento dejan de necesitar Federation — porque reducen alcance, simplifican operación o reorganizan dominios — pueden volver a Adoption sin tirar el trabajo. Las dos fases son del mismo ecosistema porque el problema cultural y el técnico son del mismo problema, separados solo por la fase de madurez en que la organización se encuentra.

Empiezas por la colonia. Evolucionas a la falange cuando tu organización lo necesita. Vuelves a la colonia si la falange deja de tener sentido. La cultura, la Constitución y el método persisten. Lo que cambia es el grado de programaticidad.

---

*Manifiesto de Myrmion Federation — versión 1.0.*
