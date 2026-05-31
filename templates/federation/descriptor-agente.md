<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Plantilla de Descriptor de Identidad de Agente

**Versión 1.0**

*Plantilla socrática para que un departamento declare su agente ante la federación. Es la pieza que rellena cada organización a partir del contrato del [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md): el documento fundacional con el que un agente declara quién es, qué dominio gobierna, qué capacidades expone y a qué versión de la Constitución se adhiere. Sin un descriptor válido y con su `coherenceReview` aprobada, un agente no entra en el service registry.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

Esta plantilla te guía, mediante **preguntas**, para redactar el **descriptor de identidad** de tu agente departamental — lo que permite que tu agente y los de otros dominios se descubran y se entiendan *sin coordinación humana previa*.

No es un formulario que rellenar a ciegas. Cada pregunta busca que **expliciten** una decisión de diseño antes de que tu agente sea descubierto, invocado o auditado por la federación. En particular, las propiedades `externalizes`, `canCommit` y `sideEffectClass` de cada capacidad son **abstracciones decidibles en tiempo de diseño**: las declaras tú, modelando el agente, no se infieren en runtime. Es lo que permite que el *gate de coherencia* evalúe el descriptor antes de que el agente se registre.

**Quién la rellena.** Dos custodios firman el descriptor: el **custodio de dominio** (`owner`) — el departamento responsable del contenido cultural del agente — y el **custodio de la plataforma de federación** (`platformCustodian`), el cuarto custodio responsable del registro y del stack. El departamento conoce su propio trabajo mejor que nadie; la plataforma garantiza que el descriptor encaja en la federación.

**Esta plantilla es el espejo socrático del contrato.** La forma exacta de los campos, sus tipos y las reglas de validación viven en el [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md). Esta plantilla te ayuda a *decidir* qué declarar; el esquema define *cómo* se declara. **El descriptor es un contrato, no una serialización:** el JSON de la sección final solo ilustra la forma; cómo se almacena y se firma en un service registry concreto es responsabilidad del stack.

**Instrucciones:**

1. Copia este fichero a tu espacio de trabajo.
2. Responde cada pregunta guía en el espacio indicado.
3. Una vez redactadas las respuestas, deriva de ellas el descriptor en su forma serializable (la sección final te ayuda a componerlo).
4. Antes de proponer el alta, valida que la `coherenceReview` está en `pendiente` y que has recalculado los `hash` de las referencias de gobernanza según el contrato de hash. **El alta en el registry falla si `coherenceReview.status != aprobado`.**

> **Nota — `<org>` es configurable.** El `agentId` tiene la forma `urn:myrmion:agent:<org>:<dominio>:<nombre>`. El token `<org>` es **un identificador que elige tu organización** (registrado en su Perfil de Adopción); el framework nunca lo fija. Sustitúyelo por el identificador corto de tu organización en todos los campos donde aparezca.

> **Nota — los hashes.** Los campos `hash` (de `constitutionRef`, `departmentLayerRef`, `regulatoryFrameworkRef`) y el conjunto `compatibleConstitutionHashes` se calculan con el contrato de hash: `"sha256:"` sobre la forma canónica del documento de gobernanza (UTF-8 NFC, saltos LF, sin trailing whitespace y **excluyendo la sección «0. Metadatos»**). Recalcula el hash cada vez que edites el documento de gobernanza al que apunta.

> **Nota — para ver esta plantilla rellena** de extremo a extremo, consulta el [ejemplo del agente legal de Consultora Modelo S.L.](./descriptor-agente-ejemplo.md).

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Departamento al que pertenece el agente | *(nombre del departamento o función)* |
| `agentId` del agente declarado | *(urn:myrmion:agent:&lt;org&gt;:&lt;dominio&gt;:&lt;nombre&gt;)* |
| `schemaVersion` (versión del esquema que cumple) | *(p. ej. 1.0)* |
| `version` del descriptor | *(p. ej. 1.0.0)* |
| Fecha de última revisión | *(YYYY-MM-DD)* |
| Custodio de dominio (`owner`) | *(rol o persona responsable del contenido cultural)* |
| Custodio de plataforma (`platformCustodian`) | *(rol del cuarto custodio: plataforma de federación)* |
| Estado | *(Borrador / En revisión / Aprobado)* |

---

## 1. Identificación del agente

*Esta sección fija quién es el agente para la federación: su clave estable, su dominio y su versión. Estos campos no cambian a la ligera — el `agentId` no se reasigna nunca.*

### 1.1 `agentId`

*Pregunta guía: ¿cuál es el identificador único global de tu agente? Sigue el formato `urn:myrmion:agent:<org>:<dominio>:<nombre>`, donde `<org>` es el identificador de TU organización, `<dominio>` el dominio departamental y `<nombre>` distingue agentes dentro del mismo dominio. ¿Es estable y único en toda la federación? Recuerda que es no reutilizable: si algún día retiras este agente, este `agentId` queda archivado, no se libera.*

[Espacio para rellenar]

### 1.2 `displayName`

*Pregunta guía: ¿cómo debe verse el nombre de tu agente cuando lo lea una persona — en un dashboard, en una auditoría, en una traza de una cadena de decisiones?*

[Espacio para rellenar]

### 1.3 `domain`

*Pregunta guía: ¿qué dominio departamental gobierna este agente (`comercial`, `legal`, `finanzas`, `personas`…)? Debe estar alineado con la Capa Departamental de la que el agente deriva. Un agente gobierna un único dominio; si necesitas cubrir más de uno, probablemente necesitas más de un agente.*

[Espacio para rellenar]

### 1.4 `version` y `schemaVersion`

*Pregunta guía: ¿cuál es la `version` del descriptor (semver `MAJOR.MINOR.PATCH`) y qué la incrementa — un cambio de capacidades, de constitución aplicada, de dominio? ¿Y qué `schemaVersion` del esquema de identidad cumple este descriptor? Distinguir ambas permite evolucionar el contrato sin romper agentes antiguos.*

[Espacio para rellenar]

### 1.5 `criticality`

*Pregunta guía: ¿cuál es la criticidad del dominio de este agente — `baja`, `media`, `alta` o `critica`? La criticidad modula la cadencia de revisión de drift y la severidad del gate de coherencia. No la infles: declarar `critica` un dominio que no lo es satura la gobernanza.*

[Espacio para rellenar]

---

## 2. Herencia de gobernanza

*Un agente departamental hereda, por construcción, del Marco Regulatorio y de la Constitución Corporativa, y deriva de una Capa Departamental concreta. Esta sección declara de qué versión de cada documento hereda, anclando cada referencia a su `hash` para que la compatibilidad sea verificable.*

### 2.1 `departmentLayerRef`

*Pregunta guía: ¿de qué Capa Departamental deriva este agente, en qué versión, y cuál es su `hash`? Indica `{docId, version, hash}`. La Capa Departamental es el origen cultural del agente: su voz, sus tipos de tarea y sus restricciones de dominio vienen de aquí.*

[Espacio para rellenar]

### 2.2 `constitutionRef`

*Pregunta guía: ¿qué versión de la Constitución Corporativa aplica este agente? Indica `{version, approvalDate, hash}`. ¿Has recalculado el `hash` tras la última edición de la Constitución?*

[Espacio para rellenar]

### 2.3 `regulatoryFrameworkRef`

*Pregunta guía: ¿de qué versión del Marco Regulatorio hereda? Indica `{version, hash}`. Atención: la incompatibilidad de Marco es **dura** — no admite excepción posible. Asegúrate de heredar de la versión vigente.*

[Espacio para rellenar]

### 2.4 `compatibleConstitutionHashes`

*Pregunta guía: ¿qué hashes de Constitución reconoce este agente como compatibles con el suyo? Este conjunto es lo que habilita la validación de compatibilidad en O(1) cuando recibe una llamada: el receptor comprueba que el `constitutionHash` del emisor está aquí, sin re-parsear la Constitución. Incluye la versión vigente y, si procede, versiones anteriores cuyas cadenas de decisión sigan abiertas. ¿Por qué declaras compatible cada una?*

[Espacio para rellenar]

---

## 3. Capacidades

*Pregunta guía general: ¿qué tools expone tu agente a la federación? Cada capacidad que declares aquí es una promesa pública y, a la vez, lo que el policy engine necesita para decidir **sin introspección de runtime**. Declara solo lo que tu agente realmente ofrece, con propiedades de gobernanza honestas.*

Repite la subsección **3.x** por cada capacidad. Para cada una, responde:

### 3.1 Capacidad: *[toolName]*

#### `toolName`

*Pregunta guía: ¿cuál es el nombre de esta tool? Debe ser estable y descriptivo (p. ej. `emitir_dictamen`).*

[Espacio para rellenar]

#### `sideEffectClass`

*Pregunta guía: ¿qué clase de efecto tiene esta tool — `lectura`, `escritura`, `comunicacion-externa` o `compromiso`? La clase permite a las policies razonar por categoría, no por tool concreta. Sé honesto: declarar `lectura` algo que escribe rompe la confianza de la federación.*

[Espacio para rellenar]

#### `externalizes`

*Pregunta guía: ¿esta tool puede sacar información fuera del dominio o de la organización? (`true` / `false`). Es el disparador típico de las policies de externalización (p. ej. cifras financieras que no deben salir sin pasar por un control). Si externaliza, ¿qué sale y hacia dónde?*

[Espacio para rellenar]

#### `canCommit`

*Pregunta guía: ¿esta tool puede generar un compromiso contractual que vincule a la organización? (`true` / `false`). Es el disparador típico de la policy «no asumimos compromisos sin pasar por legal». Si puede comprometer, ¿qué salvaguarda la gobierna?*

[Espacio para rellenar]

#### `dataClassesTouched`

*Pregunta guía: ¿qué clases de dato toca esta tool, con el vocabulario que defina tu Marco Regulatorio (p. ej. `C0..C4`)? Enumera todas las que apliquen; este campo es el disparador de las policies de des-identificación en la ruta.*

[Espacio para rellenar]

---

## 4. Endpoint e identidad criptográfica

*El descriptor declara dónde se invoca el agente y cómo se verifica su identidad — sin atarse a un transporte ni a un mecanismo de autenticación concreto. El binding a un protocolo y el mecanismo concreto viven en el apéndice del corpus.*

### 4.1 `endpoint`

*Pregunta guía: ¿dónde se invoca este agente? Declara `{transport, address}`, donde `transport` es un descriptor abstracto del protocolo (p. ej. `mcp`). El binding concreto a un protocolo no se decide aquí.*

[Espacio para rellenar]

### 4.2 `mutualAuthMechanism` y `mutualAuthVerified`

*Pregunta guía: ¿qué mecanismo de autenticación mutua soporta tu agente? Es un campo libre, no un enum: el framework no privilegia ningún mecanismo. Lo que importa es que satisfaga las tres propiedades de **autenticación mutua con identidad criptográfica verificable**: (1) el receptor verifica criptográficamente la identidad del emisor antes de ejecutar; (2) la credencial es de vida corta y revocable; (3) la identidad es vinculable de forma estable al `agentId`. ¿Ha verificado el registry (`mutualAuthVerified`) que el mecanismo declarado satisface las tres?*

[Espacio para rellenar]

### 4.3 `identityRef`

*Pregunta guía: ¿cuál es la referencia (URI opaca) a la identidad criptográfica de tu agente en el IdP? No se incrusta la clave ni el secreto: solo se referencia. ¿No asume un IdP central ni un formato concreto?*

[Espacio para rellenar]

---

## 5. Custodios, dependencias y ciclo de vida

*Esta sección declara quién responde por el agente, de qué otros agentes depende y en qué punto de su ciclo de vida está.*

### 5.1 `owner` y `platformCustodian`

*Pregunta guía: ¿quién es el custodio de dominio (`owner`) responsable del contenido cultural del agente — típicamente el departamento? ¿Y quién es el custodio de plataforma (`platformCustodian`), el cuarto custodio responsable del registro y del stack? Ambos firman el descriptor.*

[Espacio para rellenar]

### 5.2 `dependsOn`

*Pregunta guía: ¿de qué otros agentes depende este (lista de `agentId`)? Declararlo habilita la notificación en cascada cuando uno de ellos se retira. Si no depende de ninguno, déjalo vacío.*

[Espacio para rellenar]

### 5.3 `lifecycleStatus`

*Pregunta guía: ¿en qué estado del ciclo de vida está el agente — `propuesto`, `activo`, `deprecated` o `retirado`? Al proponerlo por primera vez es `propuesto`; pasa a `activo` solo cuando el gate de coherencia lo aprueba.*

[Espacio para rellenar]

### 5.4 `coherenceReview`

*Pregunta guía: ¿cuál es el resultado del gate de coherencia? Declara `{status, reviewedAgainst, date}`, donde `status ∈ {pendiente, aprobado, rechazado}` y `reviewedAgainst` es la versión del set de policy templates contra el que se revisó. Al proponer el alta, `status` será `pendiente`; el alta en el registry **falla si no llega a `aprobado`**. ¿Quién es responsable de la próxima revisión de coherencia?*

[Espacio para rellenar]

---

## 6. Composición del descriptor

*Pregunta guía: a partir de tus respuestas anteriores, ¿puedes componer el descriptor en su forma serializable y validarlo contra el contrato? Recuerda las reglas de validación: `agentId` con formato URN canónico, estable y único; campos requeridos presentes y bien tipados; los `hash` según el contrato de hash; cada capacidad con `toolName`, `sideEffectClass`, `externalizes`, `canCommit` y `dataClassesTouched`; `version` y `schemaVersion` en semver; `coherenceReview.status` en `pendiente` al proponer el alta. El YAML siguiente solo ilustra la forma — el contrato es la tabla de campos del esquema.*

```yaml
schemaVersion: "[Espacio para rellenar]"
agentId: "urn:myrmion:agent:<org>:<dominio>:<nombre>"
displayName: "[Espacio para rellenar]"
domain: "[Espacio para rellenar]"
version: "[Espacio para rellenar]"
criticality: "[baja | media | alta | critica]"
departmentLayerRef: { docId: "[…]", version: "[…]", hash: "sha256:[…]" }
constitutionRef: { version: "[…]", approvalDate: "[YYYY-MM-DD]", hash: "sha256:[…]" }
regulatoryFrameworkRef: { version: "[…]", hash: "sha256:[…]" }
compatibleConstitutionHashes: ["sha256:[…]"]
dataClasses: ["[…]"]
capabilities:
  - toolName: "[Espacio para rellenar]"
    sideEffectClass: "[lectura | escritura | comunicacion-externa | compromiso]"
    externalizes: false
    canCommit: false
    dataClassesTouched: ["[…]"]
endpoint: { transport: "[…]", address: "[…]" }
mutualAuthMechanism: "[Espacio para rellenar]"
mutualAuthVerified: false
identityRef: "[URI opaca]"
owner: "[Espacio para rellenar]"
platformCustodian: "[Espacio para rellenar]"
dependsOn: []
lifecycleStatus: "[propuesto | activo | deprecated | retirado]"
coherenceReview: { status: "[pendiente | aprobado | rechazado]", reviewedAgainst: "[…]", date: "[YYYY-MM-DD]" }
```

---

*Plantilla de descriptor de identidad de agente de Myrmion Federation — versión 1.0. Parte del corpus normativo. Espejo socrático del [Esquema de Identidad de Agente](../../docs/federation/esquema-identidad-agente.md). Ver también el [Glosario de la Federación](../../docs/federation/glosario-federacion.md) y el [ejemplo rellenado](./descriptor-agente-ejemplo.md).*
