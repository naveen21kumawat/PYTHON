s1 = { 2,3,4,6,8}
s2 = { 3, 5,6,"H",7}
print(s1.union(s2))
print(s1.union(s2)) # returns a new set with all elements from both sets


s2.update(s1)   # add s1 element into s2 those not exist in s2
print(s2)

