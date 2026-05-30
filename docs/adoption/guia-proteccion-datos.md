# Guía de protección de datos en la adopción de IA

**Capa técnica y capa contractual — versión 1.0**

*Guía operativa del ecosistema **Myrmion** para articular la protección de datos personales, datos de salud y datos regulados cuando una organización los envía — o evita enviarlos — a productos de IA comerciales.*

*Documento vivo. Las condiciones de proveedor, las certificaciones, las disponibilidades de BAA/DPA/residencia y las fechas regulatorias citadas reflejan fuentes vigentes a mayo de 2026 y **deben re-verificarse antes de cualquier decisión contractual**. Esta guía **no es asesoría legal y no la sustituye**: la interpretación jurídica de cada norma sigue siendo trabajo del DPO o de la función jurídica. Es la traducción operativa, para quien custodia el [Marco Regulatorio](../../templates/adoption/marco-regulatorio.md), de qué controles existen y dónde encaja cada uno.*

---

## Por qué esta guía existe

El [Marco Regulatorio](../../templates/adoption/marco-regulatorio.md) de Myrmion — la Capa 1 del Marco de Modelado — es donde cada organización articula sus restricciones de uso; el framework no las prescribe. La plantilla pide, por ejemplo, *"aplicar minimización"*, y una organización que trate datos sensibles típicamente declara restricciones como las que ilustra el [ejemplo de Consultora Modelo](../../templates/adoption/marco-regulatorio-ejemplo.md): *"seudonimización obligatoria de cualquier dato del cliente antes de procesamiento con IA"*, *"datos de salud identificables, sin excepción"*. Son prohibiciones correctas. Pero una prohibición declarada en un documento **no es, por sí sola, un control**. Mientras una persona pueda pegar el nombre de un paciente, un número de tarjeta o el organigrama confidencial de un cliente en la caja de texto de Copilot, ChatGPT, Claude o Gemini, la prohibición depende enteramente de que esa persona se acuerde de no hacerlo.

Cerrar ese hueco no es un único movimiento. Requiere entender que la protección de datos frente a un LLM vive en **dos capas que operan en lados distintos de la frontera de la organización**, y que **ninguna sustituye a la otra**. Esta guía articula esas dos capas, recoge el panorama de herramientas y proveedores vigente, y proporciona las matrices de decisión que el custodio del Marco Regulatorio necesita para materializar sus restricciones en controles reales.

---

## 1. Tesis central — el modelo de dos capas

Proteger datos personales, datos de salud o datos de tarjeta cuando se envían a un LLM exige dos capas:

- **Capa técnica — des-identificación / DLP.** Controla *qué dato llega a salir* del perímetro: minimización, redacción, enmascarado, tokenización, anonimización. Gobierna el dato **en tránsito** hacia el proveedor.
- **Capa contractual — licenciamiento por requisito.** Controla *qué puede hacer el proveedor* con el dato que sí recibe: tratamiento limitado a instrucciones documentadas, retención, uso secundario o entrenamiento, transferencia internacional, residencia, subencargados, notificación de brechas. Gobierna el dato **una vez está en manos del proveedor**.

La razón por la que ninguna sustituye a la otra es estructural, no de grado:

> Un contrato perfecto no puede "des-filtrar" un dato que nunca debió enviarse. Una redacción perfecta no puede vincular al proveedor respecto al dato residual que sí enviaste.

### 1.1 El matiz regulatorio que decide cuándo una capa basta

No todos los marcos tratan igual la capa técnica. La diferencia es operativa y conviene declararla sin ambigüedad:

- **HIPAA y PCI-DSS ofrecen una "puerta de salida" técnica real.** Bajo HIPAA, una des-identificación correcta — *Safe Harbor* (eliminar los 18 identificadores del 45 CFR §164.514(b)(2)) o *determinación de experto* — convierte el dato en **no-PHI**: queda fuera del alcance de la norma y no requiere BAA por esa vía. Bajo PCI-DSS, tokenizar o truncar el PAN antes del envío puede sacar el sistema del LLM del ámbito de datos de tarjeta. Pero la puerta solo funciona si la des-identificación es *de verdad* suficiente: si la redacción falla en uno solo de los 18 identificadores, sigue siendo PHI y la afirmación de Safe Harbor cae.
- **RGPD y LOPDGDD NO ofrecen esa puerta por mera redacción.** La seudonimización (reversible, con clave) **sigue siendo dato personal** y permanece bajo el RGPD — reduce el riesgo y aligera la carga de base jurídica, pero no saca el dato del ámbito. Solo la anonimización **irreversible** (sin medios razonables de reidentificación) lo saca, y eso rara vez lo logra una capa de DLP por sí sola. La AEPD es explícita en esta línea y exige una **evaluación documentada del riesgo de reidentificación**, no la presunción de que enmascarar equivale a anonimizar.
- **El EU AI Act es un eje distinto.** No es des-identificación ni contrato de tratamiento. Es transparencia y gobernanza de modelo (Art. 50: avisar de que se interactúa con IA, marcar el contenido sintético de forma legible por máquina). Una capa de redacción no satisface el AI Act; son obligaciones que recaen sobre el *deployer* y no se externalizan al proveedor del modelo. Se incluye en las matrices de esta guía por completitud de la Capa 1, aunque quede fuera del modelo estricto de dos capas.

La consecuencia práctica: una organización que solo maneja PII bajo RGPD **no puede confiar la protección a la redacción** — necesita el contrato. Una que maneja PHI sí puede, en algunos flujos, evitar el BAA des-identificando bien — pero asume el riesgo de recall. La mayoría necesita **las dos capas a la vez**.

---

## 2. Capa técnica — des-identificación / DLP

### 2.1 El punto arquitectónico honesto (y por qué importa para Myrmion)

Casi todas las herramientas que redactan, tokenizan o enmascaran son **librerías, modelos, proxies o gateways**. Ninguna redacta nada hasta que algo las hospeda y las ejecuta en la ruta de la llamada. De ahí una consecuencia directa para la arquitectura de Myrmion:

- **La redacción inline transparente — enmascarar el dato sensible *antes* de que el prompt llegue al modelo, sin bloquear la conversación — exige un intermediario en la ruta:** un proxy, un gateway MCP o una integración por API. Eso es arquitectónicamente **Myrmion Federation** (o uso API-mediado), no Adoption pura.
- **En Adoption pura** — empleados usando Copilot, ChatGPT, Claude o Gemini directamente en web o escritorio, sin proxy programático — **no hay punto de inserción** para casi ninguna de estas herramientas. Los controles realistas en Adoption pura son exactamente tres: **(a) selección de tier/contrato** (la capa contractual, §3); **(b) bloqueo, coaching y auditoría vía CASB/DLP/endpoint/navegador**; y **(c) herramienta de des-identificación sancionada como paso previo, respaldada por disciplina humana y formación**.

Esta guía mantiene deliberadamente esa frontera. La redacción inline automática no se presenta como capacidad de Adoption porque fingir que la disciplina humana es enforcement técnico sería vender humo — la misma honestidad con la que el manifiesto reconoce que no resuelve la interoperabilidad estructurada.

Hay dos excepciones verificadas que sí logran redacción inline transparente sin agente programático, pero **interponiendo un intermediario** (lo que difumina la frontera Adoption/Federation y debe asumirse como tal): **Netskope One** (proxy SSE inline que enmascara tokens y deja pasar el resto — *"redact, don't block, when feasible"*) e **Island Enterprise Browser** (AI Protect sanea el prompt en el motor del navegador). Ambas requieren inspección SSL o un navegador corporativo. Para Zscaler, Palo Alto AI Access Security, Skyhigh y Forcepoint inline, la redacción transparente **no está confirmada** por sus fuentes públicas: documentan bloqueo, coaching y aislamiento de navegador, no enmascarado.

### 2.2 Panorama por categorías

**(A) Librerías y modelos OSS (primitivas de des-identificación).**

| Herramienta | Despliegue | Cobertura ES/UE + PHI | Licencia | Fase Myrmion |
|---|---|---|---|---|
| **Microsoft Presidio** (Analyzer + Anonymizer + Image + Structured) | Self-host: pip, Docker, K8s, REST, PySpark | PII amplia; ES **por configuración** (requiere modelo spaCy/transformers + adaptar *context words*, no viene listo); PHI parcial (NPI/MBI, MedicalNERRecognizer, redactor DICOM) — **no** es un motor Safe Harbor certificado | MIT | Ambas (motor base) |
| **GLiNER PII** — `urchade/gliner_multi_pii-v1` | Self-host; se enchufa a Presidio como *recognizer* externo | Multilingüe incl. **ES**; PHI no certificado | Apache-2.0 | Federation |
| **LLM Guard** (Anonymize/Deanonymize + Vault) | Librería/microservicio | Hereda Presidio; patrón *vault* reversible de ida y vuelta | MIT | Federation |
| **Guardrails AI**, **NeMo Guardrails** | Librería/rails | Orquestan Presidio/GLiNER por debajo | Apache-2.0 | Federation |
| **Piiranha-v1** | HuggingFace transformers | Multilingüe incl. ES | **CC-BY-NC-ND-4.0 — no comercial** ⚠️ descartar para producción comercial | — |
| **Philter (UCSF)** | CLI batch | PHI clínico, **solo inglés**, mantenimiento incierto | BSD-3 | Adoption (batch sancionado) |

El punto estratégico: **Presidio (MIT) es el ancla OSS**. Es el motor que LLM Guard, Guardrails AI, NeMo Guardrails y la mayoría de gateways usan por debajo. Estandarizar en Presidio da una capa DLP portable y vendor-neutral que sobrevive a cambiar de gateway — exactamente la postura *"criterios, no marcas"* del manifiesto Federation.

**(B) Productos comerciales de des-identificación / data-privacy-vaults.**

| Herramienta | Perímetro | ES/UE + PHI | Notas |
|---|---|---|---|
| **Private AI / Limina AI** (rebranded 2025-26) | Contenedor on-prem/VPC — *el dato nunca sale* | 52 idiomas incl. ES; PHI; patrón PrivateGPT (de-id antes del LLM externo, re-id en la respuesta) | Mejor postura para no convertir el de-id en un nuevo vector de fuga |
| **Tonic Textual** | Self-host K8s/Docker (síntesis integrada, sin llamadas externas) | 50+ idiomas incl. ES; PHI vía Expert Determination | Buen encaje en ambas fases |
| **Protecto** | Cloud / on-prem / air-gapped; tokenización determinista *format-preserving* | 200+ tipos, 50+ idiomas; packs HIPAA/RGPD | SOC 2 II, ISO 27001, HIPAA + BAA |
| **Skyflow** | SaaS en VPC aislado; BYOC / Virtual Private Skyflow | PII/PHI vault; residencia en 150+ países | ISO 27001, SOC 2 I&II, PCI L1, HIPAA, RGPD. No air-gapped puro |
| **John Snow Labs Healthcare NLP** | Self-host licenciado / marketplace | **PHI clínico _best-in-class_ + ES** (xlm-roberta multilingüe) | **COMERCIAL, no gratuito** — único de-id de PHI en español de grado regulatorio entre las opciones |
| **Gretel** (NVIDIA) | SaaS / Hybrid | Síntesis + privacidad diferencial | ⚠️ Para uso *offline* (corpus de entrenamiento/RAG), no proxy en runtime |
| **Amazon Comprehend / Comprehend Medical** | Cloud-only | Comprehend PII: inglés y **español**; Comprehend Medical PHI: **solo inglés** | El dato cruza la frontera a AWS (mitigar con no-retención + BAA + VPC endpoints) |
| **Google Cloud Sensitive Data Protection** | Cloud-only | Tokenización determinista/FPE con reidentificación | Ídem — el dato transita a GCP |
| **Azure AI Language PII / Azure Health De-ID** | Cloud-only | Azure Language: ES confirmado; Azure Health De-ID: 27 entidades incl. 18 HIPAA, *redact* + *surrogate* | Ídem — cloud; Azure Language actúa como *remote recognizer* de Presidio |

**(C) Gateways de IA / prompt-firewalls con DLP en la ruta del prompt** (encaje directo con Federation).

Los que **son** gateways MCP con DLP en la ruta inter-agente:

- **IBM ContextForge** (Apache-2.0) — plugin Presidio integrado; un solo componente OSS cubre *gateway MCP* y *punto de enforcement DLP*. **Ya citado en el stack de referencia del manifiesto Federation.**
- **Lasso MCP Gateway** (MIT) — basado en plugins, Presidio + *secret masking*.
- **LiteLLM** (MIT core) — guardrails Presidio, modo `pre_mcp_call` que mapea a la ruta de llamada MCP de Federation. ⚠️ Hay *issues* abiertos reportando que el *un-masking* de PII se rompe en la ruta nativa de Anthropic con tools — validar el *round-trip* antes de depender de él.
- **Portkey** (gateway MIT + guardrails pluggables). ⚠️ Adquisición por Palo Alto (2026) hacia Prisma AIRS; el gateway MIT debería permanecer, las *features* PII enterprise migran.
- Componibles como plugin dentro de esos gateways: **Pangea AI Guard** (FPE; ahora CrowdStrike), **Pillar Security**, **Arthur Engine** (OSS), **Protect AI LLM Guard** (MIT; ahora PANW / Prisma AIRS).

**(D) DLP / CASB / DSPM-for-AI — el plano de Adoption pura.**

- **Microsoft Purview** (DSPM for AI, DLP for Copilot, Edge inline DLP, Endpoint DLP): documentado como **block / exclude / audit only** en las tres superficies — *no redacta*. La DLP de Copilot no inspecciona archivos subidos directamente al prompt. Edge inline DLP opera sobre una **lista de apps con nombre** (ChatGPT consumer, Gemini, DeepSeek, Perplexity…) y, **a fecha de la lista publicada (mayo 2026), Claude no figura** — hueco relevante para uno de los cuatro productos diana; Microsoft amplía la lista, re-verificar.
- **Netskope** (redacción inline real, vía proxy SSE) e **Island** (redacción en navegador) — las dos excepciones verificadas que sí enmascaran.
- **Zscaler / Palo Alto AI Access Security / Skyhigh / Forcepoint**: bloqueo + coaching + (Zscaler) aislamiento de navegador. Redacción transparente *no confirmada*.
- **Cisco AI Defense + Secure Access**, **Prompt Security / SentinelOne** (extensión de navegador, *shadow-AI*), **Zenity** (integra con Copilot Studio / ChatGPT Enterprise), **Credal** (plataforma-contenedor de asistentes con redacción in-platform): los pocos que añaden control en Adoption sin proxy programático, vía un plano de enforcement distinto.

### 2.3 Shortlist recomendada por fase

**Adoption pura (sin proxy):**
1. **Tier/contrato** correcto (ver §3) — el control más barato y fiable.
2. **El CASB/DLP que la organización ya posea** para *block + coach* (Purview + Edge si hay M365 E5; si no, el SSE existente).
3. **Herramienta de des-identificación sancionada como paso previo manual**: Presidio (MIT, gratis) para PII; John Snow Labs o Azure Health De-ID si hay PHI clínico en español — respaldado por disciplina y formación.
4. Si se necesita redacción transparente sin construir un proxy: **Island** (navegador) o **Netskope** (SSE inline) — aceptando que introducen un intermediario y difuminan la frontera con Federation.

**Federation (gateway programático):**
1. **Presidio Analyzer + Anonymizer** como framework de redacción.
2. **`urchade/gliner_multi_pii-v1`** (Apache-2.0, ES) como *recognizer* externo para mejor *recall* multilingüe en nombres.
3. Modelo **spaCy en español** como motor NLP.
4. **Tokenización reversible** vía el operador `encrypt` de Presidio o el patrón Vault de LLM Guard, para de-anonimizar la respuesta del LLM.
5. Como punto de enforcement: el **plugin Presidio de IBM ContextForge** (ya en el stack de referencia) o el equivalente del gateway elegido.

---

## 3. Capa contractual — licenciamiento por requisito

### 3.1 Matriz de decisión: requisito → qué obtener → qué tier lo provee

*Matriz comparativa por requisito × proveedor; es ancha y se lee mejor en render, no en diff. El detalle con sus caveats de vigencia vive en la prosa de §3.2-§3.4 — las celdas son resúmenes, no la fuente de verdad contractual.*

| Requisito | Qué hay que obtener | OpenAI | Anthropic | Microsoft | Google |
|---|---|---|---|---|---|
| **RGPD / PII** (como encargado) | **DPA** (Art. 28) + SCCs o residencia | DPA para API, Enterprise, Business | DPA (con SCCs) auto-incorporado en los Términos Comerciales (Team, Enterprise, API) | DPA de Microsoft (*Products and Services DPA*); Microsoft como encargado | *Cloud Data Processing Addendum* (CDPA) — Vertex y Workspace |
| **No-entrenamiento por defecto** | Cláusula de no-entrenamiento | **Sí** en API y todos los tiers de negocio; **NO** en consumer (entrena por defecto, opt-out) | **Sí** en API / Team / Enterprise / Gov; **NO** en Free/Pro/Max (entrena por defecto desde 2025 salvo opt-out) | **Sí** M365 Copilot EDP, Azure OpenAI, Copilot Studio | **Sí** Vertex y Gemini for Workspace; **NO** app Gemini consumer (opt-out) |
| **HIPAA / PHI** | **BAA** firmado | API (`baa@openai.com`, sin contrato enterprise) y ChatGPT Enterprise/Edu *sales-managed*; **NO** Business ni consumer | API HIPAA-ready y Claude Enterprise HIPAA-activado; **NO** Free/Pro/Max/Team/Console | M365 Copilot (BAA — **excluye búsqueda web/Bing**); Azure OpenAI HIPAA-eligible | Vertex / Gemini Enterprise vía **BAA de Google Cloud**; Workspace BAA cubre features concretas (**excluye Gemini in Chrome, NotebookLM**); AI Studio gratuito y Gemini consumer **NO** |
| **Zero Data Retention** | ZDR aprobado por el proveedor | API: ZDR para endpoints elegibles, **previa aprobación**; tiers ChatGPT: retención admin-controlada (~30 días), no ZDR | ZDR per-org, *sales-approved*, solo ciertas APIs (Messages, Token Counting) + Claude Code; UIs Team/Enterprise/Console **no** ZDR | Azure OpenAI *modified abuse monitoring* (verificable `ContentLogging=false`); M365 Copilot: dentro del límite del servicio, no ZDR por petición | Vertex: ZDR por solicitud (deshabilitar caché 24h + opt-out de *abuse logging*) |
| **Residencia UE** | Residencia *at-rest* + procesamiento regional | Enterprise/Edu: *at-rest* en al menos 10 regiones (incl. Europa/UK; lista en expansión — verificar) sin coste; inferencia US o Europa | **API solo `us`/`global`; workspace geo solo `us` — NO hay residencia UE first-party.** Para UE usar **Bedrock** (eu-central-1) o **Vertex** (eu) | EU Data Boundary (**excluye búsqueda web y modelos Anthropic**); Azure DataZone / regional | Vertex DRZ/MLP US y EU multi-region; Workspace Data Regions US/EU |
| **FedRAMP** | Autorización del *servicio* | **FedRAMP 20x Moderate** (Enterprise + API, 2026) | Vía Bedrock (FedRAMP High + IL4/5), Vertex (High + IL2), Claude for Government (High ATO) | Azure OpenAI: **FedRAMP High + DoD IL4/5/6** (la cobertura más amplia) | Vertex / Gen-AI: **FedRAMP High** (primer gen-AI en lograrlo) |

*Dos instrumentos contractuales más, enumerados en la tesis (§1) y que esta matriz no desglosa por proveedor porque se regulan dentro del DPA de cada uno: la **notificación de brechas** (RGPD Art. 33-34 — verificar plazos) y el régimen de **subencargados** (Art. 28 — verificar la lista y el derecho de objeción). Revisarlos al firmar el DPA.*

### 3.2 La corrección clave sobre SOC 2 (y otras certificaciones de proveedor)

SOC 2 Type II **no es algo que el cliente "obtiene" para sus conversaciones**. Es una *atestación* de un auditor (CPA) sobre los controles de un *proveedor* (no una certificación), de uso restringido, que se comparte normalmente bajo NDA. El cliente solo puede:

1. **Seleccionar un proveedor** que tenga un informe SOC 2 relevante y revisarlo bajo NDA (OpenAI: periodo ene–jun 2025, cubre API/Enterprise/Edu/Team, vía `trust.openai.com`; Anthropic: SOC 2 Type II bajo NDA en `trust.anthropic.com`).
2. **Implementar los CUECs** (*Complementary User Entity Controls*) que el informe del proveedor asigna al cliente — no son opcionales.

El mismo patrón rige con **ISO 27001 / 42001** (cada parte se certifica a sí misma: exige la del proveedor *y* mantén la tuya) y con **FedRAMP** (autoriza el *servicio*; un cliente no puede hacer "FedRAMP-compliant" por contrato un LLM no autorizado). El error frecuente — *"nuestro proveedor tiene SOC 2, luego cumplimos"* — es falso: es un insumo a tu propio cumplimiento, no un sustituto.

### 3.3 La vía de aprovisionamiento cambia quién es el encargado

Dato crítico para el DPO: aprovisionar el mismo modelo por vías distintas cambia *con quién contratas*.

- **Claude vía Amazon Bedrock:** firmas el **BAA/DPA con AWS**; AWS es el encargado; Anthropic es proveedor de modelo *sin acceso* a prompts/completions. El BAA propio de Anthropic **no aplica**. Es la vía más limpia para residencia UE estricta (eu-central-1) y la más fuerte para gobierno (FedRAMP High + IL4/5).
- **Claude vía Google Vertex AI:** dependes del **DPA/BAA de Google Cloud**; Google es el encargado. Mejor vía verificada de residencia UE hoy (multi-region eu / `europe-westN`).
- **Claude vía API first-party:** firmas el **BAA/DPA de Anthropic**; Anthropic es el encargado.
- **Claude vía Microsoft Foundry (preview):** atípico — factura por Azure, pero la inferencia corre en infraestructura de Anthropic como *encargado independiente* bajo términos de Anthropic. HIPAA / residencia UE **no confirmados**; residencia UE objetivo 2026. Tratar como *preview* y verificar contractualmente.

### 3.4 La trampa de los tiers consumer

El contraste más importante y el mayor riesgo de cumplimiento: **el tier consumer entrena con los datos del usuario por defecto**.

- **OpenAI Free/Plus/Pro/Go:** entrena por defecto (opt-out en *Data Controls*). Sin BAA, sin DPA, sin residencia.
- **Anthropic Free/Pro/Max:** tras el cambio anunciado el 28 de agosto de 2025 (con fecha límite de decisión el 8 de octubre de 2025), las conversaciones se usan para entrenar salvo opt-out; el opt-in extiende la retención a 5 años.
- **App Gemini consumer:** la actividad puede usarse para entrenar modelos generativos salvo opt-out; un subconjunto se revisa por humanos y, si se selecciona, se retiene hasta **3 años** desconectado de la cuenta y **no se borra** al borrar la actividad. Sin BAA. No para PHI.

Todos los tiers de negocio/empresa de los cuatro proveedores **no entrenan por defecto**. La regla de política es directa, y de hecho ya aparece en el ejemplo de Marco Regulatorio de Myrmion: **prohibir los tiers consumer/gratuitos para cualquier dato de cliente u organización.**

---

## 4. Mapa requisito → controles (capa técnica vs capa contractual)

| Régimen | Capa técnica (de-id / DLP) | Capa contractual (licenciamiento) |
|---|---|---|
| **RGPD** | Minimización (Art. 5(1)(c)), *privacy by design* (Art. 25). La seudonimización **reduce** riesgo pero sigue en ámbito; solo la anonimización irreversible saca del ámbito. La **EIPD/DPIA (Art. 35)** documenta la suficiencia de la des-identificación en tratamientos de IA de alto riesgo | **Base jurídica (Art. 6)** como control previo + **DPA (Art. 28)** + SCCs o residencia UE + cláusula de no-entrenamiento. El responsable conserva la carga de demostrabilidad (Art. 5(2)) |
| **LOPDGDD / AEPD** | Igual que RGPD + **evaluación documentada de la eficacia de la anonimización** (la AEPD distingue duramente anonimización vs seudonimización); los **datos de menores** activan garantías reforzadas (consentimiento parental) y típicamente EIPD | Igual que RGPD, supervisado por AEPD; residencia en España/EEE como mitigación de transferencia |
| **EU AI Act** | No es de-id. Aporta: aviso de interacción IA, marcado legible-por-máquina de contenido sintético (Art. 50, aplicable 2 ago 2026 — calendario sujeto a revisión, p. ej. Digital Omnibus Package; verificar fechas vigentes), *logging* | Trasladar las *assurances* de nivel-modelo del proveedor GPAI (documentación, resumen de datos de entrenamiento, Code of Practice). El *deployer* conserva su deber de transparencia |
| **HIPAA** | **Puerta de salida real**: Safe Harbor (18 identificadores) o Expert Determination convierte PHI en no-PHI → sin BAA por esa vía. El *recall* es crítico | Si llega PHI al modelo: **BAA obligatorio, innegociable**. ZDR / no-entrenamiento complementarios |
| **SOC 2 Type II** | No des-identifica nada — asegura los controles del proveedor | Atestación *del proveedor*; el cliente la revisa bajo NDA e **implementa los CUECs**. No es algo que el cliente "obtenga" |
| **ISO 27001 / 42001** | Exigen controles (manejo de datos, cifrado, gobernanza de datos de IA); el de-id es una *implementación* de esos controles | Certificado que cada parte mantiene para su propio sistema de gestión; exigir el del proveedor **y** mantener el propio. Complementa, no sustituye al DPA/BAA |
| **PCI-DSS** | **Puerta de salida real**: tokenizar/truncar el PAN antes del envío **puede sacar o reducir el ámbito** si la tokenización cumple los criterios (Req. 3) y lo valida el QSA/adquirente | Si el proveedor toca datos de tarjeta: acuerdo escrito + matriz de responsabilidad + AOC del proveedor. El control barato es el técnico |
| **FedRAMP** | No des-identifica; el de-id puede bajar la categorización de impacto y, por tanto, el *baseline* | Autorización **del servicio** (vía GovCloud/regiones gov). ATO de la agencia; el cliente conserva los controles configurables |

---

## 5. Cómo se conecta esta guía con el Marco de Modelado

Esta guía es material de referencia. Las **decisiones** de cada organización viven en sus artefactos del Marco de Modelado:

- **Capa 1 — [Marco Regulatorio](../../templates/adoption/marco-regulatorio.md).** Es donde la organización registra, como artefacto operativo y auditable: (a) qué transformación técnica de des-identificación se exige antes de enviar cada categoría de dato a IA, quién la ejecuta y con qué herramienta (sub-sección *Transformación técnica de des-identificación exigida antes de procesar con IA*); y (b) qué instrumento contractual — DPA, BAA, ZDR, residencia — tiene firmado, con qué proveedor, en qué tier y por qué vía de aprovisionamiento (sub-sección *Matriz de licenciamiento por requisito de cumplimiento*). El [ejemplo de Consultora Modelo](../../templates/adoption/marco-regulatorio-ejemplo.md) muestra ambas rellenadas.
- **Capa 2 — Constitución Corporativa.** Reafirma como compromiso cultural las restricciones que la organización aplicaría aunque la regulación las relajara (p. ej. "nunca enviamos datos de cliente a un tier consumer").
- **Myrmion Federation.** La redacción inline transparente — imposible en Adoption pura — se materializa aquí como un *policy template* del gateway: *"datos de salud identificables no cruzan al modelo"* se traduce a un plugin de des-identificación que detecta y redacta antes de la llamada inter-agente, anclado en el stack de referencia (Presidio sobre IBM ContextForge).

La jerarquía manda: ninguna herramienta ni contrato de esta guía releva a la organización de las obligaciones del Marco Regulatorio. La guía dice *qué controles existen*; el Marco Regulatorio dice *cuáles aplica esta organización y cómo*.

---

## 6. Advertencias y caveats

- **Verificar términos vigentes antes de contratar.** Las condiciones de BAA, ZDR, residencia y *features* elegibles cambian con frecuencia; el contrato firmado es la única fuente de verdad. Ningún proveedor publica *rate card* utilizable salvo los hiperescalares.
- **Consolidación 2025-2026 entre comerciales** — verificar propiedad/empaquetado actual: Lakera→Check Point; Prompt Security→SentinelOne; Protect AI y Portkey→Palo Alto (Prisma AIRS); Pangea→CrowdStrike; Aporia→Coralogix; Gretel→NVIDIA; Private AI→Limina AI (rebrand). Pesar contra la preocupación de *lock-in* del framework.
- **Residencia UE first-party de Anthropic no existe hoy** (API solo `us`/`global`, workspace geo `us`). Para residencia UE de Claude verificada: Bedrock eu-central-1 o Vertex eu. Foundry UE es objetivo 2026, no garantía.
- **EU AI Act Art. 50**: aplicable desde el 2 de agosto de 2026; las guías de implementación detalladas (marcado/etiquetado) no estaban en texto final a la fecha de esta investigación.
- **El *recall* de las herramientas de de-id es auto-reportado por el proveedor.** Validar en *tus* datos en español y clínicos antes de seleccionar. **Ninguna herramienta garantiza capturar todo el PII/PHI** — defensa en profundidad obligatoria; no apoyar una afirmación de Safe Harbor en una sola herramienta sin verificación.
- **La cobertura en español es un diferenciador y una trampa.** Presidio, NeMo, scrubadub y DataFog vienen en inglés por defecto y necesitan un modelo español + *context words* localizadas. Multilingüe *out-of-the-box*: piiranha (NC-ND, descartar para uso comercial) y `urchade/gliner_multi_pii-v1` (Apache-2.0, usable). Único de-id de PHI clínico en español de grado regulatorio: John Snow Labs (comercial).
- **Microsoft Edge inline DLP** opera sobre una lista de apps con nombre y, a fecha de la lista publicada (mayo 2026), **Claude no figura** — hueco para uno de los cuatro productos diana en bloqueo directo. Microsoft declara que la lista crecerá: re-verificar.
- **Microsoft Foundry (Claude)** es *preview*; HIPAA/DPA/residencia no confirmados desde fuente primaria.
- Mantener en todo momento el disclaimer del framework: **no es asesoría legal; la interpretación jurídica sigue siendo del DPO o de la función jurídica.**

---

## Referencias (fuentes primarias, mayo 2026)

*Selección de fuentes primarias usadas en esta guía. Verificar vigencia antes de decidir.*

**Licenciamiento y cumplimiento de proveedor**
- OpenAI — Enterprise privacy: https://openai.com/enterprise-privacy/ · Trust portal: https://trust.openai.com/ · BAA: https://help.openai.com/en/articles/8660679-how-can-i-get-a-business-associate-agreement-baa-with-openai · Data residency: https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt · FedRAMP: https://openai.com/index/openai-available-at-fedramp-moderate/
- Anthropic — Trust center: https://trust.anthropic.com/ · Certificaciones: https://privacy.claude.com/en/articles/10015870-what-certifications-has-anthropic-obtained · BAA: https://privacy.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers · DPA: https://privacy.claude.com/en/articles/7996862-how-do-i-view-and-sign-your-data-processing-addendum-dpa · ZDR: https://privacy.claude.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to · Cambio consumer 2025: https://www.anthropic.com/news/updates-to-our-consumer-terms · Claude en Bedrock (FedRAMP High): https://www.anthropic.com/news/claude-in-amazon-bedrock-fedramp-high · Claude en Foundry: https://www.anthropic.com/news/claude-in-microsoft-foundry
- Microsoft — M365 Copilot Enterprise Data Protection: https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection · Azure OpenAI data, privacy & security: https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy · EU Data Boundary: https://learn.microsoft.com/en-us/privacy/eudb/eu-data-boundary-learn · Products and Services DPA: https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA
- Google — Workspace AI privacy: https://workspace.google.com/security/ai-privacy/ · Vertex AI data governance: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/data-governance · Vertex AI residencia: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/data-residency · Google Cloud + HIPAA: https://cloud.google.com/security/compliance/hipaa

**Capa técnica (de-id / DLP / gateways)**
- Microsoft Presidio: https://github.com/microsoft/presidio/ · Idiomas: https://microsoft.github.io/presidio/analyzer/languages/ · GLiNER: https://microsoft.github.io/presidio/samples/python/gliner/
- NeMo Guardrails: https://github.com/NVIDIA-NeMo/Guardrails
- Microsoft Purview DLP para apps de IA: https://learn.microsoft.com/en-us/purview/ai-other-apps · Browser DLP: https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn
- Skyflow LLM Privacy Vault: https://www.skyflow.com/post/generative-ai-data-privacy-skyflow-llm-privacy-vault · Protecto: https://www.protecto.ai/product/privacy-vault/ · Tonic Textual: https://www.tonic.ai/solutions/use-case/llm-privacy-proxy
- Lasso (MCP gateway OSS): https://www.lasso.security/resources/open-source-mcp-gateway-security · IBM Guardium AI Security: https://www.ibm.com/products/guardium-ai-security

**Regímenes regulatorios**
- HHS — De-identification (Safe Harbor / Expert Determination): https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html
- PCI SSC — PAN masking/truncation: https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/how-can-an-entity-meet-pci-dss-requirements-for-pan-masking-and-truncation-if-it-has-migrated-to-8-digit-bins/
- FedRAMP — baselines: https://www.schellman.com/blog/federal-compliance/fedramp-baselines-low-moderate-and-high

---

*Guía de protección de datos en la adopción de IA — versión 1.0. Documento vivo del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Esta guía complementa el [manifiesto de Myrmion Adoption](./manifesto.md) y se materializa operativamente en la plantilla del [Marco Regulatorio](../../templates/adoption/marco-regulatorio.md) (Capa 1). Para el contexto del ecosistema completo, consultar el [manifiesto paraguas](../manifesto.md); para la federación programática donde vive la redacción inline, el [manifiesto de Myrmion Federation](../federation/manifesto.md).*
