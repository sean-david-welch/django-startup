from django.db import models


class TransportOperator(models.Model):
    """Represents a transport company/operator."""

    name: str = models.CharField(max_length=255, unique=True)
    operator_type: str = models.CharField(
        max_length=50,
        choices=[
            ("AIRLINE", "Airline"),
            ("TRAIN", "Train Operator"),
            ("BUS", "Bus Operator"),
            ("FERRY", "Ferry Operator"),
        ],
    )

    logo_url: str = models.URLField(blank=True)
    website: str = models.URLField(blank=True)

    is_active: bool = models.BooleanField(default=True)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "transport_operators"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
