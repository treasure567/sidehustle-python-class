try:
    a = int(input('Enter first Number: '))
    b = int(input('Enter second Number:' ))
    c = a / b
except ZeroDivisionError:
    print('Division by zero is not allowed')

print(c)