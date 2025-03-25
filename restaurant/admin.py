from django.contrib import admin
from .models import Menu, Booking
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'no_of_guests', 'booking_date')
    fields = ['name', 'no_of_guests', 'booking_date']

admin.site.register(Menu)
# admin.site.register(Booking)