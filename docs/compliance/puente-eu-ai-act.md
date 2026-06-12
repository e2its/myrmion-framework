# Myrmion — Puente con el EU AI Act

**Versión 1.0**

*Mapeo de las obligaciones del Reglamento (UE) 2024/1689, por rol y clase de riesgo, a los artefactos del ecosistema Myrmion. Parte del [área de cumplimiento](./README.md). Las fechas de aplicación de cada obligación viven en el [calendario regulatorio](./appendix/calendario-regulatorio.md), no aquí: este documento mapea estructura, que envejece lento; las fechas envejecen rápido.*

---

## Cómo usar este documento

El punto de partida es la **clasificación de casos de uso** del [Marco Regulatorio](../../templates/adoption/marco-regulatorio.md) §2.2: clase de riesgo y rol por caso de uso. Con esa tabla rellenada, este puente dice qué obligación toca y qué artefacto la cubre. Dos avisos:

- **El rol manda tanto como la clase.** La organización adoptante típica de Myrmion es **deployer** (usa productos comerciales o construye agentes internos sobre modelos de terceros). Pero el **art. 25** convierte al deployer en **proveedor** — sujeto a las obligaciones del art. 16, que arrastran desde los requisitos de los arts. 9–15 hasta el QMS (art. 17), la conservación de documentación y logs (arts. 18–19), la evaluación de conformidad (art. 43), el marcado CE (art. 48) y el registro UE (art. 49) — si pone su nombre o marca sobre un sistema de alto riesgo, lo modifica sustancialmente o cambia su finalidad prevista. Federar agentes departamentales propios roza esa frontera: la decisión de rol se toma con criterio jurídico y queda sellada en la `regulatoryClassification` del [descriptor](../federation/esquema-identidad-agente.md).
- **Este puente no da presunción de conformidad.** La darán las normas armonizadas cuando se citen en el DOUE. Lo que este puente da es la trazabilidad obligación → artefacto → evidencia.

## 1. Obligaciones de toda adopción (cualquier clase de riesgo)

| Obligación | Qué exige | Artefacto Myrmion |
|---|---|---|
| **Art. 5 — prácticas prohibidas** | No usar IA para los casos vetados | Clasificación del Marco §2.2 (un caso prohibido **no se autoriza**); en Federation, la comprobación 7 del [gate](../federation/gobernanza-federada.md) convierte el intento en **alerta al custodio del Marco** — el mecanismo «sin botón de aprobar de todos modos» que la prohibición exige |
| **Art. 4 — alfabetización en IA** | Nivel suficiente de competencia del personal y de quien opere IA en nombre de la organización | [Plan de alfabetización](../../templates/compliance/plan-alfabetizacion-ia.md), con registro de formación como evidencia |
| **Art. 50 — transparencia** | Avisar de la interacción con IA; marcar contenido sintético; divulgar deep fakes | [Ficha de transparencia](../../templates/compliance/ficha-transparencia-ia.md), una por asistente/agente |

## 2. Deployer de un sistema de alto riesgo

| Obligación | Qué exige | Artefacto Myrmion |
|---|---|---|
| Art. 26.1 — uso conforme a instrucciones | Medidas técnicas y organizativas para usar el sistema según sus instrucciones de uso | Ficha de transparencia §5 + capa departamental (uso previsto operativizado) |
| Art. 26.2 — supervisión humana competente | Personas con competencia, formación y autoridad | Constitución §Escalado + [plan de alfabetización](../../templates/compliance/plan-alfabetizacion-ia.md) (colectivo de operadores de alto riesgo) + métrica M3 |
| Art. 26.5 — vigilancia del funcionamiento | Monitorizar y suspender si hay riesgo | [Plan de monitorización post-comercialización](../../templates/compliance/plan-monitorizacion-post-mercado.md) (los patrones de drift en versión documentada) + runbooks de ciclo de vida (suspender = `deprecated`) |
| Art. 26.6 — conservación de logs | Logs bajo su control, plazo mínimo regulado | `correlationId` + `decisionChain` por construcción ([CF-05](../federation/criterios-funcionales.md)) + [política de retención](../../templates/compliance/politica-retencion-evidencias.md) |
| Art. 26.7 — información a trabajadores | Informar antes de usar alto riesgo en el trabajo | Plan de alfabetización + ficha de transparencia del sistema |
| **Art. 27 — FRIA** | Evaluación de impacto sobre derechos fundamentales (organismos públicos, servicios públicos, scoring/seguros) | [Evaluación de impacto unificada](../../templates/compliance/evaluacion-impacto-ia.md) §5–§7 |
| Art. 26.5 / art. 73 — informar de incidentes | Informar al proveedor/autoridad de riesgos e incidentes graves | [Runbook de incidentes graves](../../templates/compliance/runbook-incidentes-graves.md) |

## 3. Proveedor de un sistema de alto riesgo

Si el art. 25 (o el diseño propio) coloca a la organización como proveedor:

| Obligación | Artefacto Myrmion | Cobertura |
|---|---|---|
| Art. 9 — gestión de riesgos continua | Evaluación de impacto + criticidad + drift como ciclo vivo | **Parcial** — el proceso existe; la profundidad técnica por sistema la pone el adoptante |
| Art. 10 — datos y gobernanza de datos | [Guía de protección de datos](../adoption/guia-proteccion-datos.md), `dataClasses`, CF-06 | **Parcial** — fuerte en privacidad; representatividad/sesgo de datos de entrenamiento: AI Factory o proveedor del modelo |
| Art. 11 + Anexo IV — documentación técnica | Descriptor, esquemas, ADRs, fichas | **Parcial** — buena base; el expediente Anexo IV completo es trabajo específico del adoptante |
| Art. 12 — registro automático de logs | `decisionChain` + telemetría CF-05 | **Fuerte** — por construcción |
| Art. 13 — transparencia e instrucciones de uso | [Ficha de transparencia](../../templates/compliance/ficha-transparencia-ia.md) §5 | **Fuerte** como base |
| Art. 14 — supervisión humana | Escalado por construcción (incompatibilidad → humano; policy → humano) + M3 | **Fuerte** |
| Art. 15 — precisión, robustez, ciberseguridad | — | **Fuera del corpus** — evaluación técnica del modelo: AI Factory; identidad/autenticación de la federación ([CF-04](../federation/criterios-funcionales.md)) aporta a la ciberseguridad operativa |
| Art. 17 — sistema de gestión de calidad | Gobernanza federada + gate + versionado + [programa de auditoría](../../templates/compliance/programa-auditoria-interna-aims.md) | **Parcial-fuerte** — el QMS documental se ensambla desde estos artefactos |
| Arts. 18–19 — conservación de documentación y logs | [Política de retención](../../templates/compliance/politica-retencion-evidencias.md) | **Fuerte** con la política rellenada |
| Art. 43 — evaluación de conformidad · Art. 48 — marcado CE · Art. 49 — registro en la base de datos UE | — | **Fuera del corpus** — procedimientos administrativos ante autoridad/organismo notificado; el [service registry](../federation/criterios-funcionales.md) es el inventario interno que alimenta el registro, no lo sustituye |
| **Art. 72 — monitorización post-comercialización** | [Plan PMM](../../templates/compliance/plan-monitorizacion-post-mercado.md) sobre patrones A/B/C y M1–M6 | **Fuerte** — es la pieza donde Myrmion más se adelanta a la norma |
| **Art. 73 — incidentes graves** | [Runbook de incidentes](../../templates/compliance/runbook-incidentes-graves.md) con los plazos regulatorios | **Fuerte** con el runbook rellenado |

## 4. Modelos de propósito general (GPAI)

La organización adoptante típica **consume** GPAI, no lo provee: las obligaciones de los arts. 51–56 caen en el proveedor del modelo. Lo que el adoptante controla es la **elección**: la matriz de licenciamiento del Marco §3 debe registrar si el proveedor cumple sus obligaciones GPAI (la adhesión al GPAI Code of Practice es un proxy razonable — ver [calendario](./appendix/calendario-regulatorio.md)). Excepción: una organización que ponga en el mercado un modelo propio o un fine-tuning sustancial entra en territorio proveedor de GPAI — fuera del alcance de este corpus, frontera con AI Factory.

## 5. Síntesis: dónde Myrmion es fuerte y dónde no llega

- **Fuerte por construcción:** prohibiciones con enforcement (art. 5), logs y trazabilidad (arts. 12/26.6), supervisión humana (art. 14), monitorización post-comercialización (art. 72), control de conformidad por sistema (gate, comprobación 7).
- **Fuerte con plantilla rellenada:** transparencia (arts. 50/13), alfabetización (art. 4), FRIA (art. 27), incidentes (art. 73), retención (arts. 18–19).
- **Parcial:** QMS (art. 17), documentación técnica Anexo IV (art. 11), gobernanza de datos de entrenamiento (art. 10).
- **Fuera del corpus, declarado:** evaluación técnica del modelo (art. 15), evaluación de conformidad, marcado CE y registro UE (arts. 43/48/49), obligaciones GPAI de proveedor.

---

*Puente Myrmion ↔ EU AI Act — versión 1.0. Parte del área de cumplimiento. Complementos: [puente ISO 42001](./puente-iso42001.md) · [calendario regulatorio](./appendix/calendario-regulatorio.md).*
