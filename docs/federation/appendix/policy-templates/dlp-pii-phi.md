# Ficha de policy — Des-identificación en la ruta (PII/PHI)

> **Banner de vigencia.** Ficha del **apéndice vivo**. Menciona dialectos y motores concretos, por tanto **caduca**. Verifica la versión del dialecto antes de usar.
>
> | Campo | Valor |
> |-------|-------|
> | Última revisión | 2026-05-30 |
> | Dialectos | Rego (OPA), Cedar |
> | Efecto principal | `redact` (des-identificación reversible con `deidToken`) |
> | `automatabilityClass` | `blando` |
> | Punto de aplicación | pre-invocación |

---

## Principio de origen

> **«Los datos identificables viajan des-identificados; la re-identificación solo en el agente de origen.»**

- **Origen:** Constitución del dominio (transversal) — § 5 (Datos sensibles y restricciones). Aplica a todo dominio que maneje datos personales (PII) o de salud (PHI).
- **Lectura:** cuando una llamada inter-agente lleva en sus argumentos datos identificables, esos datos se **redactan en la ruta** antes de que alcancen el modelo. Cuando la redacción es reversible, se emite un `deidToken` que el bloque de contexto cultural transporta para re-identificar la respuesta **solo en el agente de origen**.
- Es el tercer patrón canónico del manifiesto §3.3 (*«los datos personales de cliente se seudonimizan antes de salir del dominio»*) y el criterio [CF-06](../../criterios-funcionales.md): el que cierra el hueco de enforcement que Adoption no podía cubrir, porque la ruta inter-agente **es** el punto de inserción de la redacción inline.

Trazabilidad constitucional: esta ficha implementa el principio transversal §5 (manifiesto §5; convenciones §5).

## `automatabilityClass`: `blando`

La regla depende de un **clasificador de sensibilidad** (PII/PHI) sobre los argumentos, que admite falso positivo y falso negativo (convenciones §2, clase BLANDO). El umbral de sensibilidad es un parámetro de la ficha. La defensa en profundidad combina: control de `dataClassesTouched` en el descriptor (pre-invocación), redacción efectiva en la ruta, y evidencia de qué se redactó. El falso negativo es el riesgo grave (dato en claro que viaja), por eso el comportamiento ante el fallo es `deny`.

---

## Disparador

La regla se activa cuando concurren las dos condiciones (convenciones §3, paso 2):

1. **La capacidad invocada toca datos sensibles.** En el **descriptor de identidad**, la `Capability` de la tool declara clases de dato que el Marco Regulatorio clasifica como PII/PHI:

   ```
   capability.dataClassesTouched ∩ {clases PII/PHI} ≠ ∅
   ```

2. **El clasificador detecta dato identificable sin redactar en los argumentos.** El detector de sensibilidad (externo al contrato) marca presencia de un campo PII/PHI que **aún no** viaja como `deidToken`:

   ```
   input.detector.sensitiveFields ≠ ∅
   ```

La regla **no** se activa por la presencia de `deidTokens` ya colocados: si el dato ya viaja como token, el principio ya se cumple.

> A diferencia de las otras dos fichas, el disparador aquí no mira `decisionChain` (no exige un salto previo): mira los **argumentos** de esta llamada. La des-identificación es una transformación de la ruta, no un corredor de gobierno.

---

## Efecto

- **Decisión:** `redact` — uno de los cuatro efectos del contrato (convenciones §3, paso 3).
- **Transformación:** cada campo identificable se sustituye por un `deidToken` antes de que los argumentos alcancen el modelo. El `redact` se aplica **sobre los argumentos**, dejándolos des-identificados.
- **Reversibilidad:** cuando la redacción es reversible, el `deidToken` se añade a `deidTokens` del bloque, con `{ token, scope, ttl }`. El valor original vive en un vault del stack, **nunca en el token**; se recupera **solo en el agente de origen**, dentro del `ttl` (esquema del bloque §5).
- **Si la transformación no puede aplicarse** (no hay servicio de tokenización, o un campo identificable no puede redactarse), la decisión degrada a `deny`: es preferible cortar a dejar viajar el dato en claro.

> Cuando la redacción es **irreversible**, no hay `deidToken`: el dato se ha ido y no vuelve (esquema del bloque §5). Esta ficha cubre el caso reversible, que es el que el bloque transporta.

---

## Evidencia

Cada decisión deja evidencia, anclada al `DecisionHop` (convenciones §3, paso 4):

- En `criteriaApplied`: `pol-dlp-pii@2.0`.
- En `outcome`: `redactado` (o `bloqueado` si la transformación falla).
- En la traza: `correlationId`, `agentId` del emisor, `toolInvoked`, y la lista de campos redactados como `{ field, sensitivity, token }` — **los tokens, nunca los valores originales**.

Principio de oro de esta ficha, alineado con la privacidad por construcción del bloque (esquema del bloque §6): **la evidencia jamás contiene el dato identificable en claro**. Si la evidencia necesita referirse al dato, lo hace por su `deidToken`. Una evidencia que filtra el PII/PHI viola el mismo principio que pretende hacer cumplir.

---

## Punto de aplicación

- **Cuándo:** **pre-invocación** — la des-identificación ocurre **antes** de que los argumentos alcancen el modelo ([CF-06](../../criterios-funcionales.md): «redacta, tokeniza o bloquea según la categoría, en la ruta, antes de la invocación al modelo»).
- **Dónde:** en el gateway de llamadas inter-agente ([CF-01](../../criterios-funcionales.md)) con la des-identificación/DLP en la ruta ([CF-06](../../criterios-funcionales.md)).
- **Quién evalúa:** el policy engine ([CF-03](../../criterios-funcionales.md)) decide *que* hay que redactar y *qué* campos; el motor de des-identificación vendor-neutral ([CF-06](../../criterios-funcionales.md)) ejecuta la sustitución; el vault del stack custodia la correspondencia `token → valor`. La policy orquesta; no guarda secretos.

---

## Caveats

- **Calidad del clasificador (lo que hace `blando` esta regla).** El detector de PII/PHI vive fuera del contrato. Un falso negativo deja viajar dato en claro: por eso el modo seguro ante fallo es `deny`.
- **Reversibilidad ≠ acceso libre.** Que el `deidToken` sea reversible no relaja el control: la re-identificación solo ocurre en el agente de origen, dentro del `ttl`, contra el vault gobernado. Esta ficha no cubre la operación de re-identificación.
- **Tokens estables vs. por cadena.** Un `deidToken` estable para un mismo dato permite correlación entre cadenas (útil y, a la vez, riesgo de re-identificación). Un token con `scope` por cadena (`scope: "cadena:<correlationId>"`) evita la correlación pero impide unir hilos. La elección es constitucional, no de policy; documéntala.
- **No es la autenticación de la llamada.** La des-identificación en la ruta es ortogonal a la autenticación mutua con identidad criptográfica verificable ([CF-04](../../criterios-funcionales.md)): una protege el *contenido sensible*, la otra protege el *canal y la identidad*. Hacen falta las dos.
- **PHI puede exigir más.** Algunos marcos regulatorios de datos de salud exigen mínimos adicionales (retención, jurisdicción). Esta ficha cubre la des-identificación en la ruta; no agota el cumplimiento. La capa técnica completa está en la [Guía de protección de datos](../../../adoption/guia-proteccion-datos.md) de Adoption.
- **Degradación segura.** Si el servicio de tokenización no responde o un campo no puede redactarse, la decisión es `deny`, nunca dejar pasar en claro (convenciones §3, paso 6).

---

## `testVectors`

| # | Entrada (resumen) | Salida esperada |
|---|-------------------|-----------------|
| TV-1 | `dataClassesTouched` con clase PII; `sensitiveFields` con un campo sin tokenizar; tokenización disponible. | `redact` (campo → `deidToken` en `deidTokens`) |
| TV-2 | `dataClassesTouched` con clase PHI; `sensitiveFields` no vacío; tokenización disponible. | `redact` |
| TV-3 | argumentos ya tokenizados (todos los campos sensibles son `deidToken`); `sensitiveFields` vacío. | (no dispara) → cede a otras reglas |
| TV-4 | `dataClassesTouched` sin clases PII/PHI; sin campos sensibles. | (no dispara) |
| TV-5 | PII presente, pero el servicio de tokenización no responde. | `deny` (degradación segura) |

> Ejemplo ilustrativo (`Consultora Modelo S.L.`): el agente de **Fonseca** (Comercial), `urn:myrmion:agent:consultora-modelo:comercial:propuestas`, invoca al agente de **Riera** (Legal), `urn:myrmion:agent:consultora-modelo:legal:dictamenes`, sobre el lead `lead-2026-0042`. Los argumentos incluyen el NIF y el correo del contacto del cliente (PII). La regla redacta esos campos: el NIF viaja como `deidToken` `{ token: "«NIF_1»", scope: "cadena:550e8400…", ttl: "PT1H" }`. Riera trabaja sobre tokens; la respuesta final se re-identifica solo en el agente de Fonseca. La evidencia registra los tokens, nunca los valores. Ver [`../../../../examples/federation/corredor-comercial-legal/`](../../../../examples/federation/corredor-comercial-legal/).

---

## Snippets

> Los snippets leen `input.capability` (la `Capability` de la tool, del descriptor), `input.context` (el bloque de contexto cultural) e `input.detector` (resultado del clasificador de sensibilidad). La **transformación** (colocar los `deidToken`) la ejecuta el motor de des-identificación; la policy decide *que* hay que redactar y *qué* campos. El nombre/valor concreto de los campos en el transporte lo define el [mapeo de transporte](../mapeo-transporte/).

### Rego (OPA)

```rego
package myrmion.federation.dlp_pii_phi

import future.keywords.if
import future.keywords.in

# Transversal §5 — "Los datos identificables viajan des-identificados" (CF-06)
# automatabilityClass: blando · efecto: redact · pre-invocación

sensitive_classes := {"pii", "phi"}

touches_sensitive if {
    some c in input.capability.dataClassesTouched
    c in sensitive_classes
}

# Campos identificables detectados aún sin tokenizar
fields_to_redact[f] if {
    some f in input.detector.sensitiveFields
    not f.deidToken
}

needs_redaction if {
    touches_sensitive
    count(fields_to_redact) > 0
}

# Decisión: redactar (des-identificar) los campos detectados
decision := "redact" if {
    needs_redaction
    input.detector.tokenizationAvailable == true
}

# Degradación segura: si no se puede tokenizar, no viaja
decision := "deny" if {
    needs_redaction
    not input.detector.tokenizationAvailable
}

# Instrucción de transformación que el motor de des-identificación ejecuta
transform := {"redact": [f.field | some f in fields_to_redact]} if decision == "redact"

evidence := {
    "policyId": "pol-dlp-pii@2.0",
    "decision": decision,
    "principleRef": "Transversal §5",
    "correlationId": input.context.correlationId,
    "toolInvoked": input.capability.toolName,
    # Solo nombre y sensibilidad del campo; el valor original NUNCA entra aquí
    "redactedFields": [{"field": f.field, "sensitivity": f.sensitivity} | some f in fields_to_redact],
} if needs_redaction
```

### Cedar

> Cedar no transforma datos: decide. Modelamos esta ficha como un `permit` **condicionado a que la des-identificación esté garantizada** y un `forbid` que corta si no se puede tokenizar. La sustitución por `deidToken` la ejecuta el motor de des-identificación tras el `permit`; el gateway traduce ese `permit`-con-redacción-garantizada al efecto `redact` del contrato.

```cedar
// Transversal §5 — "Los datos identificables viajan des-identificados" (CF-06)
// automatabilityClass: blando · efecto: redact · pre-invocación

// Corta si hay PII/PHI sin redactar y NO se puede des-identificar.
forbid (
    principal,
    action == Action::"invokeWithSensitiveData",
    resource
)
when {
    context.detector.carriesSensitive == true     // hay campo pii/phi sin tokenizar
}
unless {
    context.detector.tokenizationAvailable == true
};

// Permite la invocación cuando la des-identificación está garantizada por el motor de la ruta.
permit (
    principal,
    action == Action::"invokeWithSensitiveData",
    resource
)
when {
    context.detector.redactionGuaranteed == true  // el motor des-identificará antes de invocar
};
```

```cedar
// Mapeo de evidencia (anotación de policy, para la traza):
// @policyId("pol-dlp-pii@2.0")
// @principleRef("Transversal §5")
// @effect("redact")
// @rule("evidence.redactedFields NUNCA contiene valores en claro")
```

> Nota Cedar: `context.detector.carriesSensitive`, `context.detector.tokenizationAvailable` y `context.detector.redactionGuaranteed` son proyecciones que el gateway calcula a partir del clasificador y del estado del servicio de tokenización. La **transformación** (colocar los `deidToken`) no la expresa Cedar: la ejecuta el motor de des-identificación, que materializa el efecto `redact` del contrato. La equivalencia con el snippet Rego está cubierta por los `testVectors`.

---

## Enlaces relacionados

- Convenciones de mapping (cuerpo): [`../../convenciones-mapping-constitucion-policy.md`](../../convenciones-mapping-constitucion-policy.md)
- Plantilla de ficha (cuerpo): [`../../../../templates/federation/ficha-policy-template.md`](../../../../templates/federation/ficha-policy-template.md)
- Esquema del bloque de contexto cultural (`DeidToken`): [`../../esquema-bloque-contexto-cultural.md`](../../esquema-bloque-contexto-cultural.md)
- Esquema del descriptor de identidad (`dataClassesTouched`): [`../../esquema-identidad-agente.md`](../../esquema-identidad-agente.md)
- Criterio CF-06 (DLP en la ruta): [`../../criterios-funcionales.md`](../../criterios-funcionales.md)
- Ficha relacionada (externalización financiera): [`./cifras-sin-finanzas.md`](./cifras-sin-finanzas.md)
- Catálogo: [`./README.md`](./README.md)
- Glosario: [`../../glosario-federacion.md`](../../glosario-federacion.md)

---

*Ficha del apéndice vivo de Myrmion Federation. Material de referencia, no normativo. Las marcas y versiones citadas caducan.*
