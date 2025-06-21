from django.db import models
from user.models import User

class Passenger(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='passengers')
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.user.email} - {self.phone_number}"
