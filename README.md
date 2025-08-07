## 🛪 EFI Django 2025: *Aerolíneas Splinter* 🧑‍✈️

**Actualización del día Viernes 01/08/2025**:

Se añadieron funcionalidades clave relacionadas con el sistema de **reservas de vuelos**, autenticación y gestión de usuarios.  
Además, se reemplazó el modelo de usuario por una implementación basada en `AbstractUser`, permitiendo una mayor personalización del sistema.

A continuación, se detalla el contenido y las novedades de esta versión.

---

## ⚙️ Funcionalidades principales

### ✅ Sistema de autenticación

- Registro e inicio de sesión totalmente funcionales.
- Navbar contextual con opciones según el estado de sesión.
- Acceso restringido a funcionalidades importantes (como reservar un asiento).

### 🧑‍💼 Cambio de modelo de usuario

El modelo de usuario fue reemplazado por una clase personalizada basada en `**AbstractUser**`, lo cual permite:

- Agregar campos personalizados fácilmente (por ejemplo, número de documento o teléfono).
- Mayor flexibilidad para futuras funcionalidades (roles, permisos extendidos, etc.).
- Compatibilidad total con el sistema de autenticación de Django.

Más sobre esto en la [documentación oficial](https://docs.djangoproject.com/en/stable/topics/auth/customizing/#substituting-a-custom-user-model).

---

## ✈️ Sistema de reservas

Un usuario **logueado** ahora puede:

1. Visualizar los **asientos disponibles** de un vuelo específico.
2. Seleccionar un asiento **libre**.
3. Confirmar su reserva ingresando su **documento (DNI)** y **teléfono**.
4. Ver todas sus **reservas realizadas** con información detallada.

Los asientos están clasificados visualmente como:

- 🟩 **Libre** → Disponible para reservar.
- 🟨 **Reservado** → Ya fue apartado por otro usuario.
- 🟥 **Ocupado** → No está disponible (por uso anterior u otra lógica de negocio).

---

## 🚫 Restricciones del sistema

El sistema impone las siguientes **reglas** para asegurar integridad y coherencia:

- 🔁 **Solo una reserva por vuelo**: un usuario no puede reservar más de una vez en el mismo vuelo.
- ✅ El usuario debe ingresar el **mismo DNI y teléfono** que haya usado anteriormente.
- ⛔️ No es posible seleccionar un asiento **ocupado** ni **reservado**.
- 👤 Las reservas solo están disponibles para **usuarios autenticados**.

---

## 📦 Contenido

Se incorporaron mejoras visuales y de estructura:

- Templates principales: `bmy_reservations`, `seat_selection.html`.
- Integración con **Tailwind CSS** mediante `django-tailwind` para una experiencia moderna, responsiva y estilizada.

---

## 🧩 Navegación y estructura

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
