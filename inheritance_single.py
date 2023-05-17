# single inheritance:

class addition:
    def add(self):
        a = int(input("enter a:"))
        b = int(input("enter b:"))
        c = a + b
        print(c)


class subtraction(addition):
    def sub(self):
        a = int(input("enter a:"))
        b = int(input("enter b:"))
        c = a - b
        print(c)


o = subtraction()
o.add()
o.sub()
