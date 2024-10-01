def fun():
   try:
     x= input("ENTERED NUMBER IS NOT A INTEGER")
     x= int(x)
     print(x)
     return 1    
   
   except ValueError :
      print("value is not a integer")
      return ("ValueError")
   
   finally:
      print("this will always execute")
a = fun()
print(a)
