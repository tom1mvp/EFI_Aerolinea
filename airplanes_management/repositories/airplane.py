from airplanes_management.models import Airplane


class AirplaneRepository:
    # Method GET (all, by id, by status, by capacity)
    @staticmethod
    def get_all_airplanes():
        return Airplane.objects.all()
    
    @staticmethod
    def get_ariplane_by_id(airplane_id):
        return Airplane.objects.filter(id=airplane_id).first()
    
    @staticmethod
    def get_airplane_by_status(status):
        return Airplane.objects.filter(status=status).first()
    
    @staticmethod
    def get_airplane_by_capacity(capacity):
        return Airplane.objects.filter(capacity=capacity).first()
    
    # Method POST (create airplane)
    @staticmethod
    def create_airplane(name, capacity, rows, columns, status):
        new_airplane = Airplane.objects.create(
            name=name, 
            capacity=capacity, 
            rows=rows, 
            columns=columns,
            status=status, 
        )
        
        new_airplane.save()
        
        return new_airplane
    
    # Method PUT (update airplane)
    @staticmethod
    def update_airplane(airplane_id, name, capacity, rows, columns, status):
        
        airplane = Airplane.objects.filter(id=airplane_id).first()
        
        if not airplane:
          raise ValueError('El avion no existe')

        airplane.name = name
        airplane.capacity = capacity
        airplane.rows = rows
        airplane.columns = columns
        airplane.status = status
        
        return airplane
    
    # Method DELETE (soft)
    @staticmethod
    def delete_airplane(airplane_id):
        
        airplane = Airplane.objects.filter(id=airplane_id).first()
        
        if not airplane:
          raise ValueError('El avion no existe')
      
        if airplane.is_active:
            airplane.is_active = False
            
            airplane.save()
            
            return airplane