from django.contrib import admin
from destinations.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "country", "popularity_score", "is_active"]
    list_filter = ["country", "is_active"]
    search_fields = ["name", "country"]
