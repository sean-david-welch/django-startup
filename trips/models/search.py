from datetime import date
from django.db import models
from destinations.models.city import City


class TripSearch(models.Model):
    """Represents a guest search query for trip planning."""

    # Origin & Destination
    start_city: City = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="trips_starting_here"
    )
    end_city: City = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="trips_ending_here"
    )

    # Trip Parameters
    total_days: int = models.PositiveIntegerField()

    # Date Flexibility
    is_date_flexible: bool = models.BooleanField(
        default=True, help_text="Whether dates are flexible or fixed"
    )
    preferred_start_date: models.DateField = models.DateField(
        null=True, blank=True, help_text="If date NOT flexible, the fixed start date"
    )

    # Search Constraints
    max_intermediate_cities: int = models.PositiveIntegerField(default=3)
    max_budget: models.DecimalField = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    # Preferences
    preferred_transport_types: str = models.CharField(
        max_length=255, blank=True, help_text="Comma-separated transport types"
    )
    preferred_accommodation_types: str = models.CharField(
        max_length=255, blank=True, help_text="Comma-separated accommodation types"
    )

    # Session & Analytics
    session_id: str = models.CharField(
        max_length=255, blank=True, help_text="Guest session identifier"
    )
    ip_address: str = models.GenericIPAddressField(null=True, blank=True)

    # Timestamps
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "trip_searches"
        indexes = [
            models.Index(fields=["start_city", "end_city"]),
            models.Index(fields=["session_id", "-created_at"]),
            models.Index(fields=["-created_at"]),
        ]
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.start_city.name} to {self.end_city.name} ({self.total_days} days)"
