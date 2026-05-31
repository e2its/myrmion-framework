# Apéndice — Catálogo de plantillas de policy

> **Banner de vigencia.** Este documento pertenece al **apéndice vivo** de Myrmion Federation. A diferencia del cuerpo normativo, el apéndice **sí menciona productos, dialectos y versiones concretos** y, por tanto, **caduca**. Los snippets de este catálogo se escribieron contra dialectos de policy engine con la sintaxis vigente en su fecha de revisión. Antes de copiar un snippet a producción, **verifica la versión** del motor y del dialecto que uses. Si encuentras una divergencia, abre una propuesta de corrección (ver «Cómo contribuir»).
>
> | Campo | Valor |
> |-------|-------|
> | Última revisión del catálogo | 2026-05-30 |
> | Dialectos cubiertos | Rego (OPA), Cedar |
> | Estado | Vivo — sujeto a caducidad |

---

## Qué es este catálogo

Este catálogo reúne **fichas de policy template**: traducciones de referencia, ya pobladas, de principios de la Constitución recurrentes a policy ejecutable por un policy engine ([CF-03](../../criterios-funcionales.md)).

Cada ficha parte de un **principio de la Constitución** típico (uno de esos que casi toda organización acaba escribiendo de una forma u otra) y lo lleva, paso a paso, hasta el snippet que un policy engine evalúa en runtime. No inventan un principio nuevo: muestran **cómo se traduce** uno que ya existe, qué campos del descriptor de identidad y del bloque de contexto cultural disparan la regla, qué efecto produce, qué evidencia deja y en qué punto de aplicación se evalúa.

El catálogo es **material de referencia**, no normativo. El contrato — qué campos existen, qué decisiones puede tomar la policy, qué significa la trazabilidad constitucional — lo fija el cuerpo. Aquí solo materializamos ese contrato en dialectos concretos para acelerar la adopción (manifiesto §3.3: «el catálogo es comunidad, no manifiesto»).

### Por qué vive en el apéndice

El cuerpo normativo es **agnóstico de producto** por diseño: no nombra dialectos, no nombra motores, no nombra versiones (regla anti-acoplamiento §3). Esa decisión mantiene el corpus portable y duradero. Pero la adopción real necesita, en algún momento, escribir Rego o Cedar de verdad.

Resolvemos la tensión separando los dos planos:

- **El cuerpo** define el contrato y las convenciones de traducción de Constitución a policy, sin atarse a ningún dialecto. Ver [`../../convenciones-mapping-constitucion-policy.md`](../../convenciones-mapping-constitucion-policy.md).
- **El apéndice** (aquí) materializa esas convenciones en dialectos nombrados, asumiendo que caducará y se mantendrá.

Si algún día un dialecto desaparece o cambia de sintaxis, **el apéndice envejece, el cuerpo no** (manifiesto §3.3: «se desacopla deliberadamente del cuerpo para que el framework no envejezca con cada release de Cedar o OPA»).

---

## Relación con las convenciones de mapping del cuerpo

Cada ficha de este catálogo es una **instancia** de las convenciones descritas en [`../../convenciones-mapping-constitucion-policy.md`](../../convenciones-mapping-constitucion-policy.md). En particular, toda ficha respeta:

- **Trazabilidad constitucional obligatoria.** Cada ficha nombra el **principio** y su **§** de origen. Ninguna regla aparece sin un principio que la justifique (manifiesto §5; convenciones §5).
- **Los cuatro efectos del contrato.** Los snippets solo producen los efectos normativos del mapping: `allow`, `deny`, `redact` y `require-prior-hop` (convenciones §3, paso 3). Ninguna ficha inventa un quinto efecto.
- **Las tres clases de automatizabilidad.** Cada ficha se clasifica como `duro`, `blando` o `no-automatizable` (glosario §4; convenciones §2). La duda se resuelve hacia la clase más débil.
- **Lectura de campos contractuales.** Los disparadores leen campos del **descriptor de identidad** (`capabilities[].canCommit`, `capabilities[].externalizes`, `capabilities[].sideEffectClass`, `capabilities[].dataClassesTouched`, `domain`, `agentId`) y del **bloque de contexto cultural** (`decisionChain` y sus `DecisionHop`, `correlationId`, `businessCaseId`, `deidTokens`) tal como los definen sus esquemas. No leen campos inventados.
- **Punto de aplicación explícito.** Cada ficha declara si evalúa en **pre-invocación** o en **post-resultado** (convenciones §3, paso 5).
- **Evidencia y degradación segura.** Cada decisión deja evidencia (convenciones §3, paso 4) y declara su comportamiento ante el fallo: por defecto `deny`, nunca `allow` en silencio (convenciones §3, paso 6).

El cuerpo manda. Si un snippet de este catálogo contradijera al cuerpo, **el snippet está mal**, no el cuerpo.

---

## Formato de las fichas

Todas las fichas siguen el formato definido por la plantilla del cuerpo: [`../../../../templates/federation/ficha-policy-template.md`](../../../../templates/federation/ficha-policy-template.md). Cada ficha contiene, como mínimo:

| Sección | Qué contiene |
|---------|--------------|
| Principio + § | El principio de la Constitución de origen y su sección. |
| `automatabilityClass` | `duro`, `blando` o `no-automatizable` (glosario §4). |
| Disparador | Qué campos del descriptor o del bloque de contexto activan la regla. |
| Efecto | La decisión que produce: `allow`, `deny`, `redact` o `require-prior-hop`. |
| Evidencia | Qué rastro auditable deja la decisión (se ancla al `DecisionHop`). |
| Punto de aplicación | `pre-invocación` o `post-resultado`. |
| Caveats | Qué no cubre, qué supone, dónde puede fallar; comportamiento ante el fallo. |
| `testVectors` | Casos de entrada/salida esperada para verificar la traducción. |
| Snippets | Implementación de referencia por dialecto (Rego, Cedar). |

### Las tres clases de `automatabilityClass`

Tal como las fija el glosario §4 y las desarrolla convenciones §2:

| Clase | Significado |
|-------|-------------|
| `duro` | Regla booleana exacta sobre campos declarados. Dos evaluadores llegan siempre al mismo resultado. Es la clase preferente. |
| `blando` | Umbral + defensa en profundidad. La regla se evalúa mecánicamente pero conlleva un margen de error que se acota combinando controles. |
| `no-automatizable` | Juicio fino que ninguna regla reproduce con fidelidad. No se traduce a decisión automática: se enruta a juicio humano (`require-prior-hop`) y se deja constancia. |

---

## Catálogo

| Ficha | Principio de origen | Efecto principal | `automatabilityClass` | Punto de aplicación |
|-------|---------------------|------------------|------------------------|---------------------|
| [`paso-por-legal.md`](./paso-por-legal.md) | «No asumimos compromisos sin pasar por Legal» | `require-prior-hop` | `duro` | pre-invocación |
| [`cifras-sin-finanzas.md`](./cifras-sin-finanzas.md) | «No se exteriorizan cifras financieras sin pasar por Finanzas» | `deny` | `blando` | pre-invocación |
| [`dlp-pii-phi.md`](./dlp-pii-phi.md) | «Los datos identificables viajan des-identificados» | `redact` | `blando` | pre-invocación |

---

## Cómo contribuir

Este catálogo es vivo. Aceptamos:

1. **Nuevas fichas** para principios de la Constitución recurrentes que aún no estén cubiertos.
2. **Nuevos dialectos** en fichas existentes (un snippet equivalente en otro policy engine).
3. **Correcciones de caducidad**: cuando un dialecto cambie de sintaxis o un motor deprecie una construcción usada en un snippet.

Reglas para contribuir:

- **Usa la plantilla del cuerpo.** Toda ficha nueva parte de [`../../../../templates/federation/ficha-policy-template.md`](../../../../templates/federation/ficha-policy-template.md). No improvises el formato.
- **Cita el principio.** Sin principio + § de origen, no hay ficha. La trazabilidad constitucional es innegociable (manifiesto §5).
- **Respeta el contrato.** Lee solo campos contractuales; produce solo los cuatro efectos. Si necesitas algo que el contrato no ofrece, lo que falla es la propuesta, y el lugar de discusión es el cuerpo, no el apéndice.
- **Aporta `testVectors`.** Un snippet sin vectores de prueba no se acepta: sin ellos no se puede verificar que la traducción mantiene fidelidad (convenciones §1).
- **Declara la degradación segura.** Toda ficha dice qué pasa cuando falta un campo o no se puede evaluar: `deny` por defecto.
- **Marca la fecha y la versión del dialecto.** Todo snippet nuevo o corregido actualiza la fila correspondiente del banner de vigencia.
- **Mantén el agnosticismo donde corresponde.** Las marcas viven **aquí**, en el apéndice (regla anti-acoplamiento §5). Si tu propuesta toca el cuerpo, no menciones productos.

El alta de fichas y la custodia del apéndice siguen la asimetría de fricción de la regla anti-acoplamiento §5: un PR al apéndice necesita revisión ligera de la comunidad; un PR al cuerpo, aprobación de custodio.

---

## Enlaces relacionados

- Convenciones de mapping (cuerpo): [`../../convenciones-mapping-constitucion-policy.md`](../../convenciones-mapping-constitucion-policy.md)
- Plantilla de ficha (cuerpo): [`../../../../templates/federation/ficha-policy-template.md`](../../../../templates/federation/ficha-policy-template.md)
- Criterios funcionales: [`../../criterios-funcionales.md`](../../criterios-funcionales.md) — CF-03 (policy engine), CF-06 (DLP en la ruta)
- Esquema del descriptor de identidad: [`../../esquema-identidad-agente.md`](../../esquema-identidad-agente.md)
- Esquema del bloque de contexto cultural: [`../../esquema-bloque-contexto-cultural.md`](../../esquema-bloque-contexto-cultural.md)
- Mapeo de transporte (apéndice): [`../mapeo-transporte/`](../mapeo-transporte/)
- Glosario de la federación: [`../../glosario-federacion.md`](../../glosario-federacion.md)
- Manifiesto: [`../../manifesto.md`](../../manifesto.md)

---

*Apéndice vivo de Myrmion Federation. Material de referencia, no normativo. Las marcas y versiones aquí citadas caducan: verifica la vigencia antes de usar.*
