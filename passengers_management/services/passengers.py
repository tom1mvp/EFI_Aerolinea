from passengers_management.repositories.passengers import PassengerRepository

from user.repositories.user import UserRepository

class PassengerServices:
    @staticmethod
    def get_all_passenger():
        return PassengerRepository.get_all_passengers()
    
    @staticmethod
    def get_by_id(passenger_id):
        return PassengerRepository.get_by_id(passenger_id)
    
    @staticmethod
    def history_flights(passenger_id):
        return PassengerRepository.get_flight_history(passenger_id=passenger_id)
    
    @staticmethod
    def create_passenger(user_id, phone_number, document):
        user = UserRepository.get_by_id(user_id=user_id)
        
        if not user:
            raise ValueError('EL usuario no está disponible')
        
        new_passenger = PassengerRepository.create_passenger(
            user_id=user.id,  # CORREGIDO: pasar solo el id
            phone_number=phone_number,
            document=document
        )
        
        return new_passenger
    
    @staticmethod
    def update_passenger(passenger_id, user_id, phone_number, document):
        passenger = PassengerRepository.get_by_id(passenger_id=passenger_id)
        user = UserRepository.get_by_id(user_id=user_id)
        
        if not passenger:
            raise ValueError('EL pasajero no está disponible')
        
        if not user:
            raise ValueError('EL usuario no está disponible')
        
        update_passager = PassengerRepository.update_passenger(
            passenger_id=passenger.id,
            user_id=user.id,
            document=document,
            phone_number=phone_number
        )
        
        return update_passager
    
    @staticmethod
    def delete_passenger(passenger_id):
        passenger = PassengerRepository.get_by_id(passenger_id=passenger_id)
        
        if passenger:
            PassengerRepository.delete_passenger(passenger_id=passenger.id)  # CORREGIDO
            return True
        return False
