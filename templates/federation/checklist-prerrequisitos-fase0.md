<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Checklist de Prerrequisitos (Fase 0)

**Versión 1.0**

*Plantilla de autoevaluación Listo / No-listo de la **Fase 0** del [manifiesto](../../docs/federation/manifesto.md) §6 — la verificación de prerrequisitos. Es la **puerta de entrada** a Federation: si no se cumple, la respuesta no es «empieza más despacio», es «sigue en [Adoption](../../docs/adoption/manifesto.md) hasta que se cumpla».*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

Federation no es la siguiente versión de Adoption: es la fase del ecosistema que se activa cuando el modelado cultural ya está hecho y la fricción de los handovers manuales empieza a costar más que la propia adopción (manifiesto «De la colonia a la falange»). La Fase 0 existe para responder a una sola pregunta, **antes** de gastar un euro en stack: *¿esta organización tiene de verdad el problema que Federation resuelve, o tiene un problema de Adoption disfrazado?*

Esta plantilla convierte los cinco prerrequisitos del manifiesto §6 en **criterios verificables con evidencia**. No es un cuestionario de madurez subjetiva: cada criterio se marca Listo solo si existe un artefacto o un dato que lo respalda. Reglas para usarla:

- **Quién la rellena.** El patrocinador de Federation — típicamente el custodio de la Constitución Corporativa, que es quien plantea graduar la organización de Adoption a Federation — con el equipo de plataforma o SRE candidato a [cuarto custodio](../../docs/federation/gobernanza-federada.md). El primero responde de los prerrequisitos culturales (C1–C3); el segundo, de la lectura honesta de la fricción (C4) y del volumen (C5).
- **Es un gate, no un termómetro.** El veredicto es binario: **Listo** (se cumplen los cinco criterios) o **No-listo** (falta al menos uno). No hay «listo al 80 %». Federar con un prerrequisito sin cumplir no acelera nada: produce, en palabras del manifiesto §8, «un sistema más rápido en hacer mal lo que ya hacía mal antes».
- **No-listo no es un suspenso.** Es un diagnóstico con destino: cada criterio no cumplido apunta a un trabajo concreto de Adoption. Quedarse en Adoption hasta cerrarlo es la decisión correcta, no la conservadora.
- **La evidencia manda sobre la opinión.** Donde la plantilla pide «evidencia», pon el enlace al artefacto (la Constitución versionada, el repositorio de gobernanza, el dato de fricción medido), no una afirmación. Un criterio sin evidencia se marca como No cumplido por defecto.
- Marca con `[Espacio para rellenar]` lo que aún no sepas; vuelve a ello. Cuando quieras, elimina esta sección de ayuda.

> **Regla destacada — el coste de saltarse la Fase 0 lo paga la federación entera.** Federation se monta sobre la Constitución Corporativa: la propaga en cada llamada, la traduce a policy, mide el drift contra ella. Si la Constitución no es estable, o si la gobernanza de las tres capas no existe, no hay nada sólido sobre lo que montar la maquinaria. La Fase 0 no es burocracia previa: es la comprobación de que los cimientos aguantan el peso. Saltársela no adelanta la federación; adelanta su colapso.

---

## 0. Metadatos del documento

*Pregunta guía: ¿quién hace esta autoevaluación, sobre qué organización y en qué fecha? (Esta sección queda EXCLUIDA del cálculo del hash canónico, igual que en el resto del corpus.)*

| Campo | Valor |
|---|---|
| Organización | [Espacio para rellenar] |
| Versión del documento | [Espacio para rellenar — p. ej. 1.0] |
| Fecha de la autoevaluación | [Espacio para rellenar — `AAAA-MM-DD`] |
| Responsable de la evaluación (patrocinador de Federation) | [Espacio para rellenar — típicamente el custodio de la Constitución] |
| Plataforma candidata (4.º custodio) consultada | [Espacio para rellenar — equipo de plataforma o SRE] |
| Versión de la Constitución Corporativa vigente | [Espacio para rellenar — p. ej. 1.0, fecha de aprobación] |
| Versión del Marco Regulatorio vigente | [Espacio para rellenar — p. ej. 1.0, fecha de aprobación] |
| Veredicto (ver §7) | [Espacio para rellenar — `Listo` \| `No-listo`] |
| Próxima reevaluación (si No-listo) | [Espacio para rellenar — `AAAA-MM-DD`] |

---

## 1. Antes de empezar: qué estás verificando

*Pregunta guía: ¿tienes claro que esto es un gate de entrada y no una hoja de ruta? Federation tiene sentido cuando la cultura ya está articulada y gobernada, y cuando la fricción de los handovers manuales ya duele de forma medible. Los cinco criterios de las secciones siguientes son los cinco prerrequisitos del manifiesto §6, ni uno más ni uno menos. Si los cinco se cumplen con evidencia, la organización está Lista para la Fase 1 (selección de stack y prueba de concepto). Si falta uno, la organización sigue en Adoption — y este documento te dice exactamente en qué trabajar para volver a evaluar.*

[Espacio para rellenar — resume en una o dos frases por qué tu organización se plantea Federation ahora, y qué handover concreto está costando más de lo que ahorra]

---

## 2. Criterio C1 — Capas departamentales vivas en producción

*Pregunta guía: ¿hay al menos **tres** capas departamentales modeladas, aprobadas y en uso real en producción (no en piloto, no en cajón)? Federation federa agentes departamentales, y un agente departamental es la materialización programática de una [Capa Departamental](../../docs/adoption/manifesto.md) de Adoption. Sin al menos tres capas vivas no hay con qué construir una federación que valga la pena: con dos, los patrones manuales de Adoption §5 siguen siendo suficientes. «Viva en producción» significa que personas reales la usan a diario y que tiene custodio asignado — no que exista el documento.*

**Umbral del manifiesto §6:** al menos **3** capas departamentales vivas en producción.

| Sub-comprobación | Cumple | Evidencia |
|---|:---:|---|
| Hay 3 o más capas departamentales **aprobadas y versionadas** | [ ] | [Espacio para rellenar — enlace a cada capa en el repositorio de gobernanza] |
| Cada una está **en uso real en producción** (personas la usan a diario) | [ ] | [Espacio para rellenar] |
| Cada una tiene **custodio asignado** y vivo | [ ] | [Espacio para rellenar] |

*Inventario de capas (lista las que cuentan para el umbral):*

| Capa departamental | Custodio | ¿En producción desde? (`AAAA-MM`) | Evidencia de uso |
|---|---|---|---|
| [Espacio para rellenar — p. ej. Comercial] | | | |
| [Espacio para rellenar — p. ej. Legal y Compliance] | | | |
| [Espacio para rellenar] | | | |

**Veredicto C1:** [Espacio para rellenar — `Cumple` \| `No cumple`]

*Si No cumple → trabajo de Adoption: modelar y poner en producción las capas que falten usando la [plantilla de capa departamental](../adoption/capa-departamental.md). Volver a evaluar cuando haya 3 vivas.*

---

## 3. Criterio C2 — Constitución Corporativa estable

*Pregunta guía: ¿la Constitución Corporativa lleva **al menos seis meses** estable, sin reescrituras de fondo? La Constitución es lo que Federation propaga en cada llamada, traduce a policy y usa como referencia para medir drift. Si todavía está cambiando de fondo cada pocas semanas, cada cambio invalidaría las policies derivadas y rompería la [validación de compatibilidad](../../docs/federation/glosario-federacion.md) entre agentes (manifiesto §3.2). «Estable» no significa congelada: admite ajustes menores versionados. Significa que su núcleo — identidad, voz, principios, restricciones — no se ha rehecho en seis meses.*

**Umbral del manifiesto §6:** Constitución Corporativa **estable ≥ 6 meses**.

| Sub-comprobación | Cumple | Evidencia |
|---|:---:|---|
| La Constitución está **aprobada y versionada** | [ ] | [Espacio para rellenar — enlace y versión] |
| Su núcleo **no se ha reescrito en los últimos 6 meses** (solo ajustes menores versionados) | [ ] | [Espacio para rellenar — historial de versiones / fechas] |
| Sus principios están articulados con el detalle suficiente para **derivar policy** de los automatizables (manifiesto §3.3) | [ ] | [Espacio para rellenar] |

*Pregunta guía adicional: ¿cuándo se aprobó la versión vigente y qué cambió desde entonces? Un historial de «1.0 hace ocho meses, 1.1 hace dos meses con un retoque de tono» es estabilidad sana. Un historial de «2.0 el mes pasado tras rehacer los principios» reinicia el reloj de los seis meses.*

[Espacio para rellenar — resumen del historial de versiones de la Constitución]

**Veredicto C2:** [Espacio para rellenar — `Cumple` \| `No cumple`]

*Si No cumple → trabajo de Adoption: dejar sedimentar la Constitución. Si se acaba de reescribir, el reloj de los seis meses empieza ahora. La estabilidad no se acelera federando.*

---

## 4. Criterio C3 — Gobernanza formal de las tres capas

*Pregunta guía: ¿existe gobernanza **formal y operante** de las tres capas de Adoption — Marco Regulatorio, Constitución Corporativa y capas departamentales? No basta con que los documentos existan: tiene que haber custodia diferenciada por capa, revisión de coherencia antes de producción, y gestión de excepciones que deje rastro. Federation añade un cuarto custodio (la plataforma de federación), pero **da por supuesta** la gobernanza de los tres primeros: la verificación de coherencia programática y el [gate de coherencia](../../docs/federation/gobernanza-federada.md) son la versión programática de procesos que ya deben existir manualmente. Si no existen, Federation no tiene qué automatizar.*

**Umbral del manifiesto §6:** **gobernanza formal de las tres capas** (Marco, Constitución, capas departamentales), con la custodia diferenciada de Adoption §4.

| Sub-comprobación | Cumple | Evidencia |
|---|:---:|---|
| **Marco Regulatorio** con custodio asignado (típicamente legal/DPO) | [ ] | [Espacio para rellenar] |
| **Constitución Corporativa** con custodio asignado (típicamente transformación digital) | [ ] | [Espacio para rellenar] |
| **Cada capa departamental** con su custodio en el departamento | [ ] | [Espacio para rellenar] |
| Existe **revisión de coherencia** documentada antes de subir a producción | [ ] | [Espacio para rellenar] |
| Existe **gestión de excepciones** que deja rastro (manualmente, hoy) | [ ] | [Espacio para rellenar] |

**Veredicto C3:** [Espacio para rellenar — `Cumple` \| `No cumple`]

*Si No cumple → trabajo de Adoption: instituir la custodia y los procesos de gobernanza de Adoption §4 antes de plantear el cuarto custodio. La maquinaria de Federation no sustituye a la gobernanza humana: la ejecuta más rápido. No hay nada que ejecutar si no existe primero.*

---

## 5. Criterio C4 — Fricción de handovers documentada que justifica la inversión

*Pregunta guía: ¿existe **evidencia documentada** de que los handovers manuales entre dominios cuestan más tiempo del que la IA ahorra, y de que ese coste justifica la inversión en stack y operación? Este es el criterio que separa «sería interesante federar» de «hay que federar». La [reducción de fricción en handovers](../../docs/federation/glosario-federacion.md) es la primera métrica técnica de Federation (manifiesto §7), y se mide contra una **baseline pre-federación**. La Fase 0 es el momento de capturar esa baseline: si no sabes cuánto cuesta hoy un handover, no podrás demostrar después que Federation lo redujo — ni justificar la inversión antes de hacerla.*

**Umbral del manifiesto §6:** **fricción de handovers documentada** que justifica la inversión.

| Sub-comprobación | Cumple | Evidencia |
|---|:---:|---|
| Identificado **el corredor que más fricción genera** (el par origen→destino candidato a piloto) | [ ] | [Espacio para rellenar — p. ej. comercial→legal] |
| **Cuantificada la fricción** de ese corredor (tiempo de bisagra humana por handover, frecuencia) | [ ] | [Espacio para rellenar — baseline pre-federación] |
| El coste agregado **justifica** la inversión en stack y operación (caso de negocio explícito) | [ ] | [Espacio para rellenar] |

*Pregunta guía adicional: ¿cuál es el handover que tu propio equipo describiría como «el cuello de botella»? Ese es tu corredor candidato a [corredor](../../docs/federation/glosario-federacion.md) piloto de la Fase 1. Descríbelo con un dato, no con una anécdota: «el dictamen legal que el comercial necesita interpretar tarda de media X horas en cruzar, Y veces por semana».*

[Espacio para rellenar — descripción del corredor de más fricción y su baseline medida]

**Veredicto C4:** [Espacio para rellenar — `Cumple` \| `No cumple`]

*Si No cumple → no es trabajo de modelado, es trabajo de medición: instrumenta y mide la fricción real de tus handovers durante unas semanas. Si al medir resulta que la fricción no justifica la inversión, la conclusión correcta es que Federation **todavía no** es para tu organización — y eso es un buen resultado, no un fracaso.*

---

## 6. Criterio C5 — Volumen suficiente (agentes y pares colaborantes)

*Pregunta guía: ¿hay al menos **cinco o seis** agentes departamentales activos y al menos **tres pares** que colaboran con frecuencia significativa (varias veces al día)? Federation tiene un umbral de volumen explícito (manifiesto §9): por debajo de él, la sobrecarga operativa de la federación — gestión de excepciones, revisión de drift, operación del stack — no se amortiza, y los patrones manuales de Adoption §5 siguen siendo la respuesta correcta. Este criterio protege a la organización de adoptar maquinaria pesada para un problema que aún no la necesita.*

**Umbral del manifiesto §6 y §9:** **≥ 5–6 agentes** departamentales activos y **≥ 3 pares** que colaboran con frecuencia significativa.

| Sub-comprobación | Cumple | Evidencia |
|---|:---:|---|
| Hay **5 o más** agentes departamentales activos (o capas listas para materializarse como tales) | [ ] | [Espacio para rellenar — recuento] |
| Hay **3 o más pares** origen→destino que colaboran **varias veces al día** | [ ] | [Espacio para rellenar — lista de pares y frecuencia] |

*Pares colaborantes (lista los que cuentan para el umbral):*

| Par (origen → destino) | Frecuencia de colaboración | ¿Hoy es handover manual? |
|---|---|---|
| [Espacio para rellenar — p. ej. comercial → legal] | [Espacio para rellenar — p. ej. varias veces al día] | [Espacio para rellenar — Sí / No] |
| [Espacio para rellenar] | | |
| [Espacio para rellenar] | | |

**Veredicto C5:** [Espacio para rellenar — `Cumple` \| `No cumple`]

*Si No cumple → no es un defecto a corregir: es una señal de que tu organización aún no ha alcanzado el volumen donde Federation se amortiza. Sigue en Adoption. El framework es honesto sobre esto (manifiesto §9): no es para todo el mundo, ni se vende como horizonte aspiracional para quien no llegará nunca al volumen que lo justifica.*

---

## 7. Veredicto

*Pregunta guía: ¿se cumplen los **cinco** criterios con evidencia? El veredicto es binario y no admite media tinta. Marca el resultado de cada criterio, calcula el veredicto global y, si es No-listo, declara el trabajo pendiente y la fecha de reevaluación. Si es Listo, declara el corredor candidato con el que arrancará la Fase 1.*

| Criterio | Resultado |
|---|:---:|
| **C1** — ≥ 3 capas departamentales vivas en producción | [Espacio para rellenar — `Cumple` \| `No cumple`] |
| **C2** — Constitución Corporativa estable ≥ 6 meses | [Espacio para rellenar] |
| **C3** — Gobernanza formal de las tres capas | [Espacio para rellenar] |
| **C4** — Fricción de handovers documentada que justifica la inversión | [Espacio para rellenar] |
| **C5** — ≥ 5–6 agentes y ≥ 3 pares que colaboran con frecuencia | [Espacio para rellenar] |

**Regla del veredicto.** **Listo** si y solo si los cinco criterios son `Cumple`. **No-listo** si al menos uno es `No cumple`. No hay grados intermedios: un prerrequisito sin cumplir es la diferencia entre montar la falange sobre cimientos y montarla sobre arena.

**Veredicto global:** [Espacio para rellenar — `Listo para Fase 1` \| `No-listo: sigue en Adoption`]

### 7.1 Si el veredicto es No-listo

*Pregunta guía: ¿qué criterios faltan y qué trabajo concreto de Adoption los cierra? Lista cada criterio no cumplido con su acción y su responsable. No-listo no es el final del camino: es saber exactamente dónde estás.*

| Criterio no cumplido | Trabajo de Adoption que lo cierra | Responsable | Fecha objetivo |
|---|---|---|---|
| [Espacio para rellenar] | | | |
| [Espacio para rellenar] | | | |

**Fecha de reevaluación de esta checklist:** [Espacio para rellenar — `AAAA-MM-DD`]

### 7.2 Si el veredicto es Listo

*Pregunta guía: ¿con qué corredor arranca la Fase 1 y quién encarnará el cuarto custodio? La organización Lista pasa a la Fase 1 (selección de stack y prueba de concepto, manifiesto §6). El corredor de más fricción identificado en C4 es el candidato natural a piloto. Declara aquí el corredor elegido y el equipo de plataforma que asumirá la plataforma de federación.*

| Decisión de transición | Valor |
|---|---|
| Corredor candidato a piloto (de C4) | [Espacio para rellenar — p. ej. comercial → legal] |
| Equipo candidato a 4.º custodio (plataforma de federación) | [Espacio para rellenar] |
| Siguiente artefacto a producir | [Espacio para rellenar — p. ej. [charter de la plataforma de federación](./charter-plataforma-federacion.md)] |

---

*Checklist de Prerrequisitos (Fase 0) — versión 1.0. Parte del corpus normativo.*

**Relacionado:**
- Manifiesto: `../../docs/federation/manifesto.md` — §6 (Fase 0, los cinco prerrequisitos), §8 («no es una alternativa a Adoption»), §9 (umbral de volumen).
- Guía de adopción por fases: `../../docs/federation/guia-adopcion-por-fases.md` — la Fase 0 es su puerta de entrada; un veredicto Listo habilita la Fase 1.
- Perfil de adopción de Federation: `../../docs/federation/perfil-adopcion-federacion.md` — donde se registran las variables de la organización una vez superada la Fase 0.
- Manifiesto de Adoption: `../../docs/adoption/manifesto.md` — el destino al que se vuelve cuando el veredicto es No-listo; define las tres capas y su gobernanza (§5).
- Plantilla de capa departamental (Adoption): `../adoption/capa-departamental.md` — para cerrar C1 cuando faltan capas vivas.
- Gobernanza federada: `../../docs/federation/gobernanza-federada.md` — el cuarto custodio que se constituye solo después de pasar la Fase 0.
- Criterios funcionales: `../../docs/federation/criterios-funcionales.md` — lo que se evalúa en la Fase 1, una vez la organización está Lista.
- Charter de la plataforma de federación (plantilla): `./charter-plataforma-federacion.md` — el primer artefacto de la transición a Fase 1.
- Glosario de la federación: `../../docs/federation/glosario-federacion.md` — definición canónica de *corredor*, *agente departamental* y *handover*.
- Ejemplo de extremo a extremo: `../../examples/federation/corredor-comercial-legal/` — el corredor comercial→legal que ilustra el candidato a piloto.
