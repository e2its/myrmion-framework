# Myrmion Federation — Ficha de stack: «IBM ContextForge (MCP Gateway)»

**Versión 1.0**

*Materializa el contrato de desacoplamiento del [apéndice vivo](../README.md): una ficha fechada que evalúa un componente concreto contra los [criterios funcionales CF-01..CF-06](../../criterios-funcionales.md), sin contaminar el cuerpo normativo.*

---

> ## Banner de vigencia
>
> | Campo | Valor |
> | --- | --- |
> | **Componente** | IBM ContextForge (MCP Gateway / `mcp-context-forge`) |
> | **Versión evaluada** | rolling (releases frecuentes alineadas con la evolución de MCP) |
> | **Fecha de revisión** | 2026-05 |
> | **Revisor(es)** | comunidad |
> | **Próxima revisión recomendada** | 2026-11 |
> | **Estado** | vigente |
> | **Licencia (a la fecha)** | Apache-2.0 |
> | **Fuente upstream** | https://github.com/IBM/mcp-context-forge |
>
> *Esta ficha caduca. Si la fecha de revisión es anterior a 6 meses respecto a hoy, trátala como `stale` aunque el campo Estado diga lo contrario. Lo normativo está en el cuerpo ([`../../criterios-funcionales.md`](../../criterios-funcionales.md)), no aquí.*

---

## 1. Qué es y qué rol cubre

IBM ContextForge es un gateway para MCP: se sitúa delante de uno o varios servidores MCP y media toda invocación que los atraviesa, aplicando autenticación, control de acceso, registro y observabilidad. Su sistema de plugins permite interceptar el contenido de las invocaciones; uno de esos plugins ofrece des-identificación de datos personales apoyándose en Microsoft Presidio. Por eso cubre, a la vez, el rol de **gateway** (CF-01) y el de **des-identificación / DLP en la ruta** (CF-06).

---

## 2. Matriz de cobertura CF-01..CF-06

| Criterio | Cobertura | Justificación (qué punto de la checklist cumple / qué le falta) |
| --- | :---: | --- |
| **CF-01** — gateway de llamadas inter-agente | ● | Intermedia toda llamada que lo atraviesa, puede denegarla, registrarla y medirla, expone puntos de extensión (plugins) donde insertar policy antes de ejecutar, y propaga metadatos. Es su propósito declarado. |
| **CF-02** — service registry federado | ◐ | Expone un catálogo de servidores y herramientas MCP registrados, pero el filtrado del catálogo por identidad del solicitante y el descriptor extendido del cuerpo dependen de configuración y versión. |
| **CF-03** — policy engine | ◐ | Aplica control de acceso en el punto de mediación, pero no es un motor de políticas declarativo de propósito general; para CF-03 conviene un policy engine externo (ver [`policy-opa.md`](./policy-opa.md), [`policy-cedar.md`](./policy-cedar.md)). |
| **CF-04** — identity provider (autenticación mutua con identidad criptográfica verificable) | ● | Soporta autenticación de clientes y de servidores upstream; permite exigir que el receptor verifique la identidad del emisor antes de ejecutar. La emisión de credenciales de vida corta depende del despliegue. |
| **CF-05** — observabilidad agent-aware | ◐ | Emite trazas y métricas de las invocaciones que media; la trazabilidad de la cadena por `correlationId` y la exportación del bloque de contexto cultural como atributos dependen de la integración con el backend de telemetría. |
| **CF-06** — des-identificación / DLP en la ruta | ● | El plugin de des-identificación sustituye datos personales por tokens antes de que la invocación cruce la frontera, apoyándose en Presidio para la detección. La reversibilidad/auditoría dependen de la custodia de la tabla de reversión. |

> Recuerda: ninguna pieza única cubre los seis criterios. Para CF-04, el cuerpo nunca exige «mTLS» por su nombre: exige las propiedades de identidad criptográfica verificable; evalúa contra ellas.

---

## 3. Cómo se integra con MCP

Es un gateway MCP nativo: habla MCP por ambos lados (cliente → gateway → servidores MCP) sin requerir extensiones del protocolo, en línea con el manifiesto §8. El bloque de contexto cultural y los `deidToken` viajan como metadatos propagados por el gateway; el plugin de des-identificación es el punto natural donde se emiten los `deidToken`.

> Si hay detalle de serialización sobre transporte (cómo viaja el bloque de contexto cultural o los `deidToken`), documéntalo en [`../mapeo-transporte/`](../mapeo-transporte/) y enlázalo aquí; no lo incrustes en esta ficha. Si aporta implementaciones de policy, van a [`../policy-templates/`](../policy-templates/).

---

## 4. Pros

- Un solo componente cubre dos criterios que normalmente exigen piezas separadas: mediación (CF-01) y des-identificación (CF-06).
- Construido específicamente sobre MCP, el protocolo base del corpus; no introduce extensiones de protocolo.
- Sistema de plugins extensible: la des-identificación es un plugin entre varios y puede ampliarse con lógica propia.
- Respaldo de un fabricante grande (IBM) y licencia permisiva (Apache-2.0).
- La detección de datos personales se delega en Presidio, un motor especializado y auditable por separado, lo que satisface la exigencia de motor *vendor-neutral* de [CF-06](../../criterios-funcionales.md).

---

## 5. Contras

- No es un motor de políticas: para CF-03 sigue haciendo falta un policy engine externo.
- La des-identificación es tan reversible y auditable como lo sea la custodia de la tabla de reversión, que el gateway no resuelve por sí solo; hay que diseñarla.
- La calidad de la detección hereda los límites de Presidio: nunca es perfecta y requiere ajuste por idioma y dominio.
- Concentrar mediación y des-identificación en un mismo punto convierte al gateway en componente crítico; su disponibilidad y su superficie de ataque deben gobernarse.

---

## 6. Madurez

| Señal | Lectura |
| --- | --- |
| Estabilidad de API / versionado | Temprana a estable; sigue la evolución de MCP, que aún se mueve. |
| Cadencia de releases | Frecuente, alineada con la evolución de MCP. |
| Tamaño / actividad de comunidad | Activa, con respaldo de IBM. |
| Casos de producción conocidos | En crecimiento; ecosistema MCP todavía joven. |
| Calidad de documentación | Razonable y en mejora continua. |

**Veredicto de madurez:** emergente — sólido por el respaldo del fabricante, pero atado al ritmo de un protocolo (MCP) en maduración.

---

## 7. Riesgo de continuidad (M&A / cambio de licencia / abandono)

| Vector de riesgo | Nivel | Notas |
| --- | :---: | --- |
| Adquisición / M&A | bajo | El fabricante ya es un actor grande; el riesgo es de cambio de prioridades, no de adquisición. |
| Cambio de licencia (open → source-available / comercial) | medio | Apache-2.0 hoy; un fabricante grande puede reorientar la estrategia de licenciamiento de un proyecto. |
| Abandono / *bus factor* | bajo | Proyecto con equipo detrás, no de un único mantenedor. |
| Dependencia de un único *vendor* | medio | Está impulsado por un fabricante; la comunidad externa es menor que la del propio MCP. |
| Gobernanza (proyecto individual vs. fundación) | medio | Proyecto de fabricante, no de fundación neutral. |

**Plan de salida si el riesgo se materializa:** el cuerpo solo exige los criterios funcionales. CF-01 puede cubrirse con otro gateway (ver [`agentgateway.md`](./agentgateway.md)); CF-06 puede cubrirse desplegando un motor de des-identificación *vendor-neutral* (Presidio u otro) detrás de cualquier gateway con plugins. Sustituirlo no toca la especificación.

---

## 8. Veredicto

A la fecha de revisión, es una de las opciones más completas para una federación MCP que necesite cubrir mediación (CF-01) y des-identificación (CF-06) con un solo componente, además de contribuir a identidad (CF-04). Deja fuera el motor de políticas (CF-03), que hay que añadir aparte, y exige diseñar la custodia de la tabla de reversión para que la des-identificación sea verdaderamente reversible y auditable. En el [caso del corredor comercial→legal](../../../../examples/federation/corredor-comercial-legal/), interceptaría la invocación del agente de Comercial al de Legal, des-identificaría los datos personales del lead antes de que la propuesta cruce a Legal, y registraría toda la operación.

---

### Enlaces relacionados

- [Apéndice vivo — matriz global y contrato de desacoplamiento](../README.md)
- [Criterios funcionales (CF-01..CF-06)](../../criterios-funcionales.md) — definición normativa de las columnas.
- [Regla anti-acoplamiento](../../regla-anti-acoplamiento.md) — por qué esta ficha vive en el apéndice y no en el cuerpo.
- [Mapeo de transporte](../mapeo-transporte/) y [policy templates](../policy-templates/) — donde van la serialización y las implementaciones por dialecto.

*Ficha de stack — versión 1.0. Parte del corpus en su estructura; el contenido que se rellene es informativo y caduca.*
