# Señal de drift — Patrón B sobre `pol-cifras-sin-finanzas`

*Una señal de drift federado detectada por el [Patrón B](../../../docs/federation/patrones-deteccion-drift.md): acumulación de excepciones a la misma policy. Materializa el §3.4 del [manifiesto](../../../docs/federation/manifesto.md) (análisis de excepciones). No es normativo: es una salida de ejemplo del análisis sobre el registro de Consultora Modelo S.L.*

---

## Qué detectó el Patrón B

El Patrón B se ejecuta sobre el [registro de excepciones](../../../templates/federation/registro-excepciones.md). Su disparador: si las excepciones a la **misma policy** se acumulan por encima de un umbral en una ventana, hay que revisar — o la policy está desfasada, o la cultura real ha drifteado respecto a la Constitución declarada.

- **Policy señalada:** `pol-cifras-sin-finanzas@1.1`.
- **Ventana:** trimestre en curso (2026-Q2).
- **Umbral configurado para criticidad media:** 3 excepciones / trimestre.
- **Excepciones acumuladas:** 3 → **umbral alcanzado, dispara revisión.**

| Excepción | Fecha | `correlationId` | Patrón común |
|---|---|---|---|
| EX-2026-006 | 2026-04-12 | `9f1c…a201` | descuento dentro de acuerdo marco; finanzas confirma a posteriori |
| EX-2026-011 | 2026-05-08 | `b73d…44e0` | descuento dentro de acuerdo marco; finanzas confirma a posteriori |
| EX-2026-014 | 2026-05-30 | `550e8400-e29b-41d4-a716-446655440000` | descuento dentro de acuerdo marco; finanzas confirma a posteriori |

Las tres comparten el mismo patrón: clientes con **acuerdo marco vigente** donde el descuento ya está pre-aprobado, y donde el paso por finanzas que la policy exige resulta sistemáticamente redundante.

## Diagnóstico

El patrón no apunta a una cultura desviada: apunta a una **policy desfasada**. `pol-cifras-sin-finanzas@1.1` no distingue entre cifras libres y cifras ya amparadas por un acuerdo marco. La cultura real ("respetamos los acuerdos marco ya negociados con finanzas") es coherente con la Constitución; la policy simplemente no la codifica.

Cuál de las dos está mal —la policy o la cultura— es responsabilidad de la **custodia** decidir (manifiesto §3.4). En este caso, la custodia de la Constitución y el cuarto custodio (plataforma de federación) concluyen que la policy es la que ha quedado corta.

## Acción

- **Revisión propuesta de la policy:** `pol-cifras-sin-finanzas@1.2`, que añade una condición de exención cuando la cadena referencia un acuerdo marco vigente con endorsement de finanzas ya registrado, eliminando la necesidad de excepción manual repetida.
- **No se relaja el principio:** las cifras fuera de acuerdo marco siguen exigiendo paso por finanzas. Lo que cambia es que el caso ya cubierto deja de generar fricción.
- **Trazabilidad:** la revisión se documenta como decisión de gobernanza y, si altera un principio de la Constitución, se propaga al ecosistema Adoption (manifiesto §6, Fase 5).

## Por qué importa

Este es el bucle de aprendizaje que el framework promete: el bloqueo de [`policies-disparadas/bloqueo-cifras.md`](./policies-disparadas/bloqueo-cifras.md) generó una [excepción trazable](./excepcion/EX-2026-014.md), la excepción se acumuló con otras dos, y el Patrón B convirtió esa acumulación en una señal accionable. La excepción no es un fallo del sistema: es su sensor.

---

*Artefacto del [ejemplo del corredor comercial→legal](./README.md). El patrón canónico es el [Patrón B](../../../docs/federation/patrones-deteccion-drift.md); su fuente, el [registro de excepciones](../../../templates/federation/registro-excepciones.md).*
