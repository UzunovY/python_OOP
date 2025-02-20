from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(30.0, 100.0)

    def test_default_fuel_consumption(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_init_arguments(self):
        self.assertEqual(30.0, self.vehicle.fuel)
        self.assertEqual(30.0, self.vehicle.capacity)
        self.assertEqual(100.0, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_with_not_enough_fuel_raises(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.assertEqual(30.0, self.vehicle.fuel)
        self.vehicle.drive(10)
        self.assertEqual(17.5, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel_raises(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(50)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_fuel_amount_to_full_capacity(self):
        self.vehicle.fuel = 0
        result = self.vehicle.refuel(30)
        self.assertEqual(30.0, self.vehicle.fuel)

        self.assertIsNone(result)

    def test_string_method_returns_correct_message(self):
        self.assertEqual("The vehicle has 100.0 horse power "
                         "with 30.0 fuel left and 1.25 fuel consumption",
                         str(self.vehicle))


if __name__ == "__main__":
    main()
