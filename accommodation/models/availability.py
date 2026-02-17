from django.db import models
from accommodation.models.accommodation import Accommodation


class AccommodationAvailability(models.Model):
    """Tracks date-specific availability and pricing for accommodations."""

    accommodation: Accommodation = models.ForeignKey(
        Accommodation, on_delete=models.CASCADE, related_name="availability_records"
    )

    date: models.DateField = models.DateField()
    is_available: bool = models.BooleanField(default=True)
    rooms_available: int = models.PositiveIntegerField(default=10)

    # Optional: date-specific pricing override
    override_price: models.DecimalField = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "accommodation_availability"
        unique_together = [["accommodation", "date"]]
        indexes = [
            models.Index(fields=["accommodation", "date", "is_available"]),
            models.Index(fields=["date", "is_available"]),
        ]
        ordering = ["date"]

    def __str__(self) -> str:
        return f"{self.accommodation.name} on {self.date}"
