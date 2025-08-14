from flights_management.models import Flight
from airplanes_management.models import Airplane

class FlightsRepository:
    # GET
    @staticmethod
    def get_all_flights():
        return Flight.objects.all()
    
    @staticmethod
    def get_by_id(flight_id):
        return Flight.objects.filter(id=flight_id).first()
    
    @staticmethod
    def get_by_duration(duration):
        return Flight.objects.filter(duration=duration).first()
    
    @staticmethod
    def get_by_destination(destination):
        return Flight.objects.filter(destination__icontains=destination)
    
    # CREATE
    @staticmethod
    def create_flight(
        airplane,  # recibe objeto Airplane
        origin,
        destination,
        departure_date,
        arrival_date,
        duration,
        status,
        base_price
    ):
        new_flight = Flight.objects.create(
            airplane=airplane,
            origin=origin,
            destination=destination,
            departure_date=departure_date,
            arrival_date=arrival_date,
            duration=duration,
            status=status,
            base_price=base_price
        )
        return new_flight
    
    # UPDATE
    @staticmethod
    def update_flight(
        flight_id,
        airplane,  # recibe objeto Airplane
        origin,
        destination,
        departure_date,
        arrival_date,
        duration,
        status,
        base_price
    ):
        flight = Flight.objects.filter(id=flight_id).first()
        if not flight:
            raise ValueError('No se encontró el vuelo específico.')
        
        flight.airplane = airplane
        flight.origin = origin
        flight.destination = destination
        flight.departure_date = departure_date
        flight.arrival_date = arrival_date
        flight.duration = duration
        flight.status = status
        flight.base_price = base_price
        
        flight.save()
        return flight
    
    # DELETE
    @staticmethod
    def delete_flight(flight_id):
        flight = Flight.objects.filter(id=flight_id).first()
        if not flight:
            raise ValueError('No se encontró el vuelo específico.')
        flight.delete()
        
        