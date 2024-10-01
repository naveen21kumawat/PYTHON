s1 ={ 2,3,4,5,6}
s2 ={ 2,3,7,8,9}
print(s2)
s3 = s1.intersection(s2)   
print(" s1 intersection s2 : ",s3)
s2.intersection_update(s1)  # update s2 as a common element inn both set
print(s2)