# Myrmion Federation — Plantilla de ficha de stack: «<NOMBRE DEL COMPONENTE>»

**Versión 1.0**

*Materializa el contrato de desacoplamiento del [apéndice vivo](./README.md): una ficha fechada que evalúa un componente concreto contra los [criterios funcionales CF-01..CF-06](../criterios-funcionales.md), sin contaminar el cuerpo normativo.*

> **PLANTILLA — NO EDITAR ESTE FICHERO COMO SI FUERA UNA FICHA REAL.**
> Para documentar un componente: **copia** este fichero a `stacks-referencia/<componente>.md`, sustituye todo lo marcado entre `<…>` y rellena cada sección. Borra esta nota y las instrucciones en cursiva del esqueleto. Mantén el banner de vigencia: una ficha sin fecha no sirve.

---

> ## Banner de vigencia
>
> | Campo | Valor |
> | --- | --- |
> | **Componente** | `<nombre del producto / proyecto>` |
> | **Versión evaluada** | `<versión o rango; "rolling" si no versiona>` |
> | **Fecha de revisión** | `<AAAA-MM-DD>` |
> | **Revisor(es)** | `<nombre / handle del/los owner(s) — coincide con CODEOWNERS>` |
> | **Próxima revisión recomendada** | `<AAAA-MM-DD — máx. 6 meses tras la revisión>` |
> | **Estado** | `<vigente | stale | retirado>` |
> | **Licencia (a la fecha)** | `<SPDX o descripción; marca si es "source available" o comercial>` |
> | **Fuente upstream** | `<URL del proyecto / repositorio>` |
>
> *Esta ficha caduca. Si la fecha de revisión es anterior a 6 meses respecto a hoy, trátala como `stale` aunque el campo Estado diga lo contrario. Lo normativo está en el cuerpo ([`../criterios-funcionales.md`](../criterios-funcionales.md)), no aquí.*

---

## 1. Qué es y qué rol cubre

*Pregunta guía: ¿qué es exactamente este componente y qué papel juega en la federación (gateway, service registry, identity provider, policy engine, observabilidad agent-aware, des-identificación/DLP, suite de gobernanza)? Una o dos frases, sin marketing.*

[Espacio para rellenar]

---

## 2. Matriz de cobertura CF-01..CF-06

*Pregunta guía: para cada criterio funcional, ¿este componente lo cubre de forma directa (●), contribuye parcialmente o con integración adicional (◐), o no aplica (○)? Justifica cada celda que no sea ○ contra la checklist del criterio en el cuerpo. No marques ● por una promesa del README: márcalo por una capacidad demostrable frente a la checklist.*

| Criterio | Cobertura | Justificación (qué punto de la checklist cumple / qué le falta) |
| --- | :---: | --- |
| **CF-01** — gateway de llamadas inter-agente | `<● / ◐ / ○>` | [Espacio para rellenar] |
| **CF-02** — service registry federado | `<● / ◐ / ○>` | [Espacio para rellenar] |
| **CF-03** — policy engine | `<● / ◐ / ○>` | [Espacio para rellenar] |
| **CF-04** — identity provider (autenticación mutua con identidad criptográfica verificable) | `<● / ◐ / ○>` | [Espacio para rellenar] |
| **CF-05** — observabilidad agent-aware | `<● / ◐ / ○>` | [Espacio para rellenar] |
| **CF-06** — des-identificación / DLP en la ruta | `<● / ◐ / ○>` | [Espacio para rellenar] |

> Recuerda: ninguna pieza única cubre los seis criterios. Si crees que esta sí, vuelve a leer la checklist de cada criterio en [`../criterios-funcionales.md`](../criterios-funcionales.md). Para CF-04, el cuerpo nunca exige «mTLS» por su nombre: exige las propiedades de identidad criptográfica verificable; evalúa contra ellas.

---

## 3. Cómo se integra con MCP

*Pregunta guía: ¿cómo se relaciona con MCP (gateway, registry, mesh, pieza adyacente)? ¿Requiere algo del mapeo de transporte? ¿Obliga a alguna extensión de protocolo? (Si la obliga, es una señal de alarma: la federación se monta sobre MCP existente, sin extensiones — manifiesto §8.)*

[Espacio para rellenar]

> Si hay detalle de serialización sobre transporte (cómo viaja el bloque de contexto cultural o los `deidToken`), documéntalo en [`mapeo-transporte/`](./mapeo-transporte/) y enlázalo aquí; no lo incrustes en esta ficha. Si aporta implementaciones de policy, van a [`policy-templates/`](./policy-templates/).

---

## 4. Pros

*Pregunta guía: ¿qué hace bien para esta federación? Sé concreto: una ventaja sin contexto no ayuda a decidir.*

- [Espacio para rellenar]
- [Espacio para rellenar]

---

## 5. Contras

*Pregunta guía: ¿qué le falta, qué fricción introduce, qué obliga a construir alrededor? Incluye las lagunas de cobertura de la matriz de la sección 2.*

- [Espacio para rellenar]
- [Espacio para rellenar]

---

## 6. Madurez

*Pregunta guía: ¿en qué punto de su ciclo de vida está? Considera versión/estabilidad de API, frecuencia de releases, tamaño y actividad de la comunidad, casos de producción conocidos, calidad de documentación.*

| Señal | Lectura |
| --- | --- |
| Estabilidad de API / versionado | [Espacio para rellenar] |
| Cadencia de releases | [Espacio para rellenar] |
| Tamaño / actividad de comunidad | [Espacio para rellenar] |
| Casos de producción conocidos | [Espacio para rellenar] |
| Calidad de documentación | [Espacio para rellenar] |

**Veredicto de madurez:** `<experimental | emergente | consolidado | en mantenimiento | declive>` — [Espacio para rellenar].

---

## 7. Riesgo de continuidad (M&A / cambio de licencia / abandono)

*Pregunta guía: ¿qué probabilidad hay de que este componente deje de ser una opción viable a 12-24 meses? Considera respaldo corporativo (¿un solo vendor?), historial de cambios de licencia, riesgo de adquisición que cierre el código, dependencia de un único mantenedor, gobernanza de fundación. Este es el riesgo que el confinamiento de marcas al apéndice existe para absorber: el cuerpo sobrevive aunque este riesgo se materialice.*

| Vector de riesgo | Nivel `<bajo / medio / alto>` | Notas |
| --- | :---: | --- |
| Adquisición / M&A | `<…>` | [Espacio para rellenar] |
| Cambio de licencia (open → source-available / comercial) | `<…>` | [Espacio para rellenar] |
| Abandono / *bus factor* | `<…>` | [Espacio para rellenar] |
| Dependencia de un único *vendor* | `<…>` | [Espacio para rellenar] |
| Gobernanza (proyecto individual vs. fundación) | `<…>` | [Espacio para rellenar] |

**Plan de salida si el riesgo se materializa:** *Pregunta guía: si este componente desaparece o cambia de licencia, ¿con qué se sustituye y cuánto cuesta migrar? Como el cuerpo solo exige el criterio funcional, sustituir el componente no toca la especificación: la respuesta apunta a otra ficha de [`stacks-referencia/`](./stacks-referencia/) que cubra el mismo CF.*

[Espacio para rellenar]

---

## 8. Veredicto

*Pregunta guía: a la fecha de revisión, ¿para qué criterios lo recomendarías, bajo qué condiciones, y qué huecos deja que otra pieza tenga que tapar?*

[Espacio para rellenar]

---

### Enlaces relacionados

- [Apéndice vivo — matriz global y contrato de desacoplamiento](./README.md)
- [Criterios funcionales (CF-01..CF-06)](../criterios-funcionales.md) — definición normativa de las columnas.
- [Regla anti-acoplamiento](../regla-anti-acoplamiento.md) — por qué esta ficha vive en el apéndice y no en el cuerpo.
- [Mapeo de transporte](./mapeo-transporte/) y [policy templates](./policy-templates/) — donde van la serialización y las implementaciones por dialecto.

*Plantilla de ficha de stack — versión 1.0. Parte del corpus en su estructura; el contenido que se rellene es informativo y caduca.*
