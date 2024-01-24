import random




def _main():
    nombre_de_lance = int(input('Nombre de 1 à 6 ? '))

    essai = random.randint(1, 6)
    i = 1

    while essai != nombre_de_lance:

        print(f'Essai #{i}: {essai}')
        essai = random.randint(1, 6)
        i += 1
    print(f'Essai #{i}: {essai}')
    print(f'Nombre de lancés : {i}')






if __name__ == '__main__':
    _main()

