# a= (input(" ENTER A INTEGER NUMBER::"))
a=(input(" ENTER THE INDEX OF THE VALUE::"))
b = [ 2,4,5]

try:
  
    if (b[int(a)])%2==0:
        print(f"THE NUMBER IS EVEN {b[int(a)]}")
    else:
        print(f"THE NUMBER IS ODD {b[int(a)]}")
        
except TypeError:
    print("ENTERED NUMBER IS NOT A mm INTEGER")
        
except ValueError:
    print("ENTERED NUMBER IS NOT A INTEGER")

except IndexError:
    print("Invalid Index")    