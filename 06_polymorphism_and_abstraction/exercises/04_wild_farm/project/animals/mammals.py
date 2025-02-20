from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def food_menu(self):
        return [Vegetable, Fruit]

    @property
    def weight_gain(self):
        return 0.1


class Dog(Mammal):

    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def food_menu(self):
        return [Meat]

    @property
    def weight_gain(self):
        return 0.4


class Cat(Mammal):

    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def food_menu(self):
        return [Meat, Vegetable]

    @property
    def weight_gain(self):
        return 0.3


class Tiger(Mammal):

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def food_menu(self):
        return [Meat]

    @property
    def weight_gain(self):
        return 1.0

