from unittest import TestCase, main

from Cat.cat import Cat


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Pancho")

    def test_correct_init(self):
        self.assertEqual("Pancho", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_feed_cat_expect_fed_and_sleepy_cat_with_increased_size(self):
        expected_result = 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_result, self.cat.size)

    def test_feed_cat_when_cat_is_fed_raises_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleeping_cat_when_cat_is_fed_makes_cat_is_not_sleepy(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_sleeping_cat_when_cat_is_hungry_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == '__main__':
    main()
