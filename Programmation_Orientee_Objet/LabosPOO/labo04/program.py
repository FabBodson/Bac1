from random import sample #choice
from starwars.force_users import ForceUser, Jedi, Sith


def creer_liste_combattants(nb_combattants):
    melee = []

    for i in range(0, nb_combattants):
        print(f'Combattant #{i+1}')
        combattant = {"Ordre": str.lower(input("Quel ordre ? (Jedi - Sith - Force User) ")),
                      "Nom": str.lower(input(("Quel nom ? "))),
                      "Points de vie": int(input("Points de vie ? (min: 1) ")),
                      "Points d'attaque": int(input("Points d'attaque ? (min: 1) "))
                      }

        if combattant["Ordre"] != 'jedi' and combattant["Ordre"] != 'sith':
            combattant["Ordre"] = "User"

        if combattant["Nom"] == '':
            combattant["Nom"] = "Obi Wan Kenobi"

        if combattant["Points de vie"] < 1 or combattant["Points d'attaque"] < 1:
            combattant["Points de vie"] = 1
            combattant["Points d'attaque"] = 1

        if combattant["Ordre"] == 'jedi':
            combattant = Jedi(combattant["Nom"], combattant["Points de vie"], combattant["Points d'attaque"])

        elif combattant["Ordre"] == "sith":
            combattant = Sith(combattant["Nom"], combattant["Points de vie"], combattant["Points d'attaque"])

        else:
            combattant = ForceUser(combattant["Nom"], combattant["Points de vie"], combattant["Points d'attaque"])

        melee.append(combattant)

    return melee


def bataille(melee):

    while len(melee) > 1:

        j1, j2 = sample(melee, k=2)

        # j1 = choice(melee)
        # j2 = choice(melee)

        #while j2 == j1:
         #   j2 = choice(melee)

        #if type(j1) != type(j2):
        j1.use_force_on(j2)
        print(f"{j1.name} attaque {j2.name} ! Dégats causés: {j1.damage_points}")

        if j2.is_alive() is not True:
            melee.remove(j2)

    print(f'\n{melee[0].name} est le/la gagnant(e) !')


def _main():
    # nb_combattants = int(input('Combien de combattants (min: 2) ? '))
    nb_combattants = 2

    melee = creer_liste_combattants(nb_combattants)

    """melee = [Jedi("Fabrice", 100, 25),
             Jedi("Camille", 100, 25),
             Sith("Lucas", 100, 25),
             ForceUser("Dorian", 100, 25)]
"""
    bataille(melee)


if __name__ == '__main__':
    _main()
