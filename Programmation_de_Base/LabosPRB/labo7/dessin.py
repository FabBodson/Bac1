import control
from formes_geometriques import construire_carre, construire_rectangle, construire_triangle

def construire_drapeau_belge():
    """
    Cette fonction construit la liste de commandes nécessaires au dessin du drapeau belge.
    :return: list, une liste contenant les commandes à exécuter pour dessiner le drapeau belge.
    """
    return [

        *construire_rectangle(-130, 90, 65, 180, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), # Noir

        *construire_rectangle(-65, 90, 65, 180, (1.0, 1.0, 0.0), (0.0, 0.0, 0.0)), # Jaune

        *construire_rectangle(0, 90, 65, 180, (1.0, 0.0, 0.0), (0.0, 0.0, 0.0)), # Rouge

        ]




def construire_maison():
    """
    Cette fonction construit la liste de commandes nécessaires au dessin de la maison.
    :return: list, une liste contenant les commandes à exécuter pour dessiner la maison.
    """
    carre = construire_carre(200, 200, 500, (1.0, 1.0, 1.0), (0.0, 0.0, 0.0))

    toit = construire_triangle(200, 200, 0, 400, -200, 200, (1.0, 1.0, 1.0), (0.0, 0.0, 0.0))

    porte = construire_rectangle(20, -100, 60, 150, (0.4, 0.4, 0.4), (0.0, 0.0, 0.0))

    fenetre1 = construire_rectangle(-155, 100, 130, 60, (0.0, 0.74, 1.0), (0.0, 0.0, 0.0))

    fenetre2 = construire_rectangle(225, 100, 130, 60, (0.0, 0.74, 1.0), (0.0, 0.0, 0.0))


    return [*carre, *toit, *porte, *fenetre1, *fenetre2]







def construire_damier(taille):
    """
    Cette fonction construit la liste de commandes nécessaires au dessin d'un damier.
    :param taille: int, désigne le nombre de cases par axe du damier. Exemple: une taille de 8 produira un damier de 8 * 8 cases.
    :return: list, une liste contenant les commandes à exécuter pour dessiner le damier.
    """
    carre_blanc = formes_geometriques.construire_carre(0, 0, 50, (1.0, 1.0, 1.0), (0.0, 0.0, 0.0))

    carre_noir = formes_geometriques.construire_carre(0, 0, 50, (0.4, 0.4, 0.4), (0.0, 0.0, 0.0))

    return carre_noir




def _main():

    control.play([
        #*construire_drapeau_belge(),
        *construire_maison()#,
        #*construire_damier(8),
    ], speed='slow')

if __name__ == '__main__':
    _main()
