# Contribución

## Antes de contribuir

- Respeta la separación entre el motor de automatizaciones y las integraciones (ver [architecture.md](architecture.md)).
- No agregues lógica de una integración concreta (por ejemplo Google Home) fuera de `src/integrations/<plataforma>/`.
- No implementes funcionalidad simulada que aparente estar terminada; si algo no está implementado, déjalo documentado como pendiente.
- Toda carpeta nueva debe tener un propósito claro y documentado, evitando complejidad innecesaria.

## Flujo sugerido

1. Discutir el cambio y su ubicación dentro de la arquitectura.
2. Implementar respetando los límites entre capas.
3. Actualizar la documentación relevante en `docs/`.
