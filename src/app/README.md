# src/app

Páginas y enrutamiento de la aplicación.

- `router/` — configuración de rutas (pendiente de implementación).
- `layout/` — layout general: Sidebar, Header.
- `pages/dashboard/` — resumen general.
- `pages/routines/` — listado de rutinas.
- `pages/routine-builder/` — constructor/editor visual de rutinas.
- `pages/devices/` — administración de dispositivos.
- `pages/integrations/` — administración de integraciones externas.
- `pages/settings/` — configuración general de la app.

Estas páginas solo deben usar conceptos genéricos (`Device`, `Trigger`, `Condition`, `Action`, `Automation`), nunca lógica específica de una integración.
