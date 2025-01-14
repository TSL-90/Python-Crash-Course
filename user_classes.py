"""A class that can be used to represent users."""


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
