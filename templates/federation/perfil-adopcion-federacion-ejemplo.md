<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Perfil de Adopción (EJEMPLO)

**Versión 1.0 — ejemplo orientativo**

*Ejemplo rellenado de la [plantilla de Perfil de Adopción](./perfil-adopcion-federacion.md) para una organización ficticia, **Consultora Modelo S.L.** No es una recomendación: es una muestra de cómo se articula un perfil real.*

</td>
</tr>
</table>

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Organización | Consultora Modelo S.L. *(ficticia)* |
| Versión del documento | 1.0 |
| Fecha | 2026-05-30 |
| Custodio del perfil | Responsable de Plataforma de Federación (SRE) |
| Co-firmante | Dirección de Transformación Digital |
| Versión de la Constitución Corporativa vigente | 3.0 (aprobada 2026-01-15) |
| Versión del Marco Regulatorio vigente | 1.4 |

---

## 1. Variables del perfil (VF)

| ID | Variable | Respuesta de Consultora Modelo | Default | ¿Difiere? |
|---|---|---|---|---|
| **VF01** | Nº de agentes departamentales activos | 6 (comercial, legal, finanzas, personas, operaciones, soporte) | ≥5–6 | No |
| **VF02** | Nº de pares que colaboran con frecuencia | 4 (comercial↔legal, comercial↔finanzas, personas↔legal, operaciones↔soporte) | ≥3 | No |
| **VF03** | Protocolo inter-agente | MCP | MCP | No |
| **VF04** | Exposición regulatoria / sector | General + RGPD; datos de cliente C2–C3, sin C4 | General | No |
| **VF05** | Reversibilidad de des-identificación | Reversible para NIF/identificadores de cliente; irreversible para datos de RR. HH. sensibles | Reversible donde aplique | No |
| **VF06** | Stack pre-existente relevante | Gateway MCP comunitario ya en uso para tools internas | Ninguno | **Sí → ADR-0100** |
| **VF07** | Criticidad máxima de dominio | Alta (legal y finanzas) | Alta | No |
| **VF08** | Modelo de despliegue | Contenedores con identidad por carga gestionada, aislamiento de red por dominio y ciclo de vida en GitOps | *(funcional)* | No |
| **VF09** | Volumen de tráfico inter-agente | ~200 llamadas inter-agente/día | Decenas–cientos/hora | No |
| **VF10** | Token `<org>` del namespace | `consultora-modelo` | *(elige la org)* | — |

> **Lectura del perfil:** Consultora Modelo cumple los prerrequisitos de Fase 0 (≥5–6 agentes, ≥3 pares activos, Constitución estable >6 meses). La única desviación del default es VF06 (ya tienen un gateway MCP), que se documenta en el ADR de adopción 0100 y condiciona la Fase 1: se evalúa si el gateway existente cubre [CF-01](../../docs/federation/criterios-funcionales.md) antes de considerar alternativas.

---

## 2. Perfil YAML

```yaml
# perfil-federacion.yaml
organization: "Consultora Modelo S.L."
date: "2026-05-30"
owner: "Responsable de Plataforma de Federación (SRE)"

profile:
  VF01_num_agentes: 6
  VF02_pares_colaboran: 4
  VF03_protocolo: MCP
  VF04_exposicion_regulatoria: general-rgpd
  VF05_deid_reversible: where-applicable   # NIF reversible; RR.HH. sensible irreversible
  VF06_stack_preexistente: "gateway MCP comunitario"
  VF07_criticidad_max: alta
  VF08_despliegue: "contenedores con identidad por carga + aislamiento por dominio + ciclo de vida GitOps"
  VF09_volumen_inter_agente: medium       # ~200/día
  VF10_org_namespace: "consultora-modelo"

desviaciones_del_default:
  - VF06: "gateway MCP ya presente -> evaluar cobertura de CF-01 antes de elegir stack"
adrs_de_adopcion:
  - "0100-reutilizar-gateway-mcp-existente.md"
```

---

## 3. Decisiones cerradas asumidas

Consultora Modelo asume sin reservas los tres principios del manifiesto §2, la política fail-closed ante incompatibilidad de Constitución (con default `escalar`) y el carácter no excepcionable del Marco Regulatorio.

---

*Ejemplo del ecosistema **Myrmion**. Licencia MIT. Plantilla en blanco: [perfil-adopcion-federacion.md](./perfil-adopcion-federacion.md). Referencia normativa: [perfil-adopcion-federacion.md (cuerpo)](../../docs/federation/perfil-adopcion-federacion.md).*
