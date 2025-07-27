from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from airplanes_management.models import Airplane, Seat



@receiver(post_save, sender=Airplane)
def create_seats_for_airplane(sender, instance, created, **kwargs):
    if created:
        for row in range(1, instance.rows + 1):
            for column in range (1, instance.columns + 1):
                number = f"{chr(64 + column)}{row}"
                Seat.objects.create(
                    airplane=instance,
                    number=number,
                    rows=row,
                    columns=column,
                    tipe="economico",
                    state="disponible"
                )
