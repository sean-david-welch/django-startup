from decimal import Decimal
from django.db import models
from trips.models.search import TripSearch


class TripItinerary(models.Model):
    """Represents a calculated trip itinerary - a complete solution."""

    search: TripSearch = models.ForeignKey(
        TripSearch, on_delete=models.CASCADE, related_name="itineraries"
    )

    # Optimization Type
    optimization_type: str = models.CharField(
        max_length=50,
        choices=[
            ("CHEAPEST", "Lowest Total Cost"),
            ("FASTEST", "Shortest Travel Time"),
            ("BALANCED", "Balance of Cost and Time"),
            ("SCENIC", "Most Interesting Cities"),
        ],
        default="CHEAPEST",
    )

    # Calculated Totals
    total_cost: Decimal = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Total cost for all"
    )
    total_transport_cost: Decimal = models.DecimalField(max_digits=10, decimal_places=2)
    total_accommodation_cost: Decimal = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    total_travel_hours: Decimal = models.DecimalField(
        max_digits=6, decimal_places=2, help_text="Total hours in transit"
    )

    # Route Information
    cities_visited_count: int = models.PositiveIntegerField()
    cities_visited_order: str = models.TextField(
        help_text="JSON array of city IDs in visit order"
    )

    # Ranking & Selection
    rank: int = models.PositiveIntegerField(default=1)
    is_recommended: bool = models.BooleanField(default=False)

    # Calculation Metadata
    calculation_time_ms: int = models.PositiveIntegerField(null=True, blank=True)

    # Timestamps
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "trip_itineraries"
        indexes = [
            models.Index(fields=["search", "rank"]),
            models.Index(fields=["search", "optimization_type"]),
            models.Index(fields=["-created_at"]),
        ]
        ordering = ["search", "rank"]

    def __str__(self) -> str:
        return f"Itinerary #{self.rank} for {self.search} (€{self.total_cost})"
