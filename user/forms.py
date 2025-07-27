from django import forms
from user.models import User
from django.core.exceptions import ValidationError
import re

class RegisterForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        label="Nombre",
        widget=forms.TextInput(
            attrs={'class': "w-full border-gray-300 rounded-md focus:ring-orange-500 focus:border-orange-500"}
        )
    )
    
    last_name = forms.CharField(
        max_length=50,
        label="Apellido",
        widget=forms.TextInput(
            attrs={'class': "w-full border-gray-300 rounded-md focus:ring-orange-500 focus:border-orange-500"}
        )
    )
    
    username = forms.CharField(
        max_length=100,
        label="Nombre de Usuario",
        widget=forms.TextInput(
            attrs={'class': "w-full border-gray-300 rounded-md focus:ring-orange-500 focus:border-orange-500"}
        )
    )
    
    password = forms.CharField(
        label="Contraseña",
        max_length=120,
        widget=forms.PasswordInput(
            attrs={'class': "w-full border-gray-300 rounded-md focus:ring-orange-500 focus:border-orange-500"}
        )
    )
    
    email = forms.EmailField(
        label="Correo Electronico",
        widget=forms.EmailInput(
            attrs={'class': "w-full border-gray-300 rounded-md focus:ring-orange-500 focus:border-orange-500"}
        )
    )
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].strip()
        
        if len(first_name) < 2:
            raise forms.ValidationError("El nombre debe tener al menos 2 caracteres.")
        
        return first_name
        
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].strip()
        
        if len(last_name) < 2:
            raise forms.ValidationError("El apellido debe tener al menos 2 caracteres.")
        
        return last_name
        
    def clean_usename(self):
        username = self.cleaned_data['username']
        
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya fue utilizado")
        
        return username
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email de usuario ya fue utilizado")
        return email
    
    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")

        if not re.search(r'[A-Z]', password):
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")

        if not re.search(r'[a-z]', password):
            raise ValidationError("La contraseña debe contener al menos una letra minúscula.")

        if not re.search(r'\d', password):
            raise ValidationError("La contraseña debe contener al menos un número.")
        
        return password
    
class LoginForm(forms.Form):
        username=forms.CharField(
            label="Nombre de usuario ",
            max_length=150,
            widget=forms.TextInput(
                attrs={
                    'class': "w-full border-gray-300 rounded-md focus:ring-orange-500 focus:border-orange-500"
                }
            )
        )
        
        password=forms.CharField(
            label="Contraseña",
            widget=forms.PasswordInput(
                attrs={
                    'class': "w-full border-gray-300 rounded-md focus:ring-orange-500 focus:border-orange-500"
                }
            )
        )
        
        
