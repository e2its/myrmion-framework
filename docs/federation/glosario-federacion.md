# Myrmion Federation — Glosario

**Versión 1.0**

*Vocabulario normativo del corpus de Federation. Cuando un término aparece en cursiva en otro documento del cuerpo, su definición canónica está aquí. Si un término se usa de forma incompatible con esta definición, el error está en el otro documento, no en el glosario.*

---

## Cómo usar este glosario

Este documento fija el significado exacto de los términos que el resto del corpus de Federation da por sabidos. No repite las definiciones del [manifiesto](./manifesto.md) — las precisa para que sean operables. Los términos que pertenecen a Adoption (Constitución Corporativa, Marco Regulatorio, Capa Departamental, drift cultural a nivel agente) se definen en el [manifiesto de Adoption](../adoption/manifesto.md) y aquí solo se referencian.

El glosario es **normativo**: las plantillas, los esquemas y los ejemplos usan estos términos con este significado. Cualquier discrepancia se resuelve a favor del glosario.

---

## 1. Términos de federación

**Federación.** El conjunto de agentes departamentales de una organización que se invocan mutuamente bajo una capa de gobernanza común, sobre un stack que cumple los [criterios funcionales](./criterios-funcionales.md). No es un producto ni un cluster: es la propiedad de que los agentes coordinan con disciplina cultural verificable. Una organización «tiene federación» cuando al menos dos agentes se invocan sin intermediación humana propagando contexto cultural.

**Agente departamental.** La materialización programática de una Capa Departamental de Adoption como servidor invocable. En Federation, cada agente expone un *descriptor de identidad* y se registra en el *service registry*. Hereda, por construcción, de la Constitución Corporativa y del Marco Regulatorio. No confundir con «asistente»: en Adoption el asistente vive dentro de un producto comercial; en Federation el agente es un servicio con identidad criptográfica propia.

**Corredor (corridor).** El traspaso recurrente entre dos agentes departamentales (origen→destino) que hoy se hace a mano —una persona resume el output de uno y se lo entrega al otro (*handover*)— y que Federation sustituye por invocación gobernada. Ejemplo: el corredor comercial→legal, donde cada *lead* que califica Comercial pasa por Legal para validar una cláusula antes de cerrar (ver el [ejemplo end-to-end](../../examples/federation/corredor-comercial-legal/)). *El término se usa en el sentido de **corredor de tránsito** —una vía muy transitada que se pavimenta antes que las demás—, no de corredor de bolsa ni de atletismo.* El corredor es la **unidad de migración** (manifiesto §6, Fase 3): no se federa «la organización», se federa un corredor cada vez. Puede tener más de dos saltos cuando la cadena de decisión atraviesa varios dominios (p. ej. comercial→legal→finanzas).

**Salto (hop).** Una invocación inter-agente individual dentro de una cadena. `hopCount` cuenta los saltos acumulados en una cadena de decisión. La primera invocación de una cadena es `hopCount = 1`.

**Handover.** El traspaso manual de contexto entre dominios que Federation existe para eliminar — una persona toma el output de un agente, lo resume y lo entrega a otro como input. Definido en Adoption; aquí es la *baseline* contra la que se mide la reducción de fricción (manifiesto §7).

---

## 2. Identidad y descubrimiento

**Descriptor de identidad (agent descriptor).** El artefacto que declara quién es un agente, qué dominio cubre, qué criticidad tiene, qué clases de dato maneja y a qué versión de la Constitución se adhiere. Su contrato está en [esquema-identidad-agente.md](./esquema-identidad-agente.md). Es lo que permite que dos agentes se descubran y se entiendan sin coordinación humana previa.

**`agentId`.** Identificador estable y no reutilizable de un agente, en forma de URN (`urn:myrmion:agent:<org>:<dominio>:<nombre>`). No se reasigna nunca: cuando un agente se retira, su `agentId` queda archivado, no liberado. Es la clave a la que se vincula la identidad criptográfica.

**Service registry.** El catálogo federado donde los agentes se registran con su descriptor extendido (no solo nombre y endpoint, sino dominio, criticidad y versión de Constitución aplicada). El alta en el registry pasa por el *gate de coherencia*. Es responsabilidad del stack; Federation define qué debe poder almacenar y consultar, no cómo (ver [CF-02](./criterios-funcionales.md)).

**Identidad criptográfica.** La propiedad de que la identidad de un agente es verificable por medios criptográficos, con tres requisitos (CF-04): (1) el receptor verifica criptográficamente la identidad del emisor **antes de ejecutar** la llamada; (2) la credencial es de **vida corta y revocable**; (3) la identidad es **vinculable de forma estable al `agentId`**. El cuerpo nunca exige «mTLS»: exige estas tres propiedades, que mTLS u otros mecanismos satisfacen (ver [regla anti-acoplamiento](./regla-anti-acoplamiento.md), regla 4).

---

## 3. Contexto cultural

**Bloque de contexto cultural (cultural context block).** El conjunto de metadatos que viaja en cada llamada inter-agente junto a los argumentos de la tool, y que distingue una falange de un grupo de mercenarios. Su contrato está en [esquema-bloque-contexto-cultural.md](./esquema-bloque-contexto-cultural.md). Federation define el *esquema* del bloque; el *transporte* (cómo viaja por MCP u otro protocolo) vive en `appendix/mapeo-transporte/`.

**`correlationId`.** Identificador único que persiste a lo largo de toda una cadena de decisiones, desde el primer salto hasta el último. **Nunca se regenera** dentro de una cadena: es la clave con la que se reconstruye la cadena completa a posteriori. Es la pieza que hace trivial la trazabilidad que en Adoption requería trabajo forense.

**`businessCaseId`.** Identificador del caso de negocio que origina la cadena (el lead, el expediente, el ticket). Permite agrupar todas las cadenas de decisión que sirven a un mismo asunto.

**Cadena de decisiones (decision chain).** La secuencia ordenada de saltos que documenta, para cada uno, qué agente intervino, qué tool invocó, qué versión de Constitución aplicó, qué criterios aplicó y con qué resultado. Obligatoria cuando `hopCount > 1`. Cada eslabón es un *DecisionHop*.

**`criteriaApplied`.** En cada eslabón de la cadena, la lista de criterios que el agente aplicó, expresada como `policyId@version` (cuando el criterio es una policy automatizada) o como el literal `"juicio-de-modelo-no-automatizable"` (cuando el criterio es un juicio fino que Federation no pretende automatizar). Esta convención es la que hace analizable el *Patrón A* de detección de drift.

**Validación de compatibilidad.** La comprobación que hace el agente receptor: que la versión de Constitución que aplicó el emisor (`constitutionHash`) está entre las que él reconoce compatibles (`compatibleConstitutionHashes`). Si no hay match, la llamada **no procede**: se aplica `compatibilityPolicy` —valores `{escalar, rechazar}`, por defecto `escalar`— rellenando `escalationContext` y escalando a humano con el bloque completo como evidencia. La política puede endurecerse a `rechazar`, nunca relajarse a permitir.

**Token de des-identificación (`deidToken`).** Referencia opaca a un dato sensible **redactado de forma reversible** en la ruta. Nunca contiene el valor original: solo un puntero a un vault, un ámbito (`scope`) y un TTL (`ttl`). Solo existe cuando la redacción es reversible; cuando es irreversible **no hay token**, porque el dato se ha ido y no vuelve. Permite re-identificar la respuesta final **únicamente en el agente de origen**. En el bloque de contexto cultural estos tokens viajan en el campo `deidTokens` (array). Conecta con la capa técnica de la [Guía de protección de datos](../adoption/guia-proteccion-datos.md).

---

## 4. Policy y gobernanza

**Policy template.** Un patrón reutilizable que traduce un principio de la Constitución Corporativa a una regla evaluable por un policy engine. Federation define el *formato* y las *convenciones* del mapping ([convenciones-mapping-constitucion-policy.md](./convenciones-mapping-constitucion-policy.md)); el *catálogo poblado* con implementaciones por dialecto vive en `appendix/policy-templates/`.

**Clase de automatizabilidad (automatabilityClass).** La categoría de un principio cultural según cuánto se puede materializar en policy sin pérdida de fidelidad. Toma uno de tres valores literales: `duro` (regla booleana exacta), `blando` (umbral + defensa en profundidad) y `no-automatizable` (juicio fino que permanece como trabajo de modelado en el agente). No todo principio es traducible; declararlo explícitamente es parte del método (manifiesto §3.3, §8).

**Gate de coherencia.** La verificación programática que un agente nuevo debe pasar antes de registrarse en el service registry: sus capacidades declaradas se evalúan contra los policy templates derivados de la Constitución. Si declara capacidades que entran en conflicto con la Constitución, la registración **falla**. Es la versión programática de la revisión de coherencia de Adoption (manifiesto §5).

**Excepción.** Una llamada que el policy engine bloquea y que la organización decide aprobar manualmente. Las excepciones son legítimas pero **dejan rastro** en el [registro de excepciones](../../templates/federation/registro-excepciones.md): justificación, alcance temporal y autorizador. Una excepción al Marco Regulatorio no es una excepción: es una alerta (el Marco no admite excepciones, ver Adoption §4).

**Cuarto custodio (plataforma de federación).** El custodio que Federation añade a los tres de Adoption (Marco Regulatorio en legal/DPO, Constitución en transformación digital, capas departamentales en cada departamento). Responsable del stack, los policy templates transversales y la pipeline de observabilidad. Típicamente el equipo de plataforma o SRE. Su charter está en [charter-plataforma-federacion.md](../../templates/federation/charter-plataforma-federacion.md).

---

## 5. Drift federado

**Drift federado.** Cualquier patrón sistemático en el comportamiento agregado del sistema de agentes que no se deriva de la Constitución vigente. Es distinto del drift a nivel agente individual (Adoption): el drift federado solo emerge al mirar el sistema entero. Las métricas técnicas habituales (latencia, error rate) no lo capturan.

**Patrón A — análisis de cadenas de decisiones.** Detección de drift sobre el log de `correlationId`: identificar cadenas que terminaron en outputs cuestionados y comparar criterios aplicados contra los que la Constitución exigía.

**Patrón B — análisis de excepciones.** Detección de drift por acumulación: si las excepciones a la misma policy se acumulan, o la policy está desfasada o la cultura real ha drifteado respecto a la Constitución declarada.

**Patrón C — análisis de coherencia entre agentes.** Detección de drift presentando el mismo escenario hipotético a varios agentes y comparando respuestas; las incompatibilidades sistemáticas señalan drift en una capa departamental o en la propia Constitución.

Los tres patrones se desarrollan en [patrones-deteccion-drift.md](./patrones-deteccion-drift.md). Son procesos, no productos: Federation articula qué medir, cómo y con qué frecuencia; el dashboard lo aporta el stack.

---

## 6. Estructura del corpus

**Cuerpo (normativo).** Los documentos de `docs/federation/` y las plantillas de `templates/federation/`. Envejecen lento: opinan sobre criterios funcionales, esquemas, convenciones y método, no sobre marcas. Custodia: el equipo del framework.

**Apéndice (vivo).** El contenido de `appendix/`. Envejece rápido: stacks de referencia, implementaciones de policy por dialecto, recetas de drift sectoriales, mapeo de transporte por protocolo. Custodia: la comunidad. Es el único lugar del repo donde aparecen nombres de producto.

**Criterio funcional (CF).** Un requisito que el stack elegido debe cumplir, expresado como propiedad verificable sin nombrar producto. Los seis CF están en [criterios-funcionales.md](./criterios-funcionales.md) y son la espina dorsal del corpus.

**Test de pertenencia.** La regla que decide si una frase va al cuerpo o al apéndice: *¿sigue siendo verdadera tras cambiar el stack entero?* Si nombra un producto, una versión o un dialecto, va al apéndice. Definido en [regla-anti-acoplamiento.md](./regla-anti-acoplamiento.md).

---

*Glosario de Myrmion Federation — versión 1.0. Parte del corpus normativo. Términos heredados de [Myrmion Adoption](../adoption/manifesto.md) se definen allí.*
