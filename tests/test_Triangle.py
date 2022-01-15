import pytest
from source.Triangle import Triangle

name = "Tr1"


def test_create_class():
    triangle = Triangle(name, 2, 4, 3)
    assert isinstance(triangle, Triangle)
    assert triangle.a == 2
    assert triangle.b == 4
    assert triangle.c == 3
    assert triangle.name == name
    assert triangle.angles == 3


def test_perimeter():
    triangle = Triangle(name, 2, 4, 3)
    assert triangle.perimeter() == 9


def test_area():
    triangle = Triangle(name, 2, 2, 2)
    assert triangle.area() == 3


def test_add_area():
    triangle1 = Triangle(name, 2, 2, 2)
    triangle2 = Triangle(name, 4, 4, 4)
    assert triangle1.add_area(triangle2) == 9


def test_exception_in_method_add_area():
    foo_example = 0
    triangle = Triangle(name, 2, 2, 2)
    with pytest.raises(ValueError):
        triangle.add_area(foo_example)
