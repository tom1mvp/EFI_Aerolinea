from django.urls import path
from .views import select_seat, my_reservations

urlpatterns = [
    path('reservar/<int:flight_id>/asientos/', select_seat, name='select_seat'),
    path('my-reservations/', my_reservations, name='my_reservations'),
]