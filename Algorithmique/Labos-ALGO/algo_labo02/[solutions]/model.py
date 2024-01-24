

class Essence:

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f'Essence(name={self.name}, location={self.location})'


class Component:

    def __init__(self, name):
        self.name = name
        self.essences = {}

    def __str__(self):
        return f'Component(name={self.name}, essences={", ".join([essence.name for essence in self.essences])})'

    def add_essence(self, essence, quantity):
        self.essences[essence] = quantity


class User:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.bottles = []

    def __str__(self):
        return f'{self.first_name} {self.last_name.upper()}'

    def add_bottle(self, bottle):
        self.bottles.append(bottle)


class Bottle:

    def __init__(self, components):
        self.components = components
        self.essences = {}
        for component in components:
            for essence, quantity in component.essences.items():
                if essence in self.essences:
                    old_quantity = self.essences[essence]
                    self.essences[essence] = old_quantity + quantity
                else:
                    self.essences[essence] = quantity

    @property
    def name(self):
        return "-".join([component.name[:3] for component in self.components])

    def __str__(self):
        essences = "\n\t".join([f'{name} * {quantity}' for name, quantity in self.essences.items()])
        return f'Bottle(\n' \
               f'\tname={self.name},\n' \
               f'{essences}' \
               f')'
