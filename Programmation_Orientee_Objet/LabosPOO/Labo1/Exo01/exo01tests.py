import unittest
from exo01 import sum_of_terms


class SumOfTermsTests(unittest.TestCase):
    def test_sum_of_term_0_equals_1(self):
        self.assertEqual(1,  sum_of_terms(0))

    def test_sum_of_term_1_equals_8(self):
        self.assertEqual(8,  sum_of_terms(1))

    def test_sum_of_term_2_equals_27(self):
        self.assertEqual(27,  sum_of_terms(2))

    def test_sum_of_terms_minus_10_equal_0(self):
        self.assertEqual(0,  sum_of_terms(-10))


if __name__ == '__main__':
    unittest.main()
