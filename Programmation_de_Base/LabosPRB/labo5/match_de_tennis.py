
def obtenir_score(nb_points):

    if nb_points == 0:
        nb_points = 'O'

    elif nb_points == 1:
        nb_points = '15'

    elif nb_points == 2:
        nb_points = '30'

    elif nb_points == 3:
        nb_points = '40'

    elif nb_points == 4:
        nb_points = 'A'

    else:
        return False



    return nb_points





def _main():
    joueur1 = input('Joueur 1 ? ')
    joueur2 = input('Joueur 2 ? ')

    nb_points_j1 = 0
    nb_points_j2 = 0

    while nb_points_j1 <= 3 and nb_points_j2 <= 3:
        if nb_points_j1 == 3 and nb_points_j2 == 3:
            break
        else:

            print(f'\n{joueur1:<10} {obtenir_score(nb_points_j1)}')
            print(f'{joueur2:<10} {obtenir_score(nb_points_j2)}')

            gagnant = int(input('Quel joueur gagne le point (1 ou 2) ? '))

            if gagnant != 1 and gagnant != 2:
                print('Fallait choisir 1 ou 2 …')
                return False

            else:

                if gagnant == 1:
                    nb_points_j1 += 1

                elif gagnant == 2:
                    nb_points_j2 += 1




    if nb_points_j1 == nb_points_j2:

        while ((nb_points_j1 - nb_points_j2) != 2) and ((nb_points_j2 - nb_points_j1) != 2):

            if nb_points_j1 == 4 and nb_points_j2 == 4:
                nb_points_j1 = 3
                nb_points_j2 = 3

            else:
                print(f'\n{joueur1:<10} {obtenir_score(nb_points_j1)}')
                print(f'{joueur2:<10} {obtenir_score(nb_points_j2)}')

                gagnant = int(input('Quel joueur gagne le point (1 ou 2) ? '))

                if gagnant == 1:
                    nb_points_j1 += 1

                elif gagnant == 2:
                    nb_points_j2 += 1


        if nb_points_j1 > nb_points_j2:
            print(f'\n{joueur1} remporte la partie !')

        elif nb_points_j1 < nb_points_j2:
            print(f'{joueur2} remporte la partie !')




    else:

        if nb_points_j1 > nb_points_j2:
            print(f'\n{joueur1} remporte la partie !')

        elif nb_points_j1 < nb_points_j2:
            print(f'{joueur2} remporte la partie !')







if _main() == '__main__':
    _main()