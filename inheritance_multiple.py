# multiple inheritance:

class addition:
    def add(self):
        a = int(input("enter a:"))
        b = int(input("enter b:"))
        c = a + b
        print(c)


class subtraction:
    def sub(self):
        a = int(input("enter a:"))
        b = int(input("enter b:"))
        c = a - b
        print(c)


class result(addition, subtraction):
    def res(self):
        self.add()
        self.sub()


o = result()
o.res()
