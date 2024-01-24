class WordSource:
    def __init__(self, words):
        self.__words = words

    def __getitem__(self, item):
        if item <= len(self.words):
            return self.words[item]
        else:
            return None

    @property
    def words(self):
        return self.__words

    @property
    def count(self):
        return len(self.words)
