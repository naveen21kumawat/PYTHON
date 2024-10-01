class A: 
    def __init__(self , value):
        self.value = value

    def __add__(self , other):
        return A(self.value + other.value)
    
    def __str__(self):
        return f"{self.value}"
    
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")
print(A.__add__(ob1,ob2))