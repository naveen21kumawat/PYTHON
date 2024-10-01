a ="1" # 1 is the string 
b = "4" # 4 is the string
print(a+b)

#explicit typecast a and b value :- by developer
print(int (a)+ int (b))

#implicit type casting :- automaticall
print(a + str(4)) # here 4 is integer and a is string so python will convert 4 into string and then concatenate
num1 = 12.3
num2 = 13
print(num1+ num2)

x=4j

# y=int(x)
print(type(x))