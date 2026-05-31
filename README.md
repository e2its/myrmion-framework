<table>
<tr>
<td width="140" valign="middle">
<img src="./assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion

> Ecosistema opensource para articular la adopción corporativa de IA con cultura propia.

</td>
</tr>
</table>

Myrmion existe porque la mayoría de empresas que adoptan IA hoy lo hacen comprando licencias de productos comerciales — Copilot, Claude, ChatGPT Enterprise, Gemini Enterprise — y descubren a los seis meses que sus asistentes hablan más como el proveedor que como ellas. Myrmion propone un método para que eso no pase, y para que el método siga sirviendo cuando la organización gradúa a sistemas de agentes federados.

## Por qué Myrmion

El nombre Myrmion remite a *myrmex* — hormiga en griego — y a los mirmidones, soldados de élite de Aquiles, conocidos por actuar como una sola unidad bajo un mando común sin perder eficacia individual. Las dos imágenes apuntan al mismo problema: cómo coordinar muchos agentes — humanos, programáticos o productos comerciales asistidos por IA — de forma que actúen como una organización coherente sin ahogar la autonomía local de cada dominio.

Una colonia de hormigas es la referencia canónica de inteligencia colectiva con gobernanza distribuida. Cada individuo sigue reglas locales, hereda criterios comunes, y emerge un comportamiento coordinado a nivel sistema sin que nadie esté dirigiendo cada decisión. La falange de mirmidones añade el otro eje: agentes coordinados con disciplina técnica bajo un mando único, propagando contexto cultural en cada movimiento, manteniendo la cadena de decisiones auditable.

Las dos imágenes articulan el trayecto del ecosistema: **empiezas por la colonia y evolucionas a la falange cuando tu organización lo necesita**.

## El ecosistema

Myrmion se compone de tres frameworks:

### Myrmion Adoption

Framework para empresas que adoptan IA mediante productos comerciales. Modelado cultural en tres capas — Marco Regulatorio, Constitución Corporativa, Capas Departamentales — sin agentes programáticos. Audiencia: CIOs, comités de dirección, líderes de departamento.

📖 [Manifiesto de Myrmion Adoption](./docs/adoption/manifesto.md)

### Myrmion AI Factory

Framework de desarrollo de productos: un SDLC agéntico gobernado sobre Claude Code que construye software bajo gobernanza, seguridad y gates de calidad integrados. Es un framework **autónomo** — se adopta por sí solo, sin requerir Adoption ni Federation. Audiencia: equipos de ingeniería, tech leads, plataformas de desarrollo.

📦 [Repositorio: e2its/myrmion-AI-factory](https://github.com/e2its/myrmion-AI-factory)

### Myrmion Federation

Framework para organizaciones que han superado la adopción ligera y necesitan que sus agentes departamentales se invoquen mutuamente con gobernanza federada. Extiende el protocolo MCP con una capa de gobernanza culturalmente consciente, apoyándose en infraestructura opensource existente (gateways MCP, toolkits de governance de agentes). Audiencia: CIOs, jefes de plataforma, tech leads.

📖 [Manifiesto de Myrmion Federation](./docs/federation/manifesto.md)

## Cómo encajan los tres

**Adoption y Federation son complementarios.** Atacan el mismo problema — la cultura corporativa de IA — en dos grados de programaticidad. Modelar la cultura para que los asistentes la hereden es un ejercicio organizativo que cualquier empresa puede arrancar la próxima semana sin mover infraestructura (Adoption). Federar agentes programáticos con gobernanza es un proyecto de plataforma que solo tiene sentido cuando la cultura ya está articulada (Federation). La Constitución Corporativa que articulas en Adoption es la misma que materializas programáticamente en Federation; lo que cambia es el grado de programaticidad, no la cultura ni el método.

**Myrmion AI Factory es independiente de ese par.** No modela cultura corporativa ni federa agentes: construye productos de software con un SDLC gobernado. Se adopta por sí solo y resuelve un problema distinto — la disciplina de desarrollo — aunque comparta con el resto del ecosistema el principio de gobernanza explícita y auditable.

## Estado del proyecto

| Componente | Estado |
|---|---|
| Manifiesto Myrmion (paraguas) | ✅ v1.0 |
| Myrmion Adoption — Manifiesto | ✅ v1.0 |
| Myrmion Adoption — Plantillas (Capa 1, 2 y 3) | ✅ v1.0 |
| Myrmion Adoption — Guía de protección de datos (PII/PHI + licenciamiento) | ✅ v1.0 |
| Myrmion Adoption — Apéndice de mapeo a productos comerciales | 🚧 En preparación |
| Myrmion AI Factory — Framework (repositorio propio) | ✅ Activo |
| Myrmion Federation — Manifiesto | ✅ v1.0 |
| Myrmion Federation — Cuerpo normativo (índice, glosario, criterios funcionales, esquemas, mapping, drift, gobernanza, fases, métricas, perfil) | 🚧 En preparación |
| Myrmion Federation — Plantillas socráticas + ejemplo de corredor E2E | 🚧 En preparación |
| Myrmion Federation — Apéndice de stacks/policy-templates (comunidad) | 🚧 En preparación |

## Estructura del repositorio

```
myrmion/
├── README.md                      ← este archivo
├── LICENSE
├── assets/
│   └── myrmion-logo.png          ← logo del proyecto
├── docs/
│   ├── manifesto.md              ← manifiesto paraguas (corto)
│   ├── adoption/
│   │   ├── manifesto.md          ← manifiesto detallado de Adoption
│   │   └── guia-proteccion-datos.md ← guía de protección de datos (capa técnica + contractual)
│   └── federation/
│       ├── manifesto.md          ← manifiesto detallado de Federation
│       ├── indice-y-guia-de-navegacion.md  ← puerta de entrada al corpus
│       ├── glosario · criterios-funcionales · regla-anti-acoplamiento
│       ├── guia-arquitectura-funcional · esquema-identidad-agente · esquema-bloque-contexto-cultural
│       ├── convenciones-mapping-constitucion-policy · patrones-deteccion-drift
│       ├── gobernanza-federada · guia-adopcion-por-fases · metricas-federacion · perfil-adopcion-federacion
│       ├── adr/                  ← Architecture Decision Records (plantilla + ejemplo)
│       └── appendix/             ← apéndice vivo (comunidad): stacks-referencia, policy-templates, mapeo-transporte, drift-recipes
├── templates/
│   ├── adoption/                 ← plantillas y ejemplos de Marco Regulatorio, Constitución y capas departamentales
│   └── federation/               ← plantillas socráticas: descriptor, bloque, ficha-policy, charter, runbooks, checklist, perfil (+ ejemplos)
└── examples/
    └── federation/               ← corredor Comercial→Legal end-to-end + diagramas (anonimizado)
```

## Cómo empezar

1. Lee el [manifiesto paraguas](./docs/manifesto.md) para entender el ecosistema en conjunto.
2. Si tu organización está adoptando IA mediante productos comerciales, sigue con el [manifiesto de Myrmion Adoption](./docs/adoption/manifesto.md).
3. Si manejas datos personales, de salud o regulados (PII, RGPD, HIPAA, PCI-DSS…) o necesitas cumplimiento de proveedor (SOC 2, ISO 27001), lee la [Guía de protección de datos](./docs/adoption/guia-proteccion-datos.md): articula la capa técnica de des-identificación y la capa contractual de licenciamiento que el Marco Regulatorio necesita para no quedarse en prohibiciones sobre papel.
4. Si tu organización ya tiene agentes departamentales y necesita que se inter-comuniquen con gobernanza, empieza por el [manifiesto de Myrmion Federation](./docs/federation/manifesto.md) y luego el [índice y guía de navegación](./docs/federation/indice-y-guia-de-navegacion.md), que te lleva al documento concreto según tu rol (dirección, plataforma, transformación digital, tech lead).
5. Si necesitas construir productos de software con un SDLC gobernado, usa [Myrmion AI Factory](https://github.com/e2its/myrmion-AI-factory) — es un framework independiente y se adopta por sí solo.

## Cómo contribuir

Las contribuciones más valiosas, por framework:

- **Adoption:** apéndice de mapeo a productos comerciales conforme evolucionan, plantillas sectoriales (sanidad, financiero, sector público, manufacturing), casos de uso anonimizados.
- **Federation:** actualizaciones del [apéndice vivo](./docs/federation/appendix/) (stacks de referencia, policy-templates por dialecto, recetas de drift sectoriales, mapeo de transporte por protocolo), y casos de corredor anonimizados.

Antes de contribuir al **cuerpo** de Federation (`docs/federation/` y `templates/federation/`), lee la [regla anti-acoplamiento](./docs/federation/regla-anti-acoplamiento.md): el cuerpo se mantiene libre de marcas; los productos concretos viven solo en el apéndice. Ver [CONTRIBUTING.md](./CONTRIBUTING.md).

## Licencia

Este proyecto se distribuye bajo licencia [MIT](./LICENSE). Uso libre, comercial y no comercial, con atribución.

## Autor

Jose Luis Sanchez del Coso — [jose.e2its.com](https://jose.e2its.com), [www.e2its.com](https://www.e2its.com), [linkedin.com/in/jlsdc](https://www.linkedin.com/in/jlsdc)
