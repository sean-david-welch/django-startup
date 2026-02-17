from decimal import Decimal
from django.db import models
from destinations.models.city import City


class CityPair(models.Model):
    """Pre-calculated metadata about traveling between two cities."""

    from_city: City = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="routes_from"
    )
    to_city: City = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="routes_to"
    )

    # Distance & Travel Metadata
    distance_km: Decimal = models.DecimalField(
        max_digits=8, decimal_places=2, help_text="Direct distance in kilometers"
    )
    min_travel_hours: Decimal = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Minimum travel time in hours"
    )

    # Interest Score for Multi-City Routes
    intermediate_interest_score: int = models.IntegerField(default=0)

    # Caching
    has_direct_transport: bool = models.BooleanField(default=False)
    cheapest_direct_price: Decimal = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "city_pairs"
        unique_together = [["from_city", "to_city"]]
        indexes = [
            models.Index(fields=["from_city", "to_city"]),
            models.Index(fields=["has_direct_transport"]),
        ]

    def __str__(self) -> str:
        return f"{self.from_city.name} → {self.to_city.name}"
