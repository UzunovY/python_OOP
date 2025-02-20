from project.collectors.base_collector import BaseCollector


class PrivateCollector(BaseCollector):
    available_money = 25_000.0
    available_space = 3000

    def __init__(self, name: str):
        super().__init__(name, self.available_money, self.available_space)

    def increase_money(self):
        self.available_money += 5000

