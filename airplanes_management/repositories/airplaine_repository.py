from airplanes_management.models import Airplane, Seat
from airplanes_management.service.airplane_service import AirplaneService

class AirplaneRepository:
    # Method GET
    @staticmethod
    def get_all_airplanes() -> list[Airplane]:
        return Airplane.objects.all()
    
    @staticmethod
    def get_airplane_by_id(airplane_id: int) -> Airplane:
        try:
            return Airplane.objects.get(id=airplane_id)
        except Airplane.DoesNotExist:
            return None
        
    @staticmethod
    def get_airplane_by_name(name: str) -> Airplane:
        return Airplane.objects.filter(name__icontains=name)

    # Method POST
    @staticmethod
    def create_airplane(form):
        airplane = form.save()
        AirplaneService.generate_seat(airplane)
        return airplane

    # Method PUT
    @staticmethod
    def update_airplane(
        airplane: Airplane,
        name: str = None,
        capacity: int = None,
        state: str = None
    ) -> Airplane:
        if name is not None:
            airplane.name = name
        if capacity is not None:
            airplane.capacity = capacity
        if state is not None:
            airplane.state = state
        airplane.save()
        return airplane
    
    # Mehtod DELETE
    @staticmethod
    def delete_airplane(airplane: Airplane) -> bool:
        try:
            airplane.delete()
            return True
        except Airplane.DoesNotExist:
            raise ValueError("EL avión no existe o ya ha sido eliminado.")
        
    # Seat
    
    # Method GET
    @staticmethod
    def get_all_seat():
        return Seat.objects.all()
    @staticmethod
    def get_by_airplane(airplane_id):
        airplane = Airplane.objects.filter(id=airplane_id).first()
        
        if airplane is None:
            raise ValueError("El avion no exite")

        return Seat.objects.filter(airplane=airplane)
    
    @staticmethod
    def get_by_tipe(tipe: str):
        return Seat.objects.filter(tipe=tipe).first()
        
    # Method POST
    @staticmethod
    def create_seat(airplane, number, rows, columns, tipe, state):
        return Seat.objects.create(
            airplane=airplane,
            number=number,
            rows=rows,
            columns=columns,
            tipe=tipe,
            state=state
        )
    
    # Method PUT
    @staticmethod
    def update_seat(seat_id, airplane_id, number, rows, columns, tipe, state):
        seat = Seat.objects.filter(id=seat_id).first()
        
        airplane = Airplane.objects.filter(id=airplane_id)
        
        if seat is None:
            raise ValueError("El asiento no existe")
        
        if airplane is None:
            raise ValueError("El avion no existe")
        
        seat.airplane=airplane_id
        seat.number=number
        seat.rows=rows
        seat.columns=columns
        seat.tipe=tipe
        seat.state=state
        
        seat.save()
            
        return seat
    
    # Method DELETE
    def delete_seat(seat_id):
        seat = Seat.objects.filter(id=seat_id).first()
        
        if seat is None:
            raise ValueError("El asiento no existe")
        
        try:
            seat.delete()
            return True
        except Seat.DoesNotExist:
            raise ValueError("El seat no existe o ya ha sido eliminado.")