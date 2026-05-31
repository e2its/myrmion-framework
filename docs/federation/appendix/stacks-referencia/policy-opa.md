# Myrmion Federation — Ficha de stack: «OPA (Open Policy Agent)»

**Versión 1.0**

*Materializa el contrato de desacoplamiento del [apéndice vivo](../README.md): una ficha fechada que evalúa un componente concreto contra los [criterios funcionales CF-01..CF-06](../../criterios-funcionales.md), sin contaminar el cuerpo normativo.*

---

> ## Banner de vigencia
>
> | Campo | Valor |
> | --- | --- |
> | **Componente** | OPA (Open Policy Agent) — lenguaje Rego |
> | **Versión evaluada** | rolling (releases regulares y predecibles) |
> | **Fecha de revisión** | 2026-05 |
> | **Revisor(es)** | comunidad |
> | **Próxima revisión recomendada** | 2026-11 |
> | **Estado** | vigente |
> | **Licencia (a la fecha)** | Apache-2.0 |
> | **Fuente upstream** | https://www.openpolicyagent.org/ |
>
> *Esta ficha caduca. Si la fecha de revisión es anterior a 6 meses respecto a hoy, trátala como `stale` aunque el campo Estado diga lo contrario. Lo normativo está en el cuerpo ([`../../criterios-funcionales.md`](../../criterios-funcionales.md)), no aquí.*

---

## 1. Qué es y qué rol cubre

Open Policy Agent (OPA) es un motor de políticas de propósito general que decide, ante una consulta de autorización, si una acción se permite o se deniega. Las políticas se escriben en un lenguaje declarativo (Rego) y se evalúan en el momento de la consulta, fuera de la lógica de la aplicación que pregunta. Su rol en la federación es el de **policy engine** (CF-03).

---

## 2. Matriz de cobertura CF-01..CF-06

| Criterio | Cobertura | Justificación (qué punto de la checklist cumple / qué le falta) |
| --- | :---: | --- |
| **CF-01** — gateway de llamadas inter-agente | ○ | No intercepta tráfico; decide, pero no media. Necesita un gateway que le consulte. |
| **CF-02** — service registry federado | ○ | No provee catálogo de agentes; a lo sumo puede ser el motor que filtra uno externo por identidad. |
| **CF-03** — policy engine | ● | Motor de políticas separado de los agentes; evalúa la decisión en runtime, lenguaje declarativo (Rego), versionado de bundles con auditoría de cambios, latencia sub-milisegundo en el caso normal. Cumple la checklist de CF-03. |
| **CF-04** — identity provider (autenticación mutua con identidad criptográfica verificable) | ○ | Consume identidades como entrada para decidir; no las emite ni las verifica criptográficamente. |
| **CF-05** — observabilidad agent-aware | ○ | Ajeno; emite logs de decisión, no trazas de cadena de llamadas. |
| **CF-06** — des-identificación / DLP en la ruta | ○ | No des-identifica datos; puede decidir sobre datos ya tratados, pero no realiza la sustitución. |

> Recuerda: ninguna pieza única cubre los seis criterios. OPA es deliberadamente solo CF-03.

---

## 3. Cómo se integra con MCP

OPA no habla MCP: es un motor de decisión que el gateway MCP consulta (como sidecar, como librería embebida o como servicio) antes de dejar pasar una invocación. No requiere extensiones de protocolo, en línea con el manifiesto §8. El input de la consulta (atributos del emisor, del receptor y del contexto, incluidos campos del [descriptor de identidad](../../esquema-identidad-agente.md) y del [bloque de contexto cultural](../../esquema-bloque-contexto-cultural.md)) lo construye el gateway.

> Las implementaciones de los patrones de [mapping Constitución → policy](../../convenciones-mapping-constitucion-policy.md) en dialecto Rego van a [`../policy-templates/`](../policy-templates/), no en esta ficha.

---

## 4. Pros

- Cubre CF-03 de forma completa y madura: motor externo, decisión en tiempo de invocación, políticas declarativas y versionables.
- Rego es expresivo y permite políticas finas sobre cualquier entrada estructurada (JSON), no solo sobre roles.
- Agnóstico de dominio: el mismo motor sirve para autorizar invocaciones de agentes, acceso a APIs o admisión en clústeres.
- Ecosistema grande, integraciones abundantes y proyecto graduado de la CNCF: madurez y continuidad sólidas.
- El bundle de políticas se distribuye y versiona como artefacto, lo que facilita auditoría y control de cambios.

---

## 5. Contras

- Solo cubre CF-03: hay que combinarlo con un gateway (CF-01) que lo consulte y con el resto de piezas de la federación.
- Rego tiene una curva de aprendizaje real; las políticas complejas pueden ser difíciles de leer y depurar.
- La decisión es tan buena como la información que se le pasa: el diseño del input es trabajo del integrador.
- Como punto de decisión en el camino de cada invocación, su disponibilidad y latencia deben gobernarse.

---

## 6. Madurez

| Señal | Lectura |
| --- | --- |
| Estabilidad de API / versionado | Madura. |
| Cadencia de releases | Regular y predecible. |
| Tamaño / actividad de comunidad | Amplia; proyecto graduado de la CNCF con adopción industrial extensa. |
| Casos de producción conocidos | Numerosos, en múltiples sectores. |
| Calidad de documentación | Alta. |

**Veredicto de madurez:** consolidado.

---

## 7. Riesgo de continuidad (M&A / cambio de licencia / abandono)

| Vector de riesgo | Nivel | Notas |
| --- | :---: | --- |
| Adquisición / M&A | bajo | Proyecto de fundación; el respaldo comercial existe pero no controla la licencia. |
| Cambio de licencia (open → source-available / comercial) | bajo | Apache-2.0 bajo gobernanza de fundación. |
| Abandono / *bus factor* | bajo | Comunidad amplia y diversa. |
| Dependencia de un único *vendor* | bajo | No depende de un único fabricante. |
| Gobernanza (proyecto individual vs. fundación) | bajo | Graduado de la CNCF. |

**Plan de salida si el riesgo se materializa:** el cuerpo solo exige el criterio funcional. CF-03 puede cubrirse con otro policy engine declarativo (ver [`policy-cedar.md`](./policy-cedar.md)). Sustituirlo no toca la especificación, aunque sí obliga a reescribir las políticas al nuevo dialecto.

---

## 8. Veredicto

A la fecha de revisión, es la opción de referencia para CF-03 cuando se valora madurez, neutralidad de fundación y expresividad. El gateway de la federación (ver [`ibm-contextforge.md`](./ibm-contextforge.md) o [`agentgateway.md`](./agentgateway.md)) consulta a OPA antes de dejar pasar cada invocación. En el [caso del corredor comercial→legal](../../../../examples/federation/corredor-comercial-legal/), una política Rego podría exigir que solo los agentes del dominio comercial autorizados puedan invocar al agente de Legal para pedir revisión de una propuesta, y denegar el resto: el gateway hace la consulta, OPA toma la decisión.

---

### Enlaces relacionados

- [Apéndice vivo — matriz global y contrato de desacoplamiento](../README.md)
- [Criterios funcionales (CF-01..CF-06)](../../criterios-funcionales.md) — definición normativa de las columnas.
- [Regla anti-acoplamiento](../../regla-anti-acoplamiento.md) — por qué esta ficha vive en el apéndice y no en el cuerpo.
- [Convenciones de mapping Constitución → policy](../../convenciones-mapping-constitucion-policy.md) y [policy templates](../policy-templates/) — donde van las implementaciones por dialecto.

*Ficha de stack — versión 1.0. Parte del corpus en su estructura; el contenido que se rellene es informativo y caduca.*
