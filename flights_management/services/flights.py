from rest_framework.exceptions import ValidationError


from flights_management.repositories.flights import FlightRepository


class FlightService:
    # Mehtod GET (all, id, origin, destiny, date)
    @staticmethod
    def get_all_flights():
        return FlightRepository.get_all_flights()
    
    @staticmethod
    def get_by_id_flight(flight_id):
        return FlightRepository.get_by_id(flight_id)
    
    @staticmethod
    def get_flight_by_origin(origin):
        return FlightRepository.get_flight_by_origin(origin)
    
    @staticmethod
    def get_flight_by_destination(destination):
        return FlightRepository.get_flight_by_destination(destination)
    
    @staticmethod
    def get_flight_by_arrival_date(arrival_date):
        return FlightRepository.get_flight_by_arrival_date(arrival_date)
    
    # Method POST (create)
    @staticmethod
    def create_flight(data, airplane_id):
        required_fields = [
            'origin',
            'destination',
            'departure_date',
            'arrival_date',
            'duration',
            'status',
           'base_price'
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError(f'Falta el campo obligatorio: {field}')
            
        new_flight = FlightRepository.create_flight(
            airplane_id=airplane_id,
            origin=data['origin'],
            destination=data['destination'],
            departure_date=data['departure_date'],
            arrival_date=data['arrival_date'],
            duration=data['duration'],
            status=data['status'],
            base_price=data['base_price']
        )
        
        return new_flight
    
    # Method PUT (update)
    @staticmethod
    def updateflight(data, airplane, flight_id):
        required_fields = [
            'origin',
            'destination',
            'departure_date',
            'arrival_date',
            'duration',
            'status',
           'base_price'
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError(f'Falta el campo obligatorio: {field}')
            
        flight = FlightRepository.update_flight(
            flight_id=flight_id,
            airplane=airplane,
            origin=data['origin'],
            destination=data['destination'],
            departure_date=data['departure_date'],
            arrival_date=data['arrival_date'],
            duration=data['duration'],
            status=data['status'],
            base_price=data['base_price']
        )
        
        
        return flight
    
    # Method DELETE (soft)
    @staticmethod
    def delete_flight(flight_id):
        return FlightRepository.delete_flight(flight_id)