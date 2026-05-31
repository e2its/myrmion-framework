<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Bloque de Contexto Cultural (ejemplo)

**Versión 1.0**

*Ejemplo rellenado de la [plantilla del bloque de contexto cultural](./bloque-contexto-cultural.md): el bloque tal y como lo emite el agente Legal en el salto 2 del corredor comercial→legal de Consultora Modelo S.L.*

</td>
</tr>
</table>

---

> **Este es un ejemplo rellenado** aplicado al caso del **corredor comercial→legal** de la organización ficticia **Consultora Modelo S.L.** (`<org>` = `consultora-modelo`). Muestra el bloque tal y como lo construye el **agente Legal en el salto 2** (`hopCount = 2`), tras recibir el salto 1 del agente Comercial. El `correlationId` es **compartido** con el salto 1: no se regenera. Para el flujo completo de extremo a extremo, ver [`examples/federation/corredor-comercial-legal/`](../../examples/federation/corredor-comercial-legal/), que incluye `hop-1.json` y `hop-2.json` validados contra el JSON Schema derivado del contrato.

---

## El caso

Fonseca, del departamento Comercial, ha cualificado un lead (`lead-2026-0042`) y necesita revisión legal de la propuesta antes de enviarla. Su agente departamental, `urn:myrmion:agent:consultora-modelo:comercial:propuestas`, **origina** la cadena en el salto 1 (`hopCount = 1`): invoca `calificar_lead`, aplica sus criterios y deja `outcome: permitido`. Como en el lead aparece el NIF del cliente, la des-identificación en la ruta lo redacta de forma reversible y emite un `deidToken`.

El agente del departamento Legal, `urn:myrmion:agent:consultora-modelo:legal:revision` (que opera para Riera), **recibe** el bloque, valida que el `constitutionHash` del emisor es compatible con el suyo (lo es), invoca `revisar_propuesta` y decide. El bloque de abajo es el que Legal construye en el salto 2: hereda `correlationId`, `businessCaseId`, `originatingUserRef`, la cadena previa y los `deidTokens`; **incrementa `hopCount` a 2** y **añade** su propio `DecisionHop`.

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Organización | Consultora Modelo S.L. (`consultora-modelo`) |
| Custodio (plataforma de federación) | Plataforma de Federación de Consultora Modelo |
| `schemaVersion` del bloque que esta política soporta | 1.0 |
| Versión del documento | 1.0 |
| Fecha de aprobación | 2026-05-30 |
| Próxima revisión programada | 2026-11-30 |

---

## 1. El bloque emitido en el salto 2

Este es el bloque que el agente Legal adjunta a su llamada subsiguiente (y que queda como evidencia de su salto). Cumple el contrato del [esquema](../../docs/federation/esquema-bloque-contexto-cultural.md) §2–§5.

```json
{
  "schemaVersion": "1.0",
  "correlationId": "550e8400-e29b-41d4-a716-446655440000",
  "businessCaseId": "lead-2026-0042",
  "constitutionHash": "sha256:c0ffee11d2a3b4c5d6e7f8091a2b3c4d5e6f7081920a1b2c3d4e5f60718293a4",
  "regulatoryFrameworkHash": "sha256:1a2b3c4d5e6f708192a3b4c5d6e7f8091a2b3c4d5e6f708192a3b4c5d6e7f809",
  "departmentLayerHash": "sha256:9f8e7d6c5b4a39281706f5e4d3c2b1a09f8e7d6c5b4a39281706f5e4d3c2b1a0",
  "originatingUserRef": "usr_op4q7x2k (seudónimo)",
  "hopCount": 2,
  "decisionChain": [
    {
      "agentId": "urn:myrmion:agent:consultora-modelo:comercial:propuestas",
      "toolInvoked": "calificar_lead",
      "constitutionHashApplied": "sha256:c0ffee11d2a3b4c5d6e7f8091a2b3c4d5e6f7081920a1b2c3d4e5f60718293a4",
      "criteriaApplied": ["pol-calificacion-lead@1.2", "juicio-de-modelo-no-automatizable"],
      "outcome": "permitido",
      "timestamp": "2026-05-30T09:12:00Z"
    },
    {
      "agentId": "urn:myrmion:agent:consultora-modelo:legal:revision",
      "toolInvoked": "revisar_propuesta",
      "constitutionHashApplied": "sha256:c0ffee11d2a3b4c5d6e7f8091a2b3c4d5e6f7081920a1b2c3d4e5f60718293a4",
      "criteriaApplied": ["pol-revision-clausulas@2.0", "juicio-de-modelo-no-automatizable"],
      "outcome": "redactado",
      "timestamp": "2026-05-30T09:45:00Z"
    }
  ],
  "deidTokens": [
    { "token": "«NIF_1»", "scope": "cadena:550e8400-e29b-41d4-a716-446655440000", "ttl": "PT1H" }
  ],
  "compatibilityPolicy": "escalar"
}
```

---

## 2. Identidad y correlación

- **`correlationId` compartido.** El valor `550e8400-e29b-41d4-a716-446655440000` lo generó el agente Comercial al originar la cadena (`hopCount = 1`). El agente Legal lo **copia tal cual**: no lo regenera. Los dos saltos del corredor se trazan así como una sola cadena de extremo a extremo, lista para el Patrón A de detección de drift.
- **`hopCount` incrementado.** El salto 1 viajaba con `hopCount = 1` y la `decisionChain` con un solo eslabón. Legal lo lleva a `2` y la cadena pasa a tener dos eslabones: `hopCount` y la longitud de `decisionChain` deben cuadrar.
- **`originatingUserRef` heredado y seudónimo.** Es `usr_op4q7x2k`, un seudónimo opaco de Fonseca. **Nunca su nombre ni su email**: el bloque se exporta a observabilidad y no puede llevar PII directa.

---

## 3. businessCaseId

`businessCaseId` es `lead-2026-0042`, el caso de negocio que originó la cadena. Es estable durante toda la vida del caso y agrupa cualquier otra cadena que sirva a este mismo lead. No codifica por sí mismo ningún dato del cliente en claro: el NIF, que sí es sensible, viaja redactado como `deidToken`, no dentro del `businessCaseId`.

---

## 4. decisionChain

La cadena es **append-only**. El `DecisionHop` del agente Comercial (salto 1) llega intacto; el agente Legal **añade** el suyo (salto 2) sin tocar el anterior. Los `timestamp` son coherentes con el orden (`09:45:00Z` > `09:12:00Z`).

- **`constitutionHashApplied` idéntico en ambos** saltos: los dos agentes operan la misma versión de Constitución, que es justo lo que la validación de compatibilidad (esquema §4) verificó al recibir el salto 1.
- **`criteriaApplied` honesto.** Cada eslabón distingue la policy automatizada (`pol-calificacion-lead@1.2`, `pol-revision-clausulas@2.0`) del literal `"juicio-de-modelo-no-automatizable"` para el criterio fino que Federation no automatiza (Legal valoró el matiz de la cláusula de penalización con juicio de modelo, no con una regla booleana). Esta convención es la que hace **analizable** la cadena a posteriori.
- **`outcome: redactado`** en el salto 2: Legal aprueba pero la des-identificación de la ruta redactó un dato en el camino (el NIF), por lo que el resultado del salto es `redactado`, no `permitido`. Ni `toolInvoked` ni `criteriaApplied` llevan PII en claro.

En este corredor de dos saltos no hace falta truncar. Si la cadena escalara a finanzas y creciera, la política de Consultora Modelo conservaría el primer salto (originador) y el último, archivaría la cadena completa vía observabilidad agent-aware ([CF-05](../../docs/federation/criterios-funcionales.md)) y la sustituiría por los últimos N eslabones más un `chainDigest` que la mantiene verificable.

---

## 5. compatibilityPolicy

`compatibilityPolicy` es `escalar`, el default del framework: Consultora Modelo no lo ha endurecido a `rechazar`. En este flujo no se activó, porque el `constitutionHash` del emisor era compatible con el del receptor. Si Legal hubiera operado una versión incompatible de Constitución, la llamada **no habría procedido**: se habría rellenado `escalationContext` y escalado a un humano con el bloque completo como evidencia, registrándolo en el [registro de excepciones](./registro-excepciones.md). Una incompatibilidad de `regulatoryFrameworkHash` no se escala: es dura, y se trata como alerta.

---

## 6. deidTokens

El agente Comercial, al originar la cadena, redactó el NIF del cliente de forma reversible. El bloque transporta un solo `DeidToken`:

- `token`: `«NIF_1»` — el marcador que sustituye al NIF en los argumentos de la tool.
- `scope`: `cadena:550e8400-...` — solo re-identificable dentro de esta cadena.
- `ttl`: `PT1H` — la ventana de re-identificación expira en una hora.

El agente Legal **hereda** el token y lo propaga sin cambios. Legal **correlaciona sin re-identificar**: trabaja con `«NIF_1»` sabiendo que es el mismo cliente en ambos saltos, pero no puede recuperar el NIF en claro (solo el agente de origen, Comercial, puede, vía el vault del stack, dentro del `ttl`). El `deidToken` **nunca contiene el valor original**: es un puntero.

---

## 7. Reglas de privacidad aplicadas

- **No PII directa.** Fonseca viaja como `originatingUserRef` seudónimo; el NIF del cliente, como `deidToken`. Ningún valor en claro.
- **Minimización.** El bloque no lleva el texto de la propuesta ni el detalle de la cláusula: solo lo necesario para gobernar, validar compatibilidad y reconstruir la cadena.
- **Trazabilidad sin exposición.** El `correlationId` une los dos saltos y el `businessCaseId` los agrupa con el caso, sin revelar identidades.
- **Exportable a observabilidad.** Por construcción, el bloque puede volcarse al pipeline de observabilidad (CF-05) sin fugar datos personales, porque no los contiene en claro.

---

## 8. Mapeo a transporte — desacoplable

Cómo viaja este bloque sobre el cable entre el agente Comercial y el agente Legal **no se fija en este ejemplo**. Consultora Modelo se adhiere al mapeo publicado en [`appendix/mapeo-transporte/`](../../docs/federation/appendix/mapeo-transporte/). El bloque JSON de arriba sería **idéntico** aunque cambiara el transporte o se portara a A2A: ese es exactamente el punto del desacoplamiento.

---

## 9. Validación al recibir el bloque

Al recibir el salto 1, la plataforma de Consultora Modelo validó: `schemaVersion` reconocida; `correlationId` presente y bien formado; `hopCount` (1) coherente con la longitud de `decisionChain` (1); `constitutionHash` del emisor contra los `compatibleConstitutionHashes` del receptor (match); y `deidToken` con `token`/`scope`/`ttl` y sin valor en claro. El bloque del salto 2 pasa las mismas comprobaciones — ahora con `hopCount = 2` y dos eslabones — antes de propagarse.

---

*Bloque de Contexto Cultural (ejemplo) de Myrmion Federation — versión 1.0. Parte del corpus normativo. Su plantilla en blanco es [bloque-contexto-cultural.md](./bloque-contexto-cultural.md); su contrato es el [esquema del bloque](../../docs/federation/esquema-bloque-contexto-cultural.md).*

*Relacionado: [plantilla del bloque](./bloque-contexto-cultural.md) · [esquema del bloque](../../docs/federation/esquema-bloque-contexto-cultural.md) · [ejemplo del corredor comercial→legal](../../examples/federation/corredor-comercial-legal/) · [Manifiesto de Federation](../../docs/federation/manifesto.md)*
