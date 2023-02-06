# Lists: ordered, mutable and allows duplicate elements

fruits = ['Apple', 'Banana', 'Orange']

print(fruits[0])  # start with index 0

print(len(fruits))  # Return the size or length of the list

if 'Apple' in fruits:  # Checking the existance
    print('Yes')
else:
    print('No')

# Iterating through list
for fruit in fruits:
    print(fruit)

# Inserting new elements into list
fruits.append('Grape')  # Add at the end
fruits.insert(3, 'Mango')  # Add at specific position
# we can append a list also

# Removing and getting the last element
print(fruits.pop())

# Removing specific element and getting it
print(fruits.remove('Banana'))  # but the element need to exist

# Removing all elements from the list
fruits.clear()

# Reversing the list
fruits.reverse()

# Sorting the list
fruits.sort()  # Inplace change
new_fruits = sorted(fruits)  # Not inplace change

# List creation and other operation
zeros = [0] * 5  # It will create a list of five 0
ones = [1] * 5  # It will create a list of five 1

# Adding two list together
zero_one = zeros + ones

# Slicing list
zero = zero_one[0:3]  # [start_index:enging_index(excluding):steps]
print(zero)

# Copying list
new_fruits = fruits

# Now if we change new_fruits list then fruits list also get changed
# Because both refer same memory location

# Copying without same reference
new_fruits = fruits.copy()

# List comprehension
fruit = [fruit for fruit in fruits]
print(fruit)
