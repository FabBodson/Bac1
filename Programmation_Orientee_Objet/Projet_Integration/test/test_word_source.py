import unittest
from classes.word_source import WordSource


class WordSourceTest(unittest.TestCase):

    def test_provides_with_words_count(self):
        words = WordSource(["bonjour", "tout", "va", "bien"])

        found = words.count
        self.assertEqual(4, found)

    def test_provides_with_word_given_pos(self):
        words = WordSource(["bonjour", "tout", "va", "bien"])

        found = words[2]
        self.assertEqual("va", found)

    def test_can_append_word(self):
        words = WordSource(["bonjour", "tout", "va", "bien"])
        words.words.append("ici")

        self.assertEqual(["bonjour", "tout", "va", "bien", "ici"], words.words)
        self.assertEqual("ici", words.words[-1])