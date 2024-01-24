import unittest
from exo06 import count_rabbits

class CountRabbitsTests(unittest.TestCase):

    def test_count_rabbits_10(self):
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], count_rabbits(10))


if __name__ == '__main__':
    unittest.main()

