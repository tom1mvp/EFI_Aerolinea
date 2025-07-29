from ticket.repositories.ticket import TicketRepository
from reservations.repositories.reservations import ReservationRepository

class TicketServices:
    @staticmethod
    def get_all_tickets():
        return TicketRepository.get_all_tickets()

    @staticmethod
    def get_ticket_by_id(ticket_id):
        return TicketRepository.get_by_id(ticket_id)

    @staticmethod
    def create_ticket(reservation_id, ticket_number):
        reservation = ReservationRepository.get_by_id(reservation_id)
        if not reservation:
            raise ValueError("Reservation not found.")
        return TicketRepository.create_ticket(reservation=reservation, ticket_number=ticket_number)

    @staticmethod
    def delete_ticket(ticket_id):
        ticket = TicketRepository.get_by_id(ticket_id)
        if not ticket:
            raise ValueError("Ticket not found.")
        return TicketRepository.delete_ticket(ticket=ticket)