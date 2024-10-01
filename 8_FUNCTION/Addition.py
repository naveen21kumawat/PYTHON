def fun(x,y):
    return x+y

print(fun(3,4)) #required argument

def calculate(a=10 , b=20): # default argument
    print(a+b)

calculate(b=10)  #keyword argument
calculate(20 ,30)   