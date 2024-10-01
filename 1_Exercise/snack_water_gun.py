user = int (input("1 for gun \n 0 for water \n -1 for snack :"))
# generate a random number in -1 to 1
# print( " Game rules")

import random

com=(random.randint(-1, 1))
print("Computer chose:",com)

if(user == com):
    print("Drow ")

elif(user == 1 and com == 0):
     print("You Lose")
elif(user == 1 and com == -1):
     print("You Win")

elif(user == 0 and com == 1):
     print("You Lose")
elif(user == 0 and com == -1):
     print("You Win")
     
elif(user == -1 and com == 1):
     print("You Lose")
elif(user == -1 and com == 0):
     print("You Win")
     



