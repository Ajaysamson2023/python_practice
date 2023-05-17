# POLYMORPHISM:
# They are three types:
#            1.Method Overloading-(same name with different arguments)
#            2.Method Overriding-(same name with same arguments)
#            3.Operator Overloading-(Two objects does not concatenate by using constructor will do by[magic()])


"""# 1.METHOD OVERLOADING:
class poly:
    def polymorphism(self, *args):
        sum = 0
        for i in args:
            sum = sum + i
        print("sum value:",sum)


o = poly()
o.polymorphism(23, 4)
o.polymorphism(23)
o.polymorphism(23, 4, 45)"""

"""# 2.METHOD OVERRIDING:
class ram:
    def project(self):
        print("Online shopping management system")


class sam(ram):
    def project(self):
        super().project()
        print("Online car parking system")


class dad(sam):
    def project(self):
        super().project()
        print("Online correction system")


o=dad()
o.project()"""

"""# 3.OPERATOR OVERLOADING:

class operator:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a


o = operator(23)
o1 = operator(33)
print(o + o1)"""


# PRACTICE FOR OPERATOR overloading:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        print("NAME:", self.name)
        c = self.salary * other.days
        return c


class payment:
    def __init__(self, days):
        self.days = days


o1 = Employee("ram", 2000)
o2 = payment(31)
print("Net salary:", o1 * o2)

