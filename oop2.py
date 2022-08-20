class Employee:
    name = "Treasure"
    salary = 20000
    department = "Engineering"

    def show(self):
        print('The employee\'s details are:', self.name, self.salary, self.department)


a = Employee()

a.show()

# Polymorphism is the ability of an object to take more than one form.
# encapsulation is the ability of an objectto be hidden from end users.
# abstraction is the ability of an object to be represented by a simpler interface.
# Inhheritance is the ability of a class to inherit the attricutes and methods of another class.

# The public method can access the private method, but the private method cannot be accessed directly
# from outside the class.

# It creates a class called Animal.
class Animal:
    def __private(self):
        return 'This is a private Methof'

    def public(self):
        """
        The function public() is a member of the class Foo, and it prints the return value of the
        function __private(), which is also a member of the class Foo
        """
        print(self.__private())


a = Animal()

a.public()
