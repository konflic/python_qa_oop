import pytest

from src.Hero import Hero


@pytest.fixture(scope="session")
def init_test_arena():
    print("TEST ARENA CREATED!")
    yield
    print("TEST ARENA DESTROYED")


@pytest.fixture
def default_hero(init_test_arena):
    return Hero(defend=30, healing=30, power=40, name="TestHeroDefault")


@pytest.fixture
def second_hero(init_test_arena):
    hero = Hero(defend=30, healing=40, power=30, name="TestHeroOptimus")
    yield hero
    del hero
