# Hybrid inheritance:

class arithmatic:
    def arith(self):
        self.a = int(input("enter a:"))
        self.b = int(input("enter b:"))


class addition(arithmatic):
    def add(self):
        self.arith()
        c = self.a + self.b
        print("add:", c)


class subtraction(arithmatic):
    def sub(self):
        self.arith()
        c = self.a - self.b
        print("sub:", c)


class calls(addition, subtraction):
    def call(self):
        self.add()
        self.sub()


o = calls()
o.call()

print("---------------------------------------------------")

class A:
    def display(self):
        print("GRADE A")


class B(A):
    def display(self):
        print("GRADE B")


class C(A):
    def display(self):
        print("GRADE C")


class D(B, C):
    def display(self):
        print("GRADE D")


o = D()
o.display()