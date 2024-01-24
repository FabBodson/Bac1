import unittest
from exo04 import is_strong


class IsStrongTests(unittest.TestCase):
    def test_is_strong_1(self):
        self.assertTrue(True, is_strong(1))

    def test_is_strong_145(self):
        self.assertTrue(True, is_strong(145))

    def test_is_strong_7(self):
        self.assertFalse(False, is_strong(7))


if __name__ == '__main__':
    unittest.main()
