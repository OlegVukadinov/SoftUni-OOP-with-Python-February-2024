from project.robot import Robot
import unittest


class TestRobot(unittest.TestCase):
    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']
    PRICE_INCREMENT = 1.5

    def setUp(self):
        self.robot1 = Robot("001", "Education", 100, 1000)
        self.robot2 = Robot("002", "Entertainment", 200, 1500)

    def test__init__(self):
        self.assertEqual("001", self.robot1.robot_id)
        self.assertEqual("002", self.robot2.robot_id)
        self.assertEqual("Education", self.robot1.category)
        self.assertEqual("Entertainment", self.robot2.category)
        self.assertEqual(100, self.robot1.available_capacity)
        self.assertEqual(200, self.robot2.available_capacity)
        self.assertEqual(1000, self.robot1.price)
        self.assertEqual(1500, self.robot2.price)
        self.assertEqual([], self.robot1.hardware_upgrades)
        self.assertEqual([], self.robot2.hardware_upgrades)
        self.assertEqual([], self.robot1.software_updates)
        self.assertEqual([], self.robot2.software_updates)

    def test_category(self):
        self.assertEqual(self.robot1.category, "Education")
        self.assertEqual(self.robot2.category, "Entertainment")

        with self.assertRaises(ValueError) as ex:
            self.robot1.category = "InvalidCategory"
        self.assertEqual(f"Category should be one of '{self.ALLOWED_CATEGORIES}'", str(ex.exception))

    def test_price(self):
        self.assertEqual(self.robot1.price, 1000)
        self.assertEqual(self.robot2.price, 1500)

        with self.assertRaises(ValueError) as ex:
            self.robot1.price = -100
        self.assertEqual("Price cannot be negative!", str(ex.exception))

    def test_upgrade(self):
        self.assertEqual(self.robot1.upgrade("Laser", 200), "Robot 001 was upgraded with Laser.")
        self.assertEqual(self.robot1.price, 1000 + 200 * 1.5)

        self.assertEqual(self.robot1.upgrade("Laser", 200), "Robot 001 was not upgraded.")

    def test_update_successful(self):
        # Testing a successful update
        self.assertEqual(self.robot1.update(1.1, 50), "Robot 001 was updated to version 1.1.")
        self.assertEqual(self.robot1.software_updates, [1.1])
        self.assertEqual(self.robot1.available_capacity, 100 - 50)

    def test_update_unsuccessful_due_to_version(self):
        # Adding a previous version
        self.robot1.software_updates.append(1.0)
        # Attempting to update to a version that's already installed
        self.assertEqual(self.robot1.update(1.0, 50), "Robot 001 was not updated.")
        # Attempting to update to a version that's older than the current installed version
        self.assertEqual(self.robot1.update(0.9, 50), "Robot 001 was not updated.")

    def test_update_unsuccessful_due_to_capacity(self):
        # Attempting to update with needed capacity more than available capacity
        self.assertEqual(self.robot1.update(1.2, 150), "Robot 001 was not updated.")

    def test_update_unsuccessful_due_to_negative_capacity(self):
        # Attempting to update with negative needed capacity
        with self.assertRaises(ValueError):
            self.robot1.update(1.2, -50)
    # def test_update(self):
    #     self.assertEqual(self.robot1.update(1.1, 50), "Robot 001 was updated to version 1.1.")
    #     self.assertEqual(self.robot1.available_capacity, 100 - 50)
    #
    #     self.assertEqual(self.robot1.update(1.0, 200), "Robot 001 was not updated.")

    def test_comparison(self):
        self.assertEqual(self.robot1 > self.robot2, "Robot with ID 001 is cheaper than Robot with ID 002.")
        self.assertEqual(self.robot2 > self.robot1, "Robot with ID 002 is more expensive than Robot with ID 001.")
        self.assertEqual(self.robot1 > self.robot1, "Robot with ID 001 costs equal to Robot with ID 001.")


if __name__ == '__main__':
    unittest.main()
