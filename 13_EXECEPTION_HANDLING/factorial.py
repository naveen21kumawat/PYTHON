def facto(n):
       
            
          if n < 0:
             raise ValueError("Factorial is not defined for negative numbers.")
          elif n == 0:
             return 1
          else:
            return n * facto(n - 1)

print(facto(5))