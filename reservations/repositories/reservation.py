from reservations.models import Reservation

class ReservationRepository:
    @staticmethod
    def get_all_reservations():
        return Reservation.objects.all()

    @staticmethod
    def get_by_id(reservation_id):
        return Reservation.objects.filter(id=reservation_id).first()

    @staticmethod
    def create_reservation(passenger, flight_number):
        return Reservation.objects.create(passenger=passenger, flight_number=flight_number)

    @staticmethod
    def update_reservation(reservation, passenger, flight_number, status):
        reservation.passenger = passenger
        reservation.flight_number = flight_number
        reservation.status = status
        reservation.save()
        return reservation

    @staticmethod
    def delete_reservation(reservation):
        reservation.delete()
