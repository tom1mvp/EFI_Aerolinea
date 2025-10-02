from django.db import models

class Airplane(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    rows = models.IntegerField()
    columns = models.IntegerField()
    status = models.CharField(max_length=20, choices=[
         ('activo', 'Activo'),
        ('mantenimiento', 'Mantenimiento')], default='activo')
    
    def __str__(self):
        return f'Avion: {self.name} || Capacidad: {self.capacity} || Estado: {self.status}'
    
class Seat(models.Model):
    airplane = models.ForeignKey(Airplane, on_delete=models.PROTECT, related_name='seat')
    number = models.CharField(max_length=10)
    rows = models.IntegerField()
    columns = models.IntegerField()
    type_seat = models.CharField(max_length=20, choices=[
        ('economico', 'Economico'),
        ('ejecutivo', 'Ejecutivo')
    ], default='economico')
    status = models.CharField(max_length=20, choices=[
        ('disponible', 'Disponible'),
        ('fuera de servicio', 'Fuera de Servicio'),
        ('reservado', 'Reservado')
    ], default='disponible')
    
    def __str__(self):
        return f'Núm de asiento: {self.number} || Fila: {self.rows} || Columna: {self.columns} Tipo de asiento: {self.type_seat} || Estado: {self.status}'