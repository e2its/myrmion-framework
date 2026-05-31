<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Charter de la Plataforma de Federación

**Versión 1.0**

*Plantilla para constituir el **cuarto custodio** descrito en el §5 del [manifiesto](../../docs/federation/manifesto.md) y especificado en la [gobernanza federada](../../docs/federation/gobernanza-federada.md) §1 — la plataforma de federación. Articula su misión, sus responsabilidades, su RACI y sus fronteras con los otros tres custodios, para una organización concreta.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

La gobernanza de Adoption distribuye la custodia en tres responsables, diferenciados por capa: el Marco Regulatorio en legal/DPO, la Constitución Corporativa en transformación digital o equivalente, y cada capa departamental en su departamento. Federation añade un cuarto custodio que Adoption no necesitaba, porque Adoption no tenía stack: la **plataforma de federación**. Es la pieza que el resto de la gobernanza da por supuesta — sin ella, no hay ruta donde aplicar policy, ni registry donde correr el gate de coherencia, ni telemetría donde medir drift.

Este charter es el documento que **constituye** ese custodio en una organización concreta: le da mandato, fronteras y autoridad escrita. La [gobernanza federada](../../docs/federation/gobernanza-federada.md) §1 dice *qué es* el cuarto custodio en el cuerpo normativo; este charter dice *quién lo encarna, con qué alcance y rindiendo cuentas a quién* en tu organización. No redefine la gobernanza — la instancia.

**Qué NO es este charter.** No es una capa departamental: la plataforma no modela cultura, no tiene voz, no atiende a clientes. No es la Constitución ni el Marco: no decide qué dice la cultura ni qué exige la ley. Es un documento operativo y organizativo que delimita la responsabilidad sobre la **maquinaria** que hace la federación posible. La distinción es la línea roja del charter entero: la plataforma **ejecuta** el motor; **no escribe** las reglas culturales.

**Quién lo rellena.** El responsable propuesto de la plataforma de federación — típicamente el lead de plataforma o de SRE — junto con el patrocinador de Federation (a menudo el custodio de la Constitución, que es quien graduó la organización de Adoption a Federation). Se co-firma con el custodio de la Constitución y con el del Marco Regulatorio, porque el charter declara fronteras *con ellos*: una frontera que solo firma un lado no es una frontera.

**Quién encarna la plataforma.** Típicamente el equipo de plataforma o de SRE, **no** el de transformación digital. Es deliberado: la custodia del stack exige rotación de credenciales, gestión de incidentes y operación 24×7, competencias que viven en plataforma, no en el área que articula la cultura. Si tu organización no tiene esa función, el charter debe declarar explícitamente quién asume esas competencias antes de federar nada.

**Cómo se rellena.** Esta plantilla mantiene el estilo socrático del resto del corpus de adopción: preguntas guía, no respuestas copiables. Cada sección plantea qué tiene que decidir tu organización; el espacio para rellenar es tuyo. Donde el cuerpo normativo fija un contrato — los seis criterios funcionales, la atomicidad del gate, la frontera Marco/Constitución en excepciones — la plantilla lo recuerda, pero **no lo renegocia**: el charter instancia el contrato, no lo afloja.

**Cuánto tiempo lleva.** Una primera versión defendible suele requerir una o dos sesiones de trabajo de medio día entre plataforma, Constitución y Marco. El charter no debería escribirse el día antes de federar el primer corredor: si las fronteras entre custodios no están claras *antes* de que haya tráfico inter-agente, se aclaran a base de incidentes, que es la peor forma de aclararlas.

**Qué se hace después.** Una vez aprobado, este charter se versiona, se firma por los tres custodios implicados (plataforma, Constitución, Marco) y se incorpora al repositorio de gobernanza de IA, junto al resto del corpus de Federation. Los runbooks operativos de la plataforma — [onboarding](./runbook-onboarding-agente.md), [retirada](./runbook-retirada-agente.md), propagación de cambio de Constitución — cuelgan de este charter y se versionan junto al stack.

**Frecuencia de revisión recomendada.** Semestral, y ad hoc cuando: cambia el stack subyacente (cambio mayor de cualquiera de los seis componentes), rota el responsable de la plataforma, cambia la estructura de custodios de la organización, o el análisis de excepciones/drift revela que una frontera entre custodios no está donde el charter dice.

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Organización | *(nombre de la organización)* |
| Versión del documento | *(p. ej. 1.0, 1.1, 2.0)* |
| Fecha de aprobación | *(YYYY-MM-DD)* |
| Próxima revisión programada | *(YYYY-MM-DD)* |
| Custodio constituido por este charter | *(equipo/persona que encarna la plataforma de federación — típicamente plataforma o SRE)* |
| Responsable de la plataforma (rol) | *(rol concreto que rinde cuentas — p. ej. Head of Platform, SRE Lead)* |
| Co-firmante — Constitución | *(custodio de la Constitución Corporativa — típicamente Director de Transformación Digital o equivalente)* |
| Co-firmante — Marco Regulatorio | *(custodio del Marco — típicamente Asesoría Jurídica / DPO)* |
| Aprobación formal | *(órgano que ha aprobado este documento)* |
| Versión de la Constitución Corporativa vigente | *(p. ej. 1.0, fecha de aprobación)* |
| Versión del Marco Regulatorio vigente | *(p. ej. 1.0, fecha de aprobación)* |
| Fase de adopción de Federation en curso | *(ver [guía de adopción por fases](../../docs/federation/guia-adopcion-por-fases.md) — p. ej. Fase 1: selección de stack y PoC)* |

---

## 1. Misión de la plataforma de federación

*La plataforma de federación es el custodio de la **maquinaria**, no de la cultura. Su misión no es decidir qué dice la Constitución ni qué exige el Marco — es operar, con disponibilidad y reproducibilidad, el stack sobre el que la federación sucede, y traducir a algo que el policy engine evalúe lo que el custodio de la Constitución decide. Esta sección fija esa misión para tu organización en una frase verificable, no aspiracional.*

### 1.1 Misión en una frase

*Pregunta guía: en una sola frase, ¿qué garantiza la plataforma de federación que ningún otro custodio garantiza? La frase debe ser concreta y verificable. "Damos soporte a la IA de la empresa" no es misión — es vaguedad. "Operamos el stack que cumple los seis criterios funcionales y mantenemos la federación en un estado donde todo agente alcanzable cumple el contrato" sí es misión articulada. El contrato de fondo: la federación es exactamente la propiedad de que todo agente invocable ha pasado el gate de coherencia.*

[Espacio para rellenar]

### 1.2 Qué deja de ser manual al constituir este custodio

*Pregunta guía: la gobernanza federada introduce cuatro deltas respecto a Adoption — cuarto custodio, gate de coherencia programático, gestión de excepciones con rastro reproducible, y retirada por runbooks ([gobernanza federada](../../docs/federation/gobernanza-federada.md)). ¿Cuáles de esas piezas hoy se hacen a mano en tu organización y cuáles pasarán a ser programáticas con la plataforma constituida? Articular el antes/después protege contra federar sin haber industrializado lo que la federación da por supuesto.*

[Espacio para rellenar]

### 1.3 Por qué este equipo y no transformación digital

*Pregunta guía: ¿qué función concreta de tu organización encarna la plataforma, y por qué tiene las competencias operativas (rotación de credenciales, gestión de incidentes, operación 24×7) que la cultura no tiene? Si la respuesta es "transformación digital lo asume porque no hay plataforma", articular explícitamente cómo se cubre esa brecha de competencias antes de federar.*

[Espacio para rellenar]

### 1.4 La línea roja: ejecuta el motor, no escribe las reglas

*Pregunta guía: la plataforma traduce lo que el custodio de la Constitución decide; no decide ella la cultura. ¿Cómo se materializa esta separación en tu organización? En particular: cuando un policy template y la Constitución discrepan, ¿queda escrito que la autoridad es del custodio de la Constitución, no de la plataforma? Articular el mecanismo concreto de discrepancia, no solo el principio.*

[Espacio para rellenar]

### 1.5 Custodio operativo de esta sección

---

## 2. Responsabilidades de la plataforma

*La plataforma custodia tres cosas, ninguna de ellas cultural — el stack que cumple los criterios funcionales, los policy templates transversales, y la pipeline de observabilidad — y opera el ciclo de vida de los agentes (gate de coherencia, excepciones, retirada). Esta sección las instancia para tu organización. Lo que el cuerpo normativo fija como contrato se recuerda; lo que tu organización decide se rellena.*

### 2.1 El stack que cumple los seis criterios funcionales

*La plataforma custodia el stack que cumple los seis [criterios funcionales](../../docs/federation/criterios-funcionales.md) (CF-01..CF-06). La elección concreta de componentes es suya; la decisión se registra como ADR de adopción, no en este charter. Las marcas viven en el [apéndice de stacks de referencia](../../docs/federation/appendix/README.md), nunca aquí.*

*Pregunta guía: para cada criterio funcional, ¿qué componente del stack lo cubre, quién lo opera dentro de la plataforma, y dónde está el ADR que registra la decisión? Rellenar la tabla por función, sin nombrar producto en este charter — el nombre va al ADR y al apéndice.*

| Criterio funcional | Qué cubre | Componente (referencia al ADR, no marca aquí) | Responsable operativo |
|---|---|---|---|
| **CF-01 — Gateway** | Intermedia todas las llamadas inter-agente; punto de extensión para policy enforcement; propaga metadatos | *(ADR-xxxx)* | |
| **CF-02 — Service registry** | Descubrimiento de agentes con descriptores extendidos; sede del gate de coherencia (§2.4) | *(ADR-xxxx)* | |
| **CF-03 — Policy engine** | Evaluación declarativa en la ruta; versionado de políticas con auditoría de cambios | *(ADR-xxxx)* | |
| **CF-04 — Autenticación mutua con identidad criptográfica verificable** | El receptor verifica criptográficamente la identidad del emisor antes de ejecutar; credencial de vida corta y revocable; vinculable de forma estable al `agentId` | *(ADR-xxxx)* | |
| **CF-05 — Observabilidad agent-aware** | Trazabilidad de cadenas completas por `correlationId`; exportación del bloque cultural como atributos del span | *(ADR-xxxx)* | |
| **CF-06 — Des-identificación en la ruta** | Detección y redacción/tokenización de datos sensibles (PII/PHI y los que el Marco defina) antes de que alcancen el modelo | *(ADR-xxxx)* | |

*Nota de contrato: CF-04 nunca se enuncia por una sigla de transporte concreta. Lo que la plataforma garantiza son las **tres propiedades** de arriba (verificabilidad por el receptor, vida corta y revocabilidad, vinculación estable al `agentId`); el mecanismo concreto es campo libre (`mutualAuthMechanism`) y no se privilegia ninguno — ver [regla anti-acoplamiento](../../docs/federation/regla-anti-acoplamiento.md).*

### 2.2 Los policy templates transversales

*La plataforma custodia los policy templates **transversales** — los que derivan de principios de la Constitución que aplican a **toda** la federación, no a un dominio (p. ej. la des-identificación de PII/PHI en cualquier ruta, o el veto a exteriorizar cifras financieras sin endorsement). El **formato** de esos templates es el de las [convenciones de mapping](../../docs/federation/convenciones-mapping-constitucion-policy.md); las implementaciones por dialecto viven en el [apéndice de policy templates](../../docs/federation/appendix/policy-templates/README.md), no aquí.*

*Pregunta guía: ¿qué policy templates transversales custodia tu plataforma, de qué principio de la Constitución deriva cada uno, y — crítico — cuáles derivan de la Constitución (excepcionables) y cuáles del Marco (no excepcionables, ver §4)? El catálogo debe marcar el origen de cada regla, porque de eso depende si un bloqueo abre flujo de excepción o dispara alerta.*

| Policy template transversal | Principio del que deriva | Origen: Constitución / **Marco** | Implementación (referencia al apéndice) |
|---|---|---|---|
| *(p. ej. des-identificación PII/PHI en la ruta)* | *(principio de la Constitución / artículo del Marco)* | | *(appendix/policy-templates/...)* |
| | | | |
| | | | |

*Recordatorio de frontera: la plataforma **traduce** el principio a template; **no decide** el principio. Si el template y la Constitución discrepan, la autoridad es del custodio de la Constitución.*

### 2.3 La pipeline de observabilidad

*La plataforma custodia la pipeline que hace medibles la trazabilidad ([CF-05](../../docs/federation/criterios-funcionales.md)) y los [patrones de detección de drift](../../docs/federation/patrones-deteccion-drift.md): correlación por `correlationId`, exportación del bloque cultural como atributos del span, y las consultas que los patrones de drift necesitan.*

*Pregunta guía: ¿qué garantiza tu pipeline sobre trazabilidad de cadenas inter-agente, y qué consultas concretas alimentan los patrones de drift (cadenas de decisiones, excepciones, coherencia entre agentes)? Las [métricas de federación](../../docs/federation/metricas-federacion.md) que la plataforma debe poder calcular — tasa de bloqueo, reducción de fricción en handovers — ¿están cubiertas por la pipeline?*

[Espacio para rellenar]

### 2.4 El gate de coherencia en el alta

*La plataforma opera el gate de coherencia ([gobernanza federada](../../docs/federation/gobernanza-federada.md) §2): el conjunto de comprobaciones programáticas reproducibles que se ejecutan en el alta al [service registry](../../docs/federation/criterios-funcionales.md) (CF-02). El contrato es fijo y este charter no lo afloja: el gate es **bloqueante y atómico** — si cualquiera de las comprobaciones falla, el alta falla; no hay alta "con observaciones" ni alta parcial. Las seis comprobaciones están especificadas en el cuerpo; el detalle paso a paso de su ejecución sobre tu stack vive en el [runbook de onboarding](./runbook-onboarding-agente.md).*

*Pregunta guía: ¿quién, dentro de la plataforma, opera el gate; cómo se garantiza la reproducibilidad (que re-ejecutar el gate sobre el mismo descriptor y el mismo estado de Constitución produzca el mismo resultado); y cómo se sella el resultado (`coherenceReview`) en el descriptor de identidad? La autoridad de las comprobaciones culturales — `constitutionRef` vigente, conflicto de capabilities con la Constitución, `dataClasses` contra el Marco — no es de la plataforma: la plataforma ejecuta la comprobación, pero quién decide qué es "vigente" o "prohibido" es el custodio de la Constitución o del Marco.*

[Espacio para rellenar]

### 2.5 La gestión de excepciones y su rastro

*La plataforma opera la maquinaria de bloqueo — el policy engine bloquea en la ruta toda llamada que viola una policy — y garantiza el **rastro reproducible** de toda excepción aprobada en el [registro de excepciones](./registro-excepciones.md). El contrato fijo (ver §4 de este charter y [gobernanza federada](../../docs/federation/gobernanza-federada.md) §3): no existe la excepción sin registro, y la excepción al Marco no es una excepción sino una alerta.*

*Pregunta guía: ¿cómo garantiza tu plataforma que ninguna excepción se aprueba sin los campos mínimos (policy violada y versión, agentes origen/destino, `correlationId`, justificación, alcance temporal, autorizador)? ¿Y cómo distingue, en el momento del bloqueo, si la policy violada deriva de la Constitución o del Marco, para enrutar a flujo de excepción o a alerta?*

[Espacio para rellenar]

### 2.6 El ciclo de vida y la retirada por runbooks

*La plataforma ejecuta el ciclo de vida del agente — `propuesto → activo → deprecated → retirado` — como runbooks operativos versionados, no como gestos manuales ([gobernanza federada](../../docs/federation/gobernanza-federada.md) §4). El contrato fijo: retirar un agente significa, en orden, marcarlo `deprecated`, notificar a los dependientes (`dependsOn`), darlo de baja del registry sin liberar su `agentId`, revocar sus credenciales y archivar su histórico. El `agentId` nunca se reutiliza. El detalle paso a paso vive en el [runbook de retirada](./runbook-retirada-agente.md).*

*Pregunta guía: ¿quién ejecuta la retirada dentro de la plataforma, qué control técnico verificable acredita cada paso (credenciales revocadas o no; `agentId` archivado o liberado indebidamente), y cómo se evita acumular agentes zombi? Recordar: la **decisión** de retirar un agente la toma el departamento; la **mecánica** de hacerlo sin romper la federación es de la plataforma.*

[Espacio para rellenar]

### 2.7 Custodio operativo de esta sección

---

## 3. RACI de la plataforma

*Esta sección instancia el RACI mínimo de la federación ([gobernanza federada](../../docs/federation/gobernanza-federada.md) §1) para tu organización, nombrando a los responsables concretos. Cubre solo las actividades donde Federation cambia algo respecto a Adoption. **R** = responsable de ejecutar, **A** = autoridad que rinde cuentas, **C** = consultado, **I** = informado.*

### 3.1 Tabla RACI instanciada

*Pregunta guía: la columna de patrón normativo fija el reparto de cada actividad; rellena cada celda con el rol o persona concreta de tu organización. El patrón no se renegocia — si una celda de tu organización contradice el patrón normativo, no es que la plantilla esté mal: es que tu reparto de custodia aún no es de Federation.*

| Actividad | Patrón normativo | Marco (legal/DPO) | Constitución (transf. digital) | Capa departamental | **Plataforma (este charter)** |
|---|---|---|---|---|---|
| Definir el principio cultural a automatizar | A/R en Constitución | C | A/R | C | I |
| Traducir el principio a policy template transversal | A en Constitución, R en plataforma | I | A | I | **R** |
| Operar el stack y la pipeline de observabilidad | A/R en plataforma | I | I | I | **A/R** |
| Ejecutar el gate de coherencia en el alta | A/R en plataforma | I | C | C | **A/R** |
| Aprobar una excepción a una policy de Constitución | A en Constitución, R en capa | I | A | R (la solicita) | C |
| Tratar un intento de excepción al Marco | A/R en legal/DPO | A/R | I | I | **I** (genera la alerta) |
| Retirar un agente | A en capa, R en plataforma | I | C | A (lo decide) | **R** (lo ejecuta) |
| Ejecutar los patrones de drift | A en Constitución, R en plataforma | C | A | C | **R** |

### 3.2 Las tres lecturas que el charter hace explícitas

*Estas tres lecturas no son negociables; son la razón de ser de la tabla. Articula, para tu organización, cómo se cumple cada una.*

**1. La autoridad cultural no se delega a la plataforma.** Donde hay decisión cultural (qué principio, qué excepción, qué dice el drift), la **A** es del custodio de la Constitución o del Marco. La plataforma es **R** — ejecuta — pero no rinde cuentas de la cultura.

*Pregunta guía: ¿qué impide, en tu organización, que la plataforma acabe decidiendo de facto la cultura por la vía de "es lo que el stack permite"? Articular el mecanismo, no el deseo.*

[Espacio para rellenar]

**2. El Marco no tiene fila de excepción.** Su única fila relacionada es «tratar un intento de excepción», porque para el Marco un intento de excepción **es un incidente** (§4). El sistema no ofrece el botón de "aprobar de todos modos" para el Marco.

*Pregunta guía: ¿la plataforma tiene confirmado que el policy engine no expone aprobación manual para policies derivadas del Marco? ¿Quién verifica esto y con qué frecuencia?*

[Espacio para rellenar]

**3. Retirar un agente lo decide el departamento, lo ejecuta la plataforma.** La decisión de jubilar una capacidad es cultural/organizativa; la mecánica de hacerlo sin romper la federación es operativa.

*Pregunta guía: ¿cómo se formaliza en tu organización la entrega entre "el departamento decide retirar" y "la plataforma ejecuta el runbook de retirada"? ¿Qué evita que un agente se quede en `deprecated` indefinidamente sin que nadie ejecute la baja?*

[Espacio para rellenar]

### 3.3 Custodio operativo de esta sección

---

## 4. Fronteras con los otros tres custodios

*Esta es la sección más importante del charter. Un custodio nuevo solo funciona si sus fronteras con los existentes están escritas y firmadas por ambos lados. Cada subsección fija una frontera y la pregunta que tu organización debe responder para no resolverla a base de incidentes.*

### 4.1 Frontera con el custodio del Marco Regulatorio (legal/DPO)

*El Marco no admite excepciones. Es la frontera dura de toda la gobernanza. La plataforma la hace explícita en la ruta: un intento de aprobar manualmente una llamada bloqueada por una policy derivada del **Marco** — no de la Constitución — **no abre flujo de excepción**: dispara una **alerta** dirigida al custodio del Marco y se trata como **incidente**. La incompatibilidad de `regulatoryFrameworkRef` es siempre dura ([esquema de identidad](../../docs/federation/esquema-identidad-agente.md)).*

| | Policy derivada de la **Constitución** | Policy derivada del **Marco Regulatorio** |
|---|---|---|
| ¿Excepcionable? | Sí, con justificación, alcance temporal y autorizador | **No** |
| Qué genera el intento de aprobación | Entrada en el [registro de excepciones](./registro-excepciones.md) | **Alerta al custodio del Marco; incidente** |
| Autoridad | Custodio de la Constitución | Legal / DPO |
| Rol de la plataforma | Opera el flujo y garantiza el rastro | Genera la alerta; **no** ofrece aprobación |

*Pregunta guía: ¿qué garantiza la plataforma al custodio del Marco — alerta inmediata ante cualquier intento de excepción al Marco, trazabilidad completa de la cadena (`correlationId`) como evidencia, e imposibilidad técnica del "aprobar de todos modos"? ¿Y qué espera la plataforma del Marco a cambio — que las `dataClasses` autorizadas por dominio y los principios no excepcionables estén declarados de forma que el gate (§2.4, comprobación de `dataClasses` contra el Marco) los pueda evaluar?*

[Espacio para rellenar]

### 4.2 Frontera con el custodio de la Constitución Corporativa (transformación digital)

*Es la frontera de la traducción. La plataforma **traduce** lo que el custodio de la Constitución decide a policy templates que el engine evalúa; no decide el contenido cultural. Cuando un policy template y la Constitución discrepan, la autoridad es del custodio de la Constitución, no de la plataforma.*

*Pregunta guía: ¿cómo fluye un cambio de la Constitución hasta los policy templates transversales — quién avisa a la plataforma, en qué plazo, y cómo se re-ejecuta el gate sobre los agentes cuyo `constitutionRef` queda obsoleto (runbook de propagación de cambio de Constitución)? ¿Quién resuelve una discrepancia entre lo que la Constitución dice y lo que el stack puede expresar — y queda escrito que la última palabra es de la Constitución, no del stack?*

[Espacio para rellenar]

### 4.3 Frontera con los custodios de las capas departamentales

*Cada departamento custodia su propio agente; la plataforma custodia la federación en la que ese agente entra. La frontera está en el `owner` (custodio de dominio) frente al `platformCustodian` (este charter) del [descriptor de identidad](../../docs/federation/esquema-identidad-agente.md). El departamento decide qué hace su agente y cuándo se retira; la plataforma decide si ese agente puede estar en la federación (gate) y ejecuta su alta, su retirada y la operación de la ruta.*

*Pregunta guía: ¿qué le da la plataforma a un departamento que quiere federar un agente — onboarding por runbook, gate de coherencia como puerta de entrada, soporte operativo de la ruta? ¿Y qué exige a cambio — descriptor válido contra el esquema, `agentId` con la forma `urn:myrmion:agent:<org>:<dominio>:<nombre>`, declaración honesta de capabilities y `dataClasses`? ¿Quién media cuando el gate bloquea el alta de un agente que el departamento considera correcto?*

[Espacio para rellenar]

### 4.4 Lo que la plataforma NO custodia

*La frontera se define tanto por lo que se incluye como por lo que se excluye. La plataforma no custodia cultura: no decide qué dice la Constitución, no decide qué criterios aplica un dominio, no atiende a interlocutores externos, no modela voz. Opera la maquinaria y traduce decisiones ajenas.*

*Pregunta guía: lista explícita de las cosas que, en tu organización, alguien podría asumir erróneamente que son de la plataforma y no lo son. Cada elemento de esta lista es una discusión que prefieres tener ahora, por escrito, que durante un incidente.*

[Espacio para rellenar]

### 4.5 Custodio operativo de esta sección

---

## 5. Operación, escalado y continuidad

*La custodia del stack exige operación real: incidentes, rotación de credenciales, disponibilidad. Esta sección articula cómo la plataforma sostiene la federación en el día a día y qué pasa cuando algo falla.*

### 5.1 Modelo de operación y disponibilidad

*Pregunta guía: ¿qué nivel de disponibilidad garantiza la plataforma para la ruta inter-agente, qué ventana de operación (24×7 o no), y qué pasa con las cadenas en vuelo durante una indisponibilidad? Recordar: si el gateway cae, ningún agente se invoca; la disponibilidad de la plataforma es la disponibilidad de la federación.*

[Espacio para rellenar]

### 5.2 Gestión de incidentes y de credenciales

*Pregunta guía: ¿cómo gestiona la plataforma la rotación y revocación de credenciales ([CF-04](../../docs/federation/criterios-funcionales.md): vida corta y revocable), y cómo responde a un incidente de seguridad — credencial comprometida, agente que se comporta fuera de contrato? La revocación de credenciales es uno de los pasos de la retirada (§2.6) pero también una acción de incidente por sí misma.*

[Espacio para rellenar]

### 5.3 Escalado dentro de la plataforma y hacia los otros custodios

*Pregunta guía: ¿qué situaciones escala la plataforma, a quién y con qué información mínima? Distinguir el escalado **operativo** (el stack falla → resuelve la plataforma) del escalado **de gobernanza** (acumulación de excepciones, drift detectado → escala al custodio de la Constitución; intento de excepción al Marco → alerta a legal/DPO). La plataforma detecta; la autoridad de gobernanza decide.*

| Situación | Tipo (operativa / gobernanza) | A quién escala la plataforma | Información mínima a adjuntar |
|---|---|---|---|
| *(p. ej. acumulación de excepciones a una misma policy)* | *(gobernanza)* | *(custodio de la Constitución)* | *(`policyId@version`, conteo, `correlationId`s afectados)* |
| | | | |
| | | | |

### 5.4 Continuidad y relevo del custodio

*Pregunta guía: ¿qué pasa si rota el responsable de la plataforma o el equipo se reorganiza? La custodia del stack no puede quedar huérfana: hay que articular el relevo, la documentación mínima que se hereda (runbooks, ADRs, inventario de agentes y credenciales), y quién valida que el relevo está completo antes de que el saliente se vaya.*

[Espacio para rellenar]

### 5.5 Custodio operativo de esta sección

---

## 6. Coherencia y mantenimiento del charter

*Esta sección articula cómo se mantiene vivo el charter.*

### 6.1 Mecanismo de actualización

*Pregunta guía: ¿quién detecta que el charter necesita actualización, quién propone el cambio, quién lo aprueba, en qué plazos? Recordar los disparadores ad hoc: cambio mayor de stack, rotación del responsable, cambio en la estructura de custodios, o frontera que el análisis de excepciones/drift revela mal trazada.*

[Espacio para rellenar]

### 6.2 Coherencia con el corpus normativo

*El charter instancia; no renegocia. Si el corpus normativo de Federation se actualiza ([gobernanza federada](../../docs/federation/gobernanza-federada.md), [criterios funcionales](../../docs/federation/criterios-funcionales.md), esquemas), el charter se revisa para seguir siendo coherente. Si una versión del charter contradice el cuerpo, prevalece el cuerpo.*

*Pregunta guía: ¿quién verifica, en cada revisión, que el charter sigue siendo coherente con el cuerpo normativo y con los runbooks hermanos (onboarding, retirada, registro de excepciones)?*

[Espacio para rellenar]

### 6.3 Indicadores de que la frontera entre custodios se está erosionando

*Pregunta guía: ¿qué señales avisarían de que la línea roja del §1.4 se está borrando — la plataforma decidiendo cultura de facto, o un custodio cultural operando el stack a mano por su cuenta? Outputs donde "el stack no lo permite" sustituye a "la Constitución no lo permite", excepciones que la plataforma aprueba sin pasar por la Constitución, policy templates que la plataforma escribe sin mandato cultural. Estos indicadores disparan revisión del charter.*

[Espacio para rellenar]

---

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Este charter constituye el cuarto custodio — la plataforma de federación — descrito en el §5 del [manifiesto de Myrmion Federation](../../docs/federation/manifesto.md) y especificado en la [gobernanza federada](../../docs/federation/gobernanza-federada.md) §1. Instancia el contrato normativo para una organización concreta; donde charter y cuerpo discrepen, prevalece el cuerpo. La plataforma ejecuta el motor; no escribe las reglas culturales.*

*Para ver este charter rellenado como referencia orientativa, consultar el [ejemplo de Consultora Modelo S.L.](./charter-plataforma-federacion-ejemplo.md).*

**Relacionados:** [manifiesto](../../docs/federation/manifesto.md) §5 · [gobernanza federada](../../docs/federation/gobernanza-federada.md) · [criterios funcionales](../../docs/federation/criterios-funcionales.md) · [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md) · [convenciones de mapping](../../docs/federation/convenciones-mapping-constitucion-policy.md) · [patrones de detección de drift](../../docs/federation/patrones-deteccion-drift.md) · [métricas de federación](../../docs/federation/metricas-federacion.md) · [regla anti-acoplamiento](../../docs/federation/regla-anti-acoplamiento.md) · runbooks: [onboarding](./runbook-onboarding-agente.md) · [retirada](./runbook-retirada-agente.md) · [registro de excepciones](./registro-excepciones.md) · plantillas de Adoption: [Constitución Corporativa](../adoption/constitucion-corporativa.md) · [Capa Departamental](../adoption/capa-departamental.md)
