<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Runbook de alta de un agente

**Versión 1.0**

*Plantilla operativa para dar de alta un agente departamental en la federación: del descriptor al registro, pasando por el gate de coherencia. Materializa la revisión de coherencia programática del [manifiesto](../../docs/federation/manifesto.md) §5, ejecuta las seis comprobaciones definidas en [gobernanza-federada.md](../../docs/federation/gobernanza-federada.md) §2, y opera la transición de `lifecycleStatus` `propuesto → activo` del [esquema de identidad](../../docs/federation/esquema-identidad-agente.md) §8.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

Este runbook documenta el alta de **un** agente departamental en la federación: la secuencia desde que existe un descriptor candidato hasta que el agente queda registrado en el service registry con `lifecycleStatus` en `activo`. No es una guía conceptual — es un procedimiento con checklist accionable que un operador de la plataforma de federación (el cuarto custodio) ejecuta paso a paso.

**Qué fija el cuerpo y qué fija este runbook.** El gate de coherencia es **contrato normativo**: sus seis comprobaciones, su atomicidad y su carácter bloqueante están definidos en [gobernanza-federada.md](../../docs/federation/gobernanza-federada.md) §2, y este runbook **no los renegocia** — los *ejecuta* sobre el stack concreto. Lo que el runbook aporta es la operacionalización paso a paso, la checklist y la tabla de remediación. Donde runbook y cuerpo discrepen, prevalece el cuerpo.

**Quién lo instancia y quién lo ejecuta.** La plantilla la instancia el equipo de plataforma de federación una sola vez, adaptándola a su stack (ver [charter de la plataforma](./charter-plataforma-federacion.md)). A partir de ahí, **cada alta** produce una instancia rellena de las secciones de ejecución, que se archiva como evidencia del alta — igual que un descriptor o el registro de excepciones se versionan.

**Por qué un runbook y no un script.** El alta cruza tres custodias: el departamento que modeló el agente (custodio de dominio, `owner`), la transformación digital que custodia la Constitución, y la plataforma que custodia el stack (`platformCustodian`). Partes del procedimiento se automatizan en el pipeline de alta; otras son decisiones humanas que no se delegan. El runbook marca cuáles son cuáles.

**El principio que no se negocia.** El gate es **bloqueante y atómico**: o pasan las seis comprobaciones, o el agente **no se registra**. No hay alta «con observaciones» ni alta parcial (gobernanza-federada §2). Saltarse una comprobación «porque urge» es meter en la falange un agente cuyo comportamiento no está verificado contra la Constitución. La política por defecto ante cualquier fallo es **no registrar y devolver a la custodia responsable**, nunca registrar provisionalmente.

**Cuánto tiempo lleva.** El primer alta de una organización lleva días, porque se está estrenando el pipeline. A partir del tercer o cuarto agente, un alta limpia es cuestión de horas: el descriptor ya viene bien formado, las comprobaciones están automatizadas, y el gate o pasa o señala exactamente qué falla.

**Frecuencia de revisión de este runbook.** Cada vez que cambie el stack subyacente (porque las comprobaciones se materializan distinto), cuando cambie el conjunto de comprobaciones del gate en gobernanza-federada.md, y revisión ordinaria semestral.

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Organización | *(nombre de la organización que opera la federación)* |
| Versión del documento | *(p. ej. 1.0, 1.1)* |
| Fecha de aprobación | *(YYYY-MM-DD)* |
| Próxima revisión programada | *(YYYY-MM-DD)* |
| Custodio del runbook | *(rol — típicamente responsable de la plataforma de federación)* |
| Stack sobre el que se ejecuta | *(referencia a la entrada del apéndice de stacks de referencia que la organización adoptó)* |
| Versión de la Constitución Corporativa vigente | *(`hash` y versión legible de la Constitución contra la que se evalúa el gate)* |

---

## 1. Identificación del alta

*Antes de tocar el service registry, fija de qué alta estamos hablando. Un alta sin un caso de colaboración detrás es un agente zombi en potencia: se registra, nadie lo invoca, y meses después el sistema lo sigue arrastrando.*

### 1.1 Agente que se da de alta

*Pregunta guía: ¿qué agente departamental se está incorporando? Nombre legible (`displayName`), departamento de origen, y `agentId` propuesto en forma de URN (`urn:myrmion:agent:<org>:<dominio>:<nombre>`). El `agentId` no se reutiliza nunca: si coincide con uno archivado de un agente retirado, el alta se detiene aquí (lo verifica la comprobación 1 del gate, §3.1).*

[Espacio para rellenar]

### 1.2 Quién impulsa el alta y quién la autoriza

*Pregunta guía: ¿qué departamento modeló este agente (el `owner`, custodio de su capa departamental) y quién, dentro de la plataforma de federación (el `platformCustodian`), autoriza ejecutar el alta? Ambos firman el descriptor; nombrar a las personas evita que el gate se ejecute sin que nadie se haga responsable del resultado.*

[Espacio para rellenar]

### 1.3 Qué colaboración justifica el alta

*Pregunta guía: ¿qué corredor o corredores va a servir este agente? ¿Con qué agentes va a colaborar, en qué casos de negocio (`businessCaseId`), con qué frecuencia? Si la respuesta es «aún no se sabe», el alta es prematura: Federation se justifica por fricción real en handovers, no por completitud del catálogo (manifiesto §6, Fase 4).*

[Espacio para rellenar]

---

## 2. Preparación del descriptor

*El descriptor es la entrada del gate. Un descriptor mal formado no «se arregla en el registro»: se devuelve al departamento. Esta sección verifica que el descriptor está completo y que sus hashes están recalculados antes de someterlo a comprobación.*

### 2.1 Descriptor candidato

*Pregunta guía: ¿dónde vive el descriptor candidato y a qué `schemaVersion` del [esquema de identidad](../../docs/federation/esquema-identidad-agente.md) se ajusta? Debe ser una instancia de la [plantilla de descriptor](./descriptor-agente.md), no un documento ad hoc. Al proponer el alta, su `lifecycleStatus` es `propuesto` y su `coherenceReview.status` es `pendiente`. Referenciar el artefacto concreto que entra al gate.*

[Espacio para rellenar]

### 2.2 Verificación de campos requeridos

*Pregunta guía: ¿están presentes y bien formados los campos requeridos sin los cuales el descubrimiento federado no funciona? Esta verificación previa anticipa la comprobación 1 del gate; cualquier ausencia detiene el alta antes de someterlo. Marcar cada campo como presente/ausente.*

| Campo del descriptor | Presente | Bien formado | Observaciones |
|---|---|---|---|
| `agentId` (URN) | ☐ | ☐ | |
| `domain` | ☐ | ☐ | |
| `criticality` | ☐ | ☐ | |
| `dataClasses` | ☐ | ☐ | |
| `capabilities` (con `sideEffectClass`, `externalizes`, `canCommit`, `dataClassesTouched`) | ☐ | ☐ | |
| `constitutionRef` | ☐ | ☐ | |
| `regulatoryFrameworkRef` | ☐ | ☐ | |
| `compatibleConstitutionHashes` | ☐ | ☐ | |
| `mutualAuthMechanism` / `mutualAuthVerified` | ☐ | ☐ | |
| `coherenceReview` (`status = pendiente` al proponer) | ☐ | ☐ | |

### 2.3 Hashes recalculados

*Pregunta guía: ¿se han recalculado los `hash` de `constitutionRef`, `departmentLayerRef` y `regulatoryFrameworkRef`, y el conjunto `compatibleConstitutionHashes`, según el contrato de hash (`"sha256:"` sobre la forma canónica del documento de gobernanza — UTF-8 NFC, saltos LF, sin trailing whitespace y **excluyendo la sección «0. Metadatos»**)? Sin hashes correctos, las comprobaciones 2 y 4 del gate fallan. Registrar el valor obtenido para cada referencia.*

[Espacio para rellenar]

---

## 3. Gate de coherencia — las seis comprobaciones

*Aquí está el corazón del alta. El gate de coherencia es la versión programática de la revisión de coherencia de Adoption (manifiesto §5): la revisión deja de ser un juicio humano en lectura cruzada y se convierte en seis comprobaciones programáticas reproducibles. Las seis están **definidas en [gobernanza-federada.md](../../docs/federation/gobernanza-federada.md) §2.1** y este runbook las ejecuta en ese orden. El gate es **bloqueante y atómico**: el alta procede solo si las seis devuelven verdadero; si cualquiera falla, el alta falla y no hay registro parcial.*

*Para cada comprobación: resultado (pasa / falla), evidencia, y — si falla — la acción de §4 que se dispara.*

### 3.1 Comprobación 1 — Descriptor válido contra el esquema

*Pregunta guía: ¿el descriptor valida contra el contrato del [esquema de identidad](../../docs/federation/esquema-identidad-agente.md) — campos requeridos presentes, tipos correctos, `agentId` con forma `urn:myrmion:agent:<org>:<dominio>:<nombre>` y **no reutilizado** (ni en el registry activo ni en el histórico archivado de agentes retirados)? Falla si el descriptor está incompleto, malformado o reusa un `agentId` archivado.*

| Sub-comprobación | Resultado | Evidencia |
|---|---|---|
| Valida contra el esquema (campos y tipos) | ☐ pasa ☐ falla | |
| `agentId` con forma URN canónica | ☐ pasa ☐ falla | |
| `agentId` no reutilizado (registry activo + archivo) | ☐ pasa ☐ falla | |

### 3.2 Comprobación 2 — `constitutionRef` vigente

*Pregunta guía: ¿el `hash` de `constitutionRef` que el agente declara aplicar resuelve a una versión de Constitución **publicada y vigente** según el custodio de la Constitución — no a un borrador, una versión retirada ni un hash desconocido? La comprobación usa el contrato de hash, no una comparación de cadenas de versión. Falla si el `hash` no resuelve a una versión vigente: un agente adherido a una Constitución que ya no existe es un agente a la deriva.*

| Sub-comprobación | Resultado | Evidencia |
|---|---|---|
| `constitutionRef.hash` resuelve a versión vigente | ☐ pasa ☐ falla | |

### 3.3 Comprobación 3 — `capabilities` sin efectos que la Constitución prohíbe

*Pregunta guía: ¿alguna `Capability` declarada, por sus propiedades de gobernanza (`sideEffectClass`, `externalizes`, `canCommit`, `dataClassesTouched`), declara un efecto que la Constitución veta de forma absoluta — p. ej. `externalizes: true` sobre cifras financieras sin paso por finanzas, o `canCommit: true` sin paso por legal? El conflicto es estructural y no se resuelve en runtime. Falla si alguna capability declara un efecto que ningún contexto haría admisible. Esta es la comprobación que da nombre al gate y la materialización exacta de la frase del manifiesto §5: «si un agente declara capacidades que entran en conflicto con la Constitución, el alta falla».*

| Sub-comprobación | Resultado | Evidencia |
|---|---|---|
| Ninguna `capability` declara un efecto vetado de forma absoluta | ☐ pasa ☐ falla | |

### 3.4 Comprobación 4 — `dataClasses` coherentes con el Marco Regulatorio

*Pregunta guía: ¿las `dataClasses` que el agente declara manejar son un subconjunto de las que el Marco Regulatorio (`regulatoryFrameworkRef`) permite a su dominio, y para cada clase sensible (PII/PHI y las que el Marco defina) las capabilities que la tocan (`dataClassesTouched`) tienen disponible la des-identificación en la ruta ([CF-06](../../docs/federation/criterios-funcionales.md))? Falla si el agente declara una clase de dato que el Marco no autoriza a su dominio, o una clase sensible sin cobertura de des-identificación. Una discrepancia aquí no es excepcionable: es materia del Marco.*

| Sub-comprobación | Resultado | Evidencia |
|---|---|---|
| `dataClasses` ⊆ clases autorizadas por el Marco a este dominio | ☐ pasa ☐ falla | |
| Cobertura de des-identificación en la ruta para clases sensibles | ☐ pasa ☐ falla | |

### 3.5 Comprobación 5 — `mutualAuthVerified = true`

*Pregunta guía: ¿está emitida y verificada la identidad criptográfica del agente según las tres propiedades de [CF-04](../../docs/federation/criterios-funcionales.md) — el receptor puede verificar criptográficamente la identidad del emisor antes de ejecutar, la credencial es de vida corta y revocable, y es vinculable de forma estable al `agentId`? El descriptor lo refleja con `mutualAuthVerified = true` (el `mutualAuthMechanism` concreto es campo libre y no se privilegia ninguno). Falla si la autenticación mutua con identidad criptográfica verificable no está establecida. El cuerpo nunca exige «mTLS» por su nombre: exige estas tres propiedades.*

| Sub-comprobación | Resultado | Evidencia |
|---|---|---|
| Identidad verificable por el receptor antes de ejecutar | ☐ pasa ☐ falla | |
| Credencial de vida corta y revocable | ☐ pasa ☐ falla | |
| Identidad vinculable de forma estable al `agentId` | ☐ pasa ☐ falla | |
| `mutualAuthVerified = true` en el descriptor | ☐ pasa ☐ falla | |

### 3.6 Comprobación 6 — `coherenceReview.status` reproducible

*Pregunta guía: ¿el resultado del propio gate se sella en el descriptor como `coherenceReview = {status, reviewedAgainst, date}`, con el conjunto de policy templates aplicados y su versión en `reviewedAgainst`; y ese resultado es **reproducible** — volver a ejecutar el gate sobre el mismo descriptor y el mismo estado de Constitución produce el mismo `status`? El alta solo procede con `coherenceReview.status = aprobado`. Falla si el resultado no es reproducible (p. ej. depende de algo no versionado). La reproducibilidad es lo que convierte el gate en evidencia auditable, no en un sello opaco: cualquiera puede re-verificar por qué un agente entró.*

| Sub-comprobación | Resultado | Evidencia |
|---|---|---|
| `coherenceReview` sellado con `{status, reviewedAgainst, date}` | ☐ pasa ☐ falla | |
| Resultado reproducible (re-ejecución produce el mismo `status`) | ☐ pasa ☐ falla | |
| `coherenceReview.status = aprobado` | ☐ pasa ☐ falla | |

### 3.7 Veredicto del gate

*Pregunta guía: ¿pasaron las seis comprobaciones? El gate es atómico. Anotar el veredicto global y, si es FALLA, qué comprobación(es) fallaron y qué acción de §4 se dispara. Solo con veredicto PASA se avanza a §5.*

| Resultado global del gate | Comprobaciones fallidas | Acción disparada |
|---|---|---|
| ☐ PASA ☐ FALLA | | |

---

## 4. Qué hacer si el gate falla

*Un fallo del gate no es un error a silenciar: es información de gobernanza. La regla general es **no registrar y devolver a la custodia responsable** del fallo. Esta sección fija la acción por comprobación. La organización adapta los responsables, pero la política por defecto — no registrar — no se negocia, y el alta no avanza hasta que el gate pasa completo en una nueva ejecución.*

### 4.1 Tabla de remediación por comprobación

*Pregunta guía: para cada comprobación que puede fallar, ¿a quién se devuelve, qué se corrige, y quién re-ejecuta el gate?*

| Comprobación fallida | Custodia que recibe el fallo | Remediación típica |
|---|---|---|
| 1 — Descriptor válido / `agentId` único | Departamento (`owner`) + plataforma | Corregir el descriptor contra el esquema; reasignar `<nombre>` en el URN — **nunca** reutilizar un `agentId` archivado |
| 2 — `constitutionRef` vigente | Transformación digital | Actualizar el agente a la Constitución vigente y recalcular el `hash` antes de reintentar |
| 3 — `capabilities` vs Constitución | Transformación digital + departamento | Retirar/ajustar la capability cuyo efecto está vetado; si la organización decide registrar pese al conflicto, tramitar excepción documentada (§4.2) |
| 4 — `dataClasses` vs Marco | DPO / legal + plataforma | Reducir las `dataClasses` declaradas a las autorizadas, o añadir des-identificación en la ruta del corredor. **No excepcionable**: es materia del Marco |
| 5 — `mutualAuthVerified` | Plataforma de federación | Provisionar credenciales con las tres propiedades de CF-04 y verificarlas antes de reintentar |
| 6 — `coherenceReview` reproducible | Plataforma de federación | Eliminar la dependencia no versionada que rompe la reproducibilidad; re-sellar `coherenceReview` |

### 4.2 La excepción no es atajo

*Pregunta guía: si la organización decide registrar un agente pese a un conflicto de la comprobación 3 (Constitución), ¿queda registrado como excepción con justificación, alcance temporal y autorizador en el [registro de excepciones](./registro-excepciones.md)? Una excepción es una decisión consciente que deja rastro, no un bypass silencioso. Recordatorio dado en gobernanza-federada §3: un conflicto con el **Marco** (comprobación 4) **no admite excepción** — es una alerta al custodio del Marco y un incidente, no una excepción.*

[Espacio para rellenar]

### 4.3 Escalado

*Pregunta guía: ¿cuándo un fallo del gate escala a humano más allá de la remediación rutinaria? Por ejemplo, cuando el fallo revela que la Constitución y la realidad del departamento han divergido — eso no se arregla en el descriptor: dispara revisión de la Constitución o de las policies derivadas (manifiesto §5, §6 Fase 4). Articular el umbral y a quién escala.*

[Espacio para rellenar]

---

## 5. Registro y activación

*Solo se llega aquí con el gate en PASA y `coherenceReview.status = aprobado`. Esta sección documenta el alta efectiva en el service registry y la transición de `lifecycleStatus` de `propuesto` a `activo` ([esquema de identidad](../../docs/federation/esquema-identidad-agente.md) §8).*

### 5.1 Alta en el service registry

*Pregunta guía: ¿se ha registrado el descriptor — con sus hashes y su identidad criptográfica (`identityRef`) vinculada al `agentId` — en el service registry ([CF-02](../../docs/federation/criterios-funcionales.md)), de forma que otros agentes lo descubran con su descriptor extendido (dominio, criticidad, versión de Constitución aplicada)? Registrar el momento del alta y la evidencia.*

[Espacio para rellenar]

### 5.2 Transición `lifecycleStatus`: `propuesto` → `activo`

*Pregunta guía: ¿se ha cambiado el `lifecycleStatus` de `propuesto` a `activo`? Este cambio es el acto que autoriza al agente a recibir y emitir llamadas en corredores reales; antes de él, el agente existe en el catálogo pero no opera. Anotar quién ejecuta la transición y cuándo.*

| Estado anterior | Estado nuevo | Quién ejecuta la transición | Fecha/hora |
|---|---|---|---|
| `propuesto` | `activo` | | |

### 5.3 Verificación post-activación

*Pregunta guía: ¿se ha probado al menos una invocación real del corredor que justificó el alta (§1.3), comprobando que el [bloque de contexto cultural](../../docs/federation/esquema-bloque-contexto-cultural.md) viaja, que la validación de compatibilidad (`constitutionHash` ∈ `compatibleConstitutionHashes`) pasa en el agente receptor, que la cadena de decisiones se reconstruye desde el `correlationId`, y que cualquier dato sensible viaja como `deidToken`? Un agente «activo» que nunca ha completado un salto real no está verificado en producción.*

[Espacio para rellenar]

---

## 6. Cierre del alta

*El alta no termina en la activación: termina cuando queda registrada como evidencia y los demás custodios lo saben.*

### 6.1 Archivado de la evidencia del alta

*Pregunta guía: ¿se archiva esta instancia rellena del runbook — con el veredicto del gate, los hashes del descriptor y el registro de la transición `propuesto → activo` — junto al descriptor del agente? Esta evidencia es lo que permite, meses después, reconstruir bajo qué Constitución y con qué comprobaciones entró el agente a la federación.*

[Espacio para rellenar]

### 6.2 Notificación a corredores y custodias

*Pregunta guía: ¿se ha notificado el alta a los agentes y departamentos que van a colaborar con el nuevo agente, y a las custodias afectadas (Constitución y, si el agente maneja datos sensibles, el DPO)? El alta de un agente que sirve un corredor afecta al otro extremo del corredor; que se entere por la primera llamada en producción es mala operación.*

[Espacio para rellenar]

### 6.3 Checklist final del alta

*Pregunta guía: ¿se cierran todos los puntos antes de dar el alta por terminada? Esta checklist es el resumen accionable del runbook completo.*

- [ ] Agente identificado con corredor y caso de negocio que lo justifican (§1)
- [ ] Descriptor candidato completo, con `lifecycleStatus: propuesto`, `coherenceReview.status: pendiente` y hashes recalculados (§2)
- [ ] Gate de coherencia: las seis comprobaciones en PASA, veredicto atómico (§3)
- [ ] Si hubo fallo: remediado y gate re-ejecutado completo — o, solo para la comprobación 3, excepción registrada (§4)
- [ ] Descriptor registrado en el service registry con `identityRef` vinculada al `agentId` (§5.1)
- [ ] `lifecycleStatus` cambiado de `propuesto` a `activo` (§5.2)
- [ ] Invocación real del corredor verificada en producción (§5.3)
- [ ] Evidencia del alta archivada junto al descriptor (§6.1)
- [ ] Corredores y custodias notificados (§6.2)

---

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Runbook de alta de un agente — parte del corpus normativo de Myrmion Federation, versión 1.0. Operacionaliza el [gate de coherencia](../../docs/federation/gobernanza-federada.md) §2 (cuya definición normativa no renegocia) y la transición de `lifecycleStatus` del [esquema de identidad](../../docs/federation/esquema-identidad-agente.md) §8. Toma de entrada el descriptor de la [plantilla de descriptor](./descriptor-agente.md); el alta en el service registry responde a [CF-02](../../docs/federation/criterios-funcionales.md). Donde runbook y cuerpo discrepen, prevalece el cuerpo.*

*Para ver un alta completa rellenada como referencia orientativa, consultar el [ejemplo](./runbook-onboarding-agente-ejemplo.md).*

**Relacionados:** [manifiesto](../../docs/federation/manifesto.md) §5 · [gobernanza federada](../../docs/federation/gobernanza-federada.md) §2 · [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md) · [esquema del bloque de contexto cultural](../../docs/federation/esquema-bloque-contexto-cultural.md) · [criterios funcionales](../../docs/federation/criterios-funcionales.md) · [glosario](../../docs/federation/glosario-federacion.md) · plantillas: [descriptor de agente](./descriptor-agente.md) · [charter de la plataforma](./charter-plataforma-federacion.md) · [registro de excepciones](./registro-excepciones.md) · [runbook de retirada](./runbook-retirada-agente.md)
