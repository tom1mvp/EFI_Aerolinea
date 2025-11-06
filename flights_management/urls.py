from django.urls import path


from flights_management.views import (
    ListFlightView,
    DetailFlightView,
    CreateFlightView,
    UpdateFLightView,
    DeleteFlight
)

urlpatterns = [
    path(
        'list/',
        ListFlightView.as_view(),
        name='list flights'
    ),
    
    path(
        'flight/<int:pk>',
        DetailFlightView.as_view(),
        name='detail_flight'
    ),
    
    path(
        'create/',
        CreateFlightView.as_view(),
        name='create_flight'
    ),
    
    path(
        'flight/update/<int:pk>',
        UpdateFLightView.as_view(),
        name='update_flight'
    ),
    
    path(
        'flight/<int:pk>/status',
        DeleteFlight.as_view(),
        name='delete_flight'
    )
]