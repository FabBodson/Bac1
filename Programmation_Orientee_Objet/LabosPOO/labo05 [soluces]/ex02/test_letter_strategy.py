import unittest

import ex02_steganography as steganography


class LetterStrategyTests(unittest.TestCase):
    def test_decrypts_simple_case(self):
        decrypter = steganography.LetterStrategy()
        with open('letter_sample.txt') as source:
            with open('destination.txt', 'w') as destination:
                decrypter.decrypt(source, destination)

        with(open('destination.txt')) as output:
            self.assertEqual('pershingsailsfromnyjunei', output.read().strip())


if __name__ == '__main__':
    unittest.main()
