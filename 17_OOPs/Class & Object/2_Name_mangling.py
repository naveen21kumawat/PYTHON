class parent:
    def __init__(self):
        self.__name = "parent" #__name cannot be direclty accessed
     
    def __add(self,a,b):
        return a+b


class child(parent):
    def __age(self,a):
        # super().__init__()
        self.__age = a
        return self.__age

       
ob = child()

# print(ob.__name) #its cannot be accessed
print(ob._parent__name) # _pareent__Name  is a name_mangling
# print(ob.__dir__())
print(ob._parent__add(10,20))
print(ob._child__age(12))