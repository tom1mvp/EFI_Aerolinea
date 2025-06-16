from django.contrib.auth.hashers import make_password, check_password


from user.repositories.user import UserRepository

# User service
class UserServices:
    
    # Password hashed logic
    @staticmethod
    def encrip_password(password):
        return make_password(password) # Password hashed
    
    # Register and login logic
    @staticmethod
    def login(username, password):
        user = UserRepository.get_by_username(username)
        
        if not user:
            raise ValueError("El usuario ingresado no existe")
        
        UserServices.encrip_password(password)
        
        if not check_password(password, user.password):
            raise ValueError("La contraseña es incorrecta")
        
        return user
    
    @staticmethod
    def register(first_name, last_name, username, password, email):
        user = UserRepository.get_by_username(username)
        
        if user:
            raise ValueError("El usuario ingresado ya existe")
        
        # Hash password
        password_hashed = UserServices.encrip_password(password)
        
        new_user = UserRepository.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password_hashed,
            email=email
        )
        
        return new_user
    
    # Method UPDATE
    @staticmethod
    def update_user(user_id, first_name, last_name, username, password, email):
        user = UserRepository.get_by_id(user_id=user_id)
        
        if not user:
            raise ValueError("El ID solicitado no existe")
        
        password_hashed = UserServices.encrip_password(password)
        
        updated_user = UserRepository.update_user(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password_hashed,
            email=email
        )
        
        return updated_user
    
    # Method DELETE
    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_by_id(user_id=user_id)
        
        if user:
            return UserRepository.delete_user(user_id=user_id)
        return False
    