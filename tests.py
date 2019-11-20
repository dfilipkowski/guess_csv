import unittest

from run import guess_csv, Seps


class TestMethods(unittest.TestCase):

    def test_first_case(self):
        argument = "input_1.csv"
        # print(guess_csv(argument))
        # print(Seps(';', ',', '.'))
        self.assertEqual(guess_csv(argument), Seps(';', '.', ','))

    def test_second_case(self):
        argument = "input_2.csv"
        self.assertEqual(guess_csv(argument), Seps(';', '.', ','))

    def test_third_case(self):
        argument = "input_3.csv"
        self.assertEqual(guess_csv(argument), Seps(';', '.', ','))


if __name__ == '__main__':
    unittest.main()