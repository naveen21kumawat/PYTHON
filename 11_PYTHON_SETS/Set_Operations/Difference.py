
s1= {1,2,3,4,5}
s2 = {1,2,3}

print(s2.difference(s1))   # remove s1 element those exist in s2    if  set is empty return set()
print(s2.symmetric_difference(s1))  #remove common element from s1 and s2

s1.difference_update(s2) 
print(s1)