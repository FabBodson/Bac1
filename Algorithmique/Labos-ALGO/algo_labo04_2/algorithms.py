
def has_duplicates(collection):
    """
    Cherche s'il y a un doublon dans la collection.
    CTT: O(n)
    :param collection: list, liste d'éléments
    :return: True si contient un doublon, False sinon
    """
    for element in collection:
        if collection.count(element) >= 2:
            return True
    return False

