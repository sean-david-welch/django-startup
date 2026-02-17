from django.contrib import admin
from destinations.models import City, CityPair


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "country", "popularity_score", "is_active"]
    list_filter = ["country", "is_active"]
    search_fields = ["name", "country"]


@admin.register(CityPair)
class CityPairAdmin(admin.ModelAdmin):
    list_display = ["from_city", "to_city", "distance_km", "has_direct_transport"]
    list_filter = ["has_direct_transport"]
    search_fields = ["from_city__name", "to_city__name"]
