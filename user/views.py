from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, logout



from user.services.user import UserServices


# User views        
def update_user_view(request, user_id):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        
        try:
            UserServices.update_user(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email
            )
            return render(
                request,
            )
        except Exception as e:
            messages.error(request, "Faltan datos")
        
def delete_user_view(request, user_id):
    if request.method == "POST":
        try:
            UserServices.delete_user(
                user_id=user_id
            )
            return render(
                request,
            )
        except Exception as e:
            messages.error(request, "Faltan datos")