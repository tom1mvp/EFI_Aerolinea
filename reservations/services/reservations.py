import mailtrap as mt
import uuid

from django.conf import settings
from django.contrib import messages
from django.utils.translation import gettext as _
from django.core.mail import EmailMultiAlternatives
from reservations.repositories.reservations import ReservationRepository
from passengers_management.repositories.passengers import PassengerRepository
from flights_management.repositories.flights import FlightsRepository
from airplanes_management.repositories.airplaine import AirplaneRepository
from airplanes_management.models import Seat
from passengers_management.models import Passenger
from reservations.models import Reservation


class ReservationServices:
    @staticmethod
    def get_all_reservations():
        return ReservationRepository.get_all_reservations()

    @staticmethod
    def get_reservation_by_id(reservation_id):
        reservation = ReservationRepository.get_by_id(reservation_id)
        if not reservation:
            raise ValueError(_("Reservación no encontrada."))
        return reservation

    @staticmethod
    def get_seat_selection_context(flight_id):
        flight = FlightsRepository.get_by_id(flight_id)
        if not flight:
            raise ValueError(_("Vuelo no encontrado."))

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
            raise ValueError(_("Pasajero no encontrado."))
        if not flight:
            raise ValueError(_("Vuelo no encontrado."))
        if not seat:
            raise ValueError(_("Asiento no encontrado."))

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
    def update_reservation(**kwargs):
        raise ValueError(_("Actualizar reserva no está implementado con esta firma."))

    @staticmethod
    def delete_reservation(reservation_id):
        return ReservationRepository.delete_reservation(reservation_id)

    @staticmethod
    def check_seat_availability(flight_id, seat_id):
        return ReservationRepository.check_seat_availability(flight_id, seat_id)

    @staticmethod
    def reports_passagers_by_flights(flight_id):
        reservations = ReservationRepository.get_by_flight_id(flight_id)
        if not reservations.exists():
            raise ValueError(_('No reservations found for this flight.'))

        data = []
        for reservation in reservations:
            passenger = reservation.passenger.user
            data.append({
                'pasajero': f"{passenger.first_name} {passenger.last_name}",
                'email': passenger.email,
                'documento': reservation.passenger.document,
                'telefono': reservation.passenger.phone_number,
                'asiento': reservation.seat.number,
                'fecha_reserva': reservation.reservation_date,
                'estado': reservation.status,
                'precio': str(reservation.price),
                'codigo_reserva': reservation.reservation_code,
            })
        return data

    @staticmethod
    def _get_mailtrap_client():
        token = getattr(settings, "MAILTRAP_API_KEY", None)
        if not token:
            return None
        try:
            return mt.MailtrapClient(token=token)
        except Exception:
            return None

    @staticmethod
    def _build_email_payload(reservation):
        user = getattr(reservation.passenger, 'user', None)
        recipient = getattr(user, 'email', None)

        if not recipient:
            raise ValueError(_("La reserva no tiene un destinatario de email válido."))

        subject = _("Confirmación de tu reserva")
        plain = _(
            "Hola {name},\n\nTu reserva fue confirmada.\n\nCódigo: {code}\nVuelo: {flight}\n"
            "Asiento: {seat}\nFecha: {date}\n\nGracias por elegirnos."
        ).format(
            name=(getattr(user, 'first_name', '') or getattr(user, 'username', '')),
            code=getattr(reservation, 'reservation_code', ''),
            flight=str(getattr(reservation, 'flight', '')),
            seat=str(getattr(reservation, 'seat', '')),
            date=str(getattr(getattr(reservation, 'flight', None), 'departure_date', '')),
        )
        html = f"""
        <!doctype html>
        <html lang="es">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>{subject}</title>
          </head>
          <body style="margin:0;padding:0;background-color:#f6f7fb;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f6f7fb;">
              <tr>
                <td align="center" style="padding:24px;">
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:680px;background:#ffffff;border-radius:16px;overflow:hidden;border:1px solid #ffedd5;">
                    <tr>
                      <td style="background:linear-gradient(135deg,#fb923c,#f97316);padding:28px 24px;color:#ffffff;">
                        <h1 style="margin:0;font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:20px;letter-spacing:.3px;">Aerolineas Splinter</h1>
                        <p style="margin:8px 0 0 0;font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:13px;opacity:.95;">{_('Confirmación de reserva')}</p>
                      </td>
                    </tr>
                    <tr>
                      <td style="padding:24px 24px 8px 24px;">
                        <h2 style="margin:0 0 6px 0;font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-weight:700;font-size:18px;color:#7c2d12;">{subject}</h2>
                        <p style="margin:0 0 12px 0;font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:15px;line-height:1.7;color:#4b5563;">
                          {_('Hola')} {(getattr(user, 'first_name', '') or getattr(user, 'username', ''))},
                        </p>
                        <p style="margin:0 0 18px 0;font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:15px;line-height:1.7;color:#4b5563;">
                          {_('Tu reserva fue confirmada.')}
                        </p>
                        <table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="border-collapse:separate;border-spacing:0 10px;">
                          <tr>
                            <td style="background:#fff7ed;border:1px solid #ffedd5;border-radius:12px;padding:14px 16px;">
                              <table role="presentation" width="100%%" cellpadding="0" cellspacing="0">
                                <tr>
                                  <td style="font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:13px;color:#9a3412;width:140px;">{_('Código')}:</td>
                                  <td style="font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:15px;color:#7c2d12;font-weight:700;">{getattr(reservation, 'reservation_code', '')}</td>
                                </tr>
                                <tr>
                                  <td style="font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:13px;color:#9a3412;width:140px;">{_('Vuelo')}:</td>
                                  <td style="font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:15px;color:#7c2d12;font-weight:700;">{getattr(reservation, 'flight', '')}</td>
                                </tr>
                                <tr>
                                  <td style="font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:13px;color:#9a3412;width:140px;">{_('Asiento')}:</td>
                                  <td style="font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:15px;color:#7c2d12;font-weight:700;">{getattr(reservation, 'seat', '')}</td>
                                </tr>
                                <tr>
                                  <td style="font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:13px;color:#9a3412;width:140px;">{_('Fecha')}:</td>
                                  <td style="font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:15px;color:#7c2d12;font-weight:700;">{getattr(getattr(reservation, 'flight', None), 'departure_date', '')}</td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                        <p style="margin:18px 0 0 0;font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:14px;line-height:1.7;color:#4b5563;">
                          {_('Gracias por elegirnos.')}
                        </p>
                      </td>
                    </tr>
                    <tr>
                      <td style="padding:0 24px 24px 24px;">
                        <div style="height:1px;background:#ffedd5;margin:8px 0 16px 0;"></div>
                        <p style="margin:0;font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:12px;line-height:1.6;color:#9a3412;">
                          {_('Este mensaje fue enviado automáticamente. Por favor no respondas a este correo.')}
                        </p>
                      </td>
                    </tr>
                    <tr>
                      <td style="background:#fff7ed;padding:16px 24px;color:#9a3412;font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:12px;">
                        © {__import__('datetime').datetime.now().year} Aerolineas Splinter. {_('Todos los derechos reservados.') }
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </body>
        </html>
        """.strip()

        return recipient, subject, plain, html

    @staticmethod
    def _validate_sender(email: str):
        """
        Validación mínima: que exista un remitente.
        Usa el remitente que te funciona (tu propio mail o el que tengas verificado en Mailtrap).
        """
        if not email:
            raise ValueError(_("No hay remitente configurado."))

    @staticmethod
    def _send_via_mailtrap_api(recipient, subject, plain, html):
        client = ReservationServices._get_mailtrap_client()
        if client is None:
            raise ValueError(_("Mailtrap no está configurado. Defina MAILTRAP_TOKEN en el .env."))

        sender_email = getattr(settings, "MAILTRAP_SENDER_EMAIL", None)
        ReservationServices._validate_sender(sender_email)

        mail = mt.Mail(
            sender=mt.Address(email=sender_email, name="Aerolineas Splinter"),
            to=[mt.Address(email=recipient)],
            subject=subject,
            text=plain,
            html=html,
            category="Reservation Confirmation",
        )
        return client.send(mail)

    @staticmethod
    def _send_via_smtp(recipient, subject, plain, html):
        """
        Envío por SMTP (Mailtrap live SMTP).
        """
        from_email = getattr(settings, "DEFAULT_FROM_EMAIL", None)
        ReservationServices._validate_sender(from_email)

        msg = EmailMultiAlternatives(subject=subject, body=plain, from_email=from_email, to=[recipient])
        msg.attach_alternative(html, "text/html")
        msg.send(fail_silently=False)
        return True

    @staticmethod
    def send_mail(reservation_id: int):
        reservation = ReservationRepository.get_by_id(reservation_id=reservation_id)
        if not reservation:
            raise ValueError(_("No se encontró la reservación."))

        recipient, subject, plain, html = ReservationServices._build_email_payload(reservation)

        token = getattr(settings, "MAILTRAP_API_KEY", None)
        # Si tienes token de Sending, intentar API primero y fallback a SMTP ante 401/Unauthorized.
        if token:
            try:
                return ReservationServices._send_via_mailtrap_api(recipient, subject, plain, html)
            except Exception as e:
                if "unauthorized" in str(e).lower() or "401" in str(e).lower():
                    return ReservationServices._send_via_smtp(recipient, subject, plain, html)
                # Si falla por otro motivo, probamos igual SMTP como respaldo
                return ReservationServices._send_via_smtp(recipient, subject, plain, html)
        # Si no hay token, vamos directo por SMTP
        return ReservationServices._send_via_smtp(recipient, subject, plain, html)

    @staticmethod
    def reserve_seat(user, flight_id, seat_id, document, phone_number):
        if not seat_id:
            return {
                "success": False,
                "message": _("Debes seleccionar un asiento."),
                "level": messages.ERROR
            }

        flight = FlightsRepository.get_by_id(flight_id)
        seat = AirplaneRepository.get_seat_by_id(seat_id)

        if not flight:
            return {
                "success": False,
                "message": _("Vuelo no encontrado."),
                "level": messages.ERROR
            }
        if not seat:
            return {
                "success": False,
                "message": _("Asiento no encontrado."),
                "level": messages.ERROR
            }

        existing_reservation = Reservation.objects.filter(passenger__user=user, flight=flight).first()
        if existing_reservation:
            return {
                "success": False,
                "message": _("Ya tienes una reserva para este vuelo."),
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

        passenger = Passenger.objects.filter(user=user).first()
        if passenger:
            if passenger.document != document or passenger.phone_number != phone_number:
                return {
                    "success": False,
                    "message": _("Los datos del pasajero no coinciden con los registrados."),
                    "level": messages.ERROR
                }
        else:
            passenger = Passenger.objects.create(
                user=user,
                document=document,
                phone_number=phone_number
            )

        flight_number = f"{flight.origin[:3]}-{flight.destination[:3]}-{flight.departure_date.strftime('%Y%m%d')}"
        reservation_code = f"{flight.origin[:3]}-{flight.destination[:3]}-{uuid.uuid4().hex[:6]}"

        reservation = ReservationRepository.create_reservation(
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
            "message": _("¡Reserva exitosa! Recibirás un correo de confirmación."),
            "level": messages.SUCCESS,
            "reservation_id": reservation.id
        }

    @staticmethod
    def get_all_passengers():
        return Passenger.objects.select_related('user').all()
