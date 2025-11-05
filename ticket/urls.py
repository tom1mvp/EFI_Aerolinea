from django.urls import path


from ticket.views import (
    ListTicketView,
    ListTicketByCodeView,
    CreateTicket
)

urlpatterns = [
    path(
        'ticket/',
        ListTicketView.as_view(),
        name='list-ticket'
    ),
    
    path(
      'ticket/<str:barcode>',
      ListTicketByCodeView.as_view(),
      name='list-barcode'
    ),
    
    path(
      'create/',
      CreateTicket.as_view(),
      name='create-ticket'
    )
]