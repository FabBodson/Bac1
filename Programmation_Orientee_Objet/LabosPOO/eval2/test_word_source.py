import unittest
from files import FileWordSource


class WordSourceTest(unittest.TestCase):
    def test_something(self):
        words = FileWordSource("word_source.txt")
        word_list = words.get_pwd_from_file()

        self.assertEqual(5, words.count())
        self.assertEqual("bonjour", word_list[1])
        self.assertNotEqual(4, words.count())
        self.assertNotEqual("lol", word_list[1])
