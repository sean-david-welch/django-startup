from abc import abstractmethod
from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class TimestampedModel(models.Model):
    """Abstract base class providing created_at and updated_at fields."""

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ActivatableModel(models.Model):
    """Abstract base class for models that can be activated/deactivated."""

    is_active: bool = models.BooleanField(default=True)

    class Meta:
        abstract = True


class GeolocatedModel(models.Model):
    """Abstract base class for models with geographic coordinates."""

    latitude: Decimal = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude: Decimal = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    class Meta:
        abstract = True


class PriceableEntity(models.Model):
    """Abstract base class for entities with pricing information."""

    base_price: Decimal = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Base price in EUR"
    )
    currency: str = models.CharField(
        max_length=3, default="EUR", help_text="ISO 4217 currency code"
    )

    class Meta:
        abstract = True

    @abstractmethod
    def get_effective_price(self) -> Decimal:
        """Calculate effective price considering modifiers."""
        pass
