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
