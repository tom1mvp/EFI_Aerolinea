from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login  # Import the login function

from user.services.user import UserServices


# Home views
def home_view(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)  # Log in the user
            messages.success(request, "Sesión iniciada correctamente")
            return redirect("index")
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos")
    return render(request, 'accounts/login.html')
                
def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        try:
            UserServices.register(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email
            )
            messages.success(request, "Registro exitoso")
            return redirect('login')
        except Exception as e:
            messages.error(request, "Error en el registro: " + str(e))
    return render(request, 'accounts/register.html')
