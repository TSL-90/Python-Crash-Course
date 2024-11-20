cars = ['audi', 'bmw', 'subaru', 'vw', 'toyota']
for car in cars:
    if car == 'bmw' or car == 'vw':
        print(car.upper())
    else:
        print(car.title())

boat = ['Toaster']
is_toaster = boat[0].lower() == 'toaster'
print(is_toaster)


vehicle = 'Audi'
vehicle.lower() == 'audi'

answer = 23
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 20
if age < 21:
    print("Access Denied!")
else:
    print("Welcome!")

outside_temperature = 102
if outside_temperature < 60:
    print("It's a chilly day today, bring a coat!")
elif outside_temperature > 85:
    print("It's a hot day, make sure to hydrate!")
else:
    print("It's a nice day, enjoy the weather!")

age = 76
if age <= 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 30
elif age >= 65 and age <= 75:
    price = 20
else:
    price = 5

print(f"Your admission cost is ${price}.")

age = 75

match age:
    case age if age <= 4:
        price = "0"
    case age if age < 18:
        price = "25"
    case age if age < 65:
        price = "30"
    case age if 65 <= age <= 75:
        price = "20"
    case _:  # this is a catch all for unmatched conditions
        price = "5"
print(f"Your admission cost is ${price}.")

pizza_toppings = ['mushrooms', 'cheese', 'bell peppers']

if 'mushrooms':
    print("Add Mushrooms")
if 'bell peppers':
    print("Add Bell Peppers")
print("Finished making your pizza!")

# pizzera x2

available_toppings = ['mushrooms', 'bacon', 'bell peppers', 'pepperoni',
                      'pineapple', 'extra cheese', 'sausage']

requested_toppings = ['mushrooms', 'bacon', 'bell peppers', 'onion']

if not requested_toppings:
    print("Are you sure you only want a cheese pizza?")
else:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        if requested_topping not in available_toppings:
            print(f"Sorry, we don't have {requested_topping}.")

print("Finished making your pizza!")

# This is just testing the github connection. No changes have been made.
