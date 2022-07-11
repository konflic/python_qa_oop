class Vehicle:
    __engine_status = "Off"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_engine_status(self):
        return self.__engine_status

    def set_engine_status(self, status):
        if status not in ["On", "Off"]:
            self.__engine_status = status
        print("wrong value")

    def get_name(self):
        return f"{self.brand} {self.model}"


class LuxVehicle(Vehicle):

    def get_name(self):
        return f"!!!!{self.brand} {self.model}!!!!"

    def show_off(self):
        print(f"Hey you, checkout my {self.get_name()}!")
