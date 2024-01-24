import re


REGEX = '[A-Za-z]'




def chiffrer(texte, decalage):
    """
    Cette fonction chiffre le texte "texte" en utilisant l'algorithme de chiffrement par décalage nommé chiffrement de César.
    Cette fonction se limite au chiffrement des caractères: [A-Za-z]. Elle ne chiffrera ni les chiffres, ni les espaces,
    ni la ponctuation, ni les caractères accentués.
    :param texte: str: texte à chiffrer
    :param decalage: int: nombre représentant le décalage à appliquer. Un nombre positif décalera le texte vers la droite, un nombre négatif décalera le texte vers la gauche.
    :return: str, texte chiffré.
    """
    texte_chiffre = []

    for caractere in texte:
        if not re.match(REGEX, caractere):
            texte_chiffre.append(caractere)
            continue

        caractere_entier = ord(caractere)

        if 65 <= caractere_entier <= 90:

            caractere_entier -= 65

            caractere_entier = (caractere_entier + decalage) % 26

            caractere_entier += 65

            lettre_cryptee = chr(caractere_entier)
            texte_chiffre.append(lettre_cryptee)

        elif 97 <= caractere_entier <= 122:

            caractere_entier -= 97

            caractere_entier = (caractere_entier + decalage) % 26

            caractere_entier += 97

            lettre_cryptee = chr(caractere_entier)
            texte_chiffre.append(lettre_cryptee)




    texte_chiffre = ''.join(texte_chiffre)



    return texte_chiffre
