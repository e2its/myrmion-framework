# ADR-NNNN — &lt;Título de la decisión, en una frase&gt;

> Plantilla. Copia este fichero, renómbralo a `NNNN-titulo-en-kebab-case.md`, asígnale el siguiente número libre (ver [README](./README.md)) y borra esta cita y todas las notas entre corchetes. No borres los encabezados de sección: forman el contrato del ADR.

| Campo | Valor |
|---|---|
| ADR | NNNN |
| Ámbito | Framework (0001–0099) · Adopción (0100+) — *deja solo el que aplique* |
| Estado | Propuesto |
| Fecha | AAAA-MM-DD |
| Supera a | — *(ADR que esta decisión deja obsoleto, si lo hay)* |
| Superado por | — *(se rellena cuando otro ADR deje obsoleto a este)* |

---

## Contexto

[¿Qué situación obliga a decidir? Describe las fuerzas en juego: qué contrato, qué criterio funcional o qué tensión de diseño está sobre la mesa. Sé concreto y verificable. Si la decisión nace de un problema observado en la federación, descríbelo aquí. No anticipes la decisión: este apartado es el "antes".]

[Espacio para rellenar]

---

## Decisión

[Enuncia la decisión en presente y en voz activa: "Adoptamos…", "El descriptor de agente declara…". Una decisión por ADR. Si la decisión afecta a un contrato o esquema, di **exactamente** qué cambia, sin ambigüedad.]

[Espacio para rellenar]

---

## Alternativas consideradas

[Enumera las opciones que se evaluaron y se descartaron. Para cada una, una línea de por qué se descartó. Un ADR sin alternativas es sospechoso: o no había decisión real, o no se exploró.]

- **Alternativa A** — [descripción]. Descartada porque [motivo].
- **Alternativa B** — [descripción]. Descartada porque [motivo].

[Espacio para rellenar]

---

## Encaje con los tres principios

Toda decisión que da forma a la federación debe rendir cuentas ante los tres principios del [manifiesto §2](../manifesto.md). Declara, para cada uno, si la decisión lo **respeta**, lo **refuerza** o lo **tensiona**. Una tensión no invalida la decisión, pero **obliga** a justificarla y a registrar la deuda que asume.

### Compositividad sobre infraestructura existente

*Pregunta guía: ¿esta decisión se monta sobre lo que el stack ya provee (criterios funcionales CF-01..CF-06), o introduce algo que Federation tendría que reimplementar, una extensión de protocolo o un acoplamiento a un stack concreto?*

[Espacio para rellenar — declara: Respeta / Refuerza / Tensiona, y por qué.]

### Cultura propagable

*Pregunta guía: ¿esta decisión preserva que el contexto cultural viaje íntegro en cada llamada inter-agente (bloque de contexto cultural), o crea un camino por el que la versión de Constitución, los criterios aplicados o la cadena de decisiones puedan perderse o quedar atrás?*

[Espacio para rellenar — declara: Respeta / Refuerza / Tensiona, y por qué.]

### Drift como métrica de primera clase

*Pregunta guía: ¿esta decisión mantiene el drift federado medible y vigilable por los patrones del manifiesto §3.4, o introduce una desviación cultural que dejaría de ser observable?*

[Espacio para rellenar — declara: Respeta / Refuerza / Tensiona, y por qué.]

---

## Consecuencias

[Las consecuencias son los hechos que asumimos al decidir, buenos y malos. No vendas la decisión: descríbela honestamente.]

**Positivas**

- [Qué mejora, qué se desbloquea, qué contrato queda más firme.]

**Negativas o costes**

- [Qué se complica, qué deuda se asume, qué queda peor que antes.]

**Neutras (efectos a vigilar)**

- [Qué cambia sin ser claramente bueno ni malo, pero conviene observar.]

[Espacio para rellenar]

---

## Riesgos

[¿Qué podría salir mal si esta decisión resulta equivocada? Para cada riesgo, su señal de alerta y, si la hay, su mitigación o la condición que dispararía un ADR de reversión.]

- **Riesgo** — [descripción]. Señal de alerta: [qué observaríamos]. Mitigación: [qué haríamos].

[Espacio para rellenar]

---

## Estado

[Repite aquí el estado actual y su justificación de una línea. Cuando este ADR sea superado, actualiza esta sección y la tabla de cabecera (`Superado por`) enlazando el ADR que lo reemplaza; **no edites** el resto del documento. El historial es el valor.]

**Propuesto** — [una línea: en discusión, pendiente de adopción].

---

## Relacionados

- [README de los ADR](./README.md)
- [Manifiesto](../manifesto.md) — los tres principios (§2).
- [Criterios funcionales](../criterios-funcionales.md) — si la decisión toca un CF, enlázalo aquí por su id.
- *(Enlaza los contratos, esquemas o ADR que esta decisión toca: `../esquema-identidad-agente.md`, `../esquema-bloque-contexto-cultural.md`, `../appendix/…`, otros ADR.)*

---

*Myrmion Federation — Plantilla de ADR, versión 1.0. Parte del corpus normativo.*
