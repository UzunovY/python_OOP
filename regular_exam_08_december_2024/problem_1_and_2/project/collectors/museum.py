from project.collectors.base_collector import BaseCollector


class Museum(BaseCollector):
    available_money = 15_000.0
    available_space = 2000

    def __init__(self, name: str):
        super().__init__(name, self.available_money, self.available_space)

    def increase_money(self):
        self.available_money += 1000

