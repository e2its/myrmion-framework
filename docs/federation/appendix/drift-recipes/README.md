# Myrmion Federation — Apéndice vivo: recetas sectoriales de detección de drift

**Versión 1.0**

*Materializa el §6 de [`../../patrones-deteccion-drift.md`](../../patrones-deteccion-drift.md): el cuerpo normaliza **qué observar, cómo y quién responde** de forma agnóstica al sector; aquí —y solo aquí— se afinan **umbrales concretos, cadencias y herramientas** para sectores donde la criticidad lo exige.*

> **BANNER DE VIGENCIA.** Esta carpeta envejece rápido por diseño. Las recetas fijan números, escenarios y nombres de producto a una fecha concreta y **caducan**: un umbral razonable hoy puede dejar de serlo cuando cambie la regulación, el volumen de la federación o el panorama de herramientas. **No cites una receta como si fuera normativa.** Lo normativo son los tres patrones del cuerpo ([`../../patrones-deteccion-drift.md`](../../patrones-deteccion-drift.md)); esto es su afinado operativo, que alguien tiene que recalibrar.
>
> **Última revisión global de esta carpeta:** 2026-05-30. Si lees esto mucho después, asume que está desactualizado hasta que una receta demuestre lo contrario.

---

## Qué es una receta sectorial

El cuerpo define los tres patrones de detección de drift federado —**Patrón A** (análisis de cadenas de decisiones), **Patrón B** (análisis de excepciones) y **Patrón C** (análisis de coherencia entre agentes)— con una rejilla fija: entradas, método, señales/umbrales, cadencia, responsable, qué dispara revisión y qué NO es. Y lo hace **sin fijar el número exacto**: el propio documento declara que «cada organización fija el tamaño de "persistente / sostenido" en su receta sectorial; lo normativo aquí es **qué configuración cualifica**, no el número exacto» (§3.3).

Una **receta sectorial** es ese afinado. No inventa patrones nuevos ni los redefine: toma los del cuerpo, los referencia por su identificador (Patrón A, B, C) y les concreta, para un dominio regulado:

- **Umbrales numéricos** de las señales —cuánto es «persistente», qué tasa de excepción dispara, qué tolerancia de regresión—.
- **Cadencias afinadas**, casi siempre **más estrictas** que la base, porque estos sectores caen en el escalón de **criticidad alta** del modulador del cuerpo (§2.1: cadencia base ÷ 2 y revisión obligatoria ante la primera señal fuerte).
- **Escenarios de coherencia** específicos para el banco del Patrón C: los dilemas que en ese sector hay que probar en frío.
- **Herramientas e instrumentación** concretas que ayudan a poblar las entradas y a vigilar las señales. Aquí —y solo aquí— se nombran productos.

## Por qué viven en el apéndice y no en el cuerpo

Por la [regla anti-acoplamiento](../../regla-anti-acoplamiento.md). El cuerpo es agnóstico al sector y a la herramienta para que dure años; las recetas son lo contrario: opinadas, fechadas, atadas a un régimen regulatorio y a un mercado de productos que cambian. El *test de pertenencia* (regla §1) lo zanja: **una receta no sigue siendo verdadera tras cambiar el stack o el régimen regulatorio entero**, luego no es cuerpo. De ahí tres reglas operativas:

- El cuerpo nunca depende de una receta.
- Una receta **siempre** referencia el patrón del cuerpo que afina por su identificador, no lo reescribe.
- Si una receta contradice el cuerpo, **manda el cuerpo**. La receta está obsoleta o mal calibrada.

## Cómo se lee una receta

Cada receta de esta carpeta sigue la misma estructura, para que sean comparables entre sí:

1. **Banner de vigencia** propio (fecha, cadencia de revisión, régimen regulatorio asumido).
2. **A qué patrones del cuerpo afina** y por qué este sector necesita afinado.
3. **Categorías de dato** del sector y cómo se tratan en el bloque de contexto cultural (siempre vía `deidToken`, nunca en claro).
4. **Escenarios de coherencia** (afinado del Patrón C) ilustrados sobre el caso del cuerpo: el corredor comercial→legal.
5. **Umbrales y cadencias** por patrón, más estrictos que la base.
6. **Herramientas e instrumentación** sugeridas (apéndice: se nombran marcas).

## Relación con el resto del corpus

| Nivel | Documento | Qué aporta |
| --- | --- | --- |
| Cuerpo normativo | [`../../patrones-deteccion-drift.md`](../../patrones-deteccion-drift.md) | Los tres patrones y la rejilla fija. **Manda sobre cualquier receta.** |
| Cuerpo normativo | [`../../regla-anti-acoplamiento.md`](../../regla-anti-acoplamiento.md) | Por qué los productos viven aquí (test de pertenencia §1). |
| Cuerpo normativo | [`../../criterios-funcionales.md`](../../criterios-funcionales.md) | CF-05 (observabilidad agent-aware) y CF-06 (des-identificación en la ruta), que instrumentan las recetas. |
| Cuerpo normativo | [`../../esquema-bloque-contexto-cultural.md`](../../esquema-bloque-contexto-cultural.md) | `correlationId`, `criteriaApplied`, `DecisionHop`, `deidToken`, `constitutionHash` que las recetas consumen. |
| Plantilla | [`../../../../templates/federation/playbook-deteccion-drift.md`](../../../../templates/federation/playbook-deteccion-drift.md) | La plantilla operativa donde se vuelcan los umbrales de una receta. |
| Apéndice (vivo) | [`../README.md`](../README.md) | El catálogo de componentes candidatos (gateways, policy engines, motores de DLP) que las recetas citan. |
| Adoption | [`../../../../docs/adoption/guia-proteccion-datos.md`](../../../../docs/adoption/guia-proteccion-datos.md) | El panorama de des-identificación y licenciamiento por requisito regulatorio. |

## Recetas disponibles

| Sector | Receta | Patrones que afina | Estado |
| --- | --- | --- | --- |
| Sanidad / salud | [`sanidad.md`](./sanidad.md) | Patrón A, Patrón C (y nota sobre B) | Vigente (rev. 2026-05-30) |

> ¿Falta tu sector (financiero, sector público, seguros…)? Una receta nueva se aporta como fichero hermano en esta carpeta, replicando la estructura de arriba y **siempre** con su banner de vigencia. Custodia de comunidad: como el resto del apéndice, un PR aquí necesita revisión ligera ([`../README.md`](../README.md), CODEOWNERS de comunidad). Y una salvaguarda: si descubres una señal de drift que vale **para todos los sectores**, no la entierres en una receta —llévala al cuerpo ([`../../patrones-deteccion-drift.md`](../../patrones-deteccion-drift.md)).

---

### Enlaces relacionados

- [`../../patrones-deteccion-drift.md`](../../patrones-deteccion-drift.md) — los tres patrones (cuerpo normativo; manda sobre las recetas).
- [`../../regla-anti-acoplamiento.md`](../../regla-anti-acoplamiento.md) — test de pertenencia: por qué las marcas viven aquí.
- [`../README.md`](../README.md) — apéndice vivo: componentes candidatos y gobernanza de comunidad.
- [`../../../../templates/federation/playbook-deteccion-drift.md`](../../../../templates/federation/playbook-deteccion-drift.md) — plantilla operativa.
- [`../../manifesto.md`](../../manifesto.md) — manifiesto de Myrmion Federation (§3.4, §10).

*Recetas sectoriales de detección de drift — versión 1.0. Apéndice vivo: las recetas afinan, no derogan, los patrones del cuerpo. Contenido fechado y sujeto a caducidad.*
