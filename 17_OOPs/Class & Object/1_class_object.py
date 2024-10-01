class person:
    name = "Naveen"
    age = 19
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

a= person() # create a object of the class person 
a.display()  # Output: Name:  Naveen Age:  19

b = person()
b.name="nitika"
b.age= 18
b.display()