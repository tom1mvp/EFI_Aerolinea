from django.db import models

# Users models

"""Nota: No se va a requerir el uso de roles en este proyecto"""
class User(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    username = models.CharField(max_length=50)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=128, null=False)
    
    def __str__(self):
        return f"Nombre: ${self.first_name} - Apellido: ${self.last_name} - Email: ${self.email}"
    
    