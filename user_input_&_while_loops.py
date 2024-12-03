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
