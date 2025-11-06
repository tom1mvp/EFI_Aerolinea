from rest_framework.exceptions import ValidationError


from reservations.repositories.reservation import ReservationRepository


class ReservationServices:
    @staticmethod
    def get_all_reservation():
        return ReservationRepository.get_all_reservations()
    
    @staticmethod
    def get_reservation_by_id(reservation_id):
        return ReservationRepository.get_reservation_by_id(reservation_id)
    
    @staticmethod
    def get_reservation_by_passanger(passanger_id):
        return ReservationRepository.get_reservation_by_passanger(passanger_id)
    
    @staticmethod
    def create_reservation(data, passanger_id, flight_id, seat_id):
        required_fields = [
            'flight_number',
            'reservation_date',
            'status',
            'reservation_code',
            'price'
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError(f'Falta el campo obligatorio: {field}')
            
            
        new_reservation = ReservationRepository.create_reservation(
            passanger_id=passanger_id,
            flight_id=flight_id,
            seat_id=seat_id,
            flight_number=data['flight_number'],
            reservation_date=data['reservation_date'],
            status=data['status'],
            reservation_code=data['reservation_code'],
            price=data['price']
        )
        
        return new_reservation
    
    @staticmethod
    def update_reservation(data, resevation_id, passanger_id, flight_id, seat_id):
        required_fields = [
            'flight_number',
            'reservation_date',
            'status',
            'reservation_code',
            'price'
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError(f'Falta el campo obligatorio: {field}')
            
        reservation = ReservationRepository.update_resevation(
            reservation_id=resevation_id,
            passanger=passanger_id,
            flight=flight_id,
            seat=seat_id,
            flight_number=data['flight_number'],
            reservation_date=data['reservation_date'],
            status=data['status'],
            reservation_code=data['reservation_code'],
            price=data['price']
        )
        
        return reservation
    
    @staticmethod
    def delete_reservation(reservation_id):
        return ReservationRepository.delete_reservation(reservation_id)