# src/automations

Núcleo del motor de automatizaciones.

- `models/` — forma de datos de `Routine` (ver [docs/data-model.md](../../docs/data-model.md)).
- `engine/` — orquestación conceptual: evaluación de condiciones y ejecución de acciones de una rutina.

Este módulo no depende de ninguna integración externa. Trabaja únicamente con los tipos genéricos definidos en `src/triggers`, `src/conditions`, `src/actions` y `src/devices`.
