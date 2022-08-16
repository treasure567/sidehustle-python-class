fruits = ['banana', 'apple', 'pawpaw', 'lemon']
print(fruits)

counter = 0
for i in fruits:
    counter += 1
    if i == 'pawpaw':
        print('Key Found!')
        print(i)
        continue
    print(counter)

i = 0
while i <= len(fruits):
    i += 1
    print(i)
