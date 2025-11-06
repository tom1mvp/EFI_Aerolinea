from user.models import User


class UserRepository():
    
    # Method GET (all users, by id, by username and by mail)
    @staticmethod
    def get_all():
        return User.objects.all()
    
    @staticmethod
    def get_by_id(user_id):
        return User.objects.filter(id=user_id).first()
    
    
    @staticmethod
    def get_by_username(username):
        return User.objects.filter(username=username).first()
    
    @staticmethod
    def get_by_mail(mail):
        return User.objects.filter(mail=mail).first()
    
    # Method POST (create user's)
    @staticmethod
    def create_user(
        username, 
        password, 
        mail, 
        birth_day, 
        phone, 
        name, 
        document,
        role,
        is_active=True
        ):
        
        
        new_user = User.objects.create(
            username=username,
            password=password, 
            mail=mail, 
            birth_day=birth_day, 
            phone=phone, 
            name=name, 
            document=document,
            role = role,
            is_active=is_active
        )
        
        new_user.save()
        
        return new_user
    
    # Method PUT (update user's)
    @staticmethod
    def update_user(
        user_id, 
        username, 
        password, 
        mail, 
        birth_day, 
        phone, 
        name, 
        document,
        role
        ):
       
        user = User.objects.filter(id=user_id).first()
        
        if not user:
            raise ValueError("El usuario no existe")
        
        
        user.username = username
        user.password = password
        user.mail = mail
        user.birth_day=birth_day
        user.phone = phone
        user.name = name
        user.role = role
        user.document = document
        
        user.save()
        
        return user
        
    # Method DELETE (soft)
    @staticmethod
    def delete_user(user_id):
        user = User.objects.filter(id=user_id).first()
        
        if not user:
            raise ValueError("El usuario no existe")
        
        if user.is_active:
            user.is_active = False
            
            user.save()
            
            return user