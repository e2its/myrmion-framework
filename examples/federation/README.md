# Myrmion Federation — Ejemplos

**Versión 1.0**

*Materializa, sobre un caso end-to-end, las cuatro capas (§3) y los criterios (§4) del [manifiesto](../../docs/federation/manifesto.md): un corredor real entre dos dominios, validable contra los esquemas del corpus.*

Esta carpeta no añade normativa. Toma lo que las specs definen como contrato —identidad de agente, bloque de contexto cultural, gate de coherencia, ciclo de vida— y lo pone a funcionar sobre un caso concreto y reproducible. Si una spec dice "el bloque crece, nunca se reescribe", aquí se ve crecer salto a salto. Todo lo que aparece es **vendor-neutral**: roles funcionales y contratos, nunca productos.

## El caso de referencia

La organización de ejemplo es **Consultora Modelo S.L.**. El caso es el **corredor comercial→legal**: llega un *lead*, el agente `comercial:propuestas` (custodio **Fonseca**) prepara una propuesta y necesita que el agente `legal:dictamenes` (custodio **Riera**) valide cláusulas antes de enviarla. Cruzar la frontera Comercial → Legal es justo donde la federación tiene que aportar identidad verificable, contexto propagado y trazabilidad.

> Toda la `<org>` de los ejemplos es ficticia (`consultora-modelo`). El framework nunca hardcodea una organización real: cada organización fija su propio segmento `<org>` en el `agentId`. El segmento `<nombre>` nombra la **función** del agente (`propuestas`, `dictamenes`), no a la persona: Fonseca y Riera son los custodios humanos (`owner`).

## Índice

### Caso end-to-end

- **[Corredor comercial→legal](./corredor-comercial-legal/README.md)** — el recorrido completo del caso: descriptores de `comercial:propuestas` y `legal:dictamenes`, el bloque de contexto cultural propagándose y el veredicto trazado extremo a extremo.

### Diagramas (Mermaid, vendor-neutral)

- **[Secuencia del corredor](./diagramas/secuencia-corredor.md)** — los tres saltos Comercial → Legal con la propagación del bloque de contexto cultural y el encadenado de `DecisionHop`.
- **[Gate de coherencia del registro](./diagramas/gate-coherencia-registro.md)** — el alta de un agente: cómo el descriptor pasa (o no) las compuertas de identidad, hash y capacidades antes de ser descubrible.
- **[Ciclo de vida del agente](./diagramas/ciclo-vida-agente.md)** — los estados gobernados: propuesto → activo → deprecated → retirado.

## Cómo encajan los diagramas

Los tres diagramas cuentan la misma historia en tres tiempos:

1. **Antes del corredor** — el [gate de coherencia](./diagramas/gate-coherencia-registro.md) admite a `legal:dictamenes` en el registro y lo hace descubrible.
2. **Durante el corredor** — la [secuencia](./diagramas/secuencia-corredor.md) muestra a `comercial:propuestas` descubriéndolo, invocándolo con contexto y recibiendo un veredicto trazado.
3. **A lo largo del tiempo** — el [ciclo de vida](./diagramas/ciclo-vida-agente.md) gobierna cuándo `legal:dictamenes` deja de aceptar nuevos corredores y cómo se le da salida sin romper los que ya están en curso.

## Cómo validar estos ejemplos contra el corpus

Los ejemplos son comprobables, no decorativos. Cada artefacto debe casar con su contrato:

| Artefacto del ejemplo | Contrato contra el que se valida |
|-----------------------|----------------------------------|
| `agentId` de `comercial:propuestas` y `legal:dictamenes` | [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md) — forma `urn:myrmion:agent:<org>:<dominio>:<nombre>` |
| `hash` de cada descriptor | contrato de hash: `"sha256:"` sobre la forma canónica (NFC + LF + sin *trailing whitespace* + excluida la sección "0. Metadatos") |
| Bloque de contexto cultural y sus `DecisionHop` | [esquema del bloque de contexto cultural](../../docs/federation/esquema-bloque-contexto-cultural.md) |
| Uso de `deidTokens` en el salto a Legal | [esquema del bloque de contexto cultural](../../docs/federation/esquema-bloque-contexto-cultural.md) — sin datos personales en claro |
| Las compuertas del gate | [criterios funcionales](../../docs/federation/criterios-funcionales.md) — CF-01 (capacidades), CF-04 (identidad verificable) |

---

*Ejemplos de Myrmion Federation — versión 1.0. Parte del corpus normativo.*

**Relacionado:** [manifiesto](../../docs/federation/manifesto.md) · [guía de arquitectura funcional](../../docs/federation/guia-arquitectura-funcional.md) · [criterios funcionales](../../docs/federation/criterios-funcionales.md) · [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md) · [esquema del bloque de contexto cultural](../../docs/federation/esquema-bloque-contexto-cultural.md)
