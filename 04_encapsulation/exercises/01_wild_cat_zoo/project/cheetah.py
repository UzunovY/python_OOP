from project.animal import Animal


class Cheetah(Animal):
    money_for_care: int = 60

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, self.money_for_care)
