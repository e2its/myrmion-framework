# Myrmion Federation — Apéndice vivo: componentes candidatos

**Versión 1.0**

*Materializa el principio del [manifiesto](../manifesto.md) §4 y §10 de que las decisiones de implementación viven separadas de la especificación: aquí —y solo aquí— se nombran productos, versiones y marcas concretas para cubrir los [criterios funcionales CF-01..CF-06](../criterios-funcionales.md).*

> **BANNER DE VIGENCIA.** Esta carpeta envejece rápido por diseño. Las fichas describen el panorama de herramientas a una fecha concreta y **caducan**: lo que hoy cubre un criterio puede cambiar de licencia, ser absorbido por una adquisición, archivarse o renombrarse mañana. **No cites el apéndice como si fuera normativo.** Lo normativo es el cuerpo (`../criterios-funcionales.md` y las specs hermanas); esto es un mapa de carreteras que alguien tiene que repintar.
>
> **Última revisión global de esta matriz:** 2026-05-30. Si lees esto mucho después, asume que está desactualizado hasta que una ficha demuestre lo contrario.

---

## Por qué existe esta separación (el contrato de desacoplamiento)

El corpus normativo de Myrmion Federation se rige por la [regla anti-acoplamiento](../regla-anti-acoplamiento.md): **el cuerpo no nombra marcas**. El cuerpo describe *qué propiedad* debe cumplirse —los [criterios funcionales CF-01..CF-06](../criterios-funcionales.md)— y deja deliberadamente abierto *con qué* se cumple. El apéndice es la contrapartida: el único lugar del repo donde los productos concretos tienen nombre.

Esa decisión no es purismo. Responde a una asimetría de velocidades que el manifiesto declara explícitamente (§10: Federation «se diseña para no envejecer con el ecosistema sobre el que se monta»):

- **El cuerpo cambia despacio.** Un criterio funcional como «autenticación mutua con identidad criptográfica verificable» ([CF-04](../criterios-funcionales.md)) es estable durante años. El [descriptor de identidad de agente](../esquema-identidad-agente.md), su contrato de hash o la estructura del [bloque de contexto cultural](../esquema-bloque-contexto-cultural.md) son contratos: cambiarlos rompe federaciones existentes, así que cambian poco y con ADR de por medio.
- **El apéndice cambia rápido.** El mercado de gateways MCP, policy engines, service registries y herramientas de gobernanza de agentes se reescribe cada pocos trimestres. Aparecen proyectos, se fusionan, cambian de licencia (de open source a *source available* a comercial), los absorbe una adquisición o simplemente dejan de mantenerse.

Si el cuerpo nombrara productos, **el envejecimiento del mercado contaminaría la especificación**: cada cambio de licencia o cada adquisición obligaría a editar documentos normativos, y quien adoptara el framework heredaría decisiones de compra disfrazadas de arquitectura. Manteniendo las marcas confinadas aquí, el cuerpo permanece estable y portable —incluida la portabilidad a A2A que promete el manifiesto §9— mientras el apéndice absorbe toda la entropía del mercado.

**Regla operativa** (el *test de pertenencia* de la [regla anti-acoplamiento](../regla-anti-acoplamiento.md) §1): si una afirmación sigue siendo verdadera tras cambiar el stack entero, va en el cuerpo. Si describe el estado de un producto hoy, va aquí.

### Qué es y qué no es una ficha de apéndice

- **Es:** una lectura fechada de hasta qué punto un componente concreto ayuda a cubrir uno o varios criterios funcionales, con sus pros, contras, madurez y riesgo de continuidad.
- **No es:** una recomendación de Myrmion Federation, una certificación, ni una garantía. La adopción de cualquier componente listado es responsabilidad de la organización que adopta. La presencia en esta matriz **no implica respaldo**; solo afirma que, en la fecha de revisión, el componente parecía relevante para uno o más criterios.

---

## Gobernanza del apéndice (CODEOWNERS de comunidad)

La [regla anti-acoplamiento §5](../regla-anti-acoplamiento.md) fija una **salvaguarda estructural**: una asimetría de fricción deliberada entre cuerpo y apéndice.

- **El cuerpo** (`docs/federation/` y `templates/federation/`) lo custodian los mantenedores del framework: un PR exige aprobación de custodio y pasa el checklist bloqueante de la regla §6.
- **El apéndice** (`docs/federation/appendix/`) lo mantiene **la comunidad**: un PR aquí necesita una revisión ligera y puede entrar al ritmo del ecosistema.

Que sea más fácil contribuir al apéndice que al cuerpo es lo que garantiza que el contenido volátil fluya hacia donde debe estar. Reglas operativas de esta carpeta:

- **Propiedad por ficha.** Cada ficha (`stacks-referencia/<componente>.md`) declara su revisor en el banner. Idealmente esa propiedad se refleja en el `CODEOWNERS` del repositorio, asignando `docs/federation/appendix/` —y, cuando proceda, subcarpetas o ficheros concretos— a quienes se comprometen a revisar esa zona.
- **Caducidad activa.** Una ficha sin revisión en los últimos **6 meses** se considera *stale* y debe marcarse como tal en su banner hasta que un revisor la actualice o la retire. Una ficha *stale* sigue siendo informativa, pero el lector debe asumir deriva.
- **Los cambios de mercado se reflejan aquí, nunca en el cuerpo.** Una nueva versión, un cambio de licencia o una adquisición se documentan editando o añadiendo una ficha. Si alguien propone modificar un criterio funcional «porque la herramienta X ahora hace Y», la respuesta correcta es actualizar la ficha de X, no el criterio. Si una contribución al cuerpo huele a apéndice, el custodio la redirige; no la reescribe.
- **Bajo umbral de entrada, alto umbral de permanencia.** Añadir un candidato es barato (una ficha bien fechada). Mantenerlo en la matriz exige revisión periódica; lo que nadie revisa, envejece y acaba retirándose.

> Para añadir un componente, copia [`_plantilla-entrada-stack.md`](./_plantilla-entrada-stack.md) a `stacks-referencia/<componente>.md`, rellena el banner de vigencia y la matriz de cobertura, y abre el PR contra esta carpeta.

---

## Recordatorio de los criterios funcionales

La matriz se evalúa contra los seis criterios definidos —normativamente— en [`../criterios-funcionales.md`](../criterios-funcionales.md). Se reproducen aquí **solo como leyenda de columnas**; la definición vinculante es la del cuerpo.

| Criterio | Resumen (no normativo; ver el cuerpo) |
| --- | --- |
| **CF-01** | Gateway de llamadas inter-agente: intermedia toda llamada y expone puntos de extensión para policy y propagación de metadatos. |
| **CF-02** | Service registry federado: descubrimiento de agentes con descriptor de identidad extendido. |
| **CF-03** | Policy engine: evalúa en runtime las policies derivadas de la Constitución. |
| **CF-04** | Identity provider: identidad de servicio criptográfica con credenciales de vida corta (la base de la autenticación mutua verificable). |
| **CF-05** | Observabilidad agent-aware: traza cadenas de llamadas completas por `correlationId`. |
| **CF-06** | Des-identificación / DLP en la ruta: detecta y redacta/tokeniza PII/PHI antes de que alcance el modelo. |

> Si la numeración o el alcance de algún criterio difiere de lo anterior, **manda el cuerpo**. Esta tabla es un recordatorio, no la fuente de verdad.

---

## Matriz global: componente candidato × CF-01..CF-06

Lectura de la matriz:

- **●** — el componente **cubre** el criterio de forma directa y es su propósito declarado.
- **◐** — el componente **contribuye parcialmente** o lo cubre con configuración/integración adicional.
- **○** — **no aplica** o queda fuera del alcance del componente.

La cobertura no es transitiva: cubrir CF-04 no implica cubrir CF-03. **Ninguna fila cubre los seis criterios**; la federación se monta combinando componentes (un gateway/registry/IdP para CF-01/CF-02/CF-04, un policy engine para CF-03, una herramienta de deidentificación para CF-06, observabilidad agent-aware para CF-05). Los candidatos son los que enumera el manifiesto §4 y §10.

| Componente candidato | Tipo (rol) | CF-01 | CF-02 | CF-03 | CF-04 | CF-05 | CF-06 |
| --- | --- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Microsoft Agent Governance Toolkit** | Gobernanza de agentes (suite) | ◐ | ◐ | ● | ● | ◐ | ◐ |
| **IBM ContextForge** | Gateway / contexto MCP | ● | ◐ | ◐ | ● | ◐ | ● |
| **Agentgateway** | Gateway de agentes | ● | ◐ | ◐ | ● | ◐ | ○ |
| **Lunar.dev MCPX** | Gateway / proxy MCP | ● | ○ | ◐ | ◐ | ◐ | ◐ |
| **MCP Mesh** | Service mesh para MCP | ● | ◐ | ◐ | ● | ◐ | ○ |
| **MCP Gateway Registry** | Service registry MCP | ◐ | ● | ○ | ◐ | ○ | ○ |
| **OPA (Open Policy Agent)** | Policy engine | ○ | ○ | ● | ○ | ○ | ○ |
| **Cedar** | Policy engine / lenguaje | ○ | ○ | ● | ○ | ○ | ○ |
| **Casbin** | Autorización (RBAC/ABAC) | ○ | ○ | ● | ○ | ○ | ○ |
| **Microsoft Presidio** | Deidentificación PII/PHI | ○ | ○ | ○ | ○ | ○ | ● |

> **Esta matriz caduca.** Los símbolos son juicios a fecha 2026-05-30 y de grano grueso: para el detalle —versión, licencia, configuración necesaria, riesgo— consulta la ficha individual de cada componente en [`stacks-referencia/`](./stacks-referencia/) cuando exista, derivada de [`_plantilla-entrada-stack.md`](./_plantilla-entrada-stack.md). Una celda **●** **no** equivale a «listo para producción sin trabajo».

### Lectura por criterio (no normativa)

- **Gateway (CF-01), service registry (CF-02) e identity provider (CF-04)** se cubren típicamente en la capa de gateway/registry/mesh: los componentes de la mitad superior de la tabla. El manifiesto §4 y §10 señala que varios gateways integran un plugin de des-identificación —notablemente **IBM ContextForge**, típicamente sobre **Microsoft Presidio**—, lo que les permite cubrir a la vez CF-01 y CF-06.
- **Policy engine (CF-03)** es territorio de OPA, Cedar y Casbin; ninguno de ellos cubre identidad ni transporte. El **Microsoft Agent Governance Toolkit** incorpora policy enforcement propio, de ahí su **●** en CF-03.
- **Des-identificación / DLP en la ruta (CF-06)** requiere una pieza dedicada; en esta matriz la cubren de forma directa **Microsoft Presidio** y los gateways que lo integran. El cuerpo exige que el motor de detección sea *vendor-neutral* ([CF-06](../criterios-funcionales.md)) para no acoplar la política de datos al gateway.
- **Observabilidad agent-aware (CF-05)** rara vez es el propósito declarado de estos componentes: la mayoría exportan trazas (idealmente sobre un estándar abierto de telemetría) pero el dashboard y el backend los aporta el stack, de ahí el predominio de **◐** y **○** en esa columna. La trazabilidad de la [cadena de decisiones](../esquema-bloque-contexto-cultural.md) por `correlationId` y la detección de [drift federado](../patrones-deteccion-drift.md) se montan encima.

---

## Cómo encajan las marcas con MCP

El único protocolo nombrado en el **cuerpo** es **MCP**, porque es la base sobre la que se monta la federación (sin extensiones de protocolo; con portabilidad prevista a A2A, manifiesto §9). Todos los componentes de esta matriz se relacionan con MCP de un modo u otro —como gateway, service registry, service mesh o como pieza adyacente de policy/datos—, pero **el mapeo concreto de transporte** (cómo viaja el descriptor de identidad, el bloque de contexto cultural o los `deidToken` sobre un transporte real) vive en [`mapeo-transporte/`](./mapeo-transporte/), no en el cuerpo.

---

## Subcarpetas del apéndice

- [`stacks-referencia/`](./stacks-referencia/) — una ficha por componente candidato (deriva de [`_plantilla-entrada-stack.md`](./_plantilla-entrada-stack.md)).
- [`policy-templates/`](./policy-templates/) — implementaciones por dialecto de los patrones de [mapping Constitución → policy](../convenciones-mapping-constitucion-policy.md).
- [`mapeo-transporte/`](./mapeo-transporte/) — cómo se serializan los contratos sobre transportes concretos (MCP, A2A).

---

### Enlaces relacionados

- [Criterios funcionales (CF-01..CF-06)](../criterios-funcionales.md) — fuente normativa de las columnas.
- [Regla anti-acoplamiento](../regla-anti-acoplamiento.md) — por qué las marcas viven aquí y no en el cuerpo (test de pertenencia §1, CODEOWNERS dual §5).
- [Plantilla de ficha de stack](./_plantilla-entrada-stack.md) — esqueleto para añadir un candidato.
- [Manifiesto Myrmion Federation](../manifesto.md) — §4 (criterios, no marcas) y §10 originan la lista de candidatos.

*Apéndice vivo: componentes candidatos — versión 1.0. El contrato de desacoplamiento es parte del corpus normativo; el contenido de las fichas es informativo y caduca.*
