from source.Figure import Figure


class Rectangle(Figure):
    def __init__(self, name, a, b):
        super().__init__(name, 4)
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b

    def add_area(self, figure):
        super().add_area(figure)
        return figure.area() + self.area()