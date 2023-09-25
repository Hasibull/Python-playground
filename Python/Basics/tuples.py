# Tuple: order, immutable, allows duplicate elements
# Creating tuple named animal
animal = ('cat', 'dog', 'rat')

# we can create it also as -
animal = 'cat', 'dog', 'rat'
print(type(animal))

# If we create a tuple with signle element then we should
# add a comma after the elemet unless it will considered as a single variable
animal = ('dog')
print(type(animal))  # considered as a string

animal = ('dog',)
print(type(animal))  # considered as a tuple
