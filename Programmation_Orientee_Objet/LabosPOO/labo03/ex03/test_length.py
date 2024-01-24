import unittest
from ex03.length import Length


class LengthTest(unittest.TestCase):

    def test_reflexive_equivalency(self):
        """
        Reflexive: (x == x) == True
        """
        basic_length = Length(42.21)
        different_length = Length(21.42)
        self.assertTrue(basic_length == basic_length)
        self.assertTrue(different_length == different_length)

    def test_symmetric_equivalency(self):
        """
        Symmetric: ((x == y) and (y == x)) == True
        """
        basic_length = Length(42.21)
        equivalent_length = Length(42.21)
        self.assertTrue(basic_length == equivalent_length)
        self.assertTrue(equivalent_length == basic_length)

    def test_transitive_equivalency(self):
        """
        Transitive: if x == y and y == z, x == z
        """
        basic_length = Length(42.21)
        equivalent_length = Length(42.21)
        equivalent_length_2 = Length(42.21)
        self.assertTrue(basic_length == equivalent_length)
        self.assertTrue(equivalent_length == equivalent_length_2)
        self.assertTrue(basic_length == equivalent_length_2)

    def test_no_equivalency(self):
        basic_length = Length(42.21)
        different_length = Length(21.42)
        no_length = None
        self.assertFalse(basic_length == different_length)
        self.assertFalse(different_length == basic_length)
        self.assertFalse(basic_length == no_length)


    def test_is_squared(self):
        basic_length = Length(42.21)
        actual = basic_length.squared()
        self.assertAlmostEqual(1781.6841, actual.__distance, 1)
