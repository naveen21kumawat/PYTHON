def Generators():
    for i in range(5):
     yield i


gen = Generators()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))