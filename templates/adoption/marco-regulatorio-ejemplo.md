<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Marco Regulatorio — Consultora Modelo S.L.

**Ejemplo orientativo**

*Este documento es un ejemplo completamente rellenado de la plantilla del Marco Regulatorio, basado en la misma organización ficticia que articula su [Constitución Corporativa](./constitucion-corporativa-ejemplo.md). Sirve como referencia para entender el nivel de detalle, el nivel de articulación operativa y el tipo de obligaciones que la plantilla espera capturar. **No debe copiarse literalmente** — cada organización tiene sus propias jurisdicciones, sus propios sectores y sus propios compromisos contractuales. La utilidad de este ejemplo es mostrar cómo se ve un Marco Regulatorio bien articulado, no proporcionar contenido reutilizable.*

*Consultora Modelo S.L. es una organización ficticia. Cualquier parecido con organizaciones reales es casualidad.*

</td>
</tr>
</table>

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Versión del documento | 1.0 |
| Fecha de aprobación | 2026-04-15 |
| Próxima revisión programada | 2027-04-15 |
| Custodio principal | DPO interno (Manuel Riera) |
| Custodios contribuidores | Asesoría Jurídica externa (Despacho Garrido Abogados), CISO interno, Director de Operaciones |
| Aprobación formal | Comité de Dirección, acta nº 2026-04 |

---

## 1. Identificación de la organización

**Nombre legal de la organización:** Consultora Modelo, S.L.

**Forma jurídica:** Sociedad Limitada

**Jurisdicción de constitución:** España (Madrid). Inscrita en el Registro Mercantil de Madrid.

**Jurisdicciones operativas:**

- **España** — sede central y mayoría de operaciones (60% facturación)
- **Portugal** — oficina en Lisboa, consultores residentes (15% facturación)
- **Francia** — sin presencia física, proyectos remotos con consultores móviles (15% facturación)
- **Italia** — sin presencia física, proyectos remotos con consultores móviles (10% facturación)

**Sector o sectores de actividad principal:** Servicios profesionales B2B — consultoría tecnológica especializada en transformación digital de empresas medianas. Sin actividad en sector regulado por sí misma, pero con clientes en sectores regulados (financiero, sanitario, sector público).

**Categorías de datos manejados:**

- Datos personales de empleados de la propia organización (datos laborales y RRHH)
- Datos personales de empleados de clientes (recibidos en el contexto de proyectos)
- Datos comerciales y de prospección (decisores en organizaciones cliente y prospect)
- Propiedad intelectual del cliente bajo NDA (documentación técnica, organigramas, procesos internos del cliente)
- Datos confidenciales de proyecto (planificaciones, decisiones, comunicaciones)
- Datos comerciales propios (propuestas, contratos, facturación)

Sin tratamiento de datos especialmente protegidos (salud, biometría, ideología) ni datos de menores. Cualquier emergencia de estas categorías en proyecto requiere evaluación específica caso a caso.

**Tamaño:** 80 empleados, 12M€ facturación anual estimada 2026. Por umbral de plantilla, no califica como mediana empresa según criterio de la UE (recomendación 2003/361/CE) — está en el rango superior de pequeña empresa.

---

## 2. Marcos regulatorios obligatorios

### 2.1 Protección de datos personales

**Marcos aplicables:**

- **Reglamento (UE) 2016/679 — RGPD** — base normativa principal por jurisdicción de constitución y operativa europea.
- **Ley Orgánica 3/2018 de Protección de Datos Personales y Garantía de los Derechos Digitales (LOPDGDD)** — España.
- **Lei n.º 58/2019** — Portugal, regulación específica complementaria al RGPD.
- **Loi Informatique et Libertés (Loi n° 78-17 modificada)** — Francia, regulación complementaria al RGPD.
- **Decreto Legislativo 196/2003 modificado por D.Lgs. 101/2018** — Italia.
- **Reglamento (UE) 2018/1725** — solo aplicable cuando se actúa como subcontratista de instituciones europeas (caso ocasional).

**Obligaciones operativas relevantes para asistentes de IA:**

- No procesar datos personales identificables del cliente con productos de IA sin DPA firmado entre Consultora Modelo y el proveedor del producto.
- Aplicar minimización en todas las interacciones con asistentes — solo los datos estrictamente necesarios para la tarea.
- Prohibición de utilizar versiones personales o gratuitas de productos de IA con datos personales del cliente o de la organización.
- Permitir el ejercicio de derechos del interesado (acceso, rectificación, supresión, portabilidad, oposición) vía canal humano. Los asistentes no resuelven solicitudes ARCO directamente — solo identifican y escalan.
- No transferir datos personales fuera del Espacio Económico Europeo sin garantías adecuadas (cláusulas contractuales tipo, decisión de adecuación). Esto restringe qué productos de IA se autorizan según dónde tengan los servidores.
- Documentar todos los tratamientos en el Registro de Actividades de Tratamiento (RAT), incluyendo los que involucran asistentes de IA.
- Aplicar reglas de retención del cliente cuando sean más estrictas que las propias políticas de la organización.
- Etiquetar todos los outputs generados con IA en entregables al cliente, incluso cuando no es legalmente exigible (compromiso cultural más allá de la obligación legal).

**Custodio operativo:** Manuel Riera (DPO interno), con apoyo de Despacho Garrido Abogados para asesoramiento jurídico en Francia e Italia.

### 2.2 Regulación específica de IA

**Marcos aplicables:**

- **Reglamento (UE) 2024/1689 — EU AI Act** — base normativa principal.
- Calendario de aplicabilidad relevante: prohibiciones aplicables desde febrero 2025; obligaciones GPAI desde agosto 2025; mayoría de obligaciones desde agosto 2026; sistemas de alto riesgo embebidos en productos regulados desde agosto 2027 (con extensión propuesta a diciembre 2027 en Digital Omnibus Package). Verificar fechas vigentes en cada revisión anual del documento.
- **Real Decreto 817/2023** (España) — regulación de un entorno de pruebas de inteligencia artificial; aplicable solo si la organización participa en sandbox.

**Clasificación de los sistemas de IA usados por la organización:**

- **Riesgo mínimo:** asistentes de productividad interna (Microsoft Copilot for Microsoft 365 para empleados, ChatGPT Enterprise para uso interno, Claude Enterprise para análisis y redacción internos).
- **Riesgo limitado:** asistentes que generan outputs incorporados en entregables al cliente. Sujetos a obligaciones de transparencia.
- **Sin casos de uso clasificados como alto riesgo o prohibido** a la fecha de aprobación de este documento. Cualquier caso de uso nuevo que pudiera caer en alto riesgo requiere evaluación específica antes de autorización.

**Obligaciones operativas relevantes para asistentes de IA:**

- Los asistentes que interactúan con personas físicas — empleados, clientes, prospects — deben identificarse explícitamente como sistemas de IA. Esto incluye la firma de comunicaciones y la cabecera de outputs generados con asistencia.
- Etiquetar todos los outputs generados con IA en entregables al cliente con marca *"Generado con asistencia de IA. Revisado por [nombre del consultor]"*.
- Revisión humana sistemática antes de cualquier comunicación externa. Sin excepción.
- Documentación del propósito y límites de cada asistente desplegado. Esta documentación se mantiene viva en el repositorio interno de gobernanza de IA.
- Revisión de clasificación de riesgo antes de autorizar cada caso de uso nuevo. La autorización requiere firma del DPO y del Director de Operaciones.

**Custodio operativo:** Director de Operaciones (Pilar Méndez), con asesoría legal puntual de Despacho Garrido Abogados cuando emerge un caso límite.

### 2.3 Regulación sectorial

**Aplicable:** No directamente — Consultora Modelo no opera en sector regulado.

**Aplicable indirectamente:** Sí, a través de clientes que sí lo están. Cuando un proyecto involucra a un cliente del sector financiero, sanitario o público, la organización absorbe contractualmente las obligaciones sectoriales que el cliente tiene y que se transmiten en el DPA o contrato.

**Obligaciones sectoriales heredadas más recurrentes:**

- **Sector financiero (clientes bajo DORA, MiFID II, regulación bancaria nacional):** restricciones de subcontratación, requisitos de localización geográfica de procesamiento, obligaciones de auditoría.
- **Sector sanitario (clientes bajo regulación nacional sanitaria, RGPD reforzado para datos de salud):** prohibición casi absoluta de procesamiento de datos identificables, restricciones geográficas estrictas, obligaciones de seudonimización.
- **Sector público (clientes bajo Esquema Nacional de Seguridad — ENS — en España):** requisitos de certificación, restricciones de subcontratación, auditorías ENS.

**Custodio operativo:** Director Comercial (Andrés Fonseca) en colaboración con Asesoría Jurídica externa. Cada proyecto con cliente regulado pasa por revisión específica antes de aceptación.

### 2.4 Otros marcos obligatorios

**Reglamento NIS2 (Directiva (UE) 2022/2555):** Consultora Modelo no es entidad esencial ni importante por umbral de plantilla y sector. No directamente aplicable. Aplicable indirectamente cuando un cliente lo es y exige medidas de ciberseguridad alineadas a NIS2 contractualmente.

**Reglamento de propiedad intelectual:** Real Decreto Legislativo 1/1996 (España) y equivalentes europeos. Relevante porque algunos productos de IA generativa pueden producir outputs con problemas de derechos de autor. La organización monitorea las decisiones jurisprudenciales y ajusta sus restricciones de uso conforme emergen criterios.

**Custodio operativo:** Asesoría Jurídica externa (Despacho Garrido Abogados).

---

## 3. Obligaciones contractuales asumidas

### Cliente bajo cláusulas restrictivas — Sector financiero

- **Tipo de cliente:** entidad financiera de tamaño medio, supervisada por el Banco de España.
- **Obligaciones específicas para asistentes de IA:**
  - Sin procesamiento de datos del cliente con productos de IA sin endorsement contractual explícito previo a cada caso de uso.
  - Retención máxima de datos del proyecto: 90 días tras finalización, con destrucción certificada.
  - Procesamiento exclusivo en infraestructura del EEE, sin excepciones.
  - Auditoría anual del cumplimiento, con derecho del cliente a inspección presencial con preaviso.
- **Custodio operativo:** Responsable del proyecto + DPO.

### Cliente bajo cláusulas restrictivas — Sector sanitario

- **Tipo de cliente:** grupo hospitalario privado.
- **Obligaciones específicas para asistentes de IA:**
  - Cláusula de subcontratación que excluye productos de IA con procesamiento fuera del EEE.
  - Seudonimización obligatoria de cualquier dato del cliente antes de procesamiento con IA.
  - Prohibición absoluta de uso de productos de IA generativa con datos clínicos, incluso seudonimizados.
  - Notificación al cliente de cualquier incidencia de seguridad relacionada con IA en plazo máximo de 24 horas.
- **Custodio operativo:** Responsable del proyecto + DPO + CISO.

### Compromisos transversales que la organización aplica uniformemente

- Aunque solo el cliente del sector financiero exige retención de 90 días, la organización ha decidido aplicar este criterio uniformemente con todos los clientes del sector como consistencia operativa. Decisión cultural reflejada operativamente.
- Aunque solo algunos clientes exigen revisión humana antes de comunicación externa, la organización lo aplica sistemáticamente con todos. Esta decisión la articula la Constitución Corporativa (revisión humana sistemática) y se materializa en este Marco Regulatorio como obligación operativa.

**Custodio operativo de la sección:** Director Comercial (Andrés Fonseca) en lo contractual; DPO en lo de cumplimiento operativo.

### Matriz de licenciamiento por requisito de cumplimiento

*Esta matriz es la versión trazable de la lista de productos autorizados de §5. Registra, por cada requisito que aplica a Consultora Modelo, el instrumento contractual concreto, el producto/tier, la vía de aprovisionamiento (que determina con quién se firma) y el estado. Se revisa cada vez que se incorpora o retira un producto. Las condiciones de proveedor se re-verifican en cada revisión anual del documento — ver la [Guía de protección de datos](../../docs/adoption/guia-proteccion-datos.md).*

| Requisito aplicable | Instrumento a obtener | Proveedor / producto / tier | Vía de aprovisionamiento | Estado |
|---|---|---|---|---|
| RGPD — datos personales de cliente | DPA + EU Data Boundary | Microsoft 365 Copilot (Enterprise) | First-party (Microsoft como encargado) | ✅ Firmado; CUECs del informe SOC 2 de Microsoft implementados |
| RGPD — datos personales de cliente | DPA + residencia *at-rest* en Europa | ChatGPT Enterprise | First-party (OpenAI como encargado) | ✅ Firmado; residencia Europa activada |
| RGPD — datos personales de cliente | DPA + residencia EEE | Claude Enterprise | ⚠️ API first-party de Anthropic **no garantiza residencia UE** | 🔶 En evaluación de migración a **Amazon Bedrock (eu-central-1)** para los proyectos con residencia EEE estricta; mientras tanto, no se usa Claude con datos de cliente sujetos a residencia |
| No-entrenamiento con datos de cliente | Cláusula de no-entrenamiento | Los tres productos Enterprise anteriores | First-party | ✅ Incluida por defecto en el tier Enterprise de los tres proveedores |
| Residencia exclusiva EEE (cliente financiero y sanitario) | Procesamiento *at-rest* e inferencia exclusivos en el EEE | Microsoft 365 Copilot (EU Data Boundary) y, para Claude, vía Bedrock eu-central-1 | First-party / Bedrock | 🔶 Confirmado para Copilot; pendiente la vía Bedrock para Claude |
| SOC 2 Type II / ISO 27001 del proveedor | Revisión del informe bajo NDA + implementación de CUECs | Los tres proveedores | — (atestación del proveedor, no se "obtiene") | 🔄 Informes revisados anualmente bajo NDA; CUECs incorporados al programa interno |
| HIPAA / PHI | BAA | **No aplica** | — | ⛔ No procede: la organización y sus clientes operan en el EEE, sin nexo con HIPAA (no hay *covered entity* ni *business associate* bajo ley estadounidense). Además, §5 prohíbe tratar datos de salud identificables con IA y, si emergieran, se retiran o anonimizan irreversiblemente antes de cualquier interacción — no se contrata BAA |

*Observación de la custodia: la fila de Claude refleja una tensión real detectada al articular la matriz — la autorización genérica de "Claude Enterprise bajo DPA" de §5 no es suficiente para los clientes con residencia EEE estricta, porque el API first-party de Anthropic no ofrece residencia UE a la fecha de este documento. La matriz fuerza a hacer explícita esa restricción y a decidir la vía de aprovisionamiento (Bedrock eu-central-1) antes de usar el producto con esos datos. Las herramientas, tiers y vías concretas de esta matriz son ilustrativas de esta organización ficticia, no recomendaciones canónicas de Myrmion. Verificar condiciones vigentes antes de contratar.*

---

## 4. Marcos voluntarios de referencia

### 4.1 NIST AI Risk Management Framework

**Adhesión:** Parcial.

**Alcance de la adhesión:**

- Uso del Playbook como referencia interna para la articulación de procesos de gobernanza.
- Aplicación voluntaria de las cuatro funciones — Govern, Map, Measure, Manage — como estructura del programa interno de gobernanza de IA.
- Referencia al Generative AI Profile (NIST AI 600-1) para los casos de uso de IA generativa.
- Sin certificación formal — adhesión declarada pero no auditada externamente.

**Custodio operativo:** Director de Operaciones.

### 4.2 ISO/IEC 42001

**Adhesión:** En proceso de certificación.

**Alcance:**

- Implementación de Sistema de Gestión de IA (AIMS) según norma EN ISO/IEC 42001:2026.
- Certificación formal prevista para Q4 2026.
- Integración con ISO 27001 ya certificada (vigente desde 2023) y ISO 9001 ya certificada (vigente desde 2019).
- Plan-Do-Check-Act articulado y operativo desde Q1 2026.

**Organismo certificador:** AENOR (España).

**Custodio operativo:** Director de Operaciones, con apoyo de consultor externo de certificación.

### 4.3 Otros marcos voluntarios

- **HITRUST AI Framework:** No adherido. Evaluado y descartado por enfoque sectorial sanitario, que no es el principal de la organización.
- **Principios éticos de cliente final:** Algunos clientes exigen contractualmente adhesión a sus propios principios éticos de IA (típicamente principios de transparencia, equidad, supervisión humana). La organización los acepta cuando son razonables y compatibles con la Constitución Corporativa propia.

---

## 5. Restricciones de uso explícitas

### Datos que NO pueden tratarse mediante asistentes de IA

- Datos de salud identificables, sin excepción, incluso con consentimiento del titular.
- Datos de menores (no aplicable habitualmente, pero declarado por completitud).
- Datos contractualmente restringidos por cliente específico, según las cláusulas particulares de cada DPA.
- Información clasificada como confidencial estricta en proyectos con sector público.
- Credenciales, claves de acceso, secretos técnicos del cliente.
- Datos fiscales identificables del cliente sin procedimiento específico aprobado por el DPO.

### Acciones que los asistentes NO pueden realizar

- Tomar decisiones automatizadas con efectos jurídicos sobre personas (contratación, despido, evaluación de empleados, scoring de clientes) sin supervisión humana.
- Comunicar al exterior — clientes, prospects, partners, prensa — sin revisión humana previa.
- Modificar registros maestros (CRM, ERP, herramientas de proyecto) sin endorsement humano explícito.
- Transferir datos a jurisdicciones fuera del EEE sin verificación previa de garantías.
- Entrenar o reentrenar modelos con datos confidenciales del cliente.
- Aceptar compromisos contractuales con clientes en nombre de la organización.
- Decidir sobre solicitudes de ejercicio de derechos ARCO — solo identificar y escalar.

### Productos comerciales NO autorizados para casos de uso con datos sensibles

- ChatGPT plan personal y plan Plus: no autorizado para datos de cliente. Solo plan Enterprise con DPA firmado.
- Claude plan personal y plan Pro: no autorizado para datos de cliente. Solo plan Enterprise con DPA firmado.
- Gemini personal: no autorizado para datos de cliente. En evaluación para Gemini Enterprise con DPA.
- Productos de IA en versión gratuita o "free tier" de cualquier proveedor: no autorizados para datos de cliente bajo ninguna circunstancia.
- Productos de IA en evaluación o piloto: requieren autorización específica del DPO antes de cualquier uso con datos.

### Productos comerciales autorizados con configuración corporativa

- **Microsoft Copilot for Microsoft 365** (suscripción Enterprise) — autorizado para datos internos y datos de cliente bajo DPA estándar de Microsoft.
- **Claude Enterprise** (suscripción con DPA firmado con Anthropic) — autorizado para datos internos y datos de cliente bajo restricciones específicas del DPA.
- **ChatGPT Enterprise** (suscripción con DPA firmado con OpenAI) — autorizado para datos internos y datos de cliente bajo restricciones específicas del DPA.

### Casos de uso sometidos a aprobación previa

- Cualquier asistente que vaya a interactuar directamente con clientes externos sin filtro humano previo.
- Cualquier asistente que vaya a tomar decisiones financieras superiores a 5.000€.
- Cualquier integración con sistemas de pago o facturación.
- Cualquier despliegue en proyectos con cliente del sector financiero, sanitario o público.
- Cualquier uso de IA en contexto de auditoría externa o due diligence.

### Restricciones derivadas de la identidad de la organización

Algunas restricciones de uso nacen de la Constitución Corporativa, no del cumplimiento legal, pero la organización ha decidido tratarlas como restricciones absolutas no negociables al mismo nivel que las legales:

- No se aceptan proyectos cuyo entregable principal sea generar el documento que el cliente necesita para una auditoría regulatoria, cuando se sabe que la operación auditada no cumple. La organización no actúa como brazo blanqueador de operaciones que no cumplen.
- No se comprometen al cliente afirmaciones que sabemos que no se sostienen, aunque eso cueste el contrato.
- No se aceptan comisiones, pagos o ventajas de proveedores tecnológicos a cambio de recomendarlos al cliente.

*Nota: la frontera entre Capa 1 (Marco Regulatorio) y Capa 2 (Constitución Corporativa) es porosa en este punto. Es legítimo articular en el Marco Regulatorio aquellas convicciones culturales que la organización ha decidido tratar como restricciones absolutas no negociables — el efecto operativo es el mismo (restricción no susceptible de excepción) y simplifica la aplicación práctica.*

### Transformación técnica de des-identificación exigida antes de procesar con IA

*Las restricciones anteriores declaran qué no puede tratarse. Esta sub-sección articula qué transformación se exige sobre los datos que sí se permite tratar bajo condiciones, antes de que lleguen a un producto de IA, y quién la ejecuta. En la fase de Adoption la transformación es un paso previo sancionado, no una redacción transparente en la ruta del prompt (eso requeriría un intermediario programático — territorio de Federation). Para el panorama de herramientas, ver la [Guía de protección de datos](../../docs/adoption/guia-proteccion-datos.md).*

| Categoría de dato sensible | Transformación exigida antes de IA | Quién/qué la ejecuta y cuándo | Verificación / responsable |
|---|---|---|---|
| Datos personales de empleados de cliente (no sensibles) | Minimización + seudonimización reversible de identificadores directos | Consultor, como paso manual previo, con herramienta interna de des-identificación (Microsoft Presidio self-host, modelo spaCy en español + recognizers adaptados al EEE) | Revisión por muestreo trimestral del DPO (alineada con §6) |
| Propiedad intelectual del cliente bajo NDA | Minimización + retirada de identificadores de proyecto y cliente cuando no son necesarios | Consultor antes del envío | Responsable del proyecto |
| Datos de salud identificables | **No se procesan con IA** (prohibición absoluta, §5). Si emergen en un proyecto, se retiran o anonimizan irreversiblemente antes de cualquier interacción con IA | Consultor + DPO; verificación de eficacia de la anonimización documentada | DPO + CISO |
| Credenciales, claves y secretos técnicos del cliente | Nunca se introducen en ningún producto de IA | Disciplina + control de endpoint | CISO |

*Límite declarado: la des-identificación basada en Presidio en español no garantiza un recall del 100% — la organización lo trata como una capa de defensa en profundidad, no como sustituto de la revisión humana sistemática ya exigida en §2.2 ni de las prohibiciones absolutas. Ninguna afirmación de cumplimiento se apoya en la herramienta de des-identificación por sí sola. La elección concreta (Presidio + spaCy ES) es ilustrativa; cada organización selecciona y valida sus propias herramientas.*

**Custodio operativo de esta sección:** DPO + Director General.

---

## 6. Responsabilidades y trazabilidad

**Tabla de custodios principales:**

| Sub-capa | Custodio | Sustituto en caso de ausencia |
|---|---|---|
| Protección de datos | Manuel Riera (DPO) | Asesoría Jurídica externa (Despacho Garrido Abogados) |
| Regulación específica de IA | Pilar Méndez (Directora de Operaciones) | DPO |
| Regulación sectorial heredada | Andrés Fonseca (Director Comercial) | Director General |
| Obligaciones contractuales | Andrés Fonseca (Director Comercial) | DPO |
| Marcos voluntarios | Pilar Méndez (Directora de Operaciones) | Director General |
| Restricciones de uso | DPO + Director de Operaciones | Director General |

**Mecanismo de actualización:**

Cualquier persona de la organización puede notificar al DPO una posible necesidad de actualización (regulación nueva, cliente nuevo con cláusulas relevantes, producto comercial nuevo a evaluar). El DPO evalúa mensualmente las notificaciones, propone actualizaciones cuando aplique, y las eleva al Comité de Dirección para aprobación. Las actualizaciones aprobadas se versionan, comunican internamente y se incorporan al RAT cuando afectan a tratamientos.

**Mecanismo de evidencia de cumplimiento:**

- Logs de uso de los productos comerciales corporativos (acceso a logs de Microsoft 365, Claude Enterprise, ChatGPT Enterprise vía respectivos paneles de administración).
- Revisiones trimestrales de outputs muestreados generados con IA en entregables al cliente.
- Auditorías internas anuales del programa de gobernanza de IA, ejecutadas por consultor externo independiente.
- Evidencias específicas para auditoría externa de ISO 42001 cuando llegue la certificación formal.
- Registro de excepciones, escalados y decisiones de autorización en repositorio interno con acceso al DPO y al Director de Operaciones.

**Plazo de retención de evidencias:**

- Evidencias relacionadas con datos personales: según RGPD y políticas internas, mínimo 2 años, máximo según finalidad.
- Evidencias relacionadas con cumplimiento de IA: 5 años, alineado con horizonte de auditoría ISO 42001.
- Evidencias relacionadas con clientes específicos: según contrato, típicamente la mayor de 5 años o vigencia del proyecto + 2 años.

---

## 7. Notas y excepciones documentadas

### Interpretaciones formalmente adoptadas

- Se considera que los asistentes embebidos en herramientas de productividad personal (Microsoft Copilot, Claude Enterprise, ChatGPT Enterprise) usados por empleados para tareas internas, no constituyen tratamiento automatizado a efectos del artículo 22 RGPD siempre que el output sea revisado por una persona antes de comunicarse al exterior. Esta interpretación está documentada en dictamen interno de 2026-02-10 elaborado por Despacho Garrido Abogados.
- Se considera que la generación de informes con asistencia de IA no constituye "decisión automatizada" en el sentido del artículo 22 RGPD cuando el informe es input para una decisión humana posterior, no la decisión misma. Documentado en mismo dictamen.

### Limitaciones operativas conocidas

- Algunos productos de IA en evaluación no permiten configurar la región específica de procesamiento de datos. Mitigación: estos productos solo se autorizan para datos no personales de la organización (datos comerciales agregados, documentación pública) hasta que el proveedor habilite la opción.
- Microsoft Copilot Studio, en evaluación para creación de agentes corporativos personalizados, requiere validación específica del DPO para cada agente antes de despliegue. Procedimiento de validación documentado en repositorio interno.

---

*Marco Regulatorio de Consultora Modelo S.L. — versión 1.0, aprobado el 2026-04-15. Documento ficticio orientativo.*

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Para la plantilla en blanco, consultar [marco-regulatorio.md](./marco-regulatorio.md). Para ver la Constitución Corporativa de la misma organización, consultar [constitucion-corporativa-ejemplo.md](./constitucion-corporativa-ejemplo.md). Para entender el contexto del framework, consultar el [manifiesto de Myrmion Adoption](../../docs/adoption/manifesto.md).*
