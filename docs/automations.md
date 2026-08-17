# Automatizaciones

## Concepto

```
Rutina
│
├── Disparador (Trigger)
│
├── Condiciones (Condition[])
│
└── Acciones (Action[])
      │
      ├── Acción 1
      ├── Acción 2
      └── Acción N
```

Una rutina se dispara por un `Trigger`, se evalúa contra sus `Condition`s y, si se cumplen, ejecuta su lista de `Action`s en orden.

## Carpetas relacionadas

- `src/automations/models` — forma de datos de `Routine`.
- `src/automations/engine` — orquestación conceptual (evaluación de condiciones, ejecución de acciones). Sin implementación real todavía.
- `src/triggers` — catálogo de tipos de disparador.
- `src/conditions` — catálogo de tipos de condición.
- `src/actions` — catálogo de tipos de acción.

## Estado actual

Solo existe la estructura de carpetas y los contratos conceptuales descritos en [data-model.md](data-model.md). No hay evaluación ni ejecución real de rutinas.
