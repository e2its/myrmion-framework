<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion — Plantilla del Programa de Auditoría Interna y Revisión por la Dirección (AIMS)

**Versión 1.0**

*Plantilla para las dos piezas de la cláusula 9 de ISO/IEC 42001 que ningún otro artefacto del ecosistema cubre: el programa de auditoría interna del AIMS (cl. 9.2) y la revisión por la dirección (cl. 9.3). El gate, el drift y las métricas son **controles**; esto es el proceso que los audita.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

**La distinción que importa.** Myrmion genera evidencia continuamente — cadenas trazables, gates reproducibles, registros de excepciones. Pero ISO 42001 exige además que alguien, con independencia de quien opera, compruebe periódicamente que el sistema de gestión funciona conforme a lo declarado, y que la dirección revise los resultados y decida. Sin estas dos piezas, el mejor AIMS operativo no certifica.

**Quién la rellena.** El responsable del AIMS define el programa; los auditores internos deben ser **independientes de lo auditado** (quien opera la plataforma no audita la plataforma; en organizaciones pequeñas, auditoría cruzada entre custodios o apoyo externo). La revisión por la dirección la preside el órgano que aprobó el Marco y la Constitución.

**La ventaja Myrmion.** Auditar un AIMS suele ser caro porque la evidencia hay que excavarla. Aquí no: las exportaciones de auditoría de [CF-05](../../docs/federation/criterios-funcionales.md) reproducen cadenas por `correlationId`, excepciones por periodo y resultados de gate bajo demanda, y la reproducibilidad del gate permite re-verificar cualquier alta. El programa debe explotar eso: menos entrevistas, más re-ejecución de evidencia.

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Alcance del AIMS | *(coherente con la [SoA](./declaracion-aplicabilidad-iso42001.md) §0)* |
| Versión del programa | *(p. ej. 1.0)* |
| Responsable del AIMS | |
| Auditores internos designados (y de qué son independientes) | |
| Órgano de la revisión por la dirección | |
| Aprobación y vigencia | *(YYYY-MM-DD; programa anual)* |

---

## 1. Programa anual de auditoría (cl. 9.2)

*Pregunta guía: ¿qué se audita, cuándo, contra qué criterios y por quién? El ciclo completo del AIMS debe cubrirse dentro del periodo de certificación; los dominios de criticidad alta, con más frecuencia. Criterios de auditoría: las cláusulas 4–10, la SoA, y los propios artefactos Myrmion declarados (¿se cumple lo que el Marco, la Constitución y los runbooks dicen?).*

| Auditoría | Alcance / proceso auditado | Criterios | Auditor | Fecha prevista | Estado |
|---|---|---|---|---|---|
| *(p. ej. A-2026-01)* | *(gobernanza de capas: custodia, revisiones, versionado)* | *(cl. 5, 7.5; A.2–A.3)* | | | |
| *(p. ej. A-2026-02)* | *(gate de coherencia y ciclo de vida de agentes)* | *(cl. 8; A.6; gobernanza §2)* | | | |
| *(p. ej. A-2026-03)* | *(excepciones, incidentes y drift)* | *(cl. 9.1, 10; runbook de incidentes; patrones A/B/C)* | | | |
| *(p. ej. A-2026-04)* | *(datos: de-id, licenciamiento, retención)* | *(A.7, A.10; política de retención)* | | | |

## 2. Método: auditar sobre evidencia reproducible

*Pregunta guía: para cada auditoría, ¿qué evidencia se re-ejecuta en lugar de preguntarse? Ejemplos del método Myrmion: muestrear N `correlationId` del periodo y reconstruir sus cadenas completas (¿la `decisionChain` registra los `criteriaApplied` esperados?); re-ejecutar el gate sobre M descriptores activos (¿reproduce el mismo `status`?); cruzar el registro de excepciones con su caducidad (¿hay excepciones vencidas aún activas?); verificar que toda alta del periodo tiene su comprobación 7 con clasificación aprobada; comprobar el registro de formación contra las incorporaciones del periodo. Documenta qué exportaciones de auditoría usa cada prueba.*

[Espacio para rellenar]

## 3. Informe, no conformidades y seguimiento

*Pregunta guía: ¿qué formato tiene el informe (hallazgos clasificados: no conformidad mayor / menor / observación / oportunidad), quién recibe cada hallazgo (el custodio del área afectada), qué plazos tiene la acción correctiva y quién verifica su cierre? Una no conformidad sobre el Marco Regulatorio se trata con la severidad de lo que es: posible incumplimiento regulatorio — conecta con el [runbook de incidentes](./runbook-incidentes-graves.md) si procede.*

[Espacio para rellenar]

## 4. Revisión por la dirección (cl. 9.3)

*Pregunta guía: ¿con qué cadencia (mínimo anual; semestral recomendado mientras el AIMS madura) y con qué orden del día? Entradas mínimas — casi todas salen de la maquinaria existente: estado de acciones de revisiones previas; cambios externos e internos relevantes (el [calendario regulatorio](../../docs/compliance/appendix/calendario-regulatorio.md) alimenta esta entrada); desempeño — M1–M6 contra umbrales, resultados de los patrones de drift, tasa y tendencia de excepciones, incidentes del periodo con su tratamiento, resultados de auditorías internas, estado de la SoA; adecuación de recursos; oportunidades de mejora. Salidas: decisiones documentadas — cambios al AIMS, a las capas, a los recursos, a los umbrales — con responsable y plazo.*

[Espacio para rellenar]

## 5. Registro

*Pregunta guía: ¿dónde quedan los informes de auditoría, las actas de revisión por la dirección y el seguimiento de acciones? Retención según la [política de retención de evidencias](./politica-retencion-evidencias.md); son de los primeros documentos que un auditor de certificación pide.*

[Espacio para rellenar]

---

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Parte del [área de cumplimiento](../../docs/compliance/README.md). Cubre ISO/IEC 42001 cl. 9.2–9.3; en el EU AI Act, alimenta el QMS del art. 17 cuando la organización actúa como proveedor. Mapeo completo en el [puente ISO 42001](../../docs/compliance/puente-iso42001.md).*
