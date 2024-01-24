from algorithm import binary_search
from model import Bottle, Component, Essence, User
from readers import CSVReader


def read_essences():
    reader = CSVReader('essences.csv')
    return [
        Essence(d['reference'], (int(d['x']), int(d['y']), int(d['z'])))
        for d in reader.read()
    ]


def get_key_callback(essence):
    return essence.name


def read_components(essences):
    reader = CSVReader('components.csv')
    tastes, scents = [], []

    components = {}
    for d in reader.read():
        name, quantity = d['name'], int(d['quantity'])
        essence_index = binary_search(essences, d['reference'], key_function=get_key_callback)
        essence = essences[essence_index]
        try:
            component = components[name]
        except KeyError:
            component = Component(d['name'])
            components[name] = component
            upper = d['category'].upper()
            if upper == 'G':
                tastes.append(component)
            elif upper == 'O':
                scents.append(component)
            else:
                assert False
        component.add_essence(essence, quantity)

    return tastes, scents


def encode_user():
    first_name = input('Quel est votre prénom ? ')
    last_name = input('Quel est votre nom de famille ? ')
    email = input('Quel est votre adresse email ? ')
    return User(first_name, last_name, email)


def encode_selection(tastes, scents):
    print('Selection des goûts:')
    for index, taste in enumerate(tastes):
        print(f'  [{index}]: {taste.name}')
    taste_1 = tastes[int(input('> Goût 1: '))]
    taste_2 = tastes[int(input('> Goût 2: '))]

    print('Selection des odeurs:')
    for index, scent in enumerate(scents):
        print(f'  [{index}]: {scent.name}')
    scent = scents[int(input('> Odeur 1: '))]
    return taste_1, taste_2, scent


def main():
    essences = sorted(read_essences(), key=lambda essence: essence.name)
    tastes, scents = read_components(essences)

    tastes = sorted(tastes, key=lambda component: component.name)
    scents = sorted(scents, key=lambda component: component.name)

    user = encode_user()
    taste_1, taste_2, scent = encode_selection(tastes, scents)
    user.add_bottle(Bottle([taste_1, taste_2, scent]))

    print(user)
    for bottle in user.bottles:
        print(bottle)


if __name__ == '__main__':
    main()

