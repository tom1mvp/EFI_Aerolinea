from rest_framework.exceptions import ValidationError


from reporting.repositories.reporting import ReportingRepository


class ReportingServices:
    @staticmethod
    def get_passengers_by_flight(flight_id):
        return ReportingRepository.get_passengers_by_flight(flight_id)
    
    @staticmethod
    def get_reservation_by_passenger(passanger_id):
        return ReportingRepository.get_reservation_by_passenger(passanger_id)