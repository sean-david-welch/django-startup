from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from destinations.models.city import City
from transport.models.base import PriceableEntity


class Accommodation(PriceableEntity):
    """Represents a place to stay in a city."""

    city: City = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="accommodations"
    )

    # Basic Information
    name: str = models.CharField(max_length=255)
    accommodation_type: str = models.CharField(
        max_length=50,
        choices=[
            ("HOTEL", "Hotel"),
            ("HOSTEL", "Hostel"),
            ("APARTMENT", "Apartment"),
            ("GUESTHOUSE", "Guesthouse"),
            ("BNB", "Bed & Breakfast"),
        ],
    )

    # Location within City
    address: str = models.TextField(blank=True)
    neighborhood: str = models.CharField(max_length=255, blank=True)
    latitude: Decimal = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude: Decimal = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    # Quality Indicators
    star_rating: Decimal = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    review_score: Decimal = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    # Amenities
    has_wifi: bool = models.BooleanField(default=True)
    has_breakfast: bool = models.BooleanField(default=False)
    has_parking: bool = models.BooleanField(default=False)

    # Display
    description: str = models.TextField(blank=True)
    image_url: str = models.URLField(blank=True)

    # Metadata
    is_active: bool = models.BooleanField(default=True)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "accommodations"
        indexes = [
            models.Index(fields=["city", "is_active", "base_price"]),
            models.Index(fields=["city", "accommodation_type"]),
            models.Index(fields=["-review_score"]),
        ]
        ordering = ["city", "base_price"]

    def __str__(self) -> str:
        return f"{self.name} ({self.city.name})"

    def get_effective_price(self) -> Decimal:
        """Calculate effective nightly price."""
        return self.base_price
