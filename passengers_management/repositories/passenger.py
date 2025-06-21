from passengers_management.models import Passenger

class PassengerRepository:
    @staticmethod
    def get_all_passengers():
        return Passenger.objects.all()

    @staticmethod
    def get_by_id(passenger_id):
        return Passenger.objects.filter(id=passenger_id).first()

    @staticmethod
    def create_passenger(user, phone_number):
        return Passenger.objects.create(user=user, phone_number=phone_number)

    @staticmethod
    def update_passenger(passenger, phone_number):
        passenger.phone_number = phone_number
        passenger.save()
        return passenger

    @staticmethod
    def delete_passenger(passenger):
        passenger.delete()
