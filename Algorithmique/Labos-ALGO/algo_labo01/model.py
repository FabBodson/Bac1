
class Family:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f'{self.name}'


class Bus:
    def __init__(self, families, capacity):
        self.families = families
        self.capacity = capacity

    def update_capacity(self, family):
        self.capacity -= family.number
        return self.capacity
