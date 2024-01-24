

def sum_of_terms(pos):
    """
    Fonction qui retourne la somme des entiers de la ligne de position pos où pos commence à 0.
            Si pos est une valeur négative, la fonction retourne 0.
    :param: pos: int, position de la ligne dont on veut la somme des entiers contenus dedans.
    :return: 0 si valeur négative, la somme autrement.
    """

    if pos < 0:
        return 0

    elif pos > 0:
        colonne = 1
        somme = (pos + 1) * pos + 1
        somme_2 = somme

        while colonne <= pos:
            somme_2 = somme_2 + 2
            somme = somme + somme_2
            colonne += 1

    else:
        somme = 2 * pos + 1

    return somme

"""    if pos < 0:
        return 0

    return (pos + 1) ** 3
"""
