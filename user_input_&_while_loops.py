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
