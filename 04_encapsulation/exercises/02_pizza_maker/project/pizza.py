from project.dough import Dough
from project.topping import Topping


class Pizza:

    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int) -> None:
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: dict[Topping.topping_type, Topping.weight] = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings "
                             "cannot be less or equal to zero")
        self.__max_toppings = value

    def add_topping(self, topping: Topping) -> None:
        if not self.__max_toppings:
            raise ValueError("Not enough space for another topping")

        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = 0
        self.toppings[topping.topping_type] += topping.weight
        self.__max_toppings -= 1

    def calculate_total_weight(self) -> float:
        result = self.dough.weight  # + sum(self.toppings.values())
        for topping, weight in self.toppings.items():
            result += self.toppings[topping]

        return result
