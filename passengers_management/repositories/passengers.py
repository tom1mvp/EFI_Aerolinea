from passengers_management.models import Passanger


class PassangerRepository:
    @staticmethod
    def get_all_passangers():
        return Passanger.objects.all()
    
    @staticmethod
    def get_passanger_by_name(name):
        return Passanger.objects.filter(user__name__icontains=name)
    
    @staticmethod
    def create_passanger(
        user_id,
        check_in_status,
        passenger_type,
        nationality,
        is_active= True
    ):
        new_passanger = Passanger.objects.create(
            user_id=user_id,
            check_in_status=check_in_status,
            passenger_type=passenger_type,
            nationality=nationality,
            is_active=is_active
        )
        
        return new_passanger
    
    @staticmethod
    def update_passanger(
        passanger_id,
        user,
        check_in_status,
        passenger_type,
        nationality,
    ):
        pasanger = Passanger.objects.filter(id=passanger_id).first()
        
        if not pasanger:
            raise ValueError('No se encontró el pasajero específico.')
        
        pasanger.user_id = user
        pasanger.check_in_status = check_in_status
        pasanger.passenger_type = passenger_type
        pasanger.nationality = nationality
        
        pasanger.save()
        
        return pasanger
    
    @staticmethod
    def delete_passanger(passanger_id):
        pasanger = Passanger.objects.filter(id=passanger_id).first()
        
        if not pasanger:
            raise ValueError('No se encontró el pasajero específico.')
        
        if pasanger.is_active:
            pasanger.is_active = False
            
            pasanger.save()
            
            return pasanger
                          