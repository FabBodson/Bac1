class Length:

    PRECISION = 0.001

    def __init__(self, distance_in_m):
        self.__distance = distance_in_m

    def __eq__(self, other):
        return isinstance(other, self.__class__) and abs(other.__distance - self.__distance) <= self.PRECISION

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Length(self.__distance)

        else:
            return Length(self.__distance + other.value)

    def __str__(self):
        print(f'{self.in_meters():.2f} m')

    def __repr__(self):
        """ {self.__class__.__name__:.2f} recherche le nom de la classe actuelle """

        print(f'{self.__class__.__name__} of {self:.2f} m')

    def in_meters(self):
        return self.__distance

    def squared(self):
        return Length(self.__distance ** 2)
