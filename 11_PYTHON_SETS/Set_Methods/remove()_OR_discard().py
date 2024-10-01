s2 = {"avee","manish", "shubham"}
print(" Original Set : ",s2)
s2.remove("avee") # raise an error if item are not exist else remove item from the set
print(s2)
# s2.remove("kunal") # raise an error because "kunal" is not exist
# print(s2)
s2.discard("kunal") # not raise an error if item are not exist
print(s2)
s2.discard("manish")
print(s2) # remove "manish" from the set
