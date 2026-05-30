# Policy disparada en el salto 2 — exigir paso por legal

*Qué policy obligó al corredor a pasar por legal antes de poder comprometer, y con qué efecto. Materializa la decisión `require-prior-hop` de [CF-03](../../../../docs/federation/criterios-funcionales.md) y el patrón canónico de [`appendix/policy-templates/paso-por-legal.md`](../../../../docs/federation/appendix/policy-templates/paso-por-legal.md).*

---

## Contexto

- **Salto:** 2 (origen: agente comercial → destino: agente legal).
- **`correlationId`:** `550e8400-e29b-41d4-a716-446655440000` (el mismo de toda la cadena).
- **Tool que el comercial quería invocar al final del corredor:** `enviar_propuesta_cliente`, declarada en su descriptor con `canCommit: true` y `externalizes: true`.

## Qué se disparó

`pol-paso-por-legal@1.0`, derivada del principio cultural *"no asumimos compromisos sin pasar por legal"*.

El policy engine evaluó la `decisionChain` de la cadena y comprobó que **no contenía aún** un paso por el dominio legal con `outcome: permitido`. Como `enviar_propuesta_cliente` tiene `canCommit: true`, la policy exige que ese paso exista antes de ejecutar el compromiso.

Pseudo-policy neutral (ilustrativa; el dialecto vive en el apéndice):

```
IF capability.canCommit == true
AND NOT decisionChain.contains(hop WHERE hop.domain == "legal" AND hop.outcome == "permitido")
THEN require-prior-hop("legal")
```

## Efecto

- **Decisión de policy:** `require-prior-hop("legal")`.
- La policy **no bloqueó la propuesta de forma terminal**: la condicionó. El efecto operativo es que el corredor no puede saltar directo a `enviar_propuesta_cliente`; primero tiene que invocar al agente legal.
- Esto es precisamente lo que produce el **salto 2**: el comercial invoca `validar_clausula` en el agente legal, propagando el bloque actualizado (`hopCount: 2`, `decisionChain` con el eslabón del salto 1).
- **Validación de compatibilidad previa:** el agente legal comparó el `constitutionHash` del bloque (`sha256:c0n5717uc10n3000...`) contra su `compatibleConstitutionHashes`. **Hubo match** (ambos agentes heredan de la Constitución 3.0), así que la llamada procedió sujeta a policy.
- Una vez el legal emite el dictamen con `emitir_dictamen` y `outcome: permitido`, la cadena ya contiene el paso por legal exigido y el comercial podrá ejecutar `enviar_propuesta_cliente` (sujeto al resto de policies — ver [bloqueo de cifras](./bloqueo-cifras.md)).

## Por qué importa

Sin esta policy, el agente comercial podría comprometer a la organización sin validación jurídica, contradiciendo aguas abajo lo que la Constitución exige. La policy convierte un principio cultural en una precondición verificable de la cadena, no en una buena intención.

---

*Artefacto del [ejemplo del corredor comercial→legal](../README.md). No es normativo: ilustra el comportamiento descrito en [CF-03](../../../../docs/federation/criterios-funcionales.md).*
