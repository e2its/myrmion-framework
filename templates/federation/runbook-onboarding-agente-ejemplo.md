<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Runbook de alta de un agente (ejemplo)

**Versión 1.0**

*Ejemplo rellenado de la [plantilla de runbook de alta](./runbook-onboarding-agente.md), instanciado para Consultora Modelo S.L. Documenta el alta del agente Legal (`...:legal:dictamenes`) que va a servir el corredor comercial→legal. Es referencia orientativa, no normativa: la organización real rellena su propia instancia.*

</td>
</tr>
</table>

---

> **Ejemplo no normativo.** **Consultora Modelo S.L.** (`<org>` = `consultora-modelo`) y las personas que aparecen son ficticias. Ya tiene un agente Comercial activo en la federación; este runbook documenta el alta del agente Legal, que entra para sustituir el handover manual entre **Fonseca** (Comercial) y **Riera** (Legal) cuando una propuesta sobre un lead necesita validación jurídica antes de comprometer a la organización. Los hashes están abreviados con `…` y las fechas son ilustrativas. Este es el mismo agente Legal que ilustra el [ejemplo de descriptor](./descriptor-agente-ejemplo.md).

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Organización | Consultora Modelo S.L. |
| Versión del documento | 1.0 |
| Fecha de aprobación | 2026-02-10 |
| Próxima revisión programada | 2026-08-10 |
| Custodio del runbook | Responsable de Plataforma de Federación |
| Stack sobre el que se ejecuta | Gateway MCP + policy engine declarativo + service registry federado seleccionados en Fase 1 (ver la entrada del apéndice de stacks adoptada por la organización) |
| Versión de la Constitución Corporativa vigente | `sha256:a3f5…` (Constitución v3.0, aprobada 2026-01-15) |

---

## 1. Identificación del alta

### 1.1 Agente que se da de alta

Agente **Legal — Dictámenes** de Consultora Modelo S.L. Departamento de origen: Asesoría Jurídica. `agentId` propuesto:

```
urn:myrmion:agent:consultora-modelo:legal:dictamenes
```

Se ha verificado que este URN no existe en el registry activo ni en el histórico archivado de agentes retirados. Es un alta nueva, no la sustitución de un agente retirado.

### 1.2 Quién impulsa el alta y quién la autoriza

- **Custodio de dominio (`owner`):** Dirección de Asesoría Jurídica, con **Riera** como responsable (modeló la Capa Departamental Legal de la que deriva el agente).
- **Co-firma de coherencia constitucional:** Dirección de Transformación Digital, custodio de la Constitución.
- **Custodio de plataforma (`platformCustodian`) que autoriza la ejecución del alta:** Plataforma de Federación.

### 1.3 Qué colaboración justifica el alta

Corredor **comercial→legal**. El agente Comercial (`urn:myrmion:agent:consultora-modelo:comercial:propuestas`, ya activo) necesita, antes de comprometer a la organización en una propuesta sobre un lead, un dictamen jurídico. Hoy ese handover lo hacen Fonseca y Riera por correo: Fonseca resume la propuesta, Riera la revisa y devuelve un dictamen, Fonseca lo interpreta. Es exactamente la fricción de bisagra que justifica federar este par (manifiesto §1). Frecuencia observada en la baseline pre-federación: entre tres y seis handovers de este tipo por semana. El `businessCaseId` típico es el del lead (p. ej. `lead-2026-0042`).

---

## 2. Preparación del descriptor

### 2.1 Descriptor candidato

Descriptor candidato: instancia de la [plantilla de descriptor](./descriptor-agente.md), `schemaVersion` 1.0, `version` 1.0.0, conforme al [esquema de identidad](../../docs/federation/esquema-identidad-agente.md). Es el mismo artefacto que ilustra el [ejemplo de descriptor](./descriptor-agente-ejemplo.md). Al proponer el alta, su `lifecycleStatus` es `propuesto` y su `coherenceReview.status` es `pendiente`.

### 2.2 Verificación de campos requeridos

| Campo del descriptor | Presente | Bien formado | Observaciones |
|---|---|---|---|
| `agentId` (URN) | ☑ | ☑ | `urn:myrmion:agent:consultora-modelo:legal:dictamenes` |
| `domain` | ☑ | ☑ | `legal` |
| `criticality` | ☑ | ☑ | `alta` — el dominio puede condicionar compromisos contractuales |
| `dataClasses` | ☑ | ☑ | `["C2", "C3"]` (confidencial de cliente/contraparte; términos contractuales) |
| `capabilities` (con `sideEffectClass`, `externalizes`, `canCommit`, `dataClassesTouched`) | ☑ | ☑ | `emitir_dictamen`: `escritura`, `externalizes: false`, `canCommit: false`, `dataClassesTouched: [C2, C3]` |
| `constitutionRef` | ☑ | ☑ | v3.0, `hash: sha256:a3f5…` |
| `regulatoryFrameworkRef` | ☑ | ☑ | v1.4, `hash: sha256:f0a1…` |
| `compatibleConstitutionHashes` | ☑ | ☑ | `[sha256:a3f5…, sha256:b7e2…]` |
| `mutualAuthMechanism` / `mutualAuthVerified` | ☑ | ☑ | mecanismo de autenticación mutua con identidad criptográfica verificable; `mutualAuthVerified: true` |
| `coherenceReview` (`status = pendiente` al proponer) | ☑ | ☑ | `status: pendiente` hasta que pase el gate |

### 2.3 Hashes recalculados

Recalculados el 2026-02-10 según el contrato de hash (UTF-8 NFC, saltos LF, sin trailing whitespace, excluyendo la sección «0. Metadatos»):

- `departmentLayerRef.hash` (Capa Legal v2.1): `sha256:c1d2…`
- `constitutionRef.hash` (Constitución v3.0): `sha256:a3f5…`
- `regulatoryFrameworkRef.hash` (Marco v1.4): `sha256:f0a1…`
- `compatibleConstitutionHashes`: `[sha256:a3f5… (v3.0 vigente), sha256:b7e2… (v2.x, cadenas abiertas)]`

---

## 3. Gate de coherencia — las seis comprobaciones

*Las seis comprobaciones se ejecutan en el orden definido en [gobernanza-federada.md](../../docs/federation/gobernanza-federada.md) §2.1. El gate es atómico.*

### 3.1 Comprobación 1 — Descriptor válido contra el esquema

| Sub-comprobación | Resultado | Evidencia |
|---|---|---|
| Valida contra el esquema (campos y tipos) | ☑ pasa | Validación automática contra `schemaVersion` 1.0: 0 errores |
| `agentId` con forma URN canónica | ☑ pasa | `urn:myrmion:agent:consultora-modelo:legal:dictamenes` |
| `agentId` no reutilizado (registry activo + archivo) | ☑ pasa | Sin coincidencia en el registry activo ni en el archivo de retirados |

### 3.2 Comprobación 2 — `constitutionRef` vigente

| Sub-comprobación | Resultado | Evidencia |
|---|---|---|
| `constitutionRef.hash` resuelve a versión vigente | ☑ pasa | `sha256:a3f5…` resuelve a la Constitución v3.0, vigente según Transformación Digital |

### 3.3 Comprobación 3 — `capabilities` sin efectos que la Constitución prohíbe

| Sub-comprobación | Resultado | Evidencia |
|---|---|---|
| Ninguna `capability` declara un efecto vetado de forma absoluta | ☑ pasa | `emitir_dictamen` declara `externalizes: false` y `canCommit: false`; no dispara el veto de externalización de cifras ni el de compromiso sin paso por legal |

*Nota del operador: la comprobación 3 confirmó algo esperado. Este agente es precisamente el **destino** que el policy template «no asumimos compromisos sin pasar por legal» exige en el corredor comercial→legal. Que declare `canCommit: false` es lo correcto: el dictamen habilita o bloquea un compromiso futuro, no lo formaliza. Su alta es lo que hace ejecutable esa policy de extremo a extremo.*

### 3.4 Comprobación 4 — `dataClasses` coherentes con el Marco Regulatorio

| Sub-comprobación | Resultado | Evidencia |
|---|---|---|
| `dataClasses` ⊆ clases autorizadas por el Marco a este dominio | ☑ pasa | `[C2, C3]` están dentro de lo que el Marco v1.4 autoriza al dominio legal; no declara PHI |
| Cobertura de des-identificación en la ruta para clases sensibles | ☑ pasa | El corredor comercial→legal tiene des-identificación en la ruta: la PII de cliente se tokeniza antes de cruzar al dominio legal, con `deidToken` reversible para re-identificar el dictamen final en el agente de origen |

### 3.5 Comprobación 5 — `mutualAuthVerified = true`

| Sub-comprobación | Resultado | Evidencia |
|---|---|---|
| Identidad verificable por el receptor antes de ejecutar | ☑ pasa | El agente Comercial verifica la identidad de este agente antes de ejecutar; probado en pre-producción |
| Credencial de vida corta y revocable | ☑ pasa | TTL de credencial: 1 h; revocación verificada |
| Identidad vinculable de forma estable al `agentId` | ☑ pasa | `identityRef` (URI opaca al IdP) vinculada al `agentId` |
| `mutualAuthVerified = true` en el descriptor | ☑ pasa | El registry confirmó las tres propiedades |

### 3.6 Comprobación 6 — `coherenceReview.status` reproducible

| Sub-comprobación | Resultado | Evidencia |
|---|---|---|
| `coherenceReview` sellado con `{status, reviewedAgainst, date}` | ☑ pasa | `{status: aprobado, reviewedAgainst: "policies@2026-02", date: "2026-02-10"}` |
| Resultado reproducible (re-ejecución produce el mismo `status`) | ☑ pasa | Re-ejecución del gate sobre el mismo descriptor y el mismo estado de Constitución produce `aprobado` |
| `coherenceReview.status = aprobado` | ☑ pasa | `aprobado` |

### 3.7 Veredicto del gate

| Resultado global del gate | Comprobaciones fallidas | Acción disparada |
|---|---|---|
| ☑ PASA | Ninguna | Avanzar a §5 (registro y activación) |

---

## 4. Qué hacer si el gate falla

*En este alta el gate pasó completo, así que esta sección no disparó remediación. Se documenta de todos modos la decisión que se tomó sobre un caso límite que apareció durante la preparación, como evidencia de gobernanza.*

### 4.1 Tabla de remediación por comprobación

No aplicable en este alta: las seis comprobaciones pasaron en la primera ejecución del gate.

### 4.2 La excepción no es atajo

Durante la preparación se valoró si el agente debía poder, en casos urgentes, emitir un dictamen sin que la cadena de decisiones registrase el `correlationId` del lead de origen. Se rechazó: habría roto la trazabilidad que justifica el corredor. **No se tramitó excepción** porque no había conflicto real con la comprobación 3; se ajustó el modelado del agente para que el `correlationId` sea obligatorio en `emitir_dictamen`. Si en el futuro un caso exigiera registrar el agente pese a un conflicto de la comprobación 3 (Constitución), se anotaría en el [registro de excepciones](./registro-excepciones.md) con justificación, alcance temporal y autorizador. Un conflicto de la comprobación 4 (Marco) no se excepcionaría: sería alerta e incidente.

### 4.3 Escalado

No hubo escalado en este alta. Criterio acordado: si el gate hubiera fallado la comprobación 2 (`constitutionRef` vigente) revelando que la Capa Departamental Legal aplicaba una versión de Constitución anterior a la vigente, no se habría parcheado el descriptor — se habría escalado a Transformación Digital para actualizar la capa y recalcular el `hash` antes de reintentar.

---

## 5. Registro y activación

### 5.1 Alta en el service registry

El descriptor, con sus hashes y la identidad criptográfica (`identityRef`) vinculada al `agentId`, se registró en el service registry el 2026-02-10. Desde ese momento el agente Comercial puede descubrir al agente Legal con su descriptor extendido (dominio `legal`, criticidad `alta`, Constitución v3.0).

### 5.2 Transición `lifecycleStatus`: `propuesto` → `activo`

| Estado anterior | Estado nuevo | Quién ejecuta la transición | Fecha/hora |
|---|---|---|---|
| `propuesto` | `activo` | Responsable de Plataforma de Federación | 2026-02-10 |

### 5.3 Verificación post-activación

Se ejecutó una invocación real del corredor comercial→legal con un lead de prueba marcado como tal (`businessCaseId: lead-2026-0042`). Resultado:

- El [bloque de contexto cultural](../../docs/federation/esquema-bloque-contexto-cultural.md) viajó completo: `correlationId`, `businessCaseId`, `constitutionHash` del Comercial y la `decisionChain` con el salto previo.
- La **validación de compatibilidad** pasó en el agente Legal: el `constitutionHash` que aplicó el Comercial (v3.0, `sha256:a3f5…`) está entre los `compatibleConstitutionHashes` del Legal.
- La cadena de decisiones se reconstruyó desde el `correlationId`: salto 1 (Comercial, `calificar_lead`, `criteriaApplied: [pol-calificacion-lead@1.2, pol-dlp-pii@2.0]`, `outcome: redactado`) → salto 2 (Legal, `validar_clausula`, `outcome: permitido`).
- La PII del cliente llegó tokenizada al dominio legal; el dictamen final se re-identificó en el agente Comercial vía `deidToken`.

El agente queda verificado en producción, no solo activo en el catálogo.

---

## 6. Cierre del alta

### 6.1 Archivado de la evidencia del alta

Esta instancia rellena del runbook se archivó junto al descriptor del agente Legal en el repositorio de gobernanza de Consultora Modelo S.L., con el veredicto del gate (PASA), los hashes del descriptor y el registro de la transición `propuesto → activo`. Permite reconstruir, en cualquier auditoría futura, que el agente entró bajo la Constitución v3.0 (`sha256:a3f5…`) habiendo pasado las seis comprobaciones.

### 6.2 Notificación a corredores y custodias

Se notificó el alta a:

- **Fonseca (Comercial)** y al equipo que opera el agente Comercial, otro extremo del corredor.
- **Dirección de Transformación Digital**, custodia de la Constitución.
- **DPO**, por la participación del agente en una ruta que maneja PII de cliente.

### 6.3 Checklist final del alta

- [x] Agente identificado con corredor y caso de negocio que lo justifican (§1)
- [x] Descriptor candidato completo, con `lifecycleStatus: propuesto`, `coherenceReview.status: pendiente` y hashes recalculados (§2)
- [x] Gate de coherencia: las seis comprobaciones en PASA, veredicto atómico (§3)
- [x] Si hubo fallo: remediado y gate re-ejecutado — o excepción registrada (§4) *(no hubo fallo)*
- [x] Descriptor registrado en el service registry con `identityRef` vinculada al `agentId` (§5.1)
- [x] `lifecycleStatus` cambiado de `propuesto` a `activo` (§5.2)
- [x] Invocación real del corredor verificada en producción (§5.3)
- [x] Evidencia del alta archivada junto al descriptor (§6.1)
- [x] Corredores y custodias notificados (§6.2)

---

*Ejemplo del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Ejemplo orientativo de la [plantilla de runbook de alta de un agente](./runbook-onboarding-agente.md), versión 1.0. Consultora Modelo S.L., Fonseca, Riera y los hashes son ficticios. El gate de coherencia que se ejecuta está definido en [gobernanza-federada.md](../../docs/federation/gobernanza-federada.md) §2; el descriptor de este mismo agente está en el [ejemplo de descriptor](./descriptor-agente-ejemplo.md).*
