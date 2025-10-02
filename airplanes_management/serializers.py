from rest_framework import serializers


from .models import Airplane, Seat


# List airplane
class AirplaneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields ='__all__'
        
class SeatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields ='__all__'