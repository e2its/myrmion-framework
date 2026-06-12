# Myrmion — Apéndice de cumplimiento: calendario regulatorio

**Documento vivo · Estado verificado a junio de 2026**

*Parte del apéndice del [área de cumplimiento](../README.md). Este documento concentra **todo lo que envejece rápido**: fechas de aplicación, estados legislativos y el panorama de certificación. Los [puentes](../puente-iso42001.md) y las [plantillas](../../../templates/compliance/) se mantienen deliberadamente libres de fechas para no envejecer con cada cambio legislativo; cuando necesites una fecha, viene aquí — y **se verifica contra fuentes oficiales antes de usarla en un documento de gobernanza**.*

---

## 1. EU AI Act (Reglamento (UE) 2024/1689) — calendario de aplicación

Estado a junio de 2026, incorporando el acuerdo político provisional del **Digital Omnibus** (mayo de 2026):

| Obligación | Fecha de aplicación | Estado |
|---|---|---|
| Entrada en vigor del Reglamento | 1 de agosto de 2024 | — |
| Prohibiciones (art. 5) y alfabetización en IA (art. 4) | 2 de febrero de 2025 | **Ya aplican** |
| Obligaciones GPAI (arts. 51–56), gobernanza, sanciones | 2 de agosto de 2025 | **Ya aplican** (modelos anteriores a esa fecha: hasta 2-ago-2027) |
| Transparencia (art. 50) | **2 de agosto de 2026** | Se mantiene (régimen transitorio parcial hasta 2-dic-2026 para sistemas existentes y marcado de contenido) |
| Enforcement pleno de GPAI por la Comisión (multas art. 101) | 2 de agosto de 2026 | Se mantiene |
| Alto riesgo del Anexo III (arts. 6 y 8–27) | ~~2-ago-2026~~ → **2 de diciembre de 2027** | **Acuerdo provisional Omnibus — pendiente de adopción formal** |
| Alto riesgo del Anexo I (IA embebida en productos regulados) | ~~2-ago-2027~~ → **2 de agosto de 2028** | **Acuerdo provisional Omnibus — pendiente de adopción formal** |

> **Atención — estado del Digital Omnibus.** La Comisión propuso el paquete en noviembre de 2025; Parlamento y Consejo alcanzaron acuerdo político provisional en mayo de 2026 (fechas fijas, abandonando el mecanismo condicionado a normas armonizadas de la propuesta original). A la fecha de este documento **no está adoptado formalmente ni publicado en el DOUE**: hasta entonces, la fecha jurídicamente vigente para alto riesgo sigue siendo el 2 de agosto de 2026. Una organización prudente planifica con las fechas nuevas pero verifica la publicación en el DOUE antes de relajar ningún plan. Otros cambios del acuerdo: prohibiciones adicionales, registro simplificado para sistemas exentos vía art. 6(3) y flexibilidades para pymes.

**Sanciones (art. 99):** hasta 35 M€ o 7 % del volumen de negocio mundial (prohibiciones del art. 5); 15 M€ o 3 % (resto de obligaciones); 7,5 M€ o 1 % (información engañosa a autoridades). Para pymes, el menor de los dos importes.

## 2. Normas armonizadas del AI Act (CEN-CENELEC JTC21)

- A junio de 2026 **no hay normas armonizadas del AI Act citadas en el DOUE** — por tanto, **ninguna norma (tampoco ISO/IEC 42001) otorga hoy presunción de conformidad** bajo el art. 40.
- La candidata principal es **prEN 18286** (sistema de gestión de calidad para el AI Act; mapea los arts. 11, 17 y 72 vía su Anexo ZA): consulta pública cerrada en enero de 2026, publicación prevista a finales de 2026, citación en el DOUE posterior y a discreción de la Comisión.
- Cuando se publique y se cite, el [puente ISO 42001](../puente-iso42001.md) debe extenderse con el mapeo a prEN 18286. Es el principal elemento de vigilancia de este apéndice.

## 3. ISO/IEC 42001 — panorama de certificación

- **ISO/IEC 42001:2023** — publicada diciembre de 2023. Cláusulas 4–10 + Anexo A (38 controles en 9 objetivos, A.2–A.10).
- **ISO/IEC 42006:2025** (requisitos para organismos de auditoría y certificación de AIMS) — publicada en julio de 2025. Desde finales de 2025 existen **certificaciones acreditadas** (organismos acreditados por ANAB, UKAS, RvA…); el mercado de certificación está operativo y creciendo.
- Normas de soporte: **ISO/IEC 23894:2023** (gestión de riesgos de IA, extiende ISO 31000), **ISO/IEC 42005:2025** (evaluación de impacto de sistemas de IA — la referencia metodológica de la [plantilla de evaluación de impacto](../../../templates/compliance/evaluacion-impacto-ia.md)), **ISO/IEC 5338:2023** (procesos del ciclo de vida del sistema de IA).

## 4. GPAI Code of Practice

Publicado en julio de 2025 (capítulos: transparencia, copyright, seguridad). La adhesión del proveedor del modelo es voluntaria pero facilita demostrar cumplimiento de los arts. 53/55 — criterio útil para la matriz de licenciamiento del [Marco Regulatorio](../../../templates/adoption/marco-regulatorio.md) §3 al elegir proveedor. Desde el 2 de agosto de 2026 la Comisión puede imponer multas GPAI (art. 101).

## 5. Lista de vigilancia

Qué debe comprobar quien mantenga este apéndice (cadencia recomendada: trimestral, y ad hoc ante noticias legislativas):

1. **Publicación del Digital Omnibus en el DOUE** → actualizar la tabla de §1 y avisar a los custodios de Marcos Regulatorios adoptantes.
2. **Publicación de EN 18286 y su citación en el DOUE** → extender el [puente ISO 42001](../puente-iso42001.md) y revisar la [SoA](../../../templates/compliance/declaracion-aplicabilidad-iso42001.md).
3. **Actos de ejecución del art. 50** (formatos de marcado de contenido sintético) → actualizar la [ficha de transparencia](../../../templates/compliance/ficha-transparencia-ia.md).
4. **Plantilla oficial de FRIA** que publique la AI Office (art. 27.5) → alinear la [evaluación de impacto](../../../templates/compliance/evaluacion-impacto-ia.md).
5. **Guías de la Comisión sobre el art. 73** (incidentes graves) → alinear el [runbook de incidentes](../../../templates/compliance/runbook-incidentes-graves.md).

---

*Apéndice del área de cumplimiento de Myrmion — documento vivo, responsabilidad de la comunidad. Como todo el apéndice, envejece rápido: la fecha de la cabecera es parte del contenido.*
