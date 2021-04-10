class Parent1:

    def method(self):
        print("This is Parent1!")


class Parent2:

    def method(self):
        print("This is Parent2!")


class Child1(Parent2, Parent1):
    pass


class Child2(Parent2):

    def method(self):
        print("This is Child2!")


class Child(Child1, Child2):
    pass

# Показать дерево поиска методов для класса
print(Child.mro())

Child().method()
