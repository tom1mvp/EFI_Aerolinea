from reservations.models import Reservation
from passengers_management.models import Passenger
from flights_management.models import Flight
from airplanes_management.models import Seat


class ReservationRepository:
    @staticmethod
    def get_all_reservations():
        return Reservation.objects.all()

    @staticmethod
    def get_by_id(reservation_id):
        return Reservation.objects.filter(id=reservation_id).first()
    
    @staticmethod
    def get_by_flight_id(flight_id):
     return Reservation.objects.filter(flight_id=flight_id).select_related('passenger__user', 'seat')


    @staticmethod
    def create_reservation(
        passenger,
        flight,
        seat,
        flight_number,
        status,
        price,
        reservation_code
    ):
        new_reservation = Reservation.objects.create(
            passenger=passenger,
            flight=flight,
            seat=seat,
            flight_number=flight_number,
            status=status,
            price=price,
            reservation_code=reservation_code
        )
    
        return new_reservation

    @staticmethod
    def update_reservation(
        reservation,
        passenger,
        flight,
        seat,
        flight_number,
        status,
        price,
        reservation_code
    ):
        reservation.passenger = passenger
        reservation.flight = flight
        reservation.seat = seat
        reservation.flight_number = flight_number
        reservation.status = status
        reservation.price = price
        reservation.reservation_code = reservation_code
        reservation.save()
        return reservation


    @staticmethod
    def delete_reservation(reservation_id):
        reservation = Reservation.objects.filter(id=reservation_id).first()

        if not reservation:
            raise ValueError("No se encontró la reservación")

        reservation.delete()
        return True

    @staticmethod
    def check_seat_availability(flight_id, seat_id):
        seat_reserved = Reservation.objects.filter(
            flight_id=flight_id,
            seat_id=seat_id
        ).exists()

        if seat_reserved:
            raise ValueError('El asiento ya está reservado en este vuelo')

        return True
