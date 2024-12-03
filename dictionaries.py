"""Dictionarys"""

alien_0 = {'color': 'green', 'points': '5'}
print(alien_0['color'])
print(alien_0['points'])

# example use
alien_0 = {'color': 'green', 'points': '5'}

new_points = alien_0['points']
alien_color = alien_0['color']
print(f"You shot down a {alien_color} ship and earned {new_points} points!")

# adding to a dictionary
alien_0 = {'color': 'green', 'points': '5'}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# adding to an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = '5'
print(alien_0)

# modifying a dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

# example, tracking movement
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# removing key-value pairs (permanent!)
alien_0 = {'color': 'green', 'points': '5'}
print(alien_0)

del alien_0['points']
print(alien_0)

# similar objects
favorite_languages = {
    'jen': 'python',
    'bob': 'c',
    'tina': 'rust',
    'phil': 'java'
}
language = favorite_languages['jen'].title()
print(f"Jen's favorite language is {language}")

# no value get()
alien_0 = {'color': 'green', 'speed': 'slow'}  # missing 'points' : '5'

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# with value
alien_0 = {'color': 'green', 'points': '5', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# person example
best_friend = {
    'first_name': 'Fake',
    'last_name': 'Fakerson',
    'age': 34,
    'city': 'Santa Fe',
}
print(f"My best friend is {best_friend['first_name']} {
    best_friend['last_name']}. They live in {best_friend['city']}.")

# looping in dictionaries
user_0 = {
    'username': 'tsl90',
    'first': 'tyson',
    'last': 'lanier'
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# another example
favorite_languages = {
    'jen': 'python',
    'bob': 'c',
    'tina': 'rust',
    'phil': 'java'
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# looping through keys only, this is the default behavior
# calling the keys() method can make the code easier to read
favorite_languages = {
    'jen': 'python',
    'bob': 'c',
    'tina': 'rust',
    'phil': 'java'
}
for name in favorite_languages.keys():
    print(name.title())

# this is the same as above code but without the keys() method
favorite_languages = {
    'jen': 'python',
    'bob': 'c',
    'tina': 'rust',
    'phil': 'java'
}
for name in favorite_languages:
    print(name.title())

# use of set() data type to check for duplicates
favorite_languages = {
    'jen': 'python',
    'bob': 'c',
    'tina': 'rust',
    'phil': 'java',
    'edward': 'python',
    'alex': 'java',
    'collin': 'c'
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
for name in favorite_languages:
    print("Thank you for your response, " + name.title() + "!")

# nesting examples (dictionary inside a list)
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# empty list for storing aliens
aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

# list inside a dictionary
pizza = {
    'crust': 'deep dish',
    'toppings': ['cheese', 'sausage', 'bell peppers'],
}

# order summary (list in dictionary)
print(f"You ordered a {pizza['crust']} pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

# another example (list in dictionary)
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c', 'java'],
    'edward': ['rust', 'go'],
    'phil': ['c'],
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
        print(f"\t{languages[0].title()}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")

# dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
