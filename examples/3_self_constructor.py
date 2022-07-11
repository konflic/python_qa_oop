class Car:
    __engine_status = "Off"

    def __init__(self, brand, model, wheels, key):
        self.brand = brand
        self.model = model
        self.wheels = wheels
        self.key = key

    def start_engine(self, key):
        if key == self.key:
            self.__engine_status = "On"
            print(f"Engine of {self.brand} {self.model} started. On {self.wheels} wheels.")

    def drive(self):
        if self.__engine_status == "On":
            print(f"Ride on {self.brand} {self.model} started. On {self.wheels} wheels.")
        else:
            print("Turn on engine before drive.")

    def stop_engine(self):
        if self.__engine_status == "Off":
            return None
        self.__engine_status = "Off"
        print(f"Engine of {self.brand} {self.model} stopped.")


toyota_camry = Car(brand="Toyota", model="Camry", wheels=4, key="1234")

toyota_camry.drive()
