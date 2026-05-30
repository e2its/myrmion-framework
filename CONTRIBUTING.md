# Cómo contribuir a Myrmion

Gracias por contribuir. Myrmion se publica bajo licencia MIT. Estas son las contribuciones más valiosas y las reglas que mantienen la calidad del ecosistema.

## Qué contribuir

**Myrmion Adoption**
- Apéndice de mapeo a productos comerciales conforme evolucionan.
- Plantillas sectoriales (sanidad, financiero, sector público, manufacturing).
- Casos de uso anonimizados.

**Myrmion Federation**
- Actualizaciones del [apéndice vivo](./docs/federation/appendix/): fichas de stacks de referencia, policy-templates por dialecto, recetas de drift sectoriales, mapeo de transporte por protocolo.
- Catálogos de policy templates derivados de Constituciones reales (anonimizados).
- Casos de corredor end-to-end anonimizados.

## La regla que no se negocia: agnosticismo del cuerpo

Myrmion Federation separa **dos clases de contenido**:

- **Cuerpo normativo** (`docs/federation/` y `templates/federation/`): criterios funcionales, esquemas, convenciones, gobernanza y método. **Envejece lento. No nombra marcas.**
- **Apéndice vivo** (`docs/federation/appendix/`): stacks, implementaciones por dialecto, transporte por protocolo. **Envejece rápido. Es el único lugar con nombres de producto.**

Antes de tocar el cuerpo, aplica el **test de pertenencia** de la [regla anti-acoplamiento](./docs/federation/regla-anti-acoplamiento.md): *¿la frase sigue siendo verdadera si cambio el stack entero?* Si nombra un producto, una versión o un dialecto, va al apéndice, no al cuerpo.

### Checklist para un PR al cuerpo

- [ ] Sin nombres de producto (salvo la excepción única de la regla §2: mención ilustrativa «p. ej. …» que enlace al apéndice).
- [ ] Sin snippets de configuración ni dialectos de policy/transporte.
- [ ] Todo concepto técnico nuevo se ancla a un criterio funcional (CF-01..CF-06).
- [ ] Cualquier capacidad de stack requerida la podrían satisfacer ≥2 implementaciones distintas.
- [ ] Los esquemas no añaden campos con nombre o valor específico de un protocolo.
- [ ] Enlaces relativos resuelven; se hereda versión al citar Constitución o Marco Regulatorio.
- [ ] No afirma vigencia temporal (eso va al apéndice con banner de fecha y revisor).

### Contribuir al apéndice

El apéndice es de la comunidad: revisión más ligera, ritmo del ecosistema. Cada entrada lleva **banner de vigencia** (fecha + revisor) y, cuando aplica, su matriz de cobertura de criterios funcionales. Usa la [plantilla de ficha de stack](./docs/federation/appendix/_plantilla-entrada-stack.md).

## Estilo

Español, registro del manifiesto (preciso, sin relleno). Términos técnicos en inglés inline solo cuando son el término establecido (MCP, service mesh, policy engine). Las plantillas siguen el patrón socrático de `templates/adoption/` (cabecera con logo, «Cómo usar esta plantilla», «0. Metadatos», preguntas guía).

## Licencia

Al contribuir, aceptas que tu aportación se publique bajo la licencia [MIT](./LICENSE) del proyecto.
