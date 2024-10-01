# Arithmetic Operators
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333333333333335
print(a % b)  # Output: 1
print(a ** b) # Output: 1000
print(a // b) # Output: 3

# Comparison Operators
print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: True
print(a < b)   # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False

# Logical Operators
x = True
y = False
print(x and y) # Output: False
print(x or y)  # Output: True
print(not x)   # Output: False

# Bitwise Operators
print(a & b)   # Output: 2
print(a | b)   # Output: 11
print(a ^ b)   # Output: 9
print(~a)      # Output: -11
print(a << 1)  # Output: 20
print(a >> 1)  # Output: 5

# Assignment Operators
c = 5
c += 3
print(c)  # Output: 8
c -= 3
print(c)  # Output: 5
c *= 3
print(c)  # Output: 15
c /= 3
print(c)  # Output: 5.0

# Identity Operators
d = [1, 2, 3]
e = [1, 2, 3]
print(d is e)       # Output: False
print(d is not e)   # Output: True
f = d
print(d is f)       # Output: True

# Membership Operators
g = 'hello'
print('h' in g)     # Output: True
print('z' not in g) # Output: True

# Walrus Operator
n = 10
if (m := n + 5) > 10:
    print(m)  # Output: 15
