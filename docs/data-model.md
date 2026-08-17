# Modelo de datos

El modelo interno de automatización es independiente de cualquier integración. Las integraciones traducen desde/hacia este modelo, nunca al revés.

## Routine

| Campo | Descripción |
|---|---|
| `id` | Identificador único |
| `name` | Nombre de la rutina |
| `description` | Descripción |
| `status` | Estado (activa / inactiva) |
| `triggers` | Lista de `Trigger` |
| `conditions` | Lista de `Condition` |
| `actions` | Lista de `Action` |
| `settings` | Configuración propia de la rutina |
| `createdAt` | Fecha de creación |
| `updatedAt` | Fecha de modificación |

## Trigger

Tipos conceptuales: comando de voz, horario, fecha, evento, dispositivo, estado de dispositivo, evento externo.

## Condition

Tipos conceptuales: hora, día, estado de dispositivo, valor, comparación, condición múltiple.

## Action

Tipos conceptuales: encender dispositivo, apagar dispositivo, cambiar volumen, cambiar canal, ejecutar comando, esperar, ejecutar otra acción, ejecutar varias acciones.

## Device

Representación genérica de un dispositivo Smart Home, sin campos específicos de ninguna plataforma. Cada integración mapea sus propios dispositivos a esta forma común.

---

Ver [automations.md](automations.md) para cómo se relacionan estas entidades y [integrations.md](integrations.md) para cómo una integración traduce este modelo a una plataforma concreta.

> Nota: en esta etapa este documento describe el modelo conceptual. La implementación de tipos/interfaces se hará en una etapa posterior.
