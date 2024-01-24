import unittest
from classes.files import FileWordSource


class WordSourceTest(unittest.TestCase):

    def test_provides_with_words_count(self):
        words = FileWordSource("../files/words.txt")

        found = words.count
        self.assertEqual(5, found)

    def test_provides_with_word_given_pos(self):
        words = FileWordSource("../files/words.txt")

        found = words.words[2]
        self.assertEqual("password", found)

    def test_can_append_word(self):
        words = FileWordSource("../files/words.txt")
        words.words.append("ici")

        self.assertEqual(["123456", "bonjour", "password", "mot de passe", "Die", "ici"], words.words)
        self.assertEqual("ici", words.words[-1])
