from django.urls import path


from airplanes_management.views import (
    ListAirplaneView,
    CreateAirplaneView,
    UpdateAirplaneView,
    ListSeatView,
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
        'seat/update/<int:pk>',
        UpdateSeatView.as_view(),
        name='update'
    )
]
