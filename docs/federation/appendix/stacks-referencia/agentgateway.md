# Myrmion Federation — Ficha de stack: «Agentgateway»

**Versión 1.0**

*Materializa el contrato de desacoplamiento del [apéndice vivo](../README.md): una ficha fechada que evalúa un componente concreto contra los [criterios funcionales CF-01..CF-06](../../criterios-funcionales.md), sin contaminar el cuerpo normativo.*

---

> ## Banner de vigencia
>
> | Campo | Valor |
> | --- | --- |
> | **Componente** | Agentgateway |
> | **Versión evaluada** | rolling (proyecto joven, en evolución activa) |
> | **Fecha de revisión** | 2026-05 |
> | **Revisor(es)** | comunidad |
> | **Próxima revisión recomendada** | 2026-11 |
> | **Estado** | vigente |
> | **Licencia (a la fecha)** | Apache-2.0 |
> | **Fuente upstream** | https://github.com/agentgateway/agentgateway |
>
> *Esta ficha caduca. Si la fecha de revisión es anterior a 6 meses respecto a hoy, trátala como `stale` aunque el campo Estado diga lo contrario. Lo normativo está en el cuerpo ([`../../criterios-funcionales.md`](../../criterios-funcionales.md)), no aquí.*

---

## 1. Qué es y qué rol cubre

Agentgateway es un proxy de datos diseñado específicamente para tráfico de agentes y herramientas: se sitúa entre los consumidores (agentes) y los proveedores (servidores MCP, APIs, otros agentes) y media cada invocación, aplicando control de acceso, registro y observabilidad. Su rol en la federación es el de **gateway** (CF-01).

---

## 2. Matriz de cobertura CF-01..CF-06

| Criterio | Cobertura | Justificación (qué punto de la checklist cumple / qué le falta) |
| --- | :---: | --- |
| **CF-01** — gateway de llamadas inter-agente | ● | Es un proxy que intermedia toda invocación entre agentes y proveedores: puede denegar, registrar y medir cada una, los agentes resuelven a través del gateway, y expone puntos de extensión para policy. Es su propósito declarado. |
| **CF-02** — service registry federado | ◐ | Expone y enruta hacia herramientas y servidores registrados; el filtrado del catálogo por identidad del solicitante y el descriptor extendido dependen de la política y del despliegue. |
| **CF-03** — policy engine | ◐ | Aplica control de acceso e integra autorización en el punto de mediación, pero no es un motor de políticas declarativo de propósito general; para CF-03 robusto, combínalo con un policy engine externo (ver [`policy-opa.md`](./policy-opa.md), [`policy-cedar.md`](./policy-cedar.md)). |
| **CF-04** — identity provider (autenticación mutua con identidad criptográfica verificable) | ● | Como proxy puede terminar y exigir autenticación mutua con identidad criptográfica; el receptor verifica la identidad del emisor antes de ejecutar. La emisión de credenciales de vida corta depende del despliegue. |
| **CF-05** — observabilidad agent-aware | ◐ | Pensado para insertarse en el camino de datos con observabilidad; la trazabilidad de la cadena por `correlationId` y la exportación del bloque de contexto cultural como atributos dependen de la integración con el backend. |
| **CF-06** — des-identificación / DLP en la ruta | ○ | No incluye des-identificación de datos personales por sí mismo. |

> Recuerda: ninguna pieza única cubre los seis criterios. Para CF-04, el cuerpo nunca exige «mTLS» por su nombre: exige las propiedades de identidad criptográfica verificable; evalúa contra ellas.

---

## 3. Cómo se integra con MCP

Es un gateway MCP-nativo (también orientado a A2A y a APIs): habla MCP en el camino de datos sin requerir extensiones del protocolo, en línea con el manifiesto §8. El bloque de contexto cultural viaja como metadatos propagados por el gateway. Encaja de forma natural en arquitecturas de service mesh, lo que facilita observabilidad y control de tráfico a escala.

> Si hay detalle de serialización sobre transporte (cómo viaja el bloque de contexto cultural o los `deidToken`), documéntalo en [`../mapeo-transporte/`](../mapeo-transporte/) y enlázalo aquí; no lo incrustes en esta ficha. Si aporta implementaciones de policy, van a [`../policy-templates/`](../policy-templates/).

---

## 4. Pros

- Diseñado desde cero para tráfico de agentes y MCP, no un gateway HTTP genérico readaptado.
- Ligero y de alto rendimiento (núcleo en Rust), pensado para insertarse en el camino de datos sin penalizar latencia.
- Encaja de forma natural en arquitecturas de service mesh, facilitando observabilidad y control de tráfico a escala.
- Licencia permisiva (Apache-2.0) y enfoque MCP-nativo: no introduce extensiones de protocolo.

---

## 5. Contras

- Cubre con solvencia CF-01 pero deja fuera CF-03 (motor de políticas) y CF-06 (des-identificación): es una pieza, no una federación completa.
- Proyecto relativamente joven; la superficie de funcionalidades y la API aún evolucionan.
- Sacar el máximo partido suele implicar adoptar el ecosistema de service mesh asociado, lo que añade complejidad operativa.
- CF-02 y CF-05 quedan en parcial: el descriptor extendido y la trazabilidad de la cadena exigen integración adicional.

---

## 6. Madurez

| Señal | Lectura |
| --- | --- |
| Estabilidad de API / versionado | Temprana; en evolución activa junto con MCP. |
| Cadencia de releases | Frecuente. |
| Tamaño / actividad de comunidad | Comunidad opensource con respaldo comercial; tracción creciente. |
| Casos de producción conocidos | Pocos y recientes; proyecto joven. |
| Calidad de documentación | En construcción. |

**Veredicto de madurez:** emergente — proyecto joven con respaldo y tracción crecientes.

---

## 7. Riesgo de continuidad (M&A / cambio de licencia / abandono)

| Vector de riesgo | Nivel | Notas |
| --- | :---: | --- |
| Adquisición / M&A | medio | Respaldo comercial detrás; una adquisición podría reorientar el proyecto. |
| Cambio de licencia (open → source-available / comercial) | medio | Apache-2.0 hoy; los proyectos con respaldo comercial pueden cambiar de licencia. |
| Abandono / *bus factor* | medio | Comunidad creciente pero todavía concentrada. |
| Dependencia de un único *vendor* | medio | Vinculado a un ecosistema comercial concreto. |
| Gobernanza (proyecto individual vs. fundación) | medio | Proyecto con respaldo comercial, no de fundación neutral. |

**Plan de salida si el riesgo se materializa:** el cuerpo solo exige el criterio funcional. CF-01 puede cubrirse con otro gateway MCP (ver [`ibm-contextforge.md`](./ibm-contextforge.md)). Sustituirlo no toca la especificación.

---

## 8. Veredicto

A la fecha de revisión, es una opción atractiva como punto de mediación (CF-01) cuando se busca un gateway MCP-nativo y de alto rendimiento, especialmente en arquitecturas de service mesh. Hay que complementarlo con un policy engine externo para CF-03 y con un componente de des-identificación para CF-06. En el [caso del corredor comercial→legal](../../../../examples/federation/corredor-comercial-legal/), sería el punto por el que la invocación del agente de Comercial alcanza al de Legal, aplicando control de acceso, registro y observabilidad, mientras la des-identificación y la autorización por política se delegan en componentes especializados.

---

### Enlaces relacionados

- [Apéndice vivo — matriz global y contrato de desacoplamiento](../README.md)
- [Criterios funcionales (CF-01..CF-06)](../../criterios-funcionales.md) — definición normativa de las columnas.
- [Regla anti-acoplamiento](../../regla-anti-acoplamiento.md) — por qué esta ficha vive en el apéndice y no en el cuerpo.
- [Mapeo de transporte](../mapeo-transporte/) y [policy templates](../policy-templates/) — donde van la serialización y las implementaciones por dialecto.

*Ficha de stack — versión 1.0. Parte del corpus en su estructura; el contenido que se rellene es informativo y caduca.*
