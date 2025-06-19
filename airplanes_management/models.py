from django.db import models

# Create your models here.
class Airplane(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    rows = models.IntegerField()
    columns = models.IntegerField()
    state = models.CharField(max_length=20, choices=[
        ('activo', 'Activo'),
        ('mantenimiento', 'Mantenimiento')], default='activo')
    def __str__(self):
        return f"{self.name}({self.id})"


class Seat(models.Model):
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    rows = models.IntegerField()
    columns = models.IntegerField()
    tipe = models.CharField(max_length=20, choices=[
        ('economico', 'Economico'),
        ('ejecutivo', 'Ejecutivo')], default='economico')
    state = models.CharField(max_length=20, choices=[
        ('disponible', 'Disponible'),
        ('fuera de servicio', 'Fuera de Servicio'),
        ('reservado', 'Reservado')], default='disponible')

    def __str__(self):
        return f"{self.number}({self.airplane.name})"  