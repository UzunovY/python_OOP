class Vet:
    animals: list[str] = []
    space: int = 5

    def __init__(self, name: str):
        self.name = name
        self.animals: list[str] = []

    def register_animal(self, animal_name: str) -> str:
        if self.space != 0:
            Vet.space -= 1
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name in Vet.animals:
            Vet.space += 1
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self) -> str:
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
