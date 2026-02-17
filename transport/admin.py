from django.contrib import admin
from transport.models import TransportOperator, TransportRoute, TravelOption


@admin.register(TransportOperator)
class TransportOperatorAdmin(admin.ModelAdmin):
    list_display = ["name", "operator_type", "is_active"]
    list_filter = ["operator_type", "is_active"]
    search_fields = ["name"]


@admin.register(TransportRoute)
class TransportRouteAdmin(admin.ModelAdmin):
    list_display = ["origin", "destination", "transport_type", "is_active"]
    list_filter = ["transport_type", "is_active"]
    search_fields = ["origin__name", "destination__name"]


@admin.register(TravelOption)
class TravelOptionAdmin(admin.ModelAdmin):
    list_display = ["route", "departure_date", "departure_time", "arrival_date", "arrival_time", "base_price", "is_active"]
    list_filter = ["is_active", "route__transport_type", "departure_date"]
    search_fields = ["route__origin__name", "route__destination__name"]
