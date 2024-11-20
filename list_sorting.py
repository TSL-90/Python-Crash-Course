locations = ['london', 'iceland', 'alaska', 'new zeland', 'hawaii']
print(sorted(locations))

locations.reverse()
print(locations)

locations.reverse()
len(locations)
print(len(locations))

print("The first three items in the list are:")
for location in locations[:3]:
    print(location)
