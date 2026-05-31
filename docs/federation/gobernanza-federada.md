# Myrmion Federation — Gobernanza federada

**Versión 1.0**

*Materializa el §5 del [manifiesto](./manifesto.md). Parte de la gobernanza articulada en Adoption — custodia diferenciada, revisión de coherencia, detección de drift, gestión de excepciones, retirada — y especifica únicamente los **deltas** que Federation introduce cuando esas piezas, antes manuales, se ejecutan programáticamente.*

---

## Cómo usar este documento

La gobernanza de Federation no sustituye a la de Adoption: la hereda y la endurece. Todo lo que el manifiesto de [Myrmion Adoption](../adoption/manifesto.md) §4 dice sobre custodia diferenciada, revisión de coherencia, drift, excepciones y retirada **sigue vigente**. Este documento no lo repite — describe solo dónde Federation cambia algo, y por qué.

El cambio de fondo es uno y se enuncia en una frase: **lo que en Adoption era criterio humano aplicado en lectura cruzada, en Federation es comprobación reproducible aplicada en la ruta.** Eso introduce cuatro deltas que este documento detalla, una por sección (un quinto delta de gobernanza —la detección de drift— vive en su propio documento y se recoge en el resumen final):

1. Un **cuarto custodio** — la plataforma de federación (§1).
2. Un **gate de coherencia** programático en el alta al service registry (§2).
3. Una **gestión de excepciones** que deja rastro reproducible (§3).
4. Un **ciclo de vida y retirada** que se delega a runbooks operativos (§4).

Lo que este documento **no** hace: no define el stack (eso son los [criterios funcionales](./criterios-funcionales.md)), no define los esquemas (eso son los contratos de [identidad](./esquema-identidad-agente.md) y [bloque cultural](./esquema-bloque-contexto-cultural.md)), no define los patrones de drift (eso es [patrones-deteccion-drift.md](./patrones-deteccion-drift.md)), y no inventa marcas (eso lo prohíbe la [regla anti-acoplamiento](./regla-anti-acoplamiento.md)).

---

## 1. El cuarto custodio: la plataforma de federación

Adoption distribuye la custodia en tres responsables, diferenciados por capa:

- **Marco Regulatorio** → legal / DPO. No admite excepciones.
- **Constitución Corporativa** → transformación digital o equivalente.
- **Capas departamentales** → cada departamento, sobre su propio agente.

Federation añade un cuarto custodio que Adoption no necesitaba, porque Adoption no tenía stack: la **plataforma de federación**. Es la pieza que el resto de la gobernanza da por supuesta — sin ella, no hay ruta donde aplicar policy, ni registry donde correr el gate, ni telemetría donde medir drift. En el [descriptor de identidad](./esquema-identidad-agente.md) este custodio aparece como el campo `platformCustodian`, frente al `owner` (custodio de dominio).

**Qué custodia.** Tres cosas, ninguna de ellas cultural:

- **El stack que cumple los criterios funcionales** ([CF-01..CF-06](./criterios-funcionales.md)): gateway, service registry, policy engine, identity provider, observabilidad agent-aware y des-identificación en la ruta. La elección concreta es suya; la decisión se registra como ADR de adopción, no en el cuerpo.
- **Los policy templates transversales** — los que derivan de principios de la Constitución que aplican a *toda* la federación, no a un dominio (p. ej. la des-identificación de PII/PHI en cualquier ruta, o el veto a exteriorizar cifras financieras sin endorsement). El *formato* de esos templates es el de [convenciones-mapping-constitucion-policy.md](./convenciones-mapping-constitucion-policy.md); las implementaciones por dialecto viven en [`appendix/policy-templates/`](./appendix/policy-templates/).
- **La pipeline de observabilidad** que hace medibles la trazabilidad ([CF-05](./criterios-funcionales.md)) y los [patrones de drift](./patrones-deteccion-drift.md): correlación por `correlationId`, exportación del bloque cultural como atributos del span, y las tres consultas que los patrones A, B y C necesitan.

**Qué NO custodia.** No custodia cultura. La plataforma no decide qué dice la Constitución ni qué criterios aplica un dominio; *traduce* lo que el custodio de la Constitución decide a algo que el policy engine evalúa, y *opera* la maquinaria. La distinción importa: cuando un policy template y la Constitución discrepan, la autoridad es del custodio de la Constitución, no de la plataforma. La plataforma ejecuta el motor; no escribe las reglas culturales.

**Quién es.** Típicamente el equipo de plataforma o de SRE, no el de transformación digital. Es deliberado: la custodia del stack exige rotación de credenciales, gestión de incidentes y operación 24×7, competencias que viven en plataforma, no en el área que articula la cultura. Su mandato, fronteras y escalados se fijan en el [charter de la plataforma de federación](../../templates/federation/charter-plataforma-federacion.md).

### RACI mínimo de la federación

Solo las actividades donde Federation cambia algo respecto a Adoption. *R* = responsable de ejecutar, *A* = autoridad que rinde cuentas, *C* = consultado, *I* = informado.

| Actividad | Marco (legal/DPO) | Constitución (transf. digital) | Capa departamental | Plataforma (4.º custodio) |
|---|---|---|---|---|
| Definir el principio cultural a automatizar | C | **A/R** | C | I |
| Traducir el principio a policy template transversal | I | **A** | I | **R** |
| Operar el stack y la pipeline de observabilidad | I | I | I | **A/R** |
| Ejecutar el gate de coherencia en el alta (§2) | I | C | C | **A/R** |
| Aprobar una excepción a una policy de Constitución (§3) | I | **A** | **R** (la solicita) | C |
| Tratar un intento de excepción al Marco | **A/R** | I | I | I (genera la alerta) |
| Retirar un agente (§4) | I | C | **A** (lo decide) | **R** (lo ejecuta) |
| Ejecutar los patrones de drift (manifiesto §3.4) | C | **A** | C | **R** |

Tres lecturas de esta tabla que conviene declarar:

1. **La autoridad cultural no se delega a la plataforma.** Donde hay decisión cultural (qué principio, qué excepción, qué dice el drift), la *A* es del custodio de la Constitución o del Marco. La plataforma es *R* — ejecuta — pero no rinde cuentas de la cultura.
2. **El Marco no tiene fila de excepción.** Su única fila relacionada es «tratar un intento de excepción», y su autoridad es legal/DPO, porque para el Marco un intento de excepción **es un incidente** (§3).
3. **Retirar un agente lo decide el departamento, lo ejecuta la plataforma.** La decisión de jubilar una capacidad es cultural/organizativa; la mecánica de hacerlo sin romper la federación es operativa (§4).

---

## 2. El gate de coherencia

En Adoption, la revisión de coherencia se hace en lectura cruzada antes de subir a producción: una persona lee la capa departamental nueva contra la Constitución y el Marco y decide si encaja. Funciona porque el ritmo de alta es humano.

En Federation el ritmo deja de ser humano — un agente se da de alta, actualiza su descriptor, se da de baja — y la lectura cruzada manual no escala. El delta es el **gate de coherencia**: la revisión deja de ser un juicio y se convierte en un conjunto de **comprobaciones programáticas reproducibles** que se ejecutan en el alta al [service registry](./criterios-funcionales.md) ([CF-02](./criterios-funcionales.md)). No reemplaza la revisión humana de fondo cuando hace falta; reemplaza la verificación mecánica que el humano hacía a ojo y hacía mal a escala.

**El gate es bloqueante y atómico.** Si **cualquiera** de las comprobaciones falla, el alta **falla**: el agente no entra en la federación. No hay alta «con observaciones» ni alta parcial. Un agente que no pasa el gate no es invocable, porque la federación es exactamente la propiedad de que todo agente alcanzable cumple el contrato.

### 2.1 Las seis comprobaciones

El gate evalúa, en este orden, sobre el [descriptor de identidad](./esquema-identidad-agente.md) que el agente presenta y sobre el estado del stack en ese momento. Cada comprobación es una condición booleana; el alta procede solo si las seis devuelven verdadero.

1. **Descriptor válido contra el esquema.** El descriptor presentado valida contra el contrato de [esquema-identidad-agente.md](./esquema-identidad-agente.md): campos requeridos presentes, `agentId` con forma `urn:myrmion:agent:<org>:<dominio>:<nombre>` y no reutilizado, tipos correctos. *Falla si* el descriptor está incompleto, malformado o reusa un `agentId` archivado.

2. **`constitutionRef` vigente.** La versión de Constitución que el agente declara adherir (`constitutionRef`, con su `hash`) corresponde a una versión **publicada y vigente** según el custodio de la Constitución — no a un borrador, una versión retirada ni un hash desconocido. La comprobación usa el [contrato de hash](./esquema-identidad-agente.md#6-contrato-de-hash), no una comparación de cadenas de versión. *Falla si* el `hash` no resuelve a una versión vigente. Un agente que se adhiere a una Constitución que ya no existe es, por definición, un agente a la deriva.

3. **Las `capabilities` no declaran efectos que la Constitución prohíbe.** Cada `Capability` declarada se evalúa, por sus propiedades de gobernanza (`sideEffectClass`, `externalizes`, `canCommit`, `dataClassesTouched`), contra los policy templates transversales derivados de la Constitución. Si una capability declara un efecto que la Constitución veta de forma absoluta — p. ej. `externalizes: true` sobre cifras financieras sin paso por finanzas, o `canCommit: true` sin paso por legal — el conflicto es estructural y no se resuelve en runtime. *Falla si* alguna capability declara un efecto que ningún contexto haría admisible. Esta es la versión programática exacta de la frase del manifiesto §5: «si un agente declara capacidades que entran en conflicto con la Constitución, el alta falla».

4. **`dataClasses` coherentes con el Marco Regulatorio.** Las clases de dato que el agente declara manejar (`dataClasses`) son un subconjunto de las que el Marco Regulatorio (`regulatoryFrameworkRef`) permite a su dominio, y para cada clase sensible (PII/PHI y las que el Marco defina) las capabilities que la tocan (`dataClassesTouched`) tienen disponible la des-identificación en la ruta ([CF-06](./criterios-funcionales.md)). *Falla si* el agente declara manejar una clase de dato que el Marco no autoriza a su dominio, o una clase sensible sin cobertura de des-identificación. Una discrepancia aquí no es una excepción: es materia del Marco (§3).

5. **`mutualAuthVerified = true`.** La identidad criptográfica del agente está emitida y verificada según las propiedades de [CF-04](./criterios-funcionales.md): el receptor puede verificar criptográficamente la identidad del emisor antes de ejecutar, la credencial es de vida corta y revocable, y es vinculable de forma estable al `agentId`. El descriptor refleja este hecho con `mutualAuthVerified = true` (el `mutualAuthMechanism` concreto es campo libre y no se privilegia ninguno). *Falla si* la autenticación mutua con identidad criptográfica verificable no está establecida. El cuerpo nunca exige «mTLS» por su nombre — exige estas tres propiedades; ver [regla anti-acoplamiento](./regla-anti-acoplamiento.md) §3.

6. **`coherenceReview.status` reproducible.** El resultado del propio gate se sella en el descriptor como `coherenceReview` = `{status, reviewedAgainst, date}` — con el conjunto de policy templates aplicados y su versión en `reviewedAgainst`. El alta solo procede con `coherenceReview.status = aprobado` (el contrato lo exige: el alta falla si `status != aprobado`). La comprobación exige además que ese resultado sea **reproducible**: volver a ejecutar el gate sobre el mismo descriptor y el mismo estado de Constitución produce el mismo `status`. *Falla si* el resultado no es reproducible (p. ej. la evaluación depende de algo no versionado). La reproducibilidad es lo que convierte el gate en evidencia auditable y no en un sello opaco: cualquiera puede re-verificar por qué un agente entró.

> **Por qué seis y en este orden.** Las dos primeras validan el contrato del agente consigo mismo (esquema, Constitución que dice seguir). Las dos siguientes lo validan contra la cultura y la ley (qué hace, qué datos toca). La quinta valida que es quien dice ser. La sexta valida que la decisión es auditable. El orden es de barato a caro y de estructural a operativo: las validaciones que descartan un descriptor manifiestamente inválido corren antes que las que exigen consultar el estado del stack.

### 2.2 Cuándo corre el gate

El gate corre en el **alta** (`lifecycleStatus: propuesto → activo`) y en cada **actualización de descriptor** que toque `capabilities`, `dataClasses` o `constitutionRef` — exactamente los disparos que el [esquema de identidad](./esquema-identidad-agente.md) §8 declara. No corre en cada llamada: eso es trabajo del policy engine en la ruta, no del registry. La frontera es nítida: el gate decide **si un agente puede estar en la federación**; el policy engine decide **si una llamada concreta procede**. Un agente que pasó el gate puede aun así ver bloqueada una llamada por policy de runtime; son dos controles distintos en dos momentos distintos.

Cuando la Constitución se actualiza, los agentes cuyo `constitutionRef` queda obsoleto no se expulsan automáticamente, pero su próxima invocación cae en la *validación de compatibilidad* del [bloque cultural](./esquema-bloque-contexto-cultural.md) (comparación de `constitutionHash` contra `compatibleConstitutionHashes`) y, si no hay match, escala a humano. La re-ejecución del gate tras un cambio de Constitución es parte del runbook de propagación (§4). El detalle operativo del alta vive en el [runbook de onboarding de agente](../../templates/federation/runbook-onboarding-agente.md).

---

## 3. Gestión de excepciones

En Adoption, gestionar una excepción es trabajo manual de la custodia. En Federation el hecho de bloquear es automático — el policy engine bloquea en la ruta toda llamada que viola una policy derivada de la Constitución — y el delta está en lo que ocurre **después** del bloqueo.

**Toda excepción aprobada deja rastro.** Una *excepción* es una llamada que el policy engine bloqueó y que la organización decide aprobar manualmente. Las excepciones son legítimas — Adoption §4 ya lo articula — pero en Federation **no existe la excepción sin registro**. Cada excepción aprobada se anota en el [registro de excepciones](../../templates/federation/registro-excepciones.md) con, como mínimo: la policy violada y su versión (`policyId@version`), el agente origen y el destino (`agentId`), el `correlationId` de la cadena afectada, la **justificación**, el **alcance temporal** (toda excepción caduca; no hay excepción permanente) y el **autorizador**. Sin esos campos no hay aprobación: el rastro es la condición, no el subproducto.

Ese rastro no es burocracia: es la materia prima del **Patrón B** de detección de drift ([patrones-deteccion-drift.md](./patrones-deteccion-drift.md)). Si las excepciones a la misma policy se acumulan, una de dos: o la policy ha quedado desfasada respecto a la cultura real, o la cultura real ha drifteado respecto a la Constitución declarada. Cuál de las dos es responsabilidad del custodio de la Constitución decidir — pero solo puede decidirlo si las excepciones dejaron rastro analizable.

**La excepción al Marco Regulatorio no es una excepción: es una alerta.** Esta es la frontera dura de la gobernanza, y Federation la hace explícita en la ruta. El Marco Regulatorio no admite excepciones (Adoption §4; ver también la incompatibilidad **siempre dura** de `regulatoryFrameworkRef` en el [esquema de identidad](./esquema-identidad-agente.md) §7). Por tanto, un intento de aprobar manualmente una llamada bloqueada por una policy derivada del **Marco** — no de la Constitución — **no abre un flujo de excepción**: dispara una **alerta** dirigida al custodio del Marco (legal/DPO) y se trata como **incidente**, no como decisión discrecional. El sistema no ofrece el botón de «aprobar de todos modos» para el Marco. Distinguir, en el momento del bloqueo, si la policy violada deriva de la Constitución (excepcionable, con rastro) o del Marco (no excepcionable, alerta) es función del policy engine y del mapping; es la razón por la que el catálogo de templates marca el origen de cada regla.

| | Policy derivada de la **Constitución** | Policy derivada del **Marco Regulatorio** |
|---|---|---|
| ¿Excepcionable? | Sí, con justificación, alcance temporal y autorizador | **No** |
| Qué genera el intento de aprobación | Entrada en el [registro de excepciones](../../templates/federation/registro-excepciones.md) | **Alerta al custodio del Marco; incidente** |
| Autoridad | Custodio de la Constitución | Legal / DPO |
| Lectura de drift | Patrón B (acumulación → revisar policy o cultura) | No aplica: es violación regulatoria, no drift |

---

## 4. Ciclo de vida y retirada

En Adoption, retirar es marcar como *deprecated* y desmaterializar a mano. En Federation, un agente es un servicio con identidad, dependencias y un histórico de cadenas de decisión; retirarlo sin método deja **agentes zombi** que el sistema sigue invocando años después de que el departamento que los modeló haya desaparecido (manifiesto §5).

El delta es que el ciclo de vida — `propuesto → activo → deprecated → retirado` — y, en particular, la **retirada**, se ejecutan como **runbooks operativos versionados**, no como gestos manuales. Este documento normativo fija *qué* tiene que pasar y *quién* responde (la fila «Retirar un agente» del RACI de §1); el *cómo* paso a paso vive en los runbooks operativos de la plataforma, fuera del cuerpo, porque depende del stack y envejece con él.

Retirar un agente, como mínimo, significa todo esto y en orden (el detalle está en el [runbook de retirada de agente](../../templates/federation/runbook-retirada-agente.md)):

1. **Marcarlo como `deprecated`** en el [service registry](./criterios-funcionales.md), de modo que no se ofrezca a nuevos consumidores pero las cadenas en vuelo no se rompan.
2. **Notificar a los agentes dependientes** — los que lo declaran en su `dependsOn` ([CF-02](./criterios-funcionales.md)) — para que migren o escalen antes de la baja efectiva.
3. **Dar de baja (deregister)** el agente del registry y poner `lifecycleStatus: retirado`, **sin liberar su `agentId`**: el identificador queda archivado, no se reutiliza nunca (ver [esquema-identidad-agente.md](./esquema-identidad-agente.md) §2).
4. **Revocar sus credenciales** (`identityRef`) en el identity provider ([CF-04](./criterios-funcionales.md)), de modo que su identidad deje de verificarse.
5. **Archivar su histórico** de descriptores y de cadenas de decisión, que no se borra: las cadenas pasadas siguen siendo evidencia trazable por `correlationId` aunque el agente ya no exista.

La diferencia con Adoption no es el qué — desmaterializar siempre fue desmaterializar — sino que aquí cada paso tiene un control técnico que lo hace verificable: o las credenciales están revocadas o no lo están; o el `agentId` quedó archivado o se liberó indebidamente. La retirada deja de ser una intención y pasa a ser un estado comprobable.

> **Runbooks.** Los procedimientos paso a paso de alta, *deprecation*, retirada y propagación de un cambio de Constitución se mantienen como runbooks operativos de la plataforma de federación, versionados junto al stack. No son cuerpo normativo: el cuerpo fija el contrato (esta sección); el runbook fija la ejecución sobre el stack concreto, y se actualiza con él.

---

## Resumen de los deltas

| Pieza de gobernanza | En Adoption (manual) | Delta en Federation (programático) |
|---|---|---|
| **Custodia** | Tres custodios (Marco, Constitución, capas) | + Cuarto custodio: plataforma de federación (`platformCustodian`) (§1) |
| **Revisión de coherencia** | Lectura cruzada antes de producción | Gate de coherencia: seis comprobaciones, bloqueante y atómico, en el alta al registry (§2) |
| **Excepciones** | Trabajo manual de la custodia | Bloqueo automático en la ruta; rastro obligatorio; Marco = alerta, no excepción (§3) |
| **Detección de drift** | Revisión humana periódica | Patrones A/B/C sobre la telemetría — ver [patrones-deteccion-drift.md](./patrones-deteccion-drift.md) |
| **Retirada** | *Deprecated* + desmaterializar a mano | Runbooks versionados; cada paso con control técnico verificable (§4) |

---

*Gobernanza federada de Myrmion Federation — versión 1.0. Parte del corpus normativo.*

**Relacionados:** [manifiesto](./manifesto.md) §5 · [glosario](./glosario-federacion.md) · [criterios funcionales](./criterios-funcionales.md) · [esquema de identidad de agente](./esquema-identidad-agente.md) · [esquema del bloque de contexto cultural](./esquema-bloque-contexto-cultural.md) · [patrones de detección de drift](./patrones-deteccion-drift.md) · [regla anti-acoplamiento](./regla-anti-acoplamiento.md) · charter: [charter de la plataforma de federación](../../templates/federation/charter-plataforma-federacion.md) · [registro de excepciones](../../templates/federation/registro-excepciones.md) · [runbook de onboarding](../../templates/federation/runbook-onboarding-agente.md) · [runbook de retirada](../../templates/federation/runbook-retirada-agente.md) · gobernanza de [Myrmion Adoption](../adoption/manifesto.md) §4
