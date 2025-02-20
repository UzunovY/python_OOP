from typing import Union

from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget < price:
            return "Not enough budget"

        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        if worker := next((w for w in self.workers if w.name == worker_name), None):
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        # if self.__budget < (total_salaries := sum(w.salary for w in self.workers)):
        #     return "You have no budget to pay your workers. They are unhappy"
        # self.__budget -= total_salaries
        # return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return self.__expenses(self.workers)

    def tend_animals(self) -> str:
        # if self.__budget < (animals_care_cost := sum(a.money_for_care for a in self.animals)):
        #     return "You have no budget to tend the animals. They are unhappy."
        # self.__budget -= animals_care_cost
        # return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return self.__expenses(self.animals)

    def __expenses(self, objects: list[Union[Animal, Worker]]) -> str:
        if objects[0].__class__.__bases__[0].__name__ == "Worker":
            if self.__budget < (total_salaries := sum(obj.salary for obj in objects)):
                return "You have no budget to pay your workers. They are unhappy"
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        if self.__budget < (animals_care_cost := sum(obj.money_for_care for obj in objects)):
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= animals_care_cost

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self):
        return self.__status(self.animals, "Lion", "Tiger", "Cheetah")

    def workers_status(self):
        return self.__status(self.workers, "Keeper", "Caretaker", "Vet")

    @staticmethod
    def __status(objects: list[Union[Animal, Worker]], *types: str) -> str:
        info = {type_name: [] for type_name in types}
        for obj in objects:
            info[obj.__class__.__name__].append(repr(obj))

        result = [f"You have {len(objects)} {str(objects[0].__class__.__bases__[0].__name__).lower()}s"]
        for key, value in info.items():
            result.append(f"----- {len(value)} {key}s:")
            result.extend(value)

        return "\n".join(result)
