from django.shortcuts import render, redirect
from django.contrib import messages
from ticket.services.ticket import TicketServices

def ticket_list(request):
    tickets = TicketServices.get_all_tickets()
    return render(request, 'tickets/list.html', {'tickets': tickets})

def ticket_detail(request, ticket_id):
    try:
        ticket = TicketServices.get_ticket_by_id(ticket_id)
        return render(request, 'tickets/detail.html', {'ticket': ticket})
    except ValueError as e:
        messages.error(request, str(e))
        return redirect('ticket_list')

def ticket_create(request):
    reservations = TicketServices.get_all_reservations()
    if request.method == "POST":
        reservation_id = request.POST.get("reservation_id")
        ticket_number = request.POST.get("ticket_number")
        try:
            TicketServices.create_ticket(reservation_id=reservation_id, ticket_number=ticket_number)
            messages.success(request, "Ticket created successfully.")
        except ValueError as e:
            messages.error(request, str(e))
        return redirect('ticket_list')
    return render(request, 'tickets/create.html', {'reservations': reservations})

def ticket_delete(request, ticket_id):
    try:
        ticket = TicketServices.get_ticket_by_id(ticket_id)
    except ValueError as e:
        messages.error(request, str(e))
        return redirect('ticket_list')

    if request.method == "POST":
        try:
            TicketServices.delete_ticket(ticket_id=ticket_id)
            messages.success(request, "Ticket deleted successfully.")
        except ValueError as e:
            messages.error(request, str(e))
        return redirect('ticket_list')
    return render(request, 'tickets/delete.html', {'ticket': ticket})
