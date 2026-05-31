# Ficha de policy — Paso por Legal

> **Banner de vigencia.** Ficha del **apéndice vivo**. Menciona dialectos y motores concretos, por tanto **caduca**. Verifica la versión del dialecto antes de usar.
>
> | Campo | Valor |
> |-------|-------|
> | Última revisión | 2026-05-30 |
> | Dialectos | Rego (OPA), Cedar |
> | Efecto principal | `require-prior-hop` |
> | `automatabilityClass` | `duro` |
> | Punto de aplicación | pre-invocación |

---

## Principio de origen

> **«No asumimos compromisos sin pasar por Legal.»**

- **Origen:** Constitución del dominio Comercial — § 3 (Principios de comportamiento).
- **Lectura:** ninguna capacidad que pueda **comprometer a la organización** (firmar, prometer condiciones, aceptar una cláusula) puede ejecutarse si en la cadena de decisión no consta antes un salto por un agente del dominio Legal con resultado positivo.
- Es el principio que el manifiesto §3.3 cita textualmente como patrón canónico de mapping, y que convenciones §2 clasifica como **DURO**: el disparador (`canCommit == true`) es una condición booleana exacta y el efecto (`require-prior-hop`) es determinista.

Trazabilidad constitucional: esta ficha implementa el principio Comercial §3 citado arriba (manifiesto §5; convenciones §5).

## `automatabilityClass`: `duro`

El cumplimiento se decide con una condición booleana exacta sobre campos declarados, sin margen de interpretación (convenciones §2, clase DURO). No hay umbral: hay condición. Por eso la regla se evalúa de una sola vez en pre-invocación.

> Que la clase sea `duro` no significa que la policy juzgue el fondo jurídico. La policy garantiza que el salto por Legal **ocurrió con resultado positivo**; *qué* dictaminó Legal es trabajo de modelado del agente Legal, no de esta regla. La policy impone el corredor; no sustituye la revisión.

---

## Disparador

La regla se activa cuando, en una llamada, concurren las dos condiciones (convenciones §3, paso 2):

1. **La capacidad invocada puede comprometer.** En el **descriptor de identidad** del agente emisor, la `Capability` de la tool invocada declara:

   ```
   capability.canCommit == true
   ```

   (o, equivalentemente, `capability.sideEffectClass == "compromiso"`).

2. **Aún no consta el salto por Legal.** En `decisionChain` del **bloque de contexto cultural** **no** existe ningún `DecisionHop` cuyo `agentId` pertenezca al dominio `legal` con `outcome == "permitido"`.

El dominio de un salto se deriva del `agentId`, que tiene forma `urn:myrmion:agent:<org>:<dominio>:<nombre>`: el dominio es el quinto segmento del URN.

Si las dos condiciones concurren, el corredor de gobierno aún no se ha recorrido y la policy debe exigirlo.

> Nota de contrato: `canCommit` es una propiedad **decidible en tiempo de diseño** declarada en el descriptor, no un permiso de runtime. Justamente por declararla, esta policy le impone el salto previo. Es lo que permite que el [gate de coherencia](../../gobernanza-federada.md) detecte el conflicto antes incluso de que el agente se registre.

---

## Efecto

- **Decisión:** `require-prior-hop`.
- **Salto exigido:** un `DecisionHop` previo de un agente del dominio `legal` con `outcome == "permitido"`, sobre **esta misma** cadena (mismo `correlationId`).
- **Tras el salto:** una vez `decisionChain` incluye el salto de Legal con `outcome == "permitido"`, la siguiente evaluación de esta regla deja de dispararse y la decisión pasa a las demás reglas (que pueden terminar en `allow`).

`require-prior-hop` no es un `deny`: no cierra la puerta, la **encarrila**. Es el efecto del contrato (convenciones §3, paso 3) por el que se imponen los corredores de gobierno.

---

## Evidencia

Toda evaluación deja evidencia, anclada al `DecisionHop` del salto (campos `criteriaApplied` y `outcome`; convenciones §3, paso 4):

- En `criteriaApplied`: el identificador de esta policy como `policyId@version` (p. ej. `pol-paso-por-legal@1.0`).
- En `outcome`: `escalado` cuando se exige el salto previo (la llamada no procede hasta que Legal intervenga).
- En la traza de la decisión: `correlationId`, `agentId` del emisor, `toolInvoked`, y el motivo `falta-salto-legal`.
- El salto exigido: `{ dominio: "legal", outcome: "permitido" }`.

Cuando el salto por Legal finalmente ocurre, su propio `DecisionHop` se incorpora a `decisionChain` y se convierte, él mismo, en evidencia del corredor recorrido. Esa convención es la que hace **analizable el Patrón A** de detección de drift.

---

## Punto de aplicación

- **Cuándo:** **pre-invocación** — antes de que la tool de compromiso se ejecute (convenciones §3, paso 5: `allow`, `deny` y `require-prior-hop` se deciden en pre-invocación).
- **Dónde:** en el gateway de llamadas inter-agente ([CF-01](../../criterios-funcionales.md)), que evalúa la policy antes de ejecutar.
- **Quién evalúa:** el policy engine ([CF-03](../../criterios-funcionales.md)). Myrmion Federation no prescribe cuál; esta ficha ofrece snippets para dos.

---

## Caveats

- **No juzga el fondo.** La policy garantiza que Legal *intervino con resultado positivo*; no garantiza que la cláusula sea correcta. Ese juicio es trabajo de modelado del agente Legal.
- **Dominio del salto, no agente concreto.** La regla exige un agente *del dominio* `legal` (quinto segmento del `agentId`), no un `agentId` fijo, para no acoplarse a una instancia. Si la Constitución exige un agente legal concreto, parametrízalo.
- **Vigencia del salto.** Esta ficha trata el salto de Legal como válido para la cadena identificada por `correlationId`. Si la materia cambia sustancialmente tras el salto (otra cláusula, otro alcance), conviene invalidar el salto. La definición de «cambio sustancial» es constitucional, no de policy.
- **Degradación segura.** Si el bloque de contexto no trae `decisionChain` cuando `hopCount > 1` (debería traerla siempre), o si falta el campo `canCommit` en el descriptor, la regla no puede evaluarse con fidelidad: el resultado por defecto es `deny` con evidencia, nunca `allow` en silencio (convenciones §3, paso 6).

---

## `testVectors`

| # | Entrada (resumen) | Salida esperada |
|---|-------------------|-----------------|
| TV-1 | `capability.canCommit == true`; `decisionChain` sin salto de dominio `legal`. | `require-prior-hop` |
| TV-2 | `capability.canCommit == true`; `decisionChain` con `DecisionHop` de dominio `legal` y `outcome == "permitido"`. | (no dispara) → cede a otras reglas |
| TV-3 | `capability.canCommit == true`; `decisionChain` con `DecisionHop` de dominio `legal` y `outcome == "bloqueado"`. | `require-prior-hop` (el salto bloqueado no satisface el corredor) |
| TV-4 | `capability.canCommit == false`. | (no dispara) |
| TV-5 | `capability.canCommit == true`; falta `decisionChain` con `hopCount > 1`. | `deny` (degradación segura) |

> Ejemplo ilustrativo (`Consultora Modelo S.L.`): el agente de **Fonseca** (Comercial), `urn:myrmion:agent:consultora-modelo:comercial:propuestas`, invoca una tool con `canCommit == true` sobre el lead `lead-2026-0042` y la cadena no incluye salto de Legal. Sale `require-prior-hop`. Tras el salto del agente de **Riera** (Legal), `urn:myrmion:agent:consultora-modelo:legal:dictamenes`, con `outcome == "permitido"`, TV-2 aplica y la llamada puede continuar. Ver [`../../../../examples/federation/corredor-comercial-legal/`](../../../../examples/federation/corredor-comercial-legal/).

---

## Snippets

> Los snippets leen el documento de entrada `input` con la forma: `input.capability` (la `Capability` de la tool invocada, del descriptor), `input.context` (el bloque de contexto cultural). El nombre/valor concreto de los campos en el transporte (header, metadata, atributo de traza) lo define el [mapeo de transporte](../mapeo-transporte/), no esta ficha. La función `domain_of` extrae el quinto segmento del `agentId`.

### Rego (OPA)

```rego
package myrmion.federation.paso_por_legal

import future.keywords.if
import future.keywords.in

# Comercial §3 — "No asumimos compromisos sin pasar por Legal"
# automatabilityClass: duro · efecto: require-prior-hop · pre-invocación

# Dominio = quinto segmento del URN urn:myrmion:agent:<org>:<dominio>:<nombre>
domain_of(agent_id) := d if {
    parts := split(agent_id, ":")
    d := parts[4]
}

# ¿La capacidad invocada puede comprometer?
can_commit if input.capability.canCommit == true

# ¿Existe ya un salto positivo de Legal en esta cadena?
legal_hop_present if {
    some hop in input.context.decisionChain
    domain_of(hop.agentId) == "legal"
    hop.outcome == "permitido"
}

# Decisión: exigir salto previo de Legal
decision := "require-prior-hop" if {
    can_commit
    not legal_hop_present
}

# Degradación segura: sin cadena cuando debería haberla, denegar
decision := "deny" if {
    can_commit
    input.context.hopCount > 1
    not input.context.decisionChain
}

# Evidencia que se ancla al DecisionHop
evidence := {
    "policyId": "pol-paso-por-legal@1.0",
    "decision": decision,
    "principleRef": "Comercial §3",
    "correlationId": input.context.correlationId,
    "toolInvoked": input.capability.toolName,
    "requiredHop": {"domain": "legal", "outcome": "permitido"},
    "reason": "falta-salto-legal",
} if decision != "allow"
```

### Cedar

> Cedar nativo decide `permit`/`forbid`. `require-prior-hop` se modela como un `forbid` **condicionado a la ausencia del salto**: mientras no exista el salto positivo de Legal, la acción de comprometer queda prohibida; en cuanto el salto entra en el contexto, el `forbid` deja de aplicar y otra policy `permit` puede autorizar. El gateway traduce este `forbid`-por-ausencia-de-salto a la señal `require-prior-hop` del contrato.

```cedar
// Comercial §3 — "No asumimos compromisos sin pasar por Legal"
// automatabilityClass: duro · efecto: require-prior-hop · pre-invocación
// Prohíbe comprometer mientras no conste salto positivo de Legal.

forbid (
    principal,
    action == Action::"commit",
    resource
)
when {
    context.capability.canCommit == true
}
unless {
    context.legalHopPermitido == true   // un DecisionHop de dominio "legal" con outcome "permitido"
};
```

```cedar
// Mapeo de evidencia (anotación de policy, para la traza):
// @policyId("pol-paso-por-legal@1.0")
// @principleRef("Comercial §3")
// @effect("require-prior-hop")
// @requiredHop("legal:permitido")
```

> Nota Cedar: `context.legalHopPermitido` es la proyección, calculada por el gateway a partir de `decisionChain`, de la condición «existe un `DecisionHop` de dominio `legal` con `outcome == "permitido"`». Cedar no itera colecciones arbitrarias con la expresividad de Rego; por eso la cadena de saltos se pre-reduce a un booleano en el contexto. La equivalencia con el snippet Rego está cubierta por los `testVectors`.

---

## Enlaces relacionados

- Convenciones de mapping (cuerpo): [`../../convenciones-mapping-constitucion-policy.md`](../../convenciones-mapping-constitucion-policy.md)
- Plantilla de ficha (cuerpo): [`../../../../templates/federation/ficha-policy-template.md`](../../../../templates/federation/ficha-policy-template.md)
- Esquema del descriptor de identidad: [`../../esquema-identidad-agente.md`](../../esquema-identidad-agente.md)
- Esquema del bloque de contexto cultural: [`../../esquema-bloque-contexto-cultural.md`](../../esquema-bloque-contexto-cultural.md)
- Catálogo: [`./README.md`](./README.md)
- Glosario: [`../../glosario-federacion.md`](../../glosario-federacion.md)

---

*Ficha del apéndice vivo de Myrmion Federation. Material de referencia, no normativo. Las marcas y versiones citadas caducan.*
