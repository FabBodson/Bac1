from algo_labo02.file import read_csv_file
from algo_labo02.model import Component, Essence


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
    if len(collection) == 0:
        return []
    else:
        if len(collection) == 1:
            return collection[0]
        else:
            middle = len(collection)//2
            middle_element = collection[middle]
            left_half = collection[:middle]
            right_half = collection[middle+1:]

            if search_criteria == middle_element:
                return middle
            else:
                if search_criteria < middle_element:
                    binary_search(left_half, search_criteria, key_function)
                else:
                    binary_search(right_half, search_criteria, key_function)


def ajouter_produits(liste_produits):
    liste_affichage = []
    for produit in liste_produits:
        produit['Nom'] = produit['Nom'].lower()
        if produit['Nom'] not in liste_affichage:
            liste_affichage.append(produit['Nom'])
    return liste_affichage


# Récupère la position xyz d'une essence
def get_position_xyz(file, id_essence):
    olfa_xyz = read_csv_file(file)
    for line in olfa_xyz:
        if line['Essence'] == id_essence:
            pos = (int(line['X']), int(line['Y']), int(line['Z']))
            return pos
    return ()


# Crée une liste des composants choisis || Gout contient deja odeur
def create_list_of_components(liste_posologie, gouts):
    components = []
    for element in liste_posologie:
        if element['Nom'] in gouts:
            components.append(Component(element['Nom'], element['Type'], element['Essence'], element['Gouttes'],
                                        get_position_xyz("olfaxyz.csv", element['Essence'])))
    return components


# Crée une liste des essences des composants choisis
def create_essences(liste_components):
    essences = []
    for component in liste_components:
        essences.append(Essence(component.position_xyz, component.nb_drops))
    return essences
