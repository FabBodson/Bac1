import unittest
from algo_labo03.algorithm import apply_merge_sort
import random
import copy


class ApplyMergeSortTestCase(unittest.TestCase):
    def test_basic(self):
        a = [2, 4, 1, 6, 8, 5, 3, 7]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]

        self.assertListEqual(expected, apply_merge_sort(a))
        self.assertIsNot(a, apply_merge_sort(a))

    def test_one_element(self):
        a = [1]
        got = apply_merge_sort(a)
        expected = [1]

        self.assertListEqual(expected, got)
        self.assertIsNot(a, got)

    def test_no_element(self):
        a = []
        got = apply_merge_sort(a)
        expected = []

        self.assertListEqual(expected, got)
        self.assertIsNot(a, got)

    def test_liste_impaire(self):
        a = [2, 4, 1, 6, 5, 3, 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        got = apply_merge_sort(a)

        self.assertListEqual(expected, got)
        self.assertIsNot(a, got)

    def test_doublons(self):
        a = [5, 4, 1, 6, 8, 5, 3, 7]
        expected = [1, 3, 4, 5, 5, 6, 7, 8]
        got = apply_merge_sort(a)

        self.assertListEqual(expected, got)
        self.assertIsNot(a, got)

    def test_1000_elements(self):
        a = [i for i in range(0, 1000)]
        random.shuffle(a)
        deep_copy = copy.deepcopy(a)
        got = apply_merge_sort(a)

        # Vérifie si liste de base et liste obtenue ont memes éléments
        # mais pas meme liste
        self.assertListEqual(a, deep_copy)
        self.assertIsNot(a, got)

        expected = [i for i in range(0, 1000)]
        self.assertListEqual(expected, got)
