import mailtrap as mt
from django.conf import settings

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


    # Function: Report passagers by flights
    @staticmethod
    def reports_passagers_by_flights(flight_id):
        reservations = ReservationRepository.get_by_flight_id(flight_id)
        
        if not reservations.exists():
            raise ValueError('No reservations found for this flight.')

        data = []
        
        for reservation in reservations:
            passenger = reservation.passenger.user
            data.append({
                'pasajero': f"{passenger.first_name} {passenger.last_name}",
                'email': passenger.email,
                'documento': reservation.passenger.document,
                'telefono': reservation.passenger.phone_number,
                'asiento': reservation.seat.number,   # <-- acá el cambio
                'fecha_reserva': reservation.reservation_date,
                'estado': reservation.status,
                'precio': str(reservation.price),
                'codigo_reserva': reservation.reservation_code,
            })


        return data


    # Send email
    @staticmethod
    def send_mail(reservation_id):
        reservation = ReservationRepository.get_by_id(reservation_id=reservation_id)
        
        if not reservation:
            raise ValueError("No se encontro la reservación.")
        
        passenger = reservation.passenger.user
        
        passenger_mail = passenger.email
        
        
        if passenger_mail.endswith("@gmail.com") or passenger_mail.endswith("@hotmail.com"):
            mail = mt.Mail(
                sender=mt.Address(email="splinteraerolineas@gmail.com", name="Aerolineas Splinter"),
                to=[mt.Address(email=passenger_mail)],
                subject="Confirmación de boleto",
                text = (
                    f"Su reserva ({reservation}) fue registrada con éxito para el día "
                    f"{reservation.reservation_date} con un precio de ${reservation.price}. "
                    f"Su código de reserva es {reservation.reservation_code}."
                ),
                category="Alert",
            )
            
            client = mt.MailtrapClient(token=settings.MAILTRAP_TOKEN)
            response = client.send(mail)
            
            return response
        else:
            raise ValueError("No se pudo enviar el mail")
        