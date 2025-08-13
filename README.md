## 🛪 EFI Django 2025: *Aerolíneas Splinter* 🧑‍✈️

Actualización: Domingo 22/06/2025**

En esta versión se arreglaron algunos bugs del modulo de **aviones**.Ademas se integro por completo el modulo de **vuelos**.

## ⚙️ Funcionalidades Principales

### ✅ Corrección de Bugs e Integración de Módulos
- Correcciones aplicadas al módulo `airplanes_management`.
- Integración completa del módulo `flights_management`, incluyendo modelo `Flight`, repositorio (`FlightsRepository`) y servicios correspondientes.
- Nuevos métodos CRUD para gestión de vuelos.
- Se utilizó `on_delete=models.PROTECT` para proteger las relaciones entre vuelos y aviones.

---


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
