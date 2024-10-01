class math():

    @staticmethod #don't need to pass self as a argument
    def add(a,b):
        print (f"{a} + {b} = {a+b}")

ob = math()
ob.add(5,3) # Output: 5 + 3

# defination of static method
# Static methods are methods that are bound to a class rather than the instance of the class. They
# are used to group functions that belong to a class, but don't need to access the class
# or instance variables. They are essentially functions that are namespaced within a class.
# They are typically used for utility functions that don't depend on the state of the class or instance
