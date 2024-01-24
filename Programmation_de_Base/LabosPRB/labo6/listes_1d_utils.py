def est_vide(liste):
    """
    Cette fonction vérifie que la liste passée en paramètre ne comporte aucun élément.
    :param liste: list. Ce paramètre doit toujours être défini et ne peut être "None".
    :return: bool, True si la liste est vide, False si ce n'est pas le cas.
    """
    if len(liste) == 0:
        return True
    else:
        return False


def convertir_en_texte(liste):
    """
    Cette fonction permet de transformer une liste en texte de forme "[element_1, element_2, ..., element_N]". Ainsi,
    la liste [1, 2, 3] produira le texte [1, 2, 3]. La liste vide [] produira le texte [], et la liste [1] produira le
    texte [1].
    :param liste: list. Ce paramètre doit toujours être défini et ne peut être "None".
    :return: str, représentation textuelle de la liste
    """
    string = str(liste)
    return string


def generer(debut, fin, pas):
    """
    Cette fonction permet de générer une liste de nombres entiers compris entre les bornes "debut" et "fin". Le
    La borne supérieure, "fin", est exclusive. L'espacement entre chaque nombre est spécifié par le paramètre "pas".
    Exemples:
    - generer(0, 5, 1): [0, 1, 2, 3, 4]
    - generer(2, 11, 2): [2, 4, 6, 8, 10]
    :param debut: int, représente la borne inférieure (incluse).
    :param fin: int, représente la borne supérieure (exclue).
    :param pas: int, représente l'intervalle entre chaque nombre. Il doit être supérieur à 0.
    :return: list ou None. La fonction retourne une nouvelle liste contenant les nombres générés, ou None si le pas spécifié est invalide.
    """
    if pas < 1:
        return None
    else:
        liste = []
        for i in range(debut, fin, pas):
            liste.append(i)
        return liste


def cloner(liste):
    """
    Cette fonction crée une nouvelle liste contenant les mêmes éléments que la liste passée en paramètre. Il s'agit d'un
    clonage simple - seule la liste est clonée, et non ses éléments.
    :param liste: list. Ce paramètre doit toujours être défini et ne peut être "None".
    :return: list, une nouvelle liste contenant les mêmes éléments que la liste originale.
    """

    return liste.copy()


def dupliquer_sans_doublons(liste):
    """
    Cette fonction crée une nouvelle liste contenant seulement les éléments uniques de la liste originale.
    Exemples:
    - [1, 2, 3, 2, 5] -> [1, 2, 3, 5]
    - [1, 1, 3, 3, 5] -> [1, 3, 5]
    :param liste: list. Ce paramètre doit toujours être défini et ne peut être "None".
    :return: list, nouvelle liste contenant seulement les éléments uniques de la liste originale.
    """
    if len(liste) < 0:
        return False

    else:
        liste_2 = []
        for element in liste:
            if element in liste_2:
                pass
            else:
                liste_2.append(element)


    return liste_2



def compter_pairs_et_impairs(liste):
    """
    Cette fonction compte les nombres pairs et impairs contenus dans une liste d'entiers.
    :param liste: list. Il s'agit d'une liste de nombres entiers. Ce paramètre doit toujours être défini et ne peut être "None".
    :return: tuple(int, int): le nombre de nombres pairs, le nombre de nombres impairs
    """
    if len(liste) < 0:
        return False

    else:
        compte_pair = 0
        compte_impair = 0
        for element in liste:
            if element % 2 == 0:
                compte_pair += 1

            else:
                compte_impair += 1

        mon_tuple = (compte_pair, compte_impair)
        return mon_tuple


def extraire_pairs_et_impairs(liste):
    """
    Cette fonction permet d'extraire les nombres pairs et impairs contenus dans une liste d'entiers en deux listes distinctes.
    :param liste: list. Il s'agit d'une liste de nombres entiers. Ce paramètre doit toujours être défini et ne peut être "None".
    :return: tuple(list, list): une liste contenant les nombres pairs, une liste contenant les nombres impairs.
    """
    if len(liste) < 0:
        return False

    else:
        compte_pair = []
        compte_impair = []
        for element in liste:

            if element % 2 == 0:
                compte_pair.append(element)

            else:
                compte_impair.append(element)

        mon_tuple = (compte_pair, compte_impair)
        return mon_tuple


def concatener_en_entier(liste):
    """
    Cette fonction transforme une liste de nombre entiers en un seul nombre entier, en concaténant tous les chiffres les
    un aux autres. Cette fonction considère les nombres comme non-signés.
    Exemples:
    - [1, 2, 3] -> 123
    - [1, 2, -4] -> 124
    :param liste: list. Il s'agit d'une liste de nombres entiers. Ce paramètre doit toujours être défini et ne peut être "None".
    :return: int, nombre entier représentant la concaténation de tous les chiffres de la liste originale.
    """
    if len(liste) < 1:
        return False

    else:
        nbr = ''
        for element in liste:
            if element < 0:
                element = abs(element)
                nbr += str(element)
            else:
                nbr += str(element)

        nbr = int(nbr)

        return nbr


def contient_sous_liste(a, b):
    """
    Cette fonction détermine si la liste b est contenue dans la liste a. Deux listes identiques sont considérées comme
    mutuellement inclusives. Une liste vide sera considérée comme sous-ensemble de n'importe quelle liste.
    :param a: list. Ce paramètre doit toujours être défini et ne peut être "None".
    :param b: list. Ce paramètre doit toujours être défini et ne peut être "None".
    :return: bool, True si la liste b est contenue dans la liste a, False sinon.
    """


    if est_vide(a) and est_vide(b):
        return True
    elif est_vide(b):
        return True

    elif a == b:
        return True

    elif len(a) < len(b):
        return False

    else:
        position_dans_b = 0

        for i in range(len(a)):

            if a[i] == b[position_dans_b]:
                position_dans_b += 1

                if len(b) > 1:
                    if position_dans_b == len(b) - 1:
                        return True
                else:
                    if position_dans_b == len(b):
                        return True


            else:
                position_dans_b = 0

        return False








def separer_en_deux(liste, index=-1):
    """
    Cette fonction permet de couper une liste en deux sous-listes, sur base d'un indice.
    :param liste: list. Ce paramètre doit toujours être défini et ne peut être "None".
    :param index: int, paramètre optionnel. Lorsqu'il prend la valeur -1, la liste sera coupée en deux en son centre. Sinon, la liste sera coupée à l'emplacement spécifié par l'index.
    :return: tuple(list, list): sous-liste pre-séparateur, sous-liste post-séparateur.
    """
    if len(liste) < 0:
        return False
    else:
        pre_liste = []
        post_liste = []
        if index == -1:
            for i in range(len(liste)//2):
                pre_liste.append(liste[i])

            for i in range(len(liste)//2, len(liste)):
                post_liste.append(liste[i])

        else:

            for element in liste[0:index]:
                pre_liste.append(element)

            for element in liste[index:]:
                post_liste.append(element)

        mon_tuple = (pre_liste, post_liste)

        return mon_tuple
