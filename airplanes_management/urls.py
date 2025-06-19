from django.urls import path
from . import views

urlpatterns = [
    path(
        route='create/',
        view=views.create_airplane,
        name='create_airplane'
    ),
    path(
        route='list/',
        view=views.airplane_list,
        name='airplane_list'
    )
]