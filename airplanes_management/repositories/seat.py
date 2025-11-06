from airplanes_management.models import Seat, Airplane

from flights_management.models import Flight


class SeatRepository:
    # Method GET (all, by id, by status, by type)
    @staticmethod
    def get_all_seat():
        return Seat.objects.all()
    
    @staticmethod
    def get_seat_by_id(seat_id):
        return Seat.objects.filter(id=seat_id).first()
    
    @staticmethod
    def get_seat_by_status(status):
        return Seat.objects.filter(status=status).first()
    
    @staticmethod
    def verify_availability_by_flight(flight_id):
        try:
            flight = Flight.objects.get(id=flight_id)
            airplane_id = flight.airplane_id
            
        except Flight.DoesNotExist:
            raise ValueError(f"No se encontró un Vuelo con ID: {flight_id}")
            
        available_seats = Seat.objects.filter(
            airplane_id=airplane_id,
            status='disponible'
        ).order_by('rows', 'columns')
        
        return available_seats
    
    @staticmethod
    def is_seat_available_for_flight(seat_id, flight_id):
        try:
            flight = Flight.objects.get(id=flight_id)
            
            seat = Seat.objects.filter(
                id=seat_id,
                airplane=flight.airplane,
                status='disponible'
            ).first()
            
            return seat is not None
            
        except Flight.DoesNotExist:
            raise ValueError(f"No se encontró un Vuelo con ID: {flight_id}")
    
    @staticmethod
    def get_seat_by_type_seat(type_seat):
        return Seat.objects.filter(type_seat=type_seat).first()
    
    """
        # Method POST (create seat)
        @staticmethod
        def create_seat(airplane_id, number, rows, columns, type_seat, status, is_active=True):
        
            airplane = Airplane.objects.filter(id=airplane_id).first()
        
            if not airplane:
                raise ValueError('No se pudo obtener el ID del avion')
        
            new_seat = Seat.objects.create(
                airplane_id=airplane_id,
                number=number,
                rows=rows,
                columns=columns,
                type_seat=type_seat,
                status=status,
                is_active=is_active
            )
        
            return new_seat
        """
    
    # Method PUT (update seat)
    @staticmethod
    def update_seat(seat_id, airplane_id, type_seat, status):
        airplane = Airplane.objects.filter(id=airplane_id).first()
        
        if not airplane:
            raise ValueError('No se pudo obtener el ID del avion')
        
        seat = Seat.objects.filter(id=seat_id).first()
        
        if not seat:
            raise ValueError('No se pudo obtener el ID del asiento')
        
        seat.airplane=airplane
        seat.type_seat=type_seat
        seat.status=status
        
        seat.save()
        
        return seat
    
    """
    # Method DELETE (soft)
    @staticmethod
    def delete_seat(seat_id):
        seat = Seat.objects.filter(id=seat_id).first()
        
        if not seat:
            raise ValueError('No se pudo obtener el ID del asiento')
        
        if seat.is_active:
            seat.is_active = False
            
            seat.save()
            
            return seat
    """
        