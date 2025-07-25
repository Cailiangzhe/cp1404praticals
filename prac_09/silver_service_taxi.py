from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A luxurious Taxi with fanciness multiplier and flagfall."""

    flagfall = 4.50
    def __init__(self, name, fuel, fanciness):
        """Initialise SilverServiceTaxi with name, fuel, and fanciness."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the fare, including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
