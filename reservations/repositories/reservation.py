from reservations.models import Reservation



class  ReservationRepository:
    @staticmethod
    def get_all_reservations():
        return Reservation.objects.all()
    
    @staticmethod
    def get_reservation_by_id(reservation_id):
        return Reservation.objects.filter(id=reservation_id).first()
    
    @staticmethod
    def get_reservation_by_passanger(passanger_id):
        return Reservation.objects.filter(passanger_id=passanger_id)
     
    @staticmethod
    def create_reservation(
        passanger_id,
        flight_id,
        seat_id,
        flight_number,
        reservation_date,
        status,
        reservation_code,
        price,
        is_active=True
    ):
        
        new_reservation = Reservation.objects.create(
            passanger_id=passanger_id,
            flight_id=flight_id,
            seat_id=seat_id,
            flight_number=flight_number,
            reservation_date=reservation_date,
            status=status,
            reservation_code=reservation_code,
            price=price,
            is_active=is_active
        )
        
        return new_reservation
    
    @staticmethod
    def update_resevation(
        reservation_id,
        passanger,
        flight,
        seat,
        flight_number,
        reservation_date,
        status,
        reservation_code,
        price,
    ):
        
        reservation = Reservation.objects.filter(id=reservation_id).first()
        
        if not reservation:
            raise ValueError('Reserva no encontrada, intenalo nuevamente')
        
        reservation.passanger_id = passanger
        reservation.flight_id = flight
        reservation.seat_id = seat
        reservation.flight_number = flight_number
        reservation.reservation_date = reservation_date
        reservation.status = status
        reservation.reservation_code = reservation_code
        reservation.price = price
        
        reservation.save()
        
        return reservation
    
    @staticmethod
    def delete_reservation(reservation_id):
        reservation = Reservation.objects.filter(id=reservation_id).first()
        
        if not reservation:
            raise ValueError('Reserva no encontrada, intenalo nuevamente')
        
        if reservation.is_active:
            reservation.is_active = False
            
            reservation.save()
            
            return reservation
        
    