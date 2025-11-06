from rest_framework import serializers


from passengers_management.models import Passanger

class PassangerReportSerializer(serializers.ModelSerializer):
    user_fullname = serializers.SerializerMethodField()
    user_username = serializers.SerializerMethodField()
    flight_number = serializers.SerializerMethodField()
    flight_origin = serializers.SerializerMethodField()
    flight_destination = serializers.SerializerMethodField()
    seat_number = serializers.SerializerMethodField()
    reservation_code = serializers.SerializerMethodField()
    reservation_status = serializers.SerializerMethodField()

    class Meta:
        model = Passanger
        fields = [
            'user_fullname',
            'user_username',
            'check_in_status',
            'passenger_type',
            'nationality',
            'flight_number',
            'flight_origin',
            'flight_destination',
            'seat_number',
            'reservation_code',
            'reservation_status'
        ]

    def get_user_fullname(self, obj):
        return obj.user.name

    def get_user_username(self, obj):
        return obj.user.username

    # Tomamos la primera reserva del pasajero para mostrar datos del vuelo y asiento
    def get_flight_number(self, obj):
        reservation = obj.reservations.first()
        return reservation.flight_number if reservation else None

    def get_flight_origin(self, obj):
        reservation = obj.reservations.first()
        return reservation.flight.origin if reservation else None

    def get_flight_destination(self, obj):
        reservation = obj.reservations.first()
        return reservation.flight.destination if reservation else None

    def get_seat_number(self, obj):
        reservation = obj.reservations.first()
        return reservation.seat.number if reservation else None

    def get_reservation_code(self, obj):
        reservation = obj.reservations.first()
        return reservation.reservation_code if reservation else None

    def get_reservation_status(self, obj):
        reservation = obj.reservations.first()
        return reservation.status if reservation else None
