<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Ficha de Policy (ejemplo)

**Versión 1.0**

*Ejemplo rellenado de la [plantilla de ficha de policy](./ficha-policy-template.md): la entrada `pol-paso-por-legal` del catálogo, ilustrada con el corredor comercial→legal de la organización ficticia **Consultora Modelo S.L.**. Es el envoltorio **neutral** de la policy «No asumimos compromisos sin pasar por Legal»: dice qué hace y por qué, sin escribir dialecto. La serialización ejecutable por dialecto vive en la [ficha homónima del apéndice](../../docs/federation/appendix/policy-templates/paso-por-legal.md).*

</td>
</tr>
</table>

---

> **Este es un ejemplo rellenado.** Conserva las preguntas guía en cursiva para que se vea cómo se respondieron. Úsalo como referencia de tono y nivel de detalle, no como policy lista para producción: el snippet ejecutable y la verificación de vigencia están en el apéndice.

---

## 0. Metadatos del documento

*Esta sección queda EXCLUIDA del cálculo del hash canónico, igual que en el resto del corpus.*

| Campo | Valor |
|---|---|
| `id` de la policy | `pol-paso-por-legal` |
| Título legible | Paso obligatorio por Legal antes de comprometer a la organización |
| `version` de la policy (semver) | 1.0 |
| Organización | Consultora Modelo S.L. (`consultora-modelo`) |
| Custodio funcional | Constitución Corporativa (transformación digital) |
| Custodio de aplicación | Plataforma de Federación de Consultora Modelo |
| Fecha de última revisión | 2026-05-30 |
| Estado | Vigente |

---

## 1. `id`

*Pregunta guía: ¿con qué identificador estable se referencia esta policy desde el catálogo, desde el `criteriaApplied` de los `DecisionHop` y desde otras fichas?*

`pol-paso-por-legal`

En el `criteriaApplied` de un `DecisionHop` aparece sufijado con la versión: `pol-paso-por-legal@1.0`.

---

## 2. `origen` y `principioDeOrigen`

*Pregunta guía: ¿de qué capa de gobernanza deriva esta policy y qué principio la justifica?*

- **`origen`:** `constitucion` — es un principio cultural (el paso por Legal), por tanto **excepcionable** con justificación, alcance temporal y autorizador (gobernanza §3). No es del Marco.
- **Cita del principio:** «No asumimos compromisos sin pasar por Legal.»
- **Localización (§):** Constitución del dominio Comercial de Consultora Modelo S.L. — § 3 (Principios de comportamiento).

Lectura: ninguna capacidad que pueda comprometer a la organización (firmar, prometer condiciones, aceptar una cláusula) puede ejecutarse si en la cadena de decisión no consta antes un salto por un agente del dominio Legal con resultado positivo.

---

## 3. `automatabilityClass`

*Pregunta guía: ¿hasta qué punto este principio se puede materializar en regla sin pérdida de fidelidad?*

Clase elegida: **`duro`**. El cumplimiento se decide con una condición booleana exacta sobre campos declarados, sin margen de interpretación: el disparador (`capability.canCommit == true`) es exacto y el efecto (`require-prior-hop`) es determinista. No hay umbral, hay condición.

Que la clase sea `duro` no significa que la policy juzgue el fondo jurídico: garantiza que el salto por Legal **ocurrió con resultado positivo**; *qué* dictaminó Legal es trabajo de modelado del agente Legal, no de esta regla. La policy impone el corredor; no sustituye la revisión.

---

## 4. `disparador`

*Pregunta guía: ¿qué condición observable indica que este principio aplica a este salto?*

- **Campos del descriptor de identidad que intervienen:** `capabilities[].canCommit` de la tool invocada por el agente emisor (equivalentemente, `capabilities[].sideEffectClass == "compromiso"`).
- **Campos del bloque de contexto cultural que intervienen:** `decisionChain` y sus `DecisionHop` (se inspecciona en busca de un salto del dominio `legal` con `outcome == "permitido"` sobre la misma cadena, identificada por `correlationId`).
- **Condición que activa la policy:** concurren las dos condiciones — (1) `capability.canCommit == true`; y (2) en `decisionChain` **no** existe ningún `DecisionHop` cuyo `agentId` pertenezca al dominio `legal` con `outcome == "permitido"`. El dominio de un salto se deriva del quinto segmento del `agentId` (`urn:myrmion:agent:<org>:<dominio>:<nombre>`).

---

## 5. `efecto`

*Pregunta guía: cuando el disparador se cumple, ¿cuál de los cuatro efectos normativos impone la policy?*

Efecto elegido: **`require-prior-hop`**. La colaboración queda condicionada a que conste en `decisionChain` un `DecisionHop` previo de un agente del dominio `legal` con `outcome == "permitido"` sobre esta misma cadena. Una vez ese salto consta, la siguiente evaluación de la regla deja de dispararse y la decisión pasa a las demás reglas (que pueden terminar en `allow`). No es un `deny`: encarrila el corredor de gobierno, no cierra la puerta.

---

## 6. `evidenciaRequerida`

*Pregunta guía: ¿qué rastro auditable deja la evaluación?*

Anclada al `DecisionHop` del salto:

- En `criteriaApplied`: el identificador de esta policy como `pol-paso-por-legal@1.0`.
- En `outcome`: `escalado` cuando se exige el salto previo (la llamada no procede hasta que Legal intervenga).
- En la traza de la decisión: `correlationId`, `agentId` del emisor, `toolInvoked` y el motivo `falta-salto-legal`.
- El salto exigido, como `{ dominio: "legal", outcome: "permitido" }`.

Cuando el salto por Legal finalmente ocurre, su propio `DecisionHop` se incorpora a `decisionChain` y se convierte, él mismo, en evidencia del corredor recorrido. Esa convención es la que hace analizable el Patrón A de detección de drift.

---

## 7. `puntoDeAplicacion`

*Pregunta guía: ¿en qué momento del ciclo de la llamada se evalúa?*

`pre-invocación` — antes de que la tool de compromiso se ejecute (los efectos `allow`, `deny` y `require-prior-hop` se deciden en pre-invocación). Se evalúa en el **gateway de llamadas inter-agente** ([CF-01](../../docs/federation/criterios-funcionales.md)), antes de enrutar; quién evalúa es el policy engine ([CF-03](../../docs/federation/criterios-funcionales.md)), sin que el cuerpo prescriba cuál.

---

## 8. `reversibilidad`

*Pregunta guía: si la policy aplica un efecto y luego resulta improcedente, ¿se puede deshacer?*

- **Reversibilidad:** reversible.
- **Cómo se revierte (o por qué no se puede):** el efecto solo encarrila el enrutado; no transforma ni destruye el artefacto. Si la exigencia de salto resultó improcedente, basta con registrar el `DecisionHop` legal con `outcome == "permitido"` y reintentar; el contenido de la propuesta permanece intacto.

---

## 9. `caveats`

*Pregunta guía: ¿qué sabe quien diseñó esta policy que los campos anteriores no capturan? Incluye el comportamiento ante el fallo.*

- **No juzga el fondo.** La policy garantiza que Legal intervino con resultado positivo; no garantiza que la cláusula sea correcta. Ese juicio es trabajo de modelado del agente Legal.
- **Dominio del salto, no agente concreto.** La regla exige un agente *del dominio* `legal` (quinto segmento del `agentId`), no un `agentId` fijo, para no acoplarse a una instancia. Si la Constitución exige un agente legal concreto, parametrízalo.
- **Vigencia del salto.** El salto de Legal se trata como válido para la cadena identificada por `correlationId`. Si la materia cambia sustancialmente tras el salto (otra cláusula, otro alcance), conviene invalidarlo. Qué es «cambio sustancial» es constitucional, no de policy.
- **Interacción con otras fichas.** Si la propuesta contiene datos identificables, puede aplicar además una ficha de des-identificación ([CF-06](../../docs/federation/criterios-funcionales.md)) que emita `deidTokens`. Esta ficha no cubre ese caso; redáctalo aparte y enlázalo.
- **Comportamiento ante el fallo (degradación segura).** Si el bloque no trae `decisionChain` cuando `hopCount > 1` (debería traerla siempre), o si falta `canCommit` en el descriptor, la regla no puede evaluarse con fidelidad: el resultado por defecto es `deny` con evidencia, nunca `allow` en silencio (lo decide el policy engine, [CF-03](../../docs/federation/criterios-funcionales.md); convenciones §3, paso 6).

---

## 10. `testVectors`

*Pregunta guía: ¿con qué pares entrada→efecto esperado se demuestra que cualquier implementación (en cualquier dialecto) mantiene la fidelidad de la regla?*

| # | Entrada (campos relevantes del corpus) | Efecto esperado |
|---|---|---|
| TV-1 | `capability.canCommit == true`; `decisionChain` sin salto del dominio `legal`. | `require-prior-hop` |
| TV-2 | `capability.canCommit == true`; `decisionChain` con un `DecisionHop` del dominio `legal` y `outcome == "permitido"`. | (no dispara) → cede a otras reglas |
| TV-3 | `capability.canCommit == true`; `decisionChain` con un `DecisionHop` del dominio `legal` y `outcome == "bloqueado"`. | `require-prior-hop` (el salto bloqueado no satisface el corredor) |
| TV-4 | `capability.canCommit == false`. | (no dispara) |
| TV-5 | `capability.canCommit == true`; falta `decisionChain` con `hopCount > 1`. | `deny` (degradación segura) |

> Ilustración con Consultora Modelo S.L.: el agente de **Fonseca** (Comercial), `urn:myrmion:agent:consultora-modelo:comercial:propuestas`, invoca una tool con `canCommit == true` sobre el lead `lead-2026-0042` y la cadena no incluye salto de Legal → sale `require-prior-hop`. Tras el salto del agente de **Riera** (Legal), `urn:myrmion:agent:consultora-modelo:legal:dictamenes`, con `outcome == "permitido"`, TV-2 aplica y la llamada puede continuar. Ver el [flujo de extremo a extremo](../../examples/federation/corredor-comercial-legal/).

---

## 11. `refImplementaciones[]`

*Pregunta guía: ¿dónde están las serializaciones por dialecto de esta policy?*

- [`../../docs/federation/appendix/policy-templates/paso-por-legal.md`](../../docs/federation/appendix/policy-templates/paso-por-legal.md) — ficha del apéndice con los snippets de referencia por dialecto y su banner de vigencia.

> El cuerpo de esta ficha es neutral de dialecto. El snippet ejecutable para cada motor de políticas se remite al apéndice; aquí no se incluye ninguna serialización.

---

*Ficha de policy de Myrmion Federation (ejemplo) — versión 1.0. Parte del corpus normativo. Su plantilla en blanco es [`ficha-policy-template.md`](./ficha-policy-template.md); su materialización por dialecto vive en el [apéndice](../../docs/federation/appendix/policy-templates/paso-por-legal.md). Ver también las [convenciones de mapping](../../docs/federation/convenciones-mapping-constitucion-policy.md), el [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md), el [esquema del bloque de contexto cultural](../../docs/federation/esquema-bloque-contexto-cultural.md) y el [ejemplo del corredor comercial→legal](../../examples/federation/corredor-comercial-legal/).*
