class Mass:

    PRECISION = 0.001

    def __init__(self, value_in_kg):
        self.value = value_in_kg

    def __eq__(self, other):
        return isinstance(other, self.__class__) and abs(other.value - self.value) <= self.PRECISION

