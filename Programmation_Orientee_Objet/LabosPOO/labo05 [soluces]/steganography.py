import re


class SteganographicDecryptionStrategy:
    def decrypt(self, source, destination):
        self.start(destination)
        for line in source:
            self.new_words(re.split('\\W+', line.lower()), destination)

    def start(self, destination):
        pass

    def new_words(self, words, destination):
        pass

    def end(self, destination):
        pass


class AcrosticStrategy(SteganographicDecryptionStrategy):
    def __init__(self):
        self.first_word_out = False

    def start(self, destination):
        self.first_word_out = False

    def new_words(self, words, destination):
        if len(words) > 0:
            destination.write(' '+words[0] if self.first_word_out else words[0])
            self.first_word_out = True


class LetterStrategy(SteganographicDecryptionStrategy):
    def new_words(self, words, destination):
        for word in words:
            if len(word) >= 2:
                destination.write(word.lower()[1])