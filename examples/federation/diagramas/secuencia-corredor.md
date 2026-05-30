# Myrmion Federation — Diagrama: secuencia del corredor comercial→legal

**Versión 1.0**

*Materializa el flujo de los §3 (las cuatro capas) y §4 (criterios) del [manifiesto](../../../docs/federation/manifesto.md) sobre un caso concreto: la propagación del bloque de contexto cultural a lo largo de los tres saltos del corredor de ejemplo, sin acoplarse a ningún producto ni transporte.*

Este diagrama acompaña al [ejemplo del corredor comercial→legal](../corredor-comercial-legal/README.md) y a la [guía de arquitectura funcional](../../../docs/federation/guia-arquitectura-funcional.md). Los participantes son **roles funcionales**, no productos: cada uno es una capacidad descrita en la guía de arquitectura, no una marca concreta. El mapeo a transportes reales vive en el apéndice (`docs/federation/appendix/mapeo-transporte/`); aquí el contrato es la **secuencia de saltos** y **qué viaja en cada uno**, no cómo se serializa por el cable.

## El caso

La organización de ejemplo es **Consultora Modelo S.L.**. Llega un *lead* a Comercial. El agente de Comercial (`urn:myrmion:agent:consultora-modelo:comercial:propuestas`, cuyo custodio es **Fonseca**) prepara una propuesta y necesita que el agente de Legal (`urn:myrmion:agent:consultora-modelo:legal:dictamenes`, cuyo custodio es **Riera**) valide cláusulas antes de enviarla al cliente. El corredor cruza una **frontera de dominio** (Comercial → Legal): es exactamente el punto donde la federación tiene que aportar identidad verificable, contexto cultural propagado y trazabilidad.

> El `agentId` nombra al **agente** (su función: `propuestas`, `dictamenes`), no a la persona. Fonseca y Riera son los custodios humanos (`owner`) de cada agente. A lo largo del diagrama nombramos al agente por su función y, entre paréntesis, a su custodio.

Los tres saltos:

1. **Salto 1 — descubrimiento e identidad.** El corredor de Comercial localiza la capacidad legal en el registro y verifica la identidad del agente de Legal antes de hablar con él.
2. **Salto 2 — petición con contexto.** Comercial invoca a Legal propagando el bloque de contexto cultural y añadiendo su propio `DecisionHop`.
3. **Salto 3 — respuesta gobernada.** Legal responde, añade su `DecisionHop` y devuelve el bloque enriquecido; el corredor cierra con la traza completa de la decisión.

## Secuencia

```mermaid
sequenceDiagram
    autonumber
    actor Lead as Lead del cliente
    participant Com as Agente Comercial<br/>comercial:propuestas (cust. Fonseca)
    participant Reg as Registro de capacidades
    participant Gw as Frontera de dominio<br/>(autenticación mutua + política)
    participant Leg as Agente Legal<br/>legal:dictamenes (cust. Riera)
    participant Traza as Registro de trazas

    Note over Com,Leg: Org: Consultora Modelo S.L. — corredor Comercial → Legal

    Lead->>Com: Solicita propuesta comercial
    activate Com
    Note over Com: El agente redacta la propuesta;<br/>detecta que requiere validación legal

    rect rgb(235, 244, 255)
    Note over Com,Reg: Salto 1 — descubrimiento e identidad (CF-01, CF-04)
    Com->>Reg: Consulta capacidad "validación de cláusulas"
    activate Reg
    Reg-->>Com: Descriptor del agente Legal<br/>(agentId, capacidades, hash de identidad)
    deactivate Reg
    Note over Com: Verifica que el hash del descriptor<br/>= "sha256:" sobre la forma canónica
    end

    rect rgb(235, 255, 240)
    Note over Com,Leg: Salto 2 — petición con contexto (CF-02, CF-03, CF-04, CF-05)
    Note over Com: DLP redactó el NIF del lead en el salto 1:<br/>DecisionHop[0] calificar_lead, outcome: redactado,<br/>deidToken «NIF_1»; hopCount pasa a 2
    Com->>Gw: Invoca validar_clausula + bloque de contexto cultural
    activate Gw
    Note over Gw: Autenticación mutua con identidad<br/>criptográfica verificable;<br/>require-prior-hop(legal) satisfecho
    Gw->>Leg: Petición admitida + bloque propagado (2 hops)
    activate Leg
    Gw->>Traza: Asienta hop de entrada (correlationId)
    end

    rect rgb(255, 248, 235)
    Note over Leg,Traza: Salto 3 — respuesta gobernada (CF-03, CF-05, CF-06)
    Note over Leg: El agente Legal valida la cláusula con «NIF_1»;<br/>correlaciona sin re-identificar al lead
    Leg->>Leg: Añade DecisionHop[1]: validar_clausula,<br/>criteriaApplied, outcome: permitido
    Leg-->>Gw: Veredicto + bloque enriquecido
    deactivate Leg
    Gw->>Traza: Asienta hop de salida (traza encadenada)
    Gw-->>Com: Respuesta admitida + bloque con 2 hops
    deactivate Gw
    end

    Note over Com: El agente Comercial incorpora el veredicto;<br/>la propuesta queda trazable extremo a extremo
    Com-->>Lead: Propuesta validada
    deactivate Com
```

## Qué viaja en cada salto (contrato, no serialización)

| Salto | Qué se transporta | Contrato de referencia |
|-------|-------------------|------------------------|
| 1 | Descriptor del agente Legal: `agentId`, capacidades y `hash` de identidad | [esquema de identidad de agente](../../../docs/federation/esquema-identidad-agente.md) |
| 2 | Bloque de contexto cultural con `DecisionHop[0]` (Comercial) y `deidTokens` | [esquema del bloque de contexto cultural](../../../docs/federation/esquema-bloque-contexto-cultural.md) |
| 3 | Bloque enriquecido con `DecisionHop[1]` (Legal); traza encadenada | [esquema del bloque de contexto cultural](../../../docs/federation/esquema-bloque-contexto-cultural.md) |

### Notas de lectura

- **El `agentId` es una URN variable de la organización.** En este caso `urn:myrmion:agent:consultora-modelo:comercial:propuestas` y `urn:myrmion:agent:consultora-modelo:legal:dictamenes`. La parte `<org>` la fija cada organización; no está hardcodeada en el framework. El segmento `<nombre>` nombra la **función** del agente (`propuestas`, `dictamenes`), no a la persona: Fonseca y Riera son los custodios humanos (`owner`).
- **El bloque crece, nunca se reescribe.** Cada salto **añade** un `DecisionHop`; ningún participante borra ni edita los hops anteriores. La traza encadenada de los tres saltos es lo que hace la decisión reconstruible (CF-05).
- **Los datos personales del lead nunca cruzan en claro.** Legal trabaja sobre `deidTokens`: identificadores estables que permiten razonar sobre el caso sin re-identificar a la persona. La re-identificación, si procede, ocurre fuera del corredor y bajo otra política.
- **La frontera de dominio no es un producto.** "Frontera de dominio" agrupa las tres propiedades de CF-04 (autenticación mutua, identidad criptográfica verificable, integridad del canal) más la evaluación de política. Cómo se implemente —service mesh, gateway, policy engine— es una decisión de despliegue documentada en el apéndice, no parte del contrato.

---

*Diagrama: secuencia del corredor comercial→legal — versión 1.0. Parte del corpus normativo.*

**Relacionado:** [ejemplo del corredor](../corredor-comercial-legal/README.md) · [guía de arquitectura funcional](../../../docs/federation/guia-arquitectura-funcional.md) · [esquema del bloque de contexto cultural](../../../docs/federation/esquema-bloque-contexto-cultural.md) · [criterios funcionales](../../../docs/federation/criterios-funcionales.md)
