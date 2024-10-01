marks = [ 98, 89, 87 ,98,90]
print(marks)
print("Average marks: ", sum(marks) / len(marks))
print("length of the list " ,len(marks))
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print("Access Through Negative And Positive index")
print(marks[-3]) #negative index
print(marks[len(marks)-3]) #positive index

if 97 in marks:
    print("97 is present in the list")
else:
    print("97 is not present in the list")

if "av" in "Naveen":
    print("yes")

