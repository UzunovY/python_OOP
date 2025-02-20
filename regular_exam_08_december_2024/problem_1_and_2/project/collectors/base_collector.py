from abc import ABC, abstractmethod
import re

from project.artifacts.base_artifact import BaseArtifact


class BaseCollector(ABC):

    def __init__(self, name: str, available_money: float, available_space: int):
        self.name = name
        self.available_money = available_money
        self.available_space = available_space
        self.purchased_artifacts: list[BaseArtifact] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        pattern = r'^[A-Za-z0-9\s]+$'

        if not re.match(pattern, value):
            raise ValueError("Collector name must contain letters, numbers, and optional white spaces between them!")
        self.__name = value

        # if value.strip() == "" \
        #         or not all(ch.isalnum() or ch.isspace() for ch in value)\
        #         or value[0] == " " \
        #         or value[-1] == " ":
        #     raise ValueError("Collector name must contain letters, numbers, and optional white spaces between them!")
        # self.__name = value.strip()

    @property
    def available_money(self):
        return self.__available_money

    @available_money.setter
    def available_money(self, value):
        if value < 0.0:
            raise ValueError("A collector cannot have a negative amount of money!")
        self.__available_money = value

    @property
    def available_space(self):
        return self.__available_space

    @available_space.setter
    def available_space(self, value):
        if value < 0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")
        self.__available_space = value

    @abstractmethod
    def increase_money(self):
        pass

    def can_purchase(self, artifact_price: float, artifact_space_required: int) -> bool:
        if artifact_price > self.available_money or artifact_space_required > self.available_space:
            return False
        return True

    def __str__(self):
        art_names = sorted([art.name for art in self.purchased_artifacts], reverse=True)

        return f"Collector name: {self.name}; Money available: {self.available_money:.2f}; " \
               f"Space available: {self.available_space}; " \
               f"Artifacts: {', '.join(art_names) if art_names else 'none'}"
