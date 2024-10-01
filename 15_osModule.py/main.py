import os
if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0, 40):
    os.remove("data/Day1")

# for i in range(0, 40):
#     os.rename(f"data/Day{i+1}",f"data/Tutorial {i+1}")

# folders=os.listdir("data")


# print(folders)

# for f in folders:
#     print(f)
#     print(os.listdir(f"data/{f}"))

#Print current working directory
# print("Current directory:" , os.getcwd())   
 
# Change current working directory
print(os.chdir("data") )