<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion — Plantilla de Declaración de Aplicabilidad (SoA) ISO/IEC 42001

**Versión 1.0**

*Plantilla de la Declaración de Aplicabilidad del Anexo A de ISO/IEC 42001, pre-estructurada con el artefacto Myrmion que materializa cada control. La SoA es el documento donde la organización declara, control a control, si aplica, por qué, y cómo está implementado — el artefacto central de cualquier auditoría de certificación.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

**Necesitas el texto oficial de la norma.** Esta plantilla lista los controles por identificador y tema abreviado para estructurar el trabajo; la redacción normativa exacta de cada control está en ISO/IEC 42001:2023, que la organización debe poseer. La columna «Artefacto Myrmion sugerido» es el punto de partida del mapeo — no la respuesta del auditor: la organización debe verificar que el artefacto está **rellenado y operando**, no solo adoptado.

**Quién la rellena.** Quien lidere la implantación del AIMS, con los custodios de cada capa. La justificación de inaplicabilidad de un control es tan importante como la implementación de uno aplicable — «no aplica» sin justificación es no conformidad esperando auditor.

**Convención de la columna Estado:** `implementado` · `parcial` · `planificado` · `no aplicable`.

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Alcance del AIMS al que aplica esta SoA | *(unidades, sistemas, sedes)* |
| Versión | *(p. ej. 1.0)* |
| Responsable del AIMS | |
| Fecha de aprobación | *(YYYY-MM-DD)* |
| Versión de la norma de referencia | ISO/IEC 42001:2023 |

---

## A.2 — Políticas relacionadas con la IA

| Control | Tema | ¿Aplica? | Artefacto Myrmion sugerido | Estado | Evidencia |
|---|---|---|---|---|---|
| A.2.2 | Política de IA | | Marco Regulatorio + Constitución Corporativa (cúspide normativa de las tres capas) | | |
| A.2.3 | Alineamiento con otras políticas de la organización | | Marco §2–§4 (absorbe ISO 27001, sectoriales, contractuales) | | |
| A.2.4 | Revisión de la política de IA | | Frecuencia de revisión declarada en §0 y «Cómo usar» de Marco y Constitución; trazabilidad git | | |

## A.3 — Organización interna

| Control | Tema | ¿Aplica? | Artefacto Myrmion sugerido | Estado | Evidencia |
|---|---|---|---|---|---|
| A.3.2 | Roles y responsabilidades de IA | | Custodia diferenciada por capa + RACI ([gobernanza federada](../../docs/federation/gobernanza-federada.md) §1; [charter de plataforma](../federation/charter-plataforma-federacion.md)) | | |
| A.3.3 | Comunicación de preocupaciones | | Rutas de escalado + alerta al custodio del Marco + [runbook de incidentes](./runbook-incidentes-graves.md) | | |

## A.4 — Recursos de los sistemas de IA

| Control | Tema | ¿Aplica? | Artefacto Myrmion sugerido | Estado | Evidencia |
|---|---|---|---|---|---|
| A.4.2 | Documentación de recursos | | Descriptor de agente (capabilities, dependencias) + inventario del service registry | | |
| A.4.3 | Recursos de datos | | `dataClasses` + [Guía de protección de datos](../../docs/adoption/guia-proteccion-datos.md) | | |
| A.4.4 | Recursos de herramientas | | Matriz de licenciamiento (Marco §3) + ADRs de stack | | |
| A.4.5 | Recursos de sistema y cómputo | | *(del adoptante/stack — documentar aquí)* | | |
| A.4.6 | Recursos humanos | | [Plan de alfabetización](./plan-alfabetizacion-ia.md) (colectivos y competencias) | | |

## A.5 — Evaluación de impactos de los sistemas de IA

| Control | Tema | ¿Aplica? | Artefacto Myrmion sugerido | Estado | Evidencia |
|---|---|---|---|---|---|
| A.5.2 | Proceso de evaluación de impacto | | [Plantilla de evaluación de impacto](./evaluacion-impacto-ia.md) + obligatoriedad vía gate (comprobación 7) | | |
| A.5.3 | Documentación de las evaluaciones | | Evaluaciones versionadas y referenciadas por `impactAssessmentRef` | | |
| A.5.4 | Impacto sobre individuos o grupos | | Evaluación §2–§3 y §6 (FRIA) | | |
| A.5.5 | Impactos sociales | | Evaluación §3 | | |

## A.6 — Ciclo de vida del sistema de IA

| Control | Tema | ¿Aplica? | Artefacto Myrmion sugerido | Estado | Evidencia |
|---|---|---|---|---|---|
| A.6.1.2 | Objetivos del desarrollo responsable | | Constitución (principios) + clasificación de casos de uso (Marco §2.2) | | |
| A.6.1.3 | Procesos de diseño y desarrollo responsables | | *(si la organización construye: AI Factory; si no: justificar alcance)* | | |
| A.6.2.2 | Requisitos y especificación del sistema | | Descriptor + capa departamental del dominio | | |
| A.6.2.3 | Documentación de diseño y desarrollo | | Descriptor + ADRs | | |
| A.6.2.4 | Verificación y validación | | Gate de coherencia (siete comprobaciones, reproducible) + revisión de coherencia en Adoption | | |
| A.6.2.5 | Despliegue | | [Runbook de onboarding](../federation/runbook-onboarding-agente.md) | | |
| A.6.2.6 | Operación y monitorización | | [Patrones de drift](../../docs/federation/patrones-deteccion-drift.md) + [plan PMM](./plan-monitorizacion-post-mercado.md) | | |
| A.6.2.7 | Documentación técnica | | Descriptor + esquemas + fichas ([puente EU AI Act](../../docs/compliance/puente-eu-ai-act.md) para Anexo IV) | | |
| A.6.2.8 | Registro de eventos (logs) | | `correlationId` + `decisionChain` ([CF-05](../../docs/federation/criterios-funcionales.md)) + [política de retención](./politica-retencion-evidencias.md) | | |

## A.7 — Datos para los sistemas de IA

| Control | Tema | ¿Aplica? | Artefacto Myrmion sugerido | Estado | Evidencia |
|---|---|---|---|---|---|
| A.7.2 | Gestión de datos | | Guía de protección de datos + `dataClasses` + CF-06 | | |
| A.7.3 | Adquisición de datos | | Matriz de licenciamiento (qué datos entran a qué proveedor, bajo qué contrato) | | |
| A.7.4 | Calidad de los datos | | *(entrenamiento: AI Factory/proveedor; operación: controles del adoptante)* | | |
| A.7.5 | Procedencia de los datos | | `dataClassesTouched` por capability + trazabilidad de cadenas | | |
| A.7.6 | Preparación de los datos | | Des-identificación previa (Adoption §3.4) o en ruta (CF-06) | | |

## A.8 — Información para partes interesadas

| Control | Tema | ¿Aplica? | Artefacto Myrmion sugerido | Estado | Evidencia |
|---|---|---|---|---|---|
| A.8.2 | Documentación e información a usuarios | | [Ficha de transparencia](./ficha-transparencia-ia.md) | | |
| A.8.3 | Reporte externo | | Ficha §6 (canal) + [runbook de incidentes](./runbook-incidentes-graves.md) §2 (notificaciones) | | |
| A.8.4 | Comunicación de incidentes | | Runbook de incidentes §3–§5 | | |
| A.8.5 | Información a partes interesadas | | Ficha de transparencia + obligaciones contractuales (Marco §3) | | |

## A.9 — Uso de los sistemas de IA

| Control | Tema | ¿Aplica? | Artefacto Myrmion sugerido | Estado | Evidencia |
|---|---|---|---|---|---|
| A.9.2 | Procesos de uso responsable | | Constitución + policies en la ruta + [plan de alfabetización](./plan-alfabetizacion-ia.md) | | |
| A.9.3 | Objetivos del uso responsable | | Constitución (principios de decisión, restricciones) | | |
| A.9.4 | Uso previsto | | Clasificación de casos de uso (Marco §2.2) + ficha de transparencia §5 | | |

## A.10 — Relaciones con terceros y clientes

| Control | Tema | ¿Aplica? | Artefacto Myrmion sugerido | Estado | Evidencia |
|---|---|---|---|---|---|
| A.10.2 | Asignación de responsabilidades | | Matriz de licenciamiento (quién es encargado por vía de aprovisionamiento) + CUECs | | |
| A.10.3 | Proveedores | | Marco §3 (DPA/BAA/ZDR/residencia/no-entrenamiento; GPAI Code of Practice como criterio) | | |
| A.10.4 | Clientes | | Obligaciones contractuales asumidas (Marco §3) + ficha de transparencia | | |

---

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Parte del [área de cumplimiento](../../docs/compliance/README.md). Derivada del [puente Myrmion ↔ ISO 42001](../../docs/compliance/puente-iso42001.md). Los identificadores y temas se listan de forma abreviada para estructurar el trabajo: el texto normativo de cada control es el de ISO/IEC 42001:2023.*
