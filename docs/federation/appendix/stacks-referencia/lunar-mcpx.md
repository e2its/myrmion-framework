<table>
<tr>
<td><img src="../../../../assets/myrmion-logo.png" alt="Myrmion" width="72"></td>
<td><b>Myrmion Federation — Apéndice vivo · Ficha de stack</b><br/>Lunar.dev MCPX</td>
</tr>
</table>

> **Banner de vigencia** — Última revisión: **2026-05** · Revisor: comunidad. El apéndice envejece rápido: verifica las afirmaciones contra la documentación oficial del proyecto antes de decidir. Esta ficha es orientativa, no una recomendación normativa (ver [regla anti-acoplamiento](../../regla-anti-acoplamiento.md)).

---

## Qué es

Lunar.dev MCPX es un gateway/proxy para MCP que intermedia las llamadas a servidores MCP y añade control operativo (observabilidad, control de acceso, agregación de servidores). En el vocabulario de Federation se evalúa, sobre todo, como candidato para **CF-01 (gateway de llamadas inter-agente)**.

## Cobertura de criterios funcionales

Matriz frente a los [criterios funcionales](../../criterios-funcionales.md) (✓ cubre · ◐ parcial/depende de configuración o componente adicional · ✗ no es su ámbito):

| CF | Criterio | Cobertura | Nota |
|---|---|---|---|
| **CF-01** | Gateway de llamadas inter-agente | ✓ | Intermedia llamadas MCP; punto natural para insertar gobernanza en la ruta. Verifica que propaga metadatos arbitrarios sin truncarlos (transporte del bloque, ver [mapeo-transporte/mcp.md](../mapeo-transporte/mcp.md)). |
| **CF-02** | Service registry federado | ◐ | Agrega/descubre servidores MCP; comprueba si admite descriptores extendidos (dominio, criticidad, versión de Constitución) o si requiere un registry aparte. |
| **CF-03** | Policy engine | ◐ | Aporta puntos de control de acceso; para policy declarativa versionada con auditoría suele combinarse con un policy engine dedicado. |
| **CF-04** | Identity provider | ✗ | Fuera de su ámbito; se delega en el IdP del entorno. |
| **CF-05** | Observabilidad agent-aware | ◐ | Ofrece observabilidad de tráfico MCP; verifica correlación de cadenas por `correlationId` y exportación a backends estándar. |
| **CF-06** | Des-identificación / DLP en la ruta | ◐ | Comprueba si integra des-identificación nativa o si hay que añadir un motor vendor-neutral en la ruta. |

## Pros

- Pensado específicamente para intermediar y operar tráfico MCP (encaja con CF-01 sin adaptaciones forzadas).
- Agregación de múltiples servidores MCP tras un único punto de control.
- Observabilidad de tráfico incluida, útil como base de CF-05.

## Contras / a vigilar

- No cubre por sí solo identidad criptográfica (CF-04) ni, según versión, policy declarativa con auditoría (CF-03): probable necesidad de componer con otros componentes.
- Verifica la madurez del soporte de des-identificación en la ruta (CF-06) antes de apoyar en él la política de datos.

## Madurez y riesgo

- **Madurez:** proyecto activo del ecosistema MCP (2025–2026); valida el estado de releases y soporte en su repositorio oficial.
- **Riesgo de M&A / abandono:** ecosistema joven y en consolidación; mantén la elección detrás de los CF para poder sustituirlo sin tocar el cuerpo del framework.

---

*Ficha de apéndice (vivo/comunidad). Para el contrato funcional que esta herramienta debe cumplir, ver siempre [criterios-funcionales.md](../../criterios-funcionales.md). Plantilla de ficha: [_plantilla-entrada-stack.md](../_plantilla-entrada-stack.md).*
