# It creates a class called Employee.
class Employee:
    def __init__(self, age, salary):
        """
        The __init__() function is called automatically every time the class is being used to create a
        new object
        
        :param age: The age of the employee
        :param salary: The salary of the employee
        """
        self.age = age
        self.salary = salary
        print('This is a parametized constructor')

    def show(self, name):
        """
        The function show() takes in a parameter name and prints out the name, salary and age of the
        employee
        
        :param name: This is the name of the employee
        """
        print(f"The employeen name is {name}. The salary is {self.salary} and the age is {self.age}")

# Creating an object called a of the class Employee.
a = Employee(17, 20000)

# Calling the function show() and passing in the parameter "Treasure"
a.show("Treasure")