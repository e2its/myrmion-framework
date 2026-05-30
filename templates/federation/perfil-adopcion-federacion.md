<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Plantilla de Perfil de Adopción

**Versión 1.0**

*Plantilla para que una organización registre su Perfil de Adopción de Federation — las variables `VF` que, según su contexto, modifican decisiones del framework.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

El cuerpo de Federation está escrito asumiendo un conjunto de respuestas implícitas (cuántos agentes, qué protocolo, qué exposición regulatoria, etc.). Este perfil hace explícitas esas variables para tu organización. Para cada respuesta que difiera del default, revisa el criterio funcional (CF) o el documento que la variable señala y documenta la desviación como **ADR de adopción** (rango `0100+`).

**Quién lo rellena.** El custodio de la plataforma de federación (4º custodio) junto con transformación digital. **Cuándo.** Antes de la Fase 1 (selección de stack), y se revisa en cada fase. **Qué se hace después.** Se versiona en Git junto al resto del modelado y se mantiene vivo.

La referencia normativa de cada variable —su significado y su impacto— está en [perfil-adopcion-federacion.md](../../docs/federation/perfil-adopcion-federacion.md). Esta plantilla solo recoge las respuestas. Para un ejemplo rellenado, ver [perfil-adopcion-federacion-ejemplo.md](./perfil-adopcion-federacion-ejemplo.md).

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Organización | *(nombre)* |
| Versión del documento | *(p. ej. 1.0)* |
| Fecha | *(YYYY-MM-DD)* |
| Custodio del perfil | *(rol — típicamente plataforma de federación)* |
| Co-firmante | *(transformación digital o equivalente)* |
| Versión de la Constitución Corporativa vigente | *(p. ej. 3.0)* |
| Versión del Marco Regulatorio vigente | *(p. ej. 1.4)* |

---

## 1. Variables del perfil (VF)

*Pregunta guía por variable: responde con el dato de tu organización. Si difiere del default, revisa la columna «revisar» y abre un ADR de adopción.*

| ID | Variable | Tu respuesta | Default | Si difiere → revisar |
|---|---|---|---|---|
| **VF01** | Nº de agentes departamentales activos | *(rellenar)* | ≥5–6 | [checklist Fase 0](./checklist-prerrequisitos-fase0.md) |
| **VF02** | Nº de pares que colaboran con frecuencia | *(rellenar)* | ≥3 | [guia-adopcion-por-fases](../../docs/federation/guia-adopcion-por-fases.md) |
| **VF03** | Protocolo inter-agente | *(rellenar)* | MCP | [appendix/mapeo-transporte](../../docs/federation/appendix/mapeo-transporte/) |
| **VF04** | Exposición regulatoria / sector | *(rellenar)* | General | [appendix/drift-recipes](../../docs/federation/appendix/drift-recipes/), CF-06 |
| **VF05** | Reversibilidad de des-identificación requerida | *(rellenar)* | Reversible donde aplique | [CF-06](../../docs/federation/criterios-funcionales.md), [esquema-bloque §5](../../docs/federation/esquema-bloque-contexto-cultural.md) |
| **VF06** | Stack pre-existente relevante | *(rellenar)* | Ninguno | [criterios-funcionales](../../docs/federation/criterios-funcionales.md), [appendix/stacks-referencia](../../docs/federation/appendix/stacks-referencia/) |
| **VF07** | Criticidad máxima de dominio | *(rellenar)* | Alta | [patrones-deteccion-drift](../../docs/federation/patrones-deteccion-drift.md) (cadencia) |
| **VF08** | Modelo de despliegue | *(rellenar)* | *Sustrato con identidad por carga, aislamiento de red y ciclo de vida gestionado* (sin default tecnológico) | [CF-01](../../docs/federation/criterios-funcionales.md), [CF-04](../../docs/federation/criterios-funcionales.md) |
| **VF09** | Volumen de tráfico inter-agente | *(rellenar)* | Decenas–cientos/hora | [metricas-federacion](../../docs/federation/metricas-federacion.md) |
| **VF10** | Token `<org>` del namespace de `agentId` | *(rellenar)* | *(elige la organización)* | [esquema-identidad-agente §2](../../docs/federation/esquema-identidad-agente.md) |

### Preguntas guía complementarias

*VF08 — Modelo de despliegue:* el framework no prescribe Kubernetes ni ningún sustrato concreto. Describe el tuyo en términos funcionales: ¿cómo se da identidad por carga a cada agente? ¿cómo se aísla la red entre agentes? ¿quién gestiona el ciclo de vida (alta, actualización, baja)?

*VF10 — Token `<org>`:* el `agentId` tiene la forma `urn:myrmion:agent:<org>:<dominio>:<nombre>`. `<org>` es **tuyo**: elige un identificador corto y estable de la organización. El framework nunca lo fija.

---

## 2. Plantilla YAML rellenable

```yaml
# perfil-federacion.yaml
organization: "<nombre>"
date: "YYYY-MM-DD"
owner: "<custodio de plataforma de federación>"

profile:
  VF01_num_agentes: 0
  VF02_pares_colaboran: 0
  VF03_protocolo: MCP            # MCP | A2A | mixto
  VF04_exposicion_regulatoria: general
  VF05_deid_reversible: where-applicable
  VF06_stack_preexistente: null
  VF07_criticidad_max: alta
  VF08_despliegue: "sustrato con identidad por carga + aislamiento de red + ciclo de vida gestionado"
  VF09_volumen_inter_agente: medium
  VF10_org_namespace: "<org>"

desviaciones_del_default: []     # cada una → ADR de adopción 0100+
adrs_de_adopcion: []             # rango 0100+
```

---

## 3. Decisiones cerradas (no son variables)

Esto **no** se configura: quien lo rechaza está adoptando otro framework, no Federation.

- Los **tres principios** del manifiesto §2 (compositividad sobre infraestructura existente, cultura propagable, drift como métrica de primera clase).
- La política **fail-closed** ante incompatibilidad de Constitución: si no hay match de `constitutionHash`, la llamada no procede (default: escalado a humano). Se puede endurecer a `rechazar`, nunca relajar a `permitir`.
- La **incompatibilidad de Marco Regulatorio es dura**: no admite excepción.

---

*Plantilla del ecosistema **Myrmion**. Licencia MIT. Referencia normativa: [perfil-adopcion-federacion.md](../../docs/federation/perfil-adopcion-federacion.md). Ejemplo rellenado: [perfil-adopcion-federacion-ejemplo.md](./perfil-adopcion-federacion-ejemplo.md).*
