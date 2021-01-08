# New class declaration
class Car:
    pass


# New class Animal
class Animal:
    pass


# Creating class instances (objects)
toyota = Car()
lada = Car()
dog = Animal()


# Checking class of objects
print("toyota <- Car", isinstance(toyota, Car))
print("lada <- Car", isinstance(lada, Car))
print("dog <- Car", isinstance(dog, Animal))


# Class is also an object
print(Car)
honda = Car
print(isinstance(honda, Car))
