class Car:
    wheels = 4 # class attribute

    def drive(self):
        print("Car is driving")

    def stop(self):
        print("Car stopped")


class Animal:
    legs = 4 # class attribute

    def make_sound(self):
        print("I'm Animal")

    def sleep(self):
        print("Animal start sleeping")


print("======= Cars =======")
toyota = Car()
honda = Car()
dog = Animal()

dog.make_sound()

# Calling methods
toyota.drive()
honda.stop()

# Getting attributes
print(honda.wheels)
print(toyota.wheels)