# Myrmion Federation — Índice y guía de navegación

**Versión 1.0**

*Puerta de entrada al corpus de Federation. Léelo primero. El [manifiesto](./manifesto.md) explica el porqué y el qué; este índice te lleva al documento concreto según lo que necesites hacer.*

---

## 1. Cómo está organizado el corpus

Federation se compone de tres tipos de contenido, que se leen en momentos distintos:

- **Manifiesto** — el porqué, los principios, la arquitectura funcional y las fases. Es el documento fundacional y no cambia con el stack.
- **Cuerpo normativo** (`docs/federation/`) — esquemas, criterios, convenciones, gobernanza y método. Envejece lento; no nombra marcas. Custodia: el equipo del framework.
- **Apéndice vivo** (`docs/federation/appendix/`) — stacks de referencia, implementaciones de policy por dialecto, recetas de drift y mapeo de transporte. Envejece rápido; es el único lugar con nombres de producto. Custodia: la comunidad.

A esto se suman las **plantillas socráticas** (`templates/federation/`) que cada organización rellena, y los **ejemplos** (`examples/federation/`) que muestran un corredor completo.

La frontera entre cuerpo y apéndice la fija la [regla anti-acoplamiento](./regla-anti-acoplamiento.md). Si dudas dónde va algo, ese documento decide.

---

## 2. Mapa del corpus

### Documentos normativos (`docs/federation/`)

| Documento | Qué resuelve | Estado |
|---|---|---|
| [manifesto.md](./manifesto.md) | Porqué, principios, arquitectura, fases, métricas | ✅ v1.0 |
| [indice-y-guia-de-navegacion.md](./indice-y-guia-de-navegacion.md) | Este documento: puerta de entrada y rutas por rol | ✅ v1.0 |
| [glosario-federacion.md](./glosario-federacion.md) | Vocabulario normativo del corpus | ✅ v1.0 |
| [criterios-funcionales.md](./criterios-funcionales.md) | Los 6 criterios del stack (CF-01..CF-06). Espina dorsal | ✅ v1.0 |
| [regla-anti-acoplamiento.md](./regla-anti-acoplamiento.md) | Qué va al cuerpo vs al apéndice. Norma transversal | ✅ v1.0 |
| [guia-arquitectura-funcional.md](./guia-arquitectura-funcional.md) | Las 4 capas funcionales (§3) + diagramas | 📝 draft |
| [esquema-identidad-agente.md](./esquema-identidad-agente.md) | Contrato del descriptor de agente (§3.1) + contrato de hash | 📝 draft |
| [esquema-bloque-contexto-cultural.md](./esquema-bloque-contexto-cultural.md) | Contrato del bloque que viaja en cada llamada (§3.2) | 📝 draft |
| [convenciones-mapping-constitucion-policy.md](./convenciones-mapping-constitucion-policy.md) | Cómo traducir la Constitución a policy (§3.3) | 📝 draft |
| [patrones-deteccion-drift.md](./patrones-deteccion-drift.md) | Los 3 patrones de detección de drift (§3.4) | 📝 draft |
| [gobernanza-federada.md](./gobernanza-federada.md) | 4º custodio, gate de coherencia, ciclo de vida (§5) | 📝 draft |
| [guia-adopcion-por-fases.md](./guia-adopcion-por-fases.md) | Fases 0–5 con entradas, salidas y criterio de parada (§6) | 📝 draft |
| [metricas-federacion.md](./metricas-federacion.md) | Las métricas que importan (§7) | 📝 draft |
| [perfil-adopcion-federacion.md](./perfil-adopcion-federacion.md) | Variables VF que modifican decisiones según contexto | 📝 draft |
| [adr/](./adr/) | Architecture Decision Records: plantilla + ejemplos | 📝 draft |

### Apéndice vivo (`docs/federation/appendix/`) — comunidad

| Recurso | Qué contiene | Estado |
|---|---|---|
| [appendix/README.md](./appendix/README.md) | Contrato de desacoplamiento + matriz componente × CF | 📝 draft |
| appendix/stacks-referencia/ | Fichas de stacks candidatos con su cobertura de CF | 📝 draft |
| appendix/policy-templates/ | Catálogo de policy templates con snippets por dialecto | 📝 draft |
| appendix/drift-recipes/ | Patrones de drift específicos de sectores regulados | 📝 draft |
| appendix/mapeo-transporte/ | Cómo viaja el bloque de contexto por protocolo (MCP, A2A) | 📝 draft |

### Plantillas (`templates/federation/`) y ejemplos (`examples/federation/`)

| Recurso | Qué es | Estado |
|---|---|---|
| [templates/federation/](../../templates/federation/) | Plantillas socráticas que la organización rellena (descriptor, bloque, ficha de policy, playbook de drift, charter, registro de excepciones, runbooks, checklist Fase 0) | 📝 draft |
| [examples/federation/](../../examples/federation/) | Corredor end-to-end anonimizado + diagramas | 📝 draft |

---

## 3. Rutas de lectura por rol

**Dirección / CIO (¿debo plantearme Federation?).** [Manifiesto](./manifesto.md) §1–§2 y §6 (Fase 0) → checklist de prerrequisitos (`templates/federation/checklist-prerrequisitos-fase0.md`). Si no se cumplen, la respuesta es «todavía no, sigue en Adoption».

**Jefe de plataforma (¿qué stack elijo?).** [Criterios funcionales](./criterios-funcionales.md) → [appendix/stacks-referencia/](./appendix/stacks-referencia/) → [guia-arquitectura-funcional.md](./guia-arquitectura-funcional.md) → [guia-adopcion-por-fases.md](./guia-adopcion-por-fases.md) Fase 1.

**Transformación digital (¿cómo llevo mi Constitución a policy?).** [convenciones-mapping-constitucion-policy.md](./convenciones-mapping-constitucion-policy.md) → `templates/federation/ficha-policy-template.md` → [appendix/policy-templates/](./appendix/policy-templates/).

**Tech lead que modela un agente.** [esquema-identidad-agente.md](./esquema-identidad-agente.md) → `templates/federation/descriptor-agente.md` → [esquema-bloque-contexto-cultural.md](./esquema-bloque-contexto-cultural.md) → `templates/federation/runbook-onboarding-agente.md`.

**Custodia / SRE (¿cómo gobierno la federación?).** [gobernanza-federada.md](./gobernanza-federada.md) → [patrones-deteccion-drift.md](./patrones-deteccion-drift.md) → [metricas-federacion.md](./metricas-federacion.md).

**Contribuidor al framework.** [regla-anti-acoplamiento.md](./regla-anti-acoplamiento.md) primero, siempre.

---

## 4. Navegación por preguntas frecuentes

- **«Quiero dar de alta un agente nuevo.»** → [esquema-identidad-agente.md](./esquema-identidad-agente.md) (qué declarar) + `templates/federation/runbook-onboarding-agente.md` (cómo, incluido el gate de coherencia).
- **«Quiero retirar un agente.»** → `templates/federation/runbook-retirada-agente.md` (deregister, revoke, archive, notify).
- **«Una llamada se ha bloqueado y quiero aprobarla.»** → [gobernanza-federada.md](./gobernanza-federada.md) (gestión de excepciones) + `templates/federation/registro-excepciones.md`.
- **«Cómo sé si la federación está drifteando.»** → [patrones-deteccion-drift.md](./patrones-deteccion-drift.md) + `templates/federation/playbook-deteccion-drift.md`.
- **«Necesito cambiar de gateway / policy engine / stack.»** → [criterios-funcionales.md](./criterios-funcionales.md) (lo que el nuevo stack debe cumplir) + [appendix/stacks-referencia/](./appendix/stacks-referencia/). El cuerpo no cambia.
- **«Cómo viaja el contexto cultural por MCP.»** → [esquema-bloque-contexto-cultural.md](./esquema-bloque-contexto-cultural.md) (el qué) + [appendix/mapeo-transporte/](./appendix/mapeo-transporte/) (el cómo, por protocolo).

---

## 5. Relación con el resto del ecosistema Myrmion

Federation es la segunda fase del trayecto cultural; la primera es [Myrmion Adoption](../adoption/manifesto.md), de donde viene la Constitución Corporativa que aquí se materializa programáticamente. La frontera es bidireccional: se puede volver a Adoption sin tirar el trabajo (manifiesto §10). El [manifiesto paraguas](../manifesto.md) sitúa los tres frameworks del ecosistema.

La [Guía de protección de datos](../adoption/guia-proteccion-datos.md) de Adoption articula la capa técnica de des-identificación y la contractual de licenciamiento; Federation es donde la des-identificación inline en la ruta — que en Adoption no tenía punto de inserción — se vuelve nativa ([CF-06](./criterios-funcionales.md), §3.3 del manifiesto).

---

## 6. Estado del corpus

A fecha de esta versión, el manifiesto y los cimientos normativos (índice, glosario, criterios funcionales, regla anti-acoplamiento) están cerrados; el resto del cuerpo, las plantillas, el apéndice y los ejemplos se están redactando. Los documentos marcados 📝 draft arriba indican lo pendiente. La matriz de cobertura del manifiesto (qué sección del manifiesto materializa cada documento) se mantiene como artefacto de verificación.

---

*Índice de Myrmion Federation — versión 1.0. Parte del corpus normativo.*
