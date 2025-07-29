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

Esta versión introduce mejoras tanto funcionales como visuales:

Se configuró la carpeta themes para integrar Tailwind CSS mediante **django-tailwind**, lo que permite aplicar estilos modernos, responsivos y consistentes en toda la interfaz.

***Se desarrollaron vistas clave utilizando templates personalizados:***

* base.html: plantilla base que estructura la interfaz general del sistema.

* login.html y register.html: formularios para autenticación de usuarios.

***Se implementó un navbar funcional con las siguientes características:***

* Accesos directos a las páginas de Inicio de sesión y Registro.

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
