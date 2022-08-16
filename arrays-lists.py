# Creating a list of fruits.
fruits = ['apple', 'banana', 'cherry', 'lemon', 'pawpaw']

# Printing the list of fruits.
print(fruits)

# Printing the type of the variable fruits.
print(type(fruits))

# Printing the length of the list.
print(len(fruits))

# Printing the third element of the list.
print(fruits[2])

# Printing the second to the fifth element of the list.
print(fruits[1:5])

# Assigning the value of the second element of the list to the variable a.
a = fruits[1] = 'orange'

# Printing the string "This is a new list:" and the list fruits.
print("This is a new list:", fruits)

# Adding the string 'carrot' to the list fruits.
b = fruits.append('carrot')

# Printing the list of fruits.
print(fruits)

# It removes the element 'lemon' from the list.
fruits.remove('lemon')

# It prints the list of fruits.
print(fruits)

# Creating an empty list.
fruits3 = []

# Creating a new list called fruits3 and adding the element 'carrot' to it.
for i in fruits:
    if 'carrot' in i:
        fruits3.append(i)
    else:
        continue

# It prints the list fruits3.
print(fruits3)

# Creating a new list called fruits4 and adding the element 'apple' to it using list comprehension.
fruits4 = [i for i in fruits if "apple" in i]

# It prints the list fruits4.
print(fruits4)