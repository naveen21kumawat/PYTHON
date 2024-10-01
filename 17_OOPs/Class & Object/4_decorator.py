class f:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(self._value)
       
    @property
    def ten_time(self):
        return 10 * self._value


ob = f(12)
ob.show()
print(ob.ten_time)
# print(a)
