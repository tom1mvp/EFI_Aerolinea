from django.urls import path


from passengers_management.views import (
    ListPassangerView,
    SpecificPassangerView,
    CreatePassangerView,
    UpdatePassangerView,
    DeletePassangerView
)

urlpatterns = [
    path(
        'passangers/',
        ListPassangerView.as_view(),
        name='list-passanger'
    ),
    
    path(
        'passanger/<str:name>',
        SpecificPassangerView.as_view(),
        name='passanger'
    ),
    
    path(
        'create/',
        CreatePassangerView.as_view(),
        name='create-passanger'
    ),
    
    path(
        'passanger/update/<int:pk>',
        UpdatePassangerView.as_view(),
        name='update-passanger'
    ),
    
    path(
        'passanger/<int:pk>/status',
        DeletePassangerView.as_view(),
        name='delete-passanger'
    )
]