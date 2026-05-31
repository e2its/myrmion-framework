# ADR-0001 — Selección de stack de federación para Consultora Modelo S.L.

> **Ejemplo ilustrativo.** Este ADR no es una decisión vinculante del framework: es una *instancia* de adopción para la organización ficticia **Consultora Modelo S.L.**, escrita para mostrar cómo se rellena la [plantilla de ADR](./0000-plantilla-adr.md) y cómo se evalúa un stack contra los [criterios funcionales](../criterios-funcionales.md). Por eso nombra productos concretos: un ADR de adopción **sí** puede hacerlo, porque documenta una decisión real de una organización, no el cuerpo agnóstico del framework (ver [regla anti-acoplamiento](../regla-anti-acoplamiento.md)). No tomes las marcas aquí elegidas como recomendación de Federation: la recomendación de Federation son los seis CF, no este stack. Numeramos `0001` por convención del ejemplo; en una organización real, un ADR de selección de stack es una decisión de adopción y vivirá en el rango `0100+` (ver [README de los ADR](./README.md), «Numeración»).

| Campo | Valor |
|---|---|
| ADR | 0001 |
| Ámbito | Adopción — *ejemplo ilustrativo (en el repo real iría a rango 0100+; aquí se numera 0001 por didáctica)* |
| Estado | Aceptado |
| Fecha | 2026-05-30 |
| Supera a | — |
| Superado por | — |

---

## Contexto

Consultora Modelo S.L. terminó la Fase 0 del [manifiesto §6](../manifesto.md): tiene cinco capas departamentales vivas en producción (Comercial, Legal, Finanzas, Marketing y Operaciones), una Constitución Corporativa estable desde hace nueve meses y gobernanza formal de las tres capas. La fricción documentada que justifica la inversión es el corredor **Comercial → Legal**: cada propuesta que el agente comercial de Fonseca quiere cerrar tiene que pasar por una revisión que hoy la persona de Riera, en Legal, hace a mano sobre el output del comercial. Es el handover que más tiempo de bisagra consume y el que la organización elige para su primer corredor (manifiesto §6, Fase 1 y Fase 3).

La decisión sobre la mesa es **qué stack opensource concreto** monta la federación. El manifiesto (§4) es deliberadamente agnóstico y delega esta elección en el equipo de plataforma, que debe evaluar cada candidato contra las checklists de los [criterios funcionales CF-01..CF-06](../criterios-funcionales.md) y registrar el resultado como ADR (criterios funcionales, «Cómo usar este documento», punto 1).

Las fuerzas en juego para Consultora Modelo S.L.:

- **Infraestructura preexistente.** La organización ya opera un clúster con malla de servicios y exporta telemetría sobre un estándar abierto. No parte de cero: la decisión debe minimizar lo que hay que introducir.
- **Exposición regulatoria.** El corredor Comercial → Legal mueve datos personales de clientes (leads, contactos de la propuesta). El [criterio CF-06](../criterios-funcionales.md) (des-identificación / DLP en la ruta) no es opcional para esta organización: es el control que cierra el hueco de enforcement que Adoption no podía cubrir.
- **Volumen.** Decenas a cientos de invocaciones inter-agente por hora, no millones (manifiesto §9). La latencia no es la restricción dominante; la cobertura de los seis criterios y el coste operativo de mantener el stack, sí.
- **No reimplementar.** El principio de compositividad (manifiesto §2) prohíbe que la organización construya su propio gateway o su propio motor de policy. Todo lo que se elija debe ser un componente opensource mantenido.

Este ADR es el «antes»: enuncia el problema de selección. La matriz de cobertura de los candidatos vive en el apéndice ([`appendix/stacks-referencia/`](../appendix/stacks-referencia/)); aquí se decide, no se cataloga.

---

## Decisión

Consultora Modelo S.L. adopta el siguiente stack para cubrir los seis criterios funcionales:

| Criterio | Componente elegido | Ficha de referencia |
|---|---|---|
| **CF-01** Gateway de llamadas inter-agente | IBM ContextForge (MCP Gateway) | [`ibm-contextforge.md`](../appendix/stacks-referencia/ibm-contextforge.md) |
| **CF-02** Service registry federado | El registry integrado en ContextForge | [`ibm-contextforge.md`](../appendix/stacks-referencia/ibm-contextforge.md) |
| **CF-03** Policy engine | OPA / Rego | [`policy-opa.md`](../appendix/stacks-referencia/policy-opa.md) |
| **CF-04** Identity provider | Autenticación mutua con identidad criptográfica verificable terminada en ContextForge | [`ibm-contextforge.md`](../appendix/stacks-referencia/ibm-contextforge.md) |
| **CF-05** Observabilidad agent-aware | El emisor de telemetría de ContextForge sobre el backend abierto ya existente | [`ibm-contextforge.md`](../appendix/stacks-referencia/ibm-contextforge.md) |
| **CF-06** Des-identificación / DLP en la ruta | El plugin de des-identificación integrado en ContextForge (sobre motor vendor-neutral) | [`ibm-contextforge.md`](../appendix/stacks-referencia/ibm-contextforge.md) |

La razón de fondo de esta combinación es que **un único componente de gateway cubre cinco de los seis criterios** (CF-01, CF-02, CF-04, CF-05 y CF-06), lo que reduce el número de piezas que la organización tiene que operar. ContextForge intermedia todas las llamadas inter-agente sobre MCP sin extender el protocolo, lleva service registry integrado, termina la autenticación mutua con identidad criptográfica, exporta telemetría sobre el estándar abierto que la organización ya usa, e integra de fábrica un plugin de des-identificación basado en un motor vendor-neutral (lo que el [manifiesto §4](../manifesto.md) describe como el componente que «cubre a la vez el criterio de gateway MCP y el de DLP en la ruta»). Sobre ese gateway se engancha un único componente especializado: **OPA** como policy engine, en el punto de extensión que el gateway expone antes de ejecutar la llamada.

La elección entre OPA y Cedar para CF-03 se resuelve a favor de OPA por encaje con la infraestructura preexistente (la organización ya despliega OPA como sidecar en su malla para otras decisiones de autorización); la elección no es normativa y se revisará si esa premisa cambia (ver Riesgos).

---

## Cómo cada criterio queda cubierto

La evaluación contra las checklists de [criterios-funcionales.md](../criterios-funcionales.md):

- **CF-01 — Gateway.** ContextForge intermedia toda llamada inter-agente, expone un punto de extensión donde se inserta la evaluación de OPA **antes** de ejecutar la tool, y propaga metadatos arbitrarios sin truncarlos — el transporte del bloque de contexto cultural (§3.2). No requiere extensiones de MCP. Ver [`ibm-contextforge.md`](../appendix/stacks-referencia/ibm-contextforge.md).
- **CF-02 — Service registry.** El registry integrado almacena el [descriptor de identidad extendido](../esquema-identidad-agente.md) (dominio, criticidad, clases de dato, versión de Constitución aplicada) y permite condicionar el alta al gate de coherencia. El ciclo de vida completo (alta, actualización, deprecated, baja sin liberar el `agentId`) está cubierto.
- **CF-03 — Policy engine.** OPA evalúa Rego declarativo en sub-milisegundo, versiona policies con auditoría de cambios y puede expresar las decisiones `allow` / `deny` / `redact` / `require-prior-hop` consultando campos del descriptor y del bloque de contexto cultural. Ver [`policy-opa.md`](../appendix/stacks-referencia/policy-opa.md). El policy template del corredor — *«no se cierra una propuesta comercial sin un hop previo por Legal con resultado positivo»* — se materializa como una regla `require-prior-hop` que inspecciona `decisionChain`.
- **CF-04 — Identity provider.** ContextForge termina la autenticación mutua con identidad criptográfica: el receptor verifica la identidad del emisor **antes** de ejecutar la llamada, la credencial es de vida corta y revocable, y la identidad es vinculable de forma estable al `agentId`. Estas son las tres propiedades que el cuerpo entiende por «autenticación mutua con identidad criptográfica verificable» (CF-04); nunca se exige «mTLS» por su nombre. Ver [`ibm-contextforge.md`](../appendix/stacks-referencia/ibm-contextforge.md).
- **CF-05 — Observabilidad agent-aware.** ContextForge exporta trazas correlacionadas por `correlationId` sobre un estándar abierto de telemetría hacia el backend que la organización ya tiene, con los metadatos del bloque de contexto cultural como atributos del span. Eso habilita las tres consultas de los patrones de drift (por cadena, por excepción acumulada, por coherencia entre agentes).
- **CF-06 — Des-identificación / DLP en la ruta.** El plugin de des-identificación integrado en ContextForge (sobre un motor de detección vendor-neutral) detecta PII de cliente en los argumentos de la llamada Comercial → Legal y la tokeniza **antes** de que alcance el modelo. Como la redacción del corredor es reversible, emite `deidToken` que el bloque de contexto cultural transporta para re-identificar la respuesta **solo en el agente de origen** (Comercial). Ver [`ibm-contextforge.md`](../appendix/stacks-referencia/ibm-contextforge.md) y [esquema-bloque-contexto-cultural.md](../esquema-bloque-contexto-cultural.md).

Los seis criterios quedan **cubiertos**. No hay puntos de checklist sin cubrir, por lo que este ADR no asume huecos ni controles compensatorios.

---

## Alternativas consideradas

- **Agentgateway como gateway (CF-01) en lugar de ContextForge** — un gateway MCP-nativo, serio y de alto rendimiento. Descartada para Consultora Modelo S.L. porque **no integra de fábrica des-identificación**: su ficha lo marca explícitamente como no cubierto para CF-06. Cubrir CF-06 con Agentgateway exigiría desplegar y operar un componente de DLP aparte, añadiendo piezas. ContextForge cubre CF-01 y CF-06 con un solo componente, que es la prioridad de esta organización dada su exposición regulatoria. Agentgateway sigue siendo un candidato perfectamente válido para organizaciones con otro perfil. Ver [`agentgateway.md`](../appendix/stacks-referencia/agentgateway.md).
- **Cedar como policy engine (CF-03) en lugar de OPA** — lenguaje de policy declarativo con análisis y latencia excelentes. Descartada **solo** por encaje operativo: la organización ya opera OPA en su malla para otras decisiones de autorización, y añadir un segundo dialecto de policy duplicaría la superficie de mantenimiento. La decisión es de coste operativo, no de capacidad: Cedar cubre CF-03 igual de bien. Ver [`policy-cedar.md`](../appendix/stacks-referencia/policy-cedar.md).
- **DLP en cada agente en lugar de en la ruta (CF-06)** — confiar la des-identificación a cada agente departamental. Descartada porque viola el principio del criterio: si la redacción depende de la buena voluntad de cada agente, deja de ser enforcement. La ruta inter-agente **es** el punto de inserción que Adoption no tenía; renunciar a él sería renunciar al criterio que cierra ese hueco.
- **Identidad por secretos compartidos estáticos en lugar de identidad criptográfica (CF-04)** — credenciales estáticas por agente. Descartada de plano: CF-04 exige identidades criptográficas con credenciales de vida corta y revocables, no secretos compartidos estáticos.

---

## Encaje con los tres principios

Toda decisión que da forma a la federación debe rendir cuentas ante los tres principios del [manifiesto §2](../manifesto.md).

### Compositividad sobre infraestructura existente

*Pregunta guía: ¿esta decisión se monta sobre lo que el stack ya provee (criterios funcionales CF-01..CF-06), o introduce algo que Federation tendría que reimplementar, una extensión de protocolo o un acoplamiento a un stack concreto?*

**Refuerza.** Todos los componentes elegidos son opensource mantenidos; la organización no reimplementa nada. El gateway se monta sobre MCP usando los mecanismos que el protocolo ya provee (metadata, headers), sin extensiones. La elección de OPA aprovecha infraestructura que ya estaba desplegada, reduciendo lo que hay que introducir. El acoplamiento que esta decisión introduce es real pero está deliberadamente confinado: vive en este ADR de adopción y en el apéndice, nunca en el cuerpo del framework. Si mañana ContextForge dejara de mantenerse, la migración cambia este ADR, no la Constitución ni los seis CF.

### Cultura propagable

*Pregunta guía: ¿esta decisión preserva que el contexto cultural viaje íntegro en cada llamada inter-agente (bloque de contexto cultural), o crea un camino por el que la versión de Constitución, los criterios aplicados o la cadena de decisiones puedan perderse o quedar atrás?*

**Respeta.** El gateway elegido propaga metadatos arbitrarios sin truncarlos (CF-01), que es precisamente lo que el bloque de contexto cultural necesita como transporte. El `correlationId` persiste a lo largo de toda la cadena Comercial → Legal y, cuando la redacción de CF-06 es reversible, los `deidToken` viajan en el propio bloque para re-identificar la respuesta solo en origen. Ningún componente del stack reinterpreta ni descarta el bloque: el contrato del [esquema del bloque](../esquema-bloque-contexto-cultural.md) se transporta íntegro.

### Drift como métrica de primera clase

*Pregunta guía: ¿esta decisión mantiene el drift federado medible y vigilable por los patrones del manifiesto §3.4, o introduce una desviación cultural que dejaría de ser observable?*

**Respeta.** La observabilidad (CF-05) sobre un estándar abierto de telemetría y `correlationId` habilita las tres consultas que los patrones de drift necesitan: análisis de cadenas de decisiones, análisis de excepciones acumuladas y análisis de coherencia entre agentes. Cada excepción a una policy (p. ej. cerrar una propuesta sin el hop por Legal) queda registrada en el log de OPA con justificación, alcance y autorizador, alimentando el análisis de excepciones del §3.4. El stack no introduce ningún punto ciego que dejara el drift fuera de observación.

---

## Consecuencias

**Positivas**

- Un solo componente de gateway cubre cinco criterios (CF-01, CF-02, CF-04, CF-05, CF-06), minimizando las piezas a operar.
- CF-06 queda cubierto de fábrica por el plugin de des-identificación del gateway, sin desplegar DLP como componente separado.
- La elección de OPA reutiliza infraestructura ya desplegada, reduciendo coste de incorporación.
- Los seis criterios quedan cubiertos sin huecos, por lo que no se asumen controles compensatorios.

**Negativas o costes**

- La concentración de cinco criterios en un único componente crea una dependencia fuerte de ese gateway: su salud operativa y su continuidad como proyecto opensource pasan a ser un punto de atención de primer orden.
- La organización queda atada al ciclo de releases de un único proyecto para la mayor parte de su superficie de federación.

**Neutras (efectos a vigilar)**

- Mantener un único dialecto de policy (Rego) es bueno para el coste operativo hoy, pero ata el catálogo de mapping a OPA; conviene vigilar que las convenciones de mapping del catálogo sigan siendo neutrales al dialecto (no se «filtra» Rego al cuerpo).
- La latencia agregada por hop está dominada por la verificación de identidad (manifiesto §9); conviene medirla en el primer corredor real (Fase 3) para confirmar que se mantiene en el rango esperado.

---

## Riesgos

- **Concentración en el gateway** — cinco criterios dependen de un solo componente. Señal de alerta: ralentización del proyecto upstream, vulnerabilidades sin parchear, o un criterio que el gateway deje de cubrir tras una release. Mitigación: seguimiento del proyecto en el apéndice; los seis CF son la frontera de portabilidad, así que una migración a otro gateway (p. ej. Agentgateway con un componente de DLP separado) cambia este ADR sin tocar la Constitución ni el cuerpo. Esa migración dispararía un ADR sucesor.
- **Acoplamiento del catálogo a Rego** — el catálogo de mapping podría empezar a escribirse pensando en OPA. Señal de alerta: convenciones de mapping que no se pueden expresar en otro dialecto. Mitigación: mantener el catálogo del cuerpo neutral y las implementaciones por dialecto en `appendix/policy-templates/`.
- **Premisa de infraestructura preexistente** — la elección de OPA sobre Cedar se apoya en que la organización ya opera OPA. Señal de alerta: la organización deprecia OPA en el resto de su malla. Mitigación: si la premisa cae, reevaluar CF-03 (Cedar vuelve a estar sobre la mesa) en un ADR sucesor.

---

## Estado

**Aceptado** — stack seleccionado para la prueba de concepto del corredor Comercial → Legal (manifiesto §6, Fase 1). La validación operativa real llega en la Fase 3 (migración del primer corredor); si esa fase revela que algún criterio no se sostiene en producción, este ADR se superará con uno sucesor.

---

## Relacionados

- [README de los ADR](./README.md)
- [Plantilla de ADR](./0000-plantilla-adr.md) — de la que deriva este ejemplo.
- [Manifiesto](../manifesto.md) — los tres principios (§2), criterios no marcas (§4), fases de adopción (§6).
- [Criterios funcionales](../criterios-funcionales.md) — CF-01..CF-06, evaluados en este ADR.
- [Regla anti-acoplamiento](../regla-anti-acoplamiento.md) — por qué un ADR de adopción sí puede nombrar productos y el cuerpo no.
- [Esquema de identidad de agente](../esquema-identidad-agente.md) — el descriptor que CF-02 almacena.
- [Esquema del bloque de contexto cultural](../esquema-bloque-contexto-cultural.md) — lo que CF-01 transporta y CF-06 enriquece con `deidToken`.
- Fichas de stack citadas: [`ibm-contextforge.md`](../appendix/stacks-referencia/ibm-contextforge.md), [`policy-opa.md`](../appendix/stacks-referencia/policy-opa.md), [`policy-cedar.md`](../appendix/stacks-referencia/policy-cedar.md), [`agentgateway.md`](../appendix/stacks-referencia/agentgateway.md). Apéndice vivo y matriz de cobertura: [`appendix/README.md`](../appendix/README.md).

---

*Myrmion Federation — ADR-0001 (ejemplo ilustrativo de selección de stack), versión 1.0. Ejemplo de adopción, no decisión vinculante del framework.*
