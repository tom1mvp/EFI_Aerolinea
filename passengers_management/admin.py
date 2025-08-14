from django.contrib import admin


from passengers_management.models import Passenger
from passengers_management.services.passengers import PassengerServices
from reservations.models import Reservation


class ReservationInline(admin.TabularInline):
    model = Reservation
    extra = 0
    readonly_fields = (
        'flight', 'seat', 'flight_number', 'reservation_date',
        'status', 'price', 'reservation_code'
    )
    can_delete = False
    show_change_link = True


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'document', 'phone_number')
    list_filter = ('user__first_name',)
    search_fields = ('document',)
    inlines = [ReservationInline]  # Historial

    def save_model(self, request, obj, form, change):
        if not change:
            created_passenger = PassengerServices.create_passenger(
                user_id=obj.user.id,
                phone_number=obj.phone_number,
                document=obj.document
            )
            obj.id = created_passenger.id
        else:
            updated_passenger = PassengerServices.update_passenger(
                passenger_id=obj.id,
                user_id=obj.user.id,
                phone_number=obj.phone_number,
                document=obj.document
            )
            obj = updated_passenger
        # Guardamos el objeto usando el admin para que Django lo registre correctamente
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        PassengerServices.delete_passenger(obj.id)
        