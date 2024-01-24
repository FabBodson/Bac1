

def binary_search(collection, search_criteria, key_function=None):
    """
    Recherche dichotomique de l'index d'un élément précis (search_criteria) dans une collection d'éléments (collection).
    Si les élements de la collection sont complexes (comme des objets), le paramètre key_function permet de définir une
    fonction récupérant l'attribut à comparer.

    Exemple:
        binary_search(collection=[1, 2, 3, 4, 5], search_criteria=3) > Retourne l'indice du nombre 3 dans la liste
        binary_search(
            collection=[component_a, component_b, component_c],
            search_criteria='chocolat',
            key_function=lambda component: component.name
        )

    :param collection: liste de plusieurs objets
    :param search_criteria: la valeur recherchée
    :param key_function: fonction qui retourne l'attribut de l'objet servant à la comparaison
    :return: l'index de l'objet correspondant à la valeur recherchée
    """
    lower, higher = 0, len(collection) - 1
    while lower <= higher:
        middle = (lower + higher) // 2
        middle_element = collection[middle]
        attribute = key_function(middle_element) if key_function else middle_element
        if search_criteria > attribute:
            lower = middle + 1
        elif search_criteria < attribute:
            higher = middle
        else:
            return middle
    return None




