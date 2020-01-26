class Car:
    """Car class"""
    engine_status = "Off"

    def __init__(self, brand, model, wheels):
        """Class constructor"""
        self.brand = brand
        self.model = model
        self.wheels = wheels

    def start_engine(self):
        """Starting car engine"""
        self.engine_status = "On"
        print(f"Engine of {self.brand} {self.model} started.")

    def go(self):
        """Start driving the car"""
        self.start_engine()
        print(f"The {self.brand} {self.model} is driving.")

    def turn_off_engine(self):
        """Turn car engine off"""
        if self.engine_status == "On":
            self.engine_status = "Off"
            print(f"Engine of {self.brand} {self.model} is turned off")
        else:
            print(f"Engine of {self.brand} {self.model} is already off")


toyota_camry = Car(brand="Toyota", model="Camry", wheels=4)
honda_civic = Car(brand="Honda", model="Civic", wheels=4)

toyota_camry.go()
toyota_camry.turn_off_engine()
honda_civic.turn_off_engine()
