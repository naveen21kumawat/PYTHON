class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
p = student("Naveen",19,"A")
print(p.__dict__) # result will in dictionary form
print(p.__new__) # result will in dictionary form
# print(dir(p))


print(p.__module__) # result will be __main__
# print(help(student))