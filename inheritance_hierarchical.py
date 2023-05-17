# Hierarchical inheritance:

class arith:
    def arithmatic(self):
        self.a = int(input("Enter value A:"))
        self.b = int(input("Enter value B:"))


class addition(arith):
    def add(self):
        self.arithmatic()
        c = self.a + self.b
        print("addition:",c)


class subtract(arith):
    def sub(self):
        self.arithmatic()
        c = self.a - self.b
        print("subtraction",c)


o1 = addition()
o1.add()
o2 = subtract()
o2.sub()
