class programmer():
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b

    def show(self):
        print(f"Num1 : {self.num1}  Num2 : {self.num2}")


class developer(programmer):
    def tow_times(self):
        print(f"Num1 * 2 : {self.num1 * 2}")

    
a = developer(12,14)
a.show()
a.tow_times()