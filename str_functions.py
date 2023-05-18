# string:It is used to store a values in a single variable
# -that can be denoted as single or double quotation

a = "Manoj kumar"
print(a)
print(type(a))

"""
inbuilt string function:
upper()
lower()
isupper()
islower()
strip()
l strip()
r strip()
title()
splitlines()
capitalize()
partition()
"""
x="welcome to python"

count=0
for i in x:
    if i=="e":
        count+=1
print(str(count))
