from rest_framework import serializers


from .models import Flight


# List Flight's
class FlightListSerializer(serializers.ModelSerializer):
    
    airplane_name = serializers.SerializerMethodField()
    airplane_capacity = serializers.SerializerMethodField()
    class Meta:
        model=Flight
        fields = [
            'airplane_name', 
            'airplane_capacity', 
            'origin', 
            'destination', 
            'departure_date', 
            'arrival_date', 
            'duration', 
            'status', 
            'base_price'
        ]
        
    def get_airplane_name(self, obj):
        return obj.airplane.name
    
    def get_airplane_capacity(self, obj):
        return obj.airplane.capacity