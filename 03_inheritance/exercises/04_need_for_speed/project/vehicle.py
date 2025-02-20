class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int) -> None:
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: int) -> None:
        if self.fuel >= (fuel_for_trip := self.fuel_consumption * kilometers):
            self.fuel -= fuel_for_trip

