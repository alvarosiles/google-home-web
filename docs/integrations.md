# Integraciones

Una integración traduce el modelo genérico de automatización (`Device`, `Trigger`, `Condition`, `Action`) al formato/API de una plataforma externa concreta, y viceversa.

```
src/integrations/
├── shared/         Contratos e interfaces comunes a toda integración
└── google-home/     Primera integración soportada
```

## Contrato de una integración (conceptual)

Cada integración deberá exponer, en etapas futuras:

- Descubrimiento de dispositivos → mapeo a `Device` genérico.
- Traducción de `Action` genérica → comando propio de la plataforma.
- Traducción de `Trigger`/`Condition` de estado de dispositivo → eventos propios de la plataforma.

## Agregar una nueva integración

1. Crear `src/integrations/<nombre-plataforma>/`.
2. Implementar el contrato definido en `src/integrations/shared/`.
3. Registrar la integración para que quede disponible en la sección **Integraciones** de la app.

Ninguna otra parte del sistema (`src/automations`, `src/components`, páginas del dashboard) necesita cambios al agregar una integración nueva — ese es el propósito de esta separación.

Ver también [google-home.md](google-home.md).
