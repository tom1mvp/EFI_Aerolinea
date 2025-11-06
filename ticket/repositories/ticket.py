from ticket.models import Ticket


class TicketRepository:
    @staticmethod
    def get_all_tickets():
        return Ticket.objects.all()
    
    @staticmethod
    def get_ticket_by_barcode(barcode):
        return Ticket.objects.filter(barcode=barcode).first()
    
    @staticmethod
    def create_ticket(
        reservation_id,
        ticket_number,
        issue_date,
        barcode,
        status
    ):
        new_ticket = Ticket.objects.create(
            reservation_id=reservation_id,
            ticket_number=ticket_number,
            issue_date=issue_date,
            barcode=barcode,
            status=status
        )
        
        return new_ticket
    