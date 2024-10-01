class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def A_show(self):
        print(f"A: a={self.a}, b={self.b}")

class B(A):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c

class C(B):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.d=d

    def C_show(self):
        print(f"C: a={self.a}, b={self.b}, c={self.c},d={self.d}")

ob = C(1,2,3,4)
ob.A_show()
ob.C_show()
