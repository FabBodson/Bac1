# 1. Renvoyer un valeur booléenne indiquant si une liste passée en paramètre contient un doublon.
#    Vrai si liste contient un doublon et faux dans le cas contraire
#    A. Ecrire le code en python.
#    B. Noter la complexité de votre algorithme O(n).
#    C. Voyez s'il est possible d'optimiser votre algorithme.


"""
LORQUET:
"""


def has_duplicates(collection):
    return len(set(collection)) != len(collection)


"""
CARBONARA:
O(n log n)

def has_duplicates(collection):
    sorted_collection = sorted(collection)
    for i in range(1, len(sorted_collection)):
        if sorted_collection[i] == sorted_collection[i-1]:
            return True
    return False

MOI:
def has_duplicates(collection: list) -> bool:

    for element in collection:
        if collection.count(element) >= 2:
            return True
    return False


EXECUTION :

    print("Recherche d'un doublon dans une liste.")
    collection = str.rstrip(input("Entrez une liste des valeurs séparées par un espace: "))

    collection = collection.split(" ")
    print(collection)

    if has_duplicates(collection):
        print("Doublons !")
    else:
        print("Pas de doublons !")
"""