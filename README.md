# 🧑‍✈️ Aerolíneas Splinter (API Version) 💺

## 🚀 Introducción y Motivación del Proyecto

El proyecto *Aerolíneas Splinter (API Version)* se desarrolló como parte del *Trabajo Final Integrador (TFI)* del año 2025. Su creación responde a la necesidad de aplicar y consolidar los conocimientos *teóricos y prácticos* adquiridos durante el cursado de la materia *Ingeniería en Software*.

El objetivo principal de este desarrollo fue construir una *API RESTful completa* y funcional, utilizando tecnologías de vanguardia como el framework *Django* y la librería *Django REST Framework (DRF). Este enfoque nos permitió simular un entorno de desarrollo profesional, poniendo a prueba nuestras habilidades en el diseño de arquitecturas de *software, la gestión de bases de datos, y la implementación de endpoints robustos y escalables.

---

## 💻 Acerca del Proyecto

*Aerolíneas Splinter (API Version)* es una *REST API Full* diseñada para gestionar los procesos principales de una aerolínea.

### Tecnologías Clave Utilizadas:

* *Lenguaje de Programación:* Python
* *Framework:* Django
* *API Framework:* Django REST Framework (DRF)
* *Base de datos:* Postgresql

## ⚙️ Instalación y Configuración de la API 

Sigue estos pasos detallados para instalar, configurar y levantar la API en tu entorno local.

---

### Paso 1: Preparar el Entorno y Clonar el Repositorio

Abre tu terminal (Windows, Linux o macOS) y ejecuta los siguientes comandos:

1.  **Crear y acceder a la carpeta del proyecto:**

    ```bash
    mkdir <Nombre_de_la_carpeta>
    cd <Nombre_de_la_carpeta>
    ```

2.  **Clonar el repositorio de la API:**

    * **Usando SSH:**
        ```bash
        git clone git@github.com:tom1mvp/EFI_Aerolinea.git
        ```
    * **Usando HTTPS:**
        ```bash
        git clone [https://github.com/tom1mvp/EFI_Aerolinea.git](https://github.com/tom1mvp/EFI_Aerolinea.git)
        ```

3.  **Acceder al directorio del proyecto (después de clonar):**

    ```bash
    cd EFI_Aerolinea
    ```

---

### Paso 2: Crear y Activar el Entorno Virtual

Aísla las dependencias del proyecto utilizando un entorno virtual.

1.  **Crear el entorno virtual (`env`):**

    ```bash
    python -m venv env
    ```

2.  **Activar el entorno virtual:**

    * **En Linux/macOS:**
        ```bash
        source env/bin/activate
        ```
    * **En Windows (Command Prompt - CMD):**
        ```bash
        env\Scripts\activate.bat
        ```
    * **En Windows (PowerShell):**
        ```bash
        env\Scripts\Activate.ps1
        ```

    > **Nota:** La línea de comandos mostrará **`(env)`** al inicio, confirmando que el entorno está activo.

---

### Paso 3: Instalar Dependencias del Proyecto

Una vez que el entorno virtual esté activo, instala todas las librerías listadas en el archivo `requirements.txt`.

1.  **Instalar los requerimientos:**

    ```bash
    pip install -r requirements.txt
    ```

---

### Paso 4: Configurar Variables de Entorno (Archivo `.env`)

Crea este archivo en la **raíz del proyecto** para almacenar las credenciales de la base de datos de manera segura.

1.  **Crear el archivo `.env`:**
    Crea un nuevo archivo con el nombre exacto **`.env`** en el directorio principal de la API.

2.  **Definir las variables de base de datos:**
    Copia y pega el siguiente contenido en el archivo `.env`, asegurándote de **reemplazar los valores genéricos** (`<...>`):

    ```ini
    # Configuración de Base de Datos (PostgreSQL)
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=<nombre_de_tu_base_de_datos>
    DB_USER=<tu_usuario>
    DB_PASSWORD=<tu_contraseña>
    DB_HOST=localhost
    DB_PORT=5432
    # Otras variables importantes (pueden ser necesarias)
    # SECRET_KEY=TuClaveSecretaDeDjango
    ```
---

## ⚙️ Métodos
* **GET** 
* **POST**
* **PUT**
* **DELETE**
* **PATCH**

## 🧩 Modelos

En esta sección se detallan los campos que componen el modelo principal de nuestra API.


### 👨🏻 Users (Usuarios)

| Field | Type | Description |
| :--- | :--- | :--- |
| **pk** | `int` | Clave primaria (identificador único). |
| **username** | `str` | Nombre de usuario. |
| **password** | `str` | Contraseña del usuario. Se almacena hasheada por seguridad. |
| **mail** | `str` | Dirección de correo electrónico. |
| **birth_day** | `date` | Fecha de nacimiento del usuario. |
| **phone** | `str` | Número de teléfono. |
| **document** | `str` | Documento de identidad del usuario (DNI, pasaporte, etc.). |
| **name** | `str` | Nombre completo del usuario. |
| **role** | `str` | Rol o nivel de permiso asignado al usuario (ej: `admin`, `cliente`). |
| **is_active** | `bool` | Indica si el usuario está activo (`True` o `False`). |


### 👤 Passenger (Pasajero)

| Field | Type | Description |
| :--- | :--- | :--- |
| **pk** | `int` | Clave primaria (identificador único del pasajero). |
| **user_pk** | `FK (User)` | Relación de clave foránea con el modelo **Users**. |
| **check_in_status** | `bool` | Verifica si el pasajero ha realizado el *check-in* para el vuelo. |
| **passenger_type** | `str` | Tipo de pasajero (ej: 'Adulto', 'Niño', 'Bebé'). |
| **nationality** | `str` | Nacionalidad del pasajero. |
| **is_active** | `bool` | Indica si el registro del pasajero está activo (`True` o `False`). |

### 🛪 Airplane (Avión)

| Field | Type | Description |
| :--- | :--- | :--- |
| **pk** | `int` | Clave primaria (identificador único del avión). |
| **name** | `str` | Nombre o modelo del avión. |
| **capacity** | `int` | Capacidad total de asientos del avión. |
| **rows** | `int` | Número de filas de asientos en el avión. |
| **columns** | `int` | Número de columnas de asientos en el avión. |
| **status** | `str` | Estado operativo del avión (ej: 'Activo', 'Mantenimiento', 'Inactivo'). |

### 💺 Seat (Asiento)

| Field | Type | Description |
| :--- | :--- | :--- |
| **pk** | `int` | Clave primaria (identificador único del asiento). |
| **airplane_pk** | `FK (Airplane)` | Relación de clave foránea con el modelo **Airplane**. |
| **number** | `str` | Identificador único del asiento (ej: "15A"). |
| **row_number** | `int` | Número de fila a la que pertenece el asiento. |
| **column_identifier** | `str` | Identificador de columna del asiento (usualmente una letra, ej: "A"). |
| **type_seat** | `str` | Tipo de asiento (ej: 'Económico', 'Ejecutivo'). |
| **status** | `str` | Estado actual del asiento (ej: 'Disponible', 'Fuera de servicio', 'Ocupado'). |

### 🛫 Flight (Vuelo)

| Field | Type | Description |
| :--- | :--- | :--- |
| **pk** | `int` | Clave primaria (identificador único del vuelo). |
| **airplane_pk** | `FK (Airplane)` | Relación de clave foránea con el modelo **Airplane**. |
| **origin** | `str` | Ciudad de origen del vuelo (ej: 'Córdoba'). |
| **destination** | `str` | Ciudad de destino del vuelo (ej: 'Buenos Aires'). |
| **departure_date** | `datetime` | Fecha y hora programada de salida del vuelo. |
| **arrival_date** | `datetime` | Fecha y hora programada de llegada del vuelo. |
| **duration** | `timedelta / decimal` | Duración estimada del vuelo (en horas, minutos, etc.). |
| **status** | `str` | Estado actual del vuelo (ej: 'Activo', 'Inactivo'). |

### 🪪 Reservation (Reservación)

| Field | Type | Description |
| :--- | :--- | :--- |
| **pk** | `int` | Clave primaria (identificador único de la reserva). |
| **passenger_pk** | `FK (Passenger)` | Relación de clave foránea con el modelo **Passenger**. |
| **flight_pk** | `FK (Flight)` | Relación de clave foránea con el modelo **Flight**. |
| **seat_pk** | `FK (Seat)` | Relación con clave foránea con el modelo **Seat**. |
| **flight_number** | `str` | Número del vuelo (ej: 'A01'). |
| **reservation_date** | `datetime` | Fecha y hora de la reserva. | 
| **status** | `str` | Estado actual de la reserva (ej: 'Disponible', 'Reservado', 'Ocupado'). |
| **price** | `decimal` | Precio de la reserva. |
| **reservation_code** | `str` | Código único de la reserva. |
| **is_active** | `bool` | Indica si el registro de la reserva está activo (`True` o `False`). |

### 🎟️ Ticket (Billete)

| Field | Type | Description |
| :--- | :--- | :--- |
| **pk** | `int` | Clave primaria (identificador único del billete). |
| **reservation** | `OneToOneField (Reservation)` | Relación uno a uno con el modelo **Reservation**. Asegura que una reserva solo tiene un billete asociado. |
| **ticket_number** | `str` | Número de identificación único del billete. |
| **issue_date** | `datetime` | Fecha y hora en que se emitió el billete. |
| **barcode** | `str` | Código de barras único asociado al billete para validación. |
| **status** | `str` | Estado actual del billete (ej: 'Emitido', 'Utilizado', 'Anulado'). |

---

## 🔗 Endpoints

Esta sección proporciona una guía detallada de todos los *endpoints* disponibles en la API. Para cada punto de acceso, se especifican el método HTTP, la ruta, su funcionalidad y las respuestas esperadas.

---

### 👨🏻 Users (Usuarios)

* **GET** `/users/list/` — Obtener todos los usuarios
    * **Descripción**: Este *endpoint* retorna todos los usuarios que están registrados.
    * **Método**: `GET`
    * **Autenticación requerida**: Admin
    * **Cuerpo de la Solicitud (*Request body*)**: Ninguno
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "data": [
                {
                    "id": 1,
                    "name": "Thomas Elser Bratik",
                    "username": "t.bratik_admin",
                    "phone": "3586018120",
                    "document": "44973692",
                    "birth_day": "2003-07-15",
                    "mail": "t_bratik83@gmail.com"
                },
                {
                    "id": 2,
                    "name": "Maximiliano Manetti",
                    "username": "Maxi_maxito",
                    "phone": "3587823455",
                    "document": "37679871",
                    "birth_day": "1987-12-21",
                    "mail": "maxi@maxi.com"
                }
            ]
        }
        ```
* **POST** `/users/login/` — Iniciar sesión
    * **Descripción**: Este *endpoint* se utiliza para iniciar sesión.
    * **Método**: `POST`
    * **Autenticación requerida**: Ninguna
    * **Cuerpo de la Solicitud (*Request body*)**:
        ```json
        {
            "username": "tbratik.admin",
            "password": "Tbratik15072003"
        }
        ```
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "message": "Bienvenido usuario",
            "data": {
                "pk": 1,
                "username": "tbratik.admin",
                "mail": "thomasbratik83@gmail.com"
            }
        }
        ```
* **POST** `/users/register/` — Registrarse
    * **Descripción**: Este *endpoint* se utiliza para registrar un nuevo usuario.
    * **Método**: `POST`
    * **Autenticación requerida**: Ninguna
    * **Cuerpo de la Solicitud (*Request body*)**:
        ```json
        {
            "name": "Juan Doe",
            "age": "44",
            "gender": "male",
            "birth_day": "1999-12-12",
            "document": "35985435",
            "mail": "juanDoe@juan.com",
            "phone": "3587832126",
            "username": "Juancho",
            "password": "juancito123",
            "confirm_password": "juancito123",
            "role": "customer"
        }
        ```
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "message": "Usuario registrado",
            "data": {
                "id": 3,
                "name": "Juan Doe",
                "username": "Juancho",
                "phone": "3587832126",
                "document": "35985435",
                "birth_day": "1999-12-12",
                "mail": "juanDoe@juan.com"
            }
        }
        ```

* **PUT** `/users/user/update/<int:pk>` — Actualizar usuario
    * **Descripción**: Este *endpoint* se utiliza para actualizar la información de un usuario específico, identificado por su clave primaria (`pk`).
    * **Método**: `PUT`
    * **Autenticación requerida**: IsAuthenticated (Usuario debe estar autenticado)
    * **Cuerpo de la Solicitud (*Request body*)**:
        ```json
        {
            "name": "Juan Doe",
            "age": "45",  // Campo modificado para el ejemplo
            "gender": "male",
            "birth_day": "1999-12-12",
            "document": "35985435",
            "mail": "juanDoe_nuevo@juan.com", // Campo modificado para el ejemplo
            "phone": "3587832126",
            "username": "Juancho",
            "password": "juancito123",
            "confirm_password": "juancito123",
            "role": "customer"
        }
        ```
        ---
        > **Nota**: Para que la actualización se refleje, al menos uno de los campos en el cuerpo de la solicitud debe contener un valor diferente al que tiene actualmente el usuario.
        ---
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "message": "El usuario fue actualizado con éxito",
            "data": {
                "id": 3,
                "name": "Juan Doe",
                "username": "Juancho",
                "phone": "3587832126",
                "document": "35985435",
                "birth_day": "1999-12-12",
                "mail": "juanDoe@juan.com"
            }
        }
        ```

* **DELETE** `user/<int:pk>/status` — Borrar usuario (*Soft Delete*)

    * **Descripción**: Este *endpoint* se utiliza para **eliminar lógicamente** (soft delete) la información de un usuario específico, identificado por su clave primaria (`pk`), cambiando su estado en lugar de borrarlo de la base de datos.
    * **Método**: `DELETE`
    * **Autenticación requerida**: IsAuthenticated (Usuario debe estar autenticado), Admin
    * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "message": "El usuario fue eliminado con éxito"
        }
        ```

### 👤 Passenger (Pasajero)

* **GET** `passangers/passangers/` — Obtener todos los pasajeros
    * **Descripción**: Este *endpoint* retorna una lista de todos los pasajeros registrados.
    * **Método**: `GET`
    * **Autenticación requerida**: Admin
    * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "data": [
                {
                    "user_fullname": "Thomas Elser Bratik",
                    "user_username": "tbratik.admin",
                    "check_in_status": true,
                    "passenger_type": "adult",
                    "nationality": "Argentino"
                },
                {
                    "user_fullname": "Thomas Elser Bratik",
                    "user_username": "tbratik.admin",
                    "check_in_status": true,
                    "passenger_type": "adult",
                    "nationality": "Argentino"
                },
                {
                    "user_fullname": "Thomas Elser Bratik",
                    "user_username": "tbratik.admin",
                    "check_in_status": true,
                    "passenger_type": "adult",
                    "nationality": "Argentino"
                },
                {
                    "user_fullname": "Thomas Elser Bratik",
                    "user_username": "tbratik.admin",
                    "check_in_status": true,
                    "passenger_type": "adult",
                    "nationality": "Argentino"
                },
                {
                    "user_fullname": "Thomas Elser Bratik",
                    "user_username": "tbratik.admin",
                    "check_in_status": true,
                    "passenger_type": "adult",
                    "nationality": "Argentino"
                },
                {
                    "user_fullname": "Thomas Elser Bratik",
                    "user_username": "tbratik.admin",
                    "check_in_status": true,
                    "passenger_type": "adult",
                    "nationality": "Argentino"
                },
                {
                    "user_fullname": "Maximiliano Manetti",
                    "user_username": "Maxi_maxito",
                    "check_in_status": false,
                    "passenger_type": "child",
                    "nationality": "Argentino"
                },
                {
                    "user_fullname": "Maximiliano Manetti",
                    "user_username": "Maxi_maxito",
                    "check_in_status": true,
                    "passenger_type": "adult",
                    "nationality": "Argentino"
                }
            ]
        }
        ```
    * **GET** `passangers/passanger/<str:name>` — Obtener un pasajero por su nombre
        * **Descripción**: Este *endpoint* retorna una lista de pasajeros que coinciden con el nombre especificado en la ruta.
        * **Método**: `GET`
        * **Autenticación requerida**: Admin
        * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
        * **Cuerpo de la Respuesta (*Response body*)**:
            ```json
            {
                "data": [
                    {
                        "user_fullname": "Maximiliano Manetti",
                        "user_username": "Maxi_maxito",
                        "check_in_status": true,
                        "passenger_type": "adult",
                        "nationality": "Argentino"
                    },
                    {
                        "user_fullname": "Maximiliano Manetti",
                        "user_username": "Maxi_maxito",
                        "check_in_status": false,
                        "passenger_type": "child",
                        "nationality": "Argentino"
                    }
                ]
            }
            ```
    * **POST** `passangers/create/` — Crear pasajero
        * **Descripción**: Este *endpoint* se utiliza para crear un nuevo registro de pasajero asociado a un usuario existente.
        * **Método**: `POST`
        * **Autenticación requerida**: Admin
        * **Cuerpo de la Solicitud (*Request body*)**:
            ```json
            {
                "user_id": 3,
                "check_in_status": true,
                "passenger_type": "adult",
                "nationality": "Argentina",
                "is_active": true
            }
            ```
        * **Cuerpo de la Respuesta (*Response body*)**:
            ```json
            {
                "message": "El pasajero fue creado con éxito",
                "data": {
                    "user_fullname": "Juan doe",
                    "user_username": "Juancho",
                    "check_in_status": true,
                    "passenger_type": "adult",
                    "nationality": "Argentina"
                }
            }
            ```
    * **PUT** `passangers/update/<int:pk>` — Actualizar pasajero
        * **Descripción**: Este *endpoint* se utiliza para actualizar la información de un pasajero específico, identificado por su clave primaria (`pk`).
        * **Método**: `PUT`
        * **Autenticación requerida**: IsAuthenticated (Usuario debe estar autenticado)
        * **Cuerpo de la Solicitud (*Request body*)**:
            ```json
            {
                "user_id": 3,
                "check_in_status": true,
                "passenger_type": "children", // Campo modificado para el ejemplo
                "nationality": "Argentina",
                "is_active": true
            }
            ```
            ---
            > **Nota**: Para que la actualización se refleje, al menos uno de los campos en el cuerpo de la solicitud debe contener un valor diferente al que tiene actualmente el pasajero.
           ---
        * **Cuerpo de la Respuesta (*Response body*)**:
            ```json
            {
                "message": "El pasajero fue actualizado con éxito",
                "data": {
                    "user_fullname": "Juan doe",
                    "user_username": "Juancho",
                    "check_in_status": true,
                    "passenger_type": "children",
                    "nationality": "Argentina"
                }
            }
            ```
    * **DELETE** `passangers/passanger/<int:pk>/status` — Borrar pasajero (*Soft Delete*)
        * **Descripción**: Este *endpoint* se utiliza para **eliminar lógicamente** (soft delete) la información de un pasajero específico, identificado por su clave primaria (`pk`), cambiando su estado en lugar de borrarlo de la base de datos.
        * **Método**: `DELETE`
        * **Autenticación requerida**: Admin
        * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
        * **Cuerpo de la Respuesta (*Response body*)**:
            ```json
            {
                "message": "El pasajero fue eliminado con éxito"
            }
            ```

### ✈️ Airplanes (Aviones)

* **GET** `airplanes/airplane/` — Obtener todos los aviones
    * **Descripción**: Este *endpoint* retorna una lista de todos los aviones registrados en el sistema.
    * **Método**: `GET`
    * **Autenticación requerida**: Admin
    * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "data": [
                {
                    "id": 1,
                    "name": "A00LXC",
                    "capacity": 500,
                    "rows": 5,
                    "columns": 10,
                    "status": "activo"
                },
                {
                    "id": 2,
                    "name": "BLX00dd",
                    "capacity": 40,
                    "rows": 5,
                    "columns": 10,
                    "status": "activo"
                }
            ]
        }
        ```
* **POST** `airplanes/create/` — Crear un avión
    * **Descripción**: Este *endpoint* se utiliza para registrar un nuevo avión en el sistema.
    * **Método**: `POST`
    * **Autenticación requerida**: Admin
    * **Cuerpo de la Solicitud (*Request body*)**:
        ```json
        {
            "name": "ARG005",
            "capacity": 120,
            "rows": 50,
            "columns": 5,
            "status": "Activo"
        }
        ```
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "message": "El avion fue creado con éxito",
            "data": {
                "id": 3,
                "name": "ARG005",
                "capacity": 120,
                "rows": 50,
                "columns": 5,
                "status": "Activo"
            }
        }
        ```
  * **PUT** `airplanes/airplane/update/<int:pk>/` — Actualizar avión
    * **Descripción**: Este *endpoint* se utiliza para actualizar la información de un avión específico, identificado por su clave primaria (`pk`).
    * **Método**: `PUT`
    * **Autenticación requerida**: Admin
    * **Cuerpo de la Solicitud (*Request body*)**:
        ```json
        {
            "name": "ARG005",
            "capacity": 124, // Campo modificado para el ejemplo
            "rows": 60, // Campo modificado para el ejemplo
            "columns": 10, // Campo modificado para el ejemplo
            "status": "Activo"
        }
        ```
        ---
        > **Nota**: Para que la actualización se refleje, al menos uno de los campos en el cuerpo de la solicitud debe contener un valor diferente al que tiene actualmente el avión.
        ---
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "message": "El avion fue actualizado con éxito",
            "data": {
                "id": 3,
                "name": "ARG005",
                "capacity": 124,
                "rows": 60,
                "columns": 10,
                "status": "Activo"
            }
        }
        ```
  ### 💺 Seat (Asiento)
   
   * **GET** `airplanes/seat/` — Obtener todos los asientos
        * **Descripción**: Este *endpoint* retorna una lista completa de todos los asientos registrados en el sistema, detallando su ubicación, tipo y estado.
        * **Método**: `GET`
        * **Autenticación requerida**: Admin
        * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
        * **Cuerpo de la Respuesta (*Response body*)**:
            ```json
            {
                "data": [
                    {
                        "id": 2,
                        "number": "B1",
                        "rows": 1,
                        "columns": 2,
                        "type_seat": "economico",
                        "status": "disponible",
                        "airplane": 2
                    },
                    {
                        "id": 3,
                        "number": "C1",
                        "rows": 1,
                        "columns": 3,
                        "type_seat": "economico",
                        "status": "disponible",
                        "airplane": 2
                    },
                    // ... (Otros asientos)
                    {
                        "id": 187,
                        "number": "B28",
                        "rows": 28,
                        "columns": 2,
                        "type_seat": "economico",
                        "status": "disponible",
                        "airplane": 3
                    }
                ]
            }
            ```
* **GET** `flight/<int:pk>/seat_avaible/` — Obtener asientos disponibles en un vuelo
    * **Descripción**: Este *endpoint* retorna una lista de todos los asientos marcados como **'disponible'** que pertenecen al avión asignado al Vuelo ID (`pk`).
    * **Método**: `GET`
    * **Autenticación requerida**: Autenticado
    * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "data": [
                {
                    "id": 101,
                    "number": "1A",
                    "rows": 1,
                    "columns": 1,
                    "type_seat": "ejecutivo",
                    "status": "disponible",
                    "airplane": 5
                }
            ]
        }
        ```
* **GET** `flight/<int:flight_pk>/seat/<int:seat_pk>/avaible` — Verificar un asiento específico
    * **Descripción**: Este *endpoint* verifica si un asiento específico (`seat_pk`) está en estado **'disponible'** y pertenece al avión del vuelo (`flight_pk`).
    * **Método**: `GET`
    * **Autenticación requerida**: Autenticado
    * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "message": "El asiento está disponible.",
            "flight_id": 8,
            "seat_id": 120,
            "is_available": true
        }
        ```        

* **PUT** `airplanes/seat/update/<int:pk>/` — Actualizar asiento
    * **Descripción**: Este *endpoint* se utiliza para modificar la información de un asiento específico, identificado por su clave primaria (`pk`).
    * **Método**: `PUT`
    * **Autenticación requerida**: Admin
    * **Cuerpo de la Solicitud (*Request body*)**:
        ```json
        {
            "id": 6,
            "number": "F1",
            "rows": 1,
            "columns": 6,
            "type_seat": "ejecutivo",   // Campo modificado
            "status": "no disponible", // Campo modificado
            "airplane": 2
        }
        ```
        ---
        > **Nota**: El `<int:pk>` en la URL corresponde al **ID único del asiento** que se desea actualizar (en este ejemplo, `pk=6`).
        ---
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "message": "El asiento fue actualizado con éxito",
            "data": {
                "id": 6,
                "number": "F1",
                "rows": 1,
                "columns": 6,
                "type_seat": "ejecutivo",
                "status": "no disponible",
                "airplane": 2
            }
        }
        ```
            ---
            > **Nota**: Para asientos **no existe un *endpoint* de creación** (`POST`)  porque se generan automáticamente al crear el avión, basados en sus dimensiones (`rows` y `columns`).
    ---

### 🛫 Flight (Vuelo)

  * **GET** `flights/list/` — Obtener todos los vuelos
    * **Descripción**: Este *endpoint* retorna una lista completa de todos los vuelos registrados en el sistema.
    * **Método**: `GET`
    * **Autenticación requerida**: IsAuthenticated (**Usuario autenticado**)
    * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "data": [
                {
                    "airplane_name": "A00LXC",
                    "airplane_capacity": 500,
                    "origin": "Mendoza",
                    "destination": "Córdoba",
                    "departure_date": "2025-09-10T00:00:00Z",
                    "arrival_date": "2025-09-10T00:00:00Z",
                    "duration": "15.00",
                    "status": "Activo",
                    "base_price": "50000.00"
                },
                {
                    "airplane_name": "A00LXC",
                    "airplane_capacity": 500,
                    "origin": "Buenos Aires",
                    "destination": "Londres",
                    "departure_date": "2025-10-10T00:00:00Z",
                    "arrival_date": "2025-10-11T00:00:00Z",
                    "duration": "42.00",
                    "status": "Activo",
                    "base_price": "1100000.00"
                }
            ]
        }
        ```
    * **GET** `flights/flight/<int:pk>/` — Obtener información de un vuelo en específico
    * **Descripción**: Este *endpoint* retorna específicamente la información de un vuelo registrado en el sistema, identificado por su clave primaria (`pk`).
    * **Método**: `GET`
    * **Autenticación requerida**: IsAuthenticated (**Usuario autenticado**)
    * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "data": {
                "airplane_name": "A00LXC",
                "airplane_capacity": 500,
                "origin": "Mendoza",
                "destination": "Córdoba",
                "departure_date": "2025-09-10T00:00:00Z",
                "arrival_date": "2025-09-10T00:00:00Z",
                "duration": "15.00",
                "status": "Activo",
                "base_price": "50000.00"
            }
        }
        ```
        ---
    > **Nota**: El `<int:pk>` en la URL debe ser reemplazado por el **ID único del vuelo** que se desea consultar.
        ---

* **POST** `flights/create/` — Crear un vuelo
    * **Descripción**: Este *endpoint* se utiliza para crear un nuevo vuelo, relacionándolo con un avión existente a través de su ID (`airplane_id`).
    * **Método**: `POST`
    * **Autenticación requerida**: IsAuthenticated (**Usuario autenticado**)
    * **Cuerpo de la Solicitud (*Request body*)**:
        ```json
        {
            "airplane_id": 1,
            "origin": "Dubai",
            "destination": "Buenos Aires",
            "departure_date": "2025-07-08",
            "arrival_date": "2025-07-08",
            "duration": 20,
            "base_price": 120000,
            "status": "activo",
            "is_active": true
        }
        ```
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "message": "El vuelo fue creado con éxito",
            "data": {
                "airplane_name": "A00LXC",
                "airplane_capacity": 500,
                "origin": "Dubai",
                "destination": "Buenos Aires",
                "departure_date": "2025-07-08",
                "arrival_date": "2025-07-08",
                "duration": "20.00",
                "status": "activo",
                "base_price": "120000.00"
            }
        }
        ```
        
    * **PUT** `flights/update/<int:pk>/` — Actualizar vuelo
        * **Descripción**: Este *endpoint* se utiliza para modificar la información de un vuelo específico, identificado por su clave primaria (`pk`).
        * **Método**: `PUT`
        * **Autenticación requerida**: Admin
        * **Cuerpo de la Solicitud (*Request body*)**:
            ```json
            {
                "airplane_id": 1,
                "origin": "San Francisco", // Campo modificado
                "destination": "Buenos Aires",
                "departure_date": "2025-08-08",
                "arrival_date": "2025-08-09", // Campo modificado
                "duration": 20,
                "base_price": 120000,
                "status": "activo",
                "is_active": true
            }
            ```
             ---
            > **Nota**: Para que la actualización se refleje, al menos uno de los campos en el cuerpo de la solicitud debe contener un valor diferente al que tiene actualmente el vuelo. El `<int:pk>` en la URL debe ser reemplazado por el **ID único del vuelo** que se desea actualizar.
            ---
        * **Cuerpo de la Respuesta (*Response body*)**:
            ```json
            {
                "message": "El vuelo fue actualizado con éxito",
                "data": {
                            "airplane_name": "A00LXC",
                            "airplane_capacity": 500,
                            "origin": "San Francisco",
                            "destination": "Buenos Aires",
                            "departure_date": "2025-08-08",
                            "arrival_date": "2025-08-09",
                            "duration": "20.00",
                            "status": "activo",
                            "base_price": "120000.00"
                        }
            }
            ```
   * **DELETE** `flights/<int:pk>/status/` — Borrar vuelo (**Soft Delete**)
        * **Descripción**: Este *endpoint* se utiliza para **eliminar lógicamente** la información de un vuelo específico, identificado por su clave primaria (`pk`). En lugar de borrar el registro permanentemente, su **estado** es modificado para marcarlo como inactivo o eliminado.
        * **Método**: `DELETE`
        * **Autenticación requerida**: Admin
        * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
        * **Cuerpo de la Respuesta (*Response body*)**:
            ```json
            {
                "message": "El vuelo fue eliminado con éxito"
            }
            ```
    ---
    > **Nota**: El `<int:pk>` en la URL debe ser reemplazado por el **ID único del vuelo** que se desea eliminar. Esta acción realiza un **soft delete**, conservando el registro en la base de datos.
   ---
   
   
### 🪪 Reservation (Reservación)

* **GET** `reservations/list/` — Obtener todas las reservaciones
    * **Descripción**: Este *endpoint* retorna una lista completa de todos las reservas registradas en el sistema.
    * **Método**: `GET`
    * **Autenticación requerida**: Admin
    * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "data": [
                {
                    "user_fullname": "Thomas Elser Bratik",
                    "flight_origin": "Mendoza",
                    "flight_destination": "Córdoba",
                    "seat_number": "D3",
                    "flight_number": "120",
                    "reservation_date": "2025-09-10T00:00:00Z",
                    "status": "Disponible",
                    "price": "130000.00",
                    "reservation_code": "ASDMASDK0909LK"
                }
                // ... (Otras reservaciones)
            ]
        }
        ```

 * **GET** `reservations/reservation/<int:pk>/` — Obtener una reserva específica
    * **Descripción**: Este *endpoint* retorna la información detallada de una reserva registrada en el sistema, identificada por su clave primaria (`pk`).
    * **Método**: `GET`
    * **Autenticación requerida**: Admin
    * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "data": {
                "user_fullname": "Thomas Elser Bratik",
                "flight_origin": "Mendoza",
                "flight_destination": "Córdoba",
                "seat_number": "D3",
                "flight_number": "120",
                "reservation_date": "2025-09-10T00:00:00Z",
                "status": "Disponible",
                "price": "130000.00",
                "reservation_code": "ASDMASDK0909LK"
            }
        }
        ```
        ---
    > **Nota**: El `<int:pk>` en la URL debe ser reemplazado por el **ID único de la reserva** que se desea consultar.
    ---
    
 * **GET** `reservations/reservation/passanger/<int:pk>/` — Obtener una reserva de un pasajero específico
    * **Descripción**: Este *endpoint* retorna la información detallada de **una reserva** realizada por un cliente específico, identificada por la clave primaria (`pk`) que presumiblemente corresponde al **ID del pasajero**.
    * **Método**: `GET`
    * **Autenticación requerida**: Admin
    * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "data": {
                "user_fullname": "Thomas Elser Bratik",
                "flight_origin": "Mendoza",
                "flight_destination": "Córdoba",
                "seat_number": "D3",
                "flight_number": "120",
                "reservation_date": "2025-09-10T00:00:00Z",
                "status": "Disponible",
                "price": "130000.00",
                "reservation_code": "ASDMASDK0909LK"
            }
        }
        ```
       --- 
    > **Nota**: El `<int:pk>` en la URL debe ser reemplazado por el **ID único del pasajero** cuya reserva se desea consultar. Este *endpoint* asume que cada pasajero solo tiene una reserva activa asociada o que solo retorna la más reciente/relevante.
    ---
    
 * **POST** `reservations/create/` — Crear reserva
    * **Descripción**: Este *endpoint* se utiliza para crear una nueva reserva, relacionando las claves primarias de **asiento** (`seat_id`), **vuelo** (`flight_id`) y **pasajero** (`passanger_id`).
    * **Método**: `POST`
    * **Autenticación requerida**: IsAuthenticated (**Usuario autenticado**)
    * **Cuerpo de la Solicitud (*Request body*)**:
        ```json
        {
            "passanger_id": 3,
            "flight_id": 2,
            "seat_id": 282,
            "flight_number": "005",
            "reservation_date": "2025-10-14",
            "status": "disponible",
            "price": 1100000,
            "reservation_code": "APLmmm9883Lñ",
            "is_active": true
        }
        ```
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "message": "La reserva fue creada con éxito",
            "data": {
                "user_fullname": "Thomas Elser Bratik",
                "flight_origin": "Buenos Aires",
                "flight_destination": "Londres",
                "seat_number": "B47",
                "flight_number": "005",
                "reservation_date": "2025-11-05T20:22:22.351045Z",
                "status": "disponible",
                "price": "1100000.00",
                "reservation_code": "APLmmm9883Lñ"
            }
        }
        ```
        
  * **PUT** `reservations/reservation/update/<int:pk>/` — Actualizar reserva
    * **Descripción**: Este *endpoint* se utiliza para modificar la información de una reserva específica, identificada por su clave primaria (`pk`), relacionando las claves de **asiento** (`seat_id`), **vuelo** (`flight_id`) y **pasajero** (`passanger_id`).
    * **Método**: `PUT`
    * **Autenticación requerida**: IsAuthenticated (**Usuario autenticado**)
    * **Cuerpo de la Solicitud (*Request body*)**:
        ```json
        {
            "passanger_id": 3,
            "flight_id": 2,
            "seat_id": 282,
            "flight_number": "140", // Campo modificado para el ejemplo
            "reservation_date": "2025-10-14",
            "status": "disponible",
            "price": 1400000, // Campo modificado para el ejemplo
            "reservation_code": "APLmmm9883Lñ",
            "is_active": true
        }
        ```
        ---
        > **Nota**: El `<int:pk>` en la URL debe ser reemplazado por el **ID único de la reserva** que se desea actualizar. Para que la actualización se refleje, al menos uno de los campos en el cuerpo de la solicitud debe contener un valor diferente al que tiene actualmente la reserva.
      ---
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "message": "La reserva fue actualizada con éxito",
            "data": {
                "user_fullname": "Thomas Elser Bratik",
                "flight_origin": "Buenos Aires",
                "flight_destination": "Londres",
                "seat_number": "B47",
                "flight_number": "140",
                "reservation_date": "2025-10-14",
                "status": "disponible",
                "price": "1400000.00",
                "reservation_code": "APLmmm9883Lñ"
            }
        }
        ```
  * **DELETE** `reservations/reservation/<int:pk>/status/` — Borrar una reserva (**Soft Delete**)
    * **Descripción**: Este *endpoint* se utiliza para **eliminar lógicamente** la información de una reserva específica, identificado por su clave primaria (`pk`). En lugar de borrar el registro permanentemente, su **estado** es modificado para marcarlo como inactivo o eliminado.
    * **Método**: `DELETE`
    * **Autenticación requerida**: IsAuthenticated (**Usuario autenticado**)
    * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "message": "La reserva fue eliminada con éxito"
        }
        ```
        ---
    > **Nota**: El `<int:pk>` en la URL debe ser reemplazado por el **ID único de la reserva** que se desea cancelar.
        ---
        
        
 ### 🎟️ Ticket (Billete)

* **GET** `tickets/list/` — Obtener todos los tickets
    * **Descripción**: Este *endpoint* retorna una lista completa de todos los tickets registrados en el sistema.
    * **Método**: `GET`
    * **Autenticación requerida**: Admin
    * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "data": [
                {
                    "flight_number": "120",
                    "reservation_date": "2025-09-10T00:00:00Z",
                    "ticket_number": "12",
                    "issue_date": "2025-10-10T13:04:32.983698Z",
                    "barcode": "7791234567895",
                    "status": "Activo"
                }
                // ... (Otros tickets)
            ]
        }
        ```
* **GET** `tickets/ticket/<str:barcode>/` — Obtener un ticket específico a través de su código
    * **Descripción**: Este *endpoint* retorna la información detallada de un ticket específico, identificado por su **código de barras** (`barcode`).
    * **Método**: `GET`
    * **Autenticación requerida**: Admin
    * **Cuerpo de la Solicitud (*Request body*)**: Ninguna
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "data": {
                "flight_number": "120",
                "reservation_date": "2025-09-10T00:00:00Z",
                "ticket_number": "12",
                "issue_date": "2025-10-10T13:04:32.983698Z",
                "barcode": "7791234567895",
                "status": "Activo"
            }
        }
        ```
     ---
    > **Nota**: El `<str:barcode>` en la URL debe ser reemplazado por el código de barras único del ticket que se desea consultar (ejemplo: `7791234567895`).
    ---
    
  
  * **POST** `tickets/create/` — Crear ticket
    * **Descripción**: Este *endpoint* se utiliza para generar un nuevo ticket, enlazándolo a una **Reservación** única a través de su clave primaria. El `ticket_number` y el `barcode` se generan automáticamente.
    * **Método**: `POST`
    * **Autenticación requerida**: IsAuthenticated (**Usuario autenticado**)
    * **Cuerpo de la Solicitud (*Request body*)**:
        ```json
        {
            "reservation_id": 15 
            // ID de la Reservación para la cual se está emitiendo el ticket.
            // Debe ser una reservación válida y sin ticket asociado.
        }
        ```
    * **Cuerpo de la Respuesta (*Response body*)**:
        ```json
        {
            "message": "El ticket fue creado con éxito",
            "data": {
                "id": 1,
                "reservation_id": 15,
                "ticket_number": "TICKET-0001", 
                "issue_date": "2025-11-05T18:28:24.000000Z", // Generado automáticamente
                "barcode": "7798765432109", // Generado automáticamente
                "status": "Activo" // Valor por defecto
            }
        }
        ```
 ---
 
 ## ✍️ Autores 

- [@t.bratik](https://github.com/tom1mvp)
- [@m.geller](https://github.com/MarcosAyrton)
- [@s.giacomucci](https://github.com/Stefano818-bot)
