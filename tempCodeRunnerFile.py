from random import randint


class Die():
    """Model a roll of the dice."""

    def __init__(self, sides=6):
        """Initialize number of sides on a die."""
        self.sides = sides

    def roll_die(self):
        """Roll the die with and return a random output."""
        return randint(1, self.sides)  # self.sides == default value in init


die_1 = Die()

roll_result = die_1.roll_die()
print(f"The die rolled a {roll_result}.")