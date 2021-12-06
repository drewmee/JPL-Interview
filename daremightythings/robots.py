"""Robots module."""


class Rover:
    """A planetary rover."""

    def __init__(self, manufacturer):
        """
        Args:
            manufacturer (string): The name of the rover's manufacturer.
        """
        self.manufacturer = manufacturer

    def land_on_mars(self):
        """A function to tell you whether or not your rover will successfully land on Mars.

        Args:
            rover (Rover object): The rover to be landed on mars.

        Returns:
            bool: The rover will either land successfully (True) or not (False).
        """
        if self.manufacturer == "JPL":
            success = True
        else:
            success = False
        return success
