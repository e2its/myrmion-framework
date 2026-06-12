<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion — Plantilla de Ficha de Transparencia de IA

**Versión 1.0**

*Plantilla para declarar, por cada asistente o agente, cómo se cumplen las obligaciones de transparencia frente a las personas: aviso de interacción con IA, marcado de contenido sintético e instrucciones de uso. Materializa el EU AI Act art. 50 (y el art. 13 cuando el sistema es de alto riesgo) y el control A.8 de ISO/IEC 42001 (información a partes interesadas).*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

Se rellena **una ficha por asistente** (Myrmion Adoption) **o por agente** (Myrmion Federation) que interactúe con personas, genere contenido o tome decisiones que afecten a personas. En Federation, la ficha se referencia desde el [descriptor de identidad del agente](../federation/descriptor-agente.md) (campo `regulatoryClassification.transparencyRef`) y su existencia la verifica el [gate de coherencia](../../docs/federation/gobernanza-federada.md) cuando el agente la requiere.

**Quién la rellena.** El custodio de la capa departamental que modela el asistente redacta; el custodio del Marco Regulatorio (legal/DPO) **revisa y aprueba** — la transparencia es obligación de la Capa 1, no una cortesía cultural.

**Cuándo.** Antes de que el asistente entre en producción, y se revisa cuando cambia su propósito, su audiencia o el tipo de contenido que genera. Las fechas de aplicabilidad de cada obligación viven en el [calendario regulatorio](../../docs/compliance/appendix/calendario-regulatorio.md) — verificarlas antes de aprobar la ficha.

**Doble función.** Para sistemas de riesgo limitado, esta ficha cubre la transparencia del art. 50. Para sistemas de **alto riesgo**, cubre además la base de las *instrucciones de uso* del art. 13 que el deployer necesita para operar el sistema conforme — la sección §5 es obligatoria en ese caso.

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Asistente o `agentId` al que aplica | *(nombre del asistente o `urn:myrmion:agent:<org>:<dominio>:<nombre>`)* |
| Framework de origen | *(Adoption / Federation)* |
| Clasificación regulatoria del sistema | *(riesgo limitado / alto riesgo / mínimo — coherente con el Marco Regulatorio §2.2)* |
| Versión de la ficha | *(p. ej. 1.0)* |
| Fecha de aprobación | *(YYYY-MM-DD)* |
| Redacta (custodio de capa departamental) | *(rol o persona)* |
| Aprueba (custodio del Marco Regulatorio) | *(rol o persona — legal/DPO)* |
| Próxima revisión | *(YYYY-MM-DD, o «ad hoc al cambiar propósito/audiencia»)* |

---

## 1. Identificación del sistema

*Pregunta guía: ¿qué es este asistente, para qué existe y quién lo usa? Declara el propósito previsto con la precisión suficiente para que un tercero entienda qué hace y qué NO hace. Incluye el producto comercial o modelo subyacente y la vía de aprovisionamiento (coherente con la matriz de licenciamiento del [Marco Regulatorio](../adoption/marco-regulatorio.md) §3).*

[Espacio para rellenar]

## 2. Aviso de interacción con IA

*Pregunta guía: cuando una persona interactúa con este asistente, ¿cómo sabe que está interactuando con una IA? El aviso debe producirse de forma clara y a más tardar en la primera interacción. Describe dónde aparece (interfaz, firma, cabecera), con qué texto, y en qué idiomas. Si consideras que es «obvio por el contexto» para una persona razonablemente informada — la excepción que la norma admite — justifícalo por escrito aquí: la justificación es la evidencia.*

[Espacio para rellenar]

## 3. Marcado de contenido sintético

*Pregunta guía: ¿qué tipos de contenido genera este sistema (texto, imagen, audio, vídeo) y cómo se marca como generado o manipulado artificialmente, en formato legible por máquina? Atención a una confusión frecuente: la revisión editorial humana **no exime del marcado legible por máquina** — las excepciones de esta obligación son otras (función de asistencia o edición estándar que no altera sustancialmente la entrada); la excepción de revisión humana con responsabilidad editorial pertenece a la divulgación de texto publicado, que se declara en §4. Aquí declara el mecanismo de marcado, sus excepciones aplicables justificadas, y quién verifica que opera. Los formatos técnicos de marcado aceptados evolucionan: verificar el [calendario regulatorio](../../docs/compliance/appendix/calendario-regulatorio.md).*

[Espacio para rellenar]

## 4. Contenido publicado al exterior

*Pregunta guía: ¿puede el contenido de este asistente llegar a publicarse hacia fuera de la organización (web, redes, comunicaciones a clientes)? Si genera o manipula contenido que podría constituir ultrafalsificación (deep fake) o texto publicado con fines de información al público, ¿cómo se divulga visiblemente su origen artificial? Es **aquí** — y solo aquí — donde aplica la excepción de revisión humana con responsabilidad editorial sobre el texto publicado: si la organización la invoca, declara el flujo (quién revisa, quién asume la responsabilidad editorial, cómo queda registrado) y qué pasa con el contenido que se publica sin pasar por él. En Federation, relaciona esta sección con las capabilities que declaran `externalizes: true` en el descriptor.*

[Espacio para rellenar]

## 5. Instrucciones de uso y limitaciones

*Obligatoria si el sistema es de alto riesgo (alimenta las instrucciones de uso del art. 13); recomendada para todos. Pregunta guía: ¿qué necesita saber quien opera este asistente para usarlo correctamente? Declara: el propósito previsto y los usos fuera de propósito; las limitaciones conocidas (tipos de pregunta donde se equivoca, datos sobre los que no debe usarse); el nivel de precisión esperable y cómo se midió; las medidas de supervisión humana previstas (¿cuándo escala? — coherente con la sección de Escalado de la [Constitución Corporativa](../adoption/constitucion-corporativa.md)); y el mal uso razonablemente previsible.*

[Espacio para rellenar]

## 6. Canal para partes interesadas

*Pregunta guía: si una persona afectada por un output de este asistente quiere preguntar, reclamar o pedir explicación de una decisión, ¿qué canal tiene y quién responde? Para sistemas de alto riesgo, recuerda el derecho a explicación de decisiones individuales (art. 86). El canal debe existir de verdad — un buzón que nadie lee no es un canal, es un riesgo documentado.*

[Espacio para rellenar]

## 7. Verificación y evidencia

*Pregunta guía: ¿cómo demuestras que lo declarado arriba es lo que ocurre en producción? Lista las evidencias: capturas o configuración del aviso de IA, ejemplo de contenido marcado, registro de revisiones editoriales, logs. En Federation, la trazabilidad por `correlationId` permite demostrar qué avisos y marcados acompañaron a cada cadena — referencia aquí las consultas de exportación de auditoría ([CF-05](../../docs/federation/criterios-funcionales.md)). ¿Con qué cadencia se re-verifica esta ficha contra el comportamiento real?*

[Espacio para rellenar]

---

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Parte del [área de cumplimiento](../../docs/compliance/README.md). Cubre el EU AI Act arts. 50/13 y el control A.8 de ISO/IEC 42001 — el mapeo completo está en los puentes [EU AI Act](../../docs/compliance/puente-eu-ai-act.md) e [ISO 42001](../../docs/compliance/puente-iso42001.md). Las obligaciones declaradas aquí pertenecen a la Capa 1 ([Marco Regulatorio](../adoption/marco-regulatorio.md)): no admiten excepción.*
