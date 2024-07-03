class Employee:
    def __init__(self, name, role, dep, salary):
        self.name = name
        self.role = role
        self.dep = dep
        self.salary = salary
    def showDetails(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Deprtment:", self.dep)
        print("Salary:", self.salary)

emp1 = Employee("Sishir Siam", "Junior Devloper", "Odoo Devloper", 2000)

emp1.showDetails()