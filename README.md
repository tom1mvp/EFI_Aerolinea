## 🛪 EFI Django 2025: *Aerolíneas Splinter* 🧑‍✈️

**Actualización del día jueves 19/06/2025**:

Se implementaron las funciones para la gestión de ***aviones*** y ***asientos***, incluyendo la creación, actualización, eliminación y consulta de ambos recursos mediante métodos `GET`, `POST`, `PUT` y `DELETE`.
También se desarrollaron los respectivos modelos, repositorios, servicios, vistas y se configuraron en el archivo `admin.py` para su administración desde el panel de Django.

A continuación, se detalla el contenido de esta nueva actualización del proyecto.

## ⚙️ Funciones


###  👨 Usuarios 

***Get all users - Obtener todos los usuarios***

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `-` | `-` |          **Este endopoint no requiere parametros** |

***Get user by id - Obtener los usuarios por su ID***

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int`    | *ID*. **Requerido** |

***Post (Crear usuario) - Metodo para crear usuarios***

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`first_name`|    `str`| *Nombre del usuario*. **Requerido.**|
|`last_name`| `str`| *Apellido del usuario.* **Requerido.**|
|`username`| `str`| *Usuario.* **Requerido.**|
|`password`| `str`| *Contraseña.* **Requerido.**|
|`email`| `str`| *Email del usuario.* **Requerido.**|


***Update (Actualizar usuario) - Metodo para actualizar el usuario***

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`first_name`|    `str`| *Nombre del usuario*. **Requerido.**|
|`last_name`| `str`| *Apellido del usuario.* **Requerido.**|
|`username`| `str`| *Usuario.* **Requerido.**|
|`password`| `str`| *Contraseña.* **Requerido.**|
|`email`| `str`| *Email del usuario.* **Requerido.**|

***Delete (Borrar usuario) - Metodo para eliminar un usuario***

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int`    | *ID del usuario que se desea eliminar.*  **Requerido.** |

###  🛪 Aviones

***Get all airplanes - Obtener todos los aviones***

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `-` | `-` |          **Este endopoint no requiere parametros** |


***Get airplane by id - Obtener los aviones por su ID***

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int`    | *ID*. **Requerido**|

***Get airplane by name - Obtener los aviones por su nombre***

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `str`    | *Nombre del avión*. **Requerido**|


***Post (Crear avión) - Metodo para crear un avión***

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`name`|    `str`| *Nombre del avión*. **Requerido.**|
|`capacity`| `int`| *Capacidad del avión.* **Requerido.**|
|`row`| `int`| *Filas del avión* **Requerido.**|
|`columns`| `int`| *Columnas del avión* **Requerido.**|
|`status`| `str`| *Estado del avión* **Requerido.**|

***Update (Actualizar avión) - Metodo para actualizar un avión***

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`name`|    `str`| *Nombre del avión*. **Requerido.**|
|`capacity`| `int`| *Capacidad del avión.* **Requerido.**|
|`row`| `int`| *Filas del avión* **Requerido.**|
|`columns`| `int`| *Columnas del avión* **Requerido.**|
|`status`| `str`| *Estado del avión* **Requerido.**|

***Delete (Eiminar avión) - Metodo para eliminar un avión***

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int`    | *ID del avión que se quiere eliminar*. **Requerido**|


### 💺 Asientos 

***Get all seats - Obtener todos los asientos***

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `-` | `-` |          **Este endopoint no requiere parametros** |

***Get by airplane (seats) - Obtener los asientos por avión***

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `airplane_id`      | `int`    | *ID del avión*. **Requerido**|

***Get by type (seats) - Obtener los asientos por su tipo***

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `type`      | `str`    | *Tipo de asiento*. **Requerido**|

***Post (Crear asientos) - Metodo para crear asientos***

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`airplane_id`|    `int`| *ID del avión*. **Requerido.**|
|`number`| `int`| *Número del asiento.* **Requerido.**|
|`row`| `int`| *Filas del asiento* **Requerido.**|
|`columns`| `int`| *Columnas del asiento* **Requerido.**|
|`type`| `str`| *Tipo de asiento* **Requerido.**|
|`status`| `str`| *Estado del asiento* **Requerido.**|

***Update (Actualizar asientos) - Metodo para actualizar asientos***

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int`    | *ID del avión asiento*. **Requerido**|
|`airplane_id`|    `int`| *ID del avión*. **Requerido.**|
|`number`| `int`| *Número del asiento.* **Requerido.**|
|`row`| `int`| *Filas del asiento* **Requerido.**|
|`columns`| `int`| *Columnas del asiento* **Requerido.**|
|`type`| `str`| *Tipo de asiento* **Requerido.**|
|`status`| `str`| *Estado del asiento* **Requerido.**|

***Delete (Eliminar asientos) - Metodo para eliminar asiento***

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int`    | *ID del asiento que se quiere eliminar*. **Requerido**|

## 📦 Contenido

Esta versión introduce mejoras tanto funcionales como visuales:

Se configuró la carpeta themes para integrar Tailwind CSS mediante **django-tailwind**, lo que permite aplicar estilos modernos, responsivos y consistentes en toda la interfaz.

***Se desarrollaron vistas clave utilizando templates personalizados:***

* base.html: plantilla base que estructura la interfaz general del sistema.

* login.html y register.html: formularios para autenticación de usuarios.

***Se implementó un navbar funcional con las siguientes características:***

* Accesos directos a las páginas de Inicio de sesión y Registro.


### 🧩 Estructura y navegación

La interfaz del formulario de inicio de sesión incluye un **navbar** funcional, el cual contiene:

- Accesos directos a las páginas de **Inicio de sesión** y **Registro**.
- Un botón de **cerrar sesión** (visible para usuarios autenticados).
- En futuras versiones, este menú se expandirá con enlaces a funciones internas del sistema.

### 🔐 Seguridad y flujo de usuarios

En futuras versiones se implementará una restricción de acceso:  
> Los usuarios podrán navegar por ciertas secciones de la aplicación, pero **no podrán comprar boletos de avión sin estar autenticados**.

Esta decisión responde a prácticas recomendadas de seguridad y control de acceso dentro de sistemas de gestión de usuarios.


## ✍️ Autores 

- [@t.bratik](https://github.com/tom1mvp)
- [@m.geller](https://github.com/MarcosAyrton)
- [@s.giacomucci](https://github.com/Stefano818-bot)
