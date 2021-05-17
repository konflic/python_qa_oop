# new class Figure
class Figure:
    def __init__(self, name, angles):
        if self.__class__ == Figure:
            raise Exception("abstract method")
        self.name = name
        self.angles = angles

    def get_name(self):
        return self.name

    def get_angles(self):
        return self.angles

    def area(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Not instance of Figure!")
