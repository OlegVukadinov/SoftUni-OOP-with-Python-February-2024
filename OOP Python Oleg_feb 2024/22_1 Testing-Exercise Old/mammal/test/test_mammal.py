from unittest import TestCase, main

from project import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "Test type", "test sound")

    def test_correct_init(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("Test type", self.mammal.type)
        self.assertEqual("test sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_what_make_sound_returns(self):
        result = self.mammal.make_sound()
        self.assertEqual("Test makes test sound", result)

    def test_what_get_kingdom_returns(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_what_info_returns(self):
        result = self.mammal.info()
        self.assertEqual("Test is of type Test type", result)


if __name__ == "__main__":
    main()
