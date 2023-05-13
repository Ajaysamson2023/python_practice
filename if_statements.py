# check the given number is even:

a=int(input("Enter the number:"))


if a % 2==0:
    print(a, "it is even")
else:
    print("it is not even")

# To check  vote eligibility of a person:

name=input("Enter the name:")
age=int(input("Enter the age:"))

if age>=18:
    print(name, age, "Eligible to vote")
else:
    print(name, age, "NOT eligible to  vote")