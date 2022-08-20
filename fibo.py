def fib(n):
    """
    It prints out the Fibonacci sequence up to a given number
    
    :param n: The number of Fibonacci numbers to print
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """
    It creates a list of Fibonacci numbers up to a given number
    
    :param n: The number of Fibonacci numbers to generate
    :return: A list of the Fibonacci numbers up to n.
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    print(result)