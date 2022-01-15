import pytest
from source.Rectangle import Rectangle

name = "Rc1"


def test_create_class():
    rectangle = Rectangle(name, 2, 4)
    assert isinstance(rectangle, Rectangle)
    assert rectangle.a == 2
    assert rectangle.b == 4
    assert rectangle.name == name
    assert rectangle.angles == 4


def test_perimeter():
    rectangle = Rectangle(name, 2, 4)
    assert rectangle.perimeter() == 12


def test_area():
    rectangle = Rectangle(name, 2, 4)
    assert rectangle.area() == 8


def test_add_area():
    rectangle1 = Rectangle(name, 2, 4)
    rectangle2 = Rectangle(name, 3, 6)
    assert rectangle1.add_area(rectangle2) == 26


def test_exception_in_method_add_area():
    foo_example = 0
    rectangle = Rectangle(name, 2, 4)
    with pytest.raises(ValueError):
        rectangle.add_area(foo_example)
