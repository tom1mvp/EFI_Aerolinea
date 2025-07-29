from django.contrib import admin
<<<<<<< HEAD
import openpyxl
from django.http import HttpResponse
=======
>>>>>>> 31342434b0d2f48ad6df9142d7a9ad4d47f481c2

from flights_management.models import Flight
from flights_management.services.flights import FlightsServices
from reservations.models import Reservation

<<<<<<< HEAD
@admin.action(description="Reporte de pasajeros por vuelo/s")
def exportar_pasajeros_excel(modeladmin, request, queryset):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Pasajeros por vuelo"
    ws.append(['Vuelo', 'Origen', 'Destino', 'Fecha salida', 'Pasajero', 'Email', 'Documento', 'Teléfono', 'Asiento'])

    for flight in queryset:
        reservations = Reservation.objects.filter(flight=flight).select_related('passenger__user', 'seat')
        for reservation in reservations:
            passenger = reservation.passenger
            user = passenger.user
            ws.append([
                str(flight.id),
                flight.origin,
                flight.destination,
                str(flight.departure_date),
                f"{user.first_name} {user.last_name}",
                user.email,
                passenger.document,
                passenger.phone_number,
                str(reservation.seat)
            ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=pasajeros_por_vuelo.xlsx'
    wb.save(response)
    return response
=======

>>>>>>> 31342434b0d2f48ad6df9142d7a9ad4d47f481c2
@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'airplane', 'origin', 'destination',
        'departure_date', 'arrival_date', 'duration',
        'status', 'base_price'
    )
    list_filter = ('departure_date', 'destination', 'status')
    search_fields = ('origin', 'destination')
    actions = [exportar_pasajeros_excel] 

    def save_model(self, request, obj, form, change):
        if not change:
            FlightsServices.create_flights(
                airplane_id=obj.airplane.id,
                origin=obj.origin,
                destination=obj.destination,
                departure_date=obj.departure_date,
                arrival_date=obj.arrival_date,
                duration=obj.duration,
                status=obj.status,
                base_price=obj.base_price
            )
        else:
            FlightsServices.update_flights(
                flight_id=obj.id,
                airplane_id=obj.airplane.id,
                origin=obj.origin,
                destination=obj.destination,
                departure_date=obj.departure_date,
                arrival_date=obj.arrival_date,
                duration=obj.duration,
                status=obj.status,
                base_price=obj.base_price
            )

    def delete_model(self, request, obj):
        FlightsServices.delete_flight(obj.id)

