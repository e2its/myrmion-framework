<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Charter de la Plataforma de Federación (EJEMPLO)

**Versión 1.0 — ejemplo orientativo**

*Ejemplo rellenado del [charter del 4º custodio](./charter-plataforma-federacion.md) para una organización ficticia, **Consultora Modelo S.L.** Muestra cómo se articula el custodio que Federation añade a los tres de Adoption.*

</td>
</tr>
</table>

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Organización | Consultora Modelo S.L. *(ficticia)* |
| Versión del documento | 1.0 |
| Fecha de aprobación | 2026-05-30 |
| Custodio (equipo) | Plataforma de Federación (equipo de SRE, 3 personas) |
| Responsable | Responsable de Plataforma / SRE Lead |
| Aprobado por | Comité de Transformación Digital |

---

## 1. Misión

La Plataforma de Federación de Consultora Modelo es responsable de que los seis agentes departamentales se inter-comuniquen con gobernanza cultural verificable: opera el stack que cumple los [criterios funcionales](../../docs/federation/criterios-funcionales.md), mantiene los policy templates transversales y la pipeline de observabilidad, y custodia el gate de coherencia del service registry. **No** modela la cultura de ningún dominio: eso sigue siendo de cada departamento (la autoridad cultural no se delega).

## 2. Responsabilidades

- **Stack y criterios funcionales (CF-01..CF-06).** Selección, operación y evolución del gateway, service registry, policy engine, identity provider, observabilidad y des-identificación en la ruta. (En Consultora Modelo, el gateway MCP preexistente se reutiliza tras verificar CF-01 — ver ADR-0100.)
- **Policy templates transversales.** Mantiene el catálogo de policies derivadas de la Constitución que aplican a toda la federación (formato en [convenciones-mapping](../../docs/federation/convenciones-mapping-constitucion-policy.md); implementaciones por dialecto en [appendix/policy-templates](../../docs/federation/appendix/policy-templates/)).
- **Gate de coherencia.** Ejecuta las comprobaciones programáticas de [gobernanza-federada](../../docs/federation/gobernanza-federada.md) en cada alta y actualización de descriptor; un agente no entra al registry si no las pasa.
- **Observabilidad y drift.** Opera la pipeline (CF-05) que alimenta los tres [patrones de detección de drift](../../docs/federation/patrones-deteccion-drift.md) y publica las [métricas](../../docs/federation/metricas-federacion.md).
- **Gestión de excepciones.** Garantiza que ninguna excepción se aprueba sin registro completo en el [registro de excepciones](./registro-excepciones.md); distingue conflicto con la Constitución (excepcionable) de conflicto con el Marco (alerta).
- **Ciclo de vida.** Ejecuta alta y retirada de agentes ([runbook de onboarding](./runbook-onboarding-agente.md), [runbook de retirada](./runbook-retirada-agente.md)).

## 3. RACI (resumen)

| Actividad | Plataforma | Transf. Digital | Departamento | Legal/DPO |
|---|---|---|---|---|
| Operar el stack (CF-01..06) | **R/A** | C | I | I |
| Mantener policy templates transversales | **R** | **A** | C | C |
| Gate de coherencia (ejecución) | **R/A** | I | C | I |
| Detección de drift (ejecución) | **R** | **A** | C | C |
| Modelar la cultura del dominio | I | C | **R/A** | I |
| Aprobar excepción a policy de Constitución | C | **A** | C | I |
| Conflicto con el Marco Regulatorio | I | I | I | **R/A** (alerta) |
| Retirar un agente (decisión) | C | I | **A** | I |
| Retirar un agente (ejecución) | **R** | I | C | I |

*(R=Responsable, A=Aprobador, C=Consultado, I=Informado.)*

## 4. Fronteras con los otros custodios

- **Marco Regulatorio (Legal/DPO):** la Plataforma aplica el Marco, no lo interpreta; un conflicto con el Marco se enruta a Legal/DPO como alerta, no como excepción.
- **Constitución (Transformación Digital):** la Plataforma traduce la Constitución a policy templates, pero su contenido y sus cambios son de Transformación Digital.
- **Capas departamentales (cada departamento):** la Plataforma ofrece la capa de coordinación e interoperabilidad; el contenido cultural de cada agente es del departamento.

---

*Ejemplo del ecosistema **Myrmion**. Licencia MIT. Plantilla en blanco: [charter-plataforma-federacion.md](./charter-plataforma-federacion.md). Referencia normativa: [gobernanza-federada.md](../../docs/federation/gobernanza-federada.md).*
