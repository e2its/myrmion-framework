# Myrmion

> Ecosistema opensource para articular la adopción corporativa de IA con cultura propia.

Myrmion existe porque la mayoría de empresas que adoptan IA hoy lo hacen comprando licencias de productos comerciales — Copilot, Claude, ChatGPT Enterprise, Gemini Enterprise — y descubren a los seis meses que sus asistentes hablan más como el proveedor que como ellas. Myrmion propone un método para que eso no pase, y para que el método siga sirviendo cuando la organización gradúa a sistemas de agentes federados.

## El ecosistema

Myrmion se compone de dos fases articuladas:

### Myrmion Adoption

Framework para empresas que adoptan IA mediante productos comerciales. Modelado cultural en tres capas — Marco Regulatorio, Constitución Corporativa, Capas Departamentales — sin agentes programáticos. Audiencia: CIOs, comités de dirección, líderes de departamento.

📖 [Manifiesto de Myrmion Adoption](./docs/adoption/manifesto.md)

### Myrmion Federation

Framework para organizaciones que han superado la adopción ligera y necesitan que sus agentes departamentales se invoquen mutuamente con gobernanza federada. Extiende el protocolo MCP con una capa de gobernanza culturalmente consciente, apoyándose en infraestructura opensource existente (gateways MCP, toolkits de governance de agentes). Audiencia: CIOs, jefes de plataforma, tech leads.

📖 [Manifiesto de Myrmion Federation](./docs/federation/manifesto.md) 
## Por qué dos fases y no una

Porque el problema cultural y el técnico tienen ritmos distintos. Modelar la cultura corporativa para que los asistentes la hereden es un ejercicio organizativo que cualquier empresa puede arrancar la próxima semana sin mover infraestructura. Federar agentes programáticos con gobernanza es un proyecto de plataforma que solo tiene sentido cuando la cultura ya está articulada. **Empiezas por la colonia y evolucionas a la falange cuando tu organización lo necesita.**

La Constitución Corporativa que articulas en Adoption es la misma que materializas programáticamente en Federation. Lo que cambia es el grado de programaticidad, no la cultura ni el método.

## Estado del proyecto

| Componente | Estado |
|---|---|
| Manifiesto Myrmion (paraguas) | ✅ v1.0 |
| Myrmion Adoption — Manifiesto | ✅ v1.0 |
| Myrmion Adoption — Plantillas | 🚧 En preparación |
| Myrmion Adoption — Apéndice de mapeo a productos comerciales | 🚧 En preparación |
| Myrmion Federation — Manifiesto | "✅ v1.0|
| Myrmion Federation — Especificaciones técnicas | ⏳ Planeado |

## Estructura del repositorio
myrmion/
├── README.md                      ← este archivo
├── LICENSE
├── docs/
│   ├── manifesto.md              ← manifiesto paraguas (corto)
│   ├── adoption/
│   │   └── manifesto.md          ← manifiesto detallado de Adoption
│   └── federation/
│       └── manifesto.md          ← manifiesto detallado de Federation (en preparación)
├── templates/
│   ├── adoption/                 ← plantillas de Constitución Corporativa, capas departamentales (en preparación)
│   └── federation/               ← plantillas de policy, esquemas MCP corporativos (planeado)
└── examples/                     ← casos de uso anonimizados (en preparación)

## Cómo empezar

1. Lee el [manifiesto paraguas](./docs/manifesto.md) para entender el ecosistema en conjunto.
2. Si tu organización está adoptando IA mediante productos comerciales, sigue con el [manifiesto de Myrmion Adoption](./docs/adoption/manifesto.md).
3. Si tu organización ya tiene agentes departamentales y necesita que se inter-comuniquen con gobernanza, sigue con el manifiesto de Myrmion Federation (./docs/federation/manifesto.md).

## Cómo contribuir

*Próximamente — contribuciones bienvenidas para apéndice de mapeo a productos, plantillas sectoriales y casos de uso anonimizados.*

## Licencia

Este proyecto se distribuye bajo licencia [MIT](./LICENSE). Uso libre, comercial y no comercial, con atribución.

## Autor

Jose Luis Sanchez del Coso — [jose.e2its.com](https://jose.e2its.com), [www.e2its.com](https://www.e2its.com), [linkedin.com/in/jlsdc](https://www.linkedin.com/in/jlsdc)
