from django.db import models
from reservations.models import Reservation

class Ticket(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.PROTECT)
    ticket_number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket {self.ticket_number} for Reservation {self.reservation.id}"
