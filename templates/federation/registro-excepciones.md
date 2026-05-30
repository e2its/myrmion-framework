<table>
  <tr>
    <td><img src="../../assets/myrmion-logo.png" alt="Myrmion" width="72"></td>
    <td>
      <strong>Myrmion Federation</strong><br>
      Plantilla — Registro de Excepciones<br>
      <em>El rastro auditable de toda excepción a una policy de gobernanza; alimenta el Patrón B de detección de drift.</em>
    </td>
  </tr>
</table>

# Myrmion Federation — Registro de Excepciones (plantilla)

**Versión 1.0**

*Materializa la gestión de excepciones del manifiesto (§5) y de [gobernanza-federada.md](../../docs/federation/gobernanza-federada.md) §3: una excepción es una llamada que el policy engine bloqueó y que la organización aprueba manualmente, y en Federation **no existe la excepción sin registro**. Este documento es el formato de ese registro — la fuente única que consume el **Patrón B** de [detección de drift](../../docs/federation/patrones-deteccion-drift.md).*

---

## Cómo usar esta plantilla

Una **excepción** es una desviación temporal y acotada de una policy de gobernanza derivada de la Constitución: una llamada inter-agente que el policy engine bloqueó y que la organización decide aprobar manualmente, con justificación, autorizador y caducidad. No es una policy nueva ni una costumbre: es una grieta consciente, con fecha de vencimiento y con nombre y apellidos de quien la autoriza. Cada excepción que se abre es deuda; cada excepción que vence sin cerrarse es deuda vencida.

Esta plantilla define el **formato del registro de excepciones** de tu federación. Reglas para usarla:

- **Copia este fichero** a tu repositorio de gobernanza. El registro es un documento vivo: una fila por excepción.
- **El registro es la fuente única.** Si una excepción no está aquí, no existe y no protege a nadie. Sin los campos obligatorios no hay aprobación: el rastro es la condición, no el subproducto (gobernanza-federada §3).
- **No borres la fila de ejemplo** hasta tener registros reales propios; sirve de referencia del formato.
- Marca con `[Espacio para rellenar]` lo que aún no sepas; vuelve a ello.
- Cuando quieras, elimina esta sección de ayuda.

> **Regla destacada — el Marco Regulatorio no admite excepciones.** Una desviación de una policy derivada de la **Constitución** puede aprobarse y se registra aquí. Un intento de aprobar una llamada bloqueada por una policy derivada del **Marco Regulatorio** (protección de datos, retención, secreto profesional, obligaciones sectoriales) **no es una excepción: es una alerta.** No abre flujo de excepción ni se anota en este registro como excepción legítima: dispara una alerta al custodio del Marco (legal/DPO) y se trata como **incidente**. El sistema no ofrece el botón de «aprobar de todos modos» para el Marco. Registrarlo aquí sería normalizar lo que la ley prohíbe (ver [gobernanza-federada.md](../../docs/federation/gobernanza-federada.md) §3).

---

## 0. Metadatos del documento

*Pregunta guía: ¿quién custodia este registro, qué ámbito cubre y desde cuándo? (Esta sección queda EXCLUIDA del cálculo del hash canónico, igual que en el resto del corpus.)*

| Campo | Valor |
|---|---|
| Organización | [Espacio para rellenar] |
| Ámbito del registro | [Espacio para rellenar: federación completa / dominio concreto] |
| Responsable del registro (4.º custodio) | [Espacio para rellenar — típicamente la plataforma de federación] |
| Versión del documento | [Espacio para rellenar] |
| Fecha de creación | [Espacio para rellenar — `AAAA-MM-DD`] |
| Última actualización | [Espacio para rellenar — `AAAA-MM-DD`] |
| Estado | [Espacio para rellenar: borrador / en revisión / vigente] |

---

## 1. Propósito y alcance del registro

*Pregunta guía: ¿qué desviaciones cubre este registro y cuáles quedan fuera? Declara explícitamente que cubre excepciones a policies derivadas de la **Constitución** (excepcionables, con rastro) y que **nunca** registra desviaciones del **Marco Regulatorio**, que se tratan como alertas e incidentes. Un registro que mezcla ambas cosas corrompe el Patrón B y normaliza la violación regulatoria.*

[Espacio para rellenar]

---

## 2. Campos del registro

*Pregunta guía: ¿qué tiene que constar en cada fila para que una excepción sea auditable y analizable? Cada excepción se anota con los campos siguientes. Son los que permiten reconstruir quién autorizó qué, para quién, sobre qué cadena, durante cuánto y por qué — y los que el Patrón B necesita para agrupar por policy eludida. Adáptalos a tu organización sin perder ninguno de los obligatorios.*

| Campo | Obligatorio | Descripción |
|---|:---:|---|
| **ID de excepción** | Sí | Identificador único y estable de la excepción (p. ej. `EXC-0001`). Nunca se reutiliza. |
| **Fecha de apertura** | Sí | Fecha en que se autoriza la excepción (`AAAA-MM-DD`). |
| **Policy violada** | Sí | La policy de gobernanza eludida, como `policyId@version`. Debe derivar de la **Constitución**: si deriva del Marco, no es excepción (es alerta). Si no apunta a una policy existente, no es excepción: es una invocación sin gobierno. |
| **Agente origen** | Sí | `agentId` del agente que invoca bajo la excepción (`urn:myrmion:agent:<org>:<dominio>:<nombre>`). |
| **Agente destino** | Sí | `agentId` del agente invocado bajo la excepción. |
| **`correlationId`** | Sí | Identificador de la cadena de decisión afectada. Es lo que enlaza la excepción con el Patrón A y permite reconstruir el caso a posteriori. |
| **Justificación** | Sí | Por qué se concede. Una frase verificable, no una intención. El Patrón B la usa normalizada para distinguir *policy* desfasada de cultura drifteada. |
| **Alcance temporal (caducidad)** | Sí | Fecha de vencimiento (`AAAA-MM-DD`). Toda excepción caduca: no hay excepción permanente. Sin caducidad no hay excepción, hay una policy encubierta. |
| **Autorizador** | Sí | Persona u órgano que la autoriza (custodio de la Constitución, o quien éste delegue). Una excepción sin nombre no es auditable. |
| **Estado** | Sí | `activa` \| `caducada` \| `revocada` \| `cerrada`. |

*(Añade aquí los campos adicionales que tu organización necesite, p. ej. `deidToken` de referencia o enlace al registro de la decisión. Las referencias a datos del caso se hacen siempre vía `deidToken`, nunca con el dato en claro.)*

---

## 3. Tabla de registro

*Pregunta guía: ¿cómo se ve una excepción bien anotada? Una fila por excepción. La primera fila es un **ejemplo ilustrativo**; sustitúyela por tus registros reales. Recuerda: si la desviación afecta al Marco Regulatorio, **no** va en esta tabla — va al canal de incidentes.*

| ID | Fecha apertura | Policy violada | Agente origen | Agente destino | `correlationId` | Justificación | Caducidad | Autorizador | Estado |
|---|---|---|---|---|---|---|---|---|---|
| EXC-0001 | 2026-05-30 | `paso-por-legal@1.2` | `urn:myrmion:agent:consultora-modelo:comercial:propuestas` | `urn:myrmion:agent:consultora-modelo:legal:dictamenes` | `550e8400-e29b-41d4-a716-446655440000` | Cierre del lead `lead-2026-0042` vence el 02/06; Riera (Legal) emite dictamen verbal favorable y autoriza continuar mientras se formaliza el `DecisionHop` de Legal. | 2026-06-06 | Riera (Legal), por delegación del custodio de la Constitución | activa |
| [Espacio para rellenar] | | | | | | | | | |

---

## 4. Ciclo de vida de una excepción

*Pregunta guía: ¿cómo nace, vive y muere una excepción en tu organización? Describe el flujo desde la solicitud hasta el cierre, y en particular qué pasa cuando una excepción caduca sin renovarse. Por defecto: nace `activa` con caducidad explícita; al llegar la caducidad pasa a `caducada` y deja de proteger; puede revocarse antes de tiempo (`revocada`); se marca `cerrada` cuando la causa que la motivó desaparece. Una excepción caducada que sigue invocándose es una invocación sin gobierno.*

[Espacio para rellenar]

---

## 5. Relación con la detección de drift (Patrón B)

*Pregunta guía: ¿cómo consume este registro el Patrón B de [detección de drift](../../docs/federation/patrones-deteccion-drift.md)? El Patrón B agrupa las excepciones por `policyId@version` eludida y mide la tasa de excepción de cada policy. Si las excepciones a la misma policy se acumulan, una de dos: o la policy ha quedado desfasada respecto a la cultura real, o la cultura real ha drifteado respecto a la Constitución declarada. Cuál de las dos es responsabilidad del custodio de la Constitución decidir — pero solo puede decidirlo si las excepciones dejaron rastro analizable aquí. Describe la cadencia de análisis y quién emite la clasificación binaria en tu organización.*

[Espacio para rellenar]

---

## 6. Higiene del registro

*Pregunta guía: ¿con qué cadencia se revisan las excepciones activas y quién responde de su limpieza? Una excepción vieja es deuda. Define cada cuánto se revisan las excepciones `activas`, cómo se mide su antigüedad, qué umbral dispara revisión obligatoria, y qué se hace con las `caducadas` que siguen apareciendo en el log de policy (señal de invocación sin gobierno).*

[Espacio para rellenar]

---

*Registro de Excepciones (plantilla) — versión 1.0. Parte del corpus normativo.*

**Relacionado:**
- Manifiesto: `../../docs/federation/manifesto.md` — §3.4 (Patrón B), §5 (gestión de excepciones), §7 (tasa de bloqueo y excepción).
- Gobernanza federada: `../../docs/federation/gobernanza-federada.md` — §3, dónde se decide qué es excepción y qué es alerta del Marco.
- Patrones de detección de drift: `../../docs/federation/patrones-deteccion-drift.md` — el Patrón B se alimenta de este registro.
- Métricas de la federación: `../../docs/federation/metricas-federacion.md` — M6 (tasa de bloqueo y excepción) tiene aquí su fuente.
- Glosario de la federación: `../../docs/federation/glosario-federacion.md` — definición canónica de *excepción* y de los patrones A/B/C.
- Criterios funcionales: `../../docs/federation/criterios-funcionales.md` — CF-03 (policy engine) define la `policyId@version` que rellena «policy violada».
- Ficha de policy (plantilla): `./ficha-policy-template.md` — la policy de la que una excepción se desvía.
- Ejemplo de extremo a extremo: `../../examples/federation/corredor-comercial-legal/` — el corredor comercial→legal del que sale la excepción de ejemplo.
