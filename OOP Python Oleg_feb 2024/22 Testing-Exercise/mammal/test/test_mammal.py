from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Lion", "Zver", "Roar")

    def test_correct_init(self):
        self.assertEqual("Lion", self.mammal.name)
        self.assertEqual("Zver", self.mammal.type)
        self.assertEqual("Roar", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual( f"Lion makes Roar", result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual( f"Lion is of type Zver", result)


if __name__ == "__main__":
    main()





