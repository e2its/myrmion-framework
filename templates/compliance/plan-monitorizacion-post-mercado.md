<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion — Plantilla del Plan de Monitorización Post-Comercialización

**Versión 1.0**

*Plantilla para formalizar, por sistema de IA, el plan de monitorización post-comercialización que el EU AI Act art. 72 exige a los proveedores de alto riesgo — y que en Myrmion ya existe en operación: los [patrones de detección de drift](../../docs/federation/patrones-deteccion-drift.md) y las [métricas de federación](../../docs/federation/metricas-federacion.md). Este documento no inventa la monitorización; la convierte en el plan documentado que una autoridad puede pedir.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

Se rellena **un plan por sistema clasificado de alto riesgo** (en Federation, el `pmmPlanRef` del descriptor apunta aquí y la comprobación 7 del gate lo exige). Para sistemas de riesgo limitado con criticidad de negocio alta, rellenarlo es opcional pero barato: las piezas ya operan.

**La tesis.** El art. 72 pide un sistema que recoja, documente y analice de forma activa y sistemática datos sobre el funcionamiento del sistema durante toda su vida, y que permita evaluar el cumplimiento continuo de los requisitos. Eso es, casi literalmente, lo que la Fase 5 de Federation monta: telemetría por `correlationId` ([CF-05](../../docs/federation/criterios-funcionales.md)), patrones A/B/C con cadencia modulada por criticidad, y métricas con umbrales. Lo que falta para el regulador es el **documento**: qué se monitoriza, con qué umbrales, quién revisa y qué dispara cada señal. Eso es esta plantilla.

**Quién la rellena.** La plataforma de federación (que opera la monitorización) redacta; el custodio del dominio y el custodio del Marco aprueban. En Adoption pura — sin telemetría programática — el plan se apoya en la revisión humana periódica del manifiesto §7, con honestidad sobre sus límites.

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Sistema / `agentId` cubierto | |
| Clase de riesgo y rol | *(de la `regulatoryClassification` / Marco §2.2)* |
| Versión del plan | *(p. ej. 1.0)* |
| Redacta | *(plataforma de federación)* |
| Aprueban | *(custodio de dominio + custodio del Marco)* |
| Evaluación de impacto asociada | *(referencia a la [evaluación](./evaluacion-impacto-ia.md) aprobada)* |
| Próxima revisión | *(YYYY-MM-DD)* |

---

## 1. Qué se monitoriza

*Pregunta guía: ¿qué señales del funcionamiento real del sistema se recogen de forma sistemática? Mapea a lo que ya existe: trazabilidad completa por `correlationId` y `decisionChain` (¿qué criterios se aplican de verdad?); tasa de escalado y su adecuación (métrica M3); tasa de bloqueo y excepción por policy (M6, Patrón B); coherencia entre agentes ante escenarios equivalentes (M2, Patrón C); firmas de cadena y su evolución (Patrón A). Añade las señales específicas del riesgo identificado en la evaluación de impacto: si el riesgo es sesgo contra un colectivo, ¿qué señal lo haría visible aquí?*

[Espacio para rellenar]

## 2. Umbrales y cadencia

*Pregunta guía: ¿con qué frecuencia se analiza cada señal y qué valor convierte una observación en hallazgo? La cadencia base la modula la criticidad (alta: ÷2 — [patrones de drift](../../docs/federation/patrones-deteccion-drift.md) §2.1); para un sistema de alto riesgo regulatorio, la cadencia mínima se fija aquí y no se relaja. Declara umbral y baseline por métrica: un plan sin umbrales es un dashboard, no un plan.*

| Señal / métrica | Baseline | Umbral de hallazgo | Cadencia de análisis | Analiza |
|---|---|---|---|---|
| *(p. ej. M3 — tasa de escalado adecuada)* | | *(p. ej. < 90 % de escalados apropiados)* | | *(plataforma)* |
| *(p. ej. M6 — excepciones sobre policy X)* | | | | |
| | | | | |

## 3. Qué dispara cada hallazgo

*Pregunta guía: cuando una señal cruza su umbral, ¿qué pasa y quién decide? Conecta con los mecanismos existentes: revisión formal de drift (ratificar Constitución / corregir comportamiento / enmendar policy), reclasificación de riesgo si el comportamiento real difiere del evaluado, actualización de la [evaluación de impacto](./evaluacion-impacto-ia.md), y — si el hallazgo revela daño o riesgo de daño a personas — entrada **inmediata** en el [runbook de incidentes graves](./runbook-incidentes-graves.md) con sus plazos regulatorios. Un hallazgo de monitorización que apunte a un incidente grave no espera a la siguiente revisión programada.*

[Espacio para rellenar]

## 4. Registro y evidencia

*Pregunta guía: ¿dónde quedan los análisis realizados (aunque no encuentren nada — la ausencia de hallazgos también es evidencia de que se monitorizó), los hallazgos y sus decisiones? ¿Qué exportaciones de auditoría ([CF-05](../../docs/federation/criterios-funcionales.md)) reproducen cada análisis? Retención según la [política de retención de evidencias](./politica-retencion-evidencias.md). Este registro alimenta la auditoría interna y la revisión por la dirección ([programa](./programa-auditoria-interna-aims.md)).*

[Espacio para rellenar]

---

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Parte del [área de cumplimiento](../../docs/compliance/README.md). Cubre el EU AI Act art. 72; en ISO/IEC 42001 materializa el seguimiento y medición (cl. 9.1) y la mejora continua (cl. 10) para el sistema cubierto. Mapeo completo en los puentes [EU AI Act](../../docs/compliance/puente-eu-ai-act.md) e [ISO 42001](../../docs/compliance/puente-iso42001.md).*
