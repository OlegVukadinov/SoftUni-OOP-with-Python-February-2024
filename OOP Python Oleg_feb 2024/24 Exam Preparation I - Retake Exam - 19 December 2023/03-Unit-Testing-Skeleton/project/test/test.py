from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):

    def setUp(self):
        self.robot = ClimbingRobot(
            "Mountain",
            "Helper",
            100,
            200
        )

        self.robot_with_software = ClimbingRobot(
            "Mountain",
            "Helper",
            100,
            200
        )

        self.robot_with_software.installed_software = [
            {"name": "Pycharm", "capacity_consumption": 50, "memory_consumption": 49},
            {"name": "Clion", "capacity_consumption": 49, "memory_consumption": 52}
        ]

    def test_correct__init__(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("Helper", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(200, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_category_with_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Oleg"
        self.assertEqual(f"Category should be one of {self.robot.ALLOWED_CATEGORIES}", str(ve.exception))

    def test_get_used_capacity_success(self):
        expected_result = sum(s['capacity_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_used_capacity()

        self.assertEqual(expected_result, result)

    def test_get_available_capacity_expect_success(self):
        expected_result = self.robot.capacity - sum(
            s['capacity_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_available_capacity()

        self.assertEqual(expected_result, result)

    def test_get_used_memory_success(self):
        expected_result = sum(s['memory_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_used_memory()

        self.assertEqual(expected_result, result)

    def test_get_available_memory_expect_success(self):
        expected_result = self.robot.memory - sum(
            s['memory_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_available_memory()

        self.assertEqual(expected_result, result)

    def test_install_software_with_max_equal_values_success(self):
        result = self.robot.install_software(
            {"name": "Pycharm", "capacity_consumption": 100, "memory_consumption": 200},
        )
        self.assertEqual(f"Software 'Pycharm' successfully installed on Mountain part.", result)

        self.assertEqual(
            self.robot.installed_software,
            [{"name": "Pycharm", "capacity_consumption": 100, "memory_consumption": 200}]
        )

    def test_install_software_with_less_than_max_values_success(self):
        result = self.robot.install_software(
            {"name": "Pycharm", "capacity_consumption": 10, "memory_consumption": 20},
        )
        self.assertEqual(f"Software 'Pycharm' successfully installed on Mountain part.", result)

        self.assertEqual(
            self.robot.installed_software,
            [{"name": "Pycharm", "capacity_consumption": 10, "memory_consumption": 20}]
        )

    def test_install_software_with_greater_than_max_values_success(self):
        result = self.robot.install_software(
            {"name": "Pycharm", "capacity_consumption": 10, "memory_consumption": 2000},
        )
        self.assertEqual("Software 'Pycharm' cannot be installed on Mountain part.", result)

        self.assertEqual(self.robot.installed_software, [])

    def test_install_software_both_greater_than_max_values_success(self):
        result = self.robot_with_software.install_software(
            {"name": "Pycharm", "capacity_consumption": 49, "memory_consumption": 52},
        )
        self.assertEqual("Software 'Pycharm' cannot be installed on Mountain part.", result)

        self.assertEqual(self.robot.installed_software, [])


if __name__ == "__main__":
    main()
