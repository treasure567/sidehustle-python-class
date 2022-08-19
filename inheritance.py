# Defining a class called Player.
class Player:
    def Captain(self):
        print("I am the skipper of the team!")


# A class is a blueprint for creating objects
class Striker(Player):
    def Score(self, name):
        print(f"My name is {name} and i score lots of goals!")

# Creating an object of the class Player.
x = Player()

# Calling the method Captain() from the class Player.
x.Captain()

# Creating an object of the class Striker.
y = Striker()

# Calling the method Score() from the class Striker.
y.Score("Treasure")

# Calling the method Captain() from the class Player.
y.Captain()

# This class has a method called Add that takes two numbers and returns their sum
class Solution1:
    def Add(self, num1, num2):
        return num1 + num2

# This class is a solution to the problem of multiplying two numbers
class Solution2:
    def Multiply(self, num1, num2):
        return num1 * num2

# This class inherits from Solution1 and overrides the Divide method to take user input and return the
# result of the division
class Solution3(Solution1, Solution2):
    def Divide(self, a, b):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return (a / b)

# Creating an object of the class Solution1.
a = Solution1()

# Calling the method Add() from the class Solution1 and passing the arguments 1 and 2.
print(a.Add(1, 2))

# Creating an object of the class Solution3.
b = Solution3()

# Calling the method Divide() from the class Solution3 and passing the arguments 3 and 2.
print(b.Divide(3, 2))

# Calling the method Add() from the class Solution1 and passing the arguments 4 and 5.
print(b.Add(4, 5))

# Calling the method Multiply() from the class Solution2 and passing the arguments 4 and 6.
print(b.Multiply(4, 6))

# Checking if Solution3 is a subclass of Solution1.
print(issubclass(Solution3, Solution1))

# Checking if Solution2 is a subclass of Solution1.
print(issubclass(Solution2, Solution1))