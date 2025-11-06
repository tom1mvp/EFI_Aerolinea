from django.urls import path


from reporting.views import (
    ListPassangerByFlightView,
    ListReservationActiveView
)

urlpatterns = [
    path(
        'reporting/flight_id/<int:pk>',
        ListPassangerByFlightView.as_view(),
        name='list-passanger'
    ),
    
    path(
        'reporting/reservation/<int:pk>',
        ListReservationActiveView.as_view(),
        name='list-reservation'
        
    )
]