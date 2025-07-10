CURRENT_YEAR = 2025
VINTAGE_AGE = 50

class Guitar:
    """Guitar class for storing details of guitar."""

    def __init__(self,name="",year=0, cost=0):
        """Initialise a Guitar."""
        self.name=name
        self.year=year
        self.cost=cost

    def __str__(self):
        """Return a string representation of a guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is over vintage or not."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Compare guitars by year."""
        return self.year < other.year