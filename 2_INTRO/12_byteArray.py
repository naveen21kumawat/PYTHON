# Creating a bytearray
my_bytearray = bytearray(b'hello')

# Accessing elements
print(my_bytearray[0])  # Output: 104 (ASCII value of 'h')

# Modifying elements
my_bytearray[0] = 105
print(my_bytearray)  # Output: bytearray(b'iello')

# Slicing
print(my_bytearray[1:3])  # Output: bytearray(b'el')
