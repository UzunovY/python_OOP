from abc import ABC, abstractmethod


class Food(ABC):

    @abstractmethod
    def __init__(self, quantity: int) -> None:
        self.quantity = quantity


class Vegetable(Food):

    def __init__(self, quantity: int) -> None:
        super().__init__(quantity)


class Fruit(Food):

    def __init__(self, quantity: int) -> None:
        super().__init__(quantity)


class Meat(Food):

    def __init__(self, quantity: int) -> None:
        super().__init__(quantity)


class Seed(Food):

    def __init__(self, quantity: int) -> None:
        super().__init__(quantity)
