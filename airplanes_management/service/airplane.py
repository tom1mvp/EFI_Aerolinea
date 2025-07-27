from airplanes_management.repositories.airplaine import AirplaneRepository

class AirplaneService:
    
    @staticmethod
    def get_all_airplanes():
        return AirplaneRepository.get_all_airplanes()

    @staticmethod
    def get_airplane_by_id(airplane_id):
        return AirplaneRepository.get_airplane_by_id(airplane_id)

    @staticmethod
    def get_airplane_by_name(name):
        return AirplaneRepository.get_airplane_by_name(name)
    
    @staticmethod
    def create_airplane(form):
        airplane = form.save()
        AirplaneService.generate_seat(airplane)
        return airplane
    
    @staticmethod
    def update_airplane(airplane, form):
        return AirplaneRepository.update_airplane(airplane, form)
        
    @staticmethod
    def delete_airplane(airplane):
        return AirplaneRepository.delete_airplane(airplane)


    """
    @staticmethod
    def generate_seat(airplane):
        for row in range(1, airplane.rows + 1):
            for column in range(1, airplane.columns + 1):
                number = f"{chr(64 + column)}{row}"
                airplane_repository.create_seat(
                    airplane=airplane,
                    number=number,
                    rows=row,
                    columns=column,
                    tipe="economico",  # minúscula para coincidir con el modelo
                    state='disponible'
                )
    """        