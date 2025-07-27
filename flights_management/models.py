from django.db import models


class Flight(models.Model):
    airplane = models.ForeignKey('airplanes_management.Airplane', on_delete=models.PROTECT)
    origin = models.CharField(max_length=100, null=False)
    destination = models.CharField(max_length=100, null=False)
    departure_date = models.DateField(null=False, blank=False)
    arrival_date = models.DateField(null=False, blank=False)
    duration = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    status = models.CharField(max_length=20, choices=[
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo')
    ])
    base_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    
    def __str__(self):
        return f"Avion: {self.airplane.name} | Duración: {self.duration} | Destino: {self.destination}"