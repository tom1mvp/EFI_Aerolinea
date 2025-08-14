import openpyxl

from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest
from reservations.models import Reservation
from reservations.services.reservations import ReservationServices
from django.conf import settings


@login_required
def send_example_email(request):
    """
    Envía un email de prueba al usuario autenticado usando el backend SMTP configurado.
    Con Mailtrap live SMTP, el mensaje se entregará según tu remitente (DEFAULT_FROM_EMAIL/EMAIL_HOST_USER).
    """
    recipient = getattr(request.user, "email", None)
    if not recipient:
        return HttpResponseBadRequest('El usuario autenticado no tiene un email registrado.')

    try:
        subject = "Prueba de correo"
        plain = "Este es un correo de prueba desde el entorno de la aerolínea."
        html = "<p>Este es un <strong>correo de prueba</strong> desde el entorno de la aerolínea.</p>"

        from_email = getattr(settings, "DEFAULT_FROM_EMAIL", None) or settings.EMAIL_HOST_USER
        msg = EmailMultiAlternatives(subject=subject, body=plain, from_email=from_email, to=[recipient])
        msg.attach_alternative(html, "text/html")
        msg.send(fail_silently=False)

        return HttpResponse('Email enviado correctamente (SMTP).')
    except Exception as e:
        return HttpResponse(f'Fallo al enviar el email: {str(e)}')


@login_required
def select_seat(request, flight_id):
    if request.method == 'POST':
        document = request.POST.get('document')
        phone_number = request.POST.get('phone_number')
        seat_id = request.POST.get('seat_id')

        result = ReservationServices.reserve_seat(
            user=request.user,
            flight_id=flight_id,
            seat_id=seat_id,
            document=document,
            phone_number=phone_number
        )
        messages.add_message(request, result["level"], result["message"])

        if result.get("success"):
            reservation_id = result.get("reservation_id")

            if not reservation_id:
                last_reservation = (
                    Reservation.objects
                    .filter(passenger__user=request.user, flight_id=flight_id)
                    .order_by('-reservation_date')
                    .first()
                )
                reservation_id = last_reservation.id if last_reservation else None

            if reservation_id:
                try:
                    ReservationServices.send_mail(reservation_id)
                    messages.success(request, "Confirmación enviada al correo registrado.")
                except Exception as e:
                    messages.warning(request, f"La reserva fue confirmada, pero ocurrió un problema al enviar el correo: {e}")
            else:
                messages.warning(request, "Reserva confirmada, pero no se pudo identificar la reserva para enviar el correo.")

            return redirect('index')

    try:
        context = ReservationServices.get_seat_selection_context(flight_id)
    except ValueError as e:
        messages.error(request, str(e))
        return redirect('index')

    return render(request, 'reservations/select_seat.html', context)


@login_required
def my_reservations(request):
    user = request.user
    reservations = Reservation.objects.filter(passenger__user=user).order_by('-reservation_date')
    return render(request, 'reservations/my_reservations.html', {'reservations': reservations})


def reservation_list(request):
    reservations = ReservationServices.get_all_reservations()
    return render(request, 'reservations/list.html', {'reservations': reservations})


def reservation_detail(request, reservation_id):
    try:
        reservation = ReservationServices.get_reservation_by_id(reservation_id)
        return render(request, 'reservations/detail.html', {'reservation': reservation})
    except ValueError as e:
        messages.error(request, str(e))
        return redirect('reservation_list')


def reservation_create(request):
    passengers = ReservationServices.get_all_passengers()
    if request.method == "POST":

        passenger_id = request.POST.get("passenger_id")
        flight_id = request.POST.get("flight_id")
        seat_id = request.POST.get("seat_id")
        flight_number = request.POST.get("flight_number")
        status = request.POST.get("status")
        price = request.POST.get("price")
        reservation_code = request.POST.get("reservation_code")

        try:
            reservation = ReservationServices.create_reservation(
                passenger_id=passenger_id,
                flight_id=flight_id,
                seat_id=seat_id,
                flight_number=flight_number,
                status=status,
                price=price,
                reservation_code=reservation_code
            )
            try:
                ReservationServices.send_mail(reservation.id)
                messages.success(request, "Reserva creada y email enviado con éxito.")
            except Exception as e:
                messages.warning(request, f"Reserva creada, pero ocurrió un problema al enviar el correo: {e}")

        except ValueError as e:
            messages.error(request, str(e))
        return redirect('reservation_list')

    return render(request, 'reservations/create.html', {'passengers': passengers})


def reservation_update(request, reservation_id):
    try:
        reservation = ReservationServices.get_reservation_by_id(reservation_id)
    except ValueError as e:
        messages.error(request, str(e))
        return redirect('reservation_list')

    passengers = ReservationServices.get_all_passengers()
    if request.method == "POST":
        passenger_id = request.POST.get("passenger_id")
        flight_number = request.POST.get("flight_number")
        status = request.POST.get("status")
        try:
            ReservationServices.update_reservation(
                reservation_id=reservation_id,
                passenger_id=passenger_id,
                flight_number=flight_number,
                status=status
            )
            messages.success(request, "Reservation updated successfully.")
        except ValueError as e:
            messages.error(request, str(e))
        return redirect('reservation_list')
    return render(request, 'reservations/update.html', {'reservation': reservation, 'passengers': passengers})


def reservation_delete(request, reservation_id):
    try:
        reservation = ReservationServices.get_reservation_by_id(reservation_id)
    except ValueError as e:
        messages.error(request, str(e))
        return redirect('reservation_list')

    if request.method == "POST":
        try:
            ReservationServices.delete_reservation(reservation_id=reservation_id)
            messages.success(request, "Reservation deleted successfully.")
        except ValueError as e:
            messages.error(request, str(e))
        return redirect('reservation_list')
    return render(request, 'reservations/delete.html', {'reservation': reservation})


def download_passenger_excel(self, request):
    flight_ids = request.GET.get('flights')
    if not flight_ids:
        messages.error(request, "No se encontró el vuelo.")
        return redirect('..')

    flight_ids = [int(fid) for fid in flight_ids.split(',')]
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Pasajeros"
    ws.append(['Vuelo ID', 'Pasajero', 'Email', 'Documento', 'Teléfono', 'Asiento'])

    for fid in flight_ids:
        passengers = ReservationServices.reports_passagers_by_flights(fid)
        for p in passengers:
            ws.append([
                fid,
                p.pasajero,
                p.email,
                p.documento,
                p.telefono,
                p.asiento
            ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="reporte_pasajeros.xlsx"'
    wb.save(response)
    return response