from rest_framework.views import APIView


from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from ticket.services.ticket import TicketServices
from ticket.serializers import TicketListSerializer


class ListTicketView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        ticket = TicketServices.get_all_tickets()
        
        if not ticket:
            return Response(
                {'message': 'No hay tickets mostrar'},
                status=status.HTTP_204_NO_CONTENT
            )
            
        serializer = TicketListSerializer(ticket, many=True)
        
        return Response(
            {'data': serializer.data},
            status=status.HTTP_200_OK
        )

class ListTicketByCodeView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        barcode = str(kwargs.get('barcode'))
        
        if not barcode:
            return Response(
                {'message': 'No hay tickets mostrar'},
                status=status.HTTP_204_NO_CONTENT
            )

        try:
            ticket = TicketServices.get_tickey_by_barcode(barcode)
            
            serializer = TicketListSerializer(ticket)
            
            return Response(
                {'data': serializer.data},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
            
class CreateTicket(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        data = request.data
        
        if not data or 'reservation_id' not in data:
            return Response(
                {'message': 'Faltan campos esenciales'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            
            response = TicketServices.create_ticket(
                data,
                data['reservation_id']
            )
            
            serializer = TicketListSerializer(response)
            
            return Response({'message': 'La reserva fue creada con éxito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )