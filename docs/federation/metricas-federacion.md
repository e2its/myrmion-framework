# Myrmion Federation — Métricas de la federación

**Versión 1.0**

*Materializa el §7 del [manifiesto](./manifesto.md) — «Cómo saber si funciona». Convierte las seis métricas en fichas operables: las cuatro heredadas de Adoption (reconocibilidad, coherencia transversal, tasa de escalado adecuada, trazabilidad de criterio) y las dos propias de Federation (reducción de fricción en handovers, tasa de bloqueo y excepción). Para cada una: definición, de qué campo del bloque o del log sale el dato, qué señala un valor sano frente a uno insano, con qué cadencia se mide y cómo establecer la baseline pre-federación.*

---

## Cómo usar este documento

El manifiesto declara seis métricas pero no las hace medibles. Este documento lo hace. Cada métrica es una ficha con la misma estructura, de modo que el equipo de plataforma (el [cuarto custodio](./gobernanza-federada.md)) pueda instrumentarlas sobre la observabilidad del stack sin tener que reinterpretar el manifiesto.

Hay una idea que recorre todo el documento y conviene enunciarla antes: **en Federation las métricas no se construyen con instrumentación nueva, se construyen con la que ya existe por construcción.** El [bloque de contexto cultural](./esquema-bloque-contexto-cultural.md) viaja en cada llamada y el stack lo exporta como atributos del span ([CF-05](./criterios-funcionales.md)). El [registro de excepciones](../../templates/federation/registro-excepciones.md) deja rastro de cada aprobación manual. El log de policy registra cada decisión `allow`/`deny`/`redact`/`require-prior-hop`. Medir, aquí, es consultar lo que el sistema ya emite — no añadir telemetría ad hoc.

De ahí se sigue la afirmación más fuerte del §7, que este documento desarrolla en la métrica M3: **la tasa de escalado adecuada, declarada métrica difícil en Adoption, aquí es trivial.** No porque el problema sea más fácil, sino porque cada escalado queda registrado con su contexto completo y se puede clasificar a posteriori. Esa es, literalmente, una de las razones para graduarse a Federation.

Las cuatro métricas heredadas conservan el nombre y la intención que tienen en Adoption (ver [manifiesto de Adoption](../adoption/manifesto.md) §7); lo que cambia es que aquí se pueden medir con rigor que antes no era posible. Las dos propias son técnicas y nacen con Federation.

### Convenciones de las fichas

Cada ficha tiene seis campos:

- **Definición.** Qué mide, en una frase operable.
- **Fuente de datos.** De qué campo del [bloque de contexto cultural](./esquema-bloque-contexto-cultural.md), del [descriptor de identidad](./esquema-identidad-agente.md), del log de policy o del [registro de excepciones](../../templates/federation/registro-excepciones.md) sale el dato. Toda fuente es una consulta sobre lo que [CF-05](./criterios-funcionales.md) ya exporta; ninguna requiere instrumentación nueva.
- **Señal.** Qué indica un valor sano y qué indica uno insano. La métrica no es el objetivo: la señal es lo que se vigila.
- **Cadencia.** Con qué frecuencia se calcula. La regla general: cuanto más crítico el dominio, más frecuente.
- **Baseline pre-federación.** Cómo se fija el valor de partida *antes* de federar, porque sin baseline una métrica de mejora no significa nada.
- **Notas.** Trampas de interpretación y enganches con otros documentos del corpus.

> **Las métricas no son objetivos.** Ninguna de estas seis tiene un valor «correcto» universal. El rango sano depende del dominio, de la exposición regulatoria y del volumen de tráfico inter-agente. Fijar un objetivo numérico transversal («bloqueo < 2 %») es el error clásico: convierte una señal en una meta y la meta deja de medir lo que medía. Lo que se vigila es la *tendencia* y la *descomposición*, no el valor absoluto.

---

## Tabla resumen

| ID | Métrica | Origen | Materializa | Fuente principal |
|---|---|---|---|---|
| **M1** | Reconocibilidad | Heredada de Adoption | §7 | `criteriaApplied`, outputs cuestionados |
| **M2** | Coherencia transversal | Heredada de Adoption | §3.4 (Patrón C), §7 | Coherencia entre agentes |
| **M3** | Tasa de escalado adecuada | Heredada de Adoption | §3.2, §7 | Escalados registrados en la cadena de decisión |
| **M4** | Trazabilidad de criterio | Heredada de Adoption | §3.4 (Patrón A), §7 | `correlationId` + cadena de decisión |
| **M5** | Reducción de fricción en handovers | Propia de Federation | §7 | Tiempo de resolución por `businessCaseId` |
| **M6** | Tasa de bloqueo y excepción | Propia de Federation | §3.4 (Patrón B), §7 | Log de policy + registro de excepciones |

Las cuatro heredadas comparten una propiedad nueva: **en Federation se miden sobre datos, no sobre muestreo manual.** En Adoption se evaluaban revisando outputs a mano; aquí salen del log de cadenas y del bloque de contexto que viaja en cada llamada.

---

# Métricas heredadas de Adoption

## M1 — Reconocibilidad

**Definición.** Hasta qué punto una persona del dominio reconocería el output de un agente como «hecho según nuestra cultura» — no genérico, no de proveedor, sino de la organización. Es la métrica madre de Adoption: si los outputs no se reconocen como propios, el modelado cultural no ha calado.

**Fuente de datos.** En Adoption es revisión humana de muestras. En Federation se ancla además a dos señales objetivas:
- El campo `criteriaApplied` de cada *DecisionHop* en la cadena de decisión (ver [esquema del bloque](./esquema-bloque-contexto-cultural.md)): un eslabón cuyo `criteriaApplied` está vacío o es solo `"juicio-de-modelo-no-automatizable"` en un dominio donde la Constitución exige criterios concretos es candidato a output no reconocible.
- La proporción de outputs marcados como cuestionados (internamente, externamente o por reguladores) sobre el total de cadenas cerradas — la misma señal que alimenta el Patrón A de drift.

La evaluación cualitativa por una persona del dominio sigue siendo necesaria: la reconocibilidad tiene un componente de juicio que ningún campo captura. La instrumentación la *orienta* (qué cadenas revisar primero), no la sustituye.

**Señal.**
- *Sana:* la mayoría de los outputs revisados se reconocen como propios; la proporción de cuestionados es baja y estable; los eslabones aplican criterios coherentes con su dominio.
- *Insana:* sube la proporción de outputs que el dominio no reconoce como suyos; aparecen cadenas con `criteriaApplied` sistemáticamente vacío; los outputs «suenan a proveedor» o a otro departamento.

**Cadencia.** Trimestral por defecto; mensual en dominios de criticidad alta. Coincide con la revisión de coherencia de la [gobernanza federada](./gobernanza-federada.md).

**Baseline pre-federación.** Antes de federar, tomar una muestra de outputs del asistente departamental tal como opera dentro de su producto comercial (la etapa de Adoption) y evaluarla con el panel del dominio. Esa puntuación es la baseline: Federation no debe degradarla. Si la reconocibilidad cae al federar, lo más probable es que la propagación de contexto cultural esté perdiendo criterios en algún salto — revisar `criteriaApplied` a lo largo de la cadena.

**Notas.** Reconocibilidad y coherencia transversal (M2) son distintas: una organización puede tener agentes individualmente reconocibles que, juntos, se contradicen. M1 mira cada agente; M2 mira el sistema.

---

## M2 — Coherencia transversal

**Definición.** Que dos agentes de dominios distintos, ante el mismo asunto, apliquen criterios compatibles en lugar de contradecirse. Es la propiedad que distingue una falange de un grupo de individuos competentes pero descoordinados.

**Fuente de datos.** El **Patrón C** de detección de drift (ver [patrones de detección de drift](./patrones-deteccion-drift.md)): presentar periódicamente el mismo escenario hipotético a varios agentes departamentales y comparar respuestas. En Federation esto es ejecutable porque cada agente es un servicio invocable con identidad propia ([CF-04](./criterios-funcionales.md)); no hace falta reunir a las personas. Las incompatibilidades sistemáticas señalan drift en una capa departamental o en la propia Constitución.

Señal complementaria del tráfico real: cadenas donde un eslabón revierte o contradice el `criteriaApplied` de un eslabón anterior dentro de la misma cadena (`correlationId`), sin que medie un cambio de versión de Constitución que lo justifique.

**Señal.**
- *Sana:* ante el escenario de prueba, los agentes dan respuestas compatibles; las divergencias son explicables por la especialización de cada dominio, no por aplicar criterios contradictorios.
- *Insana:* las incompatibilidades se repiten ante el mismo tipo de escenario; en el tráfico real, eslabones que se contradicen entre sí dentro de una cadena. Cualquiera de las dos cosas es drift que hay que atribuir: o una capa departamental se ha desviado, o la Constitución no se ha propagado bien.

**Cadencia.** Semestral en la batería completa de escenarios; el muestreo de contradicciones intra-cadena es continuo (se calcula sobre el log, sin coste de panel).

**Baseline pre-federación.** En Adoption la coherencia transversal se evaluaba en lectura cruzada manual entre departamentos. Tomar esa evaluación cruzada como baseline cualitativa. Para la parte cuantitativa, registrar la batería de escenarios de prueba *antes* de federar y pasarla a los asistentes en su forma pre-federación; las respuestas de partida son el punto de comparación.

**Notas.** M2 es la lectura «de federación» del mismo fenómeno que el [gate de coherencia](./gobernanza-federada.md) verifica en el alta de cada agente. El gate previene la incoherencia en el registro; M2 la detecta en operación.

---

## M3 — Tasa de escalado adecuada

**Definición.** De todos los escalados a humano que ocurren, qué proporción eran *apropiados* — es decir, casos que efectivamente requerían juicio humano — frente a los que fueron escalados que el sistema podría y debería haber resuelto, o que escalaron por una causa equivocada. No mide cuánto se escala, sino si se escala *bien*.

**Fuente de datos.** Los escalados quedan registrados con su contexto completo. Las dos rutas que los producen son:
1. **Escalado por incompatibilidad de Constitución** (manifiesto §3.2): cuando la *validación de compatibilidad* falla — el `constitutionHash` del emisor no está entre los `compatibleConstitutionHashes` del receptor — la política por defecto es escalado a humano con el bloque de contexto completo como evidencia. Cada uno de estos escalados lleva adjunto el bloque que lo motivó.
2. **Escalado derivado de policy** (`require-prior-hop` no satisfecho, o `deny` con ruta de aprobación): queda en el log de policy y, si se aprueba, en el [registro de excepciones](../../templates/federation/registro-excepciones.md).

Para clasificar cada escalado como adecuado o no, se revisa el bloque de contexto adjunto: qué versión de Constitución aplicó cada lado, qué caso de negocio (`businessCaseId`), qué cadena de decisión previa. Toda esa información viaja *con* el escalado.

**Señal.**
- *Sana:* la mayoría de los escalados, al revisarlos, resultan apropiados; los inadecuados son raros y no forman patrón.
- *Insana:* alta proporción de escalados que no requerían humano (síntoma de policies demasiado tímidas o de versiones de Constitución desincronizadas que disparan incompatibilidades espurias); o escalados que *deberían* haber ocurrido y no ocurrieron (detectables como outputs cuestionados que nunca pasaron por humano — cruce con M1 y el Patrón A).

**Cadencia.** Mensual. Es barata de calcular porque el dato ya está; lo único que cuesta es la clasificación adecuado/inadecuado, que es muestreable.

**Baseline pre-federación.** **Aquí está la diferencia que justifica la métrica.** En Adoption esta métrica se declaró *difícil* precisamente porque el escalado lo hacía una persona en su flujo de trabajo y rara vez quedaba registrado con contexto suficiente para evaluarlo después: reconstruir si un escalado manual fue apropiado exigía trabajo forense. La baseline pre-federación, por tanto, suele ser una estimación pobre — y eso es esperable.

En Federation la métrica deja de ser difícil: **cada escalado queda registrado con su contexto completo (el bloque de contexto cultural que lo motivó), y se puede analizar cuántos eran apropiados y cuántos no.** No es que el problema se simplifique; es que el dato pasa a existir. Esta es, literalmente, una de las pruebas de que graduarse a Federation aporta valor: una métrica que en Adoption solo se podía estimar, aquí se mide sobre evidencia adjunta.

**Notas.** No confundir M3 con M6 (tasa de bloqueo y excepción). M6 mide cuánto bloquea el policy engine y cuántas excepciones se aprueban; M3 mide si los escalados a humano fueron acertados. Un bloqueo puede resolverse sin escalar (la cadena toma otra ruta) y un escalado puede no venir de un bloqueo (incompatibilidad de Constitución). Se cruzan, pero no son la misma métrica.

---

## M4 — Trazabilidad de criterio

**Definición.** La capacidad de reconstruir, para cualquier decisión asistida que cruzó dominios, qué criterios se aplicaron, en qué orden, por qué agente y con qué resultado. Es la métrica que ataca directamente el tercer síntoma del manifiesto (§1): la trazabilidad que se rompía en la frontera entre dominios.

**Fuente de datos.** La cadena de decisión completa, reconstruida desde el `correlationId` ([CF-05](./criterios-funcionales.md) garantiza que se traza la cadena entera correlacionada por ese identificador). Cada *DecisionHop* aporta su agente, la tool invocada, la versión de Constitución aplicada, el `criteriaApplied` (como `policyId@version` cuando es policy, o `"juicio-de-modelo-no-automatizable"` cuando es juicio fino) y el resultado. La trazabilidad no es algo que haya que *medir* aparte: es una propiedad que el bloque garantiza por construcción cuando `hopCount > 1`.

Lo que sí se mide es la **completitud** de la trazabilidad: proporción de cadenas cerradas en las que la cadena de decisión está íntegra (sin eslabones huérfanos, sin `correlationId` roto entre saltos, sin `criteriaApplied` ausente donde la cultura lo exige).

**Señal.**
- *Sana:* prácticamente toda cadena multi-salto se reconstruye completa desde su `correlationId`; ante una decisión cuestionada, la reconstrucción es inmediata, no forense.
- *Insana:* aparecen cadenas con saltos cuyo `correlationId` no enlaza (síntoma de que algún agente regenera el identificador en lugar de propagarlo — error grave: el `correlationId` **nunca** se regenera dentro de una cadena); eslabones sin `criteriaApplied`; cadenas que no se pueden cerrar.

**Cadencia.** Continua: la completitud se calcula sobre el log en tiempo real o casi. Revisión agregada mensual.

**Baseline pre-federación.** La baseline es trivial de enunciar y elocuente: **en Adoption la trazabilidad transversal es esencialmente cero** — reconstruir qué criterios se aplicaron al cruzar dominios requería trabajo forense que ningún producto comercial soportaba (manifiesto §1). El punto de partida no es «baja»: es la ausencia de trazabilidad. Por eso M4 es de las métricas donde la mejora de Federation es más visible y más fácil de defender ante quien financia la inversión.

**Notas.** M4 es la condición de posibilidad del **Patrón A** de detección de drift ([patrones de detección de drift](./patrones-deteccion-drift.md)): sin cadenas íntegras no hay análisis de cadenas cuestionadas. Si M4 se degrada, el Patrón A deja de ser fiable antes de que nadie lo note. Por eso conviene vigilar la completitud de M4 como guardián del resto del sistema de drift.

---

# Métricas propias de Federation

## M5 — Reducción de fricción en handovers

**Definición.** Cuánto se ha reducido el tiempo humano de bisagra que antes consumía cada *handover* entre dominios. La métrica concreta es el **tiempo medio de resolución de casos que cruzan más de un dominio**, comparado contra una baseline pre-federación. Es la métrica que justifica económicamente la inversión: si no baja de forma observable, Federation no se justifica.

**Fuente de datos.** El `businessCaseId` agrupa todas las cadenas de decisión que sirven a un mismo asunto (el lead, el expediente, el ticket). El tiempo de resolución de un caso multi-dominio es el intervalo entre el primer salto (`hopCount = 1`) de la primera cadena del caso y el cierre de la última — todo reconstruible desde `businessCaseId` y los timestamps de los spans ([CF-05](./criterios-funcionales.md)). Descomponer por par de dominios (corredor) para ver dónde está la fricción residual.

**Señal.**
- *Sana:* el tiempo medio de resolución de casos multi-dominio baja de forma sostenida tras migrar cada corredor; la curva se estabiliza en un nuevo régimen por debajo de la baseline.
- *Insana:* el tiempo no baja, o baja y vuelve a subir. Causas típicas: demasiados escalados (cruce con M3), demasiados bloqueos que obligan a rutas alternativas (cruce con M6), o un corredor mal modelado que reintroduce trabajo humano de bisagra que se suponía eliminado.

**Cadencia.** Mensual, descompuesta por corredor. La comparación significativa es por corredor migrado, no agregada: federar un corredor más mete casos nuevos en el promedio y puede enmascarar la mejora de los ya migrados.

**Baseline pre-federación.** **Crítica e irrecuperable a posteriori: hay que medirla antes.** Mientras los handovers son manuales, instrumentar el tiempo que consume la bisagra humana para los corredores candidatos — el intervalo entre que un dominio entrega su output y el siguiente lo retoma como input contextualizado. Bastan unas semanas de muestreo sobre los dos o tres pares que más colaboran (los candidatos naturales al primer corredor, manifiesto §6 Fase 3). Si no se mide antes de federar, la baseline se pierde y M5 queda sin término de comparación — y entonces la pregunta «¿mereció la pena?» no tiene respuesta defendible.

**Notas.** M5 es la métrica que conecta Federation con el problema del manifiesto §1 (los handovers consumen más tiempo del que ahorra la IA). Es también la que mejor traduce a lenguaje de negocio para justificar la graduación desde Adoption. El `businessCaseId` existe en el bloque precisamente para hacerla calculable.

---

## M6 — Tasa de bloqueo y excepción

**Definición.** Dos cantidades acopladas que se vigilan juntas:
- **Tasa de bloqueo:** proporción de llamadas inter-agente que el policy engine bloquea (`deny`, o `require-prior-hop` no satisfecho) sobre el total de llamadas.
- **Tasa de excepción:** proporción de esos bloqueos que la organización aprueba manualmente como excepción.

Ambas, descompuestas por agente origen, agente destino y policy violada, son información operativa de primer orden.

**Fuente de datos.** El log de policy (cada decisión `allow`/`deny`/`redact`/`require-prior-hop`, con qué `policyId@version` la produjo) y el [registro de excepciones](../../templates/federation/registro-excepciones.md), donde cada excepción aprobada deja justificación, alcance temporal y autorizador. La descomposición por origen/destino sale del bloque de contexto; la descomposición por policy, del log.

**Señal.** El rango sano depende del dominio, pero las dos colas son patológicas:
- *Tasa de bloqueo muy baja:* las policies son demasiado permisivas o la cultura no se está aplicando — el policy engine no está haciendo cumplir nada.
- *Tasa de bloqueo muy alta:* las policies son demasiado estrictas; van a generar excepciones manuales sistemáticas que socavan el sistema (cada excepción es trabajo humano y erosión de la regla).
- *Tasa de excepción que crece sobre una policy concreta:* la señal más importante. Si las excepciones a la misma policy se acumulan, no es la realidad la que está mal: o la policy ha quedado desfasada respecto a la cultura real, o la cultura real ha drifteado respecto a la Constitución declarada. **Cuál de las dos es responsabilidad de la custodia decidir** — pero el dato la obliga a mirar.

**Cadencia.** Continua para la tasa de bloqueo (es un agregado del log). Revisión de excepciones acumuladas al menos mensual; más frecuente en dominios críticos.

**Baseline pre-federación.** No hay baseline pre-federación posible y es importante decirlo: **el policy engine no existe antes de Federation**, luego no hay bloqueos que medir. La baseline de M6 se establece *durante* las primeras semanas en producción del primer corredor (manifiesto §6 Fase 3), cuando emergen latencia, errores y casos límite. Esas primeras semanas fijan el régimen «normal» de bloqueo de la organización contra el que se interpretarán las desviaciones futuras. Conviene no tocar las policies durante ese periodo de calibración salvo error claro, para no contaminar la baseline.

**Notas.** M6 es la fuente directa del **Patrón B** de detección de drift ([patrones de detección de drift](./patrones-deteccion-drift.md)): el análisis de excepciones acumuladas. Una excepción al **Marco Regulatorio no es una excepción: es una alerta** (el Marco no admite excepciones — ver [glosario](./glosario-federacion.md) y Adoption §4); si aparece, no cuenta en esta métrica, escala como incidente. M6 y M3 se rozan pero no coinciden: M6 mide el comportamiento del policy engine; M3 mide el acierto de los escalados a humano.

---

## Cómo encajan las seis: el sistema de medición

Las seis métricas no son independientes; forman un sistema que se sostiene sobre los mismos cimientos que el resto del corpus:

- **Todo sale del bloque y del log.** `correlationId` reconstruye cadenas (M4), `businessCaseId` agrupa casos (M5), `criteriaApplied` documenta criterios (M1, M4), `constitutionHash`/`compatibleConstitutionHashes` motivan escalados por incompatibilidad (M3), el log de policy alimenta el bloqueo (M6). El [esquema del bloque](./esquema-bloque-contexto-cultural.md) se diseñó para que estas métricas fueran calculables sin instrumentación adicional.
- **Tres de ellas son la cara «métrica» de los tres patrones de drift.** M4 habilita el Patrón A, M2 *es* el Patrón C en operación, M6 alimenta el Patrón B. Las métricas miden el estado; los [patrones de drift](./patrones-deteccion-drift.md) investigan la causa cuando una métrica se desvía. No se solapan: se relevan.
- **El rigor es la diferencia con Adoption.** Las cuatro heredadas ya importaban en Adoption; lo que Federation aporta no es la métrica sino la *capacidad de medirla sobre datos*. M3 es el caso extremo: difícil en Adoption, trivial aquí, porque el escalado deja de ser un acto humano no registrado para ser un evento con contexto completo adjunto.

Quien instrumenta estas métricas es la [plataforma de federación](./gobernanza-federada.md) (el cuarto custodio). El cuadro de mando que las presenta lo aporta el stack: Federation articula *qué* medir, *de dónde* sale el dato y *qué señala* cada valor — el dashboard que lo dibuja es responsabilidad de la observabilidad del stack ([CF-05](./criterios-funcionales.md)), no del framework.

---

*Métricas de la federación de Myrmion Federation — versión 1.0. Parte del corpus normativo.*

**Documentos relacionados.**
- [Manifiesto de Federation](./manifesto.md) — §7 «Cómo saber si funciona», que estas fichas materializan.
- [Patrones de detección de drift](./patrones-deteccion-drift.md) — la cara «investigación de causa» de M2, M4 y M6.
- [Esquema del bloque de contexto cultural](./esquema-bloque-contexto-cultural.md) — los campos (`correlationId`, `businessCaseId`, `criteriaApplied`, `constitutionHash`…) que son la fuente de datos de casi todas las métricas.
- [Criterios funcionales](./criterios-funcionales.md) — CF-05 (observabilidad agent-aware), del que depende toda la medición.
- [Gobernanza federada](./gobernanza-federada.md) — la plataforma de federación como custodio que instrumenta y vigila estas métricas.
- [Registro de excepciones](../../templates/federation/registro-excepciones.md) — fuente de la tasa de excepción (M6).
- [Glosario](./glosario-federacion.md) — vocabulario normativo de todos los términos en cursiva.
