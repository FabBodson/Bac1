

class Family:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f'{self.name}'


class Bus:

    def __init__(self, capacity):
        self.capacity = capacity
        self.families = []
        self.__count = 0

    def __str__(self):
        return f'{", ".join([str(family) for family in self.families])} - emplacements vides = {self.empty_seats}'

    @property
    def count(self):
        return self.__count

    @property
    def empty_seats(self):
        return self.capacity - self.__count

    def can_add(self, family):
        return (self.__count + family.size) <= self.capacity

    def add(self, family):
        if not self.can_add(family):
            raise ValueError(f'Not enough places for the family {family}!')
        self.families.append(family)
        self.__count += family.size
