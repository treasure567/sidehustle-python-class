# Creating a set.
fruits = {'apple', 'banana', 'pineapple', 'sugarcane'}

# Printing the set.
print (fruits)

# Printing the type of the variable fruits.
print (type(fruits))

# Iterating over the set and printing each element.
for a in fruits:
    print (a)

# Checking if the string 'apple' is in the set fruits.
# Printing the value of the key 'name' in the dictionary school.
print ('apple' in fruits)

# Adding the string 'pawpaw' to the set fruits.
fruits.add('pawpaw')

# Assigning the value of `fruits` to itself.
fruits = fruits

# Adding the string 'lemon' to the set fruits.
fruits.update(['lemon'])

# Removing the string 'apple' from the set `fruits`.
fruits.discard('apple')

# It removes the first element from the set.
fruits.pop()

# It removes all the elements from the set.
fruits.clear()

# Printing the set.
print (fruits)

# Creating two sets.
a = {1,3,4, 5,6,7,8}
b = {2,6,9,0,1,10, 3}

# Creating a new set `c` that contains all the elements of `a` and `b`.
c = a.union(b)

# Printing the set `c`.
print(c)

# Creating a new set `c` that contains all the elements that are in both `a` and `b`.
c =  a.intersection(b)

# Printing the set `c`.
print(c)




