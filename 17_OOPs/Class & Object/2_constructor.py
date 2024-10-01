class student:
    def __init__(self,n,a):  #parameterized constructor
        self.name = n
        self.age = a

    def info(self):
        print("Name : ",self.name)
        print("Age : ",self.age,"\n-----------------")

obj = student("naveen",19)
obj.info()  # output: Name : naveen Age : 19

obj1 = student("Arya", 20)
obj1.info()

obj2 = student("Ananya",23)
obj2.info()