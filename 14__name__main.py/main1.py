def sqrt(num):
    if num < 0:
        return 0
    elif(num == 1):
        return 1
    else:
        return num**2
    

print(__name__)
if __name__=="__main__":     
  print(sqrt(5))         