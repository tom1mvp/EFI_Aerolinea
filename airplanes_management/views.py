from rest_framework.views import APIView


from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from airplanes_management.services.airplane import AirplaneService
from airplanes_management.services.seat import SeatServices


from airplanes_management.serializers import AirplaneListSerializer, SeatListSerializer

# Airplane
class ListAirplaneView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        airplanes = AirplaneService.get_all_airplane()
        
        if not airplanes:
            return Response(
                {'message': 'No hay aviones para mostrar'},
                status=status.HTTP_204_NO_CONTENT
            )
            
        serializer = AirplaneListSerializer(airplanes, many=True)
        
        return Response(
            {'data': serializer.data},
            status=status.HTTP_200_OK
        )

class AvailableSeatsByFlightView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        flight_id = int(kwargs.get('pk'))
        
        try:
            available_seats = SeatServices.get_available_seats_for_flight(flight_id)
            
            if not available_seats:
                return Response(
                    {'message': f'No hay asientos disponibles para el vuelo ID: {flight_id}'},
                    status=status.HTTP_204_NO_CONTENT
                )
            
            serializer = SeatListSerializer(available_seats, many=True)
            
            return Response(
                {'data': serializer.data},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class SeatAvailabilityCheckView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        flight_id = int(kwargs.get('flight_pk'))
        seat_id = int(kwargs.get('seat_pk'))
        
        try:
            is_available = SeatServices.is_seat_available_for_flight(seat_id, flight_id)
            
            message = 'El asiento está disponible.' if is_available else 'El asiento NO está disponible o no existe para este vuelo.'
            
            return Response(
                {
                    'message': message,
                    'flight_id': flight_id,
                    'seat_id': seat_id,
                    'is_available': is_available
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class CreateAirplaneView(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        data = request.data
        
        if not data:
            return Response(
                {'message': 'Falta información'},
                status=status.HTTP_204_NO_CONTENT
            )
        
        try:
            response = AirplaneService.create_airplane(data)
            
            # Serializer after return Response
            serializer = AirplaneListSerializer(response)
            
            return Response({'message': 'El avion fue creado con éxito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class UpdateAirplaneView(APIView):
    permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        airplane_id = int(kwargs.get('pk'))
        
        
        if not data or not airplane_id:
            return Response(
                {'message': 'Faltan elementos esenciales'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            response = AirplaneService.update_airplane(data, airplane_id)
            serializer = AirplaneListSerializer(response)
            
            return Response({'message': 'El avion fue actualizado con éxito', 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
            
                
# Seat
class ListSeatView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        seats = SeatServices.get_all_seat()
        
        if not seats:
            return Response(
                {'message': 'No hay aviones para mostrar'},
                status=status.HTTP_204_NO_CONTENT
            )
        
        serializer = SeatListSerializer(seats, many=True)
        
        return Response(
            {'data': serializer.data},
            status=status.HTTP_200_OK
        )

class UpdateSeatView(APIView):
    permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        
        seat_id = int(kwargs.get('pk'))
        
        if not data or 'airplane_id' not in data:
            return Response(
                {'message': 'Faltan campos esenciales'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            response = SeatServices.update_seat(data, data['airplane_id'], seat_id)
            
            serializer = SeatListSerializer(response)
            
            return Response({'message': 'El asiento fue actualizado con éxito', 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
                return Response(
                    {'message': str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
