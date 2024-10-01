class shape:
    def __init__(self, height,weight):
        self.height =height
        self.weigth = weight

    def area(self):
        return self.height * self.weigth
    
class rectangle(shape):
    def __init__(self, height, weight):
        super().__init__(height, weight)

class circle(rectangle):
    def __init__(self,redius):
         self.redius = redius
         super().__init__(redius,redius)

    def area(self):
         
        return 3.14 * super().area()

ob= circle(5)
print(ob.area())




