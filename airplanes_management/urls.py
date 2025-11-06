from django.urls import path


from airplanes_management.views import (
    ListAirplaneView,
    CreateAirplaneView,
    UpdateAirplaneView,
    ListSeatView,
    AvailableSeatsByFlightView,
    SeatAvailabilityCheckView,
    UpdateSeatView
)

urlpatterns = [
    path(
        'airplane/',
        ListAirplaneView.as_view(),
        name = 'airplanes'
    ),
    
    path (
        'create/',
        CreateAirplaneView.as_view(),
        name='create'
    ),
    
    path(
        'airplane/update/<int:pk>',
        UpdateAirplaneView.as_view(),
        name='update'
    ),
    
    # Seat
    path(
        'seat/',
        ListSeatView.as_view(),
        name='list-seats'
    ),
    
    path(
        'flight/<int:pk>/seat_avaible/',
        AvailableSeatsByFlightView.as_view(),
        name='flight-available-seats'
    ),
    path (
      'flight/<int:flight_pk>/seat/<int:seat_pk>/avaible',
      SeatAvailabilityCheckView.as_view(),
      name='seat-availability-check'
    ),
    
    path(
        'seat/update/<int:pk>',
        UpdateSeatView.as_view(),
        name='update'
    )
]
