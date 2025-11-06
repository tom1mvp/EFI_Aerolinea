from django.urls import path


from reservations.views import (
    ListReservationView,
    SpecificReservationView,
    ReservationByPassangerView,
    CreateReservationView,
    UpdateReservationView,
    DeleteReservationView
)

urlpatterns = [
    path(
        'reservation/',
        ListReservationView.as_view(),
        name='reservation-list'
    ),
    
    path(
        'reservation/<int:pk>',
        SpecificReservationView.as_view(),
        name='specific-list'
    ),
    
    path(
        'reservation/passanger/<int:pk>',
        ReservationByPassangerView.as_view(),
        name='reservation-passanger'
    ),
    
    path(
        'create/',
        CreateReservationView.as_view(),
        name='create-reservation'
    ),
    
    path(
        'reservation/update/<int:pk>',
        UpdateReservationView.as_view(),
        name='update-reservation'
    ),
    
    path(
        'reservation/<int:pk>/status',
        DeleteReservationView.as_view(),
        name='delete-reservation'
    )
]
