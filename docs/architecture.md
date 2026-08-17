# Arquitectura

## Principio rector

El **motor de automatizaciones** (rutinas, triggers, conditions, actions, devices) es independiente de cualquier **integración externa** (Google Home, Alexa, Home Assistant, etc.). La interfaz solo conoce conceptos genéricos: `Device`, `Trigger`, `Condition`, `Action`, `Automation`. Cada integración es responsable de traducir esos conceptos genéricos a su propia plataforma.

```
        ┌───────────────────────────┐
        │          src/app          │  páginas, layout, router
        └─────────────┬─────────────┘
                       │ usa
        ┌─────────────▼─────────────┐
        │        src/components      │  UI reutilizable
        └─────────────┬─────────────┘
                       │ representa
        ┌─────────────▼─────────────┐
        │   src/automations (core)   │  Routine = Trigger + Condition[] + Action[]
        │   src/triggers              │
        │   src/conditions            │
        │   src/actions                │
        │   src/devices                │
        └─────────────┬─────────────┘
                       │ persiste vía
        ┌─────────────▼─────────────┐
        │        src/storage         │  abstracción de persistencia
        └─────────────┬─────────────┘
                       │ sincroniza vía
        ┌─────────────▼─────────────┐
        │          src/api           │  cliente frontend ↔ backend
        └─────────────┬─────────────┘
                       │
        ┌─────────────▼─────────────┐
        │           server/           │  backend (rutas, controllers, servicios)
        └─────────────┬─────────────┘
                       │ delega en
        ┌─────────────▼─────────────┐
        │      src/integrations      │  Google Home, y futuras plataformas
        └───────────────────────────┘
```

## Carpetas

### `src/app`
Páginas y enrutamiento de la aplicación (Dashboard, Rutinas, Crear rutina, Editar rutina, Dispositivos, Integraciones, Configuración) y el layout general (sidebar, header).

### `src/components`
Componentes de interfaz reutilizables, agnósticos de cualquier integración: `common/` (Button, Input, Select, Toggle, Modal, Dialog…), `cards/` (RoutineCard, DeviceCard, TriggerCard, ConditionCard, ActionCard…), `builder/` (piezas del constructor visual de automatizaciones), `feedback/` (EmptyState, LoadingState, Notification, StatusIndicator).

### `src/automations`
Núcleo del motor de automatizaciones: modelos de datos (`models/`) y lógica de orquestación (`engine/`) de una rutina. No depende de ninguna integración concreta.

### `src/triggers`, `src/conditions`, `src/actions`
Definiciones de los tipos de disparadores, condiciones y acciones soportados conceptualmente por el modelo (ver [automations.md](automations.md)).

### `src/devices`
Representación genérica de un dispositivo Smart Home, independiente de la plataforma que lo provee.

### `src/integrations`
Cada subcarpeta es una integración externa (por ejemplo `google-home/`) responsable de traducir el modelo genérico de automatización al formato/API de su plataforma. `shared/` contiene contratos comunes a todas las integraciones.

### `src/storage`
Abstracción de persistencia de rutinas, configuración y preferencias, desacoplada del backend concreto que se use.

### `src/api`
Cliente usado por el frontend para comunicarse con `server/` cuando sea necesario.

### `src/config`
Configuración general de la aplicación (constantes, variables de entorno tipadas, etc.).

### `src/utils`
Funciones auxiliares reutilizables sin dependencias de dominio.

### `src/styles`
Sistema de temas (`themes/` prepara Dark Mode / Light Mode) y estilos base.

### `server/`
Backend: `routes/`, `controllers/`, `services/`, `config/`. Punto de entrada para lógica de servidor futura (autenticación, comunicación con integraciones, etc.).

### `docs/`
Documentación del proyecto.

## Crecimiento futuro

Agregar una nueva plataforma (p. ej. Philips Hue) implica:

1. Crear `src/integrations/philips-hue/`.
2. Implementar la traducción de `Device`/`Action` genéricos al SDK de Philips Hue.
3. Registrar la integración en el listado de integraciones disponibles.

Ningún cambio es necesario en `src/automations`, `src/components` ni en las páginas del dashboard.
