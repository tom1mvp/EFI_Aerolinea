from rest_framework.views import APIView


from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from flights_management.services.flights import FlightService
from flights_management.serializers import FlightListSerializer


class ListFlightView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        flights = FlightService.get_all_flights()
        
        if not flights:
            return Response(
                {'message': 'No hay vuelos para mostrar'},
                status=status.HTTP_204_NO_CONTENT
            )
        
        serializer = FlightListSerializer(flights, many=True)
        
        return Response(
            {'data': serializer.data},
            status=status.HTTP_200_OK
        )

class DetailFlightView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        flight_id = int(kwargs.get('pk'))
        
        flight = FlightService.get_by_id_flight(flight_id)
        
        if not flight:
            return Response(
                {'message': 'No existe el vuelo'},
                status=status.HTTP_204_NO_CONTENT
            )
        
        serializer = FlightListSerializer(flight)
        
        return Response(
            {'data': serializer.data},
            status=status.HTTP_200_OK
        )

class CreateFlightView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        data = request.data

        if not data:
            return Response(
                {'message': 'Falta información'},
                status=status.HTTP_204_NO_CONTENT
            )

        try:
            response = FlightService.create_flight(data, data['airplane_id'])
            serializer = FlightListSerializer(response)

            return Response(
                {'message': 'El vuelo fue creado con éxito', 'data': serializer.data},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
            
class UpdateFLightView(APIView):
    permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        
        flight_id = int(kwargs.get('pk'))
        
        if not data or 'airplane_id' not in data:
            return Response(
                {'message': 'Faltan campos esenciales'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            response = FlightService.updateflight(data, data['airplane_id'], flight_id)
            serializer = FlightListSerializer(response)
            
            return Response({'message': 'El vuelo fue actualizado con éxito', 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
                return Response(
                    {'message': str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )

# SOFT DELETE
                
class DeleteFlight(APIView):
    permission_classes = [IsAdminUser]
    
    def delete(self, request, *args, **kwargs):
        flight_id = int(kwargs.get('pk'))
        
        if not flight_id:
            return Response(
                {'message': 'Falta información'},
                status=status.HTTP_204_NO_CONTENT
            )
        
        try:
            FlightService.delete_flight(flight_id)
            return Response({'message': 'El vuelo fue eliminado con éxito'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
