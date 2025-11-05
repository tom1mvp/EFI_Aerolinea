from flights_management.models import Flight


class FlightRepository:
    # Mehtod GET (all, id, origin, destiny, date)
    @staticmethod
    def get_all_flights():
        return Flight.objects.all()
    
    @staticmethod
    def get_by_id(flight_id):
        return Flight.objects.filter(id=flight_id).first()
    
    @staticmethod
    def get_flight_by_origin(origin):
        return Flight.objects.filter(origin=origin).first()
    
    @staticmethod
    def get_flight_by_destination(destination):
        return Flight.objects.filter(destination=destination).first()
    
    @staticmethod
    def get_flight_by_arrival_date(arrival_date):
        return Flight.objects.filter(arrival_date=arrival_date).first()
    
    # Mehtod POST (create)
    @staticmethod
    def create_flight(
        airplane_id,
        origin,
        destination,
        departure_date,
        arrival_date,
        duration,
        status,
        base_price,
        is_active=True
    ):
        
        new_flight = Flight.objects.create(
            airplane_id=airplane_id,
            origin=origin,
            destination=destination,
            departure_date=departure_date,
            arrival_date=arrival_date,
            duration=duration,
            status=status,
            base_price=base_price,
            is_active=is_active
        )
        
        return new_flight
    
    # Method PUT (update)
    @staticmethod
    def update_flight(
        flight_id,
        airplane,
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
        
        flight.airplane_id = airplane
        flight.origin = origin
        flight.destination = destination
        flight.departure_date = departure_date
        flight.arrival_date = arrival_date
        flight.duration = duration
        flight.status = status
        flight.base_price = base_price
        
        flight.save()
        
        return flight
    
    # Method DELETE (soft)
    @staticmethod
    def delete_flight(flight_id):
        flight = Flight.objects.filter(id=flight_id).first()
        
        if not flight:
            raise ValueError('No se encontró el vuelo específico.')
        
        if flight.is_active:
            flight.is_active = False
            
            flight.save()
            
            return flight