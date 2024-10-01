class India:
    def capital(self):
        print("The capital of the india is delhi")
    
    def language(self):
        print("Hindi is most widly spoke language in india")

    def type(self):
        print("India is a developing country")

class USA:
    def capital(self):
        print("The capital of the USA is washington D.C")
    
    def language(self):
        print("English is most widly spoke language in USA")

    def type(self):
        print("USA is a developed country") 

def func(ob):
    ob.capital()
    ob.language()
    ob.type()

ob1 = India()
ob2 = USA()

func(ob1)
print("------------")
func(ob2)