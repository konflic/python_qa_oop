class Car:  # Объявление класса Human
    """Car class"""
    wheels = 4

    def drive(self):
        print("Car is driving")

    def stop(self):
        print("Car stopped")


class Animal:  # Объявление класса Animal
    """Animal class"""
    legs = 4

    def make_sound(self):
        print("I'm Animal")

    def sleep(self):
        print("Animal start sleeping")


print("======= Cars =======")
# Создаем объекты Car
toyota = Car()
honda = Car()

toyota.drive()
honda.stop()
print(honda.wheels)
print(toyota.wheels)

print("======= Animals =======")
# Создаем объекты Animal
dog = Animal()
lion = Animal()
print(dog.legs)
