## 🛪 EFI Django 2025: *Aerolíneas Splinter* 🧑‍✈️

**Actualización del día lunes 16/07/2025**:

Se implementaron las funcionalidades de **inicio de sesión** y **registro**, las cuales incluyen sus respectivos formularios y templates.  
También se añadieron el template base y la página de inicio del sitio web.

A continuación, se detalla el contenido de esta nueva actualización del proyecto.

## ⚙️ Funciones

#### Get all users

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `-` | `-` |          **Este endopoint no requiere parametros** |

#### Get item by id

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int`    | *Este endpoint no requiere parámetros.* |

#### Post (create user)

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`first_name`|    `str`| *Nombre del usuario*. **Requerido.**|
|`last_name`| `str`| *Apellido del usuario.* **Requerido.**|
|`email`| `str`| *Email del usuario.* **Requerido.**|


#### Put (update user)

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int`    | *ID del producto que se desea actualizar.*  **Requerido**|
|`first_name`|    `str`| *Nombre del usuario*. **Requerido.**|
|`last_name`| `str`| *Apellido del usuario.* **Requerido.**|
|`email`| `str`| *Email del usuario.* **Requerido.**|

#### Delete (delete user)

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int`    | *ID del usuario que se desea eliminar.*  **Requerido.** |

## 📦 Contenido

Esta nueva versión incorpora tanto nuevas funcionalidades como mejoras en la estructura visual del sistema mediante el uso de **templates personalizados**.  
Se han desarrollado vistas clave como:

- **`base.html`**: Plantilla base que estructura la interfaz general del sitio.
- **`login.html`** y **`register.html`**: Formularios de autenticación.
- Otras vistas específicas que se integrarán progresivamente en versiones futuras.

Todos los templates están construidos utilizando **[django-tailwind](https://django-tailwind.readthedocs.io/)**, un framework que permite integrar de forma eficiente las utilidades y estilos de **Tailwind CSS** dentro del entorno de Django. Esto nos permite desarrollar interfaces modernas, responsivas y altamente personalizables, manteniendo la coherencia visual en toda la aplicación.

## 🧩 Estructura y navegación

La interfaz del formulario de inicio de sesión incluye un **navbar** funcional, el cual contiene:

- Accesos directos a las páginas de **Inicio de sesión** y **Registro**.
- Un botón de **cerrar sesión** (visible para usuarios autenticados).
- En futuras versiones, este menú se expandirá con enlaces a funciones internas del sistema.

## 🔐 Seguridad y flujo de usuarios

En futuras versiones se implementará una restricción de acceso:  
> Los usuarios podrán navegar por ciertas secciones de la aplicación, pero **no podrán comprar boletos de avión sin estar autenticados**.

Esta decisión responde a prácticas recomendadas de seguridad y control de acceso dentro de sistemas de gestión de usuarios.

## ✍️ Autores 

- [@t.bratik](https://github.com/tom1mvp)
- [@m.geller](https://github.com/MarcosAyrton)
- [@s.giacomucci](https://github.com/Stefano818-bot)
## 🛪 EFI Django 2025: *Aerolíneas Splinter* 🧑‍✈️

Trabajo práctico integrador realizado bajo los conceptos teóricos y prácticos de la materia **_Ingeniería de Software_**, dictada por el profesor **_Matias Lucero_**.  
Este proyecto se basa en el desarrollo de un sistema de gestión para una aerolínea ficticia llamada *Splinter*.

A continuación, se detalla lo que incluye esta primera parte del trabajo.

## 📦 Contenido 

Al día de hoy (13/06/2025), el proyecto se encuentra en su primera versión. Esta etapa inicial incluye los elementos básicos del sistema, aún sin implementación de modelos, repositorios, servicios ni vistas completas.

En versiones futuras se incorporarán validaciones, manejo de errores, y una arquitectura más robusta.  
Además, se contempla el desarrollo de funcionalidades especiales, tales como:

- Un botón para traducir automáticamente toda la aplicación.
- Soporte para modos oscuro y claro.
- Otras características orientadas a mejorar la experiencia del usuario y la accesibilidad.

Este documento y el repositorio se irán actualizando conforme avance el desarrollo del proyecto.

## ✍️ Autores 

- [@t.bratik](https://github.com/tom1mvp)
- [@m.geller](https://github.com/MarcosAyrton)
- [@s.giacomucci](https://github.com/Stefano818-bot)
