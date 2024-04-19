from unittest import TestCase, main

from Worker.worker import Worker


class WorkerTests(TestCase):

    def test_correct_initialization(self):
        # Act
        worker = Worker("Test", 1000, 60)

        # Assert
        self.assertEqual("Test", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(60, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_works(self):
        # Arrange
        worker = Worker("Test", 1000, 60)
        self.assertEqual(0, worker.money)
        self.assertEqual(60, worker.energy)

        # Act
        worker.work()

        # Assert
        current_expected_money = 1000
        self.assertEqual(current_expected_money, worker.money)
        expected_energy = 60 - 1
        self.assertEqual(expected_energy, worker.energy)

        worker.work()
        # Worker works again
        current_expected_money = 1000 + 1000
        self.assertEqual(current_expected_money, worker.money)
        expected_energy = 60 - 1 - 1
        self.assertEqual(expected_energy, worker.energy)

    def test_has_no_energy_can_not_work(self):
        worker = Worker("Test", 1000, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()  # act

        self.assertEqual('Not enough energy.', str(ex.exception))  # assert

    def test_has_no_enrgy_can_not_work_with_negative_energy(self):
        worker = Worker("Test", 1000, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()  # act

        self.assertEqual('Not enough energy.', str(ex.exception)) #ex.exception.args[0] # assert

    def test_worker_energy_is_increased_when_worker_rests(self):
        # Arrange
        worker = Worker("Test", 1000, 60)
        self.assertEqual(60, worker.energy)

        # Act
        worker.rest()
        self.assertEqual(61, worker.energy)

        worker.rest()
        self.assertEqual(62, worker.energy)

    def test_get_info(self):
        # Arrange
        worker = Worker("Test", 1000, 60)

        # Act
        result = worker.get_info()
        # Assert
        expected_result = 'Test has saved 0 money.'
        self.assertEqual(expected_result, result)

        worker.work()
        result = worker.get_info()
        expected_result = 'Test has saved 1000 money.'
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
