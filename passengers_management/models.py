from django.db import models


class Passanger(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='passenger_profile')
    
    check_in_status = models.BooleanField(default=False)
    passenger_type = models.CharField(
        max_length=20,
        choices=[
            ('adult', 'Adulto'),
            ('child', 'Niño'),
            ('infant', 'Bebé'),
        ],
        default='adult'
    )
    nationality = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Nombre: {self.user.name} || Usuario: {self.user.username} || Vuelo: {self.flight.origin} - {self.flight.destination} || Asiento: {self.seat.number}"