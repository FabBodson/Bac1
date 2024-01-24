class WordSource:
    def __init__(self):
        self.__words = []

    def __getitem__(self, pos):
        try:
            return self.__words[pos]

        except IndexError:
            return None

    @property
    def count(self):
        return len(self.__words)
