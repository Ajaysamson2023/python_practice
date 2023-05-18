# __init__method: To initializing  values or to do some work in the class.
# It executes whenever instance(object) is created.
# It has 'self' and we can add 'parameter'.

class data:
    def __init__(self, name, age):
        print("Call Whenever new instance is created ")
        self.name = name
        self.age = age

    def printall(self):
        print(self.name, self.age)


o1 = data("Raj", 28)
o1.printall()
print(o1.__dict__)
print("-------------------------------------------")
o2 = data("SAM", 35)
o2.printall()
print(o2.__dict__)
