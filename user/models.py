from django.db import models

# Users models
class User(models.Model):
    
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('client', 'Client'),
    ]
    
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    username = models.CharField(max_length=50)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=128, null=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    
    
    def __str__(self):
        return f"Nombre: ${self.first_name} - Apellido: ${self.last_name} - Email: ${self.email}"
    
    