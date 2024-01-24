print("Bonjour, nous allons calculer le montant de votre voiture selon la TVA et remise !\n")

prix_de_base = int(input("Prix de la voiture : "))

tva = prix_de_base * 21 / 100

prix_tva = prix_de_base + tva

remise = prix_tva * 3 / 100

prix_final = prix_tva - remise

print(f"Montant de la TVA : {tva} €\nMontant de la remise : {remise}€\nPrix total : {prix_final}€\n")
