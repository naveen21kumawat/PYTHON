class stu():
    country = "india"
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def show(self):
            print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade} , Country: {self.country}")
st1 = stu("naveen",19,"A")           
st2 = stu("sai",20,"B")
st1.show()
st2.country = "USA"
st2.show()