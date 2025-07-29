

from django.shortcuts import redirect, render
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.views import View


from user.forms import RegisterForm, LoginForm


from user.services.user import UserServices
from flights_management.services.flights import FlightsServices

# User views
class HomeView(View):
    def get(self, request):
        destination = request.GET.get("q", "").strip()

        if destination:
            flights = FlightsServices.get_by_destination(destination)
    
            if not flights:
                messages.warning(request, "No se encontraron vuelos para ese destino.")
        else:
            flights = FlightsServices.get_all_flights()

        return render(request, 'index.html', {
            'user': request.user,
            'flights': flights,
            'query': destination
        })

        
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        
        return render(
            request,
            'accounts/login.html',
            {"form": form}
        )
        
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                messages.success(request, "Sesión iniciada")
                
                return redirect("index")
            else:
                messages.error(request, "Usuario o contraseña inválidos")

        else:
            messages.error(request, "Por favor completa correctamente el formulario.")

        return render(request, "accounts/login.html", {"form": form})
        
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user = UserServices.register(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )

            messages.success(request, "Registro exitoso. Ahora podés iniciar sesión.")
            return redirect("login")

        messages.error(request, "Por favor corregí los errores en el formulario.")
        return render(request, 'accounts/register.html', {"form": form})

