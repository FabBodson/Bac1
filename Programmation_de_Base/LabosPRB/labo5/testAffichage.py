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



joueur1 = 'Fabrice'
joueur2 = 'Camille'

nb_points_j1 = 0
nb_points_j2 = 0

print(f'\n{joueur1:<10} 1 | 6 | {obtenir_score(nb_points_j1)}')
print(f'{joueur2:<10} 0 | 2 | {obtenir_score(nb_points_j2)}')

gagnant = int(input('Quel joueur gagne le point (1 ou 2) ? '))
