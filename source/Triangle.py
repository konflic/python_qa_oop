from source.Figure import Figure


class Triangle(Figure):
    def __init__(self, name, a, b, c):
        super().__init__(name, 3)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        return self.perimeter() / 2

    def add_area(self, figure):
        super().add_area(figure)
        return figure.area() + self.area()