# Myrmion Federation — Registro de decisiones de arquitectura (ADR)

**Versión 1.0**

*Materializa la gobernanza del manifiesto (§5): toda decisión que dé forma a la federación deja rastro auditable, igual que exige CF-06 para las decisiones federadas en tiempo de ejecución.*

---

## Qué es esto

Un **ADR** (Architecture Decision Record, registro de decisión de arquitectura) es un documento corto que captura **una** decisión que da forma a la federación: el contexto en el que se tomó, la decisión en sí, las alternativas descartadas y las consecuencias que asume.

El corpus de Myrmion Federation lleva su propio rastro de decisiones por el mismo motivo por el que exige trazabilidad a los agentes (CF-06): una decisión sin registro es una decisión que nadie puede revisar, refutar ni heredar. Lo que pedimos a la federación, nos lo aplicamos a nosotros.

Los ADR son **inmutables**: una decisión no se edita, se **supera** con un ADR posterior que la deja obsoleta. El historial completo —incluidos los errores— es parte del valor.

---

## Cuándo abrir un ADR

Abre un ADR cuando una decisión cumpla **al menos una** de estas condiciones:

- **Toca un contrato**: cambia o restringe el descriptor de agente, el bloque de contexto cultural, el contrato de hash o cualquier esquema normativo.
- **Toca un criterio funcional**: añade, reinterpreta o relaja un criterio (CF-01 a CF-06).
- **Toca un principio**: tensiona uno de los tres principios del manifiesto §2 (compositividad sobre infraestructura existente, cultura propagable, drift como métrica de primera clase). Toda tensión con un principio **exige** ADR, sin excepción.
- **Es difícil de revertir**: la decisión condiciona decisiones futuras o sería costosa de deshacer.
- **Hubo desacuerdo genuino**: existían alternativas defendibles y se eligió una. El ADR conserva por qué.

No abras un ADR para: correcciones de redacción, reorganización de ficheros sin cambio de contrato, o detalles de implementación de un producto concreto (eso vive en `../appendix/`, no en el cuerpo).

Ante la duda, **abre el ADR**. Un ADR de más es barato; una decisión sin rastro es cara.

---

## Numeración

Los ADR se numeran con cuatro dígitos y un título en *kebab-case*: `NNNN-titulo-en-minusculas.md`.

| Rango | Ámbito | Ejemplo |
|---|---|---|
| `0000` | Plantilla (esta carpeta) | `0000-plantilla-adr.md` |
| `0001`–`0099` | **Framework**: decisiones sobre el cuerpo normativo, los contratos, los criterios funcionales y la arquitectura de capas. | `0001-layout-plano-del-corpus.md` |
| `0100`+ | **Adopción**: decisiones sobre plantillas, guías y material de adopción que no alteran el cuerpo normativo. | `0100-orden-de-las-fases-de-adopcion.md` |

El número se asigna en orden de creación y **no se reutiliza**, igual que un `agentId` no se recicla. Si un ADR queda obsoleto, su número sigue ocupado: el rastro se conserva.

---

## Estados de un ADR

Todo ADR declara su **estado** en la sección de Estado:

- **Propuesto** — redactado, en discusión, aún no adoptado.
- **Aceptado** — adoptado; gobierna el corpus.
- **Obsoleto** — superado por un ADR posterior, que se enlaza. No se borra.
- **Rechazado** — se discutió y se decidió no adoptarlo. Se conserva por su valor de contexto.

Un cambio de estado **no edita** el ADR original más allá de su línea de Estado y el enlace al ADR que lo supera. La decisión histórica permanece legible.

---

## Cómo escribir un ADR

1. Copia `0000-plantilla-adr.md`.
2. Asígnale el siguiente número libre del rango que corresponda (framework o adopción).
3. Rellena todas las secciones, incluida la de **principios**: cada ADR declara cómo respeta o tensiona los tres principios del manifiesto §2. Esto no es opcional.
4. Añádelo al índice de abajo.
5. Ábrelo a discusión en estado **Propuesto**; pásalo a **Aceptado** cuando se adopte.

---

## Índice

> Mantén este índice en orden de número. Una fila por ADR, sin excepción.

### Framework (0001–0099)

| ADR | Título | Estado |
|---|---|---|
| — | _(aún no hay ADR de framework)_ | — |

### Adopción (0100+)

| ADR | Título | Estado |
|---|---|---|
| — | _(aún no hay ADR de adopción)_ | — |

---

## Relacionados

- [Plantilla de ADR](./0000-plantilla-adr.md)
- [Manifiesto](../manifesto.md) — los tres principios (§2) y la gobernanza (§5).
- [Criterios funcionales](../criterios-funcionales.md) — CF-06 (trazabilidad), el espejo en tiempo de ejecución de lo que aquí hacemos con las decisiones de diseño.
- [La regla anti-acoplamiento](../regla-anti-acoplamiento.md) — los ADR del cuerpo son agnósticos; las decisiones sobre productos concretos viven en `../appendix/`.

---

*Myrmion Federation — Registro de decisiones de arquitectura, versión 1.0. Parte del corpus normativo.*
