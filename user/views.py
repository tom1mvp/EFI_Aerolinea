from rest_framework.views import APIView


from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from user.services.user import UserService
from .serializers import UserSerializer


# Method GET (all)
class UserListView(APIView):
    
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        users = UserService.get_all()
        
        if not users:
            return Response(
                {'message': 'No hay usuarios para mostrar'},
                status=status.HTTP_204_NO_CONTENT
            )
        
        serializer = UserSerializer.UserListSeriaizer(users, many=True)
        
        return Response(
            {'data': serializer.data},
            status=status.HTTP_200_OK
        )

# Method POST (Login and register)
class RegisterView(APIView):
    def post(self, request):
        data = request.data
        
        if not data:
            return Response(
                {'message': 'No se recibieron datos'},
                status=status.HTTP_204_NO_CONTENT
            )
        try:
            response = UserService.register(data) or {}
            
            
            return Response({'message': 'Usuario registrado', 'data': response}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class LoginView(APIView):
    def post(self, request):
        data = request.data
        
        if not data or 'username' not in data or 'password' not in data:
            return Response(
                {'message': 'Faltan campos requeridos: nombre de usuario o contraseña'},
                status=status.HTTP_204_NO_CONTENT
                )
        
        try:
            response = UserService.login(data) or {}
            return Response({'message': 'Bienvenido usuario', "data":response}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

# Method UPDATE
class UpdateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        user_id = int(kwargs.get('pk'))
        
        if not data:
            return Response(
                {'message': 'Faltan elementos esenciales'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            response = UserService.update_user(data, user_id)
            serializer = UserSerializer.UserListSeriaizer(response)
            
            return Response({
                'message': 'El usuario fue actualizado con éxito',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print("Error:", e)
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

# Method DELETE (soft)
class DeleteView(APIView):
    
    permission_classes = [IsAdminUser, IsAuthenticated]
    
    def delete(self, request, *args, **kwargs):
        user_id = int(kwargs.get('pk'))
        
        if not user_id:
            return Response(
                {'message': 'Falta información'},
                status=status.HTTP_204_NO_CONTENT
            )
            
        try: 
            UserService.delete_user(user_id)
            return Response({'message': 'El usuario fue eliminado con éxito'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    