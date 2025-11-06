from rest_framework.views import APIView


from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from reporting.services.reporting import ReportingServices
from reservations.serializers import ReservationListSerializer
from reporting.serializers import PassangerReportSerializer


class ListPassangerByFlightView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        flight_id = int(kwargs.get('pk'))
        
        if not flight_id:
            return Response(
                    {'message': 'No hay reportes de vuelos mostrar'},
                    status=status.HTTP_204_NO_CONTENT
                )
        
        try:
            response = ReportingServices.get_passengers_by_flight(flight_id)
            
            serializer = PassangerReportSerializer(response)
            
            return Response(
                {'data': serializer.data},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class ListReservationActiveView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        passanger_id = int(kwargs.get('pk'))
        
        if not passanger_id:
            return Response(
                    {'message': 'No hay reportes de pasajeros mostrar'},
                    status=status.HTTP_204_NO_CONTENT
                )

        try:
            response = ReportingServices.get_reservation_by_passenger(passanger_id)
            
            serializer = ReservationListSerializer(response)
            
            
            return Response(
                {'data': serializer.data},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )