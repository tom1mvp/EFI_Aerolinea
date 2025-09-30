from django.urls import path


from user.views import (
    UserListView,
    LoginView,
    RegisterView,
    UpdateView,
    DeleteView
)

urlpatterns = [
    path(
        "list/", 
        UserListView.as_view(),
        name='user-list'
    ),
    
    path(
        "login/",
        LoginView.as_view(),
        name='login'
    ),
    
    path(
        "register/",
        RegisterView.as_view(),
        name='register'
    ),
    
    path(
        "user/update/<int:pk>",
        UpdateView.as_view(),
        name='update'
    ),
    
    path(
        "user/<int:pk>/status",
        DeleteView.as_view(),
        name='delete'
    )
]
