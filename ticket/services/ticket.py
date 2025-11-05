from rest_framework.exceptions import ValidationError


from ticket.repositories.ticket import TicketRepository


class TicketServices:
    @staticmethod
    def get_all_tickets():
        return TicketRepository.get_all_tickets()
    
    @staticmethod
    def get_tickey_by_barcode(barcode):
        return TicketRepository.get_ticket_by_barcode(barcode)
    
    @staticmethod
    def create_ticket(
      data,
      reservation_id
    ):
        
        required_fields = [
            'ticket_number',
            'issue_date',
            'barcode',
            'status'
        ]
        
        for field in required_fields:
            if field not in data:
                raise ValidationError(f'Falta el campo obligatorio: {field}')
            
        new_ticket =  TicketRepository.create_ticket(
            reservation_id=reservation_id,
            ticket_number=data['ticket_number'],
            issue_date=data['issue_date'],
            barcode=data['barcode'],
            status=data['status']
        )
        
        return new_ticket
    
    