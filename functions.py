"""Functions & Modules"""

# Display a simple greeting


def greet_user():  # "def" is tells python to define a function
    """ Display a simple greeting."""  # docstring describes the function
    print("Hello!")


greet_user()  # doesn't need info to work so () is empty


# another example

def hi_user(username):
    """ Display a simple greeting."""
    print(f"Hello, {username.title()}!")


hi_user('tyson')

# 8-1 Message


def display_message():
    """Display the chapter in progress"""
    print("I am learning chapter 8.")


display_message()

# 8-2 Favorite Book


def favorite_book(title):
    """Display the title of you favorite book."""
    print(f"One of my favorite books is {title.title()}.")


favorite_book("Alice in Wonderland")

# Positional Arguments (order matters)


def describe_pet(animal_type, pet_name):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('cockatiel', 'ether')
describe_pet('cockatiel', 'nike')  # you can call a function multiple times

# Keyword Arguments


def describe_pet(animal_type, pet_name):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='cockatiel', pet_name='ether')
describe_pet(pet_name='nike', animal_type='cockatiel')

# Default Value


def describe_pet(pet_name, animal_type='bird',):  # still a positional argument
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='ether')

# Equivalent Function Call (lets you overwrite a default argument)


def describe_pet(pet_name, animal_type='bird',):  # still a positional argument
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='fish', pet_name='loach')
describe_pet('loach', 'fish')  # both lines work the same
