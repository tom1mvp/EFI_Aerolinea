from rest_framework import serializers


from .models import Passanger


class PassangerListSerializer(serializers.ModelSerializer):
    user_fullname = serializers.SerializerMethodField()
    user_username = serializers.SerializerMethodField()
    
    class Meta:
        model = Passanger
        fields = [
            'user_fullname', 
            'user_username', 
            'check_in_status',
            'passenger_type',
            'nationality'
        ]
        
    def get_user_fullname(self, obj):
        return obj.user.name

    def get_user_username(self, obj):
        return obj.user.username

    def get_flight_origin(self, obj):
        return obj.flight.origin

    def get_flight_destination(self, obj):
        return obj.flight.destination

    def get_seat_number(self, obj):
        return obj.seat.number