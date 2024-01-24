import control

def construire_rectangle(x, y, largeur, hauteur, couleur_de_fond=None, couleur_du_bord=None):
    """
    Cette fonction construit la liste de commandes nécessaires au dessin d'un rectangle.
    Le coin supérieur gauche de ce rectangle sera défini à la position x, y.
    :param x: int, abscisse du coin supérieur gauche du rectangle
    :param y: int, ordonnée du coin supérieur gauche du rectangle
    :param largeur: int, largeur du rectangle
    :param hauteur: int, hauteur du rectangle
    :param couleur_de_fond: tuple[int, int, int] ou None: couleur de fond du rectangle au format (rouge, vert, bleu). Ce paramètre est optionnel.
    :param couleur_du_bord: tuple[int, int, int] ou None: couleur du tracé du rectangle au format (rouge, vert, bleu). Ce paramètre est optionnel.
    :return: list, une liste contenant les commandes à exécuter pour dessiner le rectangle
    """
    rectangle = [
        (control.STOP_FILL,),
        (control.STOP_DRAW,),

        (control.SET_POSITION, (x, y)),

        (control.SET_PEN_COLOR, couleur_du_bord),
        (control.START_DRAW, ),
        (control.SET_FILL_COLOR, couleur_de_fond),
        (control.START_FILL, ),

        (control.ROTATE_RIGHT, 90),
        (control.MOVE_FORWARD, hauteur),

        (control.ROTATE_RIGHT, 90),
        (control.MOVE_FORWARD, largeur),

        (control.ROTATE_RIGHT, 90),
        (control.MOVE_FORWARD, hauteur),

        (control.ROTATE_RIGHT, 90),
        (control.MOVE_FORWARD, largeur),

        (control.STOP_FILL, ),
        (control.STOP_DRAW, ),
    ]

    return rectangle




def construire_carre(x, y, taille, couleur_de_fond=None, couleur_du_bord=None):
    """
    Cette fonction construit la liste de commandes nécessaires au dessin d'un carré.
    Le coin supérieur gauche de ce carré sera défini à la position x, y.
    :param x: int, abscisse du coin supérieur gauche du carré
    :param y: int, ordonnée du coin supérieur gauche du carré
    :param taille: int, taille du carré
    :param couleur_de_fond: tuple[int, int, int] ou None: couleur de fond du rectangle au format (rouge, vert, bleu). Ce paramètre est optionnel.
    :param couleur_du_bord: tuple[int, int, int] ou None: couleur du tracé du rectangle au format (rouge, vert, bleu). Ce paramètre est optionnel.
    :return: list, une liste contenant les commandes à exécuter pour dessiner le carré
    """
    carre = [
        (control.STOP_FILL,),
        (control.STOP_DRAW,),

        (control.SET_POSITION, (x, y)),
        (control.SET_PEN_COLOR, couleur_du_bord),
        (control.START_DRAW,),
        (control.SET_FILL_COLOR, couleur_de_fond),
        (control.START_FILL,),

        (control.ROTATE_RIGHT, 90),
        (control.MOVE_FORWARD, taille),

        (control.ROTATE_RIGHT, 90),
        (control.MOVE_FORWARD, taille),

        (control.ROTATE_RIGHT, 90),
        (control.MOVE_FORWARD, taille),

        (control.ROTATE_RIGHT, 90),
        (control.MOVE_FORWARD, taille),

        (control.STOP_FILL,),
        (control.STOP_DRAW,),
    ]

    return carre




def construire_triangle(x1, y1, x2, y2, x3, y3, couleur_de_fond=None, couleur_du_bord=None):
    """
    Cette fonction construit la liste de commandes nécessaires au dessin d'un triangle.
    :param x1: int, abscisse du premier sommet du triangle
    :param y1: int, ordonnée du premier sommet du triangle
    :param x2: int, abscisse du deuxième sommet du triangle
    :param y2: int, ordonnée du deuxième sommet du triangle
    :param x3: int, abscisse du troisième sommet du triangle
    :param y3: int, ordonnée du troisième sommet du triangle
    :param couleur_de_fond: tuple[int, int, int] ou None: couleur de fond du rectangle au format (rouge, vert, bleu). Ce paramètre est optionnel.
    :param couleur_du_bord: tuple[int, int, int] ou None: couleur du tracé du rectangle au format (rouge, vert, bleu). Ce paramètre est optionnel.
    :return: list, une liste contenant les commandes à exécuter pour dessiner le triangle
    """

    triangle = [
        (control.STOP_FILL,),
        (control.STOP_DRAW,),

        (control.SET_POSITION, (x1, y1)),

        (control.SET_PEN_COLOR, couleur_du_bord),
        (control.START_DRAW, ),
        (control.SET_FILL_COLOR, couleur_de_fond),
        (control.START_FILL, ),

        (control.SET_POSITION, (x2, y2)),
        (control.SET_POSITION, (x3, y3)),
        (control.SET_POSITION, (x1, y1)),

        (control.STOP_FILL,),
        (control.STOP_DRAW,),

    ]


    return triangle





