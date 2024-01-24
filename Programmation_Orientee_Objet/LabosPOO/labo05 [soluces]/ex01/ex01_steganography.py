import re


class AcrosticStrategy:

    def decrypt(self, source, dest):
        decrypted_words = []
        for line in source:
            words = re.split('\\W+', line)
            decrypted_words.append(words[0].lower())
        dest.write(' '.join(decrypted_words))
