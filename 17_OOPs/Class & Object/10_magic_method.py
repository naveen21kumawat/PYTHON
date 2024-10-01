from typing import Any


class Student:
    def __init__(self,name):
        self.name = name
    
    def __len__(self):
        return len(self.name)

    def __str__(self):
        return f"Student Name {self.name}"
    
    def __call__(self) :
        return f"Hello {self.name}"
    
    
e = Student("Naveen")
print(str(e))
print(len(e))  # returns the length of the name string
print(e)  # returns the string representation of the object
print(e())  # returns the result of calling the object as a function
e()