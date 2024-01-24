from math import factorial

def is_strong(number):
    if number == 0:
        return 0

    somme = 0
    number = str(number)

    for chiffre in number:
        chiffre = int(chiffre)
        somme += factorial(chiffre)

    if somme == number:
        return True
