from django.db import models
from passengers_management.models import Passenger

class Reservation(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.PROTECT, related_name='reservations')
    flight_number = models.CharField(max_length=20)
    reservation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"Reservation {self.id} - {self.passenger.user.first_name} {self.passenger.user.last_name}"
