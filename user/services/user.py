from django.contrib.auth.hashers import make_password, check_password


from rest_framework.exceptions import ValidationError


from user.repositories.user import UserRepository
from user.serializers import UserSerializer


class UserService:
    
    # Method GET (all, by name and by mail)
    @staticmethod
    def get_all():
        return UserRepository.get_all()
    
    @staticmethod
    def get_by_id(user_id):
        return UserRepository.get_by_id(user_id)
    
    
    # Method POST (login and register)
    
    # Password hash
    @staticmethod
    def encrip_password(data):
        data['password'] = make_password(data.get('password'))
        
        # Hash
        serializer = UserSerializer.UserListSeriaizer(data=data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            return user
        else:
            raise ValidationError(serializer.errors)
        
    # Login
    @staticmethod
    def login(data):
        user = UserRepository.get_by_username(data['username'])
        
        if not user:
            raise ValidationError("Error: ", 'El usuario no existe')
        
        if not check_password(data['password'], user.password):
            raise ValidationError({'error': 'Contraseña incorrecta'})
        
        return {
            'pk': user.id,
            'username': user.username,
            'mail': user.mail
        }
        
    # Register
    @staticmethod
    def register(data):
        # Check if the user name or e-mail address already exist
        if UserRepository.get_by_username(data['username'] or UserRepository.get_by_mail(data['mail'])):
            return {'error': 'El usuario o email ya existen'}
        
        hashed_password = make_password(data['password'])
        
        user = UserRepository.create_user(
            username=data['username'], 
            password=hashed_password,
            mail=data['mail'], 
            birth_day=data['birth_day'], 
            phone=data['phone'], 
            name=data['name'], 
            document=data['document']
		)
        
        
        # Create serializer after return
        serializer = UserSerializer.UserListSeriaizer(user)
        
        return serializer.data
    
    # Method PUT (update)
    @staticmethod
    def update_user(data, user_id):
        required_fields = ['username', 'password', 'mail', 'birth_day', 'phone', 'name', 'document']
    
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
        
        hashed_password = make_password(data['password'])
        
        user = UserRepository.update_user(
            user_id=user_id,
            username=data['username'], 
            password=hashed_password,
            mail=data['mail'], 
            birth_day=data['birth_day'], 
            phone=data['phone'], 
            name=data['name'], 
            document=data['document']
        )
    
        return user

    
    # Method DELETE (soft)
    @staticmethod
    def delete_user(user_id):
        return UserRepository.delete_user(user_id)