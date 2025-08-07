## 🛪 EFI Django 2025: *Aerolíneas Splinter* 🧑‍✈️

Actualización: Sábado 21/06/2025**

En esta versión se integró la funcionalidad completa de **gestión de tickets** y se mejoró el sistema de **reservas de vuelos y pasajeros**, estructurado bajo capas de `services` y `repositories`.

---

## ⚙️ Funcionalidades principales

### 🎫 Tickets

- Se implementan operaciones CRUD: **listar**, **ver detalle**, **crear** y **eliminar** tickets.
- Cada operación utiliza vistas basadas en funciones con sus respectivos templates:
  - `list.html`
  - `detail.html`
  - `create.html`
  - `delete.html`

### 🛪 Pasajeros y Reservas

- Se incorporó el modelo `Passenger`, asociado a un usuario (`User`) con campos como:
  - Documento y número de teléfono.
- Se implementaron funcionalidades para:
  - Crear, editar y eliminar pasajeros.
  - Crear y cancelar reservas de vuelo.
- Toda la lógica de negocio se organiza mediante `services` y `repositories` para garantizar un código limpio y mantenible.

---

## ✅  Navegación y estructura del sistema

- Barra de navegación dinámica (navbar) con opciones adaptadas según el estado de autenticación.
- Vistas públicas y privadas protegidas por login.
- Formularios validados y responsivos utilizando **Django + Tailwind CSS**.
- Flujo de autenticación completo (registro, inicio y cierre de sesión).

---




## ✅  Navegación y estructura

El sistema incluye:

- Barra de navegación dinámica.
- Vistas públicas y protegidas.
- Flujo de autenticación seguro.
- Formularios claros y consistentes.

---


## ✍️ Autores 

- [@t.bratik](https://github.com/tom1mvp)
- [@m.geller](https://github.com/MarcosAyrton)
- [@s.giacomucci](https://github.com/Stefano818-bot)
