from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=128, null=False)
    mail = models.EmailField(null=False, unique=True)
    birth_day = models.DateField(blank=True, null=False)
    phone = models.CharField(max_length=10, null=False)
    name = models.CharField(max_length=120, null=False)
    document = models.CharField(max_length=9, null=False)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Nombre: {self.name} || Usuario: {self.username} || Mail: {self.mail}'
    
