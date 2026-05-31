<table>
<tr>
<td width="140" valign="top">
<img src="../../assets/myrmion-logo.png" alt="Myrmion" width="120">
</td>
<td valign="top">

# Myrmion Federation — Runbook de retirada de agente (ejemplo)

**Versión 1.0**

*Ejemplo completamente relleno del [runbook de retirada de agente](./runbook-retirada-agente.md), ambientado en la organización ficticia **Consultora Modelo S.L.** Muestra la retirada de un agente comercial de primera generación que se consolida en uno nuevo. No es normativo: ilustra cómo se ejecuta el runbook. Los valores (hashes, identidades, `correlationId`) son ficticios.*

</td>
</tr>
</table>

---

## Contexto del ejemplo

**Consultora Modelo S.L.** es la consultora ficticia que usamos en todo el corpus para ilustrar Federation. Tiene seis agentes departamentales en producción. Este ejemplo muestra la retirada del agente **`urn:myrmion:agent:consultora-modelo:comercial:cotizaciones-v1`**, una primera generación del agente comercial de cotizaciones que se consolida en el agente vigente de propuestas (`urn:myrmion:agent:consultora-modelo:comercial:propuestas`).

El motivo es una **consolidación**: las dos capacidades de cotización rápida del agente `cotizaciones-v1` se han absorbido, rediseñadas, dentro del agente `propuestas`, que ya pertenece al corredor comercial→legal. El agente viejo deja de tener sentido y se retira.

- Su responsable de dominio es **Fonseca** (Dirección Comercial), que autoriza la retirada y confirma que la capacidad ya está cubierta por el agente nuevo.
- El agente legal del corredor lo custodia **Riera** (Asesoría Jurídica). Su agente de dictámenes tenía a `cotizaciones-v1` en `dependsOn` por una integración antigua, así que recibe notificación (§5).
- La plataforma de federación ejecuta los pasos técnicos.

Como `cotizaciones-v1` es de criticidad `media`, **no** requiere la firma de quien custodia la Constitución (esa firma solo se exige para criticidad `alta` o `critica`).

---

## 0. Metadatos del documento

| Campo | Valor |
|---|---|
| Organización | Consultora Modelo S.L. |
| Versión del documento | 1.0 |
| `agentId` que se retira | `urn:myrmion:agent:consultora-modelo:comercial:cotizaciones-v1` |
| Motivo de la retirada | Consolidación en `comercial:propuestas` (capacidad absorbida y rediseñada) |
| Fecha de inicio de la retirada | 2026-06-22 |
| Fecha efectiva (estado `retirado`) | 2026-06-29 |
| Ejecutor (plataforma de federación) | Plataforma de Federación (equipo SRE) |
| Custodio de dominio que autoriza | Fonseca (Dirección Comercial) |
| Firma adicional (si criticidad alta/critica) | No aplica (criticidad `media`) |

---

## 1. Identificación del agente y su contexto

### 1.1 Datos del agente que se retira

| Campo del descriptor | Valor |
|---|---|
| `agentId` | `urn:myrmion:agent:consultora-modelo:comercial:cotizaciones-v1` |
| `displayName` | Agente Comercial — Cotizaciones (v1, legacy) |
| `domain` | `comercial` |
| `criticality` | `media` |
| `lifecycleStatus` actual | `activo` (se llevará a `deprecated` en la §2) |
| `capabilities` que desaparecen | `cotizar_rapido`, `estimar_alcance` (ambas reimplementadas en `comercial:propuestas`) |

El agente `cotizaciones-v1` lleva en producción desde la primera federación de Consultora Modelo. Su capacidad de cotización rápida quedó solapada cuando el agente `propuestas` incorporó una generación de primeras versiones más completa. Mantener los dos genera ambigüedad (¿a cuál enruta una cotización?) y un riesgo de drift de coherencia entre agentes del mismo dominio.

### 1.2 Quién depende de este agente

*Consulta al service registry: descriptores cuyo `dependsOn` contiene `urn:myrmion:agent:consultora-modelo:comercial:cotizaciones-v1`.*

| `agentId` dependiente | Dominio | Custodio de ese agente | Capacidad que consume |
|---|---|---|---|
| `urn:myrmion:agent:consultora-modelo:legal:dictamenes` | legal | Riera (Asesoría Jurídica) | `estimar_alcance` (para acotar el dictamen) |
| `urn:myrmion:agent:consultora-modelo:comercial:propuestas` | comercial | Fonseca (Dirección Comercial) | `cotizar_rapido` (ya migrado a capacidad interna) |

Solo dos agentes lo declaran en `dependsOn`. El de `propuestas` ya no lo necesita (absorbió la capacidad), pero su descriptor todavía lo lista; hay que actualizarlo. El de `dictamenes` sí lo invocaba ocasionalmente y debe reapuntar a la nueva capacidad de `propuestas`.

### 1.3 Capacidad huérfana

La capacidad **no queda huérfana**: `cotizar_rapido` y `estimar_alcance` ya están reimplementadas dentro de `comercial:propuestas` con la versión de Constitución vigente. Antes de iniciar la retirada, la plataforma confirma con Fonseca que el agente `propuestas` cubre los dos casos de uso que cubría `cotizaciones-v1`, y con Riera que el agente de dictámenes puede obtener la estimación de alcance del agente `propuestas`. Resuelto el reemplazo, la retirada procede.

---

## 2. Pre-check de cadenas en curso (bloqueante)

### 2.1 Procedimiento del pre-check

El 2026-06-22 la plataforma marca `cotizaciones-v1` como `deprecated`, configura el gate para que ninguna cadena nueva enrute a él, y abre una ventana de drenaje de cinco días hábiles —dimensionada a la cadena comercial→legal más larga observada en el dominio, que rara vez supera las 48 horas, con margen.

### 2.2 Checklist del pre-check

- [x] `lifecycleStatus` cambiado a `deprecated` en el registry (2026-06-22 09:00).
- [x] El gate ya no enruta cadenas nuevas a este agente (invocación de prueba rechazada con «destino deprecated»).
- [x] Consulta de observabilidad por `correlationId` activos ejecutada; lista de cadenas en curso registrada abajo.
- [x] Todas las cadenas en curso han terminado, escalado o caducado.
- [x] Segunda consulta (2026-06-27) confirma **cero** cadenas activas que dependan del agente.
- [x] Ventana de drenaje cerrada y documentada (inicio 2026-06-22 09:00 — cierre 2026-06-27 18:00).

### 2.3 Cadenas en curso detectadas

| `correlationId` | `businessCaseId` | Estado al detectar | Cómo se resolvió | Cerrada (fecha/hora) |
|---|---|---|---|---|
| `7b1c2d3e-…` | `lead-2026-0188` | en curso, esperando `estimar_alcance` | terminó normalmente (dictamen emitido) | 2026-06-23 11:42 |
| `9f4a5b6c-…` | `lead-2026-0190` | en curso, cotización pendiente | re-enrutada manualmente a `comercial:propuestas` | 2026-06-24 16:05 |
| `2e8d7c6b-…` | `lead-2026-0192` | iniciada, sin avanzar | caducó por inactividad (TTL de cadena) | 2026-06-26 00:00 |

Tres cadenas tocaban a `cotizaciones-v1` al iniciar la retirada. Dos terminaron solas, una se re-enrutó a mano al agente nuevo. Ninguna quedó rota. El pre-check pasa a verde el 2026-06-27.

---

## 3. Deregister del service registry

### 3.1 Procedimiento

Con el pre-check en verde, el 2026-06-29 la plataforma da de baja `cotizaciones-v1` del service registry. El descriptor se conserva para archivado (§6); el `agentId` queda reservado en estado retirado, no liberado.

### 3.2 Checklist

- [x] Deregister ejecutado en el service registry (CF-02) el 2026-06-29 10:00.
- [x] El agente no aparece en consultas de descubrimiento.
- [x] El `agentId` resuelve a estado `retirado`, no a «no encontrado».
- [x] El registry conserva el `agentId` reservado (no liberado, no reasignable).

---

## 4. Revocación de la identidad

### 4.1 Procedimiento

Inmediatamente después del deregister, la plataforma revoca en el IdP la identidad criptográfica apuntada por el `identityRef` de `cotizaciones-v1`. Como las credenciales de Consultora Modelo tienen TTL de una hora, aun sin revocación expirarían pronto; la revocación cierra la ventana al instante.

### 4.2 Checklist

- [x] Identidad apuntada por `identityRef` revocada en el IdP (CF-04) el 2026-06-29 10:05.
- [x] Una llamada de prueba con esa identidad se rechaza en la verificación, no en la lógica de negocio.
- [x] Confirmado que ninguna credencial viva del agente sigue siendo aceptable (revocación efectiva, no solo programada).

> **Nota de agnosticismo.** Consultora Modelo usa un mecanismo concreto de identidad mutua que satisface las tres propiedades de CF-04; ese detalle —cuál es y cómo se revoca— vive en su ficha de stack en el apéndice, no en este runbook. Lo que el runbook exige es el efecto: ninguna credencial del agente retirado vuelve a autenticarse.

---

## 5. Notificación a los agentes dependientes

### 5.1 Procedimiento

La plataforma notifica a Riera (agente de dictámenes) y a Fonseca (agente de propuestas), con la fecha efectiva (2026-06-29) y la indicación de que la capacidad se reubica en `comercial:propuestas`. Cada custodio actualiza el `dependsOn` de su descriptor, lo que re-dispara su gate de coherencia.

### 5.2 Registro de notificaciones

| `agentId` dependiente | Custodio notificado | Fecha de aviso | `dependsOn` actualizado | Confirmado |
|---|---|---|---|---|
| `urn:myrmion:agent:consultora-modelo:legal:dictamenes` | Riera (Asesoría Jurídica) | 2026-06-23 | Sí — reapunta a `comercial:propuestas` | Sí |
| `urn:myrmion:agent:consultora-modelo:comercial:propuestas` | Fonseca (Dirección Comercial) | 2026-06-23 | Sí — elimina la entrada (capacidad ya interna) | Sí |

Ambos dependientes confirmaron antes de la fecha efectiva. El descriptor de dictámenes pasó de nuevo el gate de coherencia tras reapuntar su `dependsOn`. Una prueba el 2026-06-30 confirmó que una cadena que antes enrutaba a `cotizaciones-v1` ahora resuelve limpiamente a `comercial:propuestas`, sin fallos silenciosos.

---

## 6. Archivado del descriptor y del histórico

### 6.1 Qué se archiva

| Artefacto | Por qué se conserva |
|---|---|
| Descriptor vigente al retirar (`lifecycleStatus: retirado`) | Reconstruir qué capacidades y versión de Constitución tenía `cotizaciones-v1` |
| Histórico de `DecisionHop` con `agentId: …:comercial:cotizaciones-v1` | Las cadenas pasadas lo referencian; el Patrón A de drift los analiza |
| Cadenas de decisión completas en las que intervino | Trazabilidad y defensa de decisiones a posteriori |
| Este runbook relleno | Evidencia de que el proceso de retirada se siguió |

### 6.2 Procedimiento

El descriptor se persiste con `lifecycleStatus: retirado` en el repositorio de gobernanza de Consultora Modelo (no en el registry de producción). Las cadenas históricas que referencian a `cotizaciones-v1` —incluidas las tres del pre-check— se conservan sin alterar. Como el `agentId` queda archivado, una auditoría futura que abra `lead-2026-0188` seguirá resolviendo el eslabón a este agente retirado, no a un homónimo.

### 6.3 Checklist

- [x] Descriptor archivado con `lifecycleStatus: retirado`.
- [x] Histórico de cadenas y `DecisionHop` conservado íntegro (inmutable).
- [x] `agentId` marcado como archivado y no reasignable (regla dura del esquema de identidad §2).
- [x] Este runbook relleno adjuntado al archivo de la retirada.

---

## 7. Checklist consolidado de retirada

- [x] **§1** Agente identificado; dependientes (`dependsOn`) localizados; capacidad huérfana resuelta (absorbida por `comercial:propuestas`).
- [x] **§2** Pre-check de cadenas en curso en verde: `deprecated`, sin entrada nueva, drenado, **cero** cadenas activas.
- [x] **§3** Deregister del service registry (CF-02); `agentId` reservado, no liberado.
- [x] **§4** Identidad (`identityRef`) revocada en el IdP (CF-04); rechazo verificado.
- [x] **§5** Dependientes notificados (Riera, Fonseca); `dependsOn` actualizados; recepción confirmada.
- [x] **§6** Descriptor e histórico archivados (inmutables); `agentId` archivado, nunca reutilizable.
- [x] **§0** Firmas requeridas según criticidad puestas (criticidad `media`: solo Fonseca); fecha efectiva 2026-06-29 registrada.

Retirada completa el 2026-06-29. El `agentId` `urn:myrmion:agent:consultora-modelo:comercial:cotizaciones-v1` queda archivado para siempre; ningún agente futuro lo reutilizará.

---

## 8. Conexión con el resto del corpus

- Esta retirada cierra el ciclo de vida del [esquema de identidad de agente](../../docs/federation/esquema-identidad-agente.md) §8 para `cotizaciones-v1` y aplica su regla del `agentId` no reutilizable (§2).
- Materializa el proceso de retirada del [manifiesto](../../docs/federation/manifesto.md) §5: aquí se ve cómo se evita un agente zombi en concreto.
- La plantilla en blanco de la que deriva este ejemplo es el [runbook de retirada de agente](./runbook-retirada-agente.md).
- El descriptor del agente comercial vigente del corredor está en [descriptor de agente (ejemplo)](./descriptor-agente-ejemplo.md).

---

*Plantilla del ecosistema **Myrmion**. Autor original: Jose Luis Sanchez del Coso. Licencia MIT.*

*Ejemplo no normativo del corpus de Myrmion Federation. Su plantilla en blanco es el [runbook de retirada de agente](./runbook-retirada-agente.md).*
