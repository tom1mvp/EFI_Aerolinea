from rest_framework.views import APIView


from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from reservations.services.reservation import ReservationServices
from reservations.serializers import ReservationListSerializer


class ListReservationView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        reservation = ReservationServices.get_all_reservation()
        
        if not reservation:
            return Response(
                {'message': 'No hay reservas mostrar'},
                status=status.HTTP_204_NO_CONTENT
            )
        
        serializer = ReservationListSerializer(reservation, many=True)
        
        return Response(
            {'data': serializer.data},
            status=status.HTTP_200_OK
        )
        
class SpecificReservationView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        reservation_id = int(kwargs.get('pk'))
        
        if not reservation_id:
            return Response(
                {'message': 'No hay reservas mostrar'},
                status=status.HTTP_204_NO_CONTENT
            )
            
        try:
            reservation = ReservationServices.get_reservation_by_id(reservation_id)
                
            serializer = ReservationListSerializer(reservation)
            
            return Response(
                {'data': serializer.data},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class ReservationByPassangerView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        passanger_id = int(kwargs.get('pk'))
        
        if not passanger_id:
            return Response(
                {'message': 'No hay reservas mostrar'},
                status=status.HTTP_204_NO_CONTENT
            )
        
        try:
            reservation = ReservationServices.get_reservation_by_passanger(passanger_id)
            serializer = ReservationListSerializer(reservation, many=True)
            
            return Response(
                {'data': serializer.data},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class CreateReservationView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        
        if not data or 'passanger_id' not in data or 'flight_id' not in data or 'seat_id' not in data:
            return Response(
                {'message': 'Faltan campos esenciales'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            response = ReservationServices.create_reservation(
                data,
                data['passanger_id'],
                data['flight_id'],
                data['seat_id']
            )
            
            serializer = ReservationListSerializer(response)
            
            return Response({'message': 'La reserva fue creada con éxito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
            
class UpdateReservationView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        
        reservation_id = int(kwargs.get('pk'))
        
        if not data or not reservation_id or 'passanger_id' not in data or 'flight_id' not in data or 'seat_id' not in data:
            return Response(
                {'message': 'Faltan campos esenciales'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            response = ReservationServices.update_reservation(
                data,
                reservation_id,
                data['passanger_id'],
                data['flight_id'],
                data['seat_id']
            )
            
            serializer = ReservationListSerializer(response)
            
            return Response({'message': 'La reserva fue actualizada con éxito', 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class DeleteReservationView(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, *args, **kwargs):
        reservation_id = int(kwargs.get('pk'))
        
        if not reservation_id:
            return Response(
                {'message': 'No hay reservas mostrar'},
                status=status.HTTP_204_NO_CONTENT
            )
            
        try:
            
            ReservationServices.delete_reservation(reservation_id)
            
            return Response({'message': 'La reserva fue eliminada con éxito'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
            
