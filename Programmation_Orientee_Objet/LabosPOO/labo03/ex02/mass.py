class Mass:

    PRECISION = 0.001

    def __init__(self, value_in_kg):
        self.__value = value_in_kg

    def __eq__(self, other):
        return isinstance(other, self.__class__) and abs(other.__value - self.__value) <= self.PRECISION

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Mass(self.__value)  # Retourne une nouvelle masse avec la meme valeur que la masse originale

        else:
            return Mass(self.__value + other.value)

    def __str__(self):
        print(f'{self.in_kilos():.2f} kg')

    def __repr__(self):
        """ {self.__class__.__name__:.2f} recherche le nom de la classe actuelle """

        print(f'{self.__class__.__name__} of {self:.2f} kg')

    def in_kilos(self):
        return self.__value

    @property
    def value(self):
        pass
