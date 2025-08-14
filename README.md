
## 🛪 EFI Django 2025: *Aerolíneas Splinter* 🧑‍✈️

**Actualización del día Martes 05/08/2025**:

En esta versión se incorporaron las primeras configuraciones para **traducción automática** de la aplicación y **envío de correos electrónicos**.
Estos avances amplían las capacidades de comunicación y accesibilidad del sistema, preparando el terreno para futuras integraciones.

---

## ⚙️ Funcionalidades principales

### 🌐 Configuración básica de traducción

* Activación del soporte multilenguaje en Django.
* Definición de idioma por defecto y estructura para añadir traducciones futuras.
* Preparación de archivos de localización (`.po` y `.mo`) para personalizar textos en diferentes idiomas.

### 📧 Configuración básica de envío de emails

* Integración inicial con servidor SMTP para enviar correos desde el sistema.
* Posibilidad de enviar notificaciones por email en eventos clave (por ejemplo, confirmación de reserva).
* Plantillas HTML base para emails.

---

## 📦 Contenido

En esta actualización se realizaron cambios clave en la configuración del proyecto:

* Ajustes en `settings.py` para activar **i18n** (internacionalización) y definir rutas de localización.
* Variables de entorno para credenciales SMTP y datos de remitente.
* Inclusión de funciones utilitarias para el envío de correos desde las vistas o servicios del sistema.

---

## 🧩 Navegación y estructura

El sistema mantiene las funcionalidades ya implementadas en actualizaciones anteriores, y suma la base para:

* Traducir la interfaz a otros idiomas.
* Comunicar eventos importantes al usuario vía email.

---

## ✍️ Autores

* [@t.bratik](https://github.com/tom1mvp)
* [@m.geller](https://github.com/MarcosAyrton)
* [@s.giacomucci](https://github.com/Stefano818-bot)

---
