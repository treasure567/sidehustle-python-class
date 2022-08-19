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