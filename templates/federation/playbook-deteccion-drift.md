<table>
<tr>
<td width="140" valign="middle">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Playbook de detección de drift

**Versión 1.0**

*Plantilla operativa que pone a trabajar los tres patrones de detección de drift federado del cuerpo. Materializa el §3.4 del manifiesto —la federación que se observa a sí misma— y cierra el lazo entre la métrica de drift (Patrones A/B/C) y la operación real: quién la ejecuta, cada cuánto, sobre qué fuentes, contra qué umbral y qué dispara.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

Esta plantilla es la cara operativa de [patrones-deteccion-drift.md](../../docs/federation/patrones-deteccion-drift.md). El documento del cuerpo define **qué** observar, **cómo** se analiza y **qué cuenta como señal**; esta plantilla rellena lo que el cuerpo deja deliberadamente abierto: los nombres concretos, las cadencias afinadas, los umbrales acordados y la última lectura.

**Quién la rellena.** El **cuarto custodio (plataforma de federación)** es el responsable transversal de los tres patrones: ejecuta el análisis y mantiene la pipeline de observabilidad. La **custodia de cada capa** afectada aporta la lectura de su dominio y co-firma las atribuciones. La plantilla es de la plataforma; las columnas de interpretación se rellenan con los dominios.

**Estilo socrático.** Cada patrón abre con una *Pregunta guía* en cursiva. Respóndela con la realidad de tu federación antes de rellenar la tabla. Donde leas "[Espacio para rellenar]", sustituye por la decisión real de tu organización.

**Qué no hace esta plantilla.** No detecta drift por sí misma —los tres patrones son **procesos, no productos**: el dashboard, las consultas y la retención los aporta el stack a través de su plano de observabilidad (CF-05). La plantilla documenta la **operación** de esos procesos. Tampoco fija los umbrales: el cuerpo dice *qué configuración cualifica como señal*; el número exacto lo fija tu organización (o tu receta sectorial en `appendix/drift-recipes/`).

**Alcance.** Solo **drift federado** —la deriva del sistema entero. El **drift a nivel agente** (un agente que se aleja de su propio mandato) se trata en Adoption, no aquí. Cuando un patrón concentra señales en un solo `agentId`, se deriva a Adoption, no se gestiona en este playbook.

**Cadencia modulada por criticidad.** Las cadencias base de cada patrón se ajustan a la criticidad del dominio (ver §2.1 del documento del cuerpo): más frecuente para dominios de criticidad alta, menos para los de baja. Cuando una cadena cruza dominios de distinta criticidad, prevalece la más alta.

**Frecuencia de revisión de esta plantilla.** Trimestral, y siempre tras un cambio de la Constitución (que obliga a re-ejecutar el Patrón C) o un cambio de stack.

> **Mini-ejemplo embebido.** Cada campo lleva, entre comillas en cursiva, un ejemplo ilustrativo de **Consultora Modelo S.L.** sobre el corredor comercial→legal (Fonseca, del dominio Comercial, traslada un lead a Riera, del dominio Legal). Los `agentId` usan la org ficticia `consultora-modelo`. Bórralos al rellenar.

---

## 0. Metadatos del documento

> Esta sección **se excluye** del cálculo del hash de integridad (contrato de hash del [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md), §6).

| Campo | Valor |
|---|---|
| Organización (`<org>` del `agentId`) | *(p. ej. consultora-modelo)* |
| Federación / alcance cubierto | *(qué corredores y dominios cubre este playbook)* |
| Responsable del playbook (4º custodio) | *(rol o persona — plataforma de federación / SRE)* |
| Versión del documento | *(p. ej. 1.0, 1.1)* |
| Fecha de aprobación | *(YYYY-MM-DD)* |
| Próxima revisión programada | *(YYYY-MM-DD)* |
| Versión de la Constitución Corporativa de referencia (`constitutionHash`) | *(versión + hash)* |
| Versión del set de policy templates de referencia | *(p. ej. policies@2026-02)* |

---

## 1. Patrón A — Análisis de cadenas de decisiones

*Pregunta guía: ¿está cambiando **cómo se decide** a lo largo de un corredor —la forma de la cadena de `criteriaApplied`— sin que un cambio de `constitutionHash` lo explique?*

Patrón sobre el log correlacionado por `correlationId`. Reconstruye cadenas, deriva su *firma* (la secuencia de `(dominio, criteriaApplied, outcome)` por salto), la compara contra una línea base segmentada por `constitutionHash` y separa el cambio decidido del **drift genuino** (cambio de forma sin Constitución ni excepción que lo justifique). Consume metadatos de decisión, nunca el contenido del caso.

| Campo | Valor |
|---|---|
| Responsable | [Espacio para rellenar] — *p. ej. 4º custodio (plataforma); la custodia Comercial y la Legal co-firman la atribución de su corredor* |
| Cadencia | [Espacio para rellenar] — *p. ej. base mensual; quincenal para corredores que tocan criticidad alta; toda señal fuerte adelanta la ejecución* |
| Fuentes (qué loggear) | [Espacio para rellenar] — *p. ej. `correlationId`, `criteriaApplied`, `agentId` emisor/receptor, `hopCount`, `businessCaseId`, `outcome` normalizado, `constitutionHash` por salto* |
| Umbrales acordados (qué cualifica como señal) | [Espacio para rellenar] — *p. ej. firma nueva persistente sin cambio de hash; desaparición de un `policyId@version` obligatorio; acortamiento sistemático de la cadena; desplazamiento sostenido de la distribución de `outcome`. Fijar el tamaño de «persistente»* |
| Último resultado | [Espacio para rellenar] — *p. ej. 2026-05-29: en el corredor comercial→legal aparece una firma nueva persistente —`enviar_propuesta_cliente` sin el `policyId` de paso por Legal— en el 6% de las cadenas, mismo `constitutionHash`* |
| Acciones disparadas | [Espacio para rellenar] — *p. ej. revisión formal inmediata (corredor de criticidad alta); decidir entre ratificar (actualizar Constitución/policies), corregir, o registrar excepción explícita (deriva al Patrón B)* |

---

## 2. Patrón B — Análisis de excepciones

*Pregunta guía: cuando las excepciones a una misma policy se acumulan, ¿es que la **policy ha quedado desfasada** (la realidad no está mal) o que la **cultura ha drifteado** respecto a la Constitución declarada?*

Patrón sobre el [registro de excepciones](../../templates/federation/registro-excepciones.md): toda llamada que el policy engine bloqueó y la organización aprobó manualmente. Agrupa por `policyId@version` eludida, mide la tasa de excepción en ventana móvil y, para las que cruzan umbral, aplica la **clasificación binaria** (*policy* desfasada vs cultura drifteada), que dispara acciones opuestas. Recuerda: una excepción al Marco Regulatorio no es excepción, es una alerta —escala fuera de este patrón.

| Campo | Valor |
|---|---|
| Responsable | [Espacio para rellenar] — *p. ej. 4º custodio ejecuta; la custodia de la capa dueña de la policy eludida emite la clasificación binaria* |
| Cadencia | [Espacio para rellenar] — *p. ej. base mensual; quincenal y alerta por umbral para policies de criticidad alta; revisión a la primera ocurrencia si la policy protege criticidad alta* |
| Fuentes (qué loggear) | [Espacio para rellenar] — *p. ej. `correlationId`, `policyId@version` bloqueada, `agentId`/dominio origen y destino, autorizador, motivo normalizado, alcance temporal, `constitutionHash`* |
| Umbrales acordados (qué cualifica como señal) | [Espacio para rellenar] — *p. ej. tasa de excepción de una policy sobre su umbral; tendencia creciente contra la misma policy; concentración en un `agentId` (deriva a Adoption) vs dispersión (se queda aquí)* |
| Último resultado | [Espacio para rellenar] — *p. ej. 2026-05-28: la policy `pol-paso-por-legal@1.0` acumula 11 excepciones/mes en el corredor comercial→legal, motivos homogéneos —clasificada como «policy desfasada»* |
| Acciones disparadas | [Espacio para rellenar] — *p. ej. «policy desfasada» → propuesta de enmienda a la policy/Constitución; «cultura drifteada» → revisión de gobernanza + escenario nuevo para el Patrón C* |

---

## 3. Patrón C — Análisis de coherencia entre agentes

*Pregunta guía: presentado el mismo dilema, ¿resuelven dos agentes de forma **compatible con la Constitución**, o la federación carece de criterio único donde debería tenerlo?*

Patrón sobre un **banco de escenarios versionado**: dilemas representativos del contrato federado, cada uno con su resolución esperada según la Constitución vigente. Cada versión del banco declara el `constitutionHash` que valida; un cambio de Constitución lo invalida hasta revisarlo. Es coherencia **en frío** —complementa A (operación real) y B (excepciones reales). Los escenarios son sintéticos y deidentificados por contrato.

| Campo | Valor |
|---|---|
| Responsable | [Espacio para rellenar] — *p. ej. 4º custodio es dueño del banco; cada custodia de capa aporta y firma la resolución esperada de los escenarios de su dominio* |
| Cadencia | [Espacio para rellenar] — *p. ej. base trimestral; mensual para bancos de criticidad alta. **No negociable: tras cada cambio de Constitución, al alta de un agente nuevo y al cambio de bloque/descriptor*** |
| Fuentes (qué loggear) | [Espacio para rellenar] — *p. ej. banco de escenarios + `constitutionHash` evaluado; resolución efectiva de cada agente como `criteriaApplied` + `outcome` normalizado* |
| Umbrales acordados (qué cualifica como señal) | [Espacio para rellenar] — *p. ej. la coherencia es binaria por escenario: cualquier par de agentes que resuelve incompatiblemente es señal; desviación de la esperada en criticidad alta; regresión de un escenario que antes pasaba* |
| Último resultado | [Espacio para rellenar] — *p. ej. 2026-05-30: re-ejecución del banco tras la enmienda de Constitución; `urn:myrmion:agent:consultora-modelo:comercial:propuestas` y `urn:myrmion:agent:consultora-modelo:legal:dictamenes` resuelven el escenario «lead con compromiso implícito» de forma incompatible* |
| Acciones disparadas | [Espacio para rellenar] — *p. ej. incoherencia confirmada → revisión de gobernanza inmediata; regresión tras cambio de Constitución → reabrir la enmienda; desviación de un solo agente → derivar a Adoption* |

---

## 4. Consolidación y escalado

*Pregunta guía: cuando un patrón cruza su umbral, ¿quién se entera, dónde se registra, cómo se atribuye y cuándo se considera resuelto?*

| Campo | Valor |
|---|---|
| Registro de incidencias de drift | [Espacio para rellenar] — *dónde se anota cada cruce de umbral, con el patrón, la fuente y el `correlationId`/`policyId`/escenario implicado* |
| Atribución y co-firma | [Espacio para rellenar] — *4º custodio + custodia de la(s) capa(s) afectada(s); cómo se separa cambio decidido / excepción / drift genuino* |
| Ruta de escalado | [Espacio para rellenar] — *a quién se escala según severidad y criticidad del dominio; qué dispara revisión formal de la Constitución o de policies derivadas* |
| Criterio de cierre | [Espacio para rellenar] — *cuándo una incidencia se da por resuelta (enmienda aplicada, comportamiento corregido, excepción registrada, banco re-ejecutado en verde)* |
| Revisión periódica de umbrales | [Espacio para rellenar] — *cada cuánto se renegocian los umbrales de los tres patrones; coordinación con la receta sectorial de `appendix/drift-recipes/`* |

---

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Esta plantilla es la cara operativa de [patrones-deteccion-drift.md](../../docs/federation/patrones-deteccion-drift.md) (cuerpo normativo de Myrmion Federation). Materializa el §3.4 del [manifiesto de federación](../../docs/federation/manifesto.md).*

Relacionados:

- [Patrones de detección de drift](../../docs/federation/patrones-deteccion-drift.md) — la especificación de los tres patrones (estructura, método, señales, cadencia, responsable).
- [Registro de excepciones](../../templates/federation/registro-excepciones.md) — fuente del Patrón B.
- [Criterios funcionales](../../docs/federation/criterios-funcionales.md) — CF-05 (observabilidad agent-aware) habilita los tres patrones.
- [Glosario de la federación](../../docs/federation/glosario-federacion.md) — drift federado, Patrones A/B/C, `correlationId`, `criteriaApplied`.
- [Esquema del bloque de contexto cultural](../../docs/federation/esquema-bloque-contexto-cultural.md) — `correlationId`, `DecisionHop`, `criteriaApplied`, `deidTokens`.
- [Esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md) — `agentId`, criticidad del dominio, contrato de hash.
