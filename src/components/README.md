# src/components

Componentes de interfaz reutilizables, agnósticos de cualquier integración.

- `common/` — Button, Input, Select, Toggle, Modal, Dialog, StatusIndicator, etc.
- `cards/` — RoutineCard, DeviceCard, TriggerCard, ConditionCard, ActionCard.
- `builder/` — piezas del constructor visual de automatizaciones (AutomationBuilder y afines).
- `feedback/` — EmptyState, LoadingState, Notification.

Ningún componente aquí debe importar código de `src/integrations`.
