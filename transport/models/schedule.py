from datetime import time
from decimal import Decimal
from django.db import models
from transport.models.base import PriceableEntity
from transport.models.route import TransportRoute


class TransportSchedule(PriceableEntity):
    """Represents a specific scheduled departure for a route."""

    route: TransportRoute = models.ForeignKey(
        TransportRoute, on_delete=models.CASCADE, related_name="schedules"
    )

    # Schedule Information
    departure_time: time = models.TimeField(help_text="Daily departure time")
    arrival_time: time = models.TimeField(help_text="Daily arrival time")
    duration_minutes: int = models.PositiveIntegerField()

    # Frequency (which days this schedule operates)
    operates_monday: bool = models.BooleanField(default=True)
    operates_tuesday: bool = models.BooleanField(default=True)
    operates_wednesday: bool = models.BooleanField(default=True)
    operates_thursday: bool = models.BooleanField(default=True)
    operates_friday: bool = models.BooleanField(default=True)
    operates_saturday: bool = models.BooleanField(default=True)
    operates_sunday: bool = models.BooleanField(default=True)

    # Validity Period
    valid_from: models.DateField = models.DateField()
    valid_until: models.DateField = models.DateField(null=True, blank=True)

    # Capacity & Availability
    total_capacity: int = models.PositiveIntegerField(default=100)
    remaining_capacity: int = models.PositiveIntegerField(default=100)

    # Status
    is_active: bool = models.BooleanField(default=True)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "transport_schedules"
        indexes = [
            models.Index(fields=["route", "departure_time"]),
            models.Index(fields=["valid_from", "valid_until"]),
            models.Index(fields=["is_active", "base_price"]),
            models.Index(fields=["route", "is_active", "base_price"]),
        ]
        ordering = ["departure_time"]

    def __str__(self) -> str:
        return f"{self.route} at {self.departure_time}"

    def get_effective_price(self) -> Decimal:
        """Calculate effective price (can add dynamic pricing later)."""
        return self.base_price

    def operates_on_day(self, day_of_week: int) -> bool:
        """Check if schedule operates on given day (0=Monday, 6=Sunday)."""
        day_map = {
            0: self.operates_monday,
            1: self.operates_tuesday,
            2: self.operates_wednesday,
            3: self.operates_thursday,
            4: self.operates_friday,
            5: self.operates_saturday,
            6: self.operates_sunday,
        }
        return day_map.get(day_of_week, False)
