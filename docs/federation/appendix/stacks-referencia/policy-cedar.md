# Myrmion Federation — Ficha de stack: «Cedar»

**Versión 1.0**

*Materializa el contrato de desacoplamiento del [apéndice vivo](../README.md): una ficha fechada que evalúa un componente concreto contra los [criterios funcionales CF-01..CF-06](../../criterios-funcionales.md), sin contaminar el cuerpo normativo.*

---

> ## Banner de vigencia
>
> | Campo | Valor |
> | --- | --- |
> | **Componente** | Cedar (lenguaje y motor de autorización) |
> | **Versión evaluada** | rolling (releases regulares) |
> | **Fecha de revisión** | 2026-05 |
> | **Revisor(es)** | comunidad |
> | **Próxima revisión recomendada** | 2026-11 |
> | **Estado** | vigente |
> | **Licencia (a la fecha)** | Apache-2.0 |
> | **Fuente upstream** | https://www.cedarpolicy.com/ |
>
> *Esta ficha caduca. Si la fecha de revisión es anterior a 6 meses respecto a hoy, trátala como `stale` aunque el campo Estado diga lo contrario. Lo normativo está en el cuerpo ([`../../criterios-funcionales.md`](../../criterios-funcionales.md)), no aquí.*

---

## 1. Qué es y qué rol cubre

Cedar es un lenguaje y un motor de autorización: dadas las entidades (principal, acción, recurso, contexto) y un conjunto de políticas, decide si una acción se permite o se deniega. Las políticas se escriben en un lenguaje declarativo propio, legible y **analizable** formalmente, y la evaluación es rápida y verificable. Su rol en la federación es el de **policy engine** (CF-03).

---

## 2. Matriz de cobertura CF-01..CF-06

| Criterio | Cobertura | Justificación (qué punto de la checklist cumple / qué le falta) |
| --- | :---: | --- |
| **CF-01** — gateway de llamadas inter-agente | ○ | No intercepta tráfico; es una librería/servicio de decisión. Necesita un gateway que lo invoque. |
| **CF-02** — service registry federado | ○ | No provee catálogo de agentes; a lo sumo puede ser el motor que filtra uno externo por identidad. |
| **CF-03** — policy engine | ● | Motor de autorización separado de los agentes; evalúa la decisión en runtime, lenguaje declarativo y versionable, evaluación rápida. Cumple la checklist de CF-03, con la ventaja diferencial de la analizabilidad formal. |
| **CF-04** — identity provider (autenticación mutua con identidad criptográfica verificable) | ○ | Consume entidades e identidades como entrada; no las emite ni las verifica criptográficamente. |
| **CF-05** — observabilidad agent-aware | ○ | Ajeno; produce decisiones, no trazas de cadena de llamadas. |
| **CF-06** — des-identificación / DLP en la ruta | ○ | No des-identifica datos. |

> Recuerda: ninguna pieza única cubre los seis criterios. Cedar es deliberadamente solo CF-03.

---

## 3. Cómo se integra con MCP

Cedar no habla MCP: es un motor de decisión que el gateway MCP invoca (embebido como librería o como servicio) antes de dejar pasar una invocación. No requiere extensiones de protocolo, en línea con el manifiesto §8. El esquema de entidades (principals, recursos, atributos) lo diseña el integrador a partir del [descriptor de identidad](../../esquema-identidad-agente.md) y del [bloque de contexto cultural](../../esquema-bloque-contexto-cultural.md).

> Las implementaciones de los patrones de [mapping Constitución → policy](../../convenciones-mapping-constitucion-policy.md) en dialecto Cedar van a [`../policy-templates/`](../policy-templates/), no en esta ficha.

---

## 4. Pros

- Cubre CF-03 de forma completa: motor externo, decisión en tiempo de invocación, políticas declarativas y versionables.
- Lenguaje diseñado para ser legible y, sobre todo, **analizable**: hay herramientas de validación y razonamiento formal sobre las políticas, lo que facilita demostrar propiedades de seguridad.
- Modelo orientado a entidades (principal, acción, recurso, contexto) que encaja de forma natural con autorizar «qué agente puede invocar qué capacidad».
- Evaluación rápida y embebible como librería, además de desplegable como servicio.
- Licencia permisiva (Apache-2.0) y respaldo de un proveedor grande.

---

## 5. Contras

- Solo cubre CF-03: necesita un gateway (CF-01) que lo consulte y el resto de piezas de la federación.
- Ecosistema e integraciones más jóvenes y menos extensos que los del policy engine más establecido del mercado (ver [`policy-opa.md`](./policy-opa.md)).
- El modelo de entidades exige diseñar bien el esquema; el resultado es tan bueno como ese diseño.
- Nació muy ligado a un ecosistema de proveedor; conviene verificar el grado de neutralidad y de integraciones de terceros.

---

## 6. Madurez

| Señal | Lectura |
| --- | --- |
| Estabilidad de API / versionado | Estable, en consolidación. |
| Cadencia de releases | Regular. |
| Tamaño / actividad de comunidad | Creciente; ecosistema más joven que el de OPA. |
| Casos de producción conocidos | En crecimiento, fuertes dentro del ecosistema del proveedor que lo impulsa. |
| Calidad de documentación | Buena, con énfasis en la analizabilidad. |

**Veredicto de madurez:** consolidado en el núcleo, emergente en ecosistema de terceros.

---

## 7. Riesgo de continuidad (M&A / cambio de licencia / abandono)

| Vector de riesgo | Nivel | Notas |
| --- | :---: | --- |
| Adquisición / M&A | bajo | Impulsado por un proveedor grande; bajo riesgo de adquisición. |
| Cambio de licencia (open → source-available / comercial) | bajo | Apache-2.0; el núcleo está liberado. |
| Abandono / *bus factor* | bajo | Equipo de proveedor detrás. |
| Dependencia de un único *vendor* | medio | El ecosistema y las integraciones gravitan en torno a un proveedor. |
| Gobernanza (proyecto individual vs. fundación) | medio | Proyecto de proveedor, con apertura creciente a contribución externa. |

**Plan de salida si el riesgo se materializa:** el cuerpo solo exige el criterio funcional. CF-03 puede cubrirse con otro policy engine declarativo (ver [`policy-opa.md`](./policy-opa.md)). Sustituirlo no toca la especificación, aunque obliga a reescribir las políticas al nuevo dialecto.

---

## 8. Veredicto

A la fecha de revisión, es una alternativa fuerte para CF-03 cuando la gobernanza debe **demostrarse** y no solo aplicarse: su analizabilidad formal permite razonar sobre las políticas. El gateway de la federación (ver [`ibm-contextforge.md`](./ibm-contextforge.md) o [`agentgateway.md`](./agentgateway.md)) consulta a Cedar antes de dejar pasar cada invocación. En el [caso del corredor comercial→legal](../../../../examples/federation/corredor-comercial-legal/), una política Cedar modelaría al agente de Comercial como *principal*, la acción «solicitar revisión» y al agente de Legal como *recurso*, permitiendo la invocación solo bajo las condiciones que la organización defina: el gateway hace la consulta, Cedar toma la decisión.

---

### Enlaces relacionados

- [Apéndice vivo — matriz global y contrato de desacoplamiento](../README.md)
- [Criterios funcionales (CF-01..CF-06)](../../criterios-funcionales.md) — definición normativa de las columnas.
- [Regla anti-acoplamiento](../../regla-anti-acoplamiento.md) — por qué esta ficha vive en el apéndice y no en el cuerpo.
- [Convenciones de mapping Constitución → policy](../../convenciones-mapping-constitucion-policy.md) y [policy templates](../policy-templates/) — donde van las implementaciones por dialecto.

*Ficha de stack — versión 1.0. Parte del corpus en su estructura; el contenido que se rellene es informativo y caduca.*
