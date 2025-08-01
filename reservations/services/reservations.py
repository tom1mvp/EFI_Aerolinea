import mailtrap as mt
import uuid

from django.conf import settings
from django.contrib import messages
from reservations.repositories.reservations import ReservationRepository
from passengers_management.repositories.passengers import PassengerRepository
from flights_management.repositories.flights import FlightsRepository
from airplanes_management.repositories.airplaine import AirplaneRepository
from airplanes_management.models import Airplane,Seat
from passengers_management.models import Passenger
from reservations.models import Reservation

class ReservationServices:
    @staticmethod
    def get_all_reservations():
        return ReservationRepository.get_all_reservations()

    @staticmethod
    def get_reservation_by_id(reservation_id):
        return ReservationRepository.get_by_id(reservation_id)
    @staticmethod
    def get_seat_selection_context(flight_id):
        flight = FlightsRepository.get_by_id(flight_id)
        if not flight:
            raise ValueError("Vuelo no encontrado.")

        airplane = flight.airplane
        seats = Seat.objects.filter(airplane=airplane).order_by('number')

        reserved_seat_ids = set(
            Reservation.objects.filter(flight=flight, status='reservado').values_list('seat_id', flat=True)
        )

        occupied_seat_ids = set(
            Reservation.objects.filter(flight=flight, status='ocupado').values_list('seat_id', flat=True)
        )

        for seat in seats:
            if seat.id in occupied_seat_ids:
                seat.state = 'ocupado'
            elif seat.id in reserved_seat_ids:
                seat.state = 'reservado'
            else:
                seat.state = 'libre'

        
        seat_rows = []
        for seat in seats:
            number_part = seat.number[1:]
            if number_part.isdigit():
                seat_rows.append(int(number_part))
        max_row = max(seat_rows) if seat_rows else 0
        seat_letters = sorted(set(seat.number[0] for seat in seats))

        return {
            'flight': flight,
            'seats': seats,
            'max_row': max_row,
            'seat_letters': seat_letters,
        }


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
    @staticmethod
    def reserve_seat(user, flight_id, seat_id, document, phone_number):
        if not seat_id:
            return {
                "success": False,
                "message": "Debes seleccionar un asiento.",
                "level": messages.ERROR
            }

        flight = FlightsRepository.get_by_id(flight_id)
        seat = AirplaneRepository.get_seat_by_id(seat_id)

        if not flight:
            return {
                "success": False,
                "message": "Vuelo no encontrado.",
                "level": messages.ERROR
            }
        if not seat:
            return {
                "success": False,
                "message": "Asiento no encontrado.",
                "level": messages.ERROR
            }

        # ❌ Validación: ¿el usuario ya tiene una reserva en este vuelo?
        existing_reservation = Reservation.objects.filter(passenger__user=user, flight=flight).first()
        if existing_reservation:
            return {
                "success": False,
                "message": "Ya tienes una reserva para este vuelo.",
                "level": messages.ERROR
            }

        try:
            ReservationRepository.check_seat_availability(flight.id, seat.id)
        except ValueError as e:
            return {
                "success": False,
                "message": str(e),
                "level": messages.ERROR
            }

        # ✅ Verificar si ya existe un pasajero con ese user
        passenger = Passenger.objects.filter(user=user).first()
        if passenger:
            # Verificar que DNI y teléfono coincidan
            if passenger.document != document or passenger.phone_number != phone_number:
                return {
                    "success": False,
                    "message": "Los datos del pasajero no coinciden con los registrados.",
                    "level": messages.ERROR
                }
        else:
            # Crear nuevo pasajero si no existe
            passenger = Passenger.objects.create(
                user=user,
                document=document,
                phone_number=phone_number
            )

        flight_number = f"{flight.origin[:3]}-{flight.destination[:3]}-{flight.departure_date.strftime('%Y%m%d')}"
        reservation_code = f"{flight.origin[:3]}-{flight.destination[:3]}-{uuid.uuid4().hex[:6]}"

        ReservationRepository.create_reservation(
            passenger=passenger,
            flight=flight,
            seat=seat,
            flight_number=flight_number,
            status='reservado',
            price=flight.base_price,
            reservation_code=reservation_code
        )

        return {
            "success": True,
            "message": "¡Reserva exitosa! Recibirás un correo de confirmación.",
            "level": messages.SUCCESS
        }
