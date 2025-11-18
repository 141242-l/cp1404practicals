import random
from car import Car

class UnreliableCar(Car):
    """A car that does not always drive reliably, depending on a reliability percentage."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar, with reliability (0-100)."""
        super().__init__(name, fuel)
        self.reliability = reliability