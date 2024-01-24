import math


#Définition des fonctions


def calculer_norme_vecteur(x, y):
    """
    Fonction permettant de calculer la norme d'un vecteur(x, y)
    :param x: nombre réel définissant la position du vecteur selon l'axe x
    :param y: nombre réel définissant la position du vecteur selon l'axe y
    :return: nombre réel représentant la norme du vecteur
    """
    norme_v = math.sqrt(x ** 2 + y ** 2)

    arrondi = round(norme_v, 1)

    return arrondi



#Acquisition des coordonne-ées du vecteur

x = float(input("Quelle est la valeur en X du vecteur ? \n"))
y = float(input("Quelle est la valeur en Y du vecteur ? \n"))


#Affichage

print(f"La norme arrondie du vecteur ({x}, {y}) est {calculer_norme_vecteur(x, y)}\n")
