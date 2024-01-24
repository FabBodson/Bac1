def convertir_en_texte(matrice):
    """
    Cette fonction transforme une matrice en un texte.

    Pour la matrice:
    [
        [-10, -20, -30],
        [4, 5, 6],
        [-30, 1, 9]
    ]

    cette fonction produira le texte:

    |   -10   -20   -30 |
    |     4     5     6 |
    |   -30     1     9 |

    :param matrice: list, liste 2D de nombres entiers
    :return: str, représentation textuelle de la matrice
    """
    matrice_txt = ''

    if len(matrice) == 0:
        matrice_txt = f'{"|"}'
        matrice_txt += f'{"|":>5}\n'

    else:
        for element in matrice:
            matrice_txt += f'{"|"}'

            for element in matrice[matrice.index(element)]:
                matrice_txt += f'{str(element):>6}'

            matrice_txt += f'{"|":>2}\n'

    return matrice_txt






def afficher(matrice):
    """
    Cette fonction permet d'afficher une matrice 2D à l'écran.
    :param matrice: list, liste 2D de nombres entiers
    """

    print(convertir_en_texte(matrice))



def minimum(matrice):
    """
    Cette fonction retourne la plus petite valeur contenue dans la matrice. Si la matrice ne contient aucune valeur,
    la fonction retourne None.
    :param matrice: list, liste 2D de nombres entiers
    :return: int: la plus petite valeur contenue dans la matrice. Si la matrice ne contient aucune valeur, None
    """
    if len(matrice) == 0:
        return None
    else:
        element_minimum = 0
        for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                element_minimum = min(element_minimum, matrice[i][j])
        return element_minimum



def maximum(matrice):
    """
    Cette fonction retourne la plus grande valeur contenue dans la matrice. Si la matrice ne contient aucune valeur,
    la fonction retourne None.
    :param matrice: list, liste 2D de nombres entiers
    :return: int: la plus grande valeur contenue dans la matrice. Si la matrice ne contient aucune valeur, None
    """
    if len(matrice) == 0:
        return None
    else:
        element_maximum = 0
        for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                element_maximum = max(element_maximum, matrice[i][j])
        return element_maximum



def minimum_par_ligne(matrice):
    """
    Cette fonction retourne une liste contenant la plus petite valeur contenue dans chaque ligne.
    Exemple:

    | 7, 3, 8 |
    | 6, 4, 1 | --> [ 3, 1, 2 ]
    | 5, 2, 7 |

    :param matrice: list, liste 2D de nombres entiers
    :return: list, contenant la valeur minimum de chaque ligne.
    """

    liste_min = []

    for i in range(len(matrice)):
        premier_element_colonne = matrice[i][0]
        element_minimum = premier_element_colonne

        for j in range(len(matrice[i])):
            element_minimum = min(element_minimum, matrice[i][j])

        liste_min.append(element_minimum)

    return liste_min




def maximum_par_ligne(matrice):
    """
    Cette fonction retourne une liste contenant la plus grande valeur contenue dans chaque ligne.
    Exemple:

    | 7, 3, 8 |
    | 6, 4, 1 | --> [ 8, 6, 7 ]
    | 5, 2, 7 |

    :param matrice: list, liste 2D de nombres entiers
    :return: list, contenant la valeur maximum de chaque ligne.
    """
    liste_max = []

    for i in range(len(matrice)):
        premier_element_colonne = matrice[i][0]
        element_maximum = premier_element_colonne

        for j in range(len(matrice[i])):
            element_maximum = max(element_maximum, matrice[i][j])

        liste_max.append(element_maximum)

    return liste_max



def minimum_par_colonne(matrice):
    """
    Cette fonction retourne une liste contenant la plus petite valeur contenue dans chaque colonne.
    Exemple:

    | 7, 3, 8 |
    | 6, 4, 1 | --> [ 5, 2, 1 ]
    | 5, 2, 7 |

    :param matrice: list, liste 2D de nombres entiers
    :return: list, contenant la valeur minimum de chaque colonne.
    """
    min_colonne, min_temporaire = [], []
    i, j = 0, 0
    for element in matrice:
        for i in range(len(matrice)):
            min_temporaire.append(matrice[i][j])


        min_colonne.append(min(min_temporaire))
        min_temporaire = []
        j += 1

    return min_colonne



def maximum_par_colonne(matrice):
    """
    Cette fonction retourne une liste contenant la plus grande valeur contenue dans chaque colonne.
    Exemple:

    | 7, 3, 8 |
    | 6, 4, 1 | --> [ 7, 4, 8 ]
    | 5, 2, 7 |

    :param matrice: list, liste 2D de nombres entiers
    :return: list, contenant la valeur maximum de chaque colonne.
    """

    max_colonne, max_temporaire = [], []
    i, j = 0, 0
    for element in matrice:
        for i in range(len(matrice)):
            max_temporaire.append(matrice[i][j])

        max_colonne.append(max(max_temporaire))
        max_temporaire = []
        j += 1

    return max_colonne



def additionner(a, b):
    """
    Cette fonction retourne le résultat de l'opération d'addition entre les deux matrices a et b.
    :param a: list, liste 2D de nombres entiers (matrice)
    :param b: list, liste 2D de nombres entiers (matrice)
    :return: list, une nouvelle liste 2D de nombres entiers (matrice)
    """
    l1, c1 = len(a), len(a[0])
    l2, c2 = len(b), len(b[0])

    lmax, cmax = max(len(a), len(b)), max(len(a[0]), len(b[0]))

    somme = []

    for i in range(0, l1):
        somme.append([])
        for j in range(0, c2):
            somme[i].append(0)

    for i in range(lmax):
        for j in range(cmax):
            if i < l1 and j < c1:
                somme[i][j] += a[i][j]
            if i < l2 and j < c2:
                somme[i][j] += b[i][j]

    return somme


def _main():
    matrice1 = [
        [3, 3, 3],
        [1, 1, 1],
        [2, 2, 2]
    ]

    matrice2 = [
        [7, 3, 8],
        [6, 4, 1],
        [5, 2, 7]
    ]

    print(additionner(matrice1, matrice2))



if __name__ == '__main__':
    _main()





def echanger_lignes(matrice, index_ligne_1, index_ligne_2):
    """
    Cette fonction échange, dans la matrice elle-même, les lignes aux indices index_ligne_1 et index_ligne_2
    Si un des indices n'existent pas, la matrice restera inchangée.
    :param matrice: list, liste 2D de nombres entiers (matrice)
    """
    ligne1 = []
    ligne2 = []

    for i in range(len(matrice)):

        if i == index_ligne_1:
            ligne1.append(matrice[i])

        if i == index_ligne_2:
            ligne2.append(matrice[i])

        else:
            continue

    matrice[index_ligne_1] = ligne2
    matrice[index_ligne_2] = ligne1

    return matrice




def echanger_colonnes(matrice, index_colonne_1, index_colonne_2):
    """
    Cette fonction échange, dans la matrice elle-même, les colonnes aux indices index_colonne_1 et index_colonne_2.
    Si un des indices n'existent pas, la matrice restera inchangée.
    :param matrice: list, liste 2D de nombres entiers (matrice)
    :param index_colonne_1: int, représentant l'index de la première colonne à échanger
    :param index_colonne_2: int, représentant l'index de la seconde colonne à échanger
    """


    for i in range(len(matrice)):
        colonne1 = None
        colonne2 = None

        for j in range(len(matrice[i])):

            if j == index_colonne_1:
                colonne1 = matrice[i][j]

            if j == index_colonne_2:
                colonne2 = matrice[i][j]

            else:
                continue

        matrice[i][index_colonne_1] = colonne2
        matrice[i][index_colonne_2] = colonne1

    return matrice









def extraire_ligne(matrice, index):
    """
    Cette fonction retourne la ligne à l'index "index". Si la matrice ne contient pas la ligne spécifiée, la
    liste retournée sera vide.
    :param matrice: list, liste 2D de nombres entiers (matrice)
    :param index: int, indice de la ligne à extraire
    :return: list, liste des nombres contenus dans la ligne "index", ou une liste vide si la matrice ne
    contient pas la ligne spécifiée
    """

    ligne_extraction = []

    for i in range(len(matrice)):

        if i == index:
            ligne_extraction.append(matrice[i])

        else:
            continue


    return ligne_extraction





def extraire_colonne(matrice, index):
    """
    Cette fonction retourne la colonne à l'index "index". Si la matrice ne contient pas la colonne spécifiée, la
    liste retournée sera vide.
    :param matrice: list, liste 2D de nombres entiers (matrice)
    :param index: int, indice de la colonne à extraire
    :return: list, liste des nombres contenus dans la colonne "index", ou une liste vide si la matrice ne
    contient pas la colonne spécifiée
    """
    colonne = []
    for i in range(len(matrice)):


        for j in range(len(matrice[i])):

            if j == index:
                colonne.append(matrice[i][j])

            else:
                continue


    return colonne







def inserer_ligne(matrice, ligne, index):
    """
    Cette fonction permet d'insérer une nouvelle ligne dans la matrice "matrice" à l'index "index".
    Pour être ajoutée, la nouvelle ligne doit contenir le même nombre d'éléments que les autres lignes de la matrice !
    Si la matrice est vide, la nouvelle ligne peut être ajoutée, peu importe sa taille.
    :param matrice: list, liste 2D de nombres entiers (matrice)
    :param ligne: list, liste de nombres entiers
    :param index: int, emplacement d'insertion de la nouvelle ligne
    """
    
    if len(matrice) == 0:
        matrice.append(ligne)

    else:

        for i in range(len(matrice)):
            if len(matrice[i]) == len(ligne):
                continue
            else:
                return False

        matrice.insert(index, ligne)

    return matrice






def inserer_colonne(matrice, colonne, index):
    """
    Cette fonction permet d'insérer une nouvelle colonne dans la matrice "matrice" à l'index "index".
    Pour être ajoutée, la nouvelle colonne doit contenir le même nombre d'éléments que les autres colonnes de la matrice !
    Si la matrice est vide, la nouvelle colonne peut être ajoutée, peu importe sa taille.
    :param matrice: list, liste 2D de nombres entiers (matrice)
    :param colonne: list, liste de nombres entiers
    :param index: int, emplacement d'insertion de la nouvelle colonne
    """

    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if j == index:
                matrice[i].insert(index, colonne[i])
            else:
                continue



    return matrice





