s1  = { 1,2,3,4}
s2  = { 5,6,7,8}
s3 =  { 8,9,0,1}

print(s1.isdisjoint(s2))  #return true if no common elemment in both sets else fales
print(s1.isdisjoint(s3))  #if any element in both set are common then isdisJoint() function return false