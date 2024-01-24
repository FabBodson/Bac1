nombre_lignes = int(input('Séléctionnez le nombre de lignes: '))

compteur = 0

for i in range(nombre_lignes):

    for j in range(i+1):
        compteur += 1
        print(compteur, end=" ")
    print()