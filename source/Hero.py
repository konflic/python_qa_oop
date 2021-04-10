class Hero:
    __COUNT = 0

    def __init__(self, defend, healing, power, name):
        if defend + healing + power > 100:
            raise AttributeError("Defend + healing + power can not be > 100")
        self.__health = 100
        self.__defend = defend
        self.__healing = healing
        self.__power = power
        self.__name = name
        self.__increase_count()
        print(f"Hero '{name}' with {defend} {healing} {power} created!")

    def __str__(self):
        return "{}:{}hp".format(self.__name, self.__health)

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

    def hit(self, other_hero):
        if not isinstance(other_hero, Hero):
            raise Exception("You can hit only Hero!")
        other_hero.__take_hit(self)

    def heal(self):
        if self.__health == 100:
            return "Hero health is full"
        else:
            res = self.__health + self.__healing
            self.__health = 100 if res > 100 else res

    def __take_hit(self, other_hero):
        damage = other_hero.__power - self.__defend
        self.__health = self.__health - damage

    @classmethod
    def __increase_count(cls):
        cls.__COUNT += 1
        print("{} heroes exist".format(cls.__COUNT))

    @classmethod
    def __decrease_count(cls):
        print("Hero was destroyed!")
        if cls.__COUNT > 0: cls.__COUNT -= 1
        print("{} heroes left".format(cls.__COUNT))
