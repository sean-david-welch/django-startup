from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from common.models import ActivatableModel, GeolocatedModel, TimestampedModel


class City(ActivatableModel, GeolocatedModel, TimestampedModel):
    """Represents a city that can be part of a travel itinerary."""

    # Basic Information
    name: str = models.CharField(max_length=255, unique=True)
    country: str = models.CharField(max_length=100)
    country_code: str = models.CharField(max_length=2)  # ISO 3166-1 alpha-2

    # Geographic Data
    timezone: str = models.CharField(max_length=100)  # e.g., "Europe/Paris"

    # Tourism & Interest Metadata
    popularity_score: int = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Score from 0-100 indicating city popularity",
    )
    tourist_attractions_count: int = models.PositiveIntegerField(default=0)
    average_stay_days: int = models.PositiveIntegerField(
        default=2, help_text="Recommended days to spend in this city"
    )

    # Search & Display
    description: str = models.TextField(blank=True)
    image_url: str = models.URLField(blank=True)

    class Meta:
        db_table = "cities"
        verbose_name_plural = "Cities"
        ordering = ["-popularity_score", "name"]
        indexes = [
            models.Index(fields=["country", "name"]),
            models.Index(fields=["-popularity_score"]),
            models.Index(fields=["is_active", "-popularity_score"]),
        ]

    def __str__(self) -> str:
        return f"{self.name}, {self.country}"
