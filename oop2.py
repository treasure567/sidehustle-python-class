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


class Animal:
    def __private(self):
        return 'This is a private Methof'

    def public(self):
        print(self.__private())


a = Animal()

a.public()
