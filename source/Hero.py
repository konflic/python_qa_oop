class Hero:
    __HERO_COUNT = 0

    def __init__(self, defend, healing, power, name):
        if defend + healing + power > 100:
            raise AttributeError("Sum of defend, healing and power skill can not be > 100")
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
        self.__HERO_COUNT -= 1
        print("Hero destroyed! Only {} Hero left!".format(self.__HERO_COUNT))

    @property
    def name(self):
        return self.__name

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
        print("Hero '{}' hit hero '{}' and made {} damage!".format(other_hero.name, self.__name, damage))

    def __increase_count(self):
        self.__HERO_COUNT += 1
        print("There are {} Hero!".format(self.__HERO_COUNT))

    def get_health(self):
        print("Hero '{}' health is {}".format(self.__name, self.__health))
        return self.__health
