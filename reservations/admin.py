import openpyxl
from datetime import datetime

from django.contrib import admin, messages
from django.http import HttpResponse
from django.urls import path, reverse
from django.shortcuts import render, redirect

from reservations.models import Reservation
from reservations.services.reservations import ReservationServices


@admin.register(Reservation)
class ReservationsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'passenger', 'flight', 'seat',
        'flight_number', 'reservation_date', 'status'
    )
    list_filter = ('flight_number', 'status')
    search_fields = ('reservation_code',)
    actions = ['view_passengers_report']

    def save_model(self, request, obj, form, change):
        try:
            # Verificar disponibilidad
            ReservationServices.check_seat_availability(
                flight_id=obj.flight.id,
                seat_id=obj.seat.id
            )

            if not change:
                # Crear nueva reserva
                ReservationServices.create_reservation(
                    passenger_id=obj.passenger.id,
                    flight_id=obj.flight.id,
                    seat_id=obj.seat.id,
                    flight_number=obj.flight_number,
                    status=obj.status,
                    price=obj.price,
                    reservation_code=obj.reservation_code
                )
            else:
                # Actualizar reserva existente
                ReservationServices.update_reservation(
                    reservation_id=obj.id,
                    passenger_id=obj.passenger.id,
                    flight_id=obj.flight.id,
                    seat_id=obj.seat.id,  # <-- CORREGIDO: usar .id
                    flight_number=obj.flight_number,
                    status=obj.status,
                    price=obj.price,
                    reservation_code=obj.reservation_code
                )
        except ValueError as e:
            self.message_user(request, str(e), level='error')

    def delete_model(self, request, obj):
        ReservationServices.delete_reservation(reservation_id=obj.id)

    @admin.action(description="View passengers by selected flight(s)")
    def view_passengers_report(self, request, queryset):
        flight_ids = queryset.values_list('flight_id', flat=True).distinct()

        if not flight_ids:
            self.message_user(request, "No flights found in selected reservations.", level='error')
            return

        url = reverse('admin:passenger-report')
        url += f"?flights={','.join(str(fid) for fid in flight_ids)}"
        return redirect(url)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'passenger-report/',
                self.admin_site.admin_view(self.passenger_report_view),
                name='passenger-report'
            ),
            path(
                'download-passenger-excel/',
                self.admin_site.admin_view(self.download_passenger_excel),
                name='download-passenger-excel'
            ),
        ]
        return custom_urls + urls

    def passenger_report_view(self, request):
        flight_ids = request.GET.get('flights')
        if not flight_ids:
            messages.error(request, "No flight IDs provided.")
            return redirect('..')

        flight_ids = [int(fid) for fid in flight_ids.split(',')]
        report_data = {}

        for fid in flight_ids:
            try:
                passengers = ReservationServices.reports_passagers_by_flights(fid)
                report_data[fid] = passengers
            except ValueError as e:
                report_data[fid] = []

        return render(request, 'passenger_report.html', {
            'report_data': report_data
        })

    def download_passenger_excel(self, request):
        flight_ids = request.GET.get('flights')
        if not flight_ids:
            messages.error(request, "No se proporcionaron IDs de vuelos.")
            return redirect('..')

        flight_ids = [int(fid) for fid in flight_ids.split(',')]
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Pasajeros"
        ws.append(['Vuelo ID', 'Pasajero', 'Email', 'Documento', 'Teléfono', 'Asiento'])

        for fid in flight_ids:
            try:
                passengers = ReservationServices.reports_passagers_by_flights(fid)
                for p in passengers:
                    ws.append([
                        fid,
                        p['pasajero'],
                        p['email'],
                        p['documento'],
                        p['telefono'],
                        p['asiento']
                    ])
            except ValueError:
                ws.append([fid, 'No hay pasajeros', '', '', '', ''])

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        filename = f"reporte_pasajeros_{datetime.now():%Y%m%d_%H%M%S}.xlsx"
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        wb.save(response)
        return response
