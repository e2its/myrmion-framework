# Myrmion Federation — Perfil de Adopción

**Versión 1.0**

*El conjunto de variables que describen el contexto de una organización concreta y que modulan cómo se aplican los criterios funcionales, los esquemas y el método del corpus. Materializa la advertencia del [manifiesto](./manifesto.md) §4 y §9: las decisiones de stack y de operación «dependen del entorno de la organización». Este documento separa lo que es **variable de contexto** (se declara una vez y se revisa) de lo que son **decisiones cerradas** del framework (no se negocian). Es la contrapartida del aviso de [criterios-funcionales.md](./criterios-funcionales.md) —«solo seis»—: lo que no es CF y sí depende del contexto, vive aquí.*

---

## Cómo usar este documento

El manifiesto es deliberadamente honesto sobre que Federation no es para todo el mundo (§9) y sobre que el stack y la operación dependen del entorno (§4). Para que esa honestidad sea operable hace falta un sitio donde la organización **declare su contexto** y donde el corpus diga, para cada rasgo de contexto, **qué criterio funcional o qué documento revisar si tu valor difiere del default**.

Eso es el Perfil de Adopción. No es una checklist de prerrequisitos (eso es la [Fase 0](./guia-adopcion-por-fases.md) y su `templates/federation/checklist-prerrequisitos-fase0.md`): es una **declaración de las variables que cambian la respuesta** a preguntas como «¿qué cobertura de CF necesito de verdad?», «¿es reversible mi des-identificación?» o «¿qué pongo en el `<org>` de mis `agentId`?».

**Prefijo `VF`.** Las variables de este perfil llevan prefijo `VF` (Variable de Federación). Son **específicas de federación**: describen el sistema de agentes y su gobernanza, no la infraestructura cloud ni el dimensionamiento de cómputo. Las variables de infraestructura (regiones, redes, tamaño de cluster, FinOps) pertenecen a la arquitectura concreta del stack y, por tanto, al [`appendix/`](./appendix/) o a la documentación del propio stack —no a este perfil ni al cuerpo (ver [regla anti-acoplamiento](./regla-anti-acoplamiento.md)).

**Cuándo se rellena.** Al inicio de la [Fase 1](./guia-adopcion-por-fases.md) (selección de stack), porque varias variables (`VF03`, `VF06`, `VF08`) condicionan qué stack encaja. Se revisa al menos en cada paso de fase y siempre que la realidad operativa cambie un valor declarado.

**Quién lo rellena.** El cuarto custodio —la **plataforma de federación** ([gobernanza-federada.md](./gobernanza-federada.md))— con input de transformación digital (para `VF04`, `VF05`, `VF07`) y de legal/DPO (para `VF04`, `VF05`). La plantilla socrática rellenable es [`templates/federation/perfil-adopcion-federacion.md`](../../templates/federation/perfil-adopcion-federacion.md); su ejemplo completo, [`templates/federation/perfil-adopcion-federacion-ejemplo.md`](../../templates/federation/perfil-adopcion-federacion-ejemplo.md) (Consultora Modelo S.L.).

---

## 1. Tabla resumen de variables

`Default` es el valor que el framework asume si la organización no declara otra cosa. La última columna dice **qué revisar cuando tu valor difiere del default**: ahí es donde el contexto cambia una decisión.

| ID | Variable | Default | Qué CF / documento revisar si difiere |
|---|---|---|---|
| **VF01** | Nº de agentes departamentales activos | ≥ 5 (umbral de sentido) | [Manifiesto §9](./manifesto.md); [Fase 0](./guia-adopcion-por-fases.md). Por debajo: Federation no se justifica todavía |
| **VF02** | Nº de pares que colaboran con frecuencia (corredores) | ≥ 3 | [Manifiesto §9](./manifesto.md); [glosario: corredor](./glosario-federacion.md). Define cuántos corredores hay que migrar (Fase 3–4) |
| **VF03** | Protocolo de comunicación inter-agente | `mcp` | [CF-01](./criterios-funcionales.md); [`appendix/mapeo-transporte/`](./appendix/mapeo-transporte/). `a2a` o `mixto` no cambian el cuerpo, solo el binding |
| **VF04** | Exposición regulatoria / sector | media | [CF-06](./criterios-funcionales.md); [`appendix/drift-recipes/`](./appendix/drift-recipes/); [patrones de drift](./patrones-deteccion-drift.md). Sector regulado endurece DLP y cadencia de drift |
| **VF05** | Reversibilidad de des-identificación requerida | mixta (reversible + irreversible) | [CF-06](./criterios-funcionales.md); `deidTokens` del [bloque](./esquema-bloque-contexto-cultural.md); [Guía de protección de datos](../adoption/guia-proteccion-datos.md). «Solo irreversible» elimina los `deidToken` |
| **VF06** | Stack opensource pre-existente | ninguno (greenfield) | [criterios-funcionales.md](./criterios-funcionales.md); [`appendix/stacks-referencia/`](./appendix/stacks-referencia/). Lo pre-existente fija qué CF ya están cubiertos |
| **VF07** | Criticidad máxima de dominio en la federación | `media` | [esquema-identidad-agente.md `criticality`](./esquema-identidad-agente.md); [gobernanza: gate y cadencia](./gobernanza-federada.md). `alta`/`critica` endurece el gate de coherencia y la frecuencia de drift |
| **VF08** | Modelo de despliegue del sustrato | sustrato con identidad por carga, aislamiento de red y ciclo de vida gestionado | [CF-04](./criterios-funcionales.md) (identidad); [CF-01](./criterios-funcionales.md) (intermediación). El framework **no** prescribe la tecnología del sustrato |
| **VF09** | Volumen de tráfico inter-agente | decenas–cientos de llamadas/hora | [Manifiesto §9](./manifesto.md); [CF-03](./criterios-funcionales.md) (latencia sub-ms). «Millones/hora» no es el caso de uso de Federation |
| **VF10** | Token `<org>` del namespace de `agentId` | sin default (la organización lo elige) | [esquema-identidad-agente.md §2](./esquema-identidad-agente.md). El framework **nunca** lo fija; en ejemplos: `consultora-modelo` |

> **Cómo leer la tabla.** Si todos tus valores coinciden con el default, el corpus se aplica tal cual. Cada vez que un valor difiere, la última columna te lleva al sitio exacto donde ese contexto cambia una decisión —normalmente un CF, un campo de esquema o una cadencia de gobernanza. Ninguna variable cambia los **principios** (§2 del manifiesto): eso es la sección 4 de este documento.

---

## 2. Detalle por variable

### VF01 — Nº de agentes departamentales activos

**Qué declara.** Cuántos agentes departamentales están vivos en producción (estado `lifecycleStatus = activo`, ver [esquema-identidad-agente.md §8](./esquema-identidad-agente.md)).

**Por qué importa.** Es el primer test de sentido del manifiesto §9: Federation tiene sentido «cuando la organización tiene al menos cinco o seis agentes departamentales activos». Por debajo, los patrones manuales de Adoption son suficientes y la sobrecarga operativa de Federation no se justifica.

**Si difiere del default (< 5).** La respuesta del framework es honesta: *todavía no*. Revisa la [Fase 0](./guia-adopcion-por-fases.md) y la checklist de prerrequisitos. Adoptar Federation con dos agentes federa rápido un sistema que no necesitaba federarse.

### VF02 — Nº de pares que colaboran con frecuencia (corredores)

**Qué declara.** Cuántos pares origen→destino colaboran «varias veces al día» —es decir, cuántos *corredores* ([glosario](./glosario-federacion.md)) existen. No es el nº de agentes (`VF01`) sino el de **relaciones de colaboración frecuente**.

**Por qué importa.** El corredor es la unidad de migración (manifiesto §6, Fase 3): no se federa la organización, se federa un corredor cada vez. `VF02` dimensiona la Fase 4 (federación progresiva). El segundo test de sentido del §9 («al menos tres pares que colaboran con frecuencia significativa») se mide aquí.

**Si difiere del default (< 3).** Mismo veredicto que `VF01`: la fricción de handovers manuales (Adoption §5) no llega al umbral que paga la federación. El [ejemplo del corredor](../../examples/federation/corredor-comercial-legal/) ilustra exactamente un corredor (comercial→legal).

### VF03 — Protocolo de comunicación inter-agente

**Qué declara.** Sobre qué protocolo viajan las llamadas inter-agente: `mcp` (default y caso primario del manifiesto), `a2a`, o `mixto` (algunos corredores por uno, otros por otro).

**Por qué importa.** El manifiesto se construye sobre MCP por pragmatismo (§9) pero los principios son portables a A2A. El protocolo **no cambia el cuerpo**: los esquemas son contratos, no serializaciones (ver [regla anti-acoplamiento](./regla-anti-acoplamiento.md) §4). Lo único que cambia es el **binding de transporte**.

**Si difiere del default.** Para `a2a` o `mixto`, revisa [`appendix/mapeo-transporte/`](./appendix/mapeo-transporte/): el mismo bloque de contexto cultural ([esquema](./esquema-bloque-contexto-cultural.md)) y el mismo descriptor viajan por A2A sin tocar el esquema. `endpoint.transport` del descriptor refleja este valor. **Lo que el framework no admite** es una extensión del protocolo base: lo descrito se monta sobre lo que el protocolo ya provee (manifiesto §8).

### VF04 — Exposición regulatoria / sector

**Qué declara.** El grado de exposición regulatoria de la organización (`baja` / `media` / `alta`) y, opcionalmente, el sector (sanidad, financiero, sector público, …). El vocabulario de clases de dato lo fija el Marco Regulatorio de la organización, no este perfil.

**Por qué importa.** Modula tres cosas: la severidad de la des-identificación en la ruta ([CF-06](./criterios-funcionales.md)), la cadencia de detección de drift ([patrones](./patrones-deteccion-drift.md)) y la finura de los análisis sectoriales. El manifiesto §10 declara que los patrones de drift de sectores regulados son una de las contribuciones más valiosas al apéndice.

**Si difiere del default (`alta` / sector regulado).** Revisa [`appendix/drift-recipes/`](./appendix/drift-recipes/) (recetas sectoriales) y endurece la cadencia de los [patrones de drift](./patrones-deteccion-drift.md). `CF-06` deja de ser opcional en la práctica: las clases de dato del Marco Regulatorio que el sector exige se detectan y redactan en la ruta sin excepción.

### VF05 — Reversibilidad de des-identificación requerida

**Qué declara.** Si la des-identificación que la organización necesita es `reversible` (la respuesta final se re-identifica en el origen), `irreversible` (el dato se va y no vuelve), o `mixta` (default: ambas, según categoría de dato).

**Por qué importa.** Determina si el bloque de contexto cultural transporta `deidTokens` o no. Cuando la redacción es reversible, el bloque transporta el token que permite re-identificar **solo en el agente de origen**, dentro de su `ttl` ([esquema del bloque](./esquema-bloque-contexto-cultural.md) §5). Cuando es irreversible, no hay token: el dato desapareció.

**Si difiere del default.** «Solo irreversible» elimina el sub-objeto `DeidToken` del bloque y simplifica la operación a costa de no poder re-identificar respuestas. «Solo reversible» exige un vault gestionado por el stack con política de TTL declarada. En ambos casos, la decisión cruza obligatoriamente la [Guía de protección de datos](../adoption/guia-proteccion-datos.md), que articula las capas técnica y contractual. La regla dura no es variable: **`deidToken` nunca contiene el valor original** (ver sección 4).

### VF06 — Stack opensource pre-existente

**Qué declara.** Qué componentes del stack ya existen en la organización antes de adoptar Federation: gateway, policy engine, service registry, IdP, observabilidad, DLP —o ninguno (greenfield, default).

**Por qué importa.** Fija qué [criterios funcionales](./criterios-funcionales.md) ya están (parcial o totalmente) cubiertos y, por tanto, qué hay que añadir en la Fase 1. Una organización con IdP criptográfico y observabilidad abierta maduros ya cubre `CF-04` y `CF-05`; solo le falta coserlos con el resto.

**Si difiere del default.** Mapea cada componente pre-existente a su CF y verifica la cobertura contra la checklist correspondiente; los huecos se registran como ADR de adopción (rango `0100+`, ver sección 5) con su control compensatorio. Las fichas de [`appendix/stacks-referencia/`](./appendix/stacks-referencia/) ayudan a evaluar si lo pre-existente cumple cada CF o si conviene sustituirlo.

### VF07 — Criticidad máxima de dominio en la federación

**Qué declara.** La criticidad más alta entre los dominios que se van a federar, con el enum del descriptor: `baja` / `media` (default) / `alta` / `critica` (ver [esquema-identidad-agente.md](./esquema-identidad-agente.md), campo `criticality`).

**Por qué importa.** La criticidad modula la severidad del *gate de coherencia* y la cadencia de revisión de drift ([gobernanza-federada.md](./gobernanza-federada.md)). No es lo mismo federar un dominio de baja criticidad que uno crítico cuyo error tiene consecuencias regulatorias o de negocio graves.

**Si difiere del default (`alta` / `critica`).** Endurece el gate de coherencia (rechazo, no aviso, ante conflicto) y sube la frecuencia de los [patrones de drift](./patrones-deteccion-drift.md). Cada agente declara su propia `criticality` en el descriptor; `VF07` es el máximo agregado que dimensiona la operación de toda la federación.

### VF08 — Modelo de despliegue del sustrato

**Qué declara.** El modelo de despliegue sobre el que corren los agentes y el gateway. **El framework no prescribe la tecnología del sustrato**: lo describe por las tres propiedades funcionales que necesita —**identidad por carga, aislamiento de red y ciclo de vida gestionado**— y deja la elección concreta a la organización y al apéndice.

- **Identidad por carga:** cada agente (carga de trabajo) tiene una identidad propia, verificable, que el sustrato le asigna y rota. Es el sustrato de [CF-04](./criterios-funcionales.md).
- **Aislamiento de red:** las llamadas inter-agente no esquivan el gateway; el sustrato impide canales laterales que salten la intermediación de [CF-01](./criterios-funcionales.md).
- **Ciclo de vida gestionado:** alta, actualización, salud y baja de cada carga son gestionadas, no manuales —lo que sostiene el ciclo de vida del descriptor ([esquema-identidad-agente.md §8](./esquema-identidad-agente.md)) y la retirada limpia.

**Por qué importa así.** Declararlo por propiedades, y no por producto, es lo que mantiene el perfil portable: cualquier sustrato que ofrezca las tres propiedades sirve, y la elección concreta (orquestador, malla, runtime) vive en [`appendix/stacks-referencia/`](./appendix/stacks-referencia/), no aquí (ver [regla anti-acoplamiento](./regla-anti-acoplamiento.md) §3, fila «fuera de scope»).

**Si difiere del default.** Si tu sustrato no ofrece alguna de las tres propiedades de forma nativa, esa propiedad es un control compensatorio que se documenta como ADR de adopción (`0100+`). Un sustrato sin identidad por carga, por ejemplo, te obliga a satisfacer `CF-04` de otro modo y a justificarlo.

### VF09 — Volumen de tráfico inter-agente

**Qué declara.** El orden de magnitud de llamadas inter-agente: el default es **decenas a cientos por hora**, que es el régimen para el que Federation tiene sentido (manifiesto §9: «agentes departamentales que se invocan decenas o cientos de veces por hora, no millones»).

**Por qué importa.** Confirma que el cuello de botella de la organización es humano (gestión de excepciones, revisión de drift) y no técnico. La latencia agregada de la capa de gobernanza es del orden de unos pocos milisegundos por salto, dominada por la verificación de identidad, no por la evaluación de policy ([CF-03](./criterios-funcionales.md), manifiesto §9).

**Si difiere del default (millones/hora).** Ese régimen no es el caso de uso de Federation. No es que el framework lo prohíba, es que el problema que resuelve —fricción cultural en handovers entre dominios— no es el problema de un sistema de millones de llamadas/hora. Antes de adoptar, revisa si tu problema real es de federación cultural o de escalado técnico de microservicios.

### VF10 — Token `<org>` del namespace de `agentId`

**Qué declara.** El token corto que la organización elige para el segmento `<org>` de sus `agentId` (`urn:myrmion:agent:<org>:<dominio>:<nombre>`).

**Por qué importa.** El framework **nunca** fija ni asume este valor: es una variable de la organización (ver [esquema-identidad-agente.md §2](./esquema-identidad-agente.md)). Es la raíz del espacio de nombres de toda la federación; una vez elegido, vive en todos los `agentId` y en todas las cadenas de decisión históricas, así que conviene elegirlo bien y estable.

**Sin default.** No hay valor por defecto: cada organización declara el suyo. En todos los ejemplos del corpus se usa el valor ficticio **`consultora-modelo`** (de Consultora Modelo S.L.), nunca el de una organización real. Recomendaciones: identificador corto, estable, en minúsculas y sin espacios; que no cambie con reorganizaciones de marca (no es un nombre comercial, es una raíz técnica).

---

## 3. Plantilla YAML rellenable

El YAML es **ilustrativo**, no normativo: el contrato es la tabla de la sección 1 y el detalle de la sección 2. Su forma rellenable y socrática (con preguntas guía) está en [`templates/federation/perfil-adopcion-federacion.md`](../../templates/federation/perfil-adopcion-federacion.md). Aquí va la estructura mínima:

```yaml
# Perfil de Adopción de Federation — <Nombre de la organización>
# Versión del perfil y fecha viven en la sección 0 de la plantilla rellenable.
perfilFederacion:
  VF01_agentesActivos: 0            # entero. Sentido si >= 5 (manifiesto §9)
  VF02_corredores: 0                # entero. Sentido si >= 3
  VF03_protocolo: "mcp"             # mcp | a2a | mixto
  VF04_exposicionRegulatoria:
    nivel: "media"                  # baja | media | alta
    sector: null                    # null | sanidad | financiero | sector-publico | ...
  VF05_reversibilidadDeid: "mixta"  # reversible | irreversible | mixta
  VF06_stackPreexistente:           # por CF: presente | parcial | ausente
    CF01_gateway: "ausente"
    CF02_serviceRegistry: "ausente"
    CF03_policyEngine: "ausente"
    CF04_identityProvider: "ausente"
    CF05_observabilidad: "ausente"
    CF06_dlpEnRuta: "ausente"
  VF07_criticidadMaxima: "media"    # baja | media | alta | critica (enum del descriptor)
  VF08_sustrato:                    # descrito por propiedades, no por producto
    identidadPorCarga: true
    aislamientoDeRed: true
    cicloDeVidaGestionado: true
    # La tecnología concreta del sustrato NO va aquí: va al ADR de adopción / appendix.
  VF09_volumenTrafico: "decenas-cientos-por-hora"  # orden de magnitud
  VF10_orgToken: "consultora-modelo"  # SIN default: la organización elige el suyo
```

> Las variables de infraestructura (regiones, redes, dimensionamiento, FinOps) **no** aparecen aquí por diseño: son propiedades del stack concreto, no de la federación. Si importan para tu organización, viven en la documentación del stack o en [`appendix/`](./appendix/), no en este perfil (ver [criterios-funcionales.md](./criterios-funcionales.md), nota «solo seis»).

---

## 4. Decisiones cerradas, no variables

No todo es variable. Hay decisiones del framework que **no** se parametrizan: ofrecerlas como opción sería vaciar Federation de contenido. Si una organización quiere cambiar alguna de estas, Federation no es para ella (manifiesto §2) —hay otros caminos válidos, pero no éste.

**Los tres principios del manifiesto §2 no son variables.**

1. **Compositividad sobre infraestructura existente.** Federation se monta sobre stack opensource maduro; no reimplementa gateway, policy engine, registry ni observabilidad. «Quiero construir mi propio gateway» no es una variable de perfil: es salirse del framework (manifiesto §8, §2).
2. **Cultura propagable.** El bloque de contexto cultural viaja en cada llamada inter-agente. «No propagar contexto en las llamadas» no es una opción configurable: es la diferencia entre una falange y un grupo de mercenarios (manifiesto §3.2).
3. **Drift como métrica de primera clase.** El drift federado se mide específicamente. «No medir drift» no es un valor de `VF`: es renunciar a lo que distingue Federation de un simple mallado de servicios (manifiesto §3.4).

**La política `fail-closed` ante incompatibilidad no es una variable.** Cuando el receptor detecta que la versión de Constitución del emisor es incompatible con la suya (`constitutionHash ∉ compatibleConstitutionHashes`), **la llamada no procede**. Lo único parametrizable es *cómo* de estricto se falla: `compatibilityPolicy ∈ {escalar, rechazar}`, con default `escalar` a humano (ver [esquema del bloque](./esquema-bloque-contexto-cultural.md) §4). Lo que **nunca** es opción es relajar a `permitir`: permitir la llamada con criterios desfasados sería la antítesis del framework (manifiesto §3.2). La incompatibilidad de **Marco Regulatorio** es además siempre dura: no admite ni siquiera `escalar` como excepción (Adoption §4, [esquema-identidad-agente.md §7](./esquema-identidad-agente.md)).

**Otras reglas duras que no se relajan vía perfil.**

- **`agentId` no reutilizable.** Cuando un agente se retira, su `agentId` queda archivado, no se libera ([esquema-identidad-agente.md §2](./esquema-identidad-agente.md)). No hay variable que lo permita reasignar.
- **`deidToken` nunca contiene el valor original.** Es siempre un puntero a un vault, con ámbito y TTL ([esquema del bloque](./esquema-bloque-contexto-cultural.md) §5). `VF05` decide *si* hay reversibilidad, no *si* el token puede llevar el dato en claro.
- **Sin extensiones de protocolo.** `VF03` elige el protocolo de transporte, pero nunca habilita una extensión del protocolo base: todo se monta sobre lo que el protocolo ya provee (manifiesto §8).
- **Cero marcas en el cuerpo.** `VF06` y `VF08` describen el stack por propiedades y por CF, nunca por producto en el cuerpo; los nombres viven en [`appendix/`](./appendix/) (ver [regla anti-acoplamiento](./regla-anti-acoplamiento.md)).

La frontera es clara: **las variables `VF` cambian cómo se aplica el método; las decisiones cerradas son el método.**

---

## 5. Relación con los ADR

Las decisiones que la organización toma a partir de su perfil se registran como Architecture Decision Records, con una numeración deliberadamente partida:

- **`0001`–`0099` — ADR del framework.** Decisiones del corpus normativo (por qué seis CF, por qué el contrato de hash excluye los metadatos, por qué `fail-closed` por defecto…). Las custodia el equipo del framework. Viven en [`adr/`](./adr/).
- **`0100`+ — ADR de adopción.** Decisiones de **tu** adopción derivadas de tu perfil: qué stack elegiste y por qué (`VF06`), qué hueco de CF dejaste cubierto con un control compensatorio ([criterios-funcionales.md](./criterios-funcionales.md)), qué propiedad de sustrato (`VF08`) satisfaces de forma no nativa, qué endureciste por criticidad (`VF07`) o por sector (`VF04`). Las custodia la plataforma de federación.

Cada vez que un valor de `VF` difiere del default y eso te lleva a una decisión, esa decisión es un candidato a ADR de adopción (`0100+`). La plantilla y los ejemplos están en [`adr/`](./adr/).

---

*Perfil de Adopción de Myrmion Federation — versión 1.0. Parte del corpus normativo.*

*Documentos relacionados: [criterios funcionales](./criterios-funcionales.md) (lo que el stack debe cubrir, modulado por `VF06`/`VF08`) · [esquema de identidad de agente](./esquema-identidad-agente.md) (`<org>` de `VF10`, `criticality` de `VF07`) · [esquema del bloque de contexto cultural](./esquema-bloque-contexto-cultural.md) (`deidTokens` de `VF05`, `compatibilityPolicy`) · [gobernanza federada](./gobernanza-federada.md) (gate y cadencia según `VF07`) · [guía de adopción por fases](./guia-adopcion-por-fases.md) (cuándo se rellena) · [regla anti-acoplamiento](./regla-anti-acoplamiento.md) (por qué las variables de infraestructura no están aquí). Su plantilla socrática es [`templates/federation/perfil-adopcion-federacion.md`](../../templates/federation/perfil-adopcion-federacion.md).*
