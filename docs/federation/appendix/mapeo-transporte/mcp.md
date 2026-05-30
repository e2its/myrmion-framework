# Myrmion Federation — Mapeo de transporte: MCP

**Versión 1.0**

*Materializa el contrato de transporte que el cuerpo deja abierto: cómo viaja el [bloque de contexto cultural](../../esquema-bloque-contexto-cultural.md) —y el [descriptor de identidad](../../esquema-identidad-agente.md) y los `deidToken`— sobre los mecanismos que MCP ya provee, sin requerir extensiones del protocolo. El esquema es del cuerpo; el transporte vive aquí ([regla anti-acoplamiento](../../regla-anti-acoplamiento.md) §4).*

---

> ## Banner de vigencia
>
> | Campo | Valor |
> | --- | --- |
> | **Protocolo** | MCP (Model Context Protocol) |
> | **Mecanismos usados** | clave de metadatos `_meta`; correlación de traza W3C `traceparent`; metadatos del transporte subyacente |
> | **Fecha de revisión** | 2026-05-30 |
> | **Revisor(es)** | comunidad |
> | **Próxima revisión recomendada** | 2026-11-30 |
> | **Estado** | vigente |
> | **Fuente upstream** | https://modelcontextprotocol.io |
>
> *Este mapeo caduca. Los mecanismos concretos de MCP (`_meta`, su forma y sus garantías) cambian con el protocolo y sus implementaciones; verifica la vigencia contra la versión que uses. Lo normativo —el contrato del bloque, que no depende de ningún transporte— está en el cuerpo ([`../../esquema-bloque-contexto-cultural.md`](../../esquema-bloque-contexto-cultural.md)), no aquí.*

---

## 1. Qué resuelve este documento

El [bloque de contexto cultural](../../esquema-bloque-contexto-cultural.md) es un **contrato de datos**, no una serialización: define qué campos existen y qué significan, no cómo viajan por el cable (regla del bloque §6.4). Este documento responde a la pregunta de transporte para **MCP**: dado el contrato, ¿sobre qué mecanismos de MCP se apoya el bloque para cruzar una frontera departamental?

La respuesta tiene una restricción dura, heredada del manifiesto (§8, «No es un protocolo nuevo»): **no se inventan extensiones de protocolo.** El bloque se monta sobre los mecanismos que MCP ya ofrece. Si una versión futura de MCP retira o renombra un mecanismo, este documento caduca —por eso vive en el apéndice y no en el cuerpo, y por eso lleva banner de vigencia.

---

## 2. Principio de mapeo

El bloque viaja como **metadatos asociados a la invocación**, no como parte de los argumentos funcionales de la tool. Esta separación es deliberada y materializa la capa §3.2 del manifiesto: el agente receptor recibe los argumentos de la llamada por un canal y el contexto cultural del emisor por otro, de modo que puede validar compatibilidad (esquema del bloque §4) e interpretar lo primero a la luz de lo segundo sin que ambos se confundan.

MCP ofrece tres puntos de anclaje, y el bloque los usa en capas:

| Necesidad del bloque | Mecanismo de MCP | Por qué ahí |
|---|---|---|
| Adjuntar el bloque completo a la invocación, fuera de los argumentos | Clave de metadatos `_meta` (`params._meta`) en la petición y en el resultado | Es el canal que MCP prevé para metadatos no funcionales que no forman parte del contrato de la tool. |
| Correlar todas las invocaciones de una misma cadena de decisión | Correlación de traza W3C (`traceparent`) en las cabeceras del transporte | Estándar transversal: sobrevive a saltos entre dominios y herramientas. Es el portador del `correlationId`. |
| Verificar integridad del bloque sin abrir los argumentos | El propio bloque lleva los hashes; la identidad del extremo la prueba el transporte | Mantiene el bloque agnóstico: la autenticación mutua (CF-04) vive por debajo de MCP. |

Ninguno de estos mecanismos exige modificar MCP. El campo `_meta` está pensado para esto; `traceparent` vive en la capa de transporte, por debajo del protocolo.

---

## 3. El bloque dentro de `_meta`

MCP reserva la clave `_meta` en peticiones (`params._meta`) y en resultados para metadatos no funcionales. El bloque de contexto cultural viaja ahí bajo una clave de espacio de nombres propia, para no colisionar con otros usos de `_meta`. Los nombres de campo son **exactamente los del contrato** (esquema del bloque §2–§5): el transporte los envuelve, no los renombra.

Este ejemplo ilustra el segundo salto del [corredor comercial→legal](../../../../examples/federation/corredor-comercial-legal/): el agente de Comercial de Consultora Modelo S.L. ha calificado un lead y ahora invoca al agente Legal para que revise la propuesta.

```json
{
  "method": "tools/call",
  "params": {
    "name": "revisar_propuesta",
    "arguments": {
      "propuestaRef": "«NIF_1»"
    },
    "_meta": {
      "myrmion/culturalContext": {
        "schemaVersion": "1.0",
        "correlationId": "550e8400-e29b-41d4-a716-446655440000",
        "businessCaseId": "lead-2026-0042",
        "constitutionHash": "sha256:…",
        "regulatoryFrameworkHash": "sha256:…",
        "departmentLayersHash": "sha256:…",
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
    }
  }
}
```

Notas sobre el mapeo:

- **La clave es de espacio de nombres** (`myrmion/culturalContext`). MCP permite reservar prefijos en `_meta`; usar uno propio evita choques con otros consumidores del campo.
- **El subárbol bajo la clave es el bloque del cuerpo, intacto.** Mismos nombres, mismo orden semántico, misma jerarquía (`decisionChain` de `DecisionHop`, `deidTokens` de `DeidToken`). Esa identidad es lo que hace portable el bloque: el mismo subárbol viaja sobre A2A sin cambiar (ver [`a2a.md`](./a2a.md)).
- **Los datos sensibles no viajan en claro.** En el ejemplo, `propuestaRef` no contiene el dato real (el NIF del lead) sino el `token` del `DeidToken` que lo sustituyó en la ruta (CF-06). El valor solo se recupera **en el agente de origen**, dentro del `ttl`, contra el vault que gestiona el stack. La regla dura del esquema del bloque §5 se preserva en transporte: `token` nunca lleva el valor original.

---

## 4. Correlación de traza: `traceparent` W3C y el `correlationId`

El `correlationId` del bloque identifica la cadena de decisión completa y **nunca se regenera** dentro de una cadena (esquema del bloque §6.2). Para que ese identificador correle también las invocaciones a nivel de transporte —petición y respuesta, y los saltos sucesivos— se apoya en el estándar **W3C Trace Context**, que define la cabecera `traceparent`:

```
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
```

El segmento central (`trace-id`) es estable a lo largo de todo el flujo federado: viaja del agente de Comercial al de Legal y vuelve en la respuesta. Esto es lo que permite que la observabilidad agent-aware (CF-05) reconstruya la cadena completa —el insumo del Patrón A de [detección de drift](../../patrones-deteccion-drift.md)— sin instrumentación ad hoc por agente.

La relación entre los dos identificadores es de complemento, no de duplicación:

| Elemento | Responde a | Vive en |
|---|---|---|
| `correlationId` (bloque) + `trace-id` (`traceparent`) | ¿Qué invocaciones pertenecen a la misma cadena de decisión? | `correlationId` en `_meta`; `trace-id` en cabecera |
| `decisionChain[].*` | ¿Qué agente decidió qué, con qué criterio y con qué resultado, en cada salto? | Bloque, en `_meta` |

**Recomendación de binding:** que el `trace-id` de `traceparent` se derive de forma estable del `correlationId` (o que la implementación los mantenga cosidos), de modo que la traza distribuida del stack y la cadena de decisión semántica del bloque se puedan unir en una sola consulta. El cuerpo exige que CF-05 trace «por `correlationId` estándar»; `traceparent` es el portador estándar natural de ese identificador sobre MCP.

---

## 5. Identidad y verificación de compatibilidad

Dos verificaciones cruzan la frontera; ninguna de las dos es un campo que el transporte añada al bloque:

- **Identidad del extremo (CF-04).** La autenticación mutua con identidad criptográfica verificable se establece **por debajo de MCP**, en el transporte. El bloque no la lleva: la asume. Si el flujo cruza un gateway (CF-01), es esa capa la que prueba la identidad de cada extremo y la vincula de forma estable al `agentId` del [descriptor](../../esquema-identidad-agente.md). El cuerpo nunca exige «mTLS» por su nombre: exige las tres propiedades de CF-04, que mTLS u otros mecanismos satisfacen.
- **Compatibilidad de Constitución (esquema del bloque §4).** Al recibir el `_meta`, el agente receptor compara el `constitutionHash` del bloque contra su propio `compatibleConstitutionHashes` (descriptor §7). Es una pertenencia a conjunto en O(1); si no hay match, la llamada **no procede** y se aplica `compatibilityPolicy`. Esto ocurre en el agente, leyendo el bloque ya transportado; el transporte solo garantiza que el bloque llegó entero y sin truncar (CF-01).

El contrato de hash que hace comparables los `constitutionHash` entre implementaciones es el del cuerpo (`sha256:` sobre forma canónica: UTF-8 NFC, saltos LF, sin trailing whitespace, excluyendo la sección «0. Metadatos» — [esquema de identidad §6](../../esquema-identidad-agente.md#6-contrato-de-hash)). El transporte no lo altera.

---

## 6. El descriptor de identidad sobre MCP

El [descriptor de identidad](../../esquema-identidad-agente.md) no viaja en cada llamada como el bloque, pero también necesita un binding: el campo `endpoint.transport` del descriptor toma el valor abstracto `mcp`, y `endpoint.address` resuelve a la dirección de servidor MCP del agente. Cómo se publica y firma el descriptor en un service registry concreto (CF-02) es responsabilidad del stack y vive en [`../stacks-referencia/`](../stacks-referencia/); este documento solo fija que, sobre MCP, un agente se invoca como un servidor MCP y su `agentId` (`urn:myrmion:agent:<org>:<dominio>:<nombre>`) es su identidad estable, no su URL.

---

## 7. Qué NO se mapea

Para que la regla anti-acoplamiento siga viva, conviene ser explícito sobre lo que este documento deliberadamente no hace:

- **No define extensiones de MCP.** Todo se apoya en `_meta` y `traceparent`, que ya existen.
- **No prescribe el transporte concreto** por debajo de MCP. Las cabeceras de la §4 son las de cualquiera que sea el transporte que MCP esté usando.
- **No mueve campos del contrato al transporte.** El bloque viaja entero en `_meta`; `traceparent` solo aporta correlación, nunca sustituye el `correlationId` ni ningún otro campo.
- **No resuelve `deidToken`.** El transporte mueve el `token` opaco; la re-identificación ocurre solo en el origen autorizado (esquema del bloque §5).

---

## Enlaces relacionados

- [Esquema del bloque de contexto cultural](../../esquema-bloque-contexto-cultural.md) — el contrato que aquí se transporta.
- [Mapeo de transporte: A2A](./a2a.md) — el binding equivalente que demuestra la portabilidad (manifiesto §9).
- [Esquema de identidad de agente](../../esquema-identidad-agente.md) — el descriptor y el contrato de hash.
- [Criterios funcionales](../../criterios-funcionales.md) — CF-01 (propagación de metadatos sin truncar), CF-04 (identidad), CF-05 (traza por `correlationId`).
- [Regla anti-acoplamiento](../../regla-anti-acoplamiento.md) §4 — por qué el transporte vive en el apéndice.
- [Apéndice vivo: componentes candidatos](../README.md) — la matriz de stacks.

---

*Mapeo de transporte: MCP — versión 1.0. Apéndice vivo del corpus; el contenido es informativo y caduca (ver banner). Lo normativo es el cuerpo.*
