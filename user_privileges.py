"""Classes that can be used to represent various users."""

from user_classes import User


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
