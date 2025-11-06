from reservations.models import Reservation
from passengers_management.models import Passanger


class ReportingRepository:
    @staticmethod
    def get_passengers_by_flight(flight_id):
        return Passanger.objects.filter(reservations__flight_id=flight_id).first()
    
    @staticmethod
    def get_reservation_by_passenger(passanger_id):
        return Reservation.objects.filter(passanger_id=passanger_id, is_active=True).first()
    
    