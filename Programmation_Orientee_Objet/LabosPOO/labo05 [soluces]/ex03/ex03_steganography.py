import re


class SteganographicDecryptionStrategy:

    def decrypt(self, source, destination):
        self.start(destination)
        for line in source:
            words = re.split('\\W+', line)
            self.new_words(destination, words)
        self.end(destination)

    def start(self, destination): pass
    def end(self, destination): pass
    def new_words(self, destination, words): pass


class AcrosticStrategy(SteganographicDecryptionStrategy):

    def __init__(self):
        self.__decrypted_words = []

    def end(self, destination):
        destination.write(' '.join(self.__decrypted_words))

    def new_words(self, destination, words):
        self.__decrypted_words.append(words[0].lower())


class LetterStrategy(SteganographicDecryptionStrategy):

    def __init__(self):
        self.__decrypted_letters = []

    def start(self, destination):
        self.__decrypted_letters.clear()

    def end(self, destination):
        destination.write(''.join(self.__decrypted_letters))

    def new_words(self, destination, words):
        for word in words:
            if len(word) > 1:
                self.__decrypted_letters.append(word[1])
