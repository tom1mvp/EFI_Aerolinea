from reservations.repositories.reservation import ReservationRepository
from passengers_management.repositories.passenger import PassengerRepository

class ReservationServices:
    @staticmethod
    def get_all_reservations():
        return ReservationRepository.get_all_reservations()

    @staticmethod
    def get_reservation_by_id(reservation_id):
        return ReservationRepository.get_by_id(reservation_id)

    @staticmethod
    def create_reservation(passenger_id, flight_number):
        passenger = PassengerRepository.get_by_id(passenger_id)
        if not passenger:
            raise ValueError("Passenger not found.")
        return ReservationRepository.create_reservation(passenger=passenger, flight_number=flight_number)

    @staticmethod
    def update_reservation(reservation_id, passenger_id, flight_number, status):
        reservation = ReservationRepository.get_by_id(reservation_id)
        if not reservation:
            raise ValueError("Reservation not found.")
        passenger = PassengerRepository.get_by_id(passenger_id)
        if not passenger:
            raise ValueError("Passenger not found.")
        return ReservationRepository.update_reservation(reservation=reservation, passenger=passenger, flight_number=flight_number, status=status)

    @staticmethod
    def delete_reservation(reservation_id):
        reservation = ReservationRepository.get_by_id(reservation_id)
        if not reservation:
            raise ValueError("Reservation not found.")
        return ReservationRepository.delete_reservation(reservation=reservation)
