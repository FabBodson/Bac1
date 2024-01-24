import unittest
from exo07 import find_children


class FindChildrenTests(unittest.TestCase):

    def test_find_children(self):
        self.assertListEqual(['Cyril', 'Nicolas'], find_children(['Nicolas', 'Dorian', 'Cyril'], ['Nicolas', 'Cyril']))


if __name__ == '__main__':
    unittest.main()

