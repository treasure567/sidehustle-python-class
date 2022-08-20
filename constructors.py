class Employee:
    def __init__(self, age, salary):
        self.age = age
        self.salary = salary
        print('This is a parametized constructor')

    def show(self, name):
        print(f"The employeen name is {name}. The salary is {self.salary} and the age is {self.age}")

a = Employee(17, 20000)

a.show("Treasure")