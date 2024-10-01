class person:
    def __init__(self ,name ,age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls ,string):
        name ,age = string.split(',')
        return cls(name ,int(age))
    
p = person.from_string("john,30")
print(p.name)
print(p.age)  