from algo_labo02.model import User, Essence, Component, Choice, Flask, Result
from algo_labo02.file import read_csv_file, write_csv_file
from algo_labo02.algorithms import ajouter_produits, create_list_of_components, create_essences


def _main():
    global seq
    print("Bonjour, encodez les informations de l'utilisateur:\n")
    seq = 0
    nom = "Dupont"
    prenom = "Mike"
    telephone = "012345678"
    email = "DMUPIK.LU951@yahoo.fr"

    user = User(nom, prenom, telephone, email)

    gouts = []
    odeur = ""

    # Lecture du fichier posologie.csv qui fournit sous forme de dictionnaire les détails des gouts/odeurs
    liste_posologie = read_csv_file("posologie.csv")
    # Liste des noms des produits disponibles
    liste_produits = ajouter_produits(liste_posologie)

    print("--- Sélection de 2 goûts et 1 odeur ---")

    # Tant que les 2 gouts et l'odeur n'ont pas été sélectionnés #
    while len(gouts) < 2 or odeur == "":
        if len(gouts) < 2:
            choix = input(f"Encodez le {len(gouts) + 1}er goût  ou  LST pour voir les goûts disponible ? ")
        else:
            choix = input(f"Encodez l'odeur voulue  ou  LST pour voir les goûts disponible ? ")

        # Si l'utilisateur veut afficher la liste des choix #
        if choix == "LST":
            print("Voici les goûts disponibles:\n")
            afficher_produits(liste_produits)
        else:
            # Si le produit n'est pas disponible #
            if choix not in liste_produits:
                print(f"Le {choix} n'est pas disponible…")
            else:
                # Si les 2 gouts n'ont pas encore été sélectionnés #
                if len(gouts) < 2:
                    gouts.append(choix)
                # Si les 2 gouts ont été sélectionnés mais pas l'odeur #
                else:
                    odeur += choix


    # Affichage des choix #
    choix_user = Choice(gouts, odeur)
    choix_user.print_choice()

    # Affichage des essences choisies #
    choix_user.print_essence_choisies(liste_posologie, gouts)

    # Composition du flacon #
    print(" - - - - Composition de votre flacon - - - - ")

    liste_components = create_list_of_components(liste_posologie, gouts)
    liste_essences = create_essences(liste_components)

    # Le flacon contient une liste d'essences ainsi qu'une référence
    flacon = Flask(liste_essences)
    print("Votre flacon porte le nom:", flacon.create_reference(gouts))

    # Resultat
    resultat = Result(user.lastname, user.firstname, user.phone, user.email)
    seq += 1
    print("Votre lot de fabrication est:", resultat.create_lot_date(seq))

    # Ecriture dans le fichier
    write_csv_file("lot_distribution.csv", user, flacon, resultat)

    # Good bye #
    print("--- - - - - - - - - - - - - - - --- \nA bientot.")


if __name__ == '__main__':
    _main()
