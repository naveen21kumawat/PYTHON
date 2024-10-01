import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n*5

print(fx(6)) #Execute after the 5 second when we run the program
print("Done for 6")
print(fx(11))#Execute after the 5 second when we run the program
print("Done for 11")
print(fx(10))#Execute after the 5 second when we run the program
print("Done for 3")

print(fx(11))#Execute withot taking one second because the fx() funciton already execute for value 11
print("Done for 11")
print(fx(11))#Execute
print("Done for 11")
print(fx(11))#Execute 
print("Done for 11")


