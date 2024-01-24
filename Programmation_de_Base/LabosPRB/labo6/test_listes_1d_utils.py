import unittest

import listes_1d_utils as utils


class IsEmptyTestCase(unittest.TestCase):

    def test_empty(self):
        self.assertTrue(utils.est_vide([]))

    def test_one_item(self):
        self.assertFalse(utils.est_vide([1]))

    def test_more_items(self):
        self.assertFalse(utils.est_vide([1, 2, 3, 4, 5]))


class ConvertToTextTestCase(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(utils.convertir_en_texte([]), '[]')

    def test_one_item(self):
        self.assertEqual(utils.convertir_en_texte([1]), '[1]')

    def test_multiple_items(self):
        self.assertEqual(utils.convertir_en_texte([1, 2, 3]), '[1, 2, 3]')


class GenerateTestCase(unittest.TestCase):

    def test_one(self):
        self.assertEqual(utils.generer(0, 1, 1), [0])

    def test_three_values(self):
        self.assertEqual(utils.generer(0, 3, 1), [0, 1, 2])

    def test_many_values(self):
        self.assertEqual(utils.generer(0, 10, 1), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_high_step(self):
        self.assertEqual(utils.generer(0, 50, 5), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45])

    def test_zero_step(self):
        self.assertIsNone(utils.generer(0, 10, 0))

    def test_negative_step(self):
        self.assertIsNone(utils.generer(0, 10, -1))

    def test_start_equals_end(self):
        self.assertEqual(utils.generer(1, 1, 1), [])

    def test_start_is_higher_than_end(self):
        self.assertEqual(utils.generer(2, 1, 1), [])


class CloneTestCase(unittest.TestCase):

    def test_empty(self):
        data = []
        self.assertListEqual(data, utils.cloner(data))

    def test_one_item(self):
        data = [1]
        self.assertListEqual(data, utils.cloner(data))

    def test_two_items(self):
        data = [1, 2]
        self.assertListEqual(data, utils.cloner(data))

    def test_multiple_items(self):
        data = [1, 2, 3]
        self.assertListEqual(data, utils.cloner(data))

    def test_different_reference(self):
        data = [1, 2, 3]
        self.assertIsNot(data, utils.cloner(data))


class DuplicateWithoutDoubles(unittest.TestCase):

    def test_empty(self):
        self.assertListEqual(utils.dupliquer_sans_doublons([]), [])

    def test_one_item(self):
        self.assertListEqual(utils.dupliquer_sans_doublons([1]), [1])

    def test_no_doubles(self):
        self.assertListEqual(utils.dupliquer_sans_doublons([1, 2, 3]), [1, 2, 3])

    def test_doubles_in_random_location(self):
        self.assertListEqual(utils.dupliquer_sans_doublons([1, 2, 3, 2, 5]), [1, 2, 3, 5])

    def test_doubles_next_to_each_other(self):
        self.assertListEqual(utils.dupliquer_sans_doublons([1, 2, 3, 3, 5]), [1, 2, 3, 5])

    def test_doubles_at_extremes(self):
        self.assertListEqual(utils.dupliquer_sans_doublons([1, 2, 3, 4, 1]), [1, 2, 3, 4])

    def test_multiple_doubles(self):
        self.assertListEqual(utils.dupliquer_sans_doublons([1, 1, 3, 4, 4]), [1, 3, 4])

    def test_multiple_doubles_next_to_each_other(self):
        self.assertListEqual(utils.dupliquer_sans_doublons([1, 1, 3, 3, 5]), [1, 3, 5])

    def test_triples(self):
        self.assertListEqual(utils.dupliquer_sans_doublons([1, 1, 3, 3, 3]), [1, 3])

    def test_original_not_modified(self):
        liste = [1, 1, 2, 2]
        self.assertIsNot(utils.dupliquer_sans_doublons(liste), liste)


class CountEvenAndOddTestCase(unittest.TestCase):

    def test_empty(self):
        even, odd = utils.compter_pairs_et_impairs([])
        self.assertEqual(even, 0)
        self.assertEqual(odd, 0)

    def test_one_even_item(self):
        even, odd = utils.compter_pairs_et_impairs([2])
        self.assertEqual(even, 1)
        self.assertEqual(odd, 0)

    def test_one_odd_item(self):
        even, odd = utils.compter_pairs_et_impairs([3])
        self.assertEqual(even, 0)
        self.assertEqual(odd, 1)

    def test_value_0(self):
        even, odd = utils.compter_pairs_et_impairs([0])
        self.assertEqual(even, 1)
        self.assertEqual(odd, 0)

    def test_value_1(self):
        even, odd = utils.compter_pairs_et_impairs([1])
        self.assertEqual(even, 0)
        self.assertEqual(odd, 1)

    def test_multiple_values(self):
        even, odd = utils.compter_pairs_et_impairs([1, 2, 3, 4, 5])
        self.assertEqual(even, 2)
        self.assertEqual(odd, 3)

    def test_multiple_values_with_negatives(self):
        even, odd = utils.compter_pairs_et_impairs([1, -2, 3, 4, -5])
        self.assertEqual(even, 2)
        self.assertEqual(odd, 3)


class ExtractEvenAndOddTestCase(unittest.TestCase):

    def test_empty(self):
        even, odd = utils.extraire_pairs_et_impairs([])
        self.assertEqual(even, [])
        self.assertEqual(odd, [])

    def test_one_even_item(self):
        even, odd = utils.extraire_pairs_et_impairs([2])
        self.assertEqual(even, [2])
        self.assertEqual(odd, [])

    def test_one_odd_item(self):
        even, odd = utils.extraire_pairs_et_impairs([3])
        self.assertEqual(even, [])
        self.assertEqual(odd, [3])

    def test_value_0(self):
        even, odd = utils.extraire_pairs_et_impairs([0])
        self.assertEqual(even, [0])
        self.assertEqual(odd, [])

    def test_value_1(self):
        even, odd = utils.extraire_pairs_et_impairs([1])
        self.assertEqual(even, [])
        self.assertEqual(odd, [1])

    def test_multiple_values(self):
        even, odd = utils.extraire_pairs_et_impairs([1, 2, 3, 4, 5])
        self.assertEqual(even, [2, 4])
        self.assertEqual(odd, [1, 3, 5])

    def test_multiple_values_with_negatives(self):
        even, odd = utils.extraire_pairs_et_impairs([1, -2, 3, 4, -5])
        self.assertEqual(even, [-2, 4])
        self.assertEqual(odd, [1, 3, -5])


class ConcatToIntTestCase(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(utils.concatener_en_entier([]), 0)

    def test_one_item_one_digit(self):
        self.assertEqual(utils.concatener_en_entier([9]), 9)

    def test_one_item_multiple_digits(self):
        self.assertEqual(utils.concatener_en_entier([42]), 42)

    def test_one_item_negative(self):
        self.assertEqual(utils.concatener_en_entier([-9]), 9)

    def test_multiple_items(self):
        self.assertEqual(utils.concatener_en_entier([1, 2, 3, 5, 8, 13]), 1235813)

    def test_multiple_items_with_negatives(self):
        self.assertEqual(utils.concatener_en_entier([1, -2, 3, -5, 8, -13]), 1235813)


class ContainsSubListTestCase(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(utils.contient_sous_liste([], []), True)

    def test_empty_sublist(self):
        self.assertEqual(utils.contient_sous_liste([1, 2, 3], []), True)

    def test_lists_with_one_item(self):
        self.assertEqual(utils.contient_sous_liste([1], [1]), True)

    def test_sublist_with_one_item(self):
        self.assertEqual(utils.contient_sous_liste([1, 2], [1]), True)

    def test_sublist_with_two_items_beginning(self):
        self.assertEqual(utils.contient_sous_liste([1, 2, 3, 4], [1, 2]), True)

    def test_sublist_with_two_items_middle(self):
        self.assertEqual(utils.contient_sous_liste([1, 2, 3, 4], [2, 3]), True)

    def test_sublist_with_two_items_end(self):
        self.assertEqual(utils.contient_sous_liste([1, 2, 3, 4], [3, 4]), True)

    def test_list_with_repeats_beginning(self):
        self.assertEqual(utils.contient_sous_liste([1, 2, 3, 1, 2, 3], [1, 2]), True)

    def test_list_with_repeats_middle(self):
        self.assertEqual(utils.contient_sous_liste([1, 2, 3, 1, 2, 3], [3, 1]), True)

    def test_list_with_repeats_end(self):
        self.assertEqual(utils.contient_sous_liste([1, 2, 3, 1, 2, 3], [2, 3]), True)

    def test_not_a_sublist(self):
        self.assertEqual(utils.contient_sous_liste([1, 2, 3], [4, 5, 6]), False)

    def test_list_with_repeats_not_a_sublist(self):
        self.assertEqual(utils.contient_sous_liste([1, 2, 3, 1, 2, 3], [1, 3, 2]), False)

    def test_bigger_sublist(self):
        self.assertEqual(utils.contient_sous_liste([1, 2, 3], [1, 2, 3, 4]), False)

    def test_sublist_with_fake_neighbor(self):
        self.assertEqual(utils.contient_sous_liste([1, 2, 3, 3, 5, 6], [3, 5]), True)


class SplitInTwoTestCase(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(utils.separer_en_deux([]), ([], []))

    def test_one_item(self):
        self.assertEqual(utils.separer_en_deux([1]), ([], [1]))

    def test_one_item_with_index(self):
        self.assertEqual(utils.separer_en_deux([1], 0), ([], [1]))

    def test_two_items(self):
        self.assertEqual(utils.separer_en_deux([1, 2]), ([1], [2]))

    def test_two_items_with_index_1(self):
        self.assertEqual(utils.separer_en_deux([1, 2], 1), ([1], [2]))

    def test_two_items_with_index_2(self):
        self.assertEqual(utils.separer_en_deux([1, 2], 2), ([1, 2], []))

    def test_multiple_items_even(self):
        self.assertEqual(utils.separer_en_deux([1, 2, 3, 4]), ([1, 2], [3, 4]))

    def test_multiple_items_even_with_index(self):
        self.assertEqual(utils.separer_en_deux([1, 2, 3, 4], 3), ([1, 2, 3], [4]))

    def test_multiple_items_odd(self):
        self.assertEqual(utils.separer_en_deux([1, 2, 3, 4, 5]), ([1, 2], [3, 4, 5]))

    def test_multiple_items_odd_with_index(self):
        self.assertEqual(utils.separer_en_deux([1, 2, 3, 4, 5], 1), ([1], [2, 3, 4, 5]))

    def test_multiple_items_index_0(self):
        self.assertEqual(utils.separer_en_deux([1, 2, 3, 4, 5], 0), ([], [1, 2, 3, 4, 5]))
