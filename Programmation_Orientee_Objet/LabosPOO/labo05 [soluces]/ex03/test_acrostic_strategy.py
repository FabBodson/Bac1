import unittest
from io import StringIO

import ex03_steganography as steganography


class AcrosticStrategyTests(unittest.TestCase):
    def test_outputs_content_to_destination(self):
        decrypter = steganography.AcrosticStrategy()
        with open('acrostic_sample_1.txt') as source:
            with open('destination.txt', 'w') as destination:
                decrypter.decrypt(source, destination)

        with open('destination.txt') as output:
            self.assertEqual('cette nuit', output.read().strip())

    def test_takes_spaces_and_separators_into_account(self):
        decrypter = steganography.AcrosticStrategy()
        with open('acrostic_sample_2.txt') as source:
            with open('destination.txt', 'w') as destination:
                decrypter.decrypt(source, destination)

        with open('destination.txt') as output:
            self.assertEqual('quand voulez vous que je couche avec vous', output.read().strip())


class AcrosticStrategyStringIOTests(unittest.TestCase):
    def test_outputs_content_to_destination(self):
        decrypter = steganography.AcrosticStrategy()
        source_stream = StringIO("""
Cette insigne faveur que votre cour réclame"
Nuit à ma renommée et répugne mon âme.
""")
        destination_stream = StringIO()
        decrypter.decrypt(source_stream, destination_stream)
        destination_stream.seek(0)
        self.assertEqual('cette nuit', destination_stream.read().strip())

    def test_takes_spaces_and_separators_into_account(self):
        decrypter = steganography.AcrosticStrategy()
        source_stream = StringIO("""
Quand je mets à vos pieds un éternel hommage
Voulez-vous qu'un instant je change de visage?
Vous avez capturé les sentiments d'un cour
Que pour vous adorer forma le Créateur.
Je vous chéris, amour, et ma plume en délire
Couche sur le papier ce que je n'ose dire.
Avec soin, de mes vers lisez les premiers mots
Vous saurez quel remède apporter à mes maux
""")
        destination_stream = StringIO()
        decrypter.decrypt(source_stream, destination_stream)
        destination_stream.seek(0)
        self.assertEqual('quand voulez vous que je couche avec vous', destination_stream.read().strip())


if __name__ == '__main__':
    unittest.main()
