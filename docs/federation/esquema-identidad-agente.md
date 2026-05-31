# Myrmion Federation — Esquema de identidad de agente

**Versión 1.0**

*El contrato del descriptor de identidad que cada agente departamental publica para registrarse en la federación y ser descubierto por otros agentes. Materializa la capa §3.1 del [manifiesto](./manifesto.md). Este documento define el contrato — qué campos, con qué semántica y con qué reglas de validación; la [plantilla socrática](../../templates/federation/descriptor-agente.md) es la que rellena cada organización, y el [ejemplo del corredor](../../examples/federation/corredor-comercial-legal/) muestra descriptores reales.*

---

## 1. Qué es el descriptor y qué no es

El descriptor es lo que permite que el agente legal y el de marketing se descubran y se entiendan **sin coordinación humana previa** (manifiesto §3.1). Declara quién es el agente, qué dominio cubre, qué criticidad tiene, qué clases de dato maneja y a qué versión de la Constitución se adhiere.

**El descriptor es un contrato, no una serialización.** Este documento define los campos y su semántica; el YAML y el JSON Schema de abajo son representaciones ilustrativas. Cómo se almacena el descriptor en un service registry concreto, o cómo se firma, es responsabilidad del stack y vive en [`appendix/stacks-referencia/`](./appendix/stacks-referencia/), no aquí (ver [regla anti-acoplamiento](./regla-anti-acoplamiento.md) §4).

**No incluye** secretos, claves privadas ni configuración de despliegue. La identidad criptográfica del agente se referencia (`identityRef`), no se incrusta.

---

## 2. El identificador: `agentId`

`agentId` es la clave estable y no reutilizable del agente. Forma:

```
urn:myrmion:agent:<org>:<dominio>:<nombre>
```

- `myrmion:agent` es el namespace del framework (fijo).
- **`<org>` es un token de namespace que elige la organización adoptante.** El framework **nunca** lo fija ni asume un valor concreto: es una variable de la organización (registrada en su [Perfil de Adopción](./perfil-adopcion-federacion.md)). En los ejemplos del corpus se usa un valor ficticio (`consultora-modelo`); en una adopción real es el identificador corto de la organización.
- `<dominio>` es el dominio departamental (`comercial`, `legal`, `finanzas`, `personas`…), alineado con la Capa Departamental de la que el agente deriva.
- `<nombre>` distingue agentes dentro de un mismo dominio.

**No reutilizable:** cuando un agente se retira, su `agentId` queda archivado, nunca se reasigna a otro agente (ver [runbook de retirada](../../templates/federation/runbook-retirada-agente.md)). Esto preserva la integridad de las cadenas de decisión históricas, que referencian agentes por `agentId`.

---

## 3. Campos del descriptor

`R` = requerido · `C` = condicional · `O` = opcional. Los tipos son lógicos; su serialización concreta es del stack.

| Campo | Req. | Tipo | Descripción |
|---|---|---|---|
| `schemaVersion` | R | string (semver) | Versión de **este** esquema que el descriptor cumple. Permite evolucionar el contrato sin romper agentes antiguos. |
| `agentId` | R | URN | Identificador estable y no reutilizable (§2). |
| `displayName` | R | string | Nombre legible para humanos (dashboards, auditoría). |
| `domain` | R | string | Dominio departamental. Vocabulario alineado con las Capas Departamentales de Adoption. |
| `departmentLayerRef` | R | objeto `{docId, version, hash}` | Referencia a la Capa Departamental de la que el agente deriva, con su versión y `hash` (ver §6). |
| `constitutionRef` | R | objeto `{version, approvalDate, hash}` | Versión de la Constitución Corporativa que el agente aplica, con su `hash`. |
| `regulatoryFrameworkRef` | R | objeto `{version, hash}` | Versión del Marco Regulatorio del que hereda. La incompatibilidad de Marco es **dura** (no hay excepción posible). |
| `compatibleConstitutionHashes` | R | array de hashes | Conjunto de hashes de Constitución que este agente reconoce como compatibles con el suyo. Es lo que habilita la **validación de compatibilidad en O(1)** (§7) sin re-parsear la Constitución. |
| `criticality` | R | enum `{baja, media, alta, critica}` | Criticidad del dominio. Modula la cadencia de revisión de drift y la severidad del gate de coherencia. |
| `dataClasses` | R | array de enum | Clases de dato que el agente maneja, con el vocabulario que defina el Marco Regulatorio de la organización (p. ej. `C0..C4`). |
| `capabilities` | R | array de `Capability` | Qué tools expone el agente y sus propiedades de gobernanza (§4). |
| `endpoint` | R | objeto `{transport, address}` | Dónde se invoca. `transport` es un descriptor abstracto del protocolo (p. ej. `mcp`); el binding concreto vive en [`appendix/mapeo-transporte/`](./appendix/mapeo-transporte/). |
| `mutualAuthMechanism` | R | string | Nombre del mecanismo de autenticación mutua que el agente soporta. **Campo libre, no enum**: el cuerpo no privilegia ningún mecanismo (ver [CF-04](./criterios-funcionales.md)). |
| `mutualAuthVerified` | R | bool | Si el registry ha verificado que el mecanismo declarado satisface las 3 propiedades de identidad criptográfica de CF-04. |
| `identityRef` | R | URI opaca | Referencia a la identidad criptográfica del agente en el IdP. No asume un IdP central ni un formato concreto. |
| `owner` | R | string (rol) | Custodio de dominio responsable del contenido cultural del agente (el departamento). |
| `platformCustodian` | R | string (rol) | El 4º custodio: la plataforma de federación responsable del registro y del stack (ver [gobernanza](./gobernanza-federada.md)). |
| `dependsOn` | O | array de `agentId` | Agentes de los que este depende. Habilita la notificación en cascada al retirar un agente. |
| `lifecycleStatus` | R | enum `{propuesto, activo, deprecated, retirado}` | Estado en el ciclo de vida (§8). |
| `coherenceReview` | R | objeto `{status, reviewedAgainst, date}` | Resultado del gate de coherencia. `status ∈ {pendiente, aprobado, rechazado}`. **El alta en el registry falla si `status != aprobado`** (manifiesto §5). `reviewedAgainst` es la versión del set de policy templates contra el que se revisó. |

### 4. El sub-objeto `Capability`

Cada entrada de `capabilities` describe una tool que el agente expone, con las propiedades que el policy engine necesita para decidir **sin introspección de runtime**:

| Campo | Req. | Tipo | Descripción |
|---|---|---|---|
| `toolName` | R | string | Nombre de la tool. |
| `sideEffectClass` | R | enum `{lectura, escritura, comunicacion-externa, compromiso}` | Clase de efecto. Permite a las policies razonar por categoría, no por tool concreta. |
| `externalizes` | R | bool | Si la tool puede sacar información fuera del dominio/organización. Disparador típico de policies de externalización (p. ej. cifras financieras). |
| `canCommit` | R | bool | Si la tool puede generar un compromiso contractual. Disparador típico de la policy «no asumimos compromisos sin pasar por legal». |
| `dataClassesTouched` | R | array de enum | Clases de dato que la tool toca. Disparador de las policies de des-identificación (CF-06). |

`externalizes` y `canCommit` son **abstracciones decidibles en tiempo de diseño**: las declara quien modela el agente, no se infieren en runtime. Es lo que permite que el [gate de coherencia](./gobernanza-federada.md) evalúe el descriptor antes de que el agente se registre.

---

## 5. Representación ilustrativa (no normativa)

El contrato es la tabla de §3–§4. Este YAML solo ilustra la forma:

```yaml
schemaVersion: "1.0"
agentId: "urn:myrmion:agent:consultora-modelo:legal:dictamenes"
displayName: "Agente Legal — Dictámenes"
domain: "legal"
departmentLayerRef: { docId: "capa-legal", version: "2.1", hash: "sha256:…" }
constitutionRef: { version: "3.0", approvalDate: "2026-01-15", hash: "sha256:…" }
regulatoryFrameworkRef: { version: "1.4", hash: "sha256:…" }
compatibleConstitutionHashes: ["sha256:…", "sha256:…"]
criticality: "alta"
dataClasses: ["C1", "C2", "C3"]
capabilities:
  - toolName: "emitir_dictamen"
    sideEffectClass: "escritura"
    externalizes: false
    canCommit: false
    dataClassesTouched: ["C2", "C3"]
endpoint: { transport: "mcp", address: "…" }
mutualAuthMechanism: "mtls"
mutualAuthVerified: true
identityRef: "spiffe://… (u otra URI opaca)"
owner: "Dirección de Asesoría Jurídica"
platformCustodian: "Plataforma de Federación"
dependsOn: []
lifecycleStatus: "activo"
coherenceReview: { status: "aprobado", reviewedAgainst: "policies@2026-02", date: "2026-02-10" }
```

> El JSON Schema derivado de este contrato se publica junto al esquema para validación automática (round-trip de verificación). Los `*.agente.yaml` del [ejemplo del corredor](../../examples/federation/corredor-comercial-legal/) validan contra él.

---

## 6. Contrato de hash

Los campos `hash` (de `constitutionRef`, `departmentLayerRef`, `regulatoryFrameworkRef`) y el conjunto `compatibleConstitutionHashes` solo son interoperables entre implementaciones si todas calculan el hash igual. El contrato:

```
hash = "sha256:" + SHA-256( forma_canónica(documento) )
```

**Forma canónica** del documento de gobernanza (Constitución, Capa, Marco):

1. Codificación UTF-8, normalización Unicode **NFC**.
2. Saltos de línea **LF** (`\n`), sin CR.
3. Trailing whitespace eliminado en cada línea; fichero termina en un único `\n`.
4. **Se excluye del hash la sección «0. Metadatos»** (versión, fecha de aprobación, custodios…), porque es volátil y no forma parte del contenido cultural. El hash captura *lo que dice* el documento, no su cabecera administrativa.

Sin este contrato, la «comparación de hashes» que el manifiesto §9 da por trivial no funciona entre dos implementaciones distintas. El [ejemplo](../../examples/federation/corredor-comercial-legal/) incluye una recomputación de hash como prueba.

---

## 7. Validación de compatibilidad

Cuando un agente recibe una llamada (ver [esquema del bloque de contexto cultural](./esquema-bloque-contexto-cultural.md)), compara el `constitutionHash` que trae el emisor contra su propio `compatibleConstitutionHashes`:

- **Hay match** → la versión de Constitución del emisor es compatible; la llamada procede (sujeta a policy).
- **No hay match** → la llamada **no procede**. La política por defecto es **escalado a humano** con el bloque de contexto completo como evidencia (manifiesto §3.2). Permitir la llamada con criterios desfasados sería la antítesis del framework.

La comparación es O(1) (pertenencia a un conjunto de hashes), no requiere re-parsear ni re-evaluar la Constitución. La incompatibilidad de `regulatoryFrameworkRef` es **siempre dura**: el Marco Regulatorio no admite excepciones (Adoption §4).

---

## 8. Ciclo de vida y registro

`lifecycleStatus` recorre: `propuesto` → (gate de coherencia) → `activo` → `deprecated` → `retirado`.

- **Alta:** el agente se propone con su descriptor; el [gate de coherencia](./gobernanza-federada.md) evalúa `capabilities` contra los policy templates derivados de la Constitución. Si pasa, `coherenceReview.status = aprobado` y el agente entra en el registry como `activo`. Si no, el alta falla. Detalle operativo en el [runbook de onboarding](../../templates/federation/runbook-onboarding-agente.md).
- **Actualización:** un cambio en `capabilities`, `constitutionRef` o `dataClasses` re-dispara el gate de coherencia.
- **Retirada:** ver [runbook de retirada](../../templates/federation/runbook-retirada-agente.md) — deregister, revocar `identityRef`, archivar el descriptor y el histórico, y notificar a los agentes que lo tienen en `dependsOn`. El `agentId` queda archivado, no liberado.

---

## 9. Qué deja agnóstico (y dónde vive lo concreto)

| Decisión concreta | Dónde vive |
|---|---|
| Formato de serialización en el registry, firma del descriptor | [`appendix/stacks-referencia/`](./appendix/stacks-referencia/) |
| Binding de `endpoint.transport` a un protocolo concreto | [`appendix/mapeo-transporte/`](./appendix/mapeo-transporte/) |
| Mecanismo concreto de `mutualAuthMechanism` (mTLS, identidad federada…) | `appendix/stacks-referencia/` |
| Formato de `identityRef` (SPIFFE u otro) | `appendix/stacks-referencia/` |

El descriptor declara *qué* información expone el agente y *qué* propiedades cumple; *cómo* se materializa cada una es del stack.

---

*Esquema de identidad de agente de Myrmion Federation — versión 1.0. Parte del corpus normativo. Su plantilla socrática es [descriptor-agente.md](../../templates/federation/descriptor-agente.md); su contraparte en runtime es el [bloque de contexto cultural](./esquema-bloque-contexto-cultural.md).*
