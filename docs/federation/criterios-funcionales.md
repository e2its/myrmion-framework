# Myrmion Federation — Criterios funcionales del stack

**Versión 1.0**

*Los seis criterios funcionales que el stack opensource elegido debe cumplir, expresados como propiedades verificables sin nombrar producto. Materializan el §4 del [manifiesto](./manifesto.md) — «criterios, no marcas» — y son la espina dorsal del corpus: el resto de documentos se apoya en ellos por identificador (CF-01..CF-06).*

---

## Cómo usar este documento

El manifiesto declara (§4) que Federation se mantiene agnóstico al stack concreto y que lo que sí declara son los criterios funcionales que el stack debe cubrir. Este documento convierte esos seis criterios en **propiedades verificables**: para cada uno, qué problema resuelve, qué capa de la arquitectura sirve, una checklist de verificación, qué NO prescribe, y dónde encontrar implementaciones candidatas.

Se usa en tres momentos:

1. **Selección de stack** (manifiesto §6, Fase 1): el equipo de plataforma evalúa cada stack candidato contra las checklists de aquí. La matriz de cobertura está en [`appendix/README.md`](./appendix/README.md).
2. **Redacción del cuerpo:** cualquier requisito técnico del corpus se expresa primero como un CF. Si un documento necesita una capacidad nueva del stack, se añade aquí como criterio antes de usarse en otro sitio.
3. **Auditoría de agnosticismo** ([regla anti-acoplamiento](./regla-anti-acoplamiento.md)): los CF son, por construcción, la frontera entre lo que el cuerpo puede afirmar y lo que pertenece al `appendix/`.

> **Solo seis.** El modelo de implementación de referencia incluye muchas más capacidades (egress controlado, rate limiting, supply chain, multi-tenancy, resiliencia/DR, FinOps). Esas son propiedades de *una* arquitectura concreta, no requisitos de federación. No son criterios funcionales: cuando importan para una organización, se tratan como variables del [Perfil de Adopción](./perfil-adopcion-federacion.md) o como notas no normativas del apéndice. Mantener la lista en seis es deliberado y es lo que mantiene el framework portable.

---

## Tabla resumen

| ID | Criterio | Capa que sirve (§3) | Resuelve |
|---|---|---|---|
| **CF-01** | Gateway de llamadas inter-agente | §3.1, §3.2 | Intermediar y observar toda llamada; punto de extensión para policy y propagación de metadatos |
| **CF-02** | Service registry federado | §3.1 | Descubrimiento de agentes con descriptores de capacidades extendidos |
| **CF-03** | Policy engine | §3.3 | Evaluar en runtime las policies derivadas de la Constitución |
| **CF-04** | Identity provider | §3.1 | Identidades de servicio criptográficas con credenciales de vida corta |
| **CF-05** | Observabilidad agent-aware | §3.2, §3.4 | Trazar cadenas de llamadas completas por `correlationId` |
| **CF-06** | Des-identificación / DLP en la ruta | §3.3 | Detectar y redactar/tokenizar PII/PHI antes de que alcance el modelo |

Cada criterio se considera **cubierto** cuando el stack satisface todos los puntos de su checklist. Un punto sin cubrir no invalida el stack, pero obliga a registrar el hueco como decisión (ADR de adopción, rango `0100+`) y a documentar el control compensatorio.

---

## CF-01 — Gateway de llamadas inter-agente

**Qué resuelve.** Que exista un punto único por el que pasan todas las llamadas inter-agente, de modo que la gobernanza (autenticación, policy, propagación de contexto, observabilidad) se aplique en la ruta y no dependa de la buena voluntad de cada agente. Sin este punto, la capa de identidad (§3.1) y la de propagación de contexto (§3.2) no tienen dónde engancharse.

**Checklist de verificación.**

- [ ] Intermedia todas las llamadas inter-agente (ningún agente llama a otro por un canal que esquive el gateway).
- [ ] Soporta autenticación mutua que satisfaga las propiedades de identidad criptográfica (ver CF-04); no se exige un mecanismo concreto.
- [ ] Expone puntos de extensión donde insertar evaluación de policy **antes** de ejecutar la llamada (CF-03).
- [ ] Propaga metadatos arbitrarios a lo largo de la llamada sin truncarlos ni reinterpretarlos — es el transporte del bloque de contexto cultural (§3.2). El esquema del bloque está en [esquema-bloque-contexto-cultural.md](./esquema-bloque-contexto-cultural.md); el mapeo concreto al transporte de cada protocolo, en `appendix/mapeo-transporte/`.
- [ ] No requiere extensiones del protocolo base (MCP): usa los mecanismos que el protocolo ya provee (metadata, headers, descriptors).

**Qué NO prescribe.** El producto de gateway, su lenguaje de extensión, su modelo de despliegue, ni el protocolo de transporte concreto. Candidatos y su cobertura: ver [`appendix/stacks-referencia/`](./appendix/stacks-referencia/).

---

## CF-02 — Service registry federado

**Qué resuelve.** Que un agente pueda descubrir a otro y entender qué hace, sin coordinación humana previa. El registry es lo que convierte un conjunto de agentes autenticados en una federación operable.

**Checklist de verificación.**

- [ ] Almacena y consulta agentes por su [descriptor de identidad](./esquema-identidad-agente.md) **extendido**: no solo nombre y endpoint, sino dominio, criticidad, clases de dato y versión de Constitución aplicada.
- [ ] El alta de un agente puede condicionarse al resultado del *gate de coherencia* (ver [gobernanza-federada.md](./gobernanza-federada.md)): si el descriptor entra en conflicto con la Constitución, la registración falla.
- [ ] Soporta el ciclo de vida completo: alta, actualización de descriptor, marcado como deprecated y baja (deregister) sin liberar el `agentId`.
- [ ] Permite notificar a los agentes dependientes (`dependsOn`) cuando un agente del que dependen se retira.

**Qué NO prescribe.** El producto de registry ni su modelo de consistencia. Candidatos: ver `appendix/stacks-referencia/`.

---

## CF-03 — Policy engine

**Qué resuelve.** Que los principios automatizables de la Constitución se evalúen en cada llamada, en runtime, con latencia despreciable. Es el músculo de la capa de mapping (§3.3).

**Checklist de verificación.**

- [ ] Lenguaje de policy declarativo (la policy se declara, no se programa imperativamente).
- [ ] Latencia de evaluación sub-milisegundo en el caso normal (la sobrecarga agregada de la capa de gobernanza la domina la verificación de identidad, no la evaluación de policy — manifiesto §9).
- [ ] Versionado de policies con auditoría de cambios (qué policy, qué versión, quién la cambió y cuándo).
- [ ] Las policies pueden expresar las decisiones que el [formato de catálogo](./convenciones-mapping-constitucion-policy.md) requiere: `allow`, `deny`, `redact`, `require-prior-hop`.
- [ ] Las policies pueden consultar campos del descriptor de identidad y del bloque de contexto cultural (p. ej. `capability.externalizes`, `decisionChain`).

**Qué NO prescribe.** El motor concreto ni su dialecto (Rego, Cedar, Casbin, etc.). Las convenciones de mapping del cuerpo son neutrales al dialecto; las implementaciones por dialecto viven en [`appendix/policy-templates/`](./appendix/policy-templates/).

---

## CF-04 — Identity provider

**Qué resuelve.** Que cada agente tenga una identidad que otro agente pueda verificar criptográficamente antes de ejecutar una llamada. Es el cimiento de la confianza de la federación.

**Checklist de verificación.**

- [ ] Emite identidades de servicio **criptográficas** (no secretos compartidos estáticos).
- [ ] Las credenciales tienen TTL corto y son revocables.
- [ ] La identidad es vinculable de forma estable al `agentId` del descriptor.
- [ ] El receptor puede verificar la identidad del emisor **antes** de ejecutar la llamada.

Estas comprobaciones materializan las **tres propiedades** de identidad criptográfica verificable que el resto del corpus exige —verificación criptográfica antes de ejecutar, credencial de vida corta y revocable, y vinculación estable al `agentId`—: es lo que el cuerpo entiende por «mTLS o equivalente». El cuerpo nunca exige mTLS por su nombre (ver [regla anti-acoplamiento](./regla-anti-acoplamiento.md), regla 4).

**Qué NO prescribe.** El IdP concreto ni el mecanismo (mTLS, identidad federada tipo SPIFFE, etc.). Candidatos: ver `appendix/stacks-referencia/`.

---

## CF-05 — Observabilidad agent-aware

**Qué resuelve.** Que la cadena de decisiones se reconstruya trivialmente y que el drift federado (§3.4) se pueda medir. Sin esto, la trazabilidad y la detección de drift son aspiraciones, no procesos.

**Checklist de verificación.**

- [ ] Traza cadenas de llamadas completas correlacionadas por `correlationId` estándar.
- [ ] Exporta los metadatos del bloque de contexto cultural como atributos del span (o equivalente), sin necesidad de instrumentación ad hoc por agente.
- [ ] Exporta a backends estándar; idealmente sobre un estándar abierto de telemetría (p. ej. OpenTelemetry) para no acoplar la observabilidad a un backend concreto.
- [ ] Permite las tres consultas que los [patrones de drift](./patrones-deteccion-drift.md) necesitan: por cadena (Patrón A), por excepción acumulada (Patrón B), por coherencia entre agentes (Patrón C).

**Qué NO prescribe.** El backend de observabilidad ni el dashboard. Federation articula qué medir; el dashboard lo aporta el stack.

---

## CF-06 — Des-identificación / DLP en la ruta

**Qué resuelve.** Redactar, tokenizar o bloquear PII y PHI en los argumentos de las llamadas inter-agente **antes** de que alcancen el modelo. Es el criterio que cierra el hueco de enforcement técnico que Adoption no podía cubrir: en Adoption pura no hay punto de inserción para la redacción inline (ver [Guía de protección de datos](../adoption/guia-proteccion-datos.md) §3.4); en Federation, la ruta inter-agente **es** ese punto.

**Checklist de verificación.**

- [ ] Detecta categorías de dato sensible (PII, PHI y las clases que el Marco Regulatorio defina) en los argumentos de la tool.
- [ ] Redacta, tokeniza o bloquea según la categoría, en la ruta, antes de la invocación al modelo.
- [ ] Cuando la redacción es reversible, emite `deidToken` que el bloque de contexto cultural transporta para re-identificar la respuesta **solo en el agente de origen** (ver [esquema-bloque-contexto-cultural.md](./esquema-bloque-contexto-cultural.md)).
- [ ] El motor de detección es vendor-neutral, para no acoplar la política de datos a un gateway concreto.

**Qué NO prescribe.** El motor de DLP concreto (p. ej. Presidio, citado como ejemplo en el manifiesto §4) ni el gateway que lo hospeda. Varios componentes de gateway integran un plugin de des-identificación que cubre a la vez CF-01 y CF-06; ver `appendix/stacks-referencia/`.

---

## Relación con las capas de la arquitectura

Los seis criterios no son las cuatro capas funcionales del §3 — son lo que el stack debe aportar para que las capas se puedan montar encima. La correspondencia:

| Capa funcional (§3) | Criterios que la habilitan |
|---|---|
| §3.1 Identidad y autorización | CF-01, CF-02, CF-04 |
| §3.2 Propagación de contexto cultural | CF-01, CF-05 |
| §3.3 Mapping Constitución → policy | CF-03, CF-06 |
| §3.4 Detección de drift | CF-05 |

El detalle de cómo cada capa se monta sobre estos criterios está en [guia-arquitectura-funcional.md](./guia-arquitectura-funcional.md).

---

*Criterios funcionales de Myrmion Federation — versión 1.0. Parte del corpus normativo. Las implementaciones candidatas viven en [`appendix/`](./appendix/README.md), nunca en este documento.*
