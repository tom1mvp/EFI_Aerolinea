## 🛪 EFI Django 2025: *Aerolíneas Splinter* 🧑‍✈️

Actualización: Domingo 27/07/2025**

En esta versión se modifico la funcionalidad de **reportes** y su modo de uso.Ademas el **usuario sin cuenta** puede ver los vuelos pero si no se registra no los puede reservar


## ⚙️ Funcionalidades Principales

### ✅ Reportes
- Se reemplazó la generación de reportes de pasajeros (desde el panel de admin) por un sistema de exportación de **vuelos en formato Excel**.
- Implementado utilizando la librería [`openpyxl`](https://openpyxl.readthedocs.io/en/stable/).

### ✅ Usuarios sin Cuenta
- Se actualizó la vista principal (`index`) para mostrar vuelos a usuarios no autenticados.
- Al intentar reservar sin estar logueado, se muestra un **modal de confirmación** y se redirige al **login** para continuar con la reserva.

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
