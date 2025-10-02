from rest_framework.exceptions import ValidationError


from airplanes_management.repositories.airplane import AirplaneRepository


class AirplaneService:
    # Method GET (all, by id, by status, by capacity)
    @staticmethod
    def get_all_airplane():
        return AirplaneRepository.get_all_airplanes()
    
    @staticmethod
    def get_airplane_by_id(airplane_id):
        return AirplaneRepository.get_ariplane_by_id(airplane_id)
    
    @staticmethod
    def get_airplane_by_status(status):
        return AirplaneRepository.get_airplane_by_status(status)
    
    @staticmethod
    def get_airplane_by_capacity(capacity):
        return AirplaneRepository.get_airplane_by_capacity(capacity)
    
    # Method POST (create airplane)
    @staticmethod
    def create_airplane(data):
        required_fields = ['name', 'capacity', 'rows', 'columns', 'status']
        
        for field in required_fields:
            if field not in data:
                raise ValidationError(f'Falta el campo obligatorio: {field}')
            
        new_airplane = AirplaneRepository.create_airplane(
            name = data['name'],
            capacity = data['capacity'],
            rows = data['rows'],
            columns = data['columns'],
            status = data['status']
        )
        
        return new_airplane
    
    # Method PUT (update airplane)
    @staticmethod
    def update_airplane(data, airplane_id):
        required_fields = ['name', 'capacity', 'rows', 'columns', 'status']
    
        for field in required_fields:
            if field not in data:
                raise ValidationError(f'Falta el campo obligatorio: {field}')
            
        airplane = AirplaneRepository.update_airplane(
            airplane_id=airplane_id,
            name=data['name'],
            capacity=data['capacity'],
            rows=data['rows'],
            columns=data['columns'],
            status=data['status']
        )
    
        return airplane

    
    # Method DELETE (soft)
    @staticmethod
    def delete_airplane(airplane_id):
        return AirplaneRepository.delete_airplane(airplane_id)