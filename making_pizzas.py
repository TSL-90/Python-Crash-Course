import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'bell pepper', 'extra cheese')

# importing a specific function or functions
# from pizza import make_pizza
# make_pizza(16, 'pineapple')
# make_pizza(12, 'pepperoni', 'green chile')

# giving the import name an alias
# from pizza import pizza as mp
# mp(16, 'pineapple')
# mp(12, 'pepperoni', 'green chile')

# giving the module name an alias
# import pizza as p
# p.make_pizza(16, 'pineapple')
# p.make_pizza(12, 'pepperoni', 'green chile')

# importing all functions in a module (best not to do this)
# from pizza import *
# make_pizza(16, 'pineapple')
# make_pizza(12, 'pepperoni', 'green chile')
# it allows you to call each function in a module without the '.' prefix
