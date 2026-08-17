# Integración: Google Home

Google Home es una integración más, ubicada en `src/integrations/google-home/`. No tiene ningún trato especial dentro del motor de automatizaciones ni en los componentes de interfaz.

## Responsabilidad futura de esta integración

- Autenticación con Google Home (no implementada aún).
- Descubrimiento de dispositivos Google Home → mapeo a `Device` genérico.
- Traducción de `Action` genérica → comandos de Google Home.
- Traducción de eventos/estados de Google Home → `Trigger`/`Condition` genéricos.

## Estado actual

Solo existe la carpeta `src/integrations/google-home/` como punto de extensión. No hay autenticación, ni llamadas a la API de Google Home, ni comunicación real con dispositivos.
