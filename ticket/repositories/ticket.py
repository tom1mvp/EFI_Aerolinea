from ticket.models import Ticket
from reservations.models import Reservation

class TicketRepository:
    @staticmethod
    def get_all_tickets():
        return Ticket.objects.all()

    @staticmethod
    def get_by_id(ticket_id):
        return Ticket.objects.filter(id=ticket_id).first()

    @staticmethod
    def create_ticket(reservation_id, ticket_number, issue_date, barcode, status):
       reservation = Reservation.objects.filter(id=reservation_id).first()
       
       if not reservation:
           raise ValueError('La reservación no existe')
       
       new_ticket = Ticket.objects.create(
            reservation=reservation_id,
            ticket_number=ticket_number,
            issue_date=issue_date,
            barcode=barcode,
            status=status
        )
       
       return new_ticket

    @staticmethod
    def update_ticket(
        ticket_id,
        reservation_id,
        ticket_number,
        issue_date,
        barcode,
        status
        ):
        
        ticket = Ticket.objects.filter(id=ticket_id).first()
        
        reservation = Reservation.objects.filter(id=reservation_id).first()
        
        if not ticket:
            raise ValueError('El ticket no existe')
        
        if not reservation:
            raise ValueError('La reservación no existe')
        
        ticket.reservation=reservation_id
        ticket.ticket_number=ticket_number
        ticket.issue_date=issue_date
        ticket.barcode=barcode
        ticket.status=status
        
        ticket.save()
        
        return ticket
    
    
    @staticmethod
    def delete_ticket(ticket_id):
        ticket = Ticket.objects.filter(id=ticket_id).first()
        
        if not ticket:
            raise ValueError('No se encontro el ticket')
        
        ticket.delete()