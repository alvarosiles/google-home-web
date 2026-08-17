Quiero crear un proyecto llamado **google-home-web**.

El objetivo del proyecto es crear una aplicación web moderna para diseñar, crear, administrar y organizar rutinas, comandos y automatizaciones relacionadas con Google Home y dispositivos de Smart Home.

## IMPORTANTE

En esta primera etapa quiero que trabajes **únicamente en la estructura del proyecto**.

NO implementes todavía la lógica de Google Home.

NO implementes todavía APIs.

NO implementes autenticación.

NO implementes comunicación con dispositivos.

NO implementes rutinas funcionales.

NO generes funcionalidades simuladas que parezcan terminadas.

Primero quiero una arquitectura limpia y escalable.

---

# OBJETIVO GENERAL

La aplicación deberá convertirse posteriormente en un panel web desde el cual el usuario pueda crear automatizaciones mediante una interfaz visual.

La idea conceptual es:

**Disparador → Condiciones → Acciones**

Por ejemplo:

"Cuando diga una determinada frase"

↓

"Si se cumple determinada condición"

↓

"Ejecutar varias acciones"

Las acciones podrían involucrar diferentes tipos de dispositivos y servicios.

---

# ARQUITECTURA

Quiero que la arquitectura esté diseñada para separar claramente:

### Frontend

Interfaz visual de la aplicación.

### Automations

Lógica relacionada con rutinas y automatizaciones.

### Triggers

Disparadores de las rutinas.

### Conditions

Condiciones que pueden evaluarse antes de ejecutar acciones.

### Actions

Acciones que puede ejecutar una rutina.

### Devices

Representación de dispositivos Smart Home.

### Integrations

Integraciones externas.

Google Home debe considerarse una integración y no debe estar mezclado directamente con toda la aplicación.

### Storage

Persistencia de rutinas, configuraciones y preferencias.

### API

Comunicación entre frontend y backend cuando sea necesaria.

### Server

Servicios backend.

### Config

Configuraciones de la aplicación.

### Utils

Funciones auxiliares reutilizables.

---

# DISEÑO MODULAR

Quiero que el proyecto pueda crecer posteriormente.

Por ejemplo, inicialmente:

Google Home

Pero posteriormente podría soportar:

* Google Home
* LG webOS
* Samsung SmartThings
* Philips Hue
* Alexa
* Home Assistant
* Chromecast
* Otros dispositivos y servicios

Por eso NO quiero que toda la arquitectura dependa directamente de Google Home.

Debe existir una separación clara entre:

**Motor de automatizaciones**

y

**Integraciones externas.**

---

# SISTEMA DE AUTOMATIZACIONES

La arquitectura debe dejar preparado un sistema conceptual para:

### Rutinas

Una rutina debe poder tener:

* Nombre
* Descripción
* Estado
* Disparadores
* Condiciones
* Acciones
* Configuración
* Fecha de creación
* Fecha de modificación

### Triggers

Preparar la arquitectura para diferentes tipos de disparadores:

* Comando de voz
* Horario
* Fecha
* Evento
* Dispositivo
* Estado de dispositivo
* Evento externo

### Conditions

Preparar soporte para:

* Hora
* Día
* Estado de dispositivo
* Valor
* Comparaciones
* Condiciones múltiples

### Actions

Preparar soporte para:

* Encender dispositivo
* Apagar dispositivo
* Cambiar volumen
* Cambiar canal
* Ejecutar comando
* Esperar
* Ejecutar otra acción
* Ejecutar varias acciones

No implementes estas funciones todavía.

Solo deja la arquitectura preparada.

---

# INTERFAZ

La aplicación deberá tener posteriormente una interfaz moderna tipo dashboard.

Quiero dejar preparada la estructura para páginas como:

### Dashboard

Resumen general.

### Rutinas

Lista de rutinas creadas.

### Crear rutina

Constructor visual de rutinas.

### Editar rutina

Editor de una rutina existente.

### Dispositivos

Lista y administración de dispositivos.

### Integraciones

Administración de servicios externos.

### Configuración

Configuración general de la aplicación.

---

# CONSTRUCTOR VISUAL

Una de las partes más importantes del proyecto será posteriormente un constructor visual de automatizaciones.

La arquitectura debe permitir construir una interfaz conceptual como:

```text
Rutina
│
├── Disparador
│
├── Condiciones
│
└── Acciones
      │
      ├── Acción 1
      ├── Acción 2
      ├── Acción 3
      └── Acción 4
```

El usuario posteriormente debería poder:

* Agregar disparadores
* Agregar condiciones
* Agregar acciones
* Eliminar elementos
* Editar elementos
* Reordenar acciones
* Duplicar acciones
* Activar/desactivar rutinas

Pero en esta primera etapa NO implementes ninguna de esas funciones.

Solo prepara la arquitectura.

---

# DISEÑO DE COMPONENTES

Quiero que la interfaz tenga componentes reutilizables.

Por ejemplo, prepara conceptualmente componentes para:

* Sidebar
* Header
* Dashboard
* Card
* Modal
* Dialog
* Button
* Input
* Select
* Toggle
* Device Card
* Routine Card
* Trigger Card
* Condition Card
* Action Card
* Automation Builder
* Empty State
* Loading State
* Notification
* Status Indicator

No es necesario implementar todos los componentes ahora.

La estructura debe permitir agregarlos posteriormente sin desordenar el proyecto.

---

# RESPONSIVE

La aplicación deberá estar preparada para:

* Desktop
* Laptop
* Tablet
* Smartphone

El diseño deberá permitir posteriormente una experiencia táctil.

---

# TEMAS

Dejar preparada la arquitectura para:

* Dark Mode
* Light Mode

No es necesario implementar todavía el sistema completo de temas.

---

# DATOS

Quiero separar claramente:

**Modelo de datos**

de

**Interfaz**

de

**Persistencia**

de

**Integraciones externas.**

Las rutinas no deben depender directamente de cómo Google Home almacena sus datos.

La aplicación debería trabajar con un modelo interno de automatización.

Posteriormente una integración podría convertir ese modelo al formato necesario.

---

# GOOGLE HOME

Google Home debe estar dentro de una sección de integraciones.

Por ejemplo conceptualmente:

Integrations

→ Google Home

No quiero que componentes de la interfaz tengan lógica específica de Google Home directamente.

La interfaz debe trabajar con conceptos genéricos como:

* Device
* Trigger
* Condition
* Action
* Automation

La integración será responsable posteriormente de traducir esos conceptos a la plataforma correspondiente.

---

# DOCUMENTACIÓN

Crear una estructura preparada para documentación.

Debe incluir documentación para:

* Arquitectura
* Instalación
* Desarrollo
* Automatizaciones
* Integraciones
* Google Home
* Modelo de datos
* API
* Contribución

---

# CALIDAD DEL PROYECTO

Quiero una estructura:

* Limpia
* Profesional
* Modular
* Escalable
* Fácil de mantener
* Fácil de entender
* Preparada para crecimiento

Evita crear una cantidad innecesaria de carpetas.

No quiero una arquitectura excesivamente compleja para un proyecto inicial.

Busca un equilibrio entre simplicidad y escalabilidad.

---

# TAREA

Ahora quiero que hagas lo siguiente:

1. Analiza los requisitos.
2. Diseña la arquitectura del proyecto.
3. Crea físicamente las carpetas necesarias.
4. Crea los archivos base necesarios.
5. Crea los archivos de documentación inicial.
6. Crea un README inicial explicando el propósito del proyecto.
7. Deja comentarios o documentación donde sea necesario para explicar la responsabilidad de determinadas carpetas.
8. Mantén la estructura preparada para futuras implementaciones.

## NO IMPLEMENTAR TODAVÍA

No implementes:

* Google Home API
* OAuth
* Autenticación
* Comunicación con dispositivos
* Rutinas reales
* Automatizaciones reales
* Backend funcional
* Base de datos funcional
* Integraciones reales
* APIs externas
* WebSockets
* Ejecución de comandos

La primera etapa es exclusivamente:

**Arquitectura + estructura + documentación inicial.**

Antes de crear cualquier funcionalidad, quiero poder revisar la estructura completa del repositorio.

Al finalizar, muéstrame:

1. Árbol completo del proyecto.
2. Explicación de cada carpeta.
3. Explicación de los archivos principales.
4. Flujo arquitectónico.
5. Cómo se conectarán posteriormente las integraciones.
6. Cómo crecerá el sistema cuando agreguemos nuevas plataformas.

No agregues funcionalidades que no hayan sido solicitadas.
