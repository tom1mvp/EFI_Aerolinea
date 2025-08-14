import openpyxl
import mailtrap as mt

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from reservations.models import Reservation
from reservations.services.reservations import ReservationServices
from django.conf import settings

client = mt.MailtrapClient(token=settings.MAILTRAP_API_KEY)

def send_example_email(request):
    try:
        mail = mt.Mail(
            sender=mt.Address(email="from@your_mailtrap_domain", name="Mailtrap Test"),
            to=[mt.Address(email="your@email.com")],
            subject="You are awesome!",
            text="Congrats for sending test email with Mailtrap!",
        )
        client.send(mail)

        return HttpResponse(f'Email sent successfully!')
    except Exception as e:
        return HttpResponse(f'Failed to send email: {str(e)}')

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
        if result["success"]:
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
            # Send mail
            ReservationServices.send_mail(reservation.id)
            messages.success(request, "Reserva creada y email enviado con éxito.")
        
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
            ReservationServices.update_reservation(reservation_id=reservation_id, passenger_id=passenger_id, flight_number=flight_number, status=status)
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

    # Esta es la única forma segura y correcta de generar descarga en Django
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="reporte_pasajeros.xlsx"'
    wb.save(response)
    return response