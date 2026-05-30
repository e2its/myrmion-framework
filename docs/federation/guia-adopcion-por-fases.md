# Myrmion Federation — Guía de Adopción por Fases

**Versión 1.0**

*Cómo se adopta una federación sin implantarla de golpe: las fases 0–5, cada una con su criterio de parada y el valor defendible que deja aunque la siguiente no llegue. Materializa las fases de adopción (§6) del manifiesto.*

---

## Qué es esto

Esta guía describe el **método de adopción** de Myrmion Federation: una secuencia de fases que llevan de cero a una federación madura. No es un cronograma ni una promesa de plazos; es un orden de dependencias. Cada fase se apoya en lo que dejó la anterior y produce algo verificable.

El principio que gobierna toda la guía es el del manifiesto (§6): **cada fase deja valor defendible aunque la siguiente no llegue.** Una organización que para en la Fase 2 no se queda con un proyecto a medias: se queda con sus departamentos descritos, su Constitución redactada y un mapa de reglas a política. Eso vale por sí mismo. La federación no es un interruptor; es una escalera donde cada peldaño se sostiene solo.

Cada fase se describe con seis elementos fijos:

- **Objetivo** — qué se busca conseguir.
- **Entradas** — qué se necesita de fases anteriores para empezar.
- **Actividades** — qué se hace.
- **Salidas / entregables** — qué queda escrito o construido al terminar.
- **Criterio de parada** — la señal observable de que la fase está hecha.
- **Estado defendible** — qué tiene la organización si para aquí.

Las fases no son agnósticas de los criterios funcionales: cada una avanza unos CF concretos y se apoya en documentos concretos del corpus. La correspondencia con tecnologías sigue viviendo en el apéndice (`./appendix/`); esta guía habla de capacidades y de método, no de productos.

---

## El mapa de las fases

| Fase | Nombre | Avanza | Cierra cuando |
|---|---|---|---|
| 0 | Prerrequisitos | — (cimientos organizativos) | Los prerrequisitos están verificados. |
| 1 | Selección de stack y PoC | CF-01, CF-02, CF-04 | Una identidad verificable existe, se publica y se descubre. |
| 2 | Mapping Constitución → política | CF-03 | La Constitución se compila a política sin pérdida. |
| 3 | Migración del primer corredor | CF-05, CF-06 (+ CF-01..CF-04 en uso) | El primer cruce de frontera ocurre gobernado y trazable. |
| 4 | Federación progresiva | CF-02 (a escala), todos en cada corredor | Un corredor nuevo se añade sin tocar los existentes. |
| 5 | Madurez y observabilidad de drift | CF-05 + señales de §7 | El drift se detecta y se acota como rutina. |

Las fases 0–2 son **preparación**: producen documentos y una prueba de concepto, pero ningún cruce de frontera real. La Fase 3 es el **primer corredor**: el primer valor de producción. Las fases 4–5 son **crecimiento y salud**: escalar lo que funciona y mantenerlo honesto en el tiempo.

---

## Fase 0 — Prerrequisitos

**Objetivo.** Tener los cimientos organizativos antes de tocar nada técnico: departamentos identificados, dueños humanos asignados, un primer cruce de frontera candidato y la autoridad para gobernar. La Fase 0 no construye federación; comprueba que se puede empezar a construirla.

**Entradas.** Ninguna del corpus. La entrada es la organización tal como está: sus departamentos, sus procesos que cruzan fronteras, sus responsables.

**Actividades.**
- Identificar los **agentes departamentales** candidatos y, para cada uno, su **dominio** y su **dueño** humano (ver glosario: *Agente departamental*, *Dominio*).
- Localizar un proceso real que cruza la frontera entre dos dominios: el **corredor** candidato para la Fase 3 (p. ej. el corredor Comercial → Legal para "lead → propuesta").
- Confirmar quién tiene **autoridad** para redactar y aprobar la Constitución. Sin un dueño de la gobernanza, no hay federación gobernada.
- Recorrer el checklist de prerrequisitos: `../../templates/federation/checklist-prerrequisitos-fase0.md`.

**Salidas / entregables.**
- Inventario de agentes departamentales candidatos, con dominio y dueño por cada uno.
- Corredor candidato elegido y justificado (qué proceso, qué dos dominios, qué valor).
- Responsable de la gobernanza nombrado.
- Checklist de prerrequisitos completado: `../../templates/federation/checklist-prerrequisitos-fase0.md`.

**Criterio de parada.** Todos los ítems del checklist de prerrequisitos están marcados y el corredor candidato está elegido. Si algún ítem no se puede marcar con honestidad, la fase **no** está hecha: cerrarla en falso es el modo más caro de fallar después.

**Estado defendible.** La organización tiene un mapa claro de qué departamentos serían agentes, quién los posee y por dónde empezaría a federar. Aunque no se siga adelante, ese mapa es un activo de gobernanza: dice quién decide qué, hoy, sin federación.

---

## Fase 1 — Selección de stack y prueba de concepto

**Objetivo.** Elegir las tecnologías concretas que materializarán las capacidades de la federación, y demostrar en pequeño que la capa de identidad y descubrimiento funciona: un agente con identidad verificable que se publica en el service registry y se descubre por su descriptor. Es la primera vez que el corpus se cruza con el apéndice.

**Entradas.** El inventario de agentes y el corredor candidato (Fase 0). El contrato del descriptor: `./esquema-identidad-agente.md`. Los criterios funcionales que el stack debe cumplir: `./criterios-funcionales.md`.

**Actividades.**
- Seleccionar, con ayuda del apéndice (`./appendix/`), las tecnologías que cubrirán cada criterio funcional: el gateway de llamadas inter-agente (CF-01), el service registry (CF-02), el policy engine (CF-03) y el identity provider (CF-04). La selección y su matriz de cobertura se documentan en el apéndice (ver `./regla-anti-acoplamiento.md`), no en el cuerpo.
- Construir un **descriptor de identidad** para un agente real, conforme al contrato (`./esquema-identidad-agente.md`): `agentId` con el formato normativo `urn:myrmion:agent:<org>:<dominio>:<nombre>`, `domain`, `criticality`, `dataClasses`, `capabilities`, `owner`, `platformCustodian`, `identityRef` y las referencias versionadas con `hash` (`constitutionRef`, `departmentLayerRef`, `regulatoryFrameworkRef`).
- Registrar el agente y comprobar que se **descubre** por su descriptor extendido —no solo nombre y endpoint, sino dominio, criticidad y versión de Constitución— sin coordinación humana previa (CF-02).
- Comprobar que la identidad es **verificable criptográficamente** antes de ejecutar una llamada, con credenciales de vida corta y revocables vinculadas al `agentId`: las propiedades de CF-04 (CF-01 es el punto por el que esa verificación se aplica en la ruta).
- Mantener el descriptor agnóstico: el cuerpo describe el contrato; la serialización en el registry, la firma y el binding de transporte concretos van al apéndice (`./appendix/stacks-referencia/` y `./appendix/mapeo-transporte/`).

**Salidas / entregables.**
- Selección de stack documentada en el apéndice de la organización, con su matriz de cobertura de CF-01..CF-04.
- Un descriptor de identidad real, conforme al contrato, con identidad criptográfica verificable.
- Un agente publicado en el service registry y descubierto por su descriptor extendido.

**Criterio de parada.** Existe una identidad de agente que (a) sigue el formato de `agentId`, (b) se verifica criptográficamente antes de la llamada (CF-04) y (c) se descubre por su descriptor extendido en el service registry (CF-02), todo a través del gateway (CF-01). Es decir: CF-01, CF-02 y CF-04 son demostrables sobre un caso real, no sobre un diagrama.

**Estado defendible.** La organización ha probado que puede dar identidad verificable y descubrible a sus agentes con el stack elegido. Aunque pare aquí, ha despejado el mayor riesgo técnico de la capa de identidad y descubrimiento (§3.1) y tiene un descriptor de referencia que reutilizar. La PoC es desechable; el aprendizaje sobre el stack, no.

---

## Fase 2 — Mapping Constitución → política

**Objetivo.** Convertir el acuerdo humano en algo ejecutable: redactar la **Constitución** de la federación y demostrar que se puede compilar a la configuración de un policy engine **sin pérdida** —es decir, que cada regla que la organización quiere imponer tiene una expresión en política, y que cada decisión de política se puede rastrear hasta una regla de la Constitución.

**Entradas.** El corredor candidato (Fase 0), el stack y el policy engine elegidos (Fase 1). El criterio de gobernanza: CF-03.

**Actividades.**
- Redactar la **Constitución** como documento vivo, versionado y auditable: quién puede hablar con quién, bajo qué condiciones, con qué datos y qué pasa cuando se rompe una regla (ver glosario: *Constitución*; manifiesto §5). La Constitución es propiedad de la organización, no del proveedor del policy engine.
- Para el corredor candidato, escribir las reglas que lo gobernarán: ¿puede el dominio emisor pedir esto al receptor, con qué datos, en qué contexto?
- **Compilar** la Constitución a la configuración del policy engine elegido y verificar la correspondencia en los dos sentidos:
  - Cada regla de la Constitución tiene una expresión en política (no se pierde nada al compilar).
  - Cada decisión de política se rastrea hasta una regla de la Constitución (no aparece nada que la Constitución no diga).
- Comprobar que los **cambios** en las reglas quedan registrados con su versión (CF-03).
- El dialecto concreto del lenguaje de políticas es una marca: vive en el apéndice (`./appendix/`), nunca en la Constitución, que se expresa en términos de capacidad y dominio.

**Salidas / entregables.**
- Constitución v1 redactada, versionada y aprobada por el responsable de la gobernanza.
- Configuración de política compilada desde la Constitución.
- Tabla de correspondencia regla ↔ política que demuestra el mapping sin pérdida en ambos sentidos.

**Criterio de parada.** La Constitución compila a política y la correspondencia se verifica en los dos sentidos: ninguna regla se pierde, ninguna política sobra. CF-03 es demostrable: una decisión de ejemplo se rastrea hasta su regla, y un cambio de regla queda registrado con versión.

**Estado defendible.** La organización tiene su Constitución escrita y un método probado para llevarla a política sin que se pierda nada por el camino. Aunque no migre ningún corredor todavía, posee el activo de gobernanza central —las reglas, explícitas y versionadas— que separa federar de conectar. Una Constitución sin federación sigue siendo un acuerdo auditable sobre quién puede hacer qué.

---

## Fase 3 — Migración del primer corredor

**Objetivo.** Poner en producción el **primer corredor**: el primer cruce de frontera real entre dos dominios, gobernado por la Constitución, con contexto que viaja y traza de extremo a extremo. Aquí la federación deja de ser preparación y se vuelve valor de producción.

**Entradas.** Identidad verificable y descubrible (Fase 1), Constitución compilada a política (Fase 2), corredor candidato (Fase 0). El contrato del contexto que viaja: `./esquema-bloque-contexto-cultural.md`. La vista de cómo fluye una interacción: `./guia-arquitectura-funcional.md`.

**Actividades.**
- Construir el **bloque de contexto cultural** que viaja en cada llamada conforme al contrato (`./esquema-bloque-contexto-cultural.md`): `correlationId` que persiste toda la cadena, `businessCaseId`, `constitutionHash` aplicado por el emisor, y la `decisionChain` de eslabones **DecisionHop** cuando `hopCount > 1`. El `constitutionHash` que viaja se valida contra el `compatibleConstitutionHashes` del descriptor receptor (Fase 1), usando el mismo contrato de hash (`./esquema-identidad-agente.md`).
- Sustituir los datos sensibles (PII/PHI) por **deidTokens** —punteros opacos, nunca el valor original— para que el contexto viaje y se exporte a observabilidad sin exponer el dato (CF-06; ver también la guía de protección de datos del ecosistema de adopción: `../adoption/guia-proteccion-datos.md`).
- Habilitar la **autenticación mutua con identidad criptográfica verificable** en el gateway (CF-01): el receptor verifica la identidad del emisor antes de ejecutar, la credencial es de vida corta y revocable, y la identidad es vinculable al `agentId` —las tres propiedades de CF-04 (para una implementación concreta, ver `./appendix/stacks-referencia/`).
- Hacer pasar una interacción real por el corredor siguiendo el flujo de la guía de arquitectura (`./guia-arquitectura-funcional.md`): descubrimiento → identidad → policy → contexto → validación de compatibilidad → traza.
- Verificar la **traza de extremo a extremo** (CF-05): la cadena se reconstruye después por su `correlationId` —quién pidió qué a quién, con qué identidad, con qué contexto (incluida la `decisionChain` y los `criteriaApplied` de cada DecisionHop) y qué decidió la gobernanza.

**Salidas / entregables.**
- Bloque de contexto cultural conforme al contrato, con `constitutionHash` validado contra el descriptor receptor.
- Corredor en producción entre los dos dominios, con autenticación mutua activa en el gateway.
- Al menos una interacción real, gobernada, con contexto presente y traza completa de extremo a extremo por `correlationId`.

**Criterio de parada.** Una petición real cruza la frontera entre los dos dominios y se cumple, sobre ese caso, todo lo siguiente: la decisión de gobierno se aplicó según la Constitución compilada (CF-03), el contexto viajó con la petición sin PII/PHI en claro —seudónimos y `deidTokens`, nunca valores— (CF-06), la autenticación fue mutua y verificada antes de ejecutar (CF-04, sobre CF-01) y la cadena es reconstruible de extremo a extremo por `correlationId` (CF-05). El corredor está hecho cuando produce **hechos defendibles**, no cuando "técnicamente conecta".

**Estado defendible.** La organización tiene un cruce de frontera que antes era un handover manual —una persona tomando el output de un agente y entregándolo a otro— y ahora ocurre gobernado, con contexto y trazable. Aunque no federe nada más, ese único corredor ya devuelve valor: sustituye un traspaso real por una invocación gobernada bajo reglas auditables. Es la prueba viva de que federar no es conectar.

---

## Fase 4 — Federación progresiva

**Objetivo.** Escalar lo que funciona: añadir nuevos corredores y nuevos agentes **sin tocar los existentes**. La señal de éxito de esta fase es de diseño, no de cantidad: que el coste de añadir el corredor número N no crezca con N.

**Entradas.** Un primer corredor en producción (Fase 3), la Constitución viva (Fase 2), el service registry poblado (Fase 1). El criterio de descubrimiento desacoplado: CF-02.

**Actividades.**
- Para cada nuevo dominio que se federa, repetir en pequeño las fases 1–3 sobre él: descriptor de identidad, bloque de contexto cultural, reglas en la Constitución para sus corredores.
- Pasar cada agente nuevo por el **gate de coherencia** antes de registrarlo: sus `capabilities` declaradas se evalúan contra los policy templates derivados de la Constitución, y el alta en el registry **falla** si entran en conflicto (`coherenceReview.status` debe ser `aprobado` —ver `./esquema-identidad-agente.md`).
- Añadir cada agente aprobado al **service registry** y comprobar que los demás lo descubren por su descriptor sin que haya que tocarlos: añadir un agente no obliga a reconfigurar los existentes (CF-02).
- **Ampliar** la Constitución con las reglas de los nuevos corredores, versionando cada cambio (CF-03). La Constitución crece por reglas, no por excepciones cableadas.
- Verificar que cada corredor nuevo nace con las garantías del primero: gobierno (CF-03), contexto que viaja sin PII/PHI en claro (CF-06), confianza verificable (CF-04, sobre CF-01) y traza por `correlationId` (CF-05). Un corredor que se salta una garantía no es un corredor federado; es una conexión punto a punto disfrazada.
- Vigilar que no reaparezca el **acoplamiento punto a punto**: los agentes se descubren y hablan contratos, no APIs internas (ver `./guia-arquitectura-funcional.md`).

**Salidas / entregables.**
- Dos o más corredores en producción, cada uno con las garantías de CF-03..CF-06.
- Service registry poblado en el que añadir un agente —tras pasar el gate de coherencia— no obliga a tocar los demás.
- Constitución ampliada y versionada con las reglas de los nuevos corredores.

**Criterio de parada.** Se ha añadido al menos un corredor nuevo **después** del primero, y hacerlo no obligó a modificar los corredores ya existentes (CF-02 a escala). El método de crecimiento está probado: la organización sabe cómo federar el siguiente dominio sin desestabilizar los anteriores.

**Estado defendible.** La organización tiene una federación de varios corredores que crece por adición, no por acoplamiento. Aunque pare de añadir corredores, lo construido es estable: cada corredor se sostiene solo y la incorporación del siguiente es un procedimiento conocido, no una reingeniería.

---

## Fase 5 — Madurez y observabilidad de drift

**Objetivo.** Mantener la federación **sana en el tiempo**. Lo que se construyó en las fases anteriores funciona el día del despliegue; esta fase asegura que siga siendo verdad meses después, detectando y acotando la deriva cultural (**drift**) y manteniendo vivas las señales de salud del manifiesto (§7).

**Entradas.** Una federación de varios corredores en producción (Fase 4), cadenas de decisión y trazas acumuladas con suficiente densidad (Fase 3 en adelante). Los patrones de detección de drift (`./patrones-deteccion-drift.md`), las métricas (`./metricas-federacion.md`) y las señales de salud del manifiesto §7.

**Actividades.**
- Instrumentar las **señales observables** sobre CF-05: cadenas trazables de extremo a extremo por `correlationId`, contexto presente en cada petición, decisiones de gobierno explícitas y revisables. Las métricas que las cuantifican están en `./metricas-federacion.md`.
- Ejercer los **tres patrones de detección de drift federado** (`./patrones-deteccion-drift.md`): Patrón A —análisis de cadenas cuestionadas, comparando los `criteriaApplied` de cada DecisionHop contra los que la Constitución exigía—; Patrón B —análisis de excepciones acumuladas sobre la misma policy—; Patrón C —análisis de coherencia presentando el mismo escenario a varios agentes—. El drift federado solo emerge al mirar el sistema entero (ver glosario: *Drift federado*).
- **Acotar** el drift cuando aparece: decidir si lo que cambió es la policy (ha quedado desfasada y hay que revisarla) o la realidad del departamento (hay que actualizar su Capa Departamental y, con ella, el `departmentLayerRef.hash` del descriptor de identidad y, si procede, el `constitutionHash` que se reconoce compatible —ver `./esquema-identidad-agente.md`).
- **Actualizar la Constitución** cuando la realidad de la federación lo exija, por proceso explícito y versionado, nunca por parche técnico (manifiesto §5). Cada cambio queda registrado con su versión (CF-03), y los agentes recalculan sus `hash` y `compatibleConstitutionHashes`.
- Propagar el cambio de la Constitución al **ecosistema de adopción**: una Constitución actualizada cambia lo que los departamentos deben capturar y declarar; esa actualización fluye hacia el Adoption Framework (las plantillas y guías de captura, p. ej. `../adoption/guia-proteccion-datos.md` y la plantilla de capa departamental `../../templates/adoption/capa-departamental.md`). Federation y Adoption son el mismo ecosistema: la Constitución que aquí se materializa programáticamente es la misma que en Adoption se articula —cambiarla en un lado obliga a propagarla al otro.

**Salidas / entregables.**
- Cuadro de señales de salud y métricas de la federación, instrumentado y revisado con periodicidad acordada según la criticidad de cada dominio.
- Los tres patrones de detección de drift ejercidos al menos una vez sobre datos reales, con su procedimiento de acotación.
- Constitución mantenida (cambios versionados, hashes recalculados) y propagación documentada hacia el ecosistema de adopción.

**Criterio de parada.** La Fase 5 no "termina": se convierte en rutina. Se considera **alcanzada** cuando el drift se detecta y se acota como práctica habitual —no como hallazgo casual— y cuando un cambio en la realidad de un departamento se propaga, por proceso explícito, desde su bloque de contexto cultural hasta la Constitución y, de ahí, al ecosistema de adopción.

**Estado defendible.** La organización tiene una federación que no solo funciona, sino que se sabe a sí misma: distingue lo que sus agentes declaran de lo que hacen, corrige la divergencia y mantiene su Constitución alineada con la realidad. Es el estado en el que la federación deja de ser un proyecto y se vuelve una capacidad permanente de la organización.

---

## Principios que atraviesan todas las fases

1. **Cada fase deja valor defendible.** Parar entre fases nunca deja un proyecto a medias, sino un activo completo de menor alcance (manifiesto §6).
2. **Gobierno antes que conexión.** No se migra ningún corredor (Fase 3) sin la Constitución compilada (Fase 2): las reglas existen antes que el canal (§4).
3. **Capacidad, no producto.** El método es agnóstico; la selección de stack (Fase 1) y todo lo concreto vive en el apéndice (`./appendix/`, ver `./regla-anti-acoplamiento.md`).
4. **Crecer por adición, no por acoplamiento.** La federación escala (Fase 4) añadiendo, no cableando: cada agente pasa el gate de coherencia y se descubre por su descriptor (CF-02).
5. **Honestidad en el tiempo.** La salud de la federación (Fase 5) se mide por la distancia entre lo declarado y lo real, y por la rapidez con que se cierra (§7).

---

## Documentos relacionados

- Manifiesto — fases de adopción (§6): `./manifesto.md`
- Glosario de la federación (vocabulario normativo): `./glosario-federacion.md`
- Criterios funcionales (CF-01..CF-06): `./criterios-funcionales.md`
- La Regla Anti-Acoplamiento (cuerpo vs. apéndice): `./regla-anti-acoplamiento.md`
- Esquema de identidad de agente (Fase 1): `./esquema-identidad-agente.md`
- Esquema del bloque de contexto cultural (Fase 3): `./esquema-bloque-contexto-cultural.md`
- Guía de arquitectura funcional (flujo de una interacción): `./guia-arquitectura-funcional.md`
- Patrones de detección de drift (Fase 5): `./patrones-deteccion-drift.md`
- Métricas de la federación (Fase 5): `./metricas-federacion.md`
- Checklist de prerrequisitos (Fase 0): `../../templates/federation/checklist-prerrequisitos-fase0.md`
- Apéndice — stacks de referencia y mapeo de transporte (Fase 1): `./appendix/`
- Ecosistema de adopción (captura y protección de datos): `../adoption/guia-proteccion-datos.md`

---

*Myrmion Federation — Guía de Adopción por Fases, versión 1.0. Parte del corpus normativo.*
