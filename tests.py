import unittest

from arguments import argument_1, argument_2, argument_3, argument_4, argument_5
from run import guess_csv, Seps


class TestMethods(unittest.TestCase):

    def test_first_case(self):
        self.assertEqual(guess_csv(argument_1), Seps(';', ',', '.'))

    def test_second_case(self):
        self.assertEqual(guess_csv(argument_2), Seps(';', '.', ','))

    def test_third_case(self):
        self.assertEqual(guess_csv(argument_3), Seps(';', '.', ','))

    def test_fourth_case(self):
        self.assertEqual(guess_csv(argument_4), Seps('|', ',', '.'))

    def test_fifth_case(self):
        self.assertEqual(guess_csv(argument_5), Seps(',', '.', None))

if __name__ == '__main__':
    unittest.main()