<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion — Plantilla del Plan de Alfabetización en IA

**Versión 1.0**

*Plantilla para articular el plan de competencia y concienciación en IA de la organización: quién necesita saber qué, cómo se forma y cómo se evidencia. Materializa el EU AI Act art. 4 (alfabetización en IA, exigible a proveedores y deployers) y las cláusulas 7.2 (competencia) y 7.3 (concienciación) de ISO/IEC 42001.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

El art. 4 del EU AI Act obliga a adoptar medidas para garantizar un nivel suficiente de alfabetización en IA del personal — y de cualquier persona que opere sistemas de IA en nombre de la organización — teniendo en cuenta sus conocimientos, su experiencia y el contexto de uso. Es una de las obligaciones de aplicación más temprana del Reglamento (ver [calendario regulatorio](../../docs/compliance/appendix/calendario-regulatorio.md)) y, a la vez, la materia de las cláusulas 7.2–7.3 de ISO/IEC 42001: un solo plan sirve a ambas.

**Quién la rellena.** La función de transformación digital (custodia de la Constitución) coordina y redacta; el custodio del Marco Regulatorio fija el mínimo no negociable (qué debe saber todo el mundo para no incumplir); cada departamento aporta las competencias específicas de su capa.

**El principio.** Myrmion ya produce el *contenido* de la alfabetización: la [Constitución Corporativa](../adoption/constitucion-corporativa.md) (voz, principios, restricciones, escalado), el [Marco Regulatorio](../adoption/marco-regulatorio.md) (qué datos y usos están vetados) y las capas departamentales. Este plan no inventa temario: organiza quién debe interiorizar qué artefacto, con qué profundidad y con qué evidencia. Formar en IA «en general», desconectado del Marco de Modelado, es exactamente el tipo de formación que se olvida en dos semanas.

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Versión del plan | *(p. ej. 1.0)* |
| Fecha de aprobación | *(YYYY-MM-DD)* |
| Coordina | *(rol — típicamente transformación digital)* |
| Fija el mínimo regulatorio | *(rol — custodio del Marco: legal/DPO)* |
| Aprobación formal | *(órgano — p. ej. Comité de Dirección)* |
| Próxima revisión | *(anual como mínimo; ad hoc ante producto, capa o regulación nueva)* |

---

## 1. Colectivos alcanzados

*Pregunta guía: ¿quién opera o usa IA en nombre de tu organización? No solo empleados: incluye contratistas, externos y proveedores que actúan por cuenta de la organización. Enumera los colectivos con su tamaño aproximado y su relación con la IA. Colectivos típicos en una adopción Myrmion: usuarios de asistentes departamentales; modeladores de capas departamentales; custodios (Marco, Constitución, capas y — en Federation — plataforma); dirección; y personal que opera sistemas clasificados de alto riesgo, si existen.*

[Espacio para rellenar]

## 2. Matriz de competencias por colectivo

*Pregunta guía: para cada colectivo de §1, ¿qué debe saber y dónde está ya escrito? Mapea cada competencia al artefacto Myrmion que la contiene — la formación es la interiorización del Marco de Modelado, no un curso genérico. La fila del mínimo regulatorio (todo el mundo) la define el custodio del Marco y no se negocia.*

| Colectivo | Qué debe dominar | Artefacto fuente | Profundidad |
|---|---|---|---|
| Todos los usuarios | Qué datos nunca se pegan en un asistente; cuándo escalar a humano; que el output es asistencia, no decisión | [Marco Regulatorio](../adoption/marco-regulatorio.md) §5 · Constitución §Escalado | *(sesión base + recordatorio periódico)* |
| Modeladores de capa | Jerarquía de capas, revisión de coherencia, gestión de excepciones | [Manifiesto Adoption](../../docs/adoption/manifesto.md) §3–§4 | |
| Custodios | Su RACI completo; en Federation, gate, excepciones y drift | [Gobernanza federada](../../docs/federation/gobernanza-federada.md) | |
| Operadores de sistemas de alto riesgo *(si aplica)* | Instrucciones de uso, supervisión humana, deber de informar incidentes | [Ficha de transparencia](./ficha-transparencia-ia.md) §5 · [runbook de incidentes](./runbook-incidentes-graves.md) | |
| *(añadir colectivos propios)* | | | |

## 3. Itinerarios y cadencia

*Pregunta guía: ¿cómo se entrega cada itinerario (sesión, e-learning, material de autoconsulta, shadowing) y con qué cadencia se refresca? Declara el itinerario de incorporación: ninguna persona nueva opera un asistente con datos reales antes de completar el mínimo de su colectivo. ¿Qué dispara formación ad hoc — un producto nuevo, una capa departamental nueva, un cambio del Marco Regulatorio, un incidente?*

[Espacio para rellenar]

## 4. Registro y evidencia

*Pregunta guía: ¿dónde queda registrado quién completó qué formación y cuándo? El registro es la evidencia ante el art. 4 y ante la cláusula 7.2 (ISO exige conservar «información documentada apropiada como evidencia de la competencia»). Declara: el sistema de registro, el responsable de mantenerlo, y el plazo de retención (coherente con la [política de retención de evidencias](./politica-retencion-evidencias.md)).*

[Espacio para rellenar]

## 5. Medición de eficacia

*Pregunta guía: ¿cómo sabes que la alfabetización funciona, más allá de la asistencia a sesiones? Myrmion ya mide los síntomas de su ausencia: una tasa de escalado inadecuada (métrica M3), excepciones recurrentes por desconocimiento (Patrón B de [drift](../../docs/federation/patrones-deteccion-drift.md)) o incidentes causados por uso indebido apuntan a colectivos con formación insuficiente. Declara qué señales revisas, con qué cadencia y quién decide reforzar qué itinerario.*

[Espacio para rellenar]

---

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Parte del [área de cumplimiento](../../docs/compliance/README.md). Cubre el EU AI Act art. 4 y las cláusulas 7.2–7.3 de ISO/IEC 42001 — mapeo completo en los puentes [EU AI Act](../../docs/compliance/puente-eu-ai-act.md) e [ISO 42001](../../docs/compliance/puente-iso42001.md).*
