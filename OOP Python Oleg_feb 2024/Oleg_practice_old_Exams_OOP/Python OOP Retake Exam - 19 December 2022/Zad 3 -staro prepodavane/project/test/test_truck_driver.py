from unittest import TestCase, main

from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self):
        self.driver = TruckDriver("Test", 1.0)

    def test_correct_init(self):
        self.assertEqual("Test", self.driver.name)
        self.assertEqual(1.0, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_below_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.earned_money = -1
        self.assertEqual(f"{self.driver.name} went bankrupt.", str(ex.exception))

    def test_set_earned_money(self):
        self.assertEqual(0, self.driver.earned_money)
        self.driver.earned_money = 5
        self.assertEqual(5, self.driver.earned_money)

    def test_add_existing_cargo_offer_raises(self):
        self.driver.add_cargo_offer("place 1", 12)

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("place 1", 13)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_drive_best_cargo_offer_no_offer(self):
        self.assertEqual(self.driver.drive_best_cargo_offer(), "There are no offers available.")

    def test_add_offer(self):
        result = self.driver.add_cargo_offer("place1", 12)
        self.assertEqual(f"Cargo for 12 to place1 was added as an offer.", result)

    # def test_drive_best_cargo_offer_no_offer_raise(self):
    #     self.driver.available_cargos = {}
    #
    #     result = self.driver.drive_best_cargo_offer()
    #     self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer(self):
        self.driver.add_cargo_offer("place1", 100)
        self.driver.add_cargo_offer("place2", 200)
        self.driver.add_cargo_offer("place3", 50)

        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

        res = self.driver.drive_best_cargo_offer()
        self.assertEqual(f"Test is driving 200 to place2.", res)

        self.assertEqual( 200, self.driver.earned_money)
        self.assertEqual(200, self.driver.miles)

    def test_check_for_activities(self):
        self.driver.earned_money = 11760
        self.driver.check_for_activities(10000)
        self.assertEqual(10, self.driver.earned_money)

    def test_drive_best_offer_with_activities(self):
        self.driver.earned_money = 11760

        needed_money_for_cargo = 11750
        km_to_drive = 10000
        money_to_earn = self.driver.money_per_mile * km_to_drive

        self.driver.add_cargo_offer("place1", 10000)

        self.driver.drive_best_cargo_offer()
        expected_money_left = (11760 + money_to_earn) - needed_money_for_cargo

        self.assertEqual(expected_money_left, self.driver.earned_money)

    def test_eat(self):
        self.driver.earned_money = 100
        self.driver.eat(250)
        self.assertEqual(self.driver.earned_money, 80)

    def test_sleep(self):
        self.driver.earned_money = 100
        self.driver.sleep(1000)
        self.assertEqual(self.driver.earned_money, 55)

    def test_pump_gas(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(1500)
        self.assertEqual(self.driver.earned_money, 500)

    def test_repair_truck(self):
        self.driver.earned_money = 8000
        self.driver.repair_truck(10000)
        self.assertEqual(self.driver.earned_money, 500)

    def test_repr(self):
        self.driver.miles = 500
        self.assertEqual(repr(self.driver), "Test has 500 miles behind his back.")


if __name__ == '__main__':
    main()
