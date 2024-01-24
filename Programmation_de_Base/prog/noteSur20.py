
note = int(input('Donnez une note entre 0 et 20: '))

if note < 0 or note > 20:

    while note < 0 or note > 20:
        note = int(input('Donnez une note entre 0 et 20: '))
    print('Enfin!')

else:
    print('Bien')