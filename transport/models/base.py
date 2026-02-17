from abc import abstractmethod
from decimal import Decimal
from django.db import models


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
