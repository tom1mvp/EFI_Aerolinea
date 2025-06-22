
from django.shortcuts import redirect, render
from django.contrib.auth import logout, login
from django.contrib import messages
from user.forms import RegisterForm, LoginForm
from django.views import View




from user.services.user import UserServices


# User views
class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    
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

        try:
            UserServices.login(request, username, password)
            messages.success(request, "Sesión iniciada")
            return redirect("index")

        except ValueError as e:
            messages.error(request, str(e))

        return render(request, "accounts/login.html", {"form": form}, {"user": username})


        
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
