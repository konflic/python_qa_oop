import pytest

from source.Hero import Hero


def test_hero_creation():
    with pytest.raises(AttributeError):
        Hero(defend=30, healing=30, power=70, name="Ninja")


def test_hero_hit_negative():
    class Car: pass

    with pytest.raises(Exception):
        hero1 = Hero(defend=30, healing=30, power=40, name="Ninja")
        hero1.hit(Car())


def test_hit():
    hero1 = Hero(defend=30, healing=30, power=40, name="Ninja")
    hero2 = Hero(defend=30, healing=40, power=30, name="Optimus")
    hero1.hit(hero2)
    assert hero2.get_health() == 90
    hero2.hit(hero1)
    assert hero1.get_health() == 100


def test_heal():
    hero1 = Hero(defend=30, healing=30, power=40, name="Ninja")
    hero2 = Hero(defend=30, healing=40, power=30, name="Optimus")
    hero1.hit(hero2)
    assert hero2.get_health() == 90
    hero2.heal()
    assert hero2.get_health() == 100
