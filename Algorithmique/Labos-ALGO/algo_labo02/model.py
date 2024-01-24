from datetime import datetime


class User:
    def __init__(self, lastname, firstname, phone, email):
        self.lastname = lastname
        self.firstname = firstname
        self.phone = phone
        self.email = email


class Essence:
    def __init__(self, position_xyz, nb_drops):
        self.position = position_xyz
        self.nb_drops = nb_drops


class Component:
    def __init__(self, essence_name, smell_taste, id_essence, nb_drops, position_xyz):
        self.essence_name = essence_name
        self.smell_taste = smell_taste
        self.id_essence = id_essence
        self.nb_drops = nb_drops
        self.position_xyz = position_xyz


class Choice:
    def __init__(self, taste, smell):
        self.taste = taste
        self.smell = smell

    def print_choice(self):
        self.taste.append(self.smell)
        print("\nVos choix:")
        for produit in self.taste:
            print(produit)

    def print_essence_choisies(self, liste_posologie, gouts):
        print("\nLes essences associées à vos choix:")
        for essence in liste_posologie:
            if essence['Nom'] in gouts:
                print(essence['Essence'])


class Flask:
    def __init__(self, liste_essences):
        self.liste_essences = liste_essences
        self.reference = ""

    # Gout contient deja odeur
    def create_reference(self, gouts):
        for taste in gouts:
            self.reference += "-" + taste[:3]
            self.reference = str.lstrip(self.reference, "-")
        return self.reference


class Result(User):
    def __init__(self, lastname, firstname, phone, email):
        super().__init__(lastname, firstname, phone, email)
        self.lot_date = ""

    def create_lot_date(self, seq):
        date = datetime.now()
        self.lot_date += str(date.year) + str(date.month) + str(date.day) + "-" + str(seq).zfill(5)

        return self.lot_date
