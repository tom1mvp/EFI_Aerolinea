from django.shortcuts import render, redirect
from .forms import AirplaneForm
from .service.airplane_service import AirplaneService

def create_airplane(request):
    if request.method == 'POST':
        form = AirplaneForm(request.POST)
        if form.is_valid():
            AirplaneService.create_airplane(form)  # Usa el servicio, no el modelo directo
            return redirect('airplane_list')
    else:
        form = AirplaneForm()
    return render(request, 'airplanes_management/create_airplane.html', {'form': form})