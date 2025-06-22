from reservations.repositories.reservations import ReservationRepository
from passengers_management.repositories.passengers import PassengerRepository
from flights_management.repositories.flights import FlightsRepository
from airplanes_management.repositories.airplaine import AirplaneRepository


class ReservationServices:
    @staticmethod
    def get_all_reservations():
        return ReservationRepository.get_all_reservations()

    @staticmethod
    def get_reservation_by_id(reservation_id):
        return ReservationRepository.get_by_id(reservation_id)

    @staticmethod
    def create_reservation(passenger_id, flight_id, seat_id, flight_number, status, price, reservation_code):
        passenger = PassengerRepository.get_by_id(passenger_id=passenger_id)
        flight = FlightsRepository.get_by_id(flight_id=flight_id)
        seat = AirplaneRepository.get_seat_by_id(seat_id=seat_id)

        if not passenger:
            raise ValueError("Pasajero no encontrado.")
        if not flight:
            raise ValueError("Vuelo no encontrado.")
        if not seat:
            raise ValueError("Asiento no encontrado.")

        
        ReservationServices.check_seat_availability(flight_id, seat_id)

        return ReservationRepository.create_reservation(
            passenger=passenger,
            flight=flight,
            seat=seat,
            flight_number=flight_number,
            status=status,
            price=price,
            reservation_code=reservation_code
        )

    @staticmethod
    def update_reservation(reservation_id, passenger_id, flight_id, seat_id, flight_number, status, price, reservation_code):
        reservation = ReservationRepository.get_by_id(reservation_id)
        passenger = PassengerRepository.get_by_id(passenger_id)
        flight = FlightsRepository.get_by_id(flight_id)
        seat = AirplaneRepository.get_seat_by_id(seat_id)

        if not reservation:
            raise ValueError("Reservación no encontrada.")
        if not passenger:
            raise ValueError("Pasajero no encontrado.")
        if not flight:
            raise ValueError("Vuelo no encontrado.")
        if not seat:
            raise ValueError("Asiento no encontrado.")

        return ReservationRepository.update_reservation(
            reservation=reservation,
            passenger=passenger,
            flight=flight,
            seat=seat,
            flight_number=flight_number,
            status=status,
            price=price,
            reservation_code=reservation_code
        )

    @staticmethod
    def delete_reservation(reservation_id):
        reservation = ReservationRepository.get_by_id(reservation_id)
        if reservation:
            return ReservationRepository.delete_reservation(reservation)
        return False

    @staticmethod
    def check_seat_availability(flight_id, seat_id):
        return ReservationRepository.check_seat_availability(flight_id, seat_id)


    """ Falta crear la generacion de boletos electronicos (proxima version) """