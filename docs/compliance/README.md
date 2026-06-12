# Myrmion — Área de cumplimiento (ISO/IEC 42001 · EU AI Act)

**Versión 1.0**

*Capa transversal de evidencia de cumplimiento del ecosistema Myrmion. No es un cuarto framework: es el puente entre los artefactos que [Adoption](../adoption/manifesto.md) y [Federation](../federation/manifesto.md) ya producen y lo que un certificador ISO/IEC 42001 o una autoridad de vigilancia del EU AI Act van a pedir.*

---

## 1. Qué es esta área y qué no es

**Qué es.** El conjunto de documentos puente y plantillas que permiten a una organización adoptante de Myrmion **demostrar** cumplimiento: mapeos de los artefactos del ecosistema a las cláusulas y controles de ISO/IEC 42001 y a las obligaciones del EU AI Act, más las plantillas que cubren las obligaciones que los frameworks no producían por sí solos (transparencia, alfabetización, evaluación de impacto, incidentes graves, monitorización post-comercialización, retención de evidencias, auditoría interna).

**Qué no es.** Tres límites, declarados con la honestidad habitual del ecosistema:

- **No sustituye a las normas.** ISO/IEC 42001 define *qué* debe existir en un sistema de gestión de IA; el EU AI Act define *qué* está prohibido y *qué* obligaciones tiene cada rol. Myrmion define *cómo* se operacionaliza la cultura y la gobernanza — y, con esta área, *cómo se evidencia*. La relación es aditiva, como declara el [manifiesto paraguas](../manifesto.md).
- **No otorga presunción de conformidad.** Certificarse en ISO/IEC 42001 **no** activa la presunción de conformidad del art. 40 del EU AI Act; esa función la tendrán las normas armonizadas europeas cuando se citen en el DOUE (ver [calendario regulatorio](./appendix/calendario-regulatorio.md)). Los puentes de esta área aceleran el trabajo de demostración; no lo eliminan.
- **No es asesoría legal ni certificación.** Igual que el Marco Regulatorio de Adoption, estos artefactos son la traducción operativa que escriben personas con criterio jurídico; la interpretación de la norma es del equipo legal/DPO, y la certificación es de la organización con su auditor acreditado.

**El argumento de fondo.** La ventaja de Myrmion frente a ambas normas no es «tener políticas»: es que la **evidencia se genera por construcción**. La cadena de decisiones trazable por `correlationId`, el [registro de excepciones](../../templates/federation/registro-excepciones.md) con autorizador y caducidad, el [gate de coherencia](../federation/gobernanza-federada.md) reproducible y el versionado con hash de los documentos de gobernanza son exactamente el tipo de evidencia auditable que un certificador y una autoridad de mercado solicitan — y en Myrmion existen antes de que nadie las pida.

---

## 2. Mapa del área

### Documentos puente (`docs/compliance/`) — estables, sin fechas

| Documento | Qué resuelve |
|---|---|
| [puente-iso42001.md](./puente-iso42001.md) | Mapeo de las cláusulas 4–10 y los 38 controles del Anexo A de ISO/IEC 42001 a artefactos Myrmion, con la cobertura honesta de cada uno |
| [puente-eu-ai-act.md](./puente-eu-ai-act.md) | Mapeo de las obligaciones del EU AI Act, por rol (proveedor / deployer) y nivel de riesgo, a artefactos Myrmion |

### Plantillas (`templates/compliance/`) — las rellena cada organización

| Plantilla | Obligación que cubre |
|---|---|
| [ficha-transparencia-ia.md](../../templates/compliance/ficha-transparencia-ia.md) | EU AI Act art. 50 (transparencia) y art. 13 (instrucciones de uso) · ISO 42001 control A.8 |
| [plan-alfabetizacion-ia.md](../../templates/compliance/plan-alfabetizacion-ia.md) | EU AI Act art. 4 (alfabetización en IA) · ISO 42001 cl. 7.2–7.3 |
| [evaluacion-impacto-ia.md](../../templates/compliance/evaluacion-impacto-ia.md) | Evaluación de impacto del sistema de IA (ISO 42001 cl. 6 / control A.5, en línea con ISO/IEC 42005) con salida FRIA (EU AI Act art. 27) |
| [runbook-incidentes-graves.md](../../templates/compliance/runbook-incidentes-graves.md) | EU AI Act art. 73 (incidentes graves) + conexión con arts. 33–34 RGPD |
| [plan-monitorizacion-post-mercado.md](../../templates/compliance/plan-monitorizacion-post-mercado.md) | EU AI Act art. 72 (monitorización post-comercialización), formalizando los [patrones de drift](../federation/patrones-deteccion-drift.md) y las [métricas](../federation/metricas-federacion.md) |
| [politica-retencion-evidencias.md](../../templates/compliance/politica-retencion-evidencias.md) | Retención de logs y documentación (arts. 12, 18, 19, 26.6) y derecho de supresión RGPD sobre la telemetría |
| [declaracion-aplicabilidad-iso42001.md](../../templates/compliance/declaracion-aplicabilidad-iso42001.md) | Declaración de Aplicabilidad (SoA) del Anexo A, pre-estructurada con el mapeo a artefactos Myrmion |
| [programa-auditoria-interna-aims.md](../../templates/compliance/programa-auditoria-interna-aims.md) | ISO 42001 cl. 9.2 (auditoría interna) y cl. 9.3 (revisión por la dirección) |

### Apéndice (`docs/compliance/appendix/`) — fechado, envejece rápido

| Recurso | Qué contiene |
|---|---|
| [calendario-regulatorio.md](./appendix/calendario-regulatorio.md) | Estado y fechas de aplicación del EU AI Act, estado de las normas armonizadas (CEN-CENELEC JTC21), estado de la certificación acreditada ISO 42001/42006. **Verificar siempre antes de usar** |

La frontera entre puente y apéndice sigue la misma lógica que la [regla anti-acoplamiento](../federation/regla-anti-acoplamiento.md) de Federation: lo que envejece lento (mapeos estructurales, plantillas) vive en el cuerpo; lo que envejece rápido (fechas, estados legislativos, listas de organismos certificadores) vive en el apéndice y es responsabilidad de la comunidad mantenerlo.

---

## 3. Cómo encaja con los tres frameworks

- **Adoption** es donde el cumplimiento se *declara*: el [Marco Regulatorio](../../templates/adoption/marco-regulatorio.md) (Capa 1) articula qué regulación aplica, clasifica los casos de uso y fija las restricciones que ningún asistente puede violar. Las plantillas de esta área son extensiones operativas de esa Capa 1 — su custodio natural es el mismo: legal/compliance/DPO.
- **Federation** es donde el cumplimiento se *evidencia programáticamente*: el [gate de coherencia](../federation/gobernanza-federada.md) verifica la clasificación regulatoria de cada agente antes del alta (comprobación 7), la telemetría ([CF-05](../federation/criterios-funcionales.md)) genera las exportaciones de auditoría, y los [patrones de drift](../federation/patrones-deteccion-drift.md) son la monitorización post-comercialización en operación.
- **AI Factory** cubre lo que esta área deliberadamente no toca: la evaluación técnica de modelos pre-despliegue (sesgos, robustez, precisión del art. 15 a nivel de modelo). Esta área evidencia la *gestión*; AI Factory disciplina la *construcción*.

## 4. Por dónde empezar

1. Si tu organización opera en la UE o sirve a clientes europeos: rellena la [ficha de transparencia](../../templates/compliance/ficha-transparencia-ia.md) por cada asistente que interactúe con personas y el [plan de alfabetización](../../templates/compliance/plan-alfabetizacion-ia.md) — son las obligaciones del AI Act de aplicación más inmediata (ver [calendario](./appendix/calendario-regulatorio.md)).
2. Si algún caso de uso puede ser de alto riesgo (Anexo III): clasifícalo en el Marco Regulatorio (§2.2 de la [plantilla](../../templates/adoption/marco-regulatorio.md)) y ejecuta la [evaluación de impacto](../../templates/compliance/evaluacion-impacto-ia.md) antes de ponerlo en producción.
3. Si buscas la certificación ISO/IEC 42001: empieza por el [puente](./puente-iso42001.md) y la [SoA pre-estructurada](../../templates/compliance/declaracion-aplicabilidad-iso42001.md), y monta el [programa de auditoría interna](../../templates/compliance/programa-auditoria-interna-aims.md).

---

*Área de cumplimiento del ecosistema Myrmion — versión 1.0. Complementa, no sustituye: [manifiesto paraguas](../manifesto.md) · [Myrmion Adoption](../adoption/manifesto.md) §3.1 y §9 · [Myrmion Federation](../federation/manifesto.md).*
