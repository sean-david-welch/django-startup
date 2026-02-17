from datetime import timedelta
from decimal import Decimal
from django.db import models
from transport.models.base import PriceableEntity
from transport.models.route import TransportRoute


class TravelOption(PriceableEntity):
    """Represents a specific travel option with exact departure and arrival times."""

    route: TransportRoute = models.ForeignKey(
        TransportRoute, on_delete=models.CASCADE, related_name="travel_options"
    )

    # Departure Information
    departure_date: models.DateField = models.DateField(help_text="Departure date")
    departure_time: models.TimeField = models.TimeField(help_text="Departure time")

    # Arrival Information
    arrival_date: models.DateField = models.DateField(help_text="Arrival date")
    arrival_time: models.TimeField = models.TimeField(help_text="Arrival time")

    # Travel Duration
    total_travel_time: models.DurationField = models.DurationField(
        help_text="Total travel time duration"
    )

    # Status & Metadata
    is_active: bool = models.BooleanField(default=True)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "transport_travel_options"
        indexes = [
            models.Index(fields=["route", "departure_date"]),
            models.Index(fields=["departure_date", "is_active"]),
        ]
        ordering = ["departure_date", "departure_time"]

    def __str__(self) -> str:
        return f"{self.route} on {self.departure_date} at {self.departure_time}"

    def get_effective_price(self) -> Decimal:
        """Calculate effective price (can add dynamic pricing later)."""
        return self.base_price
