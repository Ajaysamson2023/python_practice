# multi-level inheritance:

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


class call(subtraction):
    def result(self):
        self.add()
        self.sub()


o = call()
o.result()
