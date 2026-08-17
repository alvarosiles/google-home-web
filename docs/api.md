# API (frontend ↔ backend)

`src/api` contiene el cliente que usará el frontend para comunicarse con `server/` cuando sea necesario (por ejemplo, persistir rutinas o consultar el estado de dispositivos).

`server/` contiene el backend:

```
server/src/
├── routes/         Definición de endpoints (sin implementar aún)
├── controllers/     Manejo de peticiones (sin implementar aún)
├── services/        Lógica de negocio del servidor (sin implementar aún)
└── config/          Configuración del servidor
```

## Estado actual

No hay endpoints, rutas ni lógica de servidor implementados. Esta guía se completará cuando se defina el primer contrato de API real.
