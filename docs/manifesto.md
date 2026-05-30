# Myrmion — Manifiesto

**Versión 1.0**

*El ecosistema opensource para la adopción corporativa de IA con cultura propia: tres frameworks — la modelización cultural mediante productos comerciales (Myrmion Adoption), la federación programática de agentes corporativos (Myrmion Federation) y el desarrollo gobernado de producto (Myrmion AI Factory).*

---

## Por qué Myrmion

El nombre Myrmion remite a *myrmex* — hormiga en griego — y a los mirmidones, soldados de élite de Aquiles, conocidos por actuar como una sola unidad bajo un mando común sin perder eficacia individual. Las dos imágenes apuntan al mismo problema: cómo coordinar muchos agentes — humanos, programáticos o productos comerciales asistidos por IA — de forma que actúen como una organización coherente sin ahogar la autonomía local de cada dominio.

Una colonia de hormigas es la referencia canónica de inteligencia colectiva con gobernanza distribuida. Cada individuo sigue reglas locales, hereda criterios comunes, y emerge un comportamiento coordinado a nivel sistema sin que nadie esté dirigiendo cada decisión. La falange de mirmidones añade el otro eje: agentes coordinados con disciplina técnica bajo un mando único, propagando contexto cultural en cada movimiento, manteniendo la cadena de decisiones auditable.

Las dos imágenes articulan el trayecto cultural del ecosistema — su columna vertebral: **empiezas por la colonia (Adoption) y evolucionas a la falange (Federation) cuando tu organización lo necesita.** Sobre ese eje cultural, Myrmion suma un tercer framework independiente — AI Factory — para la disciplina de desarrollo de producto.

## El problema

La mayoría de empresas que están adoptando IA hoy no construyen agentes desde cero. Despliegan productos comerciales: Copilot sobre Microsoft 365, Claude con Cowork, ChatGPT Enterprise, Gemini Enterprise, Custom GPTs, asistentes embebidos en su CRM o ERP. Eso es razonable.

El problema no es la elección de productos. El problema es lo que pasa después. Los productos comerciales vienen con valores por defecto que no son neutros — un tono, un sesgo, un criterio para decidir qué recomendar. Cuando una organización adopta el producto sin más, lo que obtiene no es *su* asistente: obtiene el del proveedor con el logo de su empresa encima.

A los seis meses la marca interna se ha vuelto borrosa. A los doce, alguien propone migrar de proveedor pensando que el problema es el modelo. No lo es. El problema es que la organización delegó, sin saberlo, una decisión que era suya: cómo piensa, cómo decide, cómo habla.

Myrmion existe para que esa delegación deje de ocurrir.

## Los tres frameworks

Myrmion se compone de tres frameworks. Dos de ellos — **Adoption** y **Federation** — son complementarios y articulan el trayecto cultural en dos grados de programaticidad: la colonia y la falange. El tercero — **AI Factory** — es independiente: resuelve un problema distinto, la disciplina de desarrollo de producto, aunque comparta con el resto el principio de gobernanza explícita y auditable.

### Myrmion Adoption — la colonia

La primera fase del trayecto cultural aborda el problema cultural sin tocar infraestructura programática. Articula el modelado en tres capas jerárquicas:

- **Marco Regulatorio** — heterónomo, viene de fuera, prevalece siempre.
- **Constitución Corporativa** — autoritaria, definida por la organización, captura voz, principios y restricciones.
- **Capas Departamentales** — específicas de dominio, modeladas por cada departamento.

La materialización vive en los productos comerciales que la organización ya usa, mediante los mecanismos que cada producto expone (instrucciones de proyecto, asistentes personalizados, Custom GPTs, agentes Copilot Studio, etc.). El modelado se mantiene en formato neutro y portable, no atado al producto.

Audiencia: CIOs, comités de dirección, líderes de departamento. La mayoría de organizaciones está hoy en esta fase.

📖 [Manifiesto detallado de Myrmion Adoption](./adoption/manifesto.md)

### Myrmion AI Factory

Framework de desarrollo de producto: un SDLC agéntico gobernado sobre Claude Code que construye software bajo gobernanza, seguridad y gates de calidad integrados. Es un framework **autónomo** — se adopta por sí solo, sin requerir Adoption ni Federation. No modela cultura corporativa ni federa agentes; comparte con el resto del ecosistema el principio de gobernanza explícita y auditable, aplicado a la disciplina de desarrollo. Audiencia: equipos de ingeniería, tech leads, plataformas de desarrollo.

📦 [Repositorio: e2its/myrmion-AI-factory](https://github.com/e2its/myrmion-AI-factory)

### Myrmion Federation — la falange

La segunda fase del trayecto cultural aborda el problema técnico cuando los handovers manuales entre departamentos empiezan a ocupar más tiempo del que ahorra la IA. Extiende el protocolo MCP (Model Context Protocol) con una capa de gobernanza federada culturalmente consciente, apoyándose en infraestructura opensource existente — gateways MCP, toolkits de governance de agentes, registries federados — sin reimplementarla.

Lo que Myrmion Federation aporta encima de esa infraestructura: convenciones para modelar agentes departamentales como servidores MCP gobernados, mapping de la Constitución Corporativa a policy templates, propagación de contexto cultural en cada llamada inter-agente, y patrones de detección de drift cultural a nivel federación.

Audiencia: CIOs, jefes de plataforma, tech leads. Las organizaciones que llegan aquí han hecho el trabajo cultural previo y necesitan dar el salto técnico.

📖 [Manifiesto detallado de Myrmion Federation](./federation/manifesto.md) · 🧭 [Índice y guía de navegación del corpus](./federation/indice-y-guia-de-navegacion.md)

## Cómo encajan los tres

**Adoption y Federation son complementarios.** Atacan el mismo problema — la cultura corporativa de IA — en dos grados de programaticidad. La Constitución Corporativa que articulas en Adoption es la misma que materializas programáticamente en Federation; lo que cambia es el grado de programaticidad, no la cultura ni el método. Empiezas por la colonia y evolucionas a la falange cuando tu organización lo necesita.

**Myrmion AI Factory es independiente de ese par.** No modela cultura corporativa ni federa agentes: construye productos de software con un SDLC gobernado. Se adopta por sí solo y resuelve un problema distinto — la disciplina de desarrollo — aunque comparta el principio de gobernanza explícita y auditable que recorre todo el ecosistema.

## Cómo se relaciona Myrmion con NIST AI RMF, ISO 42001 y EU AI Act

Myrmion es complementario, no alternativo. NIST AI RMF, ISO/IEC 42001 y EU AI Act describen *qué* gestionar, *qué* documentar, *qué* prohibir. Myrmion describe *cómo* operacionalizar la cultura corporativa para que los asistentes la hereden, *cómo* descentralizar el modelado en capas departamentales sin perder coherencia, y *cómo* graduar a federación programática cuando la organización lo necesita.

Una organización seria sobre adopción de IA termina típicamente con NIST/ISO como referencia normativa, EU AI Act como obligación legal donde aplique, y un framework operativo como Myrmion para articular el cómo del día a día.

## Licencia y contribuciones

Myrmion se publica bajo licencia MIT. Las contribuciones más valiosas son: actualizaciones del apéndice de mapeo a productos comerciales conforme estos evolucionan, plantillas sectoriales (sanidad, financiero, sector público, manufacturing) y casos de uso anonimizados.

---

*Myrmion — Manifiesto paraguas, versión 1.0.*
