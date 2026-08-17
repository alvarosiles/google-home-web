# google-home-web

Panel web moderno para **diseñar, crear, administrar y organizar** rutinas, comandos y automatizaciones de Smart Home, usando el modelo conceptual:

```
Disparador → Condiciones → Acciones
```

Google Home es la primera integración soportada, pero la arquitectura está pensada para admitir otras plataformas (LG webOS, SmartThings, Philips Hue, Alexa, Home Assistant, Chromecast, etc.) sin acoplar el motor de automatizaciones a ninguna de ellas en particular.

## Estado del proyecto

🚧 **Etapa 1 — Arquitectura y estructura.**
Este repositorio contiene únicamente la organización del proyecto (carpetas, archivos base y documentación). Todavía **no** hay lógica funcional: sin autenticación, sin comunicación real con dispositivos, sin integraciones activas y sin rutinas ejecutables.

## Documentación

Toda la documentación de arquitectura vive en [docs/](docs/):

- [docs/architecture.md](docs/architecture.md) — visión general de la arquitectura
- [docs/data-model.md](docs/data-model.md) — modelo interno de automatizaciones
- [docs/automations.md](docs/automations.md) — rutinas, triggers, conditions, actions
- [docs/integrations.md](docs/integrations.md) — cómo se conectan integraciones externas
- [docs/google-home.md](docs/google-home.md) — integración Google Home
- [docs/api.md](docs/api.md) — comunicación frontend/backend
- [docs/installation.md](docs/installation.md) — instalación
- [docs/development.md](docs/development.md) — flujo de desarrollo
- [docs/contributing.md](docs/contributing.md) — guía de contribución

## Estructura del código

```
src/            Frontend (interfaz visual, componentes, páginas)
src/automations Motor de automatizaciones (modelo de rutinas)
src/triggers    Disparadores
src/conditions  Condiciones
src/actions     Acciones
src/devices     Representación genérica de dispositivos
src/integrations Integraciones externas (Google Home, etc.)
src/storage     Persistencia de rutinas y configuración
src/api         Cliente de comunicación con el backend
src/config      Configuración de la aplicación
src/utils       Utilidades compartidas
server/         Backend (servicios del lado del servidor)
docs/           Documentación del proyecto
```

Ver [docs/architecture.md](docs/architecture.md) para el detalle de cada carpeta y el flujo entre capas.
