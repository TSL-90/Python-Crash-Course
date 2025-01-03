message = input("Tell me something and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# using int() to covert strings into numbers
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("Welcome!")
else:
    print("Access denied!")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

# modulo operator just shows remainder
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

# 7-1 Rental Car
prompt = "What brand of car are you looking for today? "

car = input(prompt)
print(f"\nLet me see if I can find you a {car}!")

# 7-2 Seating
party = input("How many people are in your dinner group? ")
party = int(party)

if party > 8:
    print("You will need to wait while we get a table ready.")
else:
    print("A table is ready for you now.")

# 7-3 Multiples of Ten
number = input("Enter a number, and I'll tell you if it's a multiple of ten: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of ten.")
else:
    print(f"\nThe number {number} is not a multiple of ten.")

# while loops run as long as a condition is true
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1  # means current_number = current_number + 1

# parrot program
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# using a Flag allows a program to stop running when a 'false' event occurs
# flags are useful for complex programs
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True  # active is the flag name, it can be anything you want
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# cities program
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you have finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# counting
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# this loop runs forever! infinite loop
x = 1
while x <= 5:
    print(x)

# fixed
x = 1
while x <= 5:
    print(x)
    x += 1

# 7-4 pizza toppings
prompt = "\nPlease enter the each pizza topping you would like:"
prompt += "\n(Enter 'quit' when you have finished adding toppings.) "

while True:
    pizza = input(prompt)

    if pizza == 'quit':
        break
    else:
        print(f"We will add {pizza.title()} to your pizza!")

# 7-5 movie ticket
prompt = int(input("Please input your age: "))

if prompt < 3:
    print("Your ticket is free!")
elif 3 <= prompt < 13:
    print("Your ticket price is $10.")
else:
    print("Your ticket price is $15.")

# while loop with lists and dictionaries example
# Start with users that need to be verified,
#  and an empty list to hold confirmed users

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# mountain poll program
responses = {}
polling_active = True  # set a flag to indicate that polling is active
while polling_active:  # prompt for the persons name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response  # store the response in the dictionary
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n---Poll Results---")  # polling is complete, show the results
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
# note, the user can type ANYTHING but "no" and the code will proceed.

# 7-8 Deli & 7-9 No pastrami
sandwich_orders = ['philly', 'pastrami', 'pb&j', 'club', 'chopped cheese',
                   'pastrami']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("Sorry we are out of pastrami!")
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made your: {sandwich.title()}")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been made today.")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
