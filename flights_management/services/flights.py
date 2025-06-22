from flights_management.repositories.flights import FlightsRepository
from airplanes_management.repositories.airplaine import AirplaneRepository

class FlightsServices:
    # GET
    @staticmethod
    def get_all_flights():
        return FlightsRepository.get_all_flights()
    
    @staticmethod
    def get_by_destination(destination):
        return FlightsRepository.get_by_destination(destination=destination)
    
    @staticmethod
    def get_by_duration(duration):
        return FlightsRepository.get_by_duration(duration=duration)
    
    # CREATE
    @staticmethod
    def create_flights(
        airplane_id,
        origin,
        destination,
        departure_date,
        arrival_date,
        duration,
        status,
        base_price
    ):
        airplane = AirplaneRepository.get_airplane_by_id(airplane_id=airplane_id)
        if not airplane:
            raise ValueError('El avión no existe')
        
        new_flight = FlightsRepository.create_flight(
            airplane=airplane,  # pasa el objeto Airplane
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
    def update_flights(
        flight_id,
        airplane_id,
        origin,
        destination,
        departure_date,
        arrival_date,
        duration,
        status,
        base_price
    ):
        flight = FlightsRepository.get_by_id(flight_id=flight_id)
        airplane = AirplaneRepository.get_airplane_by_id(airplane_id=airplane_id)
        if not flight:
            raise ValueError('El vuelo no existe.')
        if not airplane:
            raise ValueError('El avión no existe.')
        
        updated_flight = FlightsRepository.update_flight(
            flight_id=flight_id,
            airplane=airplane,  # pasa el objeto Airplane
            origin=origin,
            destination=destination,
            departure_date=departure_date,
            arrival_date=arrival_date,
            duration=duration,
            status=status,
            base_price=base_price
        )
        return updated_flight
    
    # DELETE
    @staticmethod
    def delete_flight(flight_id):
        flight = FlightsRepository.get_by_id(flight_id=flight_id)
        if not flight:
            raise ValueError('El vuelo no existe.')
        FlightsRepository.delete_flight(flight_id=flight_id)
        return True
