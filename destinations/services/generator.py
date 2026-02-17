import random
from datetime import date, timedelta, time
from decimal import Decimal
from typing import NamedTuple
from math import radians, cos, sin, asin, sqrt
from destinations.models import City
from transport.models import TransportOperator, TransportRoute, TransportSchedule
from accommodation.models import Accommodation, AccommodationAvailability


class CityData(NamedTuple):
    """Data structure for city input."""

    name: str
    country: str
    country_code: str
    latitude: Decimal
    longitude: Decimal
    timezone: str
    avg_stay_cost: Decimal
    popularity_score: int


class TravelDataGenerator:
    """Generates realistic travel data with distance-based pricing."""

    def __init__(self, cities_data: list[CityData]) -> None:
        """Initialize generator with cities data."""
        self.cities_data = cities_data
        self.cities: dict[str, City] = {}
        self.operators: dict[str, TransportOperator] = {}

    def generate(self) -> None:
        """Generate all travel data."""
        self._create_cities()
        self._create_operators()
        self._create_routes_and_schedules()
        self._create_accommodations()
        self._create_availability()

    def _create_cities(self) -> None:
        """Create cities from input data."""
        for city_data in self.cities_data:
            city = City.objects.create(
                name=city_data.name,
                country=city_data.country,
                country_code=city_data.country_code,
                latitude=city_data.latitude,
                longitude=city_data.longitude,
                timezone=city_data.timezone,
                popularity_score=city_data.popularity_score,
                tourist_attractions_count=random.randint(20, 80),
                average_stay_days=random.randint(2, 5),
            )
            self.cities[city_data.name] = city

    def _create_operators(self) -> None:
        """Create transport operators."""
        operators_data = [
            ("Lufthansa", "AIRLINE"),
            ("Ryanair", "AIRLINE"),
            ("British Airways", "AIRLINE"),
            ("SNCF", "TRAIN"),
            ("Eurostar", "TRAIN"),
            ("FlixBus", "BUS"),
        ]

        for name, op_type in operators_data:
            operator = TransportOperator.objects.create(
                name=name, operator_type=op_type
            )
            self.operators[name] = operator

    def _create_routes_and_schedules(self) -> None:
        """Create routes between all city pairs with schedules."""
        cities_list = list(self.cities.values())

        for i, origin in enumerate(cities_list):
            for destination in cities_list[i + 1 :]:
                self._create_route_pair(origin, destination)

    def _create_route_pair(
        self, city_a: City, city_b: City
    ) -> None:
        """Create bidirectional routes between two cities."""
        self._create_directional_route(city_a, city_b)
        self._create_directional_route(city_b, city_a)

    def _create_directional_route(self, origin: City, destination: City) -> None:
        """Create route from origin to destination."""
        distance_km = self._calculate_distance(origin, destination)
        operator = random.choice(list(self.operators.values()))

        route = TransportRoute.objects.create(
            operator=operator,
            origin=origin,
            destination=destination,
            transport_type=self._select_transport_type(distance_km),
            route_code=f"{origin.country_code}-{destination.country_code}",
            origin_station=f"{origin.name} Central Station",
            destination_station=f"{destination.name} Central Station",
        )

        self._create_schedules(route, distance_km)

    def _create_schedules(self, route: TransportRoute, distance_km: float) -> None:
        """Create 3 schedules per route."""
        for _ in range(3):
            base_price = self._calculate_price(distance_km)
            departure_hour = random.randint(6, 20)

            TransportSchedule.objects.create(
                route=route,
                departure_time=time(hour=departure_hour, minute=random.choice([0, 15, 30, 45])),
                arrival_time=self._calculate_arrival_time(
                    departure_hour, distance_km
                ),
                duration_minutes=self._estimate_duration(distance_km),
                base_price=base_price,
                valid_from=date.today(),
                valid_until=date.today() + timedelta(days=365),
                operates_monday=True,
                operates_tuesday=True,
                operates_wednesday=True,
                operates_thursday=True,
                operates_friday=True,
                operates_saturday=random.choice([True, True, False]),
                operates_sunday=random.choice([True, False]),
            )

    def _create_accommodations(self) -> None:
        """Create accommodations in each city."""
        accommodation_types = [
            ("HOTEL", 2.0),
            ("HOTEL", 1.5),
            ("HOSTEL", 0.3),
            ("APARTMENT", 0.8),
        ]

        for city_data in self.cities_data:
            city = self.cities[city_data.name]

            for acc_type, price_multiplier in accommodation_types:
                base_price = city_data.avg_stay_cost * Decimal(str(price_multiplier))

                Accommodation.objects.create(
                    city=city,
                    name=f"{city.name} {acc_type} {random.randint(1, 5)}",
                    accommodation_type=acc_type,
                    base_price=base_price,
                    star_rating=Decimal(str(round(random.uniform(3.5, 4.8), 1))),
                    review_score=Decimal(str(round(random.uniform(7.5, 9.8), 1))),
                    has_wifi=random.choice([True, True, True, False]),
                    has_breakfast=random.choice([True, True, False]),
                    has_parking=random.choice([True, False, False]),
                )

    def _create_availability(self) -> None:
        """Create 180 days of availability."""
        accommodations = Accommodation.objects.all()
        start_date = date.today()

        for accommodation in accommodations:
            for day_offset in range(180):
                current_date = start_date + timedelta(days=day_offset)

                AccommodationAvailability.objects.create(
                    accommodation=accommodation,
                    date=current_date,
                    is_available=random.random() > 0.1,
                    rooms_available=random.randint(3, 15),
                )

    def _calculate_distance(self, city_a: City, city_b: City) -> float:
        """Calculate great-circle distance between cities in km."""
        lon1 = float(city_a.longitude)
        lat1 = float(city_a.latitude)
        lon2 = float(city_b.longitude)
        lat2 = float(city_b.latitude)

        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        km = 6371 * c

        return km

    def _calculate_price(self, distance_km: float) -> Decimal:
        """Calculate price based on distance + normal distribution noise."""
        base_rate = Decimal("0.08")
        base_price = Decimal(str(distance_km)) * base_rate
        noise = Decimal(str(random.gauss(0, distance_km * 0.05)))
        final_price = max(base_price + noise, Decimal("20.00"))

        return Decimal(str(round(float(final_price), 2)))

    def _select_transport_type(self, distance_km: float) -> str:
        """Select transport type based on distance."""
        if distance_km < 300:
            return random.choice(["TRAIN", "BUS", "TRAIN"])
        elif distance_km < 1000:
            return random.choice(["FLIGHT", "TRAIN", "FLIGHT"])
        else:
            return "FLIGHT"

    def _estimate_duration(self, distance_km: float) -> int:
        """Estimate travel duration in minutes."""
        if distance_km < 300:
            return int(distance_km / 100 * 60) + random.randint(-30, 30)
        elif distance_km < 1000:
            return int(distance_km / 150 * 60) + random.randint(-60, 60)
        else:
            return int(distance_km / 900 * 60) + random.randint(-45, 45)

    def _calculate_arrival_time(
        self, departure_hour: int, distance_km: float
    ) -> time:
        """Calculate arrival time based on departure and duration."""
        duration_minutes = self._estimate_duration(distance_km)
        arrival_minutes = departure_hour * 60 + duration_minutes
        arrival_hour = (arrival_minutes // 60) % 24
        arrival_minute = arrival_minutes % 60

        return time(hour=int(arrival_hour), minute=int(arrival_minute))
