from decimal import Decimal
from django.core.management.base import BaseCommand
from destinations.services import TravelDataGenerator, CityData


class Command(BaseCommand):
    """Seed database with realistic travel data."""

    help = "Generate realistic travel data with distance-based pricing"

    def handle(self, *args, **options) -> None:
        """Execute seed command."""
        self.stdout.write("Generating travel data...")

        cities = self._get_cities_data()
        generator = TravelDataGenerator(cities)
        generator.generate()

        self.stdout.write(self.style.SUCCESS("✓ Cities created"))
        self.stdout.write(self.style.SUCCESS("✓ Transport operators created"))
        self.stdout.write(
            self.style.SUCCESS("✓ Routes and schedules created (distance-based pricing)")
        )
        self.stdout.write(self.style.SUCCESS("✓ Accommodations created"))
        self.stdout.write(self.style.SUCCESS("✓ Availability data created (180 days)"))
        self.stdout.write("\n" + self.style.SUCCESS("Database seeding completed!"))

    def _get_cities_data(self) -> list[CityData]:
        """Define cities with coordinates and accommodation costs."""
        return [
            CityData(
                name="Paris",
                country="France",
                country_code="FR",
                latitude=Decimal("48.8566"),
                longitude=Decimal("2.3522"),
                timezone="Europe/Paris",
                avg_stay_cost=Decimal("120.00"),
                popularity_score=95,
            ),
            CityData(
                name="London",
                country="United Kingdom",
                country_code="GB",
                latitude=Decimal("51.5074"),
                longitude=Decimal("-0.1278"),
                timezone="Europe/London",
                avg_stay_cost=Decimal("130.00"),
                popularity_score=92,
            ),
            CityData(
                name="Berlin",
                country="Germany",
                country_code="DE",
                latitude=Decimal("52.5200"),
                longitude=Decimal("13.4050"),
                timezone="Europe/Berlin",
                avg_stay_cost=Decimal("85.00"),
                popularity_score=88,
            ),
            CityData(
                name="Rome",
                country="Italy",
                country_code="IT",
                latitude=Decimal("41.9028"),
                longitude=Decimal("12.4964"),
                timezone="Europe/Rome",
                avg_stay_cost=Decimal("100.00"),
                popularity_score=96,
            ),
            CityData(
                name="Amsterdam",
                country="Netherlands",
                country_code="NL",
                latitude=Decimal("52.3676"),
                longitude=Decimal("4.9041"),
                timezone="Europe/Amsterdam",
                avg_stay_cost=Decimal("110.00"),
                popularity_score=85,
            ),
            CityData(
                name="Barcelona",
                country="Spain",
                country_code="ES",
                latitude=Decimal("41.3851"),
                longitude=Decimal("2.1734"),
                timezone="Europe/Madrid",
                avg_stay_cost=Decimal("95.00"),
                popularity_score=90,
            ),
            CityData(
                name="Vienna",
                country="Austria",
                country_code="AT",
                latitude=Decimal("48.2082"),
                longitude=Decimal("16.3738"),
                timezone="Europe/Vienna",
                avg_stay_cost=Decimal("90.00"),
                popularity_score=82,
            ),
            CityData(
                name="Prague",
                country="Czech Republic",
                country_code="CZ",
                latitude=Decimal("50.0755"),
                longitude=Decimal("14.4378"),
                timezone="Europe/Prague",
                avg_stay_cost=Decimal("70.00"),
                popularity_score=80,
            ),
        ]
