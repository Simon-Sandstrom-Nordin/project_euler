import unittest
from main import *


class SyntaxTest(unittest.TestCase):

    def test_correct_syntax(self):
        self.assertEqual(check_syntax("Fe12"), "Formeln är syntaktiskt korrekt")

    def test_capital_letter_error(self):
        self.assertEqual(check_syntax("oa"), "Saknad stor bokstav vid radslutet oa")

    def test_number_error(self):
        self.assertEqual(check_syntax("Cr0"), "För litet tal vid radslutet ")


if __name__ == '__test__':
    unittest.main()
