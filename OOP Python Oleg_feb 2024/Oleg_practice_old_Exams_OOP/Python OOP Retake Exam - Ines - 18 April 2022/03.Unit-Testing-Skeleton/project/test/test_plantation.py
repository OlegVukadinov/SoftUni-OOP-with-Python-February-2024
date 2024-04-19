from unittest import TestCase, main

from project import Plantation


class TestPlantation(TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(2)

    def correct_init(self):
        self.assertEqual(2, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_is_negative_raises(self):
        with self.assertRaises(ValueError) as ex:
            Plantation(-1)
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_worker(self):
        self.assertEqual([], self.plantation.workers)
        self.assertEqual(0, len(self.plantation.workers))

        result = self.plantation.hire_worker("Test")

        self.assertEqual(["Test"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))
        self.assertEqual(f"Test successfully hired.", result)

    def test_hire_worker_already_hired_raises(self):
        self.plantation.hire_worker("Test")
        self.assertEqual(["Test"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker("Test")

        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_length(self):
        self.plantation.size = 3
        self.plantation.hire_worker("Test")

        self.plantation.planting("Test", 'rose')
        self.assertEqual(1, len(self.plantation))

        self.plantation.planting("Test", 'rose2')
        self.assertEqual(2, len(self.plantation))

        # Test len with two workers where 1 has 2 flowers, 2 has 1 , len should be 3

        self.plantation.hire_worker("Test2")
        self.plantation.planting("Test2", 'rose3')

        self.assertEqual({"Test": ['rose', "rose2"], "Test2": ['rose3']}, self.plantation.plants)
        self.assertEqual(3, len(self.plantation))

    def test_planting_worker_exist_raises(self):
        self.plantation.hire_worker("Test")

        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Not existing", "rose")

        self.assertEqual(f"Worker with name Not existing is not hired!", str(ex.exception))

    def test_planting_plantation_is_full_raises(self):
        self.plantation.size = 0
        self.plantation.hire_worker("Test")

        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Test", 'rose')
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting(self):
        self.assertEqual({}, self.plantation.plants)

        self.plantation.hire_worker("Test")
        result = self.plantation.planting('Test', "rose")

        self.assertEqual({"Test": ['rose']}, self.plantation.plants)
        self.assertEqual(f"Test planted it's first rose.", result)

        result = self.plantation.planting('Test', "rose2")
        self.assertEqual({"Test": ['rose', "rose2"]}, self.plantation.plants)
        self.assertEqual(f"Test planted rose2.", result)

    def test_str(self):
        self.plantation.hire_worker("Test")
        self.plantation.hire_worker("Test2")

        self.plantation.planting("Test", 'rose')
        self.plantation.planting("Test2", 'rose2')

        result = str(self.plantation)

        expected_value = f"Plantation size: 2\nTest, Test2\nTest planted: rose\nTest2 planted: rose2"
        self.assertEqual(expected_value, result)

        self.plantation.plants = {}
        self.plantation.planting("Test", 'rose')
        self.plantation.planting("Test", 'rose2')

        result = str(self.plantation)

        expected_value = f"Plantation size: 2\nTest, Test2\nTest planted: rose, rose2"
        self.assertEqual(expected_value, result)

    def test_repr(self):
        self.plantation.hire_worker("Test")
        self.plantation.hire_worker("Test2")

        result = repr(self.plantation)
        expected_result = f"Size: 2\nWorkers: Test, Test2"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
