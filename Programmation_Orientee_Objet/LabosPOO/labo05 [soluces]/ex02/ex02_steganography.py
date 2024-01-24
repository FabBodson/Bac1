import re


class AcrosticStrategy:
    def decrypt(self, source, dest):
        decrypted_words = []
        for line in source:
            words = re.split('\\W+', line)
            decrypted_words.append(words[0].lower())
        dest.write(' '.join(decrypted_words))


class LetterStrategy:
    def decrypt(self, source, dest):
        decrypted_letters = []
        for line in source:
            words = re.split('\\W+', line)
            for word in words:
                if len(word) > 1:
                    decrypted_letters.append(word[1])
        dest.write(''.join(decrypted_letters))
