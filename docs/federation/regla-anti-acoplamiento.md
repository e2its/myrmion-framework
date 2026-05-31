# Myrmion Federation — Regla anti-acoplamiento

**Versión 1.0**

*La norma transversal que mantiene el cuerpo del framework libre de marcas y el apéndice como único lugar donde aparecen productos concretos. Es lo que cumple la promesa del [manifiesto](./manifesto.md) §4 y §8 — «criterios, no marcas» — y lo que protege al framework de envejecer con cada release del stack subyacente.*

---

## Por qué existe esta regla

El manifiesto declara (§10) que Federation «se diseña explícitamente para no envejecer con el ecosistema sobre el que se monta». Esa propiedad no se mantiene sola: cada contribución bienintencionada que mete el nombre de un producto, una versión o una sintaxis de dialecto en el cuerpo del framework lo acopla un poco más, hasta que un día el framework habla de Cedar 4.x y nadie recuerda por qué no se puede cambiar a otra cosa.

Esta regla es la barrera. Define **qué frase puede estar en el cuerpo** (envejece lento) y **qué frase pertenece al apéndice** (envejece rápido, lo mantiene la comunidad), y da un procedimiento para resolver los casos dudosos. Es normativa: aplica a todo `docs/federation/` y `templates/federation/`, y los revisores la usan como criterio de aceptación de PRs.

---

## 1. El test de pertenencia (regla madre)

Ante cualquier frase candidata a entrar en el cuerpo, aplicar estas preguntas **en orden**. La primera que dispare decide.

1. **¿Nombra un producto, una marca, una versión o una sintaxis de vendor?** → No va al cuerpo. Va al [apéndice](./appendix/) (o al catálogo de policy templates si es una implementación).
2. **¿Sería falsa u obsoleta si el stack subyacente cambiara o desapareciera** (otro gateway, otro policy engine, otro motor de DLP)? → No va al cuerpo. Va al apéndice con banner de vigencia.
3. **¿Es un criterio funcional, un esquema, una convención, una pregunta guía o un método?** → Va al cuerpo.
4. **¿Afirma una vigencia temporal** («a fecha de hoy», «la versión actual de X soporta…»)? → Va al apéndice con banner de fecha y revisor.

El enunciado corto del test, el que se cita en revisión: **¿sigue siendo verdadera tras cambiar el stack entero?** Si la respuesta es no, no es cuerpo.

---

## 2. La excepción única

El cuerpo puede nombrar un producto **solo** en uno de estos dos modos, y nunca con más densidad que el propio manifiesto:

- **(a) Como ejemplo entre paréntesis,** señalado como tal: «un policy engine con lenguaje declarativo (p. ej. Cedar u OPA)». El techo es el del manifiesto §4 («idealmente Microsoft Presidio»): una mención ilustrativa, nunca una recomendación normativa.
- **(b) Como enlace al apéndice:** «ver implementaciones candidatas en [`appendix/stacks-referencia/`](./appendix/stacks-referencia/)».

Cualquier mención que no encaje en (a) o (b) — un snippet de configuración, una instrucción de instalación, una afirmación sobre el comportamiento de una versión concreta — está fuera del cuerpo por definición.

---

## 3. Casos canónicos de traducción

Para que la regla sea operable, estos son los reemplazos que más se repiten al abstraer el modelo de implementación de referencia:

| En vez de (acoplado) | El cuerpo dice (agnóstico) | Lo concreto vive en |
|---|---|---|
| «autenticación mTLS entre agentes» | «autenticación mutua con identidad criptográfica verificable» (las 3 propiedades de [CF-04](./criterios-funcionales.md)) | `appendix/stacks-referencia/` |
| «policy en Rego/Cedar» | «policy declarativa evaluable en runtime» ([CF-03](./criterios-funcionales.md)) + pseudo-policy neutral | `appendix/policy-templates/` |
| «el bloque viaja en el header `_meta` de MCP» | «el bloque viaja como metadatos propagados por el gateway» ([esquema del bloque](./esquema-bloque-contexto-cultural.md)) | `appendix/mapeo-transporte/` |
| «Istio AuthorizationPolicy con principals…» | «el gateway evalúa policy antes de ejecutar la llamada» ([CF-01](./criterios-funcionales.md)) | `appendix/stacks-referencia/` |
| «Presidio detecta PII en…» | «des-identificación en la ruta con motor vendor-neutral» ([CF-06](./criterios-funcionales.md)) | `appendix/stacks-referencia/` |
| «MLflow registry de bundles» | (fuera de scope: es de la arquitectura de referencia, no de federación) | no entra |

El caso canónico de traducción «mTLS → propiedades» (§3) merece énfasis propio: **el cuerpo nunca exige «mTLS» por su nombre.** Exige las tres propiedades de identidad criptográfica de [CF-04](./criterios-funcionales.md): (1) el receptor verifica criptográficamente la identidad del emisor antes de ejecutar; (2) la credencial es de vida corta y revocable; (3) la identidad es vinculable de forma estable al `agentId`. mTLS las satisface; otros mecanismos también.

---

## 4. Neutralidad de los esquemas

Los esquemas del cuerpo ([identidad de agente](./esquema-identidad-agente.md) y [bloque de contexto cultural](./esquema-bloque-contexto-cultural.md)) son contratos, no serializaciones. Reglas específicas:

- **Ningún campo lleva un nombre o un valor específico de MCP** (ni de ningún protocolo). El esquema describe qué información viaja y con qué semántica; cómo se serializa y por qué header viaja es transporte, y el transporte vive en `appendix/mapeo-transporte/`. Esto es lo que preserva la portabilidad a A2A que promete el manifiesto §9.
- **El contrato es la tabla de campos + su semántica + el contrato de hash.** El YAML o el JSON que aparezcan en el cuerpo son ilustrativos; la serialización a un registry concreto es apéndice.
- **Sin extensiones de protocolo.** Todo lo que el cuerpo describe se materializa sobre los mecanismos que el protocolo base (MCP) ya provee — metadata, headers, descriptors (manifiesto §8: «No es un protocolo nuevo»). Cualquier propuesta que requiera cambiar MCP se rechaza.

---

## 5. La salvaguarda estructural: CODEOWNERS dual

La regla se sostiene sobre una asimetría de fricción deliberada:

- **`docs/federation/` y `templates/federation/`** (cuerpo) → custodios del framework. Un PR aquí exige aprobación de un custodio y pasa el checklist de la §6.
- **`docs/federation/appendix/`** (vivo) → mantenedores de la comunidad. Un PR aquí necesita una revisión ligera y puede entrar al ritmo del ecosistema.

Que sea más fácil contribuir al apéndice que al cuerpo es la garantía de que el contenido volátil fluye hacia donde debe estar. Si una contribución al cuerpo huele a apéndice, el custodio la redirige; no la reescribe.

---

## 6. Checklist de PR al cuerpo (bloqueante)

Un PR a `docs/federation/` o `templates/federation/` no se acepta hasta que cumple todo esto:

- [ ] No introduce nombres de producto salvo la excepción única (§2).
- [ ] No introduce snippets de configuración ni de dialecto de policy/transporte.
- [ ] Todo concepto técnico nuevo se expresa primero como criterio funcional (CF) o se ancla a uno existente.
- [ ] Toda capacidad de stack que se requiera podría satisfacerla **al menos dos** implementaciones distintas (si solo una puede, es acoplamiento encubierto).
- [ ] Los esquemas no añaden campos con nombre/valor específico de un protocolo.
- [ ] Las referencias cruzadas resuelven y heredan versión cuando citan Constitución o Marco Regulatorio.
- [ ] No afirma vigencia temporal (eso va al apéndice con banner).
- [ ] Mantiene el estilo del corpus: español, términos técnicos en inglés inline solo cuando son el término establecido (MCP, service mesh, policy engine…).

---

## 7. Lista de control para el linter (opcional pero recomendado)

Si el repo añade un linter de CI, esta es la lista negra mínima de tokens que deben fallar el build si aparecen **fuera de** `docs/federation/appendix/` (y fuera de la excepción §2): nombres de gateway, policy engine, service mesh, IdP, motor de DLP, distribución de Kubernetes y cloud concretos del ecosistema actual. La lista vive y se mantiene junto al linter, no aquí, porque la lista misma envejece — pero el principio (cero marcas en el cuerpo) no.

---

*Regla anti-acoplamiento de Myrmion Federation — versión 1.0. Parte del corpus normativo. Su contrapartida es el [apéndice vivo](./appendix/), único lugar del repo donde los productos concretos tienen nombre.*
