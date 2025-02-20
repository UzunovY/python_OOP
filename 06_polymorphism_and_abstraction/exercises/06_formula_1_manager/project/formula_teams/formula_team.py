from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    def __init__(self, budget: int):
        self.budget = budget

    @property
    @abstractmethod
    def sponsors(self):
        ...

    @property
    @abstractmethod
    def race_expenses(self):
        ...

    @property
    def budget(self):
        return self.__budget
    
    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        for rewards in self.sponsors.values():
            for pos in rewards:
                if race_pos <= pos:
                    revenue += rewards[pos]
                    break
        revenue -= self.race_expenses
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
