class Car:  # Объявление класса Human
    pass


class Animal:  # Объявление класса Animal
    pass


# Создание объектов (экземпляров) классов
toyota = Car()
lada = Car()
dog = Animal()

# Проверка на экземпляр класса
print("toyota <- Car", isinstance(toyota, Car))
print("lada <- Car", isinstance(lada, Car))
print("dog <- Car", isinstance(dog, Animal))

# Это не создание в присвоение
honda = Car
print(isinstance(honda, Car))
