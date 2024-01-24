
def obtenir_score(nb_points):
    if nb_points == 1:
        nb_points = '15'

    elif nb_points == 2:
        nb_points = '30'

    elif nb_points == 3:
        nb_points = '40'

    elif nb_points == 4:
        nb_points = 'A'



    return nb_points





def _main():
    nb_set_j1 = 0
    nb_set_j2 = 0

    joueur1 = input('Joueur 1 ? ')
    joueur2 = input('Joueur 2 ? ')

    # Boucle qui détermine dans quel set on se trouve

    while (nb_set_j1 < 2) and (nb_set_j2 < 2):

        # Boucle qui détermine qui gagne le set ################################

        nb_jeux_j1 = 0
        nb_jeux_j2 = 0

        while (nb_jeux_j1 <= 6) and (nb_jeux_j2 <= 6):
            if nb_jeux_j1 == 6 and nb_jeux_j2 == 6:
                break
            else:

                # Boucle qui détermine qui gagne le jeu ############################

                nb_points_j1 = 0
                nb_points_j2 = 0

                while nb_points_j1 <= 3 and nb_points_j2 <= 3:
                    if nb_points_j1 == 3 and nb_points_j2 == 3:
                        break
                    else:

                        print(f'\n{joueur1:<10} {nb_set_j1} | {nb_jeux_j1} | {obtenir_score(nb_points_j1)}')
                        print(f'{joueur2:<10} {nb_set_j2} | {nb_jeux_j2} | {obtenir_score(nb_points_j2)}')

                        gagnant = int(input('Quel joueur gagne le point (1 ou 2) ? '))

                        if gagnant != 1 and gagnant != 2:
                            print('Fallait choisir 1 ou 2 …')
                            return False

                        else:

                            if gagnant == 1:
                                nb_points_j1 += 1

                            elif gagnant == 2:
                                nb_points_j2 += 1

                # Sortie de boucle #################################################

                if nb_points_j1 == nb_points_j2:

                    while ((nb_points_j1 - nb_points_j2) != 2) and ((nb_points_j2 - nb_points_j1) != 2):

                        if nb_points_j1 == 4 and nb_points_j2 == 4:
                            nb_points_j1 = 3
                            nb_points_j2 = 3

                        else:
                            print(f'\n{joueur1:<10} {nb_set_j1} | {nb_jeux_j1} | {obtenir_score(nb_points_j1)}')
                            print(f'{joueur2:<10} {nb_set_j2} | {nb_jeux_j2} | {obtenir_score(nb_points_j2)}')

                            gagnant = int(input('Quel joueur gagne le point (1 ou 2) ? '))

                            if gagnant == 1:
                                nb_points_j1 += 1

                            elif gagnant == 2:
                                nb_points_j2 += 1

                    if nb_points_j1 > nb_points_j2:
                        nb_jeux_j1 += 1

                    elif nb_points_j1 < nb_points_j2:
                        nb_jeux_j2 += 1

                else:

                    if nb_points_j1 > nb_points_j2:
                        nb_jeux_j1 += 1

                    elif nb_points_j1 < nb_points_j2:
                        nb_jeux_j2 += 1



        # Sortie de boucle #####################################################

        if (nb_jeux_j1 - nb_jeux_j2) >= 2:
            nb_set_j1 += 1

        elif (nb_jeux_j2 - nb_jeux_j1) >= 2:
            nb_set_j2 += 1

        else:

            # Boucle  ##########################################################
            while (nb_jeux_j1 != 7) and (nb_jeux_j2 != 7):

                while nb_points_j1 <= 3 and nb_points_j2 <= 3:
                    if nb_points_j1 == 3 and nb_points_j2 == 3:
                        break
                    else:

                        print(f'\n{joueur1:<10} {nb_set_j1} | {nb_jeux_j1} | {obtenir_score(nb_points_j1)}')
                        print(f'{joueur2:<10} {nb_set_j2} | {nb_jeux_j2} | {obtenir_score(nb_points_j2)}')

                        gagnant = int(input('Quel joueur gagne le point (1 ou 2) ? '))

                        if gagnant != 1 and gagnant != 2:
                            print('Fallait choisir 1 ou 2 …')
                            return False

                        else:

                            if gagnant == 1:
                                nb_points_j1 += 1

                            elif gagnant == 2:
                                nb_points_j2 += 1

                # Sortie de boucle #################################################

                if nb_points_j1 == nb_points_j2:

                    while ((nb_points_j1 - nb_points_j2) != 2) and ((nb_points_j2 - nb_points_j1) != 2):

                        if nb_points_j1 == 4 and nb_points_j2 == 4:
                            nb_points_j1 = 3
                            nb_points_j2 = 3

                        else:
                            print(f'\n{joueur1:<10} {nb_set_j1} | {nb_jeux_j1} | {obtenir_score(nb_points_j1)}')
                            print(f'{joueur2:<10} {nb_set_j2} | {nb_jeux_j2} | {obtenir_score(nb_points_j2)}')

                            gagnant = int(input('Quel joueur gagne le point (1 ou 2) ? '))

                            if gagnant == 1:
                                nb_points_j1 += 1

                            elif gagnant == 2:
                                nb_points_j2 += 1

                    if nb_points_j1 > nb_points_j2:
                        nb_jeux_j1 += 1

                    elif nb_points_j1 < nb_points_j2:
                        nb_jeux_j2 += 1

                else:

                    if nb_points_j1 > nb_points_j2:
                        nb_jeux_j1 += 1

                    elif nb_points_j1 < nb_points_j2:
                        nb_jeux_j2 += 1


            if nb_jeux_j1 == 7:
                nb_set_j1 += 1

            else:
                nb_set_j2 += 1


    if nb_set_j1 > nb_set_j2:
        nb_jeux_j1 = 0
        nb_points_j1 = 0
        print(f'{joueur1} gagne le match !')
    else:
        nb_jeux_j2 = 0
        nb_points_j2 = 0
        print(f'{joueur2} gagne le match !')


    print(f'\n{joueur1:<10} {nb_set_j1} | {nb_jeux_j1} | {obtenir_score(nb_points_j1)}')
    print(f'{joueur2:<10} {nb_set_j2} | {nb_jeux_j2} | {obtenir_score(nb_points_j2)}')




if __name__ == '__main__':
    _main()
