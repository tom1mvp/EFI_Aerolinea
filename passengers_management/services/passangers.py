from rest_framework.exceptions import ValidationError


from passengers_management.repositories.passengers import PassangerRepository


class PassangerService:
    @staticmethod
    def get_all_passangers():
        return PassangerRepository.get_all_passangers()
    
    @staticmethod
    def get_passanger_by_name(name):
        return PassangerRepository.get_passanger_by_name(name)
    
    @staticmethod
    def create_passanger(data, user_id):
        required_fields = [
            'check_in_status',
            'passenger_type',
            'nationality'
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError(f'Falta el campo obligatorio: {field}')
            
        new_passanger = PassangerRepository.create_passanger(
            user_id=user_id,
            check_in_status=data['check_in_status'],
            passenger_type=data['passenger_type'],
            nationality=data['nationality']
        )
        
        return new_passanger
    
    @staticmethod
    def update_passanger(data, passanger_id, user):
        required_fields = [
            'check_in_status',
            'passenger_type',
            'nationality'
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError(f'Falta el campo obligatorio: {field}')
            
        passanger = PassangerRepository.update_passanger(
            passanger_id=passanger_id,
            user=user,
            check_in_status=data['check_in_status'],
            passenger_type=data['passenger_type'],
            nationality=data['nationality']
        )
        
        return passanger
    
    @staticmethod
    def delete_passanger(passanger_id):
        return PassangerRepository.delete_passanger(passanger_id)