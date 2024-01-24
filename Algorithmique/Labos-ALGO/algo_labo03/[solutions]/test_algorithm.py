import random
import copy
import unittest

from algorithm import apply_merge_sort, __merge as merge


class ApplyMergeSortTestCase(unittest.TestCase):

    def test_basic_even(self):
        data = [2, 4, 1, 6, 8, 5, 3, 7]
        reality = apply_merge_sort(data)

        # Assert original data has not changed
        self.assertIsNot(data, reality)
        self.assertListEqual(data, [2, 4, 1, 6, 8, 5, 3, 7])

        # Assert the result has been correctly sorted
        expectation = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertListEqual(reality, expectation)

    def test_basic_odd(self):
        data = [2, 4, 1, 6, 5, 3, 7]
        reality = apply_merge_sort(data)

        # Assert original data has not changed
        self.assertIsNot(data, reality)
        self.assertListEqual(data, [2, 4, 1, 6, 5, 3, 7])

        # Assert the result has been correctly sorted
        expectation = [1, 2, 3, 4, 5, 6, 7]
        self.assertListEqual(reality, expectation)

    def test_empty(self):
        data = []
        reality = apply_merge_sort(data)

        # Assert original data has not changed
        self.assertIsNot(data, reality)
        self.assertListEqual(data, [])

        # Assert the result has been correctly sorted
        expectation = []
        self.assertListEqual(reality, expectation)

    def test_only_1_element(self):
        data = [5]
        reality = apply_merge_sort(data)

        # Assert original data has not changed
        self.assertIsNot(data, reality)
        self.assertListEqual(data, [5])

        # Assert the result has been correctly sorted
        expectation = [5]
        self.assertListEqual(reality, expectation)

    def test_with_duplicates(self):
        data = [9, 8, 3, 5, 3, 0, 2, 3]
        reality = apply_merge_sort(data)

        # Assert original data has not changed
        self.assertIsNot(data, reality)
        self.assertListEqual(data, [9, 8, 3, 5, 3, 0, 2, 3])

        # Assert the result has been correctly sorted
        expectation = [0, 2, 3, 3, 3, 5, 8, 9]
        self.assertListEqual(reality, expectation)

    def test_1000_elements(self):
        data = [i for i in range(0, 1000)]
        random.shuffle(data)
        data_deep_copy = copy.deepcopy(data)
        reality = apply_merge_sort(data)

        # Assert original data has not changed
        self.assertIsNot(data, reality)
        self.assertListEqual(data, data_deep_copy)

        # Assert the result has been correctly sorted
        expectation = [i for i in range(0, 1000)]
        self.assertListEqual(reality, expectation)


class MergeTestCase(unittest.TestCase):

    def test_even(self):
        left = [4, 3, 2, 1]
        right = [8, 7, 6, 5]
        reality = merge(left, right)

        # Assert original data has not changed
        self.assertIsNot(reality, left)
        self.assertIsNot(reality, right)
        self.assertListEqual(left, [4, 3, 2, 1])
        self.assertListEqual(right, [8, 7, 6, 5])

        # Assert the result has been correctly merged
        expectation = [4, 3, 2, 1, 8, 7, 6, 5]
        self.assertListEqual(reality, expectation)

    def test_odd(self):
        left = [4, 3, 2]
        right = [8, 7, 6]
        reality = merge(left, right)

        # Assert original data has not changed
        self.assertIsNot(reality, left)
        self.assertIsNot(reality, right)
        self.assertListEqual(left, [4, 3, 2])
        self.assertListEqual(right, [8, 7, 6])

        # Assert the result has been correctly merged
        expectation = [4, 3, 2, 8, 7, 6]
        self.assertListEqual(reality, expectation)

    def test_single_values(self):
        left = [4]
        right = [2]
        reality = merge(left, right)

        # Assert original data has not changed
        self.assertIsNot(reality, left)
        self.assertIsNot(reality, right)
        self.assertListEqual(left, [4])
        self.assertListEqual(right, [2])

        # Assert the result has been correctly merged
        expectation = [2, 4]
        self.assertListEqual(reality, expectation)

    def test_single_values_reverse(self):
        left = [2]
        right = [4]
        reality = merge(left, right)

        # Assert original data has not changed
        self.assertIsNot(reality, left)
        self.assertIsNot(reality, right)
        self.assertListEqual(left, [2])
        self.assertListEqual(right, [4])

        # Assert the result has been correctly merged
        expectation = [2, 4]
        self.assertListEqual(reality, expectation)

    def test_no_left(self):
        left = []
        right = [4, 6, 5, 7]
        reality = merge(left, right)

        # Assert original data has not changed
        self.assertIsNot(reality, left)
        self.assertIsNot(reality, right)
        self.assertListEqual(left, [])
        self.assertListEqual(right, [4, 6, 5, 7])

        # Assert the result has been correctly merged
        expectation = [4, 6, 5, 7]
        self.assertListEqual(reality, expectation)

    def test_no_right(self):
        left = [4, 6, 5, 7]
        right = []
        reality = merge(left, right)

        # Assert original data has not changed
        self.assertIsNot(reality, left)
        self.assertIsNot(reality, right)
        self.assertListEqual(left, [4, 6, 5, 7])
        self.assertListEqual(right, [])

        # Assert the result has been correctly merged
        expectation = [4, 6, 5, 7]
        self.assertListEqual(reality, expectation)

    def test_both_empty(self):
        left = []
        right = []
        reality = merge(left, right)

        # Assert original data has not changed
        self.assertIsNot(reality, left)
        self.assertIsNot(reality, right)
        self.assertListEqual(left, [])
        self.assertListEqual(right, [])

        # Assert the result has been correctly merged
        expectation = []
        self.assertListEqual(reality, expectation)
