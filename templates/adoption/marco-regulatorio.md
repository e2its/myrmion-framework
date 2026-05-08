<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Adoption — Plantilla del Marco Regulatorio

**Versión 1.0**

*Plantilla para articular la Capa 1 del Marco de Modelado — el Marco Regulatorio — en una organización que adopta IA mediante productos comerciales.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

Esta plantilla guía a una organización en la articulación de su Marco Regulatorio: el conjunto de obligaciones legales, normativas y contractuales que aplican a la organización por su jurisdicción, sector y naturaleza de los datos que maneja, y que sus asistentes de IA deben respetar sin excepción.

**Quién la rellena.** El custodio formal de esta capa es la función legal/compliance/DPO de la organización. En organizaciones pequeñas puede ser una sola persona; en grandes, un comité con representación de las funciones afectadas. La transformación digital coordina pero no decide el contenido — la decisión es de quien responde por el cumplimiento.

**Cómo se rellena.** Cada sección tiene una breve nota orientativa entre paréntesis y un bloque para completar. Las secciones marcadas como *opcionales* solo aplican a organizaciones para las que esos marcos son relevantes. Las marcadas como *obligatorias* deben completarse en cualquier organización que adopte Myrmion.

**Qué se hace después.** Una vez completada, esta plantilla se versiona — fecha, versión, custodios firmantes — y se incorpora al repositorio de gobernanza de IA de la organización. Los asistentes departamentales heredan estas obligaciones a través de las dos capas inferiores (Constitución Corporativa y Capas Departamentales). El Marco Regulatorio prevalece sobre las otras dos sin excepciones.

**Frecuencia de revisión recomendada.** Anual como mínimo. Ad hoc cuando entra en vigor regulación nueva relevante para la organización, cuando la organización entra en un mercado o sector con regulación adicional, o cuando hay cambios contractuales sustantivos con clientes que afecten al tratamiento de datos.

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Versión del documento | *(p. ej. 1.0, 1.1, 2.0)* |
| Fecha de aprobación | *(YYYY-MM-DD)* |
| Próxima revisión programada | *(YYYY-MM-DD)* |
| Custodio principal | *(rol o persona — p. ej. DPO, Director Legal, Responsable de Compliance)* |
| Custodios contribuidores | *(otros roles que han aportado contenido — p. ej. CISO, Director de Riesgos, Asesoría Jurídica externa)* |
| Aprobación formal | *(órgano que ha aprobado este documento — p. ej. Comité de Dirección, Comité de Riesgos)* |

---

## 1. Identificación de la organización

*(Esta sección establece el contexto que determina qué obligaciones aplican. Sin contexto claro, el resto del documento se vuelve genérico e inútil.)*

**Nombre legal de la organización:**
*(razón social completa)*

**Forma jurídica:**

**Jurisdicción de constitución:**

**Jurisdicciones operativas:**
*(países o regiones donde la organización presta servicios o procesa datos. Determina qué regulaciones aplican.)*

**Sector o sectores de actividad principal:**
*(p. ej. servicios profesionales B2B, sanidad, banca minorista, manufacturing, sector público. Determina qué regulaciones sectoriales aplican.)*

**Categorías de datos manejados:**
*(p. ej. datos personales de clientes, datos de salud, datos financieros, propiedad intelectual de terceros, secretos comerciales, datos de menores. Determina qué obligaciones específicas de protección aplican.)*

**Tamaño aproximado:**
*(plantilla, facturación o métrica relevante. Algunas regulaciones tienen umbrales de aplicabilidad por tamaño.)*

---

## 2. Marcos regulatorios obligatorios

*(Lista las regulaciones de cumplimiento obligatorio que aplican a la organización por su jurisdicción y sector. Estas obligaciones no se eligen — se cumplen. Esta sección establece qué obligaciones los asistentes deben respetar como suelo absoluto. Las excepciones a estas obligaciones no existen.)*

### 2.1 Protección de datos personales

**Marcos aplicables:**
*(p. ej. Reglamento (UE) 2016/679 — RGPD; LOPDGDD en España; UK GDPR para Reino Unido; CCPA para California; LGPD para Brasil; PIPL para China. Listar todos los aplicables.)*

**Obligaciones operativas relevantes para asistentes de IA:**
*(traducción a obligaciones que los asistentes deben respetar. Ejemplos:*
- *No procesar datos personales sin base jurídica.*
- *Aplicar minimización: solo datos estrictamente necesarios.*
- *No transferir datos personales fuera del Espacio Económico Europeo sin garantías adecuadas.*
- *Permitir ejercicio de derechos del interesado vía canal humano cuando aplique.*
- *Documentar tratamientos en RAT.)*

**Custodio operativo:**
*(rol que custodia esta sub-capa — típicamente DPO)*

### 2.2 Regulación específica de IA

**Marcos aplicables:**
*(p. ej. Reglamento (UE) 2024/1689 — EU AI Act; legislación nacional derivada; regulaciones sectoriales de IA. Listar todos los aplicables a la fecha de redacción.)*

**Calendario de aplicabilidad relevante:**
*(p. ej. para EU AI Act: prohibiciones desde febrero 2025, obligaciones GPAI desde agosto 2025, mayoría de obligaciones desde agosto 2026, alto riesgo embebido en productos regulados desde agosto 2027 — verificar fechas vigentes a la fecha de redacción del documento.)*

**Clasificación de los sistemas de IA usados por la organización:**
*(según las categorías del marco aplicable. Para EU AI Act: prohibido, alto riesgo, riesgo limitado con obligaciones de transparencia, riesgo mínimo. La mayoría de adopciones mediante productos comerciales caen en riesgo limitado o mínimo, pero algunos casos de uso pueden escalar.)*

**Obligaciones operativas relevantes para asistentes de IA:**
*(p. ej.:*
- *Transparencia: el asistente debe identificarse como tal cuando interactúa con personas.*
- *No usar IA para casos prohibidos por la regulación.*
- *Documentar el propósito y límites de cada asistente desplegado.*
- *Revisar clasificación de riesgo antes de cada caso de uso nuevo.)*

**Custodio operativo:**

### 2.3 Regulación sectorial

*(Solo aplicable si la organización opera en un sector regulado. Si no aplica, marcar como tal y omitir el contenido.)*

**Aplicable: Sí / No**

**Marcos aplicables si Sí:**
*(p. ej. para servicios financieros: DORA, MiFID II, PSD2, regulación bancaria nacional. Para sanidad: HIPAA en EE.UU., normativa nacional en cada país europeo. Para sector público: ENS en España, equivalentes europeos. Para infraestructuras críticas: NIS2.)*

**Obligaciones operativas relevantes para asistentes de IA:**
*(traducción específica al uso de IA en el sector. Variará mucho según el sector.)*

**Custodio operativo:**

### 2.4 Otros marcos obligatorios

*(Espacio abierto para regulaciones que no encajan en las categorías anteriores. Por ejemplo: regulación de propiedad intelectual relevante al uso de IA generativa, regulación laboral si los asistentes interactúan con empleados, regulación de competencia si los asistentes toman decisiones que afectan a precios o mercado.)*

**Marco:**
**Obligaciones operativas:**
**Custodio operativo:**

*(Repetir bloque para cada marco adicional.)*

---

## 3. Obligaciones contractuales asumidas

*(Las obligaciones derivadas de contratos con clientes, partners o proveedores que la organización ha asumido y que son tan vinculantes como una norma legal. Esta sección suele olvidarse y es origen frecuente de incumplimientos.)*

**Categorías típicas de obligaciones contractuales:**

- Restricciones sobre tratamiento de datos confidenciales del cliente (p. ej. no procesar en jurisdicciones específicas, no usar para entrenamiento de modelos, retención y eliminación específicas).
- Compromisos de seguridad asumidos en contratos master con grandes clientes.
- Cláusulas de auditoría que obligan a documentar tratamientos.
- Restricciones de subcontratación que afectan al uso de productos de terceros (incluyendo proveedores de IA).
- Obligaciones de notificación de incidentes con plazos específicos.

**Listado de obligaciones contractuales relevantes para asistentes de IA:**
*(una lista estructurada con: cliente o tipo de cliente afectado, obligación específica, plazo o vigencia, custodio operativo. Anonimizar nombres de clientes si el documento va a circular ampliamente dentro de la organización.)*

**Custodio operativo de esta sección:**
*(típicamente la función comercial o legal contractual)*

---

## 4. Marcos voluntarios de referencia

*(Marcos que la organización elige adoptar como referencia de buenas prácticas, sin obligación legal directa. La adopción puede ser parcial. Algunas organizaciones se certifican formalmente en estos marcos como diferenciador comercial; otras los usan como inspiración interna sin certificación.)*

### 4.1 NIST AI Risk Management Framework

**Adhesión: Sí / No / Parcial**

**Si Sí o Parcial — alcance de la adhesión:**
*(p. ej. uso del Playbook como referencia interna; cumplimiento de las cuatro funciones Govern/Map/Measure/Manage; aplicación del Generative AI Profile; mapping a controles internos.)*

**Custodio operativo:**

### 4.2 ISO/IEC 42001

**Adhesión: Sí / No / Parcial / En proceso de certificación**

**Si Sí o En proceso — alcance:**
*(p. ej. implementación de AIMS según norma; certificación formal pendiente o conseguida; integración con ISO 27001 y/o ISO 9001 si la organización ya las tiene.)*

**Organismo certificador (si aplica):**

**Custodio operativo:**

### 4.3 Otros marcos voluntarios

*(p. ej. principios de IA del cliente final si el cliente los exige como requisito comercial; principios sectoriales de asociaciones gremiales; HITRUST AI Framework para sanidad; SOC 2 Type II con controles ampliados a IA.)*

**Marco:**
**Adhesión:**
**Alcance:**
**Custodio operativo:**

---

## 5. Restricciones de uso explícitas

*(Esta sección es la más operativa de todas. Traduce las obligaciones de las secciones anteriores a restricciones concretas que los asistentes deben respetar como suelo absoluto. Se rellena después de las secciones 2-4 porque consolida lo que las anteriores establecen.)*

**Datos que NO pueden tratarse mediante asistentes de IA:**
*(p. ej. datos de salud sin anonimización previa; datos de menores sin consentimiento parental verificado; secretos comerciales clasificados; datos contractualmente restringidos del cliente X; datos sujetos a embargo regulatorio.)*

**Acciones que los asistentes NO pueden realizar:**
*(p. ej. tomar decisiones automatizadas con efectos jurídicos sobre personas sin supervisión humana; comunicar al exterior sin revisión; modificar registros maestros sin endorsement humano; transferir datos a jurisdicciones X; entrenar o reentrenar modelos con datos confidenciales del cliente.)*

**Productos comerciales NO autorizados para casos de uso con datos sensibles:**
*(algunos productos pueden estar autorizados para uso general pero NO para tratamientos de datos específicos. P. ej. *"el plan personal de ChatGPT no se autoriza para tratamiento de datos personales de clientes"*. Esta tabla se mantiene viva conforme la organización añade o retira productos.)*

**Casos de uso sometidos a aprobación previa:**
*(p. ej. cualquier asistente que vaya a interactuar directamente con clientes externos sin filtro humano; cualquier asistente que vaya a tomar decisiones financieras superiores a X; cualquier integración con sistemas de pago.)*

**Custodio operativo de esta sección:**

---

## 6. Responsabilidades y trazabilidad

*(Quién responde por qué, y cómo se documenta el cumplimiento. Sin esta sección clara, las obligaciones se difuminan y el cumplimiento real se vuelve imposible de demostrar.)*

**Tabla de custodios principales:**

| Sub-capa | Custodio | Sustituto en caso de ausencia |
|---|---|---|
| Protección de datos | *(p. ej. DPO)* | |
| Regulación específica de IA | | |
| Regulación sectorial | | |
| Obligaciones contractuales | | |
| Marcos voluntarios | | |
| Restricciones de uso | | |

**Mecanismo de actualización:**
*(cómo se actualiza este documento cuando cambia una regulación, cuando entra un cliente nuevo con cláusulas relevantes, cuando se incorpora un producto comercial nuevo, etc. Quién detecta el cambio, quién propone la actualización, quién aprueba.)*

**Mecanismo de evidencia de cumplimiento:**
*(qué se registra para poder demostrar que los asistentes están respetando estas obligaciones. P. ej. logs de uso de los productos comerciales, revisiones periódicas de outputs muestreados, auditorías internas, evidencias para auditoría externa cuando aplique.)*

**Plazo de retención de evidencias:**
*(según el marco más exigente que aplique. Típicamente 5 años, pero puede variar por sector o por contrato.)*

---

## 7. Notas y excepciones documentadas

*(Las excepciones al Marco Regulatorio NO existen por definición — es la naturaleza de las obligaciones heterónomas. Pero sí pueden documentarse interpretaciones o adaptaciones operativas que la organización ha decidido formalmente. Esta sección recoge esas decisiones, no como excepciones sino como aclaraciones de cumplimiento.)*

**Interpretaciones formalmente adoptadas:**
*(p. ej. *"se considera que los asistentes embebidos en herramientas de productividad personal no constituyen tratamiento automatizado a efectos del artículo 22 RGPD siempre que el output sea revisado por una persona antes de comunicarse al exterior. Esta interpretación está documentada en dictamen interno de fecha X."*)*

**Limitaciones operativas conocidas:**
*(situaciones donde la organización es consciente de un riesgo de cumplimiento y ha adoptado medidas mitigadoras. P. ej. *"el producto comercial X no permite limitar la región de procesamiento de datos. Mitigación: solo se autoriza para datos no personales hasta que el proveedor habilite la opción."*)*

---

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Esta plantilla es la materialización de la Capa 1 — Marco Regulatorio — del Marco de Modelado descrito en el manifiesto de [Myrmion Adoption](../../docs/adoption/manifesto.md). Para entender el contexto completo del framework y cómo esta capa se relaciona con la Constitución Corporativa y las Capas Departamentales, consultar el [manifiesto paraguas](../../docs/manifesto.md).*

*Para ver un Marco Regulatorio completamente rellenado como referencia orientativa, consultar [marco-regulatorio-ejemplo.md](./marco-regulatorio-ejemplo.md).*
