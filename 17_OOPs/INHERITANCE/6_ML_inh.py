class Age:
    def __init__(self,age):
        self.age = age

    def Age(self):
        print(f" AGE : {self.age}")

class Name(Age):
    def __init__(self,age,name):
        super().__init__(age)
        self.name = name

    def show(self):
        print(f" NAME : {self.name}")
        super().Age()

class City(Name):
    def __init__(self,age,name,city):
        super().__init__(age,name)
        self.city = city

    def show(self):
        super().show()
        print(f" CITY : {self.city}")


ob = City(19,"Avee","Jaipur")
ob.show()