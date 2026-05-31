# ADR-0002 — Decisiones de la revisión de coherencia del corpus

| Campo | Valor |
|---|---|
| ADR | 0002 |
| Ámbito | Framework (0001–0099) |
| Estado | Aceptado |
| Fecha | 2026-05-31 |
| Supera a | — |
| Superado por | — |

> Registro de tres decisiones tomadas durante el loop de revisión de coherencia del corpus (code-review adversarial, iteración 4). No son decisiones de diseño de la federación, sino resoluciones editoriales/normativas sobre cómo el corpus describe sus propios contratos. Se agrupan en un único registro por economía; cada una es independiente.

---

## Decisión 1 — El dominio es el **quinto** segmento del `agentId`, no el cuarto

**Contexto.** Varios documentos (convenciones-mapping, ficha-policy-ejemplo, fichas del apéndice) afirman que «el dominio se deriva del **quinto segmento** del `agentId`». Contando los campos delimitados por `:` en `urn:myrmion:agent:<org>:<dominio>:<nombre>`: 1=`urn`, 2=`myrmion`, 3=`agent`, 4=`<org>`, 5=`<dominio>`, 6=`<nombre>`. El quinto segmento es `<org>`; el dominio es el **quinto**. El conteo era incorrecto y consistente en todo el corpus.

**Decisión.** El dominio es el **quinto segmento** del `agentId`. Toda referencia al «quinto segmento» como dominio se corrige a «quinto segmento». Donde sea posible se nombra el segmento (`<dominio>`) en lugar de contar, para evitar errores futuros.

**Alternativas.** (A) Dejar «cuarto» contando solo las partes variables tras el prefijo fijo `urn:myrmion:agent:` — descartada: ambigua y contradice el conteo natural por `:`. (B) No numerar, solo nombrar `<dominio>` — adoptada parcialmente como refuerzo.

**Consecuencias.** Las pseudo-policies que derivan el dominio para `require-prior-hop(legal)` quedan correctas; un implementador que cuente segmentos por `:` ya no leerá `<org>` en lugar del dominio.

---

## Decisión 2 — La **degradación segura** (fail-closed) es una convención del método de mapping, no un criterio funcional

**Contexto.** El fail-closed («ante un campo ausente o una regla no evaluable, el resultado por defecto es `deny`, nunca `allow` en silencio») se atribuía a CF-06 (DLP) y, tras un fix intermedio, a CF-03 (policy engine). Pero el checklist de **ninguno** de los dos criterios funcionales menciona la degradación segura: CF-03 exige lenguaje declarativo, latencia, versionado y los cuatro efectos; CF-06 exige detección/redacción de datos sensibles. El fail-closed es una regla del **método de mapping** (convenciones §3, paso 6). Lo mismo ocurre con la atribución a CF-03 de «que exista una Constitución versionada y un mapping que declare disparador/efecto/evidencia/punto»: eso es el método de §3.3, no el checklist de CF-03 (que es el motor que *evalúa* las policies resultantes).

**Decisión.** La degradación segura se referencia como **convención del método (`convenciones §3, paso 6`)**, sin atribuirla a ningún CF. El policy engine ([CF-03]) es quien *ejecuta* el `deny`, pero el requisito es del método, no del criterio de stack. La frase de convenciones §1 se reformula: la derivación es el método de mapping (§3.3) y *produce* las policies que CF-03 evalúa.

**Alternativas.** (A) Mantener CF-06 — descartada: el fail-closed no es DLP. (B) Mantener CF-03 — descartada: CF-03 es el motor, no declara el fail-closed en su checklist. (C) Crear un CF nuevo — descartada: «solo seis CF» es deliberado (criterios-funcionales).

**Consecuencias.** Un jefe de plataforma que verifique «¿mi stack cumple CF-03/CF-06?» ya no encuentra requisitos fantasma en esos checklists; el fail-closed queda anclado donde se define (el método).

---

## Decisión 3 — La versión de `pol-cifras-sin-finanzas` **evoluciona** en el ejemplo; se hace explícito

**Contexto.** La ficha del apéndice define `pol-cifras-sin-finanzas@1.0`; el ejemplo end-to-end (corredor) ejecuta `@1.1` y la receta de drift propone `@1.2`. Las otras tres policies del corpus tienen ficha y ejemplo con la **misma** versión, así que la divergencia de cifras parecía una incoherencia. En realidad ilustra deliberadamente la evolución de una policy (base → vigente → propuesta por drift).

**Decisión.** Se **conserva** la evolución `@1.0` (ficha base) → `@1.1` (vigente en el ejemplo) → `@1.2` (propuesta por la señal de drift), y se hace **explícita** con una nota en la ficha del apéndice, para que la diferencia de versión no se lea como incoherencia.

**Alternativas.** (A) Alinear todo a una sola versión — descartada: pierde el único ejemplo del corpus de una policy versionándose por drift, que es justo lo que el Patrón B existe para provocar. (B) Dejarlo sin nota — descartada: sin explicación, ficha y ejemplo parecen contradecirse.

**Consecuencias.** El corpus conserva un ejemplo realista de ciclo de vida de policy; el lector entiende por qué ficha (@1.0) y ejemplo (@1.1) difieren.

---

## Relacionados

- [README de los ADR](./README.md) · [plantilla](./0000-plantilla-adr.md)
- [convenciones de mapping](../convenciones-mapping-constitucion-policy.md) · [criterios funcionales](../criterios-funcionales.md) (CF-03, CF-06) · [esquema de identidad de agente](../esquema-identidad-agente.md) (formato `agentId`)

---

*Myrmion Federation — ADR-0002, versión 1.0. Parte del corpus normativo.*
