from django.contrib import admin
from .models import Airplane, Seat

# Register your models here.
@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    lista_display = ('id', 'name', 'capacity', 'rows', 'columns', 'state')
    search_fields = ('name', 'state')
    list_filter = ('state',)

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'airplane', 'number', 'rows', 'columns', 'tipe', 'state')
    search_fields = ('airplane_name', 'number', 'tipe', 'state')
    list_filter = ('airplane', 'tipe', 'state')
    
    
    