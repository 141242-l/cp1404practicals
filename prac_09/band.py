class Band:
    """Band class to represent a band made up of musicians."""

    def __init__(self, name=""):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.members = []