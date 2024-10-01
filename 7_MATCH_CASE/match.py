x = 5
# in python break statement are not use to braek the execution like c and c++


match x:
    case 5:
        print("x is 5")
    case 6:
        print("x is 6")
    case 7:
        print(" x is 7")
    case _  if x!=10:
        print("x is not equal to 10")
    case _ if x == 10:
        print (" x is equal to 10")    