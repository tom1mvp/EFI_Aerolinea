from django.shortcuts import render, redirect
from django.contrib import messages
from reservations.services.reservation import ReservationServices

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
        flight_number = request.POST.get("flight_number")
        try:
            ReservationServices.create_reservation(passenger_id=passenger_id, flight_number=flight_number)
            messages.success(request, "Reservation created successfully.")
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
