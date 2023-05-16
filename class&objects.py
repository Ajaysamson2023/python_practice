# class is a 'constructor for  creating object' or 'blueprint of object'
# Object is a 'instance of class' which is consists of methods and properties
# Class attributes:"Variables that created inside a class is called class attributes"

class data:
    name = "raj kumar"
    age = 24


# Getattr

print(getattr(data, "name"))
print(getattr(data, "age"))
print(getattr(data, "gender", "NO such attribute Error"))
# dot notation:

print(data.name)
print(data.age)

# setattr

setattr(data, "name", "SAM")
print(data.name)
setattr(data, "city", "salem")
print(data.city)

data.gender = "male"
print(data.gender)

print(data.__dict__)

# Delattr

delattr(data, "city")
print(data.__dict__)

del data.gender
print(data.__dict__)
