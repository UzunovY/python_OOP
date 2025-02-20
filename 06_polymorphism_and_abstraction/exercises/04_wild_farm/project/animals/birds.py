from project.animals.animal import Bird
from project.food import Meat, Fruit, Vegetable, Seed


class Owl(Bird):

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def food_menu(self):
        return [Meat]

    @property
    def weight_gain(self):
        return 0.25


class Hen(Bird):

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def food_menu(self):
        return [Meat, Fruit, Vegetable, Seed]

    @property
    def weight_gain(self):
        return 0.35
