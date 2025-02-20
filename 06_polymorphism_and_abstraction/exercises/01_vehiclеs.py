from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AC_FUEL_CONSUMPTION: float = 0.9

    def drive(self, distance):
        required_fuel = distance * (self.fuel_consumption + self.AC_FUEL_CONSUMPTION)
        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_FUEL_CONSUMPTION: float = 1.6

    def drive(self, distance):
        required_fuel = distance * (self.fuel_consumption + self.AC_FUEL_CONSUMPTION)
        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel):
        spilled_fuel = 0.95
        self.fuel_quantity += fuel * spilled_fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
print()
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
