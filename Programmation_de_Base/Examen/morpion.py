LONGUEUR_MATRICE_MAX = 3
PLATEAU_FULL = "Il n'y a plus de cases libres - Game Over"

def initialiser_plateau(nbre_lignes):
    """
    Crée une liste 2D carrée (nombre de lignes = nombre de colonnes).  Chaque élément de la liste contient le symbole '.'
    :param nbre_lignes: int, nombre de lignes
    :return: list, liste 2D dans laquelle chaque élément contient le symbole '.'
    """
    # Initialisation de la liste
    plateau = []
    for i in range(nbre_lignes):

        # Ajout d'une ligne
        plateau.append([])
        for j in range(nbre_lignes):

            # Placement du caractere '.' à chaque élément
            plateau[i].append(obtenir_symbole(0))

    return plateau


def afficher_message_bienvenue():
    """
    Affiche le message de bienvenue au lancement du jeu.
    :return: /
    """
    print('------------------------------')
    print('Bienvenue au jeu du morpion')
    print('------------------------------')
    print(f'Joueur 1 - Symbole {obtenir_symbole(1)} | Joueur 2 - Symbole {obtenir_symbole(2)}')
    print('Plateau initial : ')



def afficher_debut_partie():
    """
    Affiche le message de début de partie.
    :return: /
    """
    print("Début de la partie :")
    print("--------------------")


def convertir_en_texte(matrice):
    """
    Convertit une liste 2D en texte - chaque élément est entouré par le symbole | et les éléments sont affichés 3 par 3
    sur une ligne.
    :param: matrice: list, liste 2D
    :return: str, matrice convertie en texte
    """
    # Création de la chaine qui contiendra la matrice
    matrice_texte = ''

    for i in range(len(matrice)):

        for caractere in matrice[i]:

            # Conversion de l'élément en texte
            chaine_caractere = str(caractere)

            # Concaténation du texte dans ma chaine
            matrice_texte += chaine_caractere


    return matrice_texte




def afficher(matrice):
    """
    Affiche à l'écran une matrice convertie en texte
    :param matrice: list, liste 2D
    :return: /
    """
    for i in range(len(matrice)):

        for caractere in matrice[i]:

            chaine_caractere = str(caractere)
            print(f'| {chaine_caractere:>2}', end='  ')

        print('|')

    print('\n')


def obtenir_symbole(num_joueur):
    """
    Retourne le symbole correspondant au numéro de joueur "num_joueur" ou le symbole de la case vide.
    Le paramètre num_joueur peut être soit 0, soit 1, soit 2.
    :param num_joueur: int, numéro du joueur
    :return: string, symbole 'x' représentant le joueur 1 - symbole 'o' représentant le joueur 2, symbole '.' représentant une case vide. None, dans les cas contraires
    """
    if 0 > num_joueur > 2:
        return None

    elif num_joueur == 0:
        return '.'

    elif num_joueur == 1:
        return 'x'

    else:
        return 'o'


def saisir_axe(num_joueur, axe):
    """
    Demande au joueur "num_joueur" d'entrer une ligne ou colonne.
    :param num_joueur: int, numero du joueur
    :param axe: str, chaine correspondant au choix ligne ou colonne.
    :return: int, numéro de la ligne ou numéro de la colonne séléctionnée.
    """
    choix = int(input(f'Joueur {num_joueur}, quelle {axe} ? '))

    # Si le choix ne correspond pas à ce qui est demandé, il est redemandé jusqu'à ce que le choix soit valide
    if choix <= 0 or choix > 3:
        while choix <= 0 or choix > 3:
            choix = int(input(f'Veuillez entrer un nombre entre 1 et 3: '))

    return choix





def assigner_symbole_joueur(plateau, num_joueur):
    """
    Assigner le symbole de l'utilisateur à un élément de la liste 2D
    :param plateau: list, liste 2D représentant le plateau de jeu
    :param num_joueur: int, numéro du joueur actif
    :return: /
    """
    # Saisie de la ligne et de la colonne où l'utilisateur veut placer son symbole
    choix_ligne = saisir_axe(num_joueur, 'ligne')-1
    choix_colonne = saisir_axe(num_joueur, 'colonne')-1


    if plateau[choix_ligne][choix_colonne] == obtenir_symbole(0):

        for i in range(len(plateau)):

            if i == choix_ligne:
                for j in range(len(plateau[i])):

                    if j == choix_colonne:

                        # Placement du symbole
                        plateau[i][j] = obtenir_symbole(num_joueur)

                    else:
                        continue

            else:
                continue

    else:
        print('Cette case est déjà occupée, rejouez ')
        # Si la case est déjà occupée, la fonction est rappelée
        assigner_symbole_joueur(plateau, num_joueur)







def verifier_victoire(plateau):
    """
    Vérifie si une ligne horizontale est complète
    :param plateau: liste 2D
    :return: int, numéro de joueur ou 0 si pas de gagnant
    """
    for ligne in plateau:

        for element in ligne[0]:

            # vérifie si le nombre délément dans ma ligne vaut 3 et n'est pas un '.'
            if ligne.count(element) == 3 and element != '.':
                if element == 'x':
                    return 1
                else:
                    return 2

            else:
                continue

    # Si le plateau est parcouru sans trouver de 'x' ou de 'o', la fonction retourne 0
    return 0



def jouer_partie(plateau):
    """
    Cette fonction gère la boucle de jeu jusqu'à ce qu'un gagnant soit trouvé ou que la plateau est complet.
    :param plateau: list, liste 2D représentant le plateau de jeu
    :return: int, numéro du gagnant ou 0 pour le game over.
    """
    numero_tour = 1

    while verifier_victoire(plateau) == 0 or plateau.count(obtenir_symbole(0)) >= 1:

        # Si on est dans un tour pair, ce sera le joueur 2 qui jouera.
        if numero_tour % 2 == 0:
            assigner_symbole_joueur(plateau, 2)
            afficher(plateau)
            verifier_victoire(plateau)
            numero_tour += 1

        # Sinon ce sera le joueur 1 qui jouera.
        else:
            assigner_symbole_joueur(plateau, 1)
            afficher(plateau)
            verifier_victoire(plateau)
            numero_tour += 1



    if verifier_victoire(plateau) == 1:
        return 1

    elif verifier_victoire(plateau) == 2:
        return 2

    else:
        return 0








def _main():
    plateau = initialiser_plateau(LONGUEUR_MATRICE_MAX)
    afficher_message_bienvenue()
    afficher(plateau)
    afficher_debut_partie()
    gagnant = jouer_partie(plateau)
    if gagnant == 0:
        print(PLATEAU_FULL)
    else:
        print(f'Le gagnant est le joueur {gagnant} qui a joué avec le symbole {obtenir_symbole(gagnant)}')


if __name__ == '__main__':
    _main()
