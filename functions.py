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

# 8-3 T-Shirt


def make_shirt(shirt_size, message):
    """Display shirt details"""
    print(f"\nThe shirt size selected is {shirt_size}.")
    print(f"The shirt will say, {message}")


make_shirt(shirt_size="4T", message="'I can't fucking read'")

# Return Values


def get_formatted_name(first_name, last_name):
    """Return full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Return a dictionary


def build_person(first_name, last_name, age=None):  # None is a 'special value'
    """Return a dictionary with info about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# Function in a while loop


def get_formatted_name(first_name, last_name):
    """Return full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# 8-6 City Names


def city_state(city, state):
    """Return the city and state."""
    full_location = f"{city} {state}"
    return full_location.title()


location = city_state('albuquerque,', 'new mexico')
print(location)

# 8-7 Album


def make_album(artist_name, album_name):
    """Return album details."""
    album = {'artist': artist_name, 'album': album_name}
    return album


record = make_album('maynard james keenan', 'emotive')
print(record)

# 8-8


def make_album(album_name, artist_name):
    """Return album details."""
    artist = artist_name.title()
    album = album_name.title()
    return f"{artist} by {album}"


while True:
    print("\nPlease tell me your favorite artist and album:")
    print("(Enter 'q' at any time to quit)")

    artist_name = input("Artist: ")
    if artist_name.lower() == 'q':
        break

    album_name = input("Album: ")
    if album_name.lower() == 'q':
        break

    record = make_album(artist_name, album_name)
    print(f"\nYour favorite album is {record}.")
