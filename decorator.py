# DECORATOR:To decorate a function with @function:

"""
1.Nested function
2.function returns another function
3.function as parameter
4.function as a reference
"""


# Function as a  parameter:

def function():
    print("this is function 1")


def function1(para):
    para()
    print("this is function 2")


function1(function)
print("----------------------------------------------")


# 1.Nested function
# 2.function returns another function
# 3.function as reference
def function1():
    msg1 = "welcome to  "

    def function2():
        msg2 = "Python"
        add = msg1 + msg2
        return add

    return function2


obj = function1()
print(obj())
