from passengers_management.repositories.passenger import PassengerRepository
from user.repositories.user import UserRepository

class PassengerServices:
    @staticmethod
    def create_passenger(user_id, phone_number):
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found.")
        return PassengerRepository.create_passenger(user=user, phone_number=phone_number)

    @staticmethod
    def update_passenger(passenger_id, phone_number):
        passenger = PassengerRepository.get_by_id(passenger_id)
        if not passenger:
            raise ValueError("Passenger not found.")
        return PassengerRepository.update_passenger(passenger=passenger, phone_number=phone_number)

    @staticmethod
    def delete_passenger(passenger_id):
        passenger = PassengerRepository.get_by_id(passenger_id)
        if not passenger:
            raise ValueError("Passenger not found.")
        return PassengerRepository.delete_passenger(passenger=passenger)
