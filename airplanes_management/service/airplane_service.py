from ..repositories import airplane_repository

class AirplaneService:
    @staticmethod
    def create_airplane(form):
        airplane = form.save()
        AirplaneService.generate_seat(airplane)
        return airplane
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
        
    @staticmethod
    def delete_airplane(airplane):
        return airplane_repository.delete_airplane(airplane)

    @staticmethod
    def update_airplane(airplane, form):
        return airplane_repository.update_airplane(airplane, form)

    @staticmethod
    def get_all_airplanes():
        return airplane_repository.get_all_airplanes()

    @staticmethod
    def get_airplane_by_id(airplane_id):
        return airplane_repository.get_airplane_by_id(airplane_id)

    @staticmethod
    def get_airplane_by_name(name):
        return airplane_repository.get_airplane_by_name(name)