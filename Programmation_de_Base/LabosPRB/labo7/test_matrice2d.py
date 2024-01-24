import unittest
import matrice2d



"""

self.assertEqual(expected, actual)  # Vérifie que la variable "expected" est égal à la variable "actual"
self.assertIs(expected, actual)  # Vérifie que la variable "expected" est exactement la variable "actual" (elles font toutes deux référence au même emplacement mémoire, elles sont donc identiques !)
self.assertListEqual(expected, actual)  # Vérifie que la liste "expected" contient les mêmes éléments que la liste "actual" (et non que ce soit exactement la même liste au même emplacement mémoire !)

"""

class ConvertirEnTexteTest(unittest.TestCase):

    def test_matrice_vide(self):
        matrice = []
        self.assertTrue(matrice2d.convertir_en_texte(matrice))

    def test_matrice_1_element(self):
        matrice = [
        [-10, -20, -30],
        [4, 5, 6],
        [-30, 1, 9]
        ]

        matrice_texte = '|   -10   -20   -30 |\n|     4     5     6 |\n|   -30     1     9 |\n'

        self.assertEqual(matrice_texte, matrice2d.convertir_en_texte(matrice))


class AfficherTest(unittest.TestCase):

    def test_matrice_vide(self):
        matrice = []
        self.assertTrue(matrice2d.convertir_en_texte(matrice))

    def test_affiche(self):
        matrice = [
            [-10, -20, -30],
            [4, 5, 6],
            [-30, 1, 9]
        ]
        self.assertFalse(matrice2d.afficher(matrice))


class MinimumTest(unittest.TestCase):

    def test_matrice_vide(self):
        matrice = []
        self.assertTrue(matrice2d.convertir_en_texte(matrice))

    def test_minimum_trouve(self):
        matrice = [
            [-10, -20, -30],
            [4, 5, 6],
            [-30, 1, 9]
        ]
        self.assertEqual(-30, matrice2d.minimum(matrice))


class MaximumTest(unittest.TestCase):

    def test_maximum_vide(self):
        matrice = []
        self.assertTrue(matrice2d.convertir_en_texte(matrice))

    def test_maximum_trouve(self):
        matrice = [
            [-10, -20, -30],
            [4, 5, 6],
            [-30, 1, 9]
        ]
        self.assertEqual(9, matrice2d.maximum(matrice))


class MinimumParLigne(unittest.TestCase):

    def test_matrice_vide(self):
        matrice = []
        self.assertTrue(matrice2d.convertir_en_texte(matrice))

    def test_minimum_par_ligne_trouve(self):
        matrice = [
            [7, 3, 8],
            [6, 4, 1],
            [5, 2, 7]
        ]
        self.assertListEqual([3, 1, 2], matrice2d.minimum_par_ligne(matrice))


    def test_minimum_par_lignes_egales(self):
        matrice = [
            [3, 3, 3],
            [1, 1, 1],
            [2, 2, 2]
        ]
        self.assertListEqual([3, 1, 2], matrice2d.minimum_par_ligne(matrice))


class MinimumParColonne(unittest.TestCase):

    matrice = [
        [7, 3, 8],
        [6, 4, 1],
        [5, 2, 7]
    ]

    def test_matrice_vide(self):
        matrice = []
        self.assertTrue(matrice2d.convertir_en_texte(matrice))


    def test_minimum_par_ligne_trouve(self):
        matrice = [
            [7, 3, 8],
            [6, 4, 1],
            [5, 2, 7]
        ]
        self.assertListEqual([5, 2, 1], matrice2d.minimum_par_colonne(matrice))


    def test_minimum_par_lignes_egales(self):
        matrice = [
            [3, 3, 3],
            [1, 1, 1],
            [2, 2, 2]
        ]
        self.assertListEqual([1, 1, 1], matrice2d.minimum_par_colonne(matrice))



class Additionner(unittest.TestCase):
    def test_matrice_vide(self):
        matrice = []
        self.assertTrue(matrice2d.convertir_en_texte(matrice))

    def test_addition_matrices_positifs(self):
        matrice1 = [
            [3, 3, 3],
            [1, 1, 1],
            [2, 2, 2]
        ]

        matrice2= [
            [7, 3, 8],
            [6, 4, 1],
            [5, 2, 7]
        ]

        self.assertEqual([[10, 6, 11], [7, 5, 2], [7, 4, 9]], matrice2d.additionner(matrice1, matrice2))

    def test_addition_matrices_positifs(self):
        matrice1 = [
            [3, 3, 3],
            [1, 1, 1],
            [2, 2, 2]
        ]
        matrice2 = [
            [7, 3, 8],
            [6, 4, 1]
        ]
        self.assertTrue(matrice2d.additionner(matrice1, matrice2))
