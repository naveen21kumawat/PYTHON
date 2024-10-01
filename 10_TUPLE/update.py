thistuple = ( "Hello" , "World", "Toyota")
print(thistuple)
x= list(thistuple)
x[2]= "Suzuki"  # Toyota update with the Suzuki
print(x)
thistuple = tuple(x)
print(type(thistuple))
print("\nLoop through items \32\n ")
for x in thistuple:
    print(x)

for value in range(len(thistuple)):
    print( value ,thistuple[value])   