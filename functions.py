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
# print("The total sum is: ", addNew('', ''))

def kwargsp(**k):
    """
    This function takes keyword arguments and prints them
    
    :param kwargs: The keyword arguments to be printed
    :return: None
    """
    print('The least child is', k['c'])

# Calling the function kwargsp and passing the keyword arguments a, b, and c.
kwargsp(a = 1, b = 2, c = 3)

def love(name = "Boy", b = 'girl'):
    """
    The function love() takes two arguments, name and b, and prints the value of name. 
    
    The function love() has two parameters, name and b. 
    
    The function love() has a default value for name, which is "Boy". 
    
    The function love() has a default value for b, which is "girl". 
    
    The function love() has a docstring, which is "Here's a one sentence summary of the above function:
    The function love() takes two arguments, name and b, and prints the value of name." 
    
    The function love() has a docstring, which is "Here's a one sentence summary of the above function:
    The function love() takes two arguments, name and b, and prints the value of name." 
    
    The function love() has a docstring, which is "Here's a one sentence summary
    
    :param name: This is a positional parameter, defaults to Boy (optional)
    :param b: This is a positional parameter, defaults to girl (optional)
    """
    print(name)

# Calling the function love() and passing the argument 'treasure' to it.
love('treasure')

