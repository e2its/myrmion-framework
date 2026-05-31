<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Plantilla del Bloque de Contexto Cultural

**Versión 1.0**

*Guía de implementación del bloque de contexto cultural — el sobre de metadatos de runtime que viaja en cada llamada inter-agente. Espejo operativo del [esquema del bloque de contexto cultural](../../docs/federation/esquema-bloque-contexto-cultural.md), que materializa la Capa de propagación de contexto cultural del [manifiesto](../../docs/federation/manifesto.md) §3.2.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

A diferencia de las plantillas de Adoption, esta **no es un documento que se rellena a mano** como una constitución o una capa departamental. El bloque de contexto cultural es un **artefacto de runtime**: lo construye el agente en código, en cada salto, no una persona en una sesión de trabajo. Por eso esta plantilla no te pide que escribas el bloque, sino que **decidas y documentes las políticas de implementación** que tu equipo de plataforma (el cuarto custodio) debe fijar para que el bloque se construya, valide y propague igual en toda la federación.

Trabaja siempre con el contrato delante: [`esquema-bloque-contexto-cultural.md`](../../docs/federation/esquema-bloque-contexto-cultural.md). Esta plantilla es su espejo operativo, no su sustituto. Si hay discrepancia entre lo que aquí decides y lo que el esquema exige, **manda el esquema**: el esquema es el contrato, esto es la política de cómo lo cumples.

**Quién la rellena.** La plataforma de federación (manifiesto §5, [glosario](../../docs/federation/glosario-federacion.md): «cuarto custodio»). Las decisiones sobre truncamiento, `compatibilityPolicy` y manejo de `deidToken` son transversales: si cada equipo de agente las toma por su cuenta, la cadena de decisiones deja de ser comparable y el análisis de drift (Patrón A) se vuelve imposible.

**Cómo se rellena.** Responde cada *pregunta guía* en prosa y sustituye cada `[Espacio para rellenar]`. No borres las preguntas: son el método. Donde una decisión sea binaria (escalar/rechazar, truncar/no truncar), declárala explícitamente y justifícala — el esquema dice «la política se declara, no se improvisa».

**Qué NO se decide aquí.** Cómo viaja el bloque sobre el cable. Eso es transporte, vive en [`appendix/mapeo-transporte/`](../../docs/federation/appendix/mapeo-transporte/) y esta plantilla solo declara a qué mapeo te adhieres (§8). Acoplar la política al transporte rompe la portabilidad a A2A que promete el manifiesto §9.

**Qué se hace después.** La política rellena se versiona, se firma por la plataforma de federación y se incorpora a la gobernanza. Los agentes que construyen el bloque la implementan; el gate de coherencia y el gateway la hacen cumplir.

Para ver el bloque construido sobre un caso real, consulta el fichero hermano [`bloque-contexto-cultural-ejemplo.md`](./bloque-contexto-cultural-ejemplo.md) y el flujo completo en [`examples/federation/corredor-comercial-legal/`](../../examples/federation/corredor-comercial-legal/).

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Organización | *(nombre y `<org>` del agentId, p. ej. `consultora-modelo`)* |
| Custodio (plataforma de federación) | *(equipo de plataforma o SRE)* |
| `schemaVersion` del bloque que esta política soporta | *(p. ej. 1.0)* |
| Versión del documento | *(p. ej. 1.0)* |
| Fecha de aprobación | *(YYYY-MM-DD)* |
| Próxima revisión programada | *(YYYY-MM-DD)* |

---

## 1. Campos a poblar en cada salto

El bloque envuelve la llamada, no la sustituye: viaja **junto a** los argumentos de la tool. Cada agente que emite un salto debe poblar los campos del contrato (§2 del esquema). Esta sección documenta **de dónde saca tu implementación cada valor** y qué hereda del salto anterior sin tocarlo.

*Pregunta guía: para cada campo, ¿es heredado del salto previo (y por tanto inmutable en esta llamada) o lo genera/actualiza este salto? ¿De qué fuente de tu stack sale el valor?*

| Campo del contrato | ¿Heredado o nuevo en este salto? | Fuente en tu implementación |
|---|---|---|
| `schemaVersion` | Constante de plataforma | [Espacio para rellenar] |
| `correlationId` | **Heredado** — lo origina el `hopCount = 1` y nunca se regenera | [Espacio para rellenar] |
| `businessCaseId` | Heredado (origen de la cadena) | [Espacio para rellenar] |
| `constitutionHash` | **Nuevo** — la versión que *este* emisor aplicó | [Espacio para rellenar] |
| `regulatoryFrameworkHash` | Nuevo — el Marco que este emisor aplicó | [Espacio para rellenar] |
| `departmentLayerHash` | Nuevo — capa departamental de la que deriva este emisor | [Espacio para rellenar] |
| `originatingUserRef` | Heredado (seudónimo opaco; ausente si la cadena la inició el sistema) | [Espacio para rellenar] |
| `hopCount` | Heredado + **se incrementa** en este salto | [Espacio para rellenar] |
| `decisionChain` | Heredada + se le **añade** este `DecisionHop` | [Espacio para rellenar] |
| `deidTokens` | Heredados y/o ampliados (§6) | [Espacio para rellenar] |
| `compatibilityPolicy` | Política de plataforma (§5) | [Espacio para rellenar] |
| `escalationContext` | Solo si la cadena se rompe | [Espacio para rellenar] |

*Pregunta guía: ¿cómo garantiza tu implementación que `constitutionHash`, `regulatoryFrameworkHash` y `departmentLayerHash` se calculan con el [contrato de hash](../../docs/federation/esquema-identidad-agente.md#6-contrato-de-hash) (sha256 sobre forma canónica, excluyendo metadatos) y no con un hash improvisado que no case con el del descriptor de identidad?*

[Espacio para rellenar]

---

## 2. Identidad y correlación

`correlationId` traza la cadena de decisiones completa de extremo a extremo. **Persiste sin cambios** desde el primer salto al último y **nunca se regenera** dentro de una cadena (esquema §6, regla 2). Es la clave que hace trivial la trazabilidad y la que alimenta los Patrones A/B de drift.

*Pregunta guía: ¿cómo genera tu agente originador (`hopCount = 1`) el `correlationId`, y cómo garantizas que ningún salto posterior lo regenera, lo modifica o crea uno nuevo para la misma cadena?*

[Espacio para rellenar]

*Pregunta guía: ¿qué hace un agente receptor si recibe un bloque sin `correlationId`, con un `correlationId` mal formado, o con un `hopCount` que no encaja con la longitud de la `decisionChain`? ¿Lo rechaza, lo registra como anomalía de integridad?*

[Espacio para rellenar]

---

## 3. businessCaseId y contexto del caso

`businessCaseId` identifica el caso de negocio que origina la cadena (el lead, el expediente, el ticket) y agrupa todas las cadenas que sirven a un mismo asunto. Es la unidad de negocio sobre la que se razona a posteriori.

*Pregunta guía: ¿qué convención de identificador usa tu organización para `businessCaseId` (formato, sistema de origen) y cómo garantizas que es estable durante toda la vida del caso, aunque la cadena salte entre dominios?*

[Espacio para rellenar]

*Pregunta guía: ¿cómo evitas que el `businessCaseId` filtre por sí mismo información sensible (p. ej. un identificador que sea a la vez el NIF del cliente)? Recuerda la regla de privacidad por construcción (esquema §6.1).*

[Espacio para rellenar]

---

## 4. decisionChain: política de la cadena de decisiones

`decisionChain` es **append-only**: cada agente añade su `DecisionHop` (`agentId`, `toolInvoked`, `constitutionHashApplied`, `criteriaApplied`, `outcome`, `timestamp`) sin modificar los eslabones anteriores. Es obligatoria cuando `hopCount > 1` (esquema §2, §3).

*Pregunta guía: ¿cómo garantiza tu implementación que ningún agente reescribe `DecisionHop` previos y que el orden y los `timestamp` son coherentes con `hopCount`?*

[Espacio para rellenar]

*Pregunta guía: la convención de `criteriaApplied` distingue criterio automatizado (`policyId@version`) del literal `"juicio-de-modelo-no-automatizable"`. ¿Cómo se asegura tu agente de registrar ambos honestamente, sin disfrazar un juicio del modelo como si fuera una policy ejecutada? (Es lo que hace analizable el Patrón A.)*

[Espacio para rellenar]

*Pregunta guía: ¿qué nivel de detalle pones en cada `DecisionHop`? ¿Cómo evitas que `toolInvoked` o `criteriaApplied` filtren PII o secretos de negocio en claro (esquema §6.1)?*

[Espacio para rellenar]

### 4.1 Política de truncamiento

La cadena crece en cada salto. En cadenas largas, el bloque puede superar los límites prácticos del transporte. El esquema (§6.3) permite truncar `decisionChain` a los últimos N saltos **más un `chainDigest`** (hash de los eslabones omitidos), de modo que la cadena completa siga siendo verificable sin transportarla entera. La política de truncamiento **se declara, no se improvisa**.

*Pregunta guía: ¿tu política trunca la `decisionChain`? Si sí, ¿bajo qué criterio (N saltos, antigüedad, tamaño del bloque) y cuál es el valor de N?*

[Espacio para rellenar]

*Pregunta guía: ¿cómo calculas el `chainDigest` de los eslabones omitidos para que la cadena truncada siga siendo verificable contra la cadena completa archivada por la observabilidad agent-aware ([CF-05](../../docs/federation/criterios-funcionales.md))? ¿Dónde queda archivada la cadena completa antes de truncar?*

[Espacio para rellenar]

*Pregunta guía: ¿qué se preserva siempre, pase lo que pase (p. ej. el primer salto / originador y el último)? ¿Cómo señala el bloque que ha habido truncamiento, para no aparentar una cadena completa que no lo es?*

[Espacio para rellenar]

---

## 5. compatibilityPolicy: escalar o rechazar

Al recibir el bloque, el agente B valida que el `constitutionHash` del emisor está entre sus `compatibleConstitutionHashes` (esquema §4). Si **no hay match**, la llamada no procede y se aplica `compatibilityPolicy`. El esquema fija el enum `{escalar, rechazar}` y el default del framework (`escalar`, a humano); una organización **puede endurecer a `rechazar`, nunca relajar a `permitir`**. La incompatibilidad de `regulatoryFrameworkHash` es **dura**: no admite excepción.

*Pregunta guía: ¿tu organización mantiene el default `escalar` (a humano, con el bloque completo como evidencia en `escalationContext`) o lo endurece a `rechazar`? Justifica la elección por criticidad del dominio.*

[Espacio para rellenar]

*Pregunta guía: cuando se escala por incompatibilidad de Constitución, ¿qué pones en `escalationContext` (motivo, agente que escala, evidencia) y quién es el humano que lo recibe? Conéctalo con tu [registro de excepciones](./registro-excepciones.md).*

[Espacio para rellenar]

*Pregunta guía: ante una incompatibilidad de `regulatoryFrameworkHash` (dura, sin excepción), ¿qué comportamiento garantizas? Recuerda: una «excepción» al Marco no es una excepción, es una alerta.*

[Espacio para rellenar]

| Situación | Decisión (escalar / rechazar) | Comportamiento concreto |
|---|---|---|
| `constitutionHash` incompatible | [Espacio para rellenar] | [Espacio para rellenar] |
| `regulatoryFrameworkHash` incompatible | *(dura: no procede, alerta)* | [Espacio para rellenar] |
| `schemaVersion` desconocida | [Espacio para rellenar] | [Espacio para rellenar] |
| Bloque sin `decisionChain` con `hopCount > 1` | [Espacio para rellenar] | [Espacio para rellenar] |

---

## 6. deidTokens: manejo de identificadores deidentificados

Cuando la des-identificación en la ruta ([CF-06](../../docs/federation/criterios-funcionales.md)) redacta un dato **de forma reversible**, emite un `DeidToken` (`token`, `scope`, `ttl`) que el bloque transporta. **Regla dura: el `deidToken` nunca contiene el valor original** — es un puntero a un vault gestionado por el stack; el valor solo se recupera **en el agente de origen**, dentro del `ttl` (esquema §5). Cuando la redacción es irreversible, no hay token.

*Pregunta guía: ¿dónde vive el vault que respalda los `deidToken`, quién puede resolverlos y cómo garantizas que solo el agente de origen (dentro del `scope` y el `ttl`) re-identifica? ¿Qué `ttl` por defecto fija tu política y por qué?*

[Espacio para rellenar]

*Pregunta guía: ¿qué hace un agente intermedio con un `deidToken` que no puede resolver (no está en su `scope`)? Confírmalo: debe poder **propagar y correlacionar sin re-identificar**, nunca exigir el valor en claro.*

[Espacio para rellenar]

*Pregunta guía: cuando la redacción es irreversible (no hay token), ¿cómo se asegura tu implementación de que el dato no aparece de ninguna otra forma en el bloque (ni en `businessCaseId`, ni en `criteriaApplied`, ni en `originatingUserRef`)?*

[Espacio para rellenar]

---

## 7. Reglas de privacidad aplicadas

El esquema (§6.1) fija que el bloque **no contiene PII directa**: viaja en cada llamada y se exporta a observabilidad. `originatingUserRef` es un seudónimo opaco; los datos sensibles son `deidToken` (punteros), nunca valores. Toda implementación cruza obligatoriamente la [Guía de protección de datos](../../docs/adoption/guia-proteccion-datos.md). Esta sección documenta **cómo lo hace cumplir tu plataforma**.

*Pregunta guía: ¿qué control automático impide que un bloque con PII directa se emita o se propague (validación en el agente, en el gateway [CF-01](../../docs/federation/criterios-funcionales.md), o en ambos)? ¿Es una validación de esquema, un escáner de PII, una revisión?*

[Espacio para rellenar]

*Pregunta guía: ¿cómo se genera `originatingUserRef` como seudónimo opaco estable y no reversible fuera del origen autorizado? ¿Cómo garantizas que es **ausente** y no vacío ni placeholder cuando la cadena la inicia el sistema?*

[Espacio para rellenar]

---

## 8. Mapeo a transporte — desacoplable

> **Esta sección es desacoplable → ver [`appendix/mapeo-transporte/`](../../docs/federation/appendix/mapeo-transporte/).** El bloque es un contrato de datos, no una serialización. Cómo viaja sobre el cable (clave de metadatos, header, atributo de traza) **no se fija aquí**: es responsabilidad del gateway y vive en el apéndice. Esto preserva la portabilidad a A2A (esquema §6.4, [regla anti-acoplamiento](../../docs/federation/regla-anti-acoplamiento.md) §4).

No documentes el transporte concreto en esta plantilla. Aquí solo declaras **a qué mapeo del apéndice te adhieres**, para que la política sea trazable sin acoplar tu agente a un transporte.

*Pregunta guía: ¿a qué mapeo de transporte del apéndice se adhiere tu implementación, y qué versión de ese mapeo?*

[Espacio para rellenar]

*Pregunta guía: si mañana cambias de transporte (o portas a A2A), ¿qué de lo que has rellenado en las secciones 1–7 tendría que cambiar? La respuesta correcta debería ser: nada. Si cambia algo, has acoplado el contrato al transporte.*

[Espacio para rellenar]

---

## 9. Validación al recibir el bloque

Al recibir el bloque, el agente B ejecuta la validación de compatibilidad (esquema §4) antes de actuar. Esta sección documenta **dónde y cuándo** la ejecuta tu plataforma.

*Pregunta guía: ¿en qué punto valida tu agente el bloque entrante (en el gateway [CF-01](../../docs/federation/criterios-funcionales.md), en el propio agente, en ambos)? Lista las comprobaciones mínimas: `schemaVersion` reconocida, `correlationId` presente, `hopCount` coherente con `decisionChain`, `constitutionHash` contra `compatibleConstitutionHashes`, `deidToken` sin valores en claro.*

[Espacio para rellenar]

*Pregunta guía: ante un fallo de validación, ¿qué hace tu agente: rechaza, registra, alerta? ¿Cómo se distingue un fallo de compatibilidad (que aplica `compatibilityPolicy`) de un fallo de integridad del bloque (bloque malformado)?*

[Espacio para rellenar]

---

*Plantilla del Bloque de Contexto Cultural de Myrmion Federation — versión 1.0. Parte del corpus normativo. Su contrato es el [esquema del bloque de contexto cultural](../../docs/federation/esquema-bloque-contexto-cultural.md); su ejemplo rellenado es [bloque-contexto-cultural-ejemplo.md](./bloque-contexto-cultural-ejemplo.md); el transporte vive en [`appendix/mapeo-transporte/`](../../docs/federation/appendix/mapeo-transporte/).*

*Relacionado: [esquema del bloque](../../docs/federation/esquema-bloque-contexto-cultural.md) · [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md) · [criterios funcionales](../../docs/federation/criterios-funcionales.md) · [regla anti-acoplamiento](../../docs/federation/regla-anti-acoplamiento.md) · [registro de excepciones](./registro-excepciones.md) · [ejemplo del corredor](../../examples/federation/corredor-comercial-legal/) · [Manifiesto de Federation](../../docs/federation/manifesto.md)*
