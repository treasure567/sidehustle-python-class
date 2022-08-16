# Creating a dictionary called school.
school = {
    'name': 'Trenalyze',
    'location': 'Lagos',
    'population': 780,
    'annual_revenus': 120000
}

# Printing the dictionary.
print(school)

# Printing the type of the variable school.
print(type(school))

# Printing the value of the key 'name' in the dictionary school.
print(school['name'])

# Printing the value of the key 'location' in the dictionary school.
print(school.get('location'))

# It prints the keys of the dictionary.
print(school.keys())

# It prints the values of the dictionary.
print(school.values())

# Changing the value of the key 'name' in the dictionary school.
school['name'] = 'Trenalyze Academy'

# It prints the dictionary.
print(school)

# It prints the items of the dictionary.
print (school.items())

# Adding a new key-value pair to the dictionary.
school.update({'name': 'Trenalyze Coding Academy'})

# It prints the dictionary.
print(school)

# Adding a new key-value pair to the dictionary.
school['owner'] = 'Treasure Uvietobore'

# It prints the dictionary.
print(school)

# Removing the key-value pair with the key 'annual_revenus' from the dictionary.
school.pop('annual_revenus')

# It prints the dictionary.
print(school)

school.popitem()

print(school)