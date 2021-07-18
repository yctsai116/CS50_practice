from django.contrib import admin
from .models import Flight, Airport, Passenger

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")


admin.site.register(Flight, FlightAdmin)

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("flights",)

admin.site.register(Passenger,PassengerAdmin)

admin.site.register(Airport)

