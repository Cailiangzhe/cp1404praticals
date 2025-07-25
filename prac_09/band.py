class Band:
    """Band class - A band has a name and a list of musicians."""

    def __init__(self, name):
        """Initialise Band with name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a Musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return string representation of the Band and its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        """Return a string showing each musician playing."""
        return '\n'.join(musician.play() for musician in self.musicians)