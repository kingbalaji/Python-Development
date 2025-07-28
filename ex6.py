import copy
car = {1:"Tesla"}
print(id(car))
secondcar = car
print(id(secondcar))

secondcar ="Tesla1"
print(car)
print(secondcar)

print(id(car))
print(id(secondcar))
