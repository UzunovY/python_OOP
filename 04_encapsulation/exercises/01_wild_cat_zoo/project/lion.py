from project.animal import Animal


class Lion(Animal):
    money_for_care: int = 50

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, self.money_for_care)
