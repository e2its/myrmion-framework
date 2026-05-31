# Policy disparada al cierre del corredor — bloqueo de cifras sin finanzas

*Qué policy **bloqueó** el envío de la propuesta y con qué efecto. Es el bloqueo del ejemplo: la cadena no procede y se abre la vía de excepción. Materializa la decisión `deny` de [CF-03](../../../../docs/federation/criterios-funcionales.md) sobre una tool con `externalizes: true`, según el patrón de [`appendix/policy-templates/cifras-sin-finanzas.md`](../../../../docs/federation/appendix/policy-templates/cifras-sin-finanzas.md).*

---

## Contexto

- **Punto de la cadena:** cierre del corredor. El legal ya validó la cláusula (salto 2, `outcome: permitido`), de modo que el paso por legal exigido por [`exigir-paso-legal.md`](./exigir-paso-legal.md) ya está satisfecho.
- **`correlationId`:** `550e8400-e29b-41d4-a716-446655440000`.
- **Tool que el comercial intenta invocar:** `enviar_propuesta_cliente` (`externalizes: true`, `comunicacion-externa`).

## Qué se disparó

`pol-cifras-sin-finanzas@1.1`, derivada del principio cultural *"cifras financieras no se exteriorizan sin pasar por finanzas"*.

La policy detecta tools de comunicación externa (`externalizes: true`) cuyos argumentos contienen patrones financieros. La propuesta de Fonseca incluía un **descuento del 22 %** sobre tarifa y un **importe total comprometido** que superaba el umbral que la Constitución reserva a endorsement de finanzas. La `decisionChain` **no** contenía un paso por el dominio finanzas con `outcome: permitido`.

Pseudo-policy neutral (ilustrativa):

```
IF capability.externalizes == true
AND args MATCH patron-financiero(importe | descuento)
AND NOT decisionChain.contains(hop WHERE domain_of(hop.agentId) == "finanzas" AND hop.outcome == "permitido")
THEN deny
```

## Efecto

- **Decisión de policy:** `deny` — **bloqueo terminal**.
- `enviar_propuesta_cliente` **no se ejecutó**. La propuesta no salió al cliente.
- El bloque registró el corte: se rellenó `escalationContext` con el motivo (`cifras financieras sin endorsement de finanzas`), el agente que escala (`comercial:propuestas`) y la evidencia (el bloque completo de la cadena).
- **`outcome` registrado:** `bloqueado`.

## Resolución

La cabeza comercial valoró que el descuento estaba dentro de la autonomía pactada para este cliente recurrente y solicitó aprobación manual. El bloqueo se levantó mediante una **excepción registrada**, no relajando la policy: ver [`excepcion/EX-2026-014.md`](../excepcion/EX-2026-014.md).

Que el bloqueo se resuelva por excepción y no por cambio de policy es deliberado: la excepción **deja rastro** y alimenta el [Patrón B de drift](../../../../docs/federation/patrones-deteccion-drift.md). Si excepciones como ésta se acumulan, la señal no es que la realidad esté mal, sino que la policy ha quedado desfasada — exactamente lo que documenta [`senal-drift.md`](../senal-drift.md).

## Por qué importa

Este es el bloqueo que el ejemplo necesita mostrar: una policy puede **denegar** una llamada inter-agente y la cadena se detiene. El sistema no improvisa: o se cumple la condición (paso por finanzas) o se abre una excepción trazable. No hay tercera vía silenciosa.

---

*Artefacto del [ejemplo del corredor comercial→legal](../README.md). No es normativo: ilustra el comportamiento descrito en [CF-03](../../../../docs/federation/criterios-funcionales.md).*
