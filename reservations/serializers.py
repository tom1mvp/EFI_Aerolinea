from rest_framework import serializers


from .models import Reservation


class ReservationListSerializer(serializers.ModelSerializer):
    
    user_fullname = serializers.SerializerMethodField()
    
    flight_origin = serializers.SerializerMethodField()
    flight_destination = serializers.SerializerMethodField()
    
    seat_number = serializers.SerializerMethodField()
    
    class Meta:
        model = Reservation
        fields = [
            'user_fullname',
            'flight_origin',
            'flight_destination',
            'seat_number',
            'flight_number',
            'reservation_date',
            'status',
            'price',
            'reservation_code'
        ]
       
    def get_user_fullname(self, obj):
        return obj.passanger.user.name
        
    def get_flight_origin(self, obj):
        return obj.flight.origin

    def get_flight_destination(self, obj):
        return obj.flight.destination

    def get_seat_number(self, obj):
        return obj.seat.number