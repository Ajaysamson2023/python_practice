# function: A block of code which  executes only when it is called.
# Passing a data into a function is called "parameter"
# It "return" data as a "RESULT"


def welcome():
    print("welcome to practice python")


welcome()



def add():
    a = int(input("Enter the A value:"))
    b = int(input("Enter the B value:"))
    c = a + b
    print("total:", c)


add()


def sub(a, b):
    c = a - b
    print("total :", c)


sub(13, 5)