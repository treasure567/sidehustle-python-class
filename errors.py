# Asking for two numbers and dividing them.
try:
    a = int(input('Enter first Number: '))
    b = int(input('Enter second Number:' ))
    c = a / b
    print(c)
# Catching the exception and printing the message.
except Exception as e:
    print('Sorry i can divide by 0')
# Printing the last line of code.
else:
    print('Last Line of code')