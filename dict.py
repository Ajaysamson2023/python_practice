# Dictionary is stored like key value pairs,Mutable,no duplicates,indexed
user = {
    "name": "raj",
    "age": 23,
    "is married": True
}
print(user)
print(user["name"])
print(user["age"])
print(user["is married"])
print(type(user))
print(user.keys())
print(user.values())
print(user.items())

for x in user:
    print(x, "", user[x])

for x in user.keys():
    print(x)

for x in user.values():
    print(x)

for x, y in user.items():
    print(x, y)
