<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion — Plantilla de Evaluación de Impacto de un Sistema de IA

**Versión 1.0**

*Plantilla unificada de evaluación de impacto con doble salida: la evaluación de impacto del sistema de IA que exige ISO/IEC 42001 (cláusula 6 y control A.5, en línea metodológica con ISO/IEC 42005) y, cuando la organización está obligada como deployer, la evaluación de impacto sobre derechos fundamentales (FRIA) del EU AI Act art. 27. Un solo ejercicio, dos evidencias.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

Se rellena **una evaluación por caso de uso de IA**, antes de su puesta en producción y siempre antes del alta de un agente clasificado como **alto riesgo** (en Federation, el `impactAssessmentRef` del descriptor debe apuntar a una evaluación **aprobada** — la comprobación 7 del [gate de coherencia](../../docs/federation/gobernanza-federada.md) lo verifica). Para casos de riesgo limitado, las secciones §1–§4 bastan como evaluación ISO; las §5–§7 se activan con el alto riesgo o cuando la FRIA es exigible.

**Quién la rellena.** El custodio del dominio que propone el caso de uso redacta; el custodio del Marco Regulatorio (legal/DPO) dirige las secciones de derechos y **aprueba**; si hay datos personales, la coordinación con la EIPD/DPIA del RGPD art. 35 es obligatoria — son ejercicios distintos pero comparten insumos, y duplicarlos sin coordinarlos produce incoherencias auditables.

**Cuándo se revisa.** Ante cualquier cambio sustancial del caso de uso: nuevo colectivo afectado, cambio del flujo de supervisión humana, cambio de proveedor o de modelo, reclasificación de riesgo. Una evaluación de impacto desactualizada es peor que ninguna: documenta una realidad que ya no existe.

> **FRIA — ¿estás obligado?** El art. 27 obliga a deployers que sean organismos de Derecho público o entidades privadas que prestan servicios públicos, y a deployers de ciertos sistemas de scoring crediticio y de seguros. Si la AI Office ha publicado plantilla oficial de FRIA, verificar su encaje (ver [calendario regulatorio](../../docs/compliance/appendix/calendario-regulatorio.md), lista de vigilancia). Aun sin obligación formal, las secciones §5–§7 son la diligencia debida que un caso de alto riesgo merece.

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Caso de uso evaluado | *(nombre; coherente con la clasificación del Marco Regulatorio §2.2)* |
| Asistente(s) o `agentId`(s) que lo materializan | |
| Clase de riesgo y rol | *(p. ej. alto riesgo — Anexo III / deployer)* |
| Versión de la evaluación | *(p. ej. 1.0)* |
| Redacta | *(custodio de dominio)* |
| Aprueba | *(custodio del Marco — legal/DPO)* |
| ¿FRIA exigible (art. 27)? | *(Sí / No — con la justificación en §5)* |
| ¿EIPD/DPIA (RGPD art. 35) asociada? | *(referencia al documento, si existe)* |
| Estado | *(borrador / en revisión / **aprobada** / desactualizada)* |
| Próxima revisión | *(YYYY-MM-DD o disparadores)* |

---

## 1. Descripción del sistema y su contexto

*Pregunta guía: ¿qué hace el sistema, sobre qué datos, con qué modelo/producto subyacente y dentro de qué proceso de negocio? ¿Cuál es el propósito previsto y qué quedaría fuera de propósito? Describe el flujo completo: entrada → procesamiento → output → quién actúa sobre el output. En Federation, referencia el descriptor del agente y el corredor donde opera.*

[Espacio para rellenar]

## 2. Partes afectadas

*Pregunta guía: ¿quién recibe el impacto de este sistema, directa o indirectamente? Empleados cuyos casos procesa, clientes que reciben sus outputs, candidatos, pacientes, terceros mencionados en los datos. Para cada colectivo: ¿qué decisión o resultado les afecta y con qué severidad y reversibilidad? Los colectivos vulnerables (menores, personas en situación de exclusión) se identifican explícitamente.*

[Espacio para rellenar]

## 3. Beneficios e impactos potenciales

*Pregunta guía: ¿qué beneficio justifica el sistema y qué puede salir mal? Para cada impacto potencial negativo: plausibilidad, severidad, reversibilidad y a quién golpea. Considera al menos: error del modelo (alucinación, falso positivo/negativo), sesgo contra colectivos, opacidad de la decisión, dependencia excesiva del operador humano (automation bias), uso fuera de propósito, y exposición de datos. El criterio de honestidad del ecosistema aplica: un riesgo no escrito aquí es un riesgo que nadie va a mitigar.*

[Espacio para rellenar]

## 4. Medidas de mitigación y gobernanza

*Pregunta guía: para cada impacto de §3, ¿qué medida lo mitiga y dónde está materializada? Mapea a los artefactos Myrmion existentes: restricciones del Marco (§5 de su plantilla), escalado de la Constitución, des-identificación ([guía de protección de datos](../../docs/adoption/guia-proteccion-datos.md) o [CF-06](../../docs/federation/criterios-funcionales.md) en ruta), policies del corredor, supervisión humana concreta (¿quién revisa qué, antes de qué?). Una mitigación sin artefacto que la materialice es una intención, no una medida. ¿Qué riesgo residual queda y quién lo acepta formalmente?*

[Espacio para rellenar]

## 5. FRIA — aplicabilidad y proceso afectado

*Obligatoria si el caso es de alto riesgo o la FRIA es exigible. Pregunta guía: ¿por qué está (o no está) la organización obligada por el art. 27? Si lo está: describe los procesos en los que el sistema se usará, el periodo y la frecuencia de uso, y las categorías de personas físicas y colectivos afectados — el contenido mínimo que el artículo exige.*

[Espacio para rellenar]

## 6. FRIA — riesgos para derechos fundamentales

*Pregunta guía: ¿qué derechos pueden verse afectados y cómo? Recorre al menos: no discriminación (¿el sistema puede tratar peor a un colectivo protegido?), protección de datos y vida privada, tutela efectiva (¿puede la persona entender y recurrir la decisión?), derechos laborales si afecta a trabajadores, e interés superior del menor si aplica. Para cada riesgo identificado: probabilidad, severidad y a qué colectivo de §2 afecta.*

[Espacio para rellenar]

## 7. FRIA — medidas de supervisión humana y reclamación

*Pregunta guía: ¿qué medidas de supervisión humana gobiernan el sistema (quién, con qué competencia — coherente con el [plan de alfabetización](./plan-alfabetizacion-ia.md) — y con qué autoridad para ignorar o revertir el output)? ¿Qué medidas se toman si los riesgos de §6 se materializan — incluida la ruta interna de reclamación y el deber de informar a la autoridad de vigilancia ([runbook de incidentes graves](./runbook-incidentes-graves.md))? Si la FRIA es exigible, recuerda la notificación de sus resultados a la autoridad de vigilancia del mercado.*

[Espacio para rellenar]

## 8. Conclusión y aprobación

*Pregunta guía: ¿procede el caso de uso? Tres salidas posibles: **aprobado** (con las medidas de §4/§7 como condición), **aprobado con restricciones** (alcance reducido, supervisión reforzada — enumerarlas) o **no aprobado** (el riesgo residual no es aceptable; el caso no entra en producción). La firma del custodio del Marco es la que convierte este documento en la evidencia que `impactAssessmentRef` referencia.*

[Espacio para rellenar]

---

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Parte del [área de cumplimiento](../../docs/compliance/README.md). Cubre la evaluación de impacto de ISO/IEC 42001 (cl. 6 / control A.5, en línea con ISO/IEC 42005) y la FRIA del EU AI Act art. 27. No sustituye a la EIPD/DPIA del RGPD art. 35: se coordinan. Mapeo completo en los puentes [ISO 42001](../../docs/compliance/puente-iso42001.md) y [EU AI Act](../../docs/compliance/puente-eu-ai-act.md).*
