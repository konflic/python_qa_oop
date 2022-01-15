from source.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, name, a):
        super().__init__(name, a, a)