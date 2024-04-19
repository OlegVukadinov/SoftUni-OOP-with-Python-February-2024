from unittest import TestCase, main

#from CarManager.car_manager import Car


class TestCarManager(TestCase):

    def setUp(self):
        self.car = Car("Nissan", "GT-R", 15, 75)

    def test_correct_init(self):
        self.assertEqual("Nissan", self.car.make)
        self.assertEqual("GT-R", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(75, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("", "GT-R", 15, 75)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Nissan", "", 15, 75)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_zero_fuel_consumption_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Nissan", "GT-R", 0, 75)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_zero_fuel_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Nissan", "GT-R", 15, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_negative_fuel_amount_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount -= 1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_zero_refuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_more_refuel_than_capacity_fills_to_capacity_raises_exception(self):
        self.car.refuel(80)
        self.assertEqual(75, self.car.fuel_amount)

    def test_drive_car_with_valid_fuel(self):
        self.car.refuel(1000)
        self.car.drive(10)

        self.assertEqual(73.5, self.car.fuel_amount)

    def test_drive_without_fuep_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
