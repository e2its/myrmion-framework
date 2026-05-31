# Myrmion Federation — Esquema del bloque de contexto cultural

**Versión 1.0**

*El contrato del bloque de metadatos que viaja en cada llamada inter-agente junto a los argumentos de la tool. Es «la pieza técnicamente más original del framework y la que ningún gateway opensource cubre por defecto» ([manifiesto](./manifesto.md) §3.2). Este documento define el **esquema** del bloque — qué viaja y con qué semántica. El **transporte** — cómo viaja por MCP u otro protocolo — vive en [`appendix/mapeo-transporte/`](./appendix/mapeo-transporte/), nunca aquí (ver [regla anti-acoplamiento](./regla-anti-acoplamiento.md) §4).*

---

## 1. Para qué sirve el bloque

Cuando el agente A invoca al agente B, lo que hoy viaja en las integraciones puntuales es solo la información operativa: el dato, la pregunta, el resultado. Lo que **no** viaja —y por eso B vuelve a aplicar criterios desde cero, a veces contradiciendo decisiones de upstream— es la cultura: qué versión de la Constitución aplicó A, qué caso de negocio, qué criterios ya se aplicaron, qué cadena de decisiones precede a esta llamada (manifiesto §1, §3.2).

El bloque de contexto cultural es lo que hace que esa cultura viaje. Es lo que distingue una falange de un grupo de mercenarios. Tres funciones:

1. **Propagar** la cultura aplicada (versión de Constitución, caso de negocio, criterios previos).
2. **Permitir validar compatibilidad** en el receptor antes de actuar (§4).
3. **Reconstruir la cadena de decisiones** trivialmente, a posteriori, vía `correlationId` — la trazabilidad que en Adoption requería trabajo forense.

---

## 2. Campos del bloque

`R` = requerido · `C` = condicional · `O` = opcional. Tipos lógicos; la serialización es transporte (apéndice).

| Campo | Req. | Tipo | Descripción |
|---|---|---|---|
| `schemaVersion` | R | string (semver) | Versión de **este** esquema que el bloque cumple. |
| `correlationId` | R | UUID | Identifica la cadena de decisiones completa. **Persiste sin cambios** desde el primer salto al último; **nunca se regenera** dentro de una cadena. Clave de reconstrucción y de los Patrones A/B de drift. |
| `businessCaseId` | R | string | Caso de negocio que origina la cadena (lead, expediente, ticket). Agrupa cadenas que sirven a un mismo asunto. |
| `constitutionHash` | R | hash | Hash de la versión de Constitución que el **emisor** aplicó (mismo [contrato de hash](./esquema-identidad-agente.md#6-contrato-de-hash)). Lo que el receptor valida (§4). |
| `regulatoryFrameworkHash` | R | hash | Hash del Marco Regulatorio que el emisor aplicó. La incompatibilidad de Marco es **dura**: no hay excepción. |
| `departmentLayerHash` | R | hash | Hash de la capa departamental de la que deriva el emisor (paralelo a `departmentLayerRef` del descriptor; mismo [contrato de hash](./esquema-identidad-agente.md#6-contrato-de-hash)). Documenta qué criterios de dominio aplicó el emisor. |
| `originatingUserRef` | C | seudónimo opaco | Referencia al usuario que originó la cadena. **Nunca PII directa**: un seudónimo opaco. **Ausente** en cadenas iniciadas por el sistema (no por una persona). |
| `hopCount` | R | entero ≥ 1 | Número de saltos acumulados. La primera invocación de la cadena es `1`. |
| `decisionChain` | C | array de `DecisionHop` | La cadena de decisiones previas. **Obligatoria cuando `hopCount > 1`.** Ver §3. |
| `deidTokens` | C | array de `DeidToken` | Tokens de des-identificación reversible (§5). **Condicional**: presente solo si se redactó algún dato reversible en la ruta. |
| `compatibilityPolicy` | O | enum `{escalar, rechazar}` | Qué hacer ante incompatibilidad de Constitución. Default del framework: `escalar` (a humano). Una organización puede endurecer a `rechazar`, nunca relajar a `permitir`. |
| `escalationContext` | C | objeto | Se rellena **solo** cuando la cadena se rompe (incompatibilidad o bloqueo): motivo, agente que escala, evidencia. Es lo que recibe el humano. |

---

## 3. El sub-objeto `DecisionHop`

Cada eslabón de `decisionChain` documenta un salto ya ocurrido:

| Campo | Req. | Tipo | Descripción |
|---|---|---|---|
| `agentId` | R | URN | Agente que ejecutó este salto. |
| `toolInvoked` | R | string | Tool que se invocó. |
| `constitutionHashApplied` | R | hash | Versión de Constitución que ese agente aplicó en ese salto. |
| `criteriaApplied` | R | array de string | Criterios aplicados, cada uno como `policyId@version` (criterio automatizado) **o** el literal `"juicio-de-modelo-no-automatizable"` (criterio fino que Federation no automatiza). |
| `outcome` | R | enum `{permitido, redactado, escalado, bloqueado}` | Resultado de la decisión en ese salto. |
| `timestamp` | R | timestamp | Cuándo ocurrió el salto. |

La convención de `criteriaApplied` es deliberada: distinguir lo automatizado de lo no automatizable es lo que hace **analizable el Patrón A** ([patrones de drift](./patrones-deteccion-drift.md)) — permite comparar, para una cadena cuestionada, qué criterios se aplicaron contra los que la Constitución exigía. Sin esta convención, la cadena documenta «pasó por aquí» pero no «con qué criterio», y el análisis de drift se vuelve imposible.

---

## 4. Validación de compatibilidad y caso límite

Al recibir el bloque, el agente B:

1. Compara `constitutionHash` (del bloque) contra su propio `compatibleConstitutionHashes` ([descriptor de identidad](./esquema-identidad-agente.md)).
2. **Match** → la cultura del emisor es compatible. B decide si aplica criterios adicionales propios de su dominio que A no podía conocer, ejecuta (sujeto a policy), y **propaga el bloque actualizado** (incrementa `hopCount`, añade su `DecisionHop`) en cualquier llamada subsiguiente.
3. **No match** → la llamada **no procede**. Se aplica `compatibilityPolicy` (default `escalar`): se rellena `escalationContext` y se escala a humano con el bloque completo como evidencia.

Este es el caso límite que el manifiesto §3.2 manda declarar explícitamente: cuando A o B no se ha actualizado tras un cambio normativo, permitir la llamada con criterios desfasados sería la antítesis del framework. La sobrecarga de la validación es una comparación de hashes — microsegundos en el caso normal (manifiesto §9).

---

## 5. El sub-objeto `DeidToken` (des-identificación reversible)

Cuando la capa de des-identificación en la ruta ([CF-06](./criterios-funcionales.md)) redacta un dato **de forma reversible**, emite un token que el bloque transporta para que la respuesta final pueda re-identificarse **solo en el agente de origen**:

| Campo | Req. | Tipo | Descripción |
|---|---|---|---|
| `token` | R | string opaco | Marcador que sustituye al dato en los argumentos. |
| `scope` | R | string | Ámbito de validez (qué agente/cadena puede re-identificar). |
| `ttl` | R | duración | Vida del token; expira para limitar la ventana de re-identificación. |

**Regla dura: `deidToken` nunca contiene el valor original.** Es un puntero a un vault gestionado por el stack; el valor solo se recupera en el origen autorizado, dentro del `ttl`. Cuando la redacción es **irreversible**, no hay token: el dato se ha ido y no vuelve. Esto conecta con la capa técnica de la [Guía de protección de datos](../adoption/guia-proteccion-datos.md): Federation es donde la redacción inline en la ruta —que en Adoption no tenía punto de inserción— se vuelve nativa.

---

## 6. Reglas normativas del bloque

1. **Privacidad por construcción.** El bloque viaja en cada llamada y se exporta a observabilidad; por eso **no contiene PII directa**: `originatingUserRef` es seudónimo, los datos sensibles son `deidToken` (punteros), nunca valores. Toda implementación cruza obligatoriamente la [Guía de protección de datos](../adoption/guia-proteccion-datos.md).
2. **Persistencia del `correlationId`.** Una cadena = un `correlationId`, de principio a fin. Regenerarlo rompe la trazabilidad y la detección de drift.
3. **Truncamiento controlado.** En cadenas muy largas, `decisionChain` puede truncarse a los últimos N saltos más un `chainDigest` (hash de los eslabones omitidos), de modo que la cadena completa siga siendo verificable sin transportarla entera. La política de truncamiento se declara, no se improvisa.
4. **El transporte no está aquí.** Cómo se serializa el bloque y por qué mecanismo viaja (clave de metadatos, header, atributo de traza) es responsabilidad del gateway y vive en [`appendix/mapeo-transporte/`](./appendix/mapeo-transporte/). Esto preserva la portabilidad: los mismos campos viajan por MCP hoy y por A2A mañana sin cambiar el esquema (manifiesto §9).
5. **Sin extensiones de protocolo.** El bloque se materializa sobre los mecanismos que el protocolo base ya provee (manifiesto §8). Ningún campo lleva nombre ni valor específico de un protocolo.

---

## 7. Representación ilustrativa (no normativa)

El contrato es §2–§5. Este JSON solo ilustra un bloque en el segundo salto de una cadena:

```json
{
  "schemaVersion": "1.0",
  "correlationId": "550e8400-e29b-41d4-a716-446655440000",
  "businessCaseId": "lead-2026-0042",
  "constitutionHash": "sha256:…",
  "regulatoryFrameworkHash": "sha256:…",
  "departmentLayerHash": "sha256:…",
  "originatingUserRef": "usr_op4q…(seudónimo)",
  "hopCount": 2,
  "decisionChain": [
    {
      "agentId": "urn:myrmion:agent:consultora-modelo:comercial:propuestas",
      "toolInvoked": "calificar_lead",
      "constitutionHashApplied": "sha256:…",
      "criteriaApplied": ["pol-calificacion-lead@1.2", "juicio-de-modelo-no-automatizable"],
      "outcome": "permitido",
      "timestamp": "2026-05-30T10:00:00Z"
    }
  ],
  "deidTokens": [
    { "token": "«NIF_1»", "scope": "cadena:550e8400…", "ttl": "PT1H" }
  ],
  "compatibilityPolicy": "escalar"
}
```

El [ejemplo del corredor](../../examples/federation/corredor-comercial-legal/) incluye `hop-1.json` y `hop-2.json` con el mismo `correlationId`, validados contra el JSON Schema derivado de este contrato.

---

*Esquema del bloque de contexto cultural de Myrmion Federation — versión 1.0. Parte del corpus normativo. Su plantilla socrática es [bloque-contexto-cultural.md](../../templates/federation/bloque-contexto-cultural.md); su contraparte estática es el [descriptor de identidad](./esquema-identidad-agente.md); el transporte vive en [`appendix/mapeo-transporte/`](./appendix/mapeo-transporte/).*
