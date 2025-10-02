from rest_framework.exceptions import ValidationError


from airplanes_management.repositories.airplane import AirplaneRepository
from airplanes_management.repositories.seat import SeatRepository


class SeatServices:
    # Method GET (all, by id, by status, by type)
    @staticmethod
    def get_all_seat():
        return SeatRepository.get_all_seat()
    
    @staticmethod
    def get_seat_by_id(seat_id):
        return SeatRepository.get_seat_by_id(seat_id)
    
    @staticmethod
    def get_seat_by_status(status):
        return SeatRepository.get_seat_by_status(status)
    
    @staticmethod
    def get_seat_by_type_seat(type_seat):
        return SeatRepository.get_seat_by_type_seat(type_seat)
   
    """
    # Method POST (create seat)
    @staticmethod
    def create_seat(data, airplane_id):
        required_fields = ['number', 'rows', 'columns', 'type_seat', 'status']
        
        for field in required_fields:
            if field not in data:
                raise ValidationError(f'Falta el campo obligatorio: {field}')
            
        new_seat = SeatRepository.create_seat(
            airplane_id=airplane_id,
            number=data['number'],
            rows=data['rows'],
            columns=data['columns'],
            type_seat=data['type_seat'],
            status=data['status']
        )
        
        return new_seat
   """
    
    
    # Method PUT (update seat)
    @staticmethod
    def update_seat(data, airplane_id, seat_id):
        required_fields = ['type_seat', 'status']
        
        for field in required_fields:
            if field not in data:
                raise ValidationError(f'Falta el campo obligatorio: {field}')
            
        seat = SeatRepository.update_seat(
            airplane_id=airplane_id,
            seat_id=seat_id,
            type_seat=data['type_seat'],
            status=data['status']
        )
        
        return seat
    
    # Method DELETE (soft)
    @staticmethod
    def delete_seat(seat_id):
        return SeatRepository.delete_seat(seat_id)