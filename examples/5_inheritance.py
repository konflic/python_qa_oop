class Vehicle:
    __engine_status = "Off"

    def __init__(self, brand, model, wheels):
        self.brand = brand
        self.model = model
        self._wheels = wheels

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


class Luxurious:

    def get_name(self):
        raise NotImplemented("This method is not implemented!")

    def show_off(self):
        print(f"Hey you, checkout my {self.get_name()}!")
