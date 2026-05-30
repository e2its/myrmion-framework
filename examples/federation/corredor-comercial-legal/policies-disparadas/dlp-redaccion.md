# Policy disparada en el salto 1 — DLP / redacción en la ruta

*Qué policy se disparó cuando el agente comercial calificó el lead, y con qué efecto. Materializa [CF-06](../../../../docs/federation/criterios-funcionales.md) y el campo `deidTokens` del [bloque de contexto cultural](../../../../docs/federation/esquema-bloque-contexto-cultural.md) §5.*

---

## Contexto

- **Salto:** 1 (origen: agente comercial; la cadena nace aquí).
- **`correlationId`:** `550e8400-e29b-41d4-a716-446655440000`
- **`businessCaseId`:** `lead-2026-0042`
- **Tool invocada:** `calificar_lead` (`sideEffectClass: escritura`, `dataClassesTouched: ["C2", "C3"]`).
- **Quién originó:** una persona del equipo comercial (Fonseca), referenciada en el bloque solo como seudónimo opaco `usr_op4q7x2k` — nunca PII directa.

## Qué se disparó

`pol-dlp-pii@2.0`, derivada del principio cultural *"los datos personales de cliente se seudonimizan antes de salir del dominio"* ([convenciones de mapping](../../../../docs/federation/convenciones-mapping-constitucion-policy.md); implementación por dialecto en [`appendix/policy-templates/dlp-pii-phi.md`](../../../../docs/federation/appendix/policy-templates/dlp-pii-phi.md)).

El lead entrante contenía el NIF del contacto del cliente. La capa de des-identificación en la ruta (CF-06) detectó la categoría *identificador fiscal* en los argumentos de la tool **antes** de que alcanzaran el modelo.

## Efecto

- **Decisión de policy:** `redact` (redacción **reversible**).
- El NIF se sustituyó por el marcador opaco `«NIF_1»` en los argumentos.
- Se emitió un `deidToken` que el bloque transporta a partir de este salto:

  ```json
  { "token": "«NIF_1»", "scope": "cadena:550e8400-e29b-41d4-a716-446655440000", "ttl": "PT1H" }
  ```

- **Regla dura:** el token **nunca** contiene el valor original. Es un puntero a un vault del stack; el NIF solo se re-identifica **en el agente de origen** (el comercial), dentro del `ttl`, al componer la respuesta final. El agente legal trabaja siempre con `«NIF_1»`, nunca con el NIF real.
- **`outcome` registrado en el `DecisionHop` del salto 1:** `redactado`.

## Por qué importa

Este es exactamente el hueco que Adoption no podía cubrir: en Adoption pura no hay punto de inserción para la redacción inline en la ruta del prompt. En Federation, la ruta inter-agente **es** ese punto ([Guía de protección de datos](../../../../docs/adoption/guia-proteccion-datos.md) §3.4). El dato sensible nunca cruza la frontera de dominio en claro, pero la cadena sigue siendo operativa porque el origen puede re-identificar la respuesta.

---

*Artefacto del [ejemplo del corredor comercial→legal](../README.md). No es normativo: ilustra el comportamiento descrito en [CF-06](../../../../docs/federation/criterios-funcionales.md).*
