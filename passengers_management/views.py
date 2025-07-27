from django.shortcuts import render, redirect
from django.contrib import messages


from passengers_management.services.passengers import PassengerServices

def passenger_list(request):
    passengers = PassengerServices.get_all_passengers()
    return render(request, 'passengers/list.html', {'passengers': passengers})

def passenger_detail(request, passenger_id):
    try:
        passenger = PassengerServices.get_passenger_by_id(passenger_id)
        return render(request, 'passengers/detail.html', {'passenger': passenger})
    except ValueError as e:
        messages.error(request, str(e))
        return redirect('passenger_list')

def passenger_create(request):
    users = PassengerServices.get_all_users()
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        phone_number = request.POST.get("phone_number")
        try:
            PassengerServices.create_passenger(user_id=user_id, phone_number=phone_number)
            messages.success(request, "Passenger created successfully.")
        except ValueError as e:
            messages.error(request, str(e))
        return redirect('passenger_list')
    return render(request, 'passengers/create.html', {'users': users})

def passenger_update(request, passenger_id):
    try:
        passenger = PassengerServices.get_passenger_by_id(passenger_id)
    except ValueError as e:
        messages.error(request, str(e))
        return redirect('passenger_list')

    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        try:
            PassengerServices.update_passenger(passenger_id=passenger_id, phone_number=phone_number)
            messages.success(request, "Passenger updated successfully.")
        except ValueError as e:
            messages.error(request, str(e))
        return redirect('passenger_list')
    return render(request, 'passengers/update.html', {'passenger': passenger})

def passenger_delete(request, passenger_id):
    try:
        passenger = PassengerServices.get_passenger_by_id(passenger_id)
    except ValueError as e:
        messages.error(request, str(e))
        return redirect('passenger_list')

    if request.method == "POST":
        try:
            PassengerServices.delete_passenger(passenger_id=passenger_id)
            messages.success(request, "Passenger deleted successfully.")
        except ValueError as e:
            messages.error(request, str(e))
        return redirect('passenger_list')
    return render(request, 'passengers/delete.html', {'passenger': passenger})
