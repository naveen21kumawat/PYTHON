class Vehical:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("move!")

class  car(Vehical):
    pass

class boat(Vehical):
    def move(self):
        print("sail!")

class plan(Vehical):
    def move(self):
        print("fly!")

car1 = car("N","A")
boat1 = boat("V","E")
plan1 = plan("E","N")

for x in (car1,boat1,plan1  ):
    x.move()
    print(x.brand)
    print(x.model)