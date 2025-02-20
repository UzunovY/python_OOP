from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Test_name", "Test_type", "Test_sound")

    def test_init_correct_data(self):
        self.assertEqual("Test_name", self.mammal.name)
        self.assertEqual("Test_type", self.mammal.type)
        self.assertEqual("Test_sound", self.mammal.sound)

    def test_make_sound_if_message_returned_is_correct(self):
        self.assertEqual("Test_name makes Test_sound", self.mammal.make_sound())

    def test_get_kingdom_returns_correct_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_if_info_returns_correct_message(self):
        self.assertEqual("Test_name is of type Test_type", self.mammal.info())


if __name__ == "__main__":
    main()
