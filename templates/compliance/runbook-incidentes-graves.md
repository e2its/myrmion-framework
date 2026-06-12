<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion — Runbook de Incidentes Graves de IA

**Versión 1.0**

*Plantilla operativa para clasificar, tratar y — cuando proceda — notificar a la autoridad los incidentes relacionados con sistemas de IA. Extiende la alerta al custodio del Marco que la [gobernanza federada](../../docs/federation/gobernanza-federada.md) §3 ya dispara, hasta el procedimiento regulatorio completo: el EU AI Act art. 73 (incidentes graves) y su conexión con la notificación de brechas del RGPD arts. 33–34.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

Myrmion ya genera las **señales** de incidente: el intento de excepción a una policy derivada del Marco Regulatorio es una alerta automática (no una excepción), un intento de federar un caso prohibido dispara la comprobación 7 del gate, y los patrones de drift señalan desviaciones. Lo que este runbook añade es lo que pasa **después de la señal**: la clasificación de severidad, los responsables, los plazos — incluidos los regulatorios, que no esperan — y el registro.

**Quién la rellena.** El custodio del Marco Regulatorio (legal/DPO) es la autoridad del procedimiento; la plataforma de federación (si existe) opera la detección y aporta la evidencia técnica; cada custodio de dominio responde por la contención en su dominio.

**El principio que no se negocia.** Los plazos de notificación a la autoridad son **regulatorios, no internos**: el reloj corre desde que la organización establece el vínculo entre el sistema de IA y el incidente, no desde que termina la investigación. Notificar con información incompleta y completar después es el comportamiento correcto; callar mientras se investiga no lo es.

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Versión del runbook | *(p. ej. 1.0)* |
| Autoridad del procedimiento | *(custodio del Marco — legal/DPO)* |
| Opera la detección y evidencia | *(plataforma de federación / IT)* |
| Autoridad(es) de vigilancia competente(s) | *(autoridad nacional de vigilancia del AI Act; AEPD u homóloga para brechas de datos; sectorial si aplica)* |
| Aprobación formal | *(órgano)* |
| Próxima revisión / simulacro | *(YYYY-MM-DD — un runbook de incidentes sin simulacro es papel)* |

---

## 1. Qué es un incidente aquí

*Pregunta guía: ¿qué eventos entran en este procedimiento? Como mínimo: (a) **incidente grave** en el sentido del art. 73 — fallecimiento o daño grave a la salud de una persona, alteración grave e irreversible de la gestión de infraestructura crítica, incumplimiento de obligaciones de protección de derechos fundamentales, o daño grave a la propiedad o al medio ambiente, vinculado a un sistema de IA; (b) **violación del Marco Regulatorio** — incluido el intento de excepción a una policy de Marco y el intento de alta de un caso prohibido; (c) **brecha de datos personales** que involucre a un sistema de IA (conecta con RGPD arts. 33–34); (d) **mal funcionamiento con afectación a personas** que no llegue a (a) pero merezca registro. Define los umbrales con ejemplos del propio dominio.*

[Espacio para rellenar]

## 2. Clasificación de severidad y plazos

*Pregunta guía: ¿quién clasifica, en cuánto tiempo desde la señal, y con qué consecuencia? La tabla siguiente fija los plazos regulatorios del art. 73 para sistemas de alto riesgo; añade los internos. Verificar los plazos vigentes y las guías de la Comisión en el [calendario regulatorio](../../docs/compliance/appendix/calendario-regulatorio.md) antes de aprobar este runbook.*

| Severidad | Definición | Plazo de notificación a la autoridad | Notifica |
|---|---|---|---|
| **Crítica** | Infracción generalizada o incidente grave en infraestructura crítica | **≤ 2 días** desde el vínculo IA–incidente | *(rol)* |
| **Mayor — fallecimiento** | Incidente grave con fallecimiento de una persona | **≤ 10 días** | |
| **Mayor** | Resto de incidentes graves del art. 73 | **≤ 15 días** | |
| **Brecha de datos** | Violación de seguridad con datos personales | **≤ 72 h** a la autoridad de protección de datos (RGPD art. 33); a los interesados sin dilación indebida si alto riesgo para sus derechos (art. 34) | |
| **Interna** | Violación de Marco sin daño externo; señal de drift grave | *(plazo interno — sin notificación externa salvo escalada)* | |

*Nota: como deployer, el deber típico es informar **al proveedor** del sistema sin demora (y a la autoridad si el proveedor no es localizable o el deployer causó el incidente); como proveedor, la notificación a la autoridad es propia. El rol viene de la `regulatoryClassification` del descriptor o de la clasificación del Marco §2.2.*

## 3. Procedimiento

*Pregunta guía: ¿cuál es la secuencia desde la señal hasta el cierre? Como mínimo: (1) **detección y registro** — toda señal entra con su `correlationId` si procede de la federación: la cadena de decisiones completa es la primera evidencia; (2) **contención** — qué se detiene (¿se marca el agente `deprecated`? ¿se desactiva el asistente? ¿quién puede pararlo y en cuánto tiempo?); (3) **clasificación** según §2, por la autoridad del procedimiento; (4) **notificación** — proveedor, autoridad(es), interesados, según rol y severidad; (5) **investigación** — causa raíz con la evidencia de la telemetría ([CF-05](../../docs/federation/criterios-funcionales.md)); (6) **remediación y cierre** — incluida la actualización de la evaluación de impacto, las policies o la Constitución si el incidente revela un hueco; (7) **lección registrada** — alimenta la revisión por la dirección ([programa de auditoría](./programa-auditoria-interna-aims.md)).*

[Espacio para rellenar]

## 4. Registro de incidentes

*Pregunta guía: ¿dónde queda cada incidente y con qué campos mínimos? Propuesta: identificador, fecha de señal y de vínculo IA–incidente, sistema/`agentId`, severidad, `correlationId`(s) afectados, descripción, colectivos afectados, notificaciones realizadas (a quién, cuándo, referencia), causa raíz, remediación, estado, cierre. El registro se conserva según la [política de retención de evidencias](./politica-retencion-evidencias.md) y es insumo directo de la auditoría interna y de la revisión por la dirección.*

[Espacio para rellenar]

## 5. Contactos y escalado

*Pregunta guía: ¿a quién se llama, en qué orden, con qué datos de contacto verificados? Autoridad del procedimiento, sustituto, dirección, comunicación (si el incidente trasciende), proveedor del sistema (el contacto de incidentes del DPA/contrato — verificar que existe **antes** del primer incidente), autoridad de vigilancia. Incluye el canal fuera de horario.*

[Espacio para rellenar]

---

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Parte del [área de cumplimiento](../../docs/compliance/README.md). Cubre el EU AI Act art. 73 y su conexión con RGPD arts. 33–34; en ISO/IEC 42001 alimenta la mejora continua (cl. 10) y la revisión por la dirección (cl. 9.3). La frontera con la gestión de excepciones es nítida: una excepción a la Constitución se gestiona ([registro de excepciones](../federation/registro-excepciones.md)); una violación del Marco se trata aquí.*
