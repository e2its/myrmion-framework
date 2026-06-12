# Myrmion — Puente con ISO/IEC 42001

**Versión 1.0**

*Mapeo de las cláusulas (4–10) y de los objetivos de control del Anexo A de ISO/IEC 42001 a los artefactos del ecosistema Myrmion, con la cobertura honesta de cada uno: qué aporta el corpus, qué debe aportar la organización adoptante y qué pertenece a otro framework. Parte del [área de cumplimiento](./README.md).*

---

## Cómo usar este documento

Tres advertencias antes de la primera tabla:

1. **Myrmion no certifica.** La certificación ISO/IEC 42001 es de la organización, sobre su AIMS, con su organismo acreditado. Este puente acelera la preparación — señala qué evidencia ya existe por construcción y qué falta — pero no la sustituye. El texto normativo de la norma hay que tenerlo: este documento la mapea, no la reproduce.
2. **ISO 42001 no da presunción de conformidad con el EU AI Act.** Son objetivos distintos: la norma certifica un sistema de gestión *organizacional*; el Reglamento exige conformidad *por sistema*. Myrmion cubre el hueco entre ambos justo donde duele — la comprobación 7 del [gate de coherencia](../federation/gobernanza-federada.md) y la `regulatoryClassification` del descriptor son control por sistema. El mapeo regulatorio está en el [puente EU AI Act](./puente-eu-ai-act.md); el estado de las normas armonizadas, en el [calendario](./appendix/calendario-regulatorio.md).
3. **La cobertura depende de la fase.** Una organización solo-Adoption tiene los artefactos pero su evidencia operativa es manual (revisión humana periódica, manifiesto Adoption §7); con Federation, la evidencia se genera por construcción (telemetría, gate, registros). Las tablas lo distinguen donde importa.

La herramienta operativa derivada de este puente es la [Declaración de Aplicabilidad pre-estructurada](../../templates/compliance/declaracion-aplicabilidad-iso42001.md).

---

## 1. Cláusulas 4–10 (el sistema de gestión)

| Cláusula | Qué exige | Artefacto Myrmion | Cobertura |
|---|---|---|---|
| **4. Contexto** | Comprender la organización, las partes interesadas y el alcance del AIMS | Marco Regulatorio §1 (identificación, jurisdicciones, sectores, datos) y §2–§4 (obligaciones); [Perfil de Adopción](../federation/perfil-adopcion-federacion.md) en Federation | **Alta** — el alcance formal del AIMS lo redacta el adoptante |
| **5. Liderazgo** | Compromiso de la dirección, política de IA, roles y autoridades (5.3) | Aprobación formal de Marco y Constitución por órganos de dirección (metadatos §0); custodia diferenciada + RACI ([gobernanza federada](../federation/gobernanza-federada.md) §1) | **Alta** |
| **6. Planificación** | Riesgos y oportunidades, **evaluación de riesgos y de impacto de sistemas de IA**, objetivos | `criticality` y `dataClasses` del [descriptor](../federation/esquema-identidad-agente.md); [evaluación de impacto](../../templates/compliance/evaluacion-impacto-ia.md) (en línea con ISO/IEC 42005); objetivos medibles sobre M1–M6 ([métricas](../federation/metricas-federacion.md)) | **Alta** con los artefactos del área de cumplimiento |
| **7. Soporte** | Competencia (7.2), concienciación (7.3), comunicación, información documentada (7.5) | [Plan de alfabetización](../../templates/compliance/plan-alfabetizacion-ia.md); corpus git-versionado con [contrato de hash](../federation/esquema-identidad-agente.md#6-contrato-de-hash) y ADRs como información documentada | **Alta** |
| **8. Operación** | Planificación y control operacional; ejecutar evaluación de impacto y tratamiento de riesgos | Gate de coherencia (control pre-producción), policy engine en la ruta ([CF-03](../federation/criterios-funcionales.md)), [registro de excepciones](../../templates/federation/registro-excepciones.md), runbooks de ciclo de vida | **Alta** en Federation; en Adoption, revisión de coherencia manual |
| **9. Evaluación del desempeño** | Seguimiento y medición (9.1), **auditoría interna (9.2)**, **revisión por la dirección (9.3)** | M1–M6 + [patrones de drift](../federation/patrones-deteccion-drift.md) (9.1); [programa de auditoría interna y revisión por la dirección](../../templates/compliance/programa-auditoria-interna-aims.md) (9.2–9.3) | **Alta** con el programa del área de cumplimiento |
| **10. Mejora** | No conformidades, acción correctiva, mejora continua | Señal de drift → revisión formal (ratificar / corregir / enmendar); excepciones acumuladas como retroalimentación (Patrón B); [runbook de incidentes](../../templates/compliance/runbook-incidentes-graves.md) §3.7 (lección registrada) | **Alta** |

## 2. Anexo A (objetivos de control)

La aplicabilidad control a control se declara en la [SoA](../../templates/compliance/declaracion-aplicabilidad-iso42001.md). Aquí, el mapeo por objetivo:

| Objetivo | Tema | Artefacto Myrmion | Cobertura y huecos |
|---|---|---|---|
| **A.2** | Políticas de IA | Las tres capas del Marco de Modelado — Marco Regulatorio, Constitución, capas departamentales — versionadas, con jerarquía de prevalencia y revisión declarada | **Fuerte.** La «política de IA» exigida es, en la práctica, la cúspide de la Capa 1 + Constitución |
| **A.3** | Organización interna | Custodia diferenciada (3 custodios en Adoption, 4 en Federation) + RACI; canal de preocupaciones vía escalado y [runbook de incidentes](../../templates/compliance/runbook-incidentes-graves.md) | **Fuerte** |
| **A.4** | Recursos de los sistemas de IA | Descriptor del agente (capabilities, datos, dependencias) como documentación de recursos; matriz de licenciamiento (recursos de terceros); [plan de alfabetización](../../templates/compliance/plan-alfabetizacion-ia.md) (recursos humanos) | **Media.** La documentación de recursos de cómputo y tooling es del adoptante/stack |
| **A.5** | Evaluación de impactos | [Evaluación de impacto unificada](../../templates/compliance/evaluacion-impacto-ia.md) — proceso, documentación, impacto sobre individuos/colectivos y societal | **Fuerte** con la plantilla; el contenido es del adoptante |
| **A.6** | Ciclo de vida del sistema de IA | Ciclo `propuesto → activo → deprecated → retirado`; gate de coherencia (verificación y validación pre-despliegue); runbooks de [onboarding](../../templates/federation/runbook-onboarding-agente.md) y [retirada](../../templates/federation/runbook-retirada-agente.md); registro de eventos por construcción (`correlationId`, `decisionChain`) | **Fuerte** en gestión y logging. El desarrollo/verificación técnica del modelo (si la organización construye) es territorio de **AI Factory** |
| **A.7** | Datos para sistemas de IA | [Guía de protección de datos](../adoption/guia-proteccion-datos.md) (de-id/DLP + capa contractual), `dataClasses` + CF-06 en ruta, [política de retención](../../templates/compliance/politica-retencion-evidencias.md) | **Fuerte** en protección y gestión. Calidad/procedencia de datos de **entrenamiento**: AI Factory o el proveedor del modelo |
| **A.8** | Información a partes interesadas | [Ficha de transparencia](../../templates/compliance/ficha-transparencia-ia.md) (documentación a usuarios, canal de preguntas); [runbook de incidentes](../../templates/compliance/runbook-incidentes-graves.md) (comunicación de incidentes y reporte externo) | **Fuerte** con las plantillas |
| **A.9** | Uso responsable | Constitución (principios de decisión, restricciones, escalado); clasificación de casos de uso del Marco §2.2 (uso previsto); policies en la ruta | **Fuerte** |
| **A.10** | Terceros y clientes | Matriz de licenciamiento por requisito (Marco §3); DPA/BAA/ZDR/residencia; CUECs declarados; obligaciones contractuales con clientes como sub-capa del Marco | **Fuerte** |

## 3. Lo que el adoptante pone (y Myrmion no)

Para que la SoA no genere falsas expectativas, lo que ningún artefacto del corpus puede dar hecho:

- **El alcance del AIMS y su integración** con otros sistemas de gestión (ISO 27001/9001) — decisión organizativa.
- **El contenido**: Myrmion da la estructura de cada artefacto; la cultura, los riesgos y las clasificaciones son de la organización.
- **La operación sostenida**: cadencias cumplidas, registros al día, formación impartida. La evidencia de Myrmion es por construcción solo si la maquinaria está construida y operando.
- **La verificación técnica de modelos** (sesgo, robustez, precisión): AI Factory o el proveedor, con su evidencia propia.

## 4. Normas satélite

- **ISO/IEC 23894** (gestión de riesgos de IA): metodología de referencia para la cláusula 6; el adoptante la usa al rellenar la evaluación de impacto y el tratamiento de riesgos.
- **ISO/IEC 42005** (evaluación de impacto): la [plantilla unificada](../../templates/compliance/evaluacion-impacto-ia.md) sigue su línea metodológica y añade la salida FRIA.
- **ISO/IEC 5338** (ciclo de vida): referencia para los controles A.6 cuando la organización construye sistemas — territorio AI Factory.
- **prEN 18286 y demás normas armonizadas del AI Act**: cuando se citen en el DOUE serán la vía de presunción de conformidad; este puente se extenderá entonces con ese mapeo (compromiso registrado en la [lista de vigilancia](./appendix/calendario-regulatorio.md)).

---

*Puente Myrmion ↔ ISO/IEC 42001 — versión 1.0. Parte del área de cumplimiento. Herramienta derivada: [Declaración de Aplicabilidad](../../templates/compliance/declaracion-aplicabilidad-iso42001.md). Complemento regulatorio: [puente EU AI Act](./puente-eu-ai-act.md).*
