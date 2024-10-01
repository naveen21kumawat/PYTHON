info = {
    1 : "Naveen",
    2 : "Manish",
    3 : "Shubham",
    4 : "ridhi"
}

print(info.keys()) #Get All the keys 
print(info.values())# get All the values
print(len(info))
# print(info[12]) #raise an error
print(info[4])
print(info.get(12,"Not Found")) # return Not Found if key is not present
print(info.get(12))  # print None if key is not found
print(info.get(1)) # print the value of key 1