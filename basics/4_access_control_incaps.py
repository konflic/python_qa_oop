class Car:
    """Car class"""
    _wheels = 4
    __engine_status = "Off"

    def __init__(self, brand, model):
        """Class constructor"""
        self.brand = brand
        self.model = model

    def get_wheels(self):
        """Returns the status of private"""
        return self._wheels

    def get_engine_status(self):
        """Returns the value off protected attribute"""
        return self.__engine_status

    def get_car_name(self):
        return f"{self.brand} {self.model}"

    def start_engine(self):
        """Start car engine"""
        self.__engine_status = "On"
        print(f"Engine of {self.get_car_name()} started.")

    def drive(self):
        """Start driving the car"""
        if self.__engine_status == "Off":
            print("Turn on engine first!")
        else:
            print(f"The {self.get_car_name()} is driving.")

    def turn_off_engine(self):
        """Turn car engine off"""
        if self.get_engine_status() == "On":
            self.__engine_status = "Off"
            print(f"Engine of {self.get_car_name()} was turned off")
        else:
            print(f"Engine of {self.get_car_name()} is already off")


toyota_camry = Car(brand="Toyota", model="Camry")
