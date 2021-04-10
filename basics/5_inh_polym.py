class Vehicle:
    _wheels = None
    __engine_status = "Off"

    def __init__(self, brand, model, wheels):
        self.brand = brand
        self.model = model
        self._wheels = wheels

    def get_wheels(self):
        return self._wheels

    def get_engine_status(self):
        return self.__engine_status

    def get_name(self):
        return f"{self.brand} {self.model}"

    def start_engine(self):
        self.__engine_status = "On"
        print(f"Engine of {self.get_name()} started.")

    def drive(self):
        self.start_engine()
        print(f"The {self.get_name()} is driving.")

    def turn_off_engine(self):
        if self.get_engine_status() == "On":
            self.__engine_status = "Off"
            print(f"Engine of {self.get_name()} was turned off")
        else:
            print(f"Engine of {self.get_name()} is already off")

    def crash_into(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            print("Only another Vehicle class can be crashed into!")
        else:
            print(f"Bang! {self.get_name()} crashed into {vehicle.get_name()}!")


class Luxurious:

    def get_name(self):
        raise NotImplemented("This method is not implemented!")

    def show_off(self):
        print(f"Hey you, checkout my {self.get_name()}!")


class Car(Vehicle):

    def __init__(self, brand, model):
        # Через super() обращаемся к конструктору Vehicle
        super().__init__(brand, model, 4)


class Motocycle(Luxurious, Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand, model, 2)

    def boom(self):
        print("Boom!")

    def drive(self):
        if self.get_engine_status() != "On":
            print(f"To drive {self.get_name()} you must start engine first!")
        else:
            print(f"The {self.get_name()} is driving.")


if __name__ == "__main__":
    ducati_supersport = Motocycle(brand="Ducati", model="Supersport")
    ducati_supersport.drive()
    ducati_supersport.boom()
    print(ducati_supersport.get_wheels())
    ducati_supersport.show_off()
    ducati_supersport.get_name()

