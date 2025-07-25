import random
from car import Car

class UnreliableCar(Car):
    """A car that might not drive depending on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with name, fuel, and reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if it passes the reliability check."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0