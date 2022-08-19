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

class Solution1:
    def Add(self, num1, num2):
        return num1 + num2

class Solution2:
    def Multiply(self, num1, num2):
        return num1 * num2

class Solution3(Solution1):
    def Divide(self, a, b):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return (a / b)

a = Solution1()

print(a.Add(1, 2))