<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Ejemplo de Descriptor de Identidad de Agente

**Versión 1.0**

*La [plantilla de descriptor de agente](./descriptor-agente.md) rellenada para el agente legal de Consultora Modelo S.L. Materializa, sobre un caso concreto, el contrato del [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md).*

</td>
</tr>
</table>

---

> **Ejemplo no normativo.** La organización **Consultora Modelo S.L.** (`<org>` = `consultora-modelo`) y las personas que aparecen son ficticias. Este documento ilustra cómo se rellena la [plantilla de descriptor de agente](./descriptor-agente.md). Los hashes están abreviados con `…`.

Consultora Modelo S.L. está federando sus agentes departamentales. Su caso de referencia es el **corredor comercial → legal**: el agente comercial de **Fonseca** traslada una propuesta sobre un lead al agente legal de **Riera** para que emita un dictamen antes de comprometer a la organización. Este documento declara el **lado legal** de ese corredor: el agente que emite los dictámenes.

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Departamento al que pertenece el agente | Legal |
| `agentId` del agente declarado | `urn:myrmion:agent:consultora-modelo:legal:dictamenes` |
| `schemaVersion` (versión del esquema que cumple) | 1.0 |
| `version` del descriptor | 1.0.0 |
| Fecha de última revisión | 2026-05-01 |
| Custodio de dominio (`owner`) | Dirección de Asesoría Jurídica (Riera) |
| Custodio de plataforma (`platformCustodian`) | Plataforma de Federación |
| Estado | Aprobado |

---

## 1. Identificación del agente

### 1.1 `agentId`

*Pregunta guía: ¿cuál es el identificador único global de tu agente?*

`urn:myrmion:agent:consultora-modelo:legal:dictamenes`

El `<org>` es `consultora-modelo` (identificador corto de Consultora Modelo S.L.), el `<dominio>` es `legal` y el `<nombre>` es `dictamenes`. Es único en la federación: no existe otro agente del dominio legal cuyo nombre sea `dictamenes`. Si algún día se retira, este `agentId` quedará archivado para no romper las cadenas de decisión históricas que lo referencian.

### 1.2 `displayName`

*Pregunta guía: ¿cómo debe verse el nombre cuando lo lea una persona?*

Agente Legal — Dictámenes

### 1.3 `domain`

*Pregunta guía: ¿qué dominio departamental gobierna?*

`legal`

Gobierna exclusivamente el dominio legal, alineado con la Capa Departamental Legal de Consultora Modelo. No emite ofertas comerciales ni firma en nombre del área comercial: cuando recibe el corredor de Fonseca, actúa solo sobre la dimensión jurídica de la propuesta.

### 1.4 `version` y `schemaVersion`

*Pregunta guía: ¿cuál es la `version` del descriptor y qué `schemaVersion` cumple?*

- `version`: `1.0.0`. Primera versión estable. Se incrementará `MINOR` al añadir capacidades compatibles, `MAJOR` ante un cambio de dominio o de identidad, y `PATCH` ante un cambio de la Constitución aplicada que no altere las capacidades (que además actualiza `constitutionRef`).
- `schemaVersion`: `1.0`. Cumple la versión 1.0 del esquema de identidad de agente.

### 1.5 `criticality`

*Pregunta guía: ¿cuál es la criticidad del dominio?*

`alta`

El dominio legal puede generar compromisos vinculantes para la organización; un dictamen erróneo tiene consecuencias contractuales. Esto justifica `alta`, lo que endurece la cadencia de revisión de drift y la severidad del gate de coherencia. No se declara `critica` porque ningún dictamen se externaliza ni se ejecuta sin revisión, según se ve en las capacidades.

---

## 2. Herencia de gobernanza

### 2.1 `departmentLayerRef`

*Pregunta guía: ¿de qué Capa Departamental deriva, en qué versión y con qué hash?*

```yaml
departmentLayerRef: { docId: "capa-legal", version: "2.1", hash: "sha256:c1d2…" }
```

Deriva de la Capa Departamental Legal de Consultora Modelo, versión 2.1. El `hash` se calculó sobre su forma canónica, excluyendo la sección «0. Metadatos».

### 2.2 `constitutionRef`

*Pregunta guía: ¿qué versión de la Constitución Corporativa aplica?*

```yaml
constitutionRef: { version: "3.0", approvalDate: "2026-01-15", hash: "sha256:a3f5…" }
```

Aplica la Constitución Corporativa 3.0, aprobada el 2026-01-15. El `hash` `sha256:a3f5…` se recalculó el 2026-05-01 tras la última edición de la Constitución.

### 2.3 `regulatoryFrameworkRef`

*Pregunta guía: ¿de qué versión del Marco Regulatorio hereda?*

```yaml
regulatoryFrameworkRef: { version: "1.4", hash: "sha256:f0a1…" }
```

Hereda del Marco Regulatorio 1.4, la versión vigente. La compatibilidad de Marco es dura: si una llamada entrante declarara una versión de Marco distinta, no procedería bajo ninguna excepción.

### 2.4 `compatibleConstitutionHashes`

*Pregunta guía: ¿qué hashes de Constitución reconoce como compatibles?*

```yaml
compatibleConstitutionHashes: ["sha256:a3f5…", "sha256:b7e2…"]
```

- `sha256:a3f5…` — la Constitución vigente (3.0).
- `sha256:b7e2…` — la versión anterior (2.x), aún en uso por cadenas de decisión abiertas antes de la actualización a 3.0; se declara compatible para que esas cadenas sigan considerándose culturalmente coherentes hasta su cierre. Cuando una llamada de Fonseca llegue con cualquiera de estos dos hashes, la validación de compatibilidad da match y la llamada procede (sujeta a policy); con cualquier otro, se escala a humano con el bloque de contexto completo como evidencia.

---

## 3. Capacidades

*Pregunta guía general: ¿qué tools expone tu agente a la federación?*

El agente expone una única tool pública: `emitir_dictamen`. Es la capacidad que el agente comercial de Fonseca invoca en el corredor comercial → legal.

### 3.1 Capacidad: `emitir_dictamen`

#### `toolName`

*Pregunta guía: ¿cuál es el nombre de esta tool?*

`emitir_dictamen`

#### `sideEffectClass`

*Pregunta guía: ¿qué clase de efecto tiene?*

`escritura`

Deja constancia interna del dictamen emitido (modifica el estado del dominio legal), pero no produce comunicación externa ni un compromiso por sí misma. Por eso es `escritura` y no `comunicacion-externa` ni `compromiso`.

#### `externalizes`

*Pregunta guía: ¿puede sacar información fuera del dominio o de la organización?*

`false`

El dictamen se devuelve al agente solicitante dentro de la federación; la tool no publica datos hacia sistemas externos a la organización.

#### `canCommit`

*Pregunta guía: ¿puede generar un compromiso contractual?*

`false`

El dictamen *habilita o bloquea* un futuro compromiso, pero no lo formaliza: la tool no firma ni contrata. El compromiso contractual lo ejecuta otra capacidad (de otro agente o con intervención humana) una vez el dictamen es favorable. Declararlo `false` es lo que permite que la policy «no asumimos compromisos sin pasar por legal» se concentre en las tools que sí comprometen.

#### `dataClassesTouched`

*Pregunta guía: ¿qué clases de dato toca?*

```yaml
dataClassesTouched: ["C2", "C3"]
```

Toca datos confidenciales de cliente/contraparte (`C2`) y términos contractuales sensibles de la propuesta (`C3`), según el vocabulario del Marco Regulatorio de Consultora Modelo. Los datos identificables que lleguen en el bloque de contexto se manejan deidentificados (con `deidToken`) según la política de protección de datos.

---

## 4. Endpoint e identidad criptográfica

### 4.1 `endpoint`

*Pregunta guía: ¿dónde se invoca este agente?*

```yaml
endpoint: { transport: "mcp", address: "…" }
```

El `transport` declarado es `mcp` como descriptor abstracto del protocolo base. El binding concreto a una dirección y el mapeo de transporte no se fijan en el descriptor.

### 4.2 `mutualAuthMechanism` y `mutualAuthVerified`

*Pregunta guía: ¿qué mecanismo de autenticación mutua soporta y está verificado?*

```yaml
mutualAuthMechanism: "autenticacion-mutua-identidad-criptografica"
mutualAuthVerified: true
```

El mecanismo declarado satisface las tres propiedades de autenticación mutua con identidad criptográfica verificable: el agente de Fonseca verifica criptográficamente la identidad de este agente antes de ejecutar, con credenciales de vida corta y revocables, vinculadas de forma estable al `agentId`. El registry ha verificado las tres propiedades, de ahí `mutualAuthVerified: true`.

### 4.3 `identityRef`

*Pregunta guía: ¿cuál es la referencia a la identidad criptográfica en el IdP?*

```yaml
identityRef: "… (URI opaca al IdP)"
```

Una URI opaca que apunta a la identidad del agente en el IdP de Consultora Modelo. No se incrusta clave ni secreto; el formato de la URI no asume un IdP concreto.

---

## 5. Custodios, dependencias y ciclo de vida

### 5.1 `owner` y `platformCustodian`

*Pregunta guía: ¿quién es el custodio de dominio y quién el de plataforma?*

```yaml
owner: "Dirección de Asesoría Jurídica"
platformCustodian: "Plataforma de Federación"
```

El `owner` es la Dirección de Asesoría Jurídica, con **Riera** como responsable; vela por el contenido cultural del agente. El `platformCustodian` es el equipo de Plataforma de Federación, el cuarto custodio, responsable del registro y del stack.

### 5.2 `dependsOn`

*Pregunta guía: ¿de qué otros agentes depende?*

```yaml
dependsOn: []
```

El agente legal no depende de otros agentes para emitir un dictamen: es un destino en el corredor, no un origen. Por eso `dependsOn` está vacío.

### 5.3 `lifecycleStatus`

*Pregunta guía: ¿en qué estado del ciclo de vida está?*

`activo`

Pasó el gate de coherencia y entró en el service registry como `activo`.

### 5.4 `coherenceReview`

*Pregunta guía: ¿cuál es el resultado del gate de coherencia?*

```yaml
coherenceReview: { status: "aprobado", reviewedAgainst: "policies@2026-02", date: "2026-02-10" }
```

El gate de coherencia evaluó las capacidades declaradas contra los policy templates derivados de la Constitución 3.0 (set `policies@2026-02`) el 2026-02-10, con resultado `aprobado`. La próxima revisión ordinaria la programa Riera como `owner`; cualquier cambio de Constitución, alta o baja de capacidad, o cambio de dominio dispara una revisión extraordinaria que vuelve a poner `status` en `pendiente`.

---

## 6. Composición del descriptor

*Pregunta guía: ¿puedes componer el descriptor en su forma serializable y validarlo contra el contrato?*

```yaml
schemaVersion: "1.0"
agentId: "urn:myrmion:agent:consultora-modelo:legal:dictamenes"
displayName: "Agente Legal — Dictámenes"
domain: "legal"
version: "1.0.0"
criticality: "alta"
departmentLayerRef: { docId: "capa-legal", version: "2.1", hash: "sha256:c1d2…" }
constitutionRef: { version: "3.0", approvalDate: "2026-01-15", hash: "sha256:a3f5…" }
regulatoryFrameworkRef: { version: "1.4", hash: "sha256:f0a1…" }
compatibleConstitutionHashes: ["sha256:a3f5…", "sha256:b7e2…"]
dataClasses: ["C2", "C3"]
capabilities:
  - toolName: "emitir_dictamen"
    sideEffectClass: "escritura"
    externalizes: false
    canCommit: false
    dataClassesTouched: ["C2", "C3"]
endpoint: { transport: "mcp", address: "…" }
mutualAuthMechanism: "autenticacion-mutua-identidad-criptografica"
mutualAuthVerified: true
identityRef: "… (URI opaca al IdP)"
owner: "Dirección de Asesoría Jurídica"
platformCustodian: "Plataforma de Federación"
dependsOn: []
lifecycleStatus: "activo"
coherenceReview: { status: "aprobado", reviewedAgainst: "policies@2026-02", date: "2026-02-10" }
```

Validación: el `agentId` sigue el formato URN canónico y es único; todos los campos requeridos están presentes y bien tipados; los `hash` siguen el contrato de hash; la capacidad `emitir_dictamen` declara `toolName`, `sideEffectClass`, `externalizes`, `canCommit` y `dataClassesTouched`; `version` y `schemaVersion` siguen semver; `coherenceReview.status` es `aprobado`, así que el agente puede estar `activo` en el registry. El descriptor es **válido**.

---

*Ejemplo de descriptor de identidad de agente de Myrmion Federation — versión 1.0. Parte del corpus normativo. Acompaña a la [plantilla de descriptor de agente](./descriptor-agente.md) y materializa el [Esquema de Identidad de Agente](../../docs/federation/esquema-identidad-agente.md).*
