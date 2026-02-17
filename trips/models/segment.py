from decimal import Decimal
from django.db import models
from destinations.models.city import City
from transport.models.schedule import TransportSchedule
from accommodation.models.accommodation import Accommodation
from trips.models.itinerary import TripItinerary


class ItinerarySegment(models.Model):
    """Represents one segment/leg of a trip itinerary."""

    itinerary: TripItinerary = models.ForeignKey(
        TripItinerary, on_delete=models.CASCADE, related_name="segments"
    )

    # Segment Order
    sequence_number: int = models.PositiveIntegerField()

    # City Information
    city: City = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="itinerary_segments"
    )

    # Transport TO this city (null for first segment)
    transport_schedule: TransportSchedule = models.ForeignKey(
        TransportSchedule,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="itinerary_segments",
    )
    transport_date: models.DateField = models.DateField(
        null=True, blank=True, help_text="Date of transport departure"
    )
    transport_cost: Decimal = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )

    # Stay in this city
    accommodation: Accommodation = models.ForeignKey(
        Accommodation,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="itinerary_segments",
    )
    check_in_date: models.DateField = models.DateField()
    check_out_date: models.DateField = models.DateField()
    nights_count: int = models.PositiveIntegerField()
    accommodation_cost: Decimal = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )

    # Segment Totals
    segment_total_cost: Decimal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "itinerary_segments"
        unique_together = [["itinerary", "sequence_number"]]
        indexes = [
            models.Index(fields=["itinerary", "sequence_number"]),
            models.Index(fields=["city"]),
            models.Index(fields=["check_in_date", "check_out_date"]),
        ]
        ordering = ["itinerary", "sequence_number"]

    def __str__(self) -> str:
        return f"Segment {self.sequence_number}: {self.city.name}"
