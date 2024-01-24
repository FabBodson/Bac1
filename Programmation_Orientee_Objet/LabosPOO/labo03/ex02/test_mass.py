import unittest

from ex02.mass import Mass


class MassTest(unittest.TestCase):

    def test_reflexive_equivalency(self):
        """
        Reflexive: (x == x) == True
        """
        basic_mass = Mass(42.21)
        different_mass = Mass(21.42)
        self.assertTrue(basic_mass == basic_mass)
        self.assertTrue(different_mass == different_mass)

    def test_symmetric_equivalency(self):
        """
        Symmetric: ((x == y) and (y == x)) == True
        """
        basic_mass = Mass(42.21)
        equivalent_mass = Mass(42.21)
        self.assertTrue(basic_mass == equivalent_mass)
        self.assertTrue(equivalent_mass == basic_mass)

    def test_transitive_equivalency(self):
        """
        Transitive: if x == y and y == z, x == z
        """
        basic_mass = Mass(42.21)
        equivalent_mass = Mass(42.21)
        equivalent_mass_2 = Mass(42.21)
        self.assertTrue(basic_mass == equivalent_mass)
        self.assertTrue(equivalent_mass == equivalent_mass_2)
        self.assertTrue(basic_mass == equivalent_mass_2)

    def test_no_equivalency(self):
        basic_mass = Mass(42.21)
        different_mass = Mass(21.42)
        no_mass = None
        self.assertFalse(basic_mass == different_mass)
        self.assertFalse(different_mass == basic_mass)
        self.assertFalse(basic_mass == no_mass)
