from django.urls import path


from flights_management.views import FlightManagementView

urlpatterns = [
    path('', FlightManagementView.as_view(), name='index'),
]
