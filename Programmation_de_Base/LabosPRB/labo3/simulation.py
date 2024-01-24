import emprunt




capital = float(input("Quel est le capital que vous souhaitez emprunter ?\n"))

taux_annuel = float(input("Quel est le taux annuel en % ?\n")) / 100

nb_durees = int(input("Combien de durées voulez-vous calculer (1 ou 2) ? \n"))


if nb_durees == 1:
    annee_remboursement = int(input("En combien d'années voulez_vous rembourser ?\n"))

    nb_mensualites = annee_remboursement * 12


    taux_mensuel = emprunt.calculer_taux_mensuel(taux_annuel) * 100
    taux_mensuel = round(taux_mensuel, 5)


    remboursement_mensuel = emprunt.calculer_mensualite(capital, taux_annuel, nb_mensualites)
    remboursement_mensuel = round(remboursement_mensuel, 2)



    print(f"\nCapital à emprunter : {capital:>19} €\n")
    print(f"Taux d'interet mensuel : {taux_mensuel:>16} %\n")
    print(f"Remboursement mensuel sur {annee_remboursement} ans : {remboursement_mensuel} €\n")



else:

    annee_remboursement1 = int(input("Durée 1 : en combien d'années voulez_vous rembourser ?\n"))
    annee_remboursement2 = int(input("\nDurée 2 : en combien d'années voulez_vous rembourser ?\n"))


    nb_mensualites1 = annee_remboursement1 * 12
    nb_mensualites2 = annee_remboursement2 * 12


    taux_mensuel = emprunt.calculer_taux_mensuel(taux_annuel) * 100
    taux_mensuel = round(taux_mensuel, 5)


    remboursement_mensuel1 = emprunt.calculer_mensualite(capital, taux_annuel, nb_mensualites1)
    remboursement_mensuel1 = round(remboursement_mensuel1, 2)


    remboursement_mensuel2 = emprunt.calculer_mensualite(capital, taux_annuel, nb_mensualites2)
    remboursement_mensuel2 = round(remboursement_mensuel2, 2)


    print(f"\nCapital à emprunter : {capital:>10} €\n")
    print(f"Taux d'interet mensuel : {taux_mensuel} %\n")


    #Durée 1 :

    print(f"Sur {annee_remboursement1} ans :\n")

    print(f"\tNombre de paiements = {nb_mensualites1} fois\n")
    print(f"\tRemboursement mensuel = {remboursement_mensuel1} €\n")

    total_rembourse1 = round(remboursement_mensuel1 * nb_mensualites1, 2)
    print(f"\tTotal remboursé = {total_rembourse1:>12} €\n")

    interet_pret1 = round(total_rembourse1 - capital, 2)
    print(f"\tInterets pret = {interet_pret1:>14} €\n")


    #Durée 2 :

    print(f"Sur {annee_remboursement2} ans :\n")

    print(f"\tNombre de paiements = {nb_mensualites2} fois\n")
    print(f"\tRemboursement mensuel = {remboursement_mensuel2} €\n")

    total_rembourse2 = round(remboursement_mensuel2 * nb_mensualites2, 2)
    print(f"\tTotal remboursé = {total_rembourse2:>12} €\n")

    interet_pret2 = round(total_rembourse2 - capital, 2)
    print(f"\tInterets pret = {interet_pret2:>14} €\n")




