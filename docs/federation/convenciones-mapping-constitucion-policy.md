# Myrmion Federation — Convenciones de mapping de la Constitución a policy

**Versión 1.0**

*Materializa §3.3 del manifiesto: el método por el que cada principio de la Constitución, escrito en lenguaje natural, se traduce a una regla evaluable —o se marca explícitamente como no automatizable— sin perder fidelidad.*

---

## Propósito

La Constitución de la federación está escrita en lenguaje natural. Esa es una decisión, no una limitación: un principio se entiende, se discute y se aprueba en prosa, no en sintaxis de motor. Pero un principio en prosa no se puede evaluar en una llamada entre agentes. El **mapping** es el puente: convierte cada principio en una regla que un punto de aplicación puede ejecutar, sin que el principio pierda lo que quería decir.

Este documento fija las **convenciones** del mapping: qué clase de regla corresponde a qué clase de principio, cómo se traduce un principio paso a paso, qué partes del descriptor de identidad y del bloque de contexto cultural se usan como disparador, y qué se hace con lo que no es traducible. No es el catálogo de reglas ni el formato de cada ficha: esos viven, respectivamente, en el apéndice y en la plantilla, y este documento remite a ellos.

La regla que gobierna este puente es la de §5 del manifiesto: *sin mapping, la Constitución es un deseo; con mapping, es un control*. Y la frontera que lo limita es la de §8: *lo que no es traducible a regla queda como juicio en el agente, y se dice explícitamente*.

---

## 1. La Constitución es lenguaje natural; el mapping la hace evaluable

Un principio constitucional declara una obligación, un límite o un derecho de la federación en términos que una persona puede aprobar. Por ejemplo: *"ningún agente comercial puede comprometer a la organización sin que Legal haya validado la cláusula"*. Eso es claro para un humano y opaco para un punto de aplicación.

El mapping no reescribe el principio: lo **deriva**. Toma la obligación expresada en prosa y la descompone en cuatro piezas que un punto de aplicación sí entiende:

1. **Disparador** — la condición observable, leída de campos del descriptor de identidad y del bloque de contexto cultural, que indica que el principio aplica a este salto.
2. **Efecto** — la acción que el principio impone cuando el disparador se cumple: `allow`, `deny`, `redact` o `require-prior-hop`.
3. **Evidencia** — el registro verificable de que la regla se evaluó y con qué resultado.
4. **Punto de aplicación** — el momento del ciclo de la llamada en que se evalúa: pre-invocación o post-resultado.

La **fidelidad** es la propiedad que define un buen mapping: la regla derivada debe permitir todo lo que el principio permite y denegar todo lo que el principio prohíbe, sin añadir ni quitar. Cuando un principio no se puede derivar con fidelidad a una regla mecánica, no se fuerza la traducción: se clasifica como no automatizable (§4) y se documenta como tal. Forzar una regla infiel es peor que no tener regla, porque crea la ilusión de control donde no lo hay.

Esta derivación realiza el criterio funcional [CF-03](./criterios-funcionales.md): que exista una Constitución versionada y un mapping que, principio a principio, declare disparador, efecto, evidencia y punto de aplicación, o lo marque como no automatizable.

**El mismo método sirve para el Marco Regulatorio.** Aunque este documento habla de «la Constitución» por brevedad, las convenciones de mapping se aplican igual a los principios del **Marco Regulatorio**: se derivan a regla con el mismo disparador / efecto / evidencia / punto de aplicación. La diferencia no está en *cómo* se derivan, sino en su **`origen`** —Constitución o Marco—, que la [ficha de policy](../../templates/federation/ficha-policy-template.md) declara y que determina el tratamiento de su violación: las reglas de la Constitución son **excepcionables**; las del Marco **no** —el intento de excepción es una alerta a legal/DPO tratada como incidente ([gobernanza](./gobernanza-federada.md) §3). Por eso el catálogo marca el origen de cada regla.

---

## 2. Taxonomía de automatizabilidad

No todos los principios se traducen igual, porque no todos tienen la misma naturaleza. Antes de derivar una regla hay que clasificar el principio en una de tres clases. La clase determina qué clase de regla es legítimo escribir y cuánta defensa hay que poner alrededor.

### Clase DURO — regla booleana exacta

Un principio es **duro** cuando su cumplimiento se decide con una condición booleana evaluable sin ambigüedad sobre campos declarados. No hay margen de interpretación: o el disparador se cumple o no se cumple, y el efecto es determinista.

**Criterios para clasificar un principio como DURO:**

- El disparador se expresa íntegramente con campos del descriptor (`capabilities.externalizes`, `canCommit`, `sideEffectClass`, `dataClassesTouched`) o del bloque de contexto cultural (`jurisdiction`, `dataSensitivity`, `language`, `businessRules`), comparados con valores fijos.
- Dos evaluadores que apliquen la regla a la misma entrada llegan siempre al mismo resultado.
- El efecto no depende de cuánto, sino de si: no hay umbral, hay condición.

**Ejemplo de principio duro:** *"Una capacidad que puede comprometer a la organización no puede ejecutarse si el salto previo de validación de Legal no consta."* El disparador (`canCommit = true`) es exacto; el efecto (`require-prior-hop`) es determinista.

El mapping de un principio duro es directo y se evalúa de una sola vez en su punto de aplicación. Es la clase preferente: cuando un principio se puede expresar como duro sin perder fidelidad, se expresa como duro.

### Clase BLANDO — umbral con defensa en profundidad

Un principio es **blando** cuando su cumplimiento depende de una magnitud, una probabilidad o una señal que admite umbral, pero no certeza. La regla puede evaluarse mecánicamente, pero su resultado conlleva un margen de error que hay que acotar.

**Criterios para clasificar un principio como BLANDO:**

- El disparador depende de un valor continuo o de una estimación (p. ej. un nivel de sensibilidad inferido, una puntuación de riesgo, una cantidad) comparado con un umbral.
- Un falso positivo o un falso negativo es posible y tiene coste; el umbral es una elección de compromiso, no una verdad.
- El cumplimiento no se garantiza con una sola comprobación: se refuerza combinando varias.

Un principio blando exige **defensa en profundidad**: nunca se confía a un único disparador. Se combinan controles —por ejemplo, un umbral en pre-invocación más una redacción en post-resultado más una marca en la evidencia para revisión posterior— de modo que el fallo de uno no abra la frontera. El umbral se documenta como un parámetro de la ficha, no como una constante oculta, para que pueda revisarse sin reescribir el principio.

**Ejemplo de principio blando:** *"El contexto que cruza a otro dominio no debe exponer datos sensibles más allá de lo necesario."* "Lo necesario" no es booleano: se acota con un umbral de sensibilidad (`dataSensitivity`) que dispara `redact`, reforzado con `deidTokens` para los campos que aun así deben correlacionarse, y con evidencia de qué se redactó.

### Clase NO-AUTOMATIZABLE — juicio fino que permanece en el agente

Un principio es **no automatizable** cuando su cumplimiento exige un juicio que ninguna regla mecánica reproduce con fidelidad: valoración de proporcionalidad, lectura de intención, ponderación de circunstancias o decisión que la organización reserva a una persona.

**Criterios para clasificar un principio como NO-AUTOMATIZABLE:**

- No existe un conjunto de campos declarados cuya combinación capture el principio sin perder lo esencial.
- Dos personas razonables y bien informadas podrían decidir distinto, y esa diferencia es legítima.
- Reducir el principio a un umbral o a un booleano falsificaría su intención.

Un principio no automatizable **no se traduce a regla**: se documenta como modelado que permanece en el agente o como decisión que se enruta a un humano. Esto es exactamente lo que el manifiesto reserva en §8: la federación enruta el criterio humano, no lo suprime. La ficha de un principio no automatizable existe igualmente —para dejar constancia de que el principio fue considerado y de por qué no se mecanizó—, pero su "efecto" es `require-prior-hop` hacia el punto de juicio, no una decisión automática.

**Ejemplo de principio no automatizable:** *"Una propuesta debe ser justa para ambas partes."* La justicia de una propuesta no se decide con campos: se decide con criterio. El mapping enruta la decisión a Legal y deja constancia; no la sustituye.

### Cómo elegir la clase

La clasificación se hace en este orden, de la más fuerte a la más débil:

1. ¿Se puede expresar el principio como una condición booleana exacta sobre campos declarados, sin perder fidelidad? → **DURO**.
2. Si no, ¿se puede acotar con un umbral más defensa en profundidad, asumiendo y documentando el margen de error? → **BLANDO**.
3. Si no, no se fuerza la traducción → **NO-AUTOMATIZABLE**, y se enruta a juicio humano con constancia.

La duda se resuelve siempre hacia la clase más débil. Clasificar como duro lo que es blando crea reglas frágiles; clasificar como automatizable lo que exige juicio crea reglas infieles. La degradación segura ([CF-06](./criterios-funcionales.md)) gobierna también aquí: ante la duda sobre si un principio es evaluable, se trata como no evaluable y se deniega o se enruta, nunca se permite en silencio.

---

## 3. Procedimiento de mapping paso a paso

Cada principio de la Constitución se mapea siguiendo el mismo procedimiento. El resultado es una ficha de policy (formato en §4).

### Paso 1 — Del principio a su clase

Se enuncia el principio tal como aparece en la Constitución y se clasifica según la taxonomía de §2. La clase condiciona todos los pasos siguientes.

### Paso 2 — Del principio al disparador

El disparador es la condición observable que dice "este principio aplica a este salto". Se construye **solo** con campos declarados, nunca con inferencias sobre el transporte ni sobre la red. Las fuentes legítimas del disparador son:

- **Del descriptor de identidad** ([esquema](./esquema-identidad-agente.md)):
  - `capabilities.externalizes` — si la capacidad invocada expone resultados fuera del dominio del agente.
  - `canCommit` — si la capacidad puede comprometer a la organización.
  - `sideEffectClass` — `read`, `write` o `external`.
  - `dataClassesTouched` — clases de datos que la capacidad lee o produce.
- **Del bloque de contexto cultural** ([esquema](./esquema-bloque-contexto-cultural.md)):
  - `language`, `jurisdiction`, `dataSensitivity`, `businessRules` — el marco interpretativo del salto.
  - Campos del `DecisionHop` — en especial la existencia o ausencia de un salto previo (`fromAgent`, `toAgent`, `policyRefs`).

Para un principio duro, el disparador es una condición booleana sobre estos campos. Para un principio blando, es una comparación contra umbral más los controles de refuerzo. Para un principio no automatizable, el disparador identifica cuándo escalar a juicio, no cuándo decidir.

### Paso 3 — Del disparador al efecto

Cuando el disparador se cumple, la regla impone uno de los cuatro efectos normativos:

- `allow` — la colaboración procede.
- `deny` — la colaboración se rechaza.
- `redact` — el resultado se devuelve con datos suprimidos o sustituidos por `deidTokens`.
- `require-prior-hop` — la colaboración exige que conste un salto previo (p. ej. una validación) antes de proceder.

El efecto debe ser consistente con la clase: un principio duro produce un efecto determinista; un principio blando suele combinar `redact` con marcas de evidencia; un principio no automatizable produce `require-prior-hop` hacia el punto de juicio.

### Paso 4 — Del efecto a la evidencia

Toda evaluación deja **evidencia**: el registro verificable de que la regla se evaluó, con qué entrada y con qué resultado. La evidencia se ancla al `DecisionHop` del salto (campo `policyRefs` y `outcome`) y alimenta la cadena de custodia. Sin evidencia, una regla no es auditable, y una regla no auditable no satisface [CF-05](./criterios-funcionales.md). La evidencia es obligatoria incluso cuando el efecto es `allow`: que algo se permitió debe constar igual que que algo se denegó.

### Paso 5 — Del efecto al punto de aplicación

Cada regla declara **dónde** se evalúa en el ciclo de la llamada:

- **Pre-invocación** — antes de que el agente llamado ejecute. Aquí se deciden `allow`, `deny` y `require-prior-hop`, porque dependen de si la colaboración puede siquiera empezar.
- **Post-resultado** — antes de devolver el resultado al llamante. Aquí se decide `redact`, porque depende de lo que el resultado contiene.

Un mismo principio puede generar reglas en ambos puntos (típico de los principios blandos, que disparan en pre-invocación y refuerzan en post-resultado). El punto de aplicación nunca se deja implícito: forma parte de la ficha.

### Paso 6 — Cierre con degradación segura

Antes de dar por cerrada una regla se comprueba su comportamiento ante el fallo: si un campo necesario para el disparador falta, si la identidad no se puede verificar o si la regla no se puede evaluar, el resultado por defecto es `deny` con evidencia, nunca `allow` en silencio ([CF-06](./criterios-funcionales.md)). Una regla que no especifica su comportamiento ante el fallo está incompleta.

---

## 4. Dónde vive el formato y dónde vive el catálogo

Este documento fija el **método** del mapping. No define el formato de cada ficha ni enumera el catálogo de reglas, para no acoplar el método ni a una plantilla concreta ni a un motor concreto.

- El **formato de la ficha de policy** —los campos que toda ficha debe rellenar y cómo— vive en la plantilla socrática [`templates/federation/ficha-policy-template.md`](../../templates/federation/ficha-policy-template.md). Una ficha es la unidad del mapping; la plantilla es su esqueleto.
- El **catálogo poblado** —fichas concretas ya rellenas, con sus disparadores, efectos y, donde corresponde, el dialecto de motor con que se materializa cada regla— vive en el apéndice, en [`appendix/policy-templates/`](./appendix/policy-templates/). Allí, y solo allí, las reglas tocan el suelo tecnológico.

Esta separación es deliberada: el método del mapping no cambia cuando cambia el motor, y por eso el dialecto de motor no aparece en este documento. Si una regla del catálogo necesita ilustrar un disparador, lo hace en el apéndice, junto a la marca que lo materializa.

---

## 5. No todo es traducible

El manifiesto lo dice sin rodeos en §8: *lo que no es traducible a regla queda como juicio en el agente, y se dice explícitamente*. Este documento lo convierte en disciplina de método.

Un mapping honesto no es el que traduce todos los principios, sino el que traduce los que se pueden traducir con fidelidad y **declara con la misma claridad** los que no. Un principio no automatizable que aparece sin ficha es un agujero de gobierno disfrazado de cobertura total; un principio no automatizable documentado como tal es una decisión de gobierno tomada con los ojos abiertos.

Por eso la clase NO-AUTOMATIZABLE no es un cajón de descarte: es una salida de primera clase del procedimiento. Marca el límite entre lo que la federación decide y lo que enruta a una persona. Respetar ese límite es lo que separa un control de una pretensión de control.

---

## Pseudo-policy neutral (ilustrativo, sin dialecto de motor)

Una regla derivada se puede expresar de forma neutral, sin sintaxis de ningún motor, para razonar sobre ella antes de materializarla. La forma neutral solo nombra campos del descriptor y del bloque, y los cuatro efectos normativos:

```
regla: compromiso-requiere-validacion-legal   (clase: DURO)
  cuando:
    capability.canCommit == true
    y NO existe DecisionHop previo con policyRefs incluyendo "validacion-legal"
  entonces:
    efecto = require-prior-hop -> dominio "legal"
  punto-aplicacion: pre-invocacion
  evidencia: registrar en DecisionHop.policyRefs y DecisionHop.outcome
  ante-fallo: deny con evidencia
```

```
regla: redaccion-de-datos-sensibles-en-frontera   (clase: BLANDO)
  cuando:
    dataSensitivity >= umbral_sensibilidad
    y toAgent.domain != fromAgent.domain
  entonces:
    efecto = redact   (sustituir por deidTokens los campos por encima del umbral)
  punto-aplicacion: post-resultado
  evidencia: registrar qué campos se redactaron
  defensa-en-profundidad: combinar con control de pre-invocacion sobre dataClassesTouched
  ante-fallo: deny con evidencia
```

Estas formas son ilustrativas y no normativas: su único fin es mostrar cómo el método de §3 produce una regla legible sin atarse a ningún motor. El dialecto concreto vive en el apéndice.

---

*Myrmion Federation — Convenciones de mapping de la Constitución a policy, versión 1.0. Parte del corpus normativo.*

**Relacionados:**

- [Manifiesto de la federación](./manifesto.md) — §3.3 (Capa 3, Gobierno), §5 (Gobernanza), §8 (lo que no es).
- [Criterios funcionales](./criterios-funcionales.md) — [CF-03](./criterios-funcionales.md) (gobierno por Constitución mapeada), [CF-05](./criterios-funcionales.md) (trazabilidad), [CF-06](./criterios-funcionales.md) (degradación segura).
- [Glosario de la federación](./glosario-federacion.md) — Constitución, Mapping, Ficha de policy, Disparador, Efecto, Punto de aplicación, Evidencia.
- [Esquema del descriptor de identidad de agente](./esquema-identidad-agente.md) — campos del disparador.
- [Esquema del bloque de contexto cultural](./esquema-bloque-contexto-cultural.md) — campos del disparador y DecisionHop.
- [Guía de arquitectura funcional](./guia-arquitectura-funcional.md) — la función de gobierno y sus puntos de aplicación.
- [La regla anti-acoplamiento](./regla-anti-acoplamiento.md) — por qué el dialecto de motor no aparece en este documento.
- Plantilla: [`templates/federation/ficha-policy-template.md`](../../templates/federation/ficha-policy-template.md) — formato de la ficha de policy.
- Apéndice: [`appendix/policy-templates/`](./appendix/policy-templates/) — catálogo poblado con dialectos de motor.
