f = open("info.txt", "a+")

# print("File name:", file.name)
# print("File mode:", file.mode)
# print("File closed?", file.closed)
# print("File encoding:", file.encoding)

print(f.closed) 
print(f.encoding) 
print(f.mode) 
print(f.newlines) 
# print(f.softspace) 

f.close()
print(f.closed) 