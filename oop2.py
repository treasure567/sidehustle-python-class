class Employee:
    name = "Treasure"
    salary = 20000
    department = "Engineering"

    def show(self):
        print('The employee\'s details are:', self.name, self.salary, self.department)


a = Employee()

a.show()