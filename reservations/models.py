from django.db import models


from passengers_management.models import Passanger
from airplanes_management.models import Seat


class Reservation(models.Model):
    passanger = models.ForeignKey(Passanger, on_delete=models.PROTECT, related_name='reservations')
    flight = models.ForeignKey('flights_management.Flight', on_delete=models.PROTECT)
    seat = models.OneToOneField(Seat, on_delete=models.PROTECT)
    
    flight_number = models.CharField(max_length=20)
    ticket_number = models.CharField(max_length=20, unique=True)
    reservation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),
        ('ocupado', 'Ocupado')
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reservation_code = models.CharField(max_length=120, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Fecha de reserva: {self.reservation_date} | Nombre del pasajero: {self.passanger.user.name} | Estado: {self.status}"