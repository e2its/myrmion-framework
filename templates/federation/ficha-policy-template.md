<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Plantilla de Ficha de Policy

**Versión 1.0**

*Plantilla socrática para redactar una entrada del catálogo de policy: el envoltorio neutral de una regla derivada de la Constitución. Materializa la capa de mapping Constitución → policy del [manifiesto](../../docs/federation/manifesto.md) §3.3 y fija el formato que exigen las [convenciones de mapping](../../docs/federation/convenciones-mapping-constitucion-policy.md). Una ficha dice **qué** hace la policy y **por qué**, nunca cómo se serializa para un motor concreto: las implementaciones por dialecto viven en el [catálogo del apéndice](../../docs/federation/appendix/policy-templates/), nunca aquí.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

Esta plantilla te guía, mediante **preguntas**, para redactar **una** entrada del catálogo de policy. Una ficha es la unidad del mapping: toma un principio de la Constitución escrito en prosa y lo lleva hasta una regla que un punto de aplicación puede ejecutar, sin perder lo que el principio quería decir.

No es un formulario que rellenar a ciegas. Cada pregunta busca que **expliciten** una decisión antes de que la regla se evalúe en producción o se audite. Las respuestas son el contrato neutral de la policy; el dialecto de motor es una materialización posterior que vive en el apéndice.

**Quién la rellena.** El custodio de la Constitución (transformación digital) decide *qué* principio se mapea y con qué efecto; la plataforma de federación decide *dónde* y *cómo* se aplica. La ficha la firman ambos, porque une un principio cultural con un control técnico.

**Esta plantilla es el envoltorio; el dialecto vive en el apéndice.** El cuerpo del corpus es agnóstico de producto por diseño ([regla anti-acoplamiento](../../docs/federation/regla-anti-acoplamiento.md) §3): aquí no se escribe ningún dialecto de motor. La serialización ejecutable de cada policy se referencia en `refImplementaciones[]`, que apunta a [`appendix/policy-templates/`](../../docs/federation/appendix/policy-templates/) — el único lugar donde las reglas tocan el suelo tecnológico.

**Instrucciones:**

1. Copia este fichero a tu catálogo y renómbralo por el `id` de la policy (p. ej. `ficha-paso-por-legal.md`).
2. Responde cada pregunta guía en el espacio indicado.
3. Mantén una ficha por policy: si necesitas dos efectos independientes, redacta dos fichas y enlázalas en `caveats`.
4. Ancla todo en el corpus: los disparadores se expresan sobre campos del [descriptor de identidad](../../docs/federation/esquema-identidad-agente.md) y del [bloque de contexto cultural](../../docs/federation/esquema-bloque-contexto-cultural.md). No inventes campos.

> **Nota — sin marcas en la ficha.** El cuerpo (esta ficha incluida) no nombra productos, dialectos ni versiones. La única excepción es MCP. Cuando una ilustración lo exija, escríbela como «(p. ej. …)» y enlaza al apéndice ([regla anti-acoplamiento](../../docs/federation/regla-anti-acoplamiento.md) §2).

> **Nota — solo cuatro efectos.** Una policy produce uno (y solo uno) de los efectos normativos del contrato: `allow`, `deny`, `redact`, `require-prior-hop` ([convenciones](../../docs/federation/convenciones-mapping-constitucion-policy.md) §3, paso 3; [CF-03](../../docs/federation/criterios-funcionales.md)). No inventes un quinto efecto.

> **Nota — para ver esta plantilla rellena**, consulta el [ejemplo de la ficha `paso-por-legal`](./ficha-policy-template-ejemplo.md).

---

## 0. Metadatos del documento

*Esta sección queda EXCLUIDA del cálculo del hash canónico, igual que en el resto del corpus (contrato de hash del [esquema de identidad](../../docs/federation/esquema-identidad-agente.md) §6): captura lo administrativo, no el contenido de la regla.*

| Campo | Valor |
|---|---|
| `id` de la policy | *(p. ej. pol-paso-por-legal)* |
| Título legible | *(qué hace la policy, en una línea)* |
| `version` de la policy (semver) | *(p. ej. 1.0)* |
| Organización | *(razón social o identificador corto)* |
| Custodio funcional | *(rol que decide qué principio se mapea — típicamente transformación digital)* |
| Custodio de aplicación | *(rol que decide dónde se aplica — plataforma de federación)* |
| Fecha de última revisión | *(YYYY-MM-DD)* |
| Estado | *(Borrador / En revisión / Vigente / Derogada)* |

---

## 1. `id`

*Pregunta guía: ¿con qué identificador estable se referencia esta policy desde el catálogo, desde el `criteriaApplied` de los `DecisionHop` y desde otras fichas? Usa minúsculas con guiones y no lo cambies aunque cambie la implementación. En el `criteriaApplied` del bloque de contexto cultural aparecerá sufijado con la versión, en la forma `<id>@<version>`.*

[Espacio para rellenar]

---

## 2. `principioConstitucional`

*Pregunta guía: ¿qué principio de la Constitución justifica esta policy, y dónde está escrito? Cita el texto del principio y su localización (§). La trazabilidad constitucional es innegociable: una regla sin principio que la respalde es un agujero de gobierno disfrazado de control (convenciones §5; manifiesto §5).*

- **Cita del principio:** [Espacio para rellenar]
- **Localización (§):** [Espacio para rellenar]

---

## 3. `automatabilityClass`

*Pregunta guía: ¿hasta qué punto este principio se puede materializar en regla sin pérdida de fidelidad? Clasifícalo en una de las tres clases del corpus (glosario §4; convenciones §2). La duda se resuelve siempre hacia la clase más débil: clasificar como `duro` lo que es `blando` crea reglas frágiles; clasificar como automatizable lo que exige juicio crea reglas infieles.*

Elige una clase:

- `duro` — regla booleana exacta sobre campos declarados. Dos evaluadores llegan siempre al mismo resultado. Es la clase preferente.
- `blando` — umbral + defensa en profundidad. La regla se evalúa mecánicamente pero conlleva un margen de error que se acota combinando controles. Documenta el umbral como parámetro de la ficha, no como constante oculta.
- `no-automatizable` — juicio fino que ninguna regla reproduce con fidelidad. No se traduce a decisión automática: su efecto es `require-prior-hop` hacia el punto de juicio, y la ficha existe para dejar constancia de que el principio se consideró y de por qué no se mecanizó.

Clase elegida y justificación: [Espacio para rellenar]

---

## 4. `disparador`

*Pregunta guía: ¿qué condición observable indica que este principio aplica a este salto? Constrúyela **solo** con campos declarados del descriptor de identidad y/o del bloque de contexto cultural, nunca con inferencias sobre el transporte ni la red. Para un principio `duro` es una condición booleana; para uno `blando`, una comparación contra umbral más los controles de refuerzo; para uno `no-automatizable`, la condición que identifica cuándo escalar a juicio.*

- **Campos del descriptor de identidad que intervienen:** [Espacio para rellenar — p. ej. `capabilities[].canCommit`, `capabilities[].externalizes`, `capabilities[].sideEffectClass`, `capabilities[].dataClassesTouched`, `domain`]
- **Campos del bloque de contexto cultural que intervienen:** [Espacio para rellenar — p. ej. existencia/ausencia de un `DecisionHop` en `decisionChain`, `correlationId`, `businessCaseId`, `deidTokens`]
- **Condición que activa la policy:** [Espacio para rellenar]

---

## 5. `efecto`

*Pregunta guía: cuando el disparador se cumple, ¿cuál de los cuatro efectos normativos impone la policy? Debe ser uno y solo uno, consistente con la clase. Un efecto que «depende» o «recomienda» no es ejecutable.*

Elige uno:

- `allow` — la colaboración procede.
- `deny` — la colaboración se rechaza; el llamante recibe un rechazo trazable.
- `redact` — la colaboración procede, pero el resultado se devuelve con datos suprimidos o sustituidos por `deidTokens`.
- `require-prior-hop` — la colaboración exige que conste un `DecisionHop` previo (p. ej. una validación de otro dominio) antes de proceder. No es un `deny`: encarrila, no cierra la puerta.

Efecto elegido y descripción precisa de qué bloquea, transforma o exige: [Espacio para rellenar]

---

## 6. `evidenciaRequerida`

*Pregunta guía: ¿qué rastro auditable deja la evaluación? Toda decisión deja evidencia, anclada al `DecisionHop` del salto (campos `criteriaApplied` y `outcome`), incluso cuando el efecto es `allow`: que algo se permitió debe constar igual que que algo se denegó (convenciones §3, paso 4). Sin evidencia, una regla no satisface [CF-05](../../docs/federation/criterios-funcionales.md).*

[Espacio para rellenar]

---

## 7. `puntoDeAplicacion`

*Pregunta guía: ¿en qué momento del ciclo de la llamada se evalúa? Decláralo explícitamente; nunca se deja implícito (convenciones §3, paso 5).*

Elige uno (o ambos, si el principio genera reglas en los dos):

- `pre-invocación` — antes de que el agente llamado ejecute. Aquí se deciden `allow`, `deny` y `require-prior-hop`.
- `post-resultado` — antes de devolver el resultado al llamante. Aquí se decide `redact`.

Punto de aplicación y dónde se evalúa (rol arquitectónico: gateway antes de enrutar, agente receptor…), expresado sin nombrar producto: [Espacio para rellenar]

---

## 8. `reversibilidad`

*Pregunta guía: si la policy aplica un efecto y luego resulta improcedente, ¿se puede deshacer? Un `redact` con `deidToken` recuperable dentro de su `ttl` es reversible; un `redact` irreversible destruye el original; un `deny` que solo bloquea es reversible. Declararlo informa la gestión de excepciones.*

- **Reversibilidad:** *(reversible / irreversible / parcial)* — [Espacio para rellenar]
- **Cómo se revierte (o por qué no se puede):** [Espacio para rellenar]

---

## 9. `caveats`

*Pregunta guía: ¿qué sabe quien diseñó esta policy que los campos anteriores no capturan? Supuestos, interacciones con otras fichas, casos límite, falsos positivos conocidos, granularidad de las autorizaciones que exige. Incluye obligatoriamente el **comportamiento ante el fallo**: si falta un campo del disparador o la regla no se puede evaluar, el resultado por defecto es `deny` con evidencia, nunca `allow` en silencio ([CF-06](../../docs/federation/criterios-funcionales.md); convenciones §3, paso 6).*

[Espacio para rellenar]

---

## 10. `testVectors`

*Pregunta guía: ¿con qué pares entrada→efecto esperado se demuestra que cualquier implementación (en cualquier dialecto) mantiene la fidelidad de la regla? Son el contrato observable de la policy. Incluye al menos un caso que dispare la policy, uno que no, y el caso de degradación segura (campo ausente → `deny`).*

| # | Entrada (campos relevantes del corpus) | Efecto esperado |
|---|---|---|
| TV-1 | [Espacio para rellenar] | [Espacio para rellenar] |
| TV-2 | [Espacio para rellenar] | [Espacio para rellenar] |
| TV-3 | [Espacio para rellenar — caso de degradación segura] | [Espacio para rellenar] |

---

## 11. `refImplementaciones[]`

*Pregunta guía: ¿dónde están las serializaciones por dialecto de esta policy? El cuerpo nunca contiene el dialecto; solo lo referencia. Lista aquí los punteros al catálogo del apéndice, uno por ficha de dialecto. Si la ficha aún no existe, déjalo anotado como pendiente.*

- [Espacio para rellenar — p. ej. `../../docs/federation/appendix/policy-templates/<id>.md`]
- [Espacio para rellenar]

---

*Plantilla de ficha de policy de Myrmion Federation — versión 1.0. Parte del corpus normativo. El formato lo fijan las [convenciones de mapping](../../docs/federation/convenciones-mapping-constitucion-policy.md); el catálogo poblado con dialectos vive en [`appendix/policy-templates/`](../../docs/federation/appendix/policy-templates/), nunca en esta ficha. Ver también el [glosario](../../docs/federation/glosario-federacion.md), el [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md), el [esquema del bloque de contexto cultural](../../docs/federation/esquema-bloque-contexto-cultural.md) y el [ejemplo rellenado](./ficha-policy-template-ejemplo.md).*
