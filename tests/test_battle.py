import pytest
import random

from source.Hero import Hero


def test_hero_creation():
    """Check creating hero with sum of attributes > 100"""
    with pytest.raises(AttributeError):
        Hero(defend=30, healing=30, power=70, name="Ninja")


def test_hero_hit_negative():
    """Hero can't hit other classes"""

    class Car: pass

    with pytest.raises(Exception):
        hero1 = Hero(defend=30, healing=30, power=40, name="Ninja")
        hero1.hit(Car())


def test_hit():
    """Hero hit other hero"""
    hero1 = Hero(defend=30, healing=30, power=40, name="Ninja")
    hero2 = Hero(defend=30, healing=40, power=30, name="Optimus")
    hero1.hit(hero2)
    assert hero2.health == 90


def test_heal_health_increase():
    """Healing can't increase health over 100"""
    hero1 = Hero(defend=30, healing=30, power=40, name="Ninja")
    hero2 = Hero(defend=30, healing=40, power=30, name="Optimus")
    hero1.hit(hero2)
    assert hero2.health == 90
    hero2.heal()
    assert hero2.health == 100


def test_heal_hero_full_health():
    """Full health is not healing for hero"""
    hero = Hero(defend=30, healing=30, power=40, name="Ninja")
    assert hero.heal() == "Hero health is full"
    assert hero.health == 100


def test_hero_counter():
    random_amount = random.randint(5, 10)
    heroes = []
    for i in range(random_amount):
        heroes.append(Hero(defend=30, healing=30, power=40, name=f"Hero{i}"))
    assert heroes[0].count == random_amount


def test_hero_counter_delete():
    random_amount = random.randint(5, 10)
    heroes = []
    for i in range(random_amount):
        heroes.append(Hero(defend=30, healing=30, power=40, name=f"Hero{i}"))
    assert len(heroes) == random_amount
    del heroes[0]
    assert heroes[1].count == random_amount - 1
