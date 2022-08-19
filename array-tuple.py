# Creating a tuple.
fruits = ('apple', 'banana', 'orange', 'cashew', 'pawpaw')

# Printing the tuple.
print(fruits)

# Printing the type of the variable `fruits`.
print(type(fruits))

# Printing the length of the tuple.
print(len(fruits))

# Printing the third element in the tuple.
print(fruits[2])

# Printing the third element from the end of the tuple to the second element from the end of the
# tuple.
print(fruits[-3:-1])

#tuple does not support item assignment
# fruits[1] = 'orange'

# Converting the tuple `fruits` to a list.
a = list(fruits)

# Assigning the value `'watermelon'` to the second element in the list `a`.
a[1] = 'watermelon'

# Printing the list `a`.
print("This is the new list", a)

# Creating a tuple with one element.
addition = ('melon',)

# Concatenating the tuple `fruits` with the tuple `addition`.
new = fruits + addition

print(new)