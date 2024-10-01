class parent :
    def parent_mehod(self):
        print("This is parent method")

class Child(parent):
    def child_method(self):
        print("This is child method")
        super().parent_mehod()

PM = parent()
PM.parent_mehod()

CM = Child()
CM.child_method()
CM.parent_method()