import pytest

from src.Hero import Hero, DEFAULT_HEALTH


def test_hero_creation():
    """Check creating hero with sum of attributes > 100"""
    with pytest.raises(AssertionError):
        Hero(defend=30, healing=30, power=70, name="Ninja")


def test_hero_hit_negative(default_hero):
    """Hero can't hit other classes"""
    class Car: pass
    with pytest.raises(Exception):
        default_hero.hit(Car())


def test_hero_hit_positive(default_hero):
    """Hero can't hit other classes"""
    default_hero.hit(Hero(defend=20, healing=10, power=70, name="TestHero"))


def test_hero_hit_reduce_health(default_hero, second_hero):
    """Hero can't hit other classes"""
    health_before_hit = second_hero.health
    default_hero.hit(second_hero)
    assert second_hero.health == (health_before_hit - default_hero.get_power() + second_hero.get_defend())
    assert default_hero.health == DEFAULT_HEALTH


def test_heal_health_increase():
    """Healing can't increase health over 100"""
    hero1 = Hero(defend=60, healing=10, power=30, name="TestHero1")
    hero2 = Hero(defend=20, healing=20, power=60, name="TestHero2")
    hero1.hit(hero2)
    assert hero2.health == 90
    hero2.heal()
    assert hero2.health == 100
