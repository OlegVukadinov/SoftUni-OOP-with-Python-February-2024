from unittest import TestCase, main

from project.restaurant import Restaurant


class TestRestaurant(TestCase):

    def setUp(self):
        self.restaurant = Restaurant("Oleg Restaurant", 10)
        self.restaurant.add_waiter("Oleg")
        self.restaurant.add_waiter("Alice")
        self.restaurant.waiters[0]['total_earnings'] = 100
        self.restaurant.waiters[1]['total_earnings'] = 200

    def test_init(self):
        self.restaurant = Restaurant("Oleg Restaurant", 10)
        self.assertEqual(self.restaurant.name, "Oleg Restaurant")
        self.assertEqual(self.restaurant.capacity, 10)
        self.assertEqual(self.restaurant.waiters, [])

    def test_for_invalid_name(self):
        with self.assertRaises(ValueError) as ex:
            Restaurant("", 5)
        self.assertEqual("Invalid name!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            Restaurant("   ", 5)
        self.assertEqual("Invalid name!", str(ex.exception))

    def test_for_invalid_capacity(self):
        with self.assertRaises(ValueError) as ex:
            Restaurant("Oleg Restaurant", -5)
        self.assertEqual("Invalid capacity!", str(ex.exception))

    def test_for_valid_properties(self):
        self.restaurant = Restaurant("Oleg Restaurant", 10)
        self.restaurant.name = "New Restaurant"
        self.restaurant.capacity = 20

        self.assertEqual(self.restaurant.name, "New Restaurant")
        self.assertEqual(self.restaurant.capacity, 20)

    def test_add_new_waiter(self):
        # Test adding a new waiter
        #self.restaurant.add_waiter("Pesho")
        self.assertEqual(self.restaurant.add_waiter("Pesho"), "The waiter Pesho has been added.")
        self.assertEqual(len(self.restaurant.waiters), 3)
        self.assertEqual(self.restaurant.waiters[2]['name'], "Pesho")

    def test_add_existing_waiter(self):  # ???
        # Test adding an existing waiter
        self.assertEqual(self.restaurant.add_waiter("Oleg"), "The waiter Oleg already exists!")
        self.assertEqual(len(self.restaurant.waiters), 2)

    # def test_add_waiter_to_full_capacity(self):
    #     # Test adding a waiter when the restaurant is at full capacity
    #     self.restaurant.add_waiter("Phill")  # Fill up the restaurant
    #     self.assertEqual(self.restaurant.add_waiter("Bob"), "No more places!")
    #     self.assertEqual(len(self.restaurant.waiters), 1)  # Capacity is 2

    def test_remove_waiter(self):
        self.assertEqual(self.restaurant.remove_waiter("Oleg"), "The waiter Oleg has been removed.")
        self.assertEqual(self.restaurant.remove_waiter("Bob"), "No waiter found with the name Bob.")

    def test_get_waiters(self):
        self.assertEqual(len(self.restaurant.get_waiters()), 2)
        self.assertEqual(len(self.restaurant.get_waiters(min_earnings=150)), 1)
        self.assertEqual(len(self.restaurant.get_waiters(max_earnings=150)), 1)
        self.assertEqual(len(self.restaurant.get_waiters(min_earnings=150, max_earnings=250)), 1)

    def test_get_total_earnings(self):
        self.assertEqual(self.restaurant.get_total_earnings(), 300)


if __name__ == '__main__':
    main()
