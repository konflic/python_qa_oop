DEFAULT_HEALTH = 100


class Hero:
    __COUNT = 0

    def __init__(self, defend, healing, power, name):
        if defend + healing + power > DEFAULT_HEALTH:
            raise AssertionError("Defend + healing + power can not be > 100")
        self.__health = DEFAULT_HEALTH
        self.__defend = defend
        self.__healing = healing
        self.__power = power
        self.__name = name
        self.__increase_count()

    def __repr__(self):
        return "{}:{}".format(self.__name, self.__health)

    def __del__(self):
        self.__decrease_count()

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @property
    def count(self):
        return self.__COUNT

    def get_power(self):
        return self.__power

    def get_defend(self):
        return self.__defend

    def hit(self, enemy):
        print(f"{self} hit {enemy}")
        if not isinstance(enemy, Hero):
            raise Exception("You can hit only Hero!")
        enemy.__take_hit(self)

    def heal(self):
        if self.__health == DEFAULT_HEALTH:
            return "Hero health is full"
        else:
            res = self.__health + self.__healing
            self.__health = DEFAULT_HEALTH if res > 100 else res

    def __take_hit(self, enemy):
        print(f"{self} got hit from {enemy}")
        damage = enemy.__power - self.__defend
        self.__health = self.__health - damage
        if self.__health <= 0:
            del self

    @classmethod
    def __increase_count(cls):
        cls.__COUNT += 1
        print("{} hero created".format(cls.__COUNT))

    @classmethod
    def __decrease_count(cls):
        if cls.__COUNT > 0: cls.__COUNT -= 1
        print("{} hero left".format(cls.__COUNT))
