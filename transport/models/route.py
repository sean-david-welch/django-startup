from django.db import models
from destinations.models.city import City
from transport.models.operator import TransportOperator


class TransportRoute(models.Model):
    """Represents a logical transport route between two cities."""

    operator: TransportOperator = models.ForeignKey(
        TransportOperator, on_delete=models.CASCADE, related_name="routes"
    )

    origin: City = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="departing_routes"
    )
    destination: City = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="arriving_routes"
    )

    # Route Metadata
    transport_type: str = models.CharField(
        max_length=20,
        choices=[
            ("FLIGHT", "Flight"),
            ("TRAIN", "Train"),
            ("BUS", "Bus"),
            ("FERRY", "Ferry"),
        ],
    )
    route_code: str = models.CharField(max_length=50, blank=True)

    # Departure/Arrival Points
    origin_station: str = models.CharField(max_length=255)
    destination_station: str = models.CharField(max_length=255)

    # Status
    is_active: bool = models.BooleanField(default=True)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "transport_routes"
        indexes = [
            models.Index(fields=["origin", "destination", "transport_type"]),
            models.Index(fields=["is_active"]),
            models.Index(fields=["operator", "is_active"]),
        ]
        unique_together = [["operator", "origin", "destination", "route_code"]]

    def __str__(self) -> str:
        return f"{self.origin.name} → {self.destination.name} ({self.transport_type})"
