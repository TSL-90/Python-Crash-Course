"""This chapter covers Object-oriented programming (OOP)."""


class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributs."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Max', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()


# 9-1 Restaurant 9-2 Three Restaurants

class Restaurant:
    """A simple restaurant model."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and food type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Provide a message say that the restaurant is now open."""
        print(f"{self.restaurant_name} is now open!")


my_restaurant = Restaurant("NM's best subs", "Sandwiches")
best_voted_restaurant = Restaurant("Savoy", "Italian Cuisine")
worst_in_town = Restaurant("Golden Pride", "Breakfast Burritos")

print(f"{my_restaurant.restaurant_name} is a tasty spot to eat!")
my_restaurant.describe_restaurant()
best_voted_restaurant.describe_restaurant()
worst_in_town.describe_restaurant()


# 9-3 Users

class User:
    """Create a user model."""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize user attributs."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        """Provide user details."""
        print(f"{self.first_name} {self.last_name} is a "
              f"{self.age}-year old {self.gender}.")

    def greet_user(self):
        """Output a user greeting."""
        print(f"\nHello {self.first_name} {self.last_name}, "
              f"welcome to your new profile.")


user_tyson = User('Tyson', 'Lanier', '34', 'male')
user_david = User('David', 'Bowie', '39', 'non binary')
user_tonks = User('Tonks', 'Nymphadora', '24', 'female')
user_cyborg = User('Victor', 'Stone', '18', 'cyborg')

user_tyson.greet_user()
user_tyson.describe_user()

user_david.greet_user()
user_david.describe_user()

user_tonks.greet_user()
user_tonks.describe_user()

user_cyborg.greet_user()
user_cyborg.describe_user()
