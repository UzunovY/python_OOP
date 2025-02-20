from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Hero", 10, 100.0, 5.0)
        self.enemy = Hero("Enemy", 10, 100.0, 5.0)

    def test_init_correct_initialization(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(5.0, self.hero.damage)

    def test_battle_enemy_with_same_name_raises(self):
        self.enemy.username = "Hero"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_health_less_or_equal_to_zero_raises(self):
        self.hero.health = -1

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_health_less_or_equal_to_zero_raises(self):
        self.enemy.health = -1

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

    def test_battle_ending_in_a_draw(self):
        self.hero.health = 10
        self.enemy.health = 10

        battle = self.hero.battle(self.enemy)

        self.assertEqual(-40, self.hero.health)
        self.assertEqual(-40, self.enemy.health)
        self.assertEqual("Draw", battle)

        self.hero.health = 50
        self.enemy.health = 50

        battle = self.hero.battle(self.enemy)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy.health)
        self.assertEqual("Draw", battle)

    def test_battle_when_hero_wins(self):
        self.hero.health = 100
        self.enemy.health = 40

        battle = self.hero.battle(self.enemy)

        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(10, self.hero.damage)
        self.assertEqual(-10, self.enemy.health)
        self.assertEqual("You win", battle)

        self.hero.health = 100
        self.enemy.health = 50
        self.hero.level = 10
        self.hero.damage = 5

        battle = self.hero.battle(self.enemy)

        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(10, self.hero.damage)
        self.assertEqual(0, self.enemy.health)
        self.assertEqual("You win", battle)

    def test_battle_when_hero_loses(self):

        battle = self.hero.battle(self.enemy)

        self.assertEqual(11, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(10, self.enemy.damage)
        self.assertEqual(50, self.hero.health)
        self.assertEqual("You lose", battle)

    def test_hero_string_representation_returning_correct_message(self):
        self.assertEqual("Hero Hero: 10 lvl\n"
                         "Health: 100.0\n"
                         "Damage: 5.0\n",
                         str(self.hero)
                         )


if __name__ == "__main__":
    main()
