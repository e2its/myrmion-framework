# Ficha de policy — Cifras sin Finanzas

> **Banner de vigencia.** Ficha del **apéndice vivo**. Menciona dialectos y motores concretos, por tanto **caduca**. Verifica la versión del dialecto antes de usar.
>
> | Campo | Valor |
> |-------|-------|
> | Última revisión | 2026-05-30 |
> | Dialectos | Rego (OPA), Cedar |
> | Efecto principal | `deny` |
> | `automatabilityClass` | `blando` |
> | Punto de aplicación | pre-invocación |

> **Nota de versión.** Esta ficha documenta la policy base `pol-cifras-sin-finanzas@1.0`. El [ejemplo end-to-end](../../../../examples/federation/corredor-comercial-legal/) ejecuta la versión vigente `@1.1` (la organización la endureció) y la [señal de drift](../../../../examples/federation/corredor-comercial-legal/senal-drift.md) propone evolucionar a `@1.2`. La divergencia es **deliberada**: ilustra el ciclo de vida de una policy (ver [ADR-0002](../../adr/0002-decisiones-de-revision-de-coherencia.md), D3).

---

## Principio de origen

> **«No se exteriorizan cifras financieras sin pasar por Finanzas.»**

- **Origen:** Constitución del dominio Comercial — § 5 (Datos sensibles y restricciones), reforzado por la Constitución del dominio Finanzas — § 3.
- **Lectura:** ninguna tool que **saque información fuera del dominio/organización** puede ejecutarse si sus argumentos contienen **cifras financieras** (precios, márgenes, descuentos, condiciones económicas) y en la cadena no consta un respaldo (endorsement) de Finanzas.
- Es el segundo patrón canónico que el manifiesto §3.3 cita: «detecta tools de comunicación externa y bloquea si los argumentos contienen patrones financieros sin endorsement de finanzas».

Trazabilidad constitucional: esta ficha implementa Comercial §5 y Finanzas §3 (manifiesto §5; convenciones §5).

## `automatabilityClass`: `blando`

A diferencia del paso por Legal, esta regla no es booleana exacta: depende de un **detector de patrón financiero** sobre los argumentos, que admite falso positivo y falso negativo (convenciones §2, clase BLANDO). El umbral del detector es un parámetro de la ficha, no una constante oculta. Por eso la regla exige **defensa en profundidad**: el bloqueo en pre-invocación se refuerza con la marca de evidencia para revisión posterior (Patrón B de drift) y, donde aplique, con la des-identificación de la ficha [`./dlp-pii-phi.md`](./dlp-pii-phi.md).

> La policy impide la fuga; no calcula el número correcto. *Qué* cifra es defendible lo decide Finanzas mediante su endorsement.

---

## Disparador

La regla se activa cuando concurren las dos condiciones (convenciones §3, paso 2):

1. **La capacidad invocada externaliza.** En el **descriptor de identidad**, la `Capability` de la tool declara:

   ```
   capability.externalizes == true
   ```

   (o `capability.sideEffectClass == "comunicacion-externa"`).

2. **Hay patrón financiero en los argumentos.** El detector de patrón financiero (clasificador o reglas, externo al contrato) marca presencia de cifra financiera por encima del umbral configurado:

   ```
   input.detector.financialPattern == true
   ```

Y **no** consta respaldo de Finanzas:

3. En `decisionChain` del **bloque de contexto cultural** no existe ningún `DecisionHop` cuyo `agentId` sea de dominio `finanzas` con `outcome == "permitido"`.

El dominio de un salto se deriva del `agentId` (quinto segmento del URN `urn:myrmion:agent:<org>:<dominio>:<nombre>`).

> Nota de contrato: el efecto aquí es `deny`, no `require-prior-hop`. La diferencia es deliberada y sigue el manifiesto §3.3, que para este principio dice «bloquea». Exteriorizar sin respaldo no es un paso que falte en un corredor: es una acción que **no debe ocurrir tal cual**. El camino correcto (obtener el endorsement de Finanzas) se recorre **antes**, por iniciativa del agente. Una organización que prefiera encarrilar en vez de cortar puede cambiar el efecto a `require-prior-hop`; esta ficha documenta la variante estricta.

---

## Efecto

- **Decisión:** `deny`.
- **Alcance:** se deniega la **externalización**, no el trabajo interno. El agente puede seguir trabajando la cifra dentro del dominio; lo que no puede es **sacarla** sin respaldo.
- **Salida del bloqueo:** obtener un `DecisionHop` de Finanzas con `outcome == "permitido"` sobre la cadena (`correlationId`). Con el endorsement presente, la condición 3 deja de cumplirse y la regla no se dispara.

`deny` es uno de los cuatro efectos del contrato (convenciones §3, paso 3); deja evidencia y detiene la externalización en el gateway.

---

## Evidencia

Cada `deny` deja evidencia, anclada al `DecisionHop` (convenciones §3, paso 4):

- En `criteriaApplied`: `pol-cifras-sin-finanzas@1.0`.
- En `outcome`: `bloqueado`.
- En la traza: `correlationId`, `agentId` del emisor, `toolInvoked`, motivo `cifra-externa-sin-endorsement`, y el **tipo** de patrón detectado (p. ej. `importe-con-divisa`, `descuento-pct`).
- El respaldo que faltaba: `{ dominio: "finanzas", outcome: "permitido" }`.

Principio de cautela: la evidencia registra el **tipo** de patrón financiero, no la cifra en claro si esa cifra es sensible. Si hace falta referenciar el valor, se hace por su `deidToken` (ver la ficha DLP). Esto conecta con la regla de privacidad por construcción del bloque (esquema del bloque §6).

---

## Punto de aplicación

- **Cuándo:** **pre-invocación** — en el momento de la externalización, sobre los argumentos ya resueltos, antes de que la tool ejecute (convenciones §3, paso 5).
- **Dónde:** en el gateway de llamadas inter-agente ([CF-01](../../criterios-funcionales.md)), que es el punto único por el que la externalización cruza.
- **Quién evalúa:** el policy engine ([CF-03](../../criterios-funcionales.md)), alimentado por un detector de patrón financiero cuyo resultado llega como `input.detector.financialPattern`.

---

## Caveats

- **Calidad del detector (lo que hace `blando` esta regla).** Un falso negativo deja pasar la fuga; un falso positivo bloquea de más. El detector vive **fuera** del contrato: la policy consume su veredicto. Versiona y mide el detector aparte, y combina controles (defensa en profundidad).
- **Cifras no numéricas.** Un dato financiero puede no ser una cifra (p. ej. «aplicaremos el mejor precio de mercado»). Esta regla, basada en patrón, no lo captura; complétala con detección semántica si tu riesgo lo exige.
- **Endorsement caduco.** Igual que en «Paso por Legal», un endorsement de Finanzas vale para la materia tal como era al respaldarla. Si la cifra cambia tras el endorsement, invalídalo. La definición de «cambio sustancial» es constitucional.
- **Frontera de externalización.** `externalizes` la declara el modelador del agente en el descriptor (decidible en tiempo de diseño): la policy la consume como booleano, no la infiere en runtime.
- **Degradación segura.** Si falta el campo `externalizes` en el descriptor o no se puede ejecutar el detector, la regla no se evalúa con fidelidad: el resultado por defecto es `deny` con evidencia (convenciones §3, paso 6).

---

## `testVectors`

| # | Entrada (resumen) | Salida esperada |
|---|-------------------|-----------------|
| TV-1 | `externalizes == true`; `financialPattern == true`; sin salto `finanzas:permitido`. | `deny` |
| TV-2 | `externalizes == true`; `financialPattern == true`; con `DecisionHop` `finanzas` `outcome == "permitido"`. | (no dispara) → cede a otras reglas |
| TV-3 | `externalizes == true`; `financialPattern == false`. | (no dispara) |
| TV-4 | `externalizes == false`; `financialPattern == true` (uso interno). | (no dispara) |
| TV-5 | `externalizes == true`; `financialPattern == true`; `DecisionHop` `finanzas` `outcome == "bloqueado"`. | `deny` (un salto bloqueado no es endorsement) |
| TV-6 | `externalizes == true`; detector no disponible. | `deny` (degradación segura) |

> Ejemplo ilustrativo (`Consultora Modelo S.L.`): el agente de **Fonseca** (Comercial), `urn:myrmion:agent:consultora-modelo:comercial:propuestas`, intenta enviar a la contraparte una propuesta con un descuento del 18% sin respaldo de Finanzas. Sale `deny` con patrón `descuento-pct`. Tras el `DecisionHop` del agente de Finanzas con `outcome == "permitido"`, TV-2 aplica y la externalización puede continuar (sujeta al resto de reglas, incluidas las de paso por Legal y DLP). Ver [`../../../../examples/federation/corredor-comercial-legal/`](../../../../examples/federation/corredor-comercial-legal/).

---

## Snippets

> Los snippets leen `input.capability` (la `Capability` de la tool, del descriptor), `input.context` (el bloque de contexto cultural) e `input.detector` (resultado del detector de patrón financiero). El nombre/valor concreto de los campos en el transporte lo define el [mapeo de transporte](../mapeo-transporte/). `domain_of` extrae el quinto segmento del `agentId`.

### Rego (OPA)

```rego
package myrmion.federation.cifras_sin_finanzas

import future.keywords.if
import future.keywords.in

# Comercial §5 + Finanzas §3 — "No se exteriorizan cifras financieras sin pasar por Finanzas"
# automatabilityClass: blando · efecto: deny · pre-invocación

domain_of(agent_id) := d if {
    parts := split(agent_id, ":")
    d := parts[4]
}

externalizing if input.capability.externalizes == true

has_financial_pattern if input.detector.financialPattern == true

# ¿Existe respaldo (endorsement) de Finanzas en esta cadena?
finance_endorsement if {
    some hop in input.context.decisionChain
    domain_of(hop.agentId) == "finanzas"
    hop.outcome == "permitido"
}

# Decisión: denegar externalización de cifras sin respaldo
decision := "deny" if {
    externalizing
    has_financial_pattern
    not finance_endorsement
}

# Degradación segura: si el detector no está disponible y la tool externaliza, denegar
decision := "deny" if {
    externalizing
    not input.detector.available
}

evidence := {
    "policyId": "pol-cifras-sin-finanzas@1.0",
    "decision": "deny",
    "principleRef": "Comercial §5; Finanzas §3",
    "correlationId": input.context.correlationId,
    "toolInvoked": input.capability.toolName,
    "reason": "cifra-externa-sin-endorsement",
    "detectedPattern": input.detector.patternType,   # tipo, NUNCA el valor en claro
    "missingEndorsement": {"domain": "finanzas", "outcome": "permitido"},
} if decision == "deny"
```

### Cedar

> Aquí el `forbid` de Cedar coincide directamente con el efecto del contrato (`deny`): prohíbe la externalización con patrón financiero salvo que conste el endorsement de Finanzas.

```cedar
// Comercial §5 + Finanzas §3 — "No se exteriorizan cifras financieras sin pasar por Finanzas"
// automatabilityClass: blando · efecto: deny · pre-invocación

forbid (
    principal,
    action == Action::"externalize",
    resource
)
when {
    context.detector.financialPattern == true
}
unless {
    context.financeEndorsed == true   // un DecisionHop de dominio "finanzas" con outcome "permitido"
};
```

```cedar
// Mapeo de evidencia (anotación de policy, para la traza):
// @policyId("pol-cifras-sin-finanzas@1.0")
// @principleRef("Comercial §5; Finanzas §3")
// @effect("deny")
// @reason("cifra-externa-sin-endorsement")
```

> Nota Cedar: `context.financeEndorsed` es la proyección, calculada por el gateway a partir de `decisionChain`, de «existe un `DecisionHop` de dominio `finanzas` con `outcome == "permitido"`». El propio `Action::"externalize"` ya implica `externalizes == true`, por lo que no hace falta repetir esa condición. La equivalencia con el snippet Rego está cubierta por los `testVectors`.

---

## Enlaces relacionados

- Convenciones de mapping (cuerpo): [`../../convenciones-mapping-constitucion-policy.md`](../../convenciones-mapping-constitucion-policy.md)
- Plantilla de ficha (cuerpo): [`../../../../templates/federation/ficha-policy-template.md`](../../../../templates/federation/ficha-policy-template.md)
- Esquema del descriptor de identidad: [`../../esquema-identidad-agente.md`](../../esquema-identidad-agente.md)
- Esquema del bloque de contexto cultural: [`../../esquema-bloque-contexto-cultural.md`](../../esquema-bloque-contexto-cultural.md)
- Ficha relacionada (des-identificación): [`./dlp-pii-phi.md`](./dlp-pii-phi.md)
- Catálogo: [`./README.md`](./README.md)
- Glosario: [`../../glosario-federacion.md`](../../glosario-federacion.md)

---

*Ficha del apéndice vivo de Myrmion Federation. Material de referencia, no normativo. Las marcas y versiones citadas caducan.*
