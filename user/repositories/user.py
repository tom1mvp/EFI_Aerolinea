from user.models import User

# Methods GET, POST, PUT and DELETE

class UserRepository:
    # Method GET
    @staticmethod
    def get_all_users():
        return User.objects.all() # It's return all users in db
    
    @staticmethod
    def get_by_username(username):
       return User.objects.filter(username=username).first() # Get the specific user
   
    @staticmethod
    def get_by_id(user_id):
        return User.objects.filter(id=user_id).first() # Get the specific id
   
    # Method POST
    @staticmethod
    def create_user(first_name, last_name, username, password, email):
        new_user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
   
        return new_user

    # Method PUT
    @staticmethod
    def update_user(user_id, first_name, last_name, username, password, email):
        # Search the ID of user
        user = User.objects.filter(id=user_id).first()
        
        if not user:
            raise ValueError('No se pudo encontrar el usuario específico.')
        
        user.first_name=first_name
        user.last_name=last_name
        user.username=username
        user.password=password
        user.email=email
        
        user.save()
        
        return user
   
    # Method DELETE
    @staticmethod
    def delete_user(user_id):
        user = User.objects.filter(id=user_id).first()
        
        if not user:
            raise ValueError('No se pudo encontrar el usuario específico.')
        
        user.delete()
        
        
        