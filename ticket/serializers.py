from rest_framework import serializers


from .models import Ticket


class TicketListSerializer(serializers.ModelSerializer):
    flight_number = serializers.SerializerMethodField()
    reservation_date = serializers.SerializerMethodField()
    
    class Meta:
        model = Ticket
        fields = [
            'flight_number',
            'reservation_date',
            'ticket_number',
            'issue_date',
            'barcode',
            'status'
        ]
        
    def get_flight_number(self, obj):
        return obj.reservation.flight_number
    
    def get_reservation_date(self, obj):
        return obj.reservation.reservation_date