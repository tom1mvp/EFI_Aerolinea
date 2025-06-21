from ticket.models import Ticket

class TicketRepository:
    @staticmethod
    def get_all_tickets():
        return Ticket.objects.all()

    @staticmethod
    def get_by_id(ticket_id):
        return Ticket.objects.filter(id=ticket_id).first()

    @staticmethod
    def create_ticket(reservation, ticket_number):
        return Ticket.objects.create(reservation=reservation, ticket_number=ticket_number)

    @staticmethod
    def delete_ticket(ticket):
        ticket.delete()
