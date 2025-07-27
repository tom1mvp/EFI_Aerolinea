from django.contrib import admin

from flights_management.models import Flight
from flights_management.services.flights import FlightsServices


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'airplane', 'origin', 'destination',
        'departure_date', 'arrival_date', 'duration',
        'status', 'base_price'
    )
    list_filter = ('departure_date', 'destination', 'status')
    search_fields = ('origin', 'destination')

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

