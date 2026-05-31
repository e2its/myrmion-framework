<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Runbook de retirada de agente

**Versión 1.0**

*Plantilla operativa para retirar un agente departamental de la federación sin dejar agentes zombi ni romper cadenas en curso. Materializa el «proceso de retirada» del [manifiesto](../../docs/federation/manifesto.md) §5 y el tramo final del ciclo de vida del [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md) §8: deregister del registry, revocar la identidad, archivar el descriptor y el histórico de cadenas, notificar a los agentes que dependen de él, y dejar el `agentId` ARCHIVADO — nunca reutilizable.*

</td>
</tr>
</table>

---

## Cómo usar esta plantilla

Retirar un agente no es apagar un servidor. En Adoption bastaba con marcar un asistente como deprecated y desmaterializarlo a mano; en Federation el agente es un nodo de una red de invocaciones, y apagarlo sin más deja tres heridas: cadenas en curso que se quedan sin destino, agentes dependientes que siguen invocando a un endpoint muerto, y un histórico de cadenas de decisión que referencia a un agente que ya no existe. El [manifiesto](../../docs/federation/manifesto.md) §5 lo dice sin rodeos: «sin este proceso, las organizaciones acumulan agentes zombi que el sistema sigue invocando años después de que el departamento que los modeló haya desaparecido».

Esta plantilla es el procedimiento que evita las tres heridas. Es un runbook: una secuencia ordenada de pasos con un responsable, una verificación y un punto de no retorno. Se rellena **una vez por retirada** y se archiva junto al descriptor retirado como evidencia de que el proceso se siguió.

**Quién lo ejecuta.** La plataforma de federación (cuarto custodio) coordina y ejecuta los pasos técnicos (deregister, revocación, archivado, notificación). El custodio de dominio del agente —el departamento que lo modeló— autoriza la retirada y confirma que el dominio ya no necesita la capacidad. La retirada de un agente de criticidad `alta` o `critica` exige además la firma de quien custodia la Constitución, porque su salida puede dejar sin cubrir un paso obligatorio de alguna policy (`require-prior-hop`).

**Cuándo se retira un agente.** Reorganización que disuelve el departamento, consolidación de dos agentes en uno, sustitución por una versión rediseñada con nuevo `agentId`, o capacidad que deja de prestarse. La retirada **no** es el mecanismo para un cambio de capacidades del mismo agente —eso es una actualización de descriptor que re-dispara el gate de coherencia (esquema de identidad §8)— ni para una rotación de credenciales —eso es el runbook de rotación de identidad (runbook futuro, aún no publicado).

> **El `agentId` queda archivado, nunca liberado.** Cuando un agente se retira, su `agentId` no se reasigna jamás a otro agente. Las cadenas de decisión históricas referencian agentes por `agentId` (campo `agentId` de cada `DecisionHop`); reutilizar un identificador retirado corrompería la trazabilidad que es la razón de ser del framework. Un agente nuevo que herede la capacidad recibe un `agentId` nuevo. Esto es una regla dura del [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md) §2, no una recomendación.

> **No se retira un agente con cadenas en curso.** Antes de cualquier paso destructivo se ejecuta el pre-check de la §2. Retirar un agente que está a mitad de una cadena de decisiones deja esa cadena rota y sin destino: el peor momento para perder un nodo es cuando una invocación inter-agente ya lo está esperando.

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Organización | *(nombre de la organización)* |
| Versión del documento | *(p. ej. 1.0)* |
| `agentId` que se retira | *(p. ej. `urn:myrmion:agent:<org>:<dominio>:<nombre>`)* |
| Motivo de la retirada | *(reorganización / consolidación / sustitución / capacidad discontinuada)* |
| Fecha de inicio de la retirada | *(YYYY-MM-DD)* |
| Fecha efectiva (estado `retirado`) | *(YYYY-MM-DD)* |
| Ejecutor (plataforma de federación) | *(rol o persona)* |
| Custodio de dominio que autoriza | *(rol — el departamento que modeló el agente)* |
| Firma adicional (si criticidad alta/critica) | *(rol que custodia la Constitución)* |

---

## 1. Identificación del agente y su contexto

*Antes de tocar nada, fijar qué se retira y a qué está conectado. Esta información se lee del descriptor vigente del agente en el service registry.*

### 1.1 Datos del agente que se retira

*Pregunta guía: ¿qué agente, en qué versión de descriptor, y por qué se retira ahora y no en otro momento? El motivo debe ser concreto —«el departamento de X se disuelve el 30 de junio», no «ya no se usa mucho».*

| Campo del descriptor | Valor |
|---|---|
| `agentId` | *(p. ej. `urn:myrmion:agent:<org>:<dominio>:<nombre>`)* |
| `displayName` | *[Espacio para rellenar]* |
| `domain` | *[Espacio para rellenar]* |
| `criticality` | *(baja / media / alta / critica — determina las firmas requeridas)* |
| `lifecycleStatus` actual | *(debe ser `activo` o `deprecated` antes de iniciar)* |
| `capabilities` que desaparecen | *(lista de `toolName` que dejarán de estar disponibles)* |

[Espacio para rellenar]

### 1.2 Quién depende de este agente

*Pregunta guía: ¿qué otros agentes tienen este `agentId` en su campo `dependsOn`? Esta lista determina a quién hay que notificar (§5). Se obtiene consultando el service registry por todos los descriptores cuyo `dependsOn` contiene el `agentId` que se retira.*

| `agentId` dependiente | Dominio | Custodio de ese agente | Capacidad que consume |
|---|---|---|---|
| *(p. ej. `urn:myrmion:agent:<org>:<dominio>:<nombre>`)* | | | |
| | | | |

[Espacio para rellenar]

### 1.3 Capacidad huérfana

*Pregunta guía: la capacidad que prestaba este agente, ¿desaparece, se consolida en otro agente, o la asume un agente nuevo? Si algún dependiente la necesita y nadie la va a prestar, la retirada deja un hueco que romperá sus cadenas. Resolverlo es prerrequisito, no consecuencia, de la retirada.*

[Espacio para rellenar]

---

## 2. Pre-check de cadenas en curso (bloqueante)

*Ningún paso destructivo de las §3–§6 procede hasta que este pre-check esté en verde. Una cadena en curso es una cadena de decisiones que tiene este agente como destino de una invocación pendiente, o como eslabón de una cadena que aún no ha terminado. Retirar el agente mientras una cadena lo espera la rompe sin destino.*

### 2.1 Procedimiento del pre-check

1. **Marcar `deprecated`.** Cambiar `lifecycleStatus` a `deprecated` en el registry. Un agente `deprecated` sigue sirviendo cadenas ya iniciadas pero no debe ser destino de cadenas nuevas (lo gobierna la policy de la §2.3). Esto abre la ventana de drenaje sin cortar de golpe.
2. **Detener la entrada de cadenas nuevas.** Configurar el gate para que ninguna cadena nueva enrute a este agente como destino. Cómo se materializa el corte es del stack (CF-01); el efecto requerido es: cero invocaciones nuevas a partir de este punto.
3. **Drenar las cadenas en curso.** Consultar la observabilidad (CF-05) por `correlationId` activos que tengan a este agente como eslabón pendiente o destino. Esperar a que terminen, escalen o caduquen. La ventana de drenaje se dimensiona a la cadena más larga del dominio.
4. **Verificar cero cadenas activas.** Repetir la consulta hasta que no quede ninguna cadena en curso que dependa del agente. Solo entonces el pre-check pasa a verde.

### 2.2 Checklist del pre-check

- [ ] `lifecycleStatus` cambiado a `deprecated` en el registry.
- [ ] El gate ya no enruta cadenas nuevas a este agente (verificado con una invocación de prueba que debe rechazarse).
- [ ] Consulta de observabilidad por `correlationId` activos ejecutada; lista de cadenas en curso registrada abajo.
- [ ] Todas las cadenas en curso han terminado, escalado o caducado.
- [ ] Segunda consulta confirma **cero** cadenas activas que dependan del agente.
- [ ] Ventana de drenaje cerrada y documentada (fecha/hora de inicio y de cierre).

### 2.3 Cadenas en curso detectadas

*Cada fila es una cadena que tenía a este agente como eslabón pendiente o destino al iniciar la retirada, y cómo se resolvió antes de continuar.*

| `correlationId` | `businessCaseId` | Estado al detectar | Cómo se resolvió | Cerrada (fecha/hora) |
|---|---|---|---|---|
| *550e8400-…* | *lead-2026-0042* | *en curso, esperando este agente* | *terminó normalmente* | *2026-06-28 14:10* |
| | | | | |

*Pregunta guía: ¿cuánto dura la cadena más larga que pasa por este agente? Esa es la ventana mínima de drenaje. Cortar antes deja cadenas rotas; el peor momento para perder un nodo es cuando una invocación ya lo está esperando.*

---

## 3. Deregister del service registry

*Con el pre-check en verde, se da de baja el agente del catálogo federado para que nadie pueda descubrirlo ni enrutar hacia él. Deregister no es borrar: el descriptor se archiva (§4), no se elimina.*

### 3.1 Procedimiento

1. **Confirmar pre-check.** No se ejecuta deregister sin el verde de la §2.
2. **Deregister.** Retirar el agente del service registry de modo que deje de aparecer en descubrimiento (CF-02). El registry conserva el `agentId` en estado retirado, no lo libera.
3. **Verificar invisibilidad.** Una consulta de descubrimiento ya no devuelve el agente; una resolución directa de su `agentId` devuelve «retirado», no «no existe».

### 3.2 Checklist

- [ ] Deregister ejecutado en el service registry (CF-02).
- [ ] El agente no aparece en consultas de descubrimiento.
- [ ] El `agentId` resuelve a estado `retirado`, no a «no encontrado».
- [ ] El registry conserva el `agentId` reservado (no liberado, no reasignable).

---

## 4. Revocación de la identidad

*Deregister quita al agente del catálogo; la revocación de identidad le quita la capacidad de autenticarse. Hasta que la identidad se revoca, un endpoint todavía vivo podría aceptar o emitir llamadas con credenciales válidas.*

### 4.1 Procedimiento

1. **Revocar la identidad referenciada.** Invalidar la identidad criptográfica del agente apuntada por `identityRef` en el IdP (CF-04), de modo que ninguna llamada con esas credenciales se autentique a partir de este punto.
2. **Confiar en el TTL corto como red de seguridad.** Las credenciales de Federation son de vida corta y revocables (CF-04, propiedad 2); aun sin revocación explícita expirarían pronto, pero la revocación cierra la ventana de inmediato.
3. **Verificar el rechazo.** Una invocación de prueba con la identidad del agente retirado debe rechazarse en la verificación de identidad, antes de ejecutar nada.

### 4.2 Checklist

- [ ] Identidad apuntada por `identityRef` revocada en el IdP (CF-04).
- [ ] Una llamada de prueba con esa identidad se rechaza en la verificación, no en la lógica de negocio.
- [ ] Confirmado que ninguna credencial viva del agente sigue siendo aceptable (revocación efectiva, no solo programada).

> **Nota de agnosticismo.** El cuerpo no nombra ningún mecanismo concreto de identidad: exige las tres propiedades de [CF-04](../../docs/federation/criterios-funcionales.md) (verificación criptográfica antes de ejecutar, credenciales de vida corta y revocables, vinculación estable al `agentId`). Cómo se revoca en el IdP concreto vive en [`appendix/stacks-referencia/`](../../docs/federation/appendix/stacks-referencia/), no aquí.

---

## 5. Notificación a los agentes dependientes

*Los agentes que tienen el `agentId` retirado en su `dependsOn` (lista de la §1.2) deben enterarse de que su dependencia desaparece, para que sus custodios reaccionen antes de que una cadena suya intente invocar a un agente que ya no responde.*

### 5.1 Procedimiento

1. **Notificar a cada dependiente.** Avisar al custodio de cada agente de la lista §1.2 de que el `agentId` se retira, con la fecha efectiva y la capacidad que desaparece o dónde se reubica.
2. **Pedir actualización de descriptor.** Cada dependiente debe quitar el `agentId` retirado de su `dependsOn` y, si la capacidad se reubica, apuntar al `agentId` nuevo. Ese cambio de descriptor re-dispara el gate de coherencia del dependiente (esquema de identidad §8).
3. **Confirmar recepción.** La retirada no se cierra hasta que cada dependiente ha confirmado y, si procede, ha actualizado su `dependsOn`.

### 5.2 Registro de notificaciones

| `agentId` dependiente | Custodio notificado | Fecha de aviso | `dependsOn` actualizado | Confirmado |
|---|---|---|---|---|
| *(p. ej. `urn:myrmion:agent:<org>:<dominio>:<nombre>`)* | | | *(sí/no/n.a.)* | *(sí/no)* |
| | | | | |

*Pregunta guía: si un dependiente NO actualiza su `dependsOn`, ¿qué le pasa a su próxima cadena que intente invocar al agente retirado? Debería fallar de forma limpia y trazable (destino retirado), nunca de forma silenciosa. Confirmarlo es parte de cerrar la retirada.*

---

## 6. Archivado del descriptor y del histórico

*Lo que se retira de producción no se borra de la historia. El descriptor y el histórico de cadenas de este agente son evidencia de auditoría: una cadena cuestionada años después puede referenciar al agente por `agentId`, y debe poder reconstruirse.*

### 6.1 Qué se archiva

| Artefacto | Por qué se conserva |
|---|---|
| Descriptor vigente al retirar (`lifecycleStatus: retirado`) | Reconstruir qué capacidades, criticidad y versión de Constitución tenía el agente |
| Histórico de `DecisionHop` con su `agentId` | Las cadenas pasadas lo referencian; el Patrón A de drift los analiza |
| Cadenas de decisión completas en las que intervino | Trazabilidad y defensa de decisiones a posteriori (manifiesto §1) |
| Este runbook relleno | Evidencia de que el proceso de retirada se siguió |

### 6.2 Procedimiento

1. **Fijar el descriptor en `retirado`.** Persistir el descriptor con `lifecycleStatus: retirado` en el archivo de gobernanza (no en el registry de producción).
2. **Archivar el histórico.** Conservar las cadenas de decisión y los `DecisionHop` que referencian al `agentId`, sin alterarlos. Nada se reescribe: la historia es inmutable.
3. **Preservar la legibilidad del `agentId`.** Como el `agentId` queda archivado y nunca se reasigna, cualquier referencia histórica a él sigue resolviendo a este agente retirado, no a un homónimo posterior.

### 6.3 Checklist

- [ ] Descriptor archivado con `lifecycleStatus: retirado`.
- [ ] Histórico de cadenas y `DecisionHop` conservado íntegro (inmutable).
- [ ] `agentId` marcado como archivado y no reasignable (regla dura del esquema de identidad §2).
- [ ] Este runbook relleno adjuntado al archivo de la retirada.

---

## 7. Checklist consolidado de retirada

*Resumen accionable de extremo a extremo. La retirada está completa cuando todas las casillas están marcadas y las firmas de la §0 están puestas. El orden importa: el pre-check precede a todo lo destructivo.*

- [ ] **§1** Agente identificado; dependientes (`dependsOn`) localizados; capacidad huérfana resuelta.
- [ ] **§2** Pre-check de cadenas en curso en verde: `deprecated`, sin entrada nueva, drenado, **cero** cadenas activas.
- [ ] **§3** Deregister del service registry (CF-02); `agentId` reservado, no liberado.
- [ ] **§4** Identidad (`identityRef`) revocada en el IdP (CF-04); rechazo verificado.
- [ ] **§5** Dependientes notificados; `dependsOn` actualizados; recepción confirmada.
- [ ] **§6** Descriptor e histórico archivados (inmutables); `agentId` archivado, nunca reutilizable.
- [ ] **§0** Firmas requeridas según criticidad puestas; fecha efectiva registrada.

*Punto de no retorno: tras el §3 (deregister) y el §4 (revocación), el agente no puede volver a servir sin un alta nueva (con `agentId` nuevo si ya estaba archivado). Por eso el §2 es bloqueante.*

---

## 8. Conexión con el resto del corpus

- La retirada cierra el **ciclo de vida** del [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md) §8 (`activo` → `deprecated` → `retirado`) y aplica su regla del `agentId` no reutilizable (§2).
- Materializa el **proceso de retirada** del [manifiesto](../../docs/federation/manifesto.md) §5 y evita los «agentes zombi» que allí se nombran.
- Las capacidades del stack que usa (deregister, revocación, observabilidad de cadenas) se expresan como [criterios funcionales](../../docs/federation/criterios-funcionales.md): CF-02 (registry y baja sin liberar `agentId`, notificación a `dependsOn`), CF-04 (revocación de identidad), CF-05 (drenaje de cadenas por `correlationId`).
- Es la contraparte del alta: ver [runbook de onboarding de agente](./runbook-onboarding-agente.md). Para sustituir credenciales sin retirar el agente, ver runbook de rotación de identidad (runbook futuro, aún no publicado).
- El histórico que se archiva alimenta el **Patrón A** de drift: ver [playbook de detección de drift](./playbook-deteccion-drift.md).
- La gobernanza de la retirada (quién autoriza, qué firmas) la coordina la plataforma de federación: ver [charter de la plataforma de federación](./charter-plataforma-federacion.md).

---

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Parte del corpus normativo de Myrmion Federation. Cierra el ciclo de vida del [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md); su ejemplo relleno es [runbook-retirada-agente-ejemplo.md](./runbook-retirada-agente-ejemplo.md).*
