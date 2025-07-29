from django.apps import AppConfig


class AirplanesManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'airplanes_management'

    def ready(self):
        from . import signal
        return super().ready()