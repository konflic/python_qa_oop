class Account:
    __counter = 0
    __balance = 100

    def __init__(self):
        if self.__up_counter() > 5:
            raise Exception("Too many accounts created!")
        print("Account {} created!".format(self.__counter))

    @property
    def balance(self):
        print("Notification: Balance was get!")
        return self.__balance

    @staticmethod
    def static():
        print("Call this method without instance, its ok!")

    @classmethod
    def __up_counter(cls):
        cls.__counter += 1
        return cls.__counter

    def accounts_created(self):
        return self.__counter


ex = Account()
ex2 = Account()
ex3 = Account()
ex4 = Account()
ex5 = Account()

print(ex.accounts_created())