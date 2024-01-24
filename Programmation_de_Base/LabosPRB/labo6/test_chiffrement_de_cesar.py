import unittest

from chiffrement_de_cesar import chiffrer


class CypherTestCase(unittest.TestCase):

    def test_no_decay_empty_string(self):
        self.assertEqual(chiffrer('', 0), '')

    def test_no_decay_one_upper_char(self):
        self.assertEqual(chiffrer('A', 0), 'A')

    def test_no_decay_more_upper_chars(self):
        self.assertEqual(chiffrer('ABC', 0), 'ABC')

    def test_no_decay_one_lower_char(self):
        self.assertEqual(chiffrer('a', 0), 'a')

    def test_no_decay_more_lower_chars(self):
        self.assertEqual(chiffrer('abc', 0), 'abc')

    def test_no_decay_mixed_chars(self):
        self.assertEqual(chiffrer('AbCdEf', 0), 'AbCdEf')

    def test_positive_decay_empty_string(self):
        self.assertEqual(chiffrer('', 3), '')

    def test_positive_decay_one_upper_char(self):
        self.assertEqual(chiffrer('A', 3), 'D')

    def test_positive_decay_more_upper_chars(self):
        self.assertEqual(chiffrer('ABC', 3), 'DEF')

    def test_positive_decay_one_lower_char(self):
        self.assertEqual(chiffrer('a', 3), 'd')

    def test_positive_decay_more_lower_chars(self):
        self.assertEqual(chiffrer('abc', 3), 'def')

    def test_positive_decay_mixed_chars(self):
        self.assertEqual(chiffrer('AbCdEf', 3), 'DeFgHi')

    def test_positive_high_decay(self):
        self.assertEqual(chiffrer('AbCdEf', 42), 'QrStUv')

    def test_negative_decay_empty_string(self):
        self.assertEqual(chiffrer('', -3), '')

    def test_negative_decay_one_upper_char(self):
        self.assertEqual(chiffrer('A', -3), 'X')

    def test_negative_decay_more_upper_chars(self):
        self.assertEqual(chiffrer('ABC', -3), 'XYZ')

    def test_negative_decay_one_lower_char(self):
        self.assertEqual(chiffrer('a', -3), 'x')

    def test_negative_decay_more_lower_chars(self):
        self.assertEqual(chiffrer('abc', -3), 'xyz')

    def test_negative_decay_mixed_chars(self):
        self.assertEqual(chiffrer('AbCdEf', -3), 'XyZaBc')

    def test_negative_high_decay(self):
        self.assertEqual(chiffrer('AbCdEf', -42), 'KlMnOp')

    def test_reciprocity(self):
        original = 'AbCdEf'
        decay = 3
        encrypted = chiffrer(original, +decay)
        decrypted = chiffrer(encrypted, -decay)
        self.assertEqual(original, decrypted)

    def test_with_illegal_chars_numbers(self):
        self.assertEqual(chiffrer('AbC0123456789dEf', -3), 'XyZ0123456789aBc')

    def test_with_illegal_chars_punctuation(self):
        self.assertEqual(chiffrer('AbC.,;:?!"\'_-+(){}[]<>dEf', -3), 'XyZ.,;:?!"\'_-+(){}[]<>aBc')

    def test_with_illegal_chars_space(self):
        self.assertEqual(chiffrer('A b C d E f', -3), 'X y Z a B c')

    def test_with_illegal_chars_accents(self):
        self.assertEqual(chiffrer('AàâbéCçdèEf', -3), 'XàâyéZçaèBc')

