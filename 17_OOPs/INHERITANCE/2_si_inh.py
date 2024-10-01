class Animal:
    def __init__(self):
        self.name = "Dog"
        self.age = 3

    def sound(self):
        print("The animal makes a sound")

class Cat(Animal):
    def __init__(self):
        self.name = "cat"
    
   
ob = Cat()
ob.sound()

