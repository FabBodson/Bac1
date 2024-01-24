user_prop = int(input('Trouvez le nombre secret entre 1 et 10: '))
nombre_secret = 4


if user_prop < 1 or user_prop > 10:

    user_prop = int(input('Trouvez le nombre secret entre 1 et 10: '))

elif user_prop != nombre_secret:
    indice = 1

    while user_prop != nombre_secret:
        if indice <= 4:

            if user_prop > nombre_secret:
                print('Nombre secret est plus petit ;-)')

            if user_prop < nombre_secret:
                print('Nombre secret est plus grand ;-)')

            indice += 1

        user_prop = int(input('Trouvez le nombre secret entre 1 et 10: '))


else:
    print('Bien')