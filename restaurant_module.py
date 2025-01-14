"""A class that can be used to represent a restaurant."""


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
