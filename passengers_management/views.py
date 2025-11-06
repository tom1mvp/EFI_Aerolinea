from rest_framework.views import APIView


from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from passengers_management.services.passangers import PassangerService
from passengers_management.serializers import PassangerListSerializer


class ListPassangerView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        passanger = PassangerService.get_all_passangers()
        
        if not passanger:
            return Response(
                {'message': 'No hay pasajeros mostrar'},
                status=status.HTTP_204_NO_CONTENT
            )
        
        serializer = PassangerListSerializer(passanger, many=True)
        
        return Response(
            {'data': serializer.data},
            status=status.HTTP_200_OK
        )

class SpecificPassangerView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        
        name = str(kwargs.get('name'))
        try:
            passanger = PassangerService.get_passanger_by_name(name)
            
            if not passanger:
                return Response(
                    {'message': 'No hay pasajeros mostrar'},
                    status=status.HTTP_204_NO_CONTENT
                )
                
            serializer = PassangerListSerializer(passanger, many=True)
            
            return Response(
                {'data': serializer.data},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class CreatePassangerView(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        data = request.data

        if not data:
            return Response({'message': 'Falta información'},  status=status.HTTP_204_NO_CONTENT)
        
        try:
            passenger = PassangerService.create_passanger(
                data, 
                data['user_id'],
            )
            
            serializer = PassangerListSerializer(passenger)
            return Response({
                'message': 'El pasajero fue creado con éxito',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
class UpdatePassangerView(APIView):
    permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        
        passanger_id = int(kwargs.get('pk'))
        
        if not data or 'user_id' not in data or not passanger_id:
            return Response(
                {'message': 'Faltan campos esenciales'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            
            response = PassangerService.update_passanger(
                data, 
                passanger_id, 
                data['user_id']
            )
            serializer = PassangerListSerializer(response)
            
            return Response({'message': 'El pasajero fue actualizado con éxito', 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
            
class DeletePassangerView(APIView):
    permission_classes = [IsAdminUser]
    
    def delete(self, request, *args, **kwargs):
        passanger_id = int(kwargs.get('pk'))
        
        if not passanger_id:
            return Response(
                {'message': 'Falta información'},
                status=status.HTTP_204_NO_CONTENT
            )
        
        try:
            PassangerService.delete_passanger(passanger_id)
            return Response({'message': 'El pasajero fue eliminado con éxito'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )