# Myrmion Federation — Mapeo de transporte: A2A

**Versión 1.0**

*Binding del [bloque de contexto cultural](../../esquema-bloque-contexto-cultural.md) sobre A2A. Los mismos campos, otro transporte: la prueba de la portabilidad que promete el [manifiesto](../../manifesto.md) §9. El esquema es del cuerpo; el transporte vive aquí ([regla anti-acoplamiento](../../regla-anti-acoplamiento.md) §4).*

---

> ## Banner de vigencia
>
> | Campo | Valor |
> | --- | --- |
> | **Protocolo** | A2A (Agent-to-Agent) |
> | **Mecanismos usados** | metadatos del mensaje / de la tarea (`metadata`); correlación de traza W3C `traceparent`; tarjeta de agente (agent card) para el descubrimiento |
> | **Fecha de revisión** | 2026-05-30 |
> | **Revisor(es)** | comunidad |
> | **Próxima revisión recomendada** | 2026-11-30 |
> | **Estado** | prospectivo |
> | **Fuente upstream** | https://a2a-protocol.org |
>
> *Este binding es **prospectivo**: equivalencia de diseño, no implementación verificada contra una versión concreta de A2A. Caduca como cualquier ficha del apéndice y, además, debe revalidarse al fijarse contra una versión real. Lo normativo —el contrato del bloque, idéntico sea cual sea el transporte— está en el cuerpo ([`../../esquema-bloque-contexto-cultural.md`](../../esquema-bloque-contexto-cultural.md)), no aquí.*

---

## 1. Por qué existe este documento

El manifiesto (§9) hace una promesa: la federación se **construye sobre MCP** pero es **portable a A2A** —«si A2A se vuelve dominante en el futuro, Federation portará a A2A los mismos principios sin reescribirse». Una promesa de portabilidad que no se demuestra es marketing. Este documento la demuestra del único modo que cuenta: tomando el mismo bloque de contexto cultural que viaja sobre MCP (ver [`mcp.md`](./mcp.md)) y mostrando que cruza A2A **sin cambiar un solo campo del contrato**.

La portabilidad no es una propiedad del transporte. Es una propiedad del **contrato**: como el bloque es un contrato de datos y no una serialización acoplada a un protocolo (regla anti-acoplamiento §4), cualquier transporte capaz de llevar metadatos arbitrarios junto a una invocación puede transportarlo. MCP y A2A son dos casos de lo mismo.

Este binding es **prospectivo**: se ofrece como equivalencia de diseño, no como implementación verificada contra una versión concreta de A2A. De ahí el `Estado: prospectivo` del banner.

---

## 2. La equivalencia, en una tabla

El bloque necesita tres cosas del transporte, y las tres existen tanto en MCP como en A2A:

| Necesidad del bloque | Mecanismo en MCP | Mecanismo equivalente en A2A |
|---|---|---|
| Adjuntar el bloque completo a la invocación, fuera de los argumentos | Clave `_meta` (`params._meta`) | Metadatos del mensaje / de la tarea (`metadata`) |
| Correlar invocaciones de la misma cadena de decisión | `traceparent` W3C en cabeceras (portador del `correlationId`) | `traceparent` W3C en cabeceras (mismo estándar, mismo `correlationId`) |
| Establecer identidad mutua verificable (CF-04) | Autenticación mutua del transporte, por debajo del protocolo | Autenticación mutua del transporte, por debajo del protocolo |

La fila de correlación es **literal**: ambos protocolos delegan en el mismo estándar transversal (W3C Trace Context), portando el mismo `correlationId`. La fila de identidad es idéntica porque la autenticación mutua vive por debajo del protocolo en ambos casos. Solo cambia el nombre del contenedor de metadatos: `_meta` en uno, `metadata` en el otro.

---

## 3. El mismo bloque, sobre A2A

El bloque viaja como **metadatos del mensaje o de la tarea** A2A. El subárbol del bloque es el mismo que sobre MCP; cambia únicamente la envoltura. Mismo segundo salto del [corredor comercial→legal](../../../../examples/federation/corredor-comercial-legal/) que en [`mcp.md`](./mcp.md) §3:

```json
{
  "message": {
    "role": "agent",
    "parts": [
      { "kind": "text", "text": "Solicito revisión de cláusulas de la propuesta «NIF_1»" }
    ],
    "metadata": {
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

Compárese con el ejemplo de [`mcp.md`](./mcp.md) §3: el subárbol bajo `myrmion/culturalContext` es **idéntico campo a campo**. Esa identidad es el resultado que este documento quiere hacer visible. Si algún día el subárbol tuviera que diferir entre transportes, el bloque habría dejado de ser portable —y el contrato, de ser un contrato.

Las mismas reglas del bloque se preservan sobre A2A sin cambio:

- `correlationId` no se regenera (esquema del bloque §6.2).
- `token` del `DeidToken` sigue siendo un puntero opaco; la re-identificación ocurre solo en el origen autorizado (§5).
- La validación de compatibilidad (`constitutionHash ∈ compatibleConstitutionHashes`) la hace el agente receptor leyendo `metadata`, igual que leía `_meta`.

---

## 4. Mapeo del `agentId` al descubrimiento de A2A

A2A publica capacidades de agente en un descriptor propio (la *agent card*). El [descriptor de identidad](../../esquema-identidad-agente.md) del cuerpo es agnóstico de ese formato, pero el `agentId` debe poder anclarse en él:

- El `agentId` (`urn:myrmion:agent:<org>:<dominio>:<nombre>`) se publica como **identificador estable** dentro de la agent card, no como su URL de acceso. La URL es transporte; el `agentId` es identidad, y no se reasigna nunca (esquema de identidad §2).
- El `domain` del descriptor mapea al dominio departamental del corpus (`comercial`, `legal`…), no a un dominio DNS.
- Las `capabilities` del descriptor —con sus propiedades de gobernanza `sideEffectClass`, `externalizes`, `canCommit`, `dataClassesTouched`— se exponen como las capacidades anunciadas en la agent card. El gate de coherencia (gobernanza federada) se evalúa contra esas propiedades, igual que sobre MCP.

Esto preserva CF-02 (descubrimiento gobernado con descriptor extendido) con independencia de que el descubrimiento se resuelva por el service registry del corpus o por la agent card nativa de A2A: el `agentId` es la clave que ambos comparten.

---

## 5. Lo que no cambia entre transportes

La lista de invariantes es, en sí misma, la definición operativa de portabilidad. Al cambiar de MCP a A2A:

- **No cambian los nombres de los campos** del bloque (esquema del bloque §2–§5).
- **No cambia la `decisionChain`** ni la semántica de cada `DecisionHop` (`criteriaApplied`, `outcome`…).
- **No cambia el contrato de `deidTokens`**: los datos sensibles siguen viajando como `token` opaco, resoluble solo en origen.
- **No cambia el contrato de hash** ni el alcance de los `*Hash` del bloque.
- **No cambia el estándar de correlación**: `traceparent` W3C portando el `correlationId`, en ambos.
- **No cambia la validación de compatibilidad** ni la política por defecto (`escalar`).

Lo único que cambia es el nombre del contenedor de metadatos (`_meta` ↔ `metadata`) y los detalles de la capa de transporte que establece la autenticación mutua. Ninguno de esos dos toca el contrato.

---

## 6. Estado de este binding

| Aspecto | Estado |
|---|---|
| Contrato del bloque | Estable (cuerpo normativo, sin marcas) |
| Mapeo a MCP | Documentado (ver [`mcp.md`](./mcp.md)) |
| Mapeo a A2A | **Prospectivo**: equivalencia de diseño, pendiente de fijar contra una versión concreta de A2A |

Cuando este binding se valide contra una versión concreta de A2A, el banner (`Estado`, `Versión evaluada`, fecha) y esta tabla deberán actualizarse. Hasta entonces, léase como la demostración de que el diseño **admite** la portabilidad que el manifiesto §9 promete —no como una garantía de interoperabilidad ya verificada.

---

## Enlaces relacionados

- [Esquema del bloque de contexto cultural](../../esquema-bloque-contexto-cultural.md) — el contrato que aquí se transporta.
- [Mapeo de transporte: MCP](./mcp.md) — el binding de referencia con el que se compara campo a campo.
- [Esquema de identidad de agente](../../esquema-identidad-agente.md) — el `agentId` y el descriptor.
- [Criterios funcionales](../../criterios-funcionales.md) — CF-01, CF-02, CF-04, CF-05.
- [Regla anti-acoplamiento](../../regla-anti-acoplamiento.md) §4 — la portabilidad a A2A como razón de ser de la neutralidad de los esquemas.
- [Manifiesto de Myrmion Federation](../../manifesto.md) — §9: construido sobre MCP, portable a A2A.

---

*Mapeo de transporte: A2A — versión 1.0. Apéndice vivo del corpus; binding prospectivo, informativo y sujeto a revisión (ver banner). Lo normativo es el cuerpo.*
