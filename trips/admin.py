from django.contrib import admin
from trips.models import TripSearch, TripItinerary, ItinerarySegment


@admin.register(TripSearch)
class TripSearchAdmin(admin.ModelAdmin):
    list_display = ["start_city", "end_city", "total_days", "created_at"]
    list_filter = ["total_days", "created_at"]
    search_fields = ["start_city__name", "end_city__name"]


@admin.register(TripItinerary)
class TripItineraryAdmin(admin.ModelAdmin):
    list_display = ["search", "optimization_type", "rank", "total_cost"]
    list_filter = ["optimization_type", "rank"]
    search_fields = ["search__start_city__name", "search__end_city__name"]


@admin.register(ItinerarySegment)
class ItinerarySegmentAdmin(admin.ModelAdmin):
    list_display = ["itinerary", "sequence_number", "city", "segment_total_cost"]
    list_filter = ["city", "sequence_number"]
    search_fields = ["itinerary__search__start_city__name", "city__name"]
