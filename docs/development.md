# Desarrollo

## Reglas de la arquitectura

1. `src/automations`, `src/triggers`, `src/conditions`, `src/actions` y `src/devices` no deben importar nada de `src/integrations`.
2. `src/components` y `src/app` no deben contener lógica específica de Google Home ni de ninguna otra integración — solo conceptos genéricos (`Device`, `Trigger`, `Condition`, `Action`, `Automation`).
3. Toda traducción hacia/desde una plataforma externa vive dentro de su carpeta en `src/integrations/<plataforma>/`.
4. La persistencia (`src/storage`) no debe depender del formato de ninguna integración; guarda y lee el modelo interno.

Ver [architecture.md](architecture.md) para el detalle completo.

> Los scripts de desarrollo (dev server, build, lint, test) se documentarán cuando se agreguen las dependencias del proyecto.
