from django.contrib import admin
from .models import Airplane, Seat

@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capacity', 'rows', 'columns', 'status')
    search_fields = ('name', 'status')
    list_filter = ('status',)
    
@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'airplane', 'number', 'rows', 'columns', 'type_seat', 'status')
    search_fields = ('airplane_name', 'number', 'type_seat', 'status')
    list_filter = ('airplane', 'type_seat', 'status')