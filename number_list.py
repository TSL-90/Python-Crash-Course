# two ways of writing the same number list

squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)


squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)


# same code w/ list comprehension***

squares = [value**2 for value in range(1, 11)]
print(squares)

# lesson 4-3

for numbers in range(1, 21):
    print(numbers)

# lesson 4-4, terminal truncates list due to length

millions = []
for value in range(0, 1000000):
    million = value + 1
    millions.append(million)
print(millions)

# alternate comprehension
millions = [value for value in range(0, 1000000)]
print(millions)
