class Employee():
    def __init__(self):
        self.name = "naveen"
        self.age = 25
        self.salary = 50000
    def display(self):
        print("Employee Name: ",self.name)
        print("Employee Age: ",self.age)
        print("Employee Salary: ",self.salary)
        
emp = Employee()
emp.display()
