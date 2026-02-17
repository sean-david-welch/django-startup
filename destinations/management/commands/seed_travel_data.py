from datetime import date, timedelta
from decimal import Decimal
from django.core.management.base import BaseCommand
from destinations.models import City
from transport.models import TransportOperator, TransportRoute, TransportSchedule
from accommodation.models import Accommodation, AccommodationAvailability


class Command(BaseCommand):
    """Seed database with travel data."""

    help = "Populate database with cities, routes, and accommodations"

    def handle(self, *args, **options) -> None:
        """Execute seed command."""
        self.stdout.write("Starting database seeding...")
        self._create_cities()
        self._create_operators()
        self._create_routes_and_schedules()
        self._create_accommodations()
        self._create_availability()
        self.stdout.write(self.style.SUCCESS("Database seeding completed!"))

    def _create_cities(self) -> None:
        """Create major European cities."""
        cities_data = [
            {
                "name": "Paris",
                "country": "France",
                "country_code": "FR",
                "latitude": Decimal("48.8566"),
                "longitude": Decimal("2.3522"),
                "timezone": "Europe/Paris",
                "popularity_score": 95,
                "tourist_attractions_count": 50,
            },
            {
                "name": "London",
                "country": "United Kingdom",
                "country_code": "GB",
                "latitude": Decimal("51.5074"),
                "longitude": Decimal("-0.1278"),
                "timezone": "Europe/London",
                "popularity_score": 92,
                "tourist_attractions_count": 45,
            },
            {
                "name": "Berlin",
                "country": "Germany",
                "country_code": "DE",
                "latitude": Decimal("52.5200"),
                "longitude": Decimal("13.4050"),
                "timezone": "Europe/Berlin",
                "popularity_score": 88,
                "tourist_attractions_count": 40,
            },
            {
                "name": "Rome",
                "country": "Italy",
                "country_code": "IT",
                "latitude": Decimal("41.9028"),
                "longitude": Decimal("12.4964"),
                "timezone": "Europe/Rome",
                "popularity_score": 96,
                "tourist_attractions_count": 60,
            },
            {
                "name": "Amsterdam",
                "country": "Netherlands",
                "country_code": "NL",
                "latitude": Decimal("52.3676"),
                "longitude": Decimal("4.9041"),
                "timezone": "Europe/Amsterdam",
                "popularity_score": 85,
                "tourist_attractions_count": 35,
            },
            {
                "name": "Barcelona",
                "country": "Spain",
                "country_code": "ES",
                "latitude": Decimal("41.3851"),
                "longitude": Decimal("2.1734"),
                "timezone": "Europe/Madrid",
                "popularity_score": 90,
                "tourist_attractions_count": 42,
            },
        ]

        for city_data in cities_data:
            City.objects.get_or_create(**city_data)

        self.stdout.write(self.style.SUCCESS(f"✓ Created {len(cities_data)} cities"))

    def _create_operators(self) -> None:
        """Create transport operators."""
        operators_data = [
            {
                "name": "Lufthansa",
                "operator_type": "AIRLINE",
                "website": "https://www.lufthansa.com",
            },
            {
                "name": "Ryanair",
                "operator_type": "AIRLINE",
                "website": "https://www.ryanair.com",
            },
            {
                "name": "SNCF",
                "operator_type": "TRAIN",
                "website": "https://www.sncf.com",
            },
            {
                "name": "Eurostar",
                "operator_type": "TRAIN",
                "website": "https://www.eurostar.com",
            },
            {
                "name": "FlixBus",
                "operator_type": "BUS",
                "website": "https://www.flixbus.com",
            },
        ]

        for op_data in operators_data:
            TransportOperator.objects.get_or_create(**op_data)

        self.stdout.write(self.style.SUCCESS(f"✓ Created {len(operators_data)} operators"))

    def _create_routes_and_schedules(self) -> None:
        """Create transport routes with schedules."""
        cities = {city.name: city for city in City.objects.all()}
        operators = {op.name: op for op in TransportOperator.objects.all()}

        routes_data = [
            {
                "operator": operators["Lufthansa"],
                "origin": cities["Paris"],
                "destination": cities["Berlin"],
                "transport_type": "FLIGHT",
                "route_code": "LH100",
                "origin_station": "CDG Airport",
                "destination_station": "BER Airport",
            },
            {
                "operator": operators["SNCF"],
                "origin": cities["Paris"],
                "destination": cities["Amsterdam"],
                "transport_type": "TRAIN",
                "route_code": "TGV200",
                "origin_station": "Paris Gare du Nord",
                "destination_station": "Amsterdam Centraal",
            },
            {
                "operator": operators["Ryanair"],
                "origin": cities["London"],
                "destination": cities["Barcelona"],
                "transport_type": "FLIGHT",
                "route_code": "FR500",
                "origin_station": "Stansted Airport",
                "destination_station": "Barcelona-El Prat",
            },
            {
                "operator": operators["Eurostar"],
                "origin": cities["London"],
                "destination": cities["Paris"],
                "transport_type": "TRAIN",
                "route_code": "ES300",
                "origin_station": "London St Pancras",
                "destination_station": "Paris Gare du Nord",
            },
        ]

        for route_data in routes_data:
            route, _ = TransportRoute.objects.get_or_create(**route_data)
            self._create_schedules(route)

        self.stdout.write(self.style.SUCCESS(f"✓ Created {len(routes_data)} routes"))

    def _create_schedules(self, route: TransportRoute) -> None:
        """Create schedules for a route."""
        schedules_data = [
            {
                "route": route,
                "departure_time": "08:00:00",
                "arrival_time": "10:30:00",
                "duration_minutes": 150,
                "base_price": Decimal("120.00"),
                "valid_from": date.today(),
                "valid_until": date.today() + timedelta(days=365),
            },
            {
                "route": route,
                "departure_time": "14:00:00",
                "arrival_time": "16:30:00",
                "duration_minutes": 150,
                "base_price": Decimal("100.00"),
                "valid_from": date.today(),
                "valid_until": date.today() + timedelta(days=365),
            },
        ]

        for schedule_data in schedules_data:
            TransportSchedule.objects.get_or_create(**schedule_data)

    def _create_accommodations(self) -> None:
        """Create accommodations in cities."""
        cities = {city.name: city for city in City.objects.all()}

        accommodations_data = [
            {
                "city": cities["Paris"],
                "name": "Hotel Eiffel Tower",
                "accommodation_type": "HOTEL",
                "base_price": Decimal("150.00"),
                "star_rating": Decimal("4.5"),
                "has_wifi": True,
                "has_breakfast": True,
            },
            {
                "city": cities["Paris"],
                "name": "Hostel Paris Central",
                "accommodation_type": "HOSTEL",
                "base_price": Decimal("35.00"),
                "star_rating": Decimal("4.0"),
                "has_wifi": True,
            },
            {
                "city": cities["London"],
                "name": "Westminster Hotel",
                "accommodation_type": "HOTEL",
                "base_price": Decimal("140.00"),
                "star_rating": Decimal("4.0"),
                "has_wifi": True,
                "has_parking": True,
            },
            {
                "city": cities["Berlin"],
                "name": "Berlin Boutique Hotel",
                "accommodation_type": "HOTEL",
                "base_price": Decimal("90.00"),
                "star_rating": Decimal("4.2"),
                "has_wifi": True,
            },
            {
                "city": cities["Rome"],
                "name": "Colosseum Hotel",
                "accommodation_type": "HOTEL",
                "base_price": Decimal("160.00"),
                "star_rating": Decimal("4.6"),
                "has_wifi": True,
                "has_breakfast": True,
            },
            {
                "city": cities["Amsterdam"],
                "name": "Canal Apartment",
                "accommodation_type": "APARTMENT",
                "base_price": Decimal("120.00"),
                "star_rating": Decimal("4.3"),
                "has_wifi": True,
            },
        ]

        for acc_data in accommodations_data:
            Accommodation.objects.get_or_create(**acc_data)

        self.stdout.write(self.style.SUCCESS(f"✓ Created {len(accommodations_data)} accommodations"))

    def _create_availability(self) -> None:
        """Create availability records for next 90 days."""
        accommodations = Accommodation.objects.all()
        start_date = date.today()
        end_date = start_date + timedelta(days=90)

        total_created = 0
        for accommodation in accommodations:
            current_date = start_date
            while current_date <= end_date:
                AccommodationAvailability.objects.get_or_create(
                    accommodation=accommodation,
                    date=current_date,
                    defaults={"is_available": True, "rooms_available": 10},
                )
                current_date += timedelta(days=1)
                total_created += 1

        self.stdout.write(self.style.SUCCESS(f"✓ Created {total_created} availability records"))
