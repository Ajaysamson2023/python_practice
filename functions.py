# function: A block of code which  executes only when it is called.
# Passing a data into a function is called "parameter"
# It "return" data as a "RESULT"


def welcome():
    print("welcome to practice python")


welcome()
"""
4 types of functions:
1.Built in function----('68' functions)
2.User defined function--(User based function)
3.Lambda function ----(anonymous function)
4.Recursive function---- (call itself to finish work)(4 types known)

Some Built-in- function in python:

"""


# no return type without arguments function:


def add():
    a = int(input("Enter the A value:"))
    b = int(input("Enter the B value:"))
    c = a + b
    print("total:", c)


add()


# no return type with arguments function:


def sub(a, b):
    c = a - b
    print("total :", c)


sub(13, 5)


# return type without arguments function:

def mul():
    a = int(input("Enter the A value:"))
    b = int(input("Enter the B value:"))
    c = a * b
    return c


x = mul()
print("total:", x)


# return type with arguments:


def div(a, b):
    c = a / b
    return c


x = div(12, 4)
print("total:", x)


# arbitrary arguments (*args):

def classDetails(*students):
    print(students)


classDetails("raj", "sam", "ni", "son", "dad", "faf")


# keyword arguments function:(kwargs)

def classDetails(name, age, gender):
    print("your name is ", name, age, "age old , gender:", gender)


classDetails(name="ajay", gender="male", age=24)


# arbitrary keyword arguments(**kwargs):


def class10(**list):
    print(list)


class10(name="raj", age=24, gender="male", phone=8122338494, address="3/1200,new street, bangalore")


# passing list as an arguments[list]:

def total(marks):
    print("total:", sum(marks))


total([23, 33, 22, 3])


# default parameter arguments:

def student(name, city="salem"):
    print("The name is", name, "from", city)


student("Raj")
student("SAM", "bangalore")


# recursive function(call itself to finish work) factorial:

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


c = factorial(5)
print(c)


# recursive function for sum of values(numbers):
def sum(x):
    if x == 1:
        return 1
    else:
        return x + sum(x - 1)


x = int(input("Enter the value:"))
c = sum(x)
print("sum of value:", c)


# Recursive function for [sequence of values]:
def num(x):
    if x != 0:
        num(x - 1)
        print(x)


x = int(input("Enter the number:"))
num(x)


# recursive function for Tables:
def tables(n, t):
    if n != 0:
        tables(n - 1, t)
        print(n, "*", t, "=", n * t)


t = int(input("Enter t value:"))
n = int(input("Enter n value:"))

tables(n, t)

# lambda function (anonymous function):

x = lambda a, b: a + b
print(x(23, 4))

x = lambda a, b, c: a + b * c
print(x(2, 4, 3))

x = lambda a, b, c: a / b * c
print(x(2, 4, 3))
