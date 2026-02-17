from django.contrib import admin
from accommodation.models import Accommodation, AccommodationAvailability


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ["name", "city", "accommodation_type", "base_price", "is_active"]
    list_filter = ["accommodation_type", "is_active", "city"]
    search_fields = ["name", "city__name"]


@admin.register(AccommodationAvailability)
class AccommodationAvailabilityAdmin(admin.ModelAdmin):
    list_display = ["accommodation", "date", "is_available", "rooms_available"]
    list_filter = ["is_available", "date"]
    search_fields = ["accommodation__name"]
