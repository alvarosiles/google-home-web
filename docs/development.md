# Desarrollo

## Stack técnico propuesto

Decidido para etapas futuras, todavía **sin instalar ni configurar**:

- **Frontend**: React + TypeScript + Vite.
- **Estilos**: CSS Modules (o Tailwind, a confirmar al implementar `src/styles`), con soporte para Dark/Light Mode vía `src/styles/themes`.
- **Backend**: Node.js + TypeScript (Express o Fastify, a confirmar) sobre la estructura ya creada en `server/src/{routes,controllers,services,config}`.
- **Persistencia inicial**: almacenamiento local simple (archivo/JSON) detrás de la abstracción de `src/storage`, reemplazable después por una base de datos real.
- **Comunicación frontend↔backend**: REST vía `src/api`, documentado en [api.md](api.md).

Esta elección no implica ningún cambio en la arquitectura descrita en [architecture.md](architecture.md) — solo fija con qué tecnología se implementará cada capa cuando llegue esa etapa.

## Reglas de la arquitectura

1. `src/automations`, `src/triggers`, `src/conditions`, `src/actions` y `src/devices` no deben importar nada de `src/integrations`.
2. `src/components` y `src/app` no deben contener lógica específica de Google Home ni de ninguna otra integración — solo conceptos genéricos (`Device`, `Trigger`, `Condition`, `Action`, `Automation`).
3. Toda traducción hacia/desde una plataforma externa vive dentro de su carpeta en `src/integrations/<plataforma>/`.
4. La persistencia (`src/storage`) no debe depender del formato de ninguna integración; guarda y lee el modelo interno.

Ver [architecture.md](architecture.md) para el detalle completo.

> Los scripts de desarrollo (dev server, build, lint, test) se documentarán cuando se agreguen las dependencias del proyecto.
