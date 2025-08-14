from django.views import View
from django.shortcuts import render


from flights_management.services.flights import FlightsServices

class FlightManagementView(View):
    def get(self, request):
        flights = FlightsServices.get_all_flights()
        return render(request, 'index.html', {'flights': flights})
