class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Hello, my name is {self.name}")

class Dance:
    def __init__(self,dance):
        self.dance = dance
        
    def show(self):
        print(f"I'm dancing {self.dance}")


class DancerEmployee(Employee,Dance):
    def __init__(self ,dance,name):
        self.name = name
        self.dance= dance

    # def __str__(self):
    #      print(self.name)
    #      print(self.dance)

o = DancerEmployee("kathak","shivani")

o.show()
print(o.dance)
print(o.name)

print(DancerEmployee.mro())