import re

from chiffrement_de_cesar import chiffrer, REGEX


def attaque_force_brute(texte):
    """
    Cette fonction liste l'ensemble des déchiffrements possibles pour un texte chiffré au moyen de l'algorithme de César.
    Cette fonction se limite au déchiffrement des caractères: [A-Za-z]. Elle ne déchiffrera ni les chiffres, ni les espaces,
    ni la ponctuation, ni les caractères accentués.
    :param texte: str, texte chiffré.
    :return: list, liste de tous les déchiffrements possibles.
    """

    candidats = []

    for decalage in range(0, 26):
        texte_dechiffre = ''

        for caractere in texte:
            if not re.match(REGEX, caractere):
                texte_dechiffre += caractere
                continue

            caractere_entier = ord(caractere)

            if 65 <= caractere_entier <= 90:

                caractere_entier -= 65

                caractere_entier = (caractere_entier - decalage) % 26

                caractere_entier += 65

                texte_dechiffre += chr(caractere_entier)

            elif 97 <= caractere_entier <= 122:

                caractere_entier -= 97

                caractere_entier = (caractere_entier - decalage) % 26

                caractere_entier += 97

                texte_dechiffre += chr(caractere_entier)

        candidats.append(texte_dechiffre)

    return candidats




def _main():

    # Chiffrement :
    print('Chiffrement: ')


    votre = chiffrer('votre', 3)
    print(votre)


    premier = chiffrer('premier', -8)
    print(premier)


    algorithme = chiffrer('algorithme', -1)
    print(algorithme)


    de = chiffrer('de', 78)
    print(de)


    chiffrement = chiffrer('chiffrement:', 20)
    print(chiffrement)


    le = chiffrer('le', 3)
    print(le)


    celebre = chiffrer('célèbre', 2)
    print(celebre)


    chiffrement_2 = chiffrer('Chiffrement', 16)
    print(chiffrement_2)


    de_2 = chiffrer('de', -7)
    print(de_2)


    cesar = chiffrer('César !', 9)
    print(cesar)








    #  Par force brute :
    print('\nDéchiffrement: ')


    votre2 = attaque_force_brute(votre)
    print(votre2)


    premier2 = attaque_force_brute(premier)
    print(premier2)


    algorithme2 = attaque_force_brute(algorithme)
    print(algorithme2)


    de_3 = attaque_force_brute(de)
    print(de_3)


    chiffrement_3 = attaque_force_brute(chiffrement)
    print(chiffrement_3)


    le2 = attaque_force_brute(le)
    print(le2)


    celebre2 = attaque_force_brute(celebre)
    print(celebre2)


    chiffrement_4 = attaque_force_brute(chiffrement)
    print(chiffrement_4)


    de_4 = attaque_force_brute(de)
    print(de_4)


    cesar2 = attaque_force_brute(cesar)
    print(cesar2)






if __name__ == '__main__':
    _main()