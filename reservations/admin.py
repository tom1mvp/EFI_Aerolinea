from django.contrib import admin
from reservations.models import Reservation
from reservations.services.reservations import ReservationServices


@admin.register(Reservation)
class ReservationsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'passenger', 'flight', 'seat',
        'flight_number', 'reservation_date', 'status'
    )
    list_filter = ('flight_number', 'status')
    search_fields = ('reservation_code',)

    def save_model(self, request, obj, form, change):
        try:
            ReservationServices.check_seat_availability(
                flight_id=obj.flight.id,
                seat_id=obj.seat.id
            )

            if not change:
                ReservationServices.create_reservation(
                    passenger_id=obj.passenger.id,
                    flight_id=obj.flight.id,
                    seat_id=obj.seat.id,
                    flight_number=obj.flight_number,
                    status=obj.status,
                    price=obj.price,
                    reservation_code=obj.reservation_code
                )
            else:
                ReservationServices.update_reservation(
                    reservation_id=obj.id,
                    passenger_id=obj.passenger.id,
                    flight_id=obj.flight.id,
                    seat_id=obj.seat,
                    flight_number=obj.flight_number,
                    status=obj.status,
                    price=obj.price,
                    reservation_code=obj.reservation_code
                )
        except ValueError as e:
            self.message_user(request, str(e), level='error')

    def delete_model(self, request, obj):
        ReservationServices.delete_reservation(reservation_id=obj.id)
