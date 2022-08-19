def exampleFunction():
    """
    This function prints "hey"
    """
    print("hey")

def add(x,y):
    """
    This function takes two numbers as input and returns their sum
    
    :param x: The first number to add
    :param y: The function to be decorated
    :return: The sum of x and y
    """
    return x+y


# It prints "hey"
exampleFunction()

# It prints the sum of 2 and 30
print(add(2,30))

def addNew(*args):
    """
    It takes three numbers as input, adds them together, and returns the result
    
    :param a: int
    :param b: int = 0
    :param c: int = 0
    :return: The sum of the three numbers.
    """
    a = int(input('Enter first Number: '))
    b = int(input('Enter second Number: '))
    c = int(input('Enter third Number: '))
    return a + b + c

# Printing the sum of the three numbers.
print("The total sum is: ", addNew('', ''))