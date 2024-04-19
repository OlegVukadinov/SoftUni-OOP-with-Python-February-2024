from unittest import TestCase, main

from project import Hero


class TestHero(TestCase):
    username = "Hercules"
    level = 5
    health = 25.6
    damage = 10.2

    def setUp(self):
        self.hero = Hero("Hercules", self.level, self.health, self.damage)

    def test_correct_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_attributes_types(self):
        self.assertTrue(self.hero.username, str)
        self.assertTrue(self.hero.level, int)
        self.assertTrue(self.hero.health, float)
        self.assertTrue(self.hero.damage, float)

    def test_battle_enemy_same_username_hero(self):
        enemy_hero = Hero("Hercules", self.level, self.health, self.damage)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_health_is_zero(self):
        self.hero.health = 0
        enemy_hero = Hero("Devil", self.level, self.health, self.damage)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_hero_health_is_negative(self):
        self.hero.health = -1
        enemy_hero = Hero("Devil", self.level, self.health, self.damage)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_is_zero(self):
        enemy_hero = Hero("Devil", self.level, 0, self.damage)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight Devil. He needs to rest", str(ex.exception))

    def test_battle_enemy_health_is_negative(self):
        enemy_hero = Hero("Devil", self.level, -1, self.damage)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight Devil. He needs to rest", str(ex.exception))

    def test_draw(self):
        enemy_hero = Hero("Devil", self.level, self.health, self.damage)

        self.assertEqual("Draw", self.hero.battle(enemy_hero))
        self.assertEqual(5, self.hero.level)
        self.assertEqual(-25.4, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_hero_wins(self):
        enemy_hero = Hero("Devil", 1, 1, 1)

        self.assertEqual("You win", self.hero.battle(enemy_hero))
        self.assertEqual(6, self.hero.level)
        self.assertEqual(29.6, self.hero.health)
        self.assertEqual(15.2, self.hero.damage)

    def test_hero_looses(self):
        self.hero.health = 10
        self.hero.damage = 10
        enemy_hero = Hero("Devil", 100, 100, 100)

        self.assertEqual("You lose", self.hero.battle(enemy_hero))
        self.assertEqual(101, enemy_hero.level)
        self.assertEqual(55, enemy_hero.health)
        self.assertEqual(105, enemy_hero.damage)

    def test_str(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
                   f"Health: {self.health}\n" \
                   f"Damage: {self.damage}\n"

        self.assertEqual(expected, self.hero.__str__())


if __name__ == "__main__":
    main()
