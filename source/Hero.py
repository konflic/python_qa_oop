class Hero:
    __health = None
    __defend = None
    __healing = None
    __power = None
    __name = None

    def __init__(self, defend, healing, power, name):
        if defend + healing + power > 100:
            raise AttributeError("Такого героя создать нельзя, сумма всех навыков должна быть ровно 100")
        self.__health = 100
        self.__defend = defend
        self.__healing = healing
        self.__power = power
        self.__name = name
        print(f"Hero {name} with {defend} {healing} {power} created!")

    def __str__(self):
        return self.__name

    def hit(self, other_hero):
        other_hero.take_hit(self)

    def heal(self):
        if self.__health == 100:
            return "Health is full"
        else:
            res = self.__health + self.__healing
            self.__health = 100 if res > 100 else res

    def take_hit(self, other_hero):
        self.__health = self.__health - (other_hero.__power - self.__defend)

    def get_health(self):
        return self.__health
