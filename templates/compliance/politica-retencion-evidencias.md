<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion — Plantilla de Política de Retención de Evidencias de IA

**Versión 1.0**

*Plantilla para fijar cuánto tiempo se conserva cada tipo de evidencia que el ecosistema genera — logs, cadenas de decisión, registros de excepciones, documentación de gobernanza — y cómo se concilia esa retención con la minimización y el derecho de supresión del RGPD. El corpus define **qué** se traza; esta política fija **cuánto tiempo** y **cómo se borra**.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

La rellena el custodio del Marco Regulatorio (los plazos son obligaciones de Capa 1) con la plataforma de federación (que opera el almacenamiento). Los plazos concretos del EU AI Act dependen del rol y de la clase de riesgo — verificar vigencia en el [calendario regulatorio](../../docs/compliance/appendix/calendario-regulatorio.md). La tensión central que esta política resuelve por escrito: **la trazabilidad pide conservar; la minimización pide borrar**. La respuesta de Myrmion ya está medio construida — el bloque de contexto cultural nunca transporta PII en claro (`originatingUserRef` es un seudónimo opaco; los `deidTokens` son punteros a vault, no valores) — pero la política debe declarar el resto.

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Versión | *(p. ej. 1.0)* |
| Custodio | *(custodio del Marco — legal/DPO)* |
| Opera el almacenamiento | *(plataforma de federación / IT)* |
| Aprobación formal | *(órgano)* |
| Próxima revisión | *(anual; ad hoc ante cambio regulatorio o contractual)* |

---

## 1. Inventario de evidencias y plazos

*Pregunta guía: para cada tipo de evidencia, ¿qué plazo manda — el regulatorio mínimo, el contractual o el de prescripción de responsabilidad — y cuál se adopta? Mínimos típicos del EU AI Act a verificar: **logs generados automáticamente por sistemas de alto riesgo: al menos 6 meses** en poder del deployer (art. 26.6) y según corresponda al proveedor (art. 19); **documentación técnica, del QMS y de evaluación de conformidad del proveedor: 10 años** desde la introducción en el mercado (art. 18). Los documentos de gobernanza versionados (Marco, Constitución, capas, descriptores, ADRs) se conservan mientras existan cadenas de decisión que los referencien por hash — borrar una versión de la Constitución que una cadena histórica referencia rompe la trazabilidad de criterio (métrica M4).*

| Tipo de evidencia | Origen | Plazo regulatorio mínimo | Plazo adoptado | Soporte y responsable |
|---|---|---|---|---|
| Logs / spans de cadenas (`correlationId`, `decisionChain`) | CF-05 | *(p. ej. ≥ 6 meses si alto riesgo, deployer)* | | |
| Registro de excepciones | [Plantilla](../federation/registro-excepciones.md) | | | |
| Resultados del gate de coherencia (`coherenceReview`) | Registry | | | |
| Registro de incidentes y notificaciones | [Runbook](./runbook-incidentes-graves.md) | | | |
| Análisis de monitorización post-comercialización | [Plan PMM](./plan-monitorizacion-post-mercado.md) | | | |
| Evaluaciones de impacto y FRIA | [Plantilla](./evaluacion-impacto-ia.md) | | | |
| Documentos de gobernanza versionados (con hash) | Repositorio de gobernanza | *(mientras haya cadenas que los referencien)* | | |
| Registro de formación (alfabetización) | [Plan](./plan-alfabetizacion-ia.md) | | | |
| Vault de des-identificación (`deidTokens`) | CF-06 | *(TTL corto — es el dato sensible, no evidencia)* | | |

## 2. Derecho de supresión y minimización

*Pregunta guía: si un interesado ejerce su derecho de supresión (RGPD art. 17), ¿qué pasa con la telemetría? Declara la posición de la organización por escrito — es la pregunta que un auditor de protección de datos hará primero. La arquitectura de Myrmion permite una respuesta limpia: la PII vive en el vault de des-identificación (borrable selectivamente: eliminar la entrada del vault convierte el `deidToken` de las cadenas históricas en un puntero irreversiblemente huérfano), mientras la cadena de decisiones — seudonimizada por construcción — puede conservarse como evidencia de cumplimiento. Documenta: el procedimiento de supresión selectiva, los casos en que la retención prevalece por obligación legal (y su base jurídica), y cómo se verifica que ningún dato en claro se coló en logs fuera de la ruta gobernada.*

[Espacio para rellenar]

## 3. Eliminación al vencer el plazo

*Pregunta guía: ¿cómo se borra lo que vence — proceso, periodicidad, verificación y registro de la eliminación? La eliminación también deja rastro: qué se eliminó, cuándo, bajo qué regla de esta política. ¿Y los backups? Un plazo de retención que los backups incumplen silenciosamente no es una política, es una intención.*

[Espacio para rellenar]

---

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Parte del [área de cumplimiento](../../docs/compliance/README.md). Cubre los plazos de los arts. 12/18/19/26.6 del EU AI Act y la conciliación con RGPD arts. 5(1)(e) y 17; en ISO/IEC 42001, materializa el control de información documentada (cl. 7.5) sobre la evidencia operativa. Complementa la [Guía de protección de datos](../../docs/adoption/guia-proteccion-datos.md).*
