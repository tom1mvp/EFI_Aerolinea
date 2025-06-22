from airplanes_management.models import Airplane, Seat


class AirplaneRepository:
    # Method GET
    @staticmethod
    def get_all_airplanes():
        return Airplane.objects.all()
    
    @staticmethod
    def get_airplane_by_id(airplane_id):
        try:
            return Airplane.objects.get(id=airplane_id)
        except Airplane.DoesNotExist:
            return None
        
    @staticmethod
    def get_airplane_by_name(name):
        return Airplane.objects.filter(name__icontains=name)

    # Method POST
    @staticmethod
    def create_airplane(name, capacity, row, column, state):
        new_airplane = Airplane.objects.create(
            name=name,
            capacity=capacity,
            row=row,
            column=column,
            state=state
        )
        
        return new_airplane

    # Method PUT
    @staticmethod
    def update_airplane(
        airplane_id,
        name,
        capacity,
        row,
        column,
        state
    ):
      airplane = Airplane.objects.filter(id=airplane_id).first()
      
      if not airplane:
          raise ValueError('El avion no existe')
    
    # Mehtod DELETE
    @staticmethod
    def delete_airplane(airplane):
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
    
    def get_seat_by_id(seat_id):
        return Seat.objects.filter(id=seat_id).first()
    
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