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


# 9-1 Restaurant, 9-2 Three Restaurants, 9-4 Number Served

class Restaurant:
    """A simple restaurant model."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and food type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Provide a message say that the restaurant is now open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, customers):
        """Set the number of customers served."""
        self.number_served = customers

    def increment_number_served(self, customer):
        """Add the given customer volume tot the served output."""
        self.number_served += customer


my_restaurant = Restaurant("NM's best subs", "Sandwiches")
best_voted_restaurant = Restaurant("Savoy", "Italian Cuisine")
worst_in_town = Restaurant("Golden Pride", "Breakfast Burritos")
random_restaurant = Restaurant("Bob's Burgers", "Burgers")

random_restaurant.number_served = 106  # 9-4 step 1
random_restaurant.set_number_served(125)  # 9-4 step 2
random_restaurant.increment_number_served(63)  # 9-4 step 3

print(f"{random_restaurant.restaurant_name} has served "
      f"{random_restaurant.number_served} customers.")

print(f"{my_restaurant.restaurant_name} is a tasty spot to eat!")

my_restaurant.describe_restaurant()
best_voted_restaurant.describe_restaurant()
worst_in_town.describe_restaurant()


# 9-6 Ice Cream Stand (subclass of superclass Restaurant 9-4)

class IceCreamStand(Restaurant):
    """Create a specific type of restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initalize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def flavor(self):
        """Method that displays the flavors available."""
        print(f"We currently have {self.flavors} available.")


the_cream_shop = IceCreamStand('The Cream Shop', 'Ice Cream')

the_cream_shop.flavor()


# 9-3 Users, 9-5 Login Attempts

class User:  # this is a class
    """Create a user model."""

    def __init__(self, first_name, last_name, age, gender):
        # this is the initalizer method
        """Initialize user attributes."""
        self.first_name = first_name  # this is a required attribute
        self.last_name = last_name  # this is a required attribute
        self.age = age  # this is a required attribute
        self.gender = gender  # this is a required attribute
        self.login_attempts = 0
        # this is an instance attribute with a default value

    def describe_user(self):  # this is a method
        """Provide user details."""
        print(f"{self.first_name} {self.last_name} is a "
              f"{self.age}-year old {self.gender}.")

    def greet_user(self):  # this is a method
        """Output a user greeting."""
        print(f"\nHello {self.first_name} {self.last_name}, "
              f"welcome to your new profile.")

    def increment_login_attemps(self):  # this is a method
        """Increment the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):  # this is a method
        """Resets the number of login attempts to 0."""
        self.login_attempts = 0


user_tyson = User('Tyson', 'Lanier', '34', 'male')  # this is an instance
user_david = User('David', 'Bowie', '39', 'non binary')  # this is an instance
user_tonks = User('Tonks', 'Nymphadora', '24', 'female')  # this is an instance
user_cyborg = User('Victor', 'Stone', '18', 'cyborg')  # this is an instance

user_tyson.greet_user()
user_tyson.describe_user()
user_tyson.increment_login_attemps()
print(user_tyson.login_attempts)
user_tyson.increment_login_attemps()
print(user_tyson.login_attempts)
user_tyson.increment_login_attemps()
print(user_tyson.login_attempts)
user_tyson.increment_login_attemps()
print(user_tyson.login_attempts)
user_tyson.increment_login_attemps()
print(user_tyson.login_attempts)
user_tyson.increment_login_attemps()
print(user_tyson.login_attempts)
user_tyson.reset_login_attempts()
print(user_tyson.login_attempts)

user_david.greet_user()
user_david.describe_user()

user_tonks.greet_user()
user_tonks.describe_user()

user_cyborg.greet_user()
user_cyborg.describe_user()


# 9-8 Privileges

class Privileges:
    """Create an indipendent class for privileges."""

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = privileges

    def show_privileges(self):
        """Show a list of administrator privileges."""
        print(f"Administrator's can {self.privileges}.")

# 9-7 Admin (subclass of User superclass)


class Admin(User):
    """Create an admin class under users."""

    def __init__(self, first_name, last_name, age, gender):
        """Initalize attributes of the parent class User."""
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()

    def show_privileges(self):
        """Show a list of administrator privileges."""
        print(f"Administrator's can {self.privileges.show_privileges}.")


user_admin1 = Admin('Tony', 'Stark', '39', 'male')

user_admin1.privileges.show_privileges()
