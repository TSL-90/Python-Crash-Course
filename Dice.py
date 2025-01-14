"""Using the standard library to model a playing die."""
# 9-13 Dice

import random
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


# 9-14 Lottery

# from random import randint

# import random (saves to top of file)

characters = ['A', 'B', 'C', 'D', 'E', '1', '2', '3',
              '4', '5', '6', '7', '8', '9', '10']

random_selection = [characters[random.randint(0, len(characters) - 1)]
                    for _ in range(4)]
# '_' is a name used when you don’t care about the loop variable

result = ''.join(random_selection)

print("The winning characters are:", result)

# ALTERNATE
# import random
# characters = ['A', 'B', 'C', 'D', 'E', '1', '2', '3',
#              '4', '5', '6', '7', '8', '9', '10']
# random_selection = random.choices(characters, k=4)
# result = ''.join(random_selection)
# print("Randomly selected characters:", result)

# ALTERNATE
# import random
# characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
# 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
# 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
# '4', '5', '6', '7', '8', '9']

# Initialize an empty list to store the random selections
# random_selection = []

# Loop 4 times to select 4 random characters
# for _ in range(4):
# Generate a random index
# random_index = random.randint(0, len(characters) - 1)
# Append the character at the random index to the list
# random_selection.append(characters[random_index])

# Combine the selected characters into a string (optional)
# result = ''.join(random_selection)

# print("Randomly selected characters:", result)


# 9-15 Lottery Ticket
# import random #(saves to top of file)

characters = ['A', 'B', 'C', 'D', 'E', '1', '2', '3',
              '4', '5', '6', '7', '8', '9', '10']

winning_ticket = [characters[random.randint(0, len(characters) - 1)]
                  for _ in range(4)]
winning_result = ''.join(winning_ticket)
print("The winning characters are:", winning_result)

my_ticket = []
attempts = 0

while my_ticket != winning_ticket:

    my_ticket = [characters[random.randint(0, len(characters) - 1)]
                 for _ in range(4)]
    attempts += 1


print(f"You won after {attempts} attempts! Your ticket: {''.join(my_ticket)}")
