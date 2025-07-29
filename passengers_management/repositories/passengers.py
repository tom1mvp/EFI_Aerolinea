from passengers_management.models import Passenger
from user.models import User
from reservations.models import Reservation


class PassengerRepository:
    @staticmethod
    def get_all_passengers():
        return Passenger.objects.all()

    @staticmethod
    def get_by_id(passenger_id):
        return Passenger.objects.filter(id=passenger_id).first()
    
    @staticmethod
    def get_flight_history(passenger_id):
        return Reservation.objects.filter(passenger_id=passenger_id).select_related('flight', 'seat')

    @staticmethod
    def create_passenger(user_id, phone_number, document):
       user = User.objects.filter(id=user_id).first()
       
       if not user:
           raise ValueError('El usuario no existe')
     
       new_passenger = Passenger.objects.create(
            user=user,
            document=document,
            phone_number=phone_number
        )
       
       return new_passenger
       

    @staticmethod
    def update_passenger(passenger_id, user_id, document, phone_number):
        passenger = Passenger.objects.filter(id=passenger_id).first()
        
        user = User.objects.filter(id=user_id).first()
        
        if not passenger:
            raise ValueError('El pasajero no existe')
        
        if not user:
           raise ValueError('El usuario no existe')
        
        passenger.user=user
        passenger.phone_number=phone_number
        passenger.document=document
        
        passenger.save()
        
        return passenger

    @staticmethod
    def delete_passenger(passenger_id):
        passenger = Passenger.objects.filter(id=passenger_id).first()
        
        if passenger:
            passenger.delete()
        return False
        
        
        