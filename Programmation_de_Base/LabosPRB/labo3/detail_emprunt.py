import emprunt


capital = float(input("Quel est le capital que vous souhaitez emprunter ?\n"))


taux_annuel = float(input("Quel est le taux annuel en % ?\n")) / 100


annee_remboursement = int(input("En combien d'années voulez_vous rembourser ?\n"))


nb_mensualites = annee_remboursement * 12



taux_mensuel = emprunt.calculer_taux_mensuel(taux_annuel) * 100
taux_mensuel = round(taux_mensuel, 5)



remboursement_mensuel = emprunt.calculer_mensualite(capital, taux_annuel, nb_mensualites)
remboursement_mensuel = round(remboursement_mensuel, 2)



#Année 1 :
mensualites_restantes_a1 = nb_mensualites - 12

solde_a1 = round(emprunt.calculer_solde_capital(capital, taux_annuel, nb_mensualites, mensualites_restantes_a1), 2)

capital_rembourse_a1 = round(capital - solde_a1, 2)

interets_rembourses_a1 = round((remboursement_mensuel * 12) - (capital - solde_a1), 2)



#Année 2 :

mensualites_restantes_a2 = nb_mensualites - 24

solde_a2 = round(emprunt.calculer_solde_capital(capital, taux_annuel, nb_mensualites, mensualites_restantes_a2), 2)

capital_rembourse_a2 = round(solde_a1 - solde_a2, 2)

interets_rembourses_a2 = round((remboursement_mensuel * 12) - (solde_a1 - solde_a2), 2)





#Année 3 :

mensualites_restantes_a3 = nb_mensualites - 36

solde_a3 = round(emprunt.calculer_solde_capital(capital, taux_annuel, nb_mensualites, mensualites_restantes_a3), 2)

capital_rembourse_a3 = round(solde_a2 - solde_a3, 2)

interets_rembourses_a3 = round((remboursement_mensuel * 12) - (solde_a2 - solde_a3), 2)






total_rembourse = remboursement_mensuel * nb_mensualites

interets_pret = round(total_rembourse - capital, 2)


print(f"\nTaux d'interet mensuel : {taux_mensuel} %\n")
print(f"Nombre de paiements = {nb_mensualites}\n")
print(f"Remboursement mensuel en {annee_remboursement} ans : {remboursement_mensuel} €\n")


print(f"\nCapital emprunté : {capital} €\n")
print(f"Total remboursé = {total_rembourse} €\n")
print(f"Interets pret = {interets_pret} €\n")



print("Année 1: \n")

print(f"\tSolde du capital = {solde_a1} €\n")
print(f"\tCapital remboursé = {capital_rembourse_a1} €\n")
print(f"\tInterets remboursés = {interets_rembourses_a1} €\n")


print("Année 2: \n")

print(f"\tSolde du capital = {solde_a2} €\n")
print(f"\tCapital remboursé = {capital_rembourse_a2} €\n")
print(f"\tInterets remboursés = {interets_rembourses_a2} €\n")



print("Année 3: \n")

print(f"\tSolde du capital = {solde_a3} €\n")
print(f"\tCapital remboursé = {capital_rembourse_a3} €\n")
print(f"\tInterets remboursés = {interets_rembourses_a3} €\n")