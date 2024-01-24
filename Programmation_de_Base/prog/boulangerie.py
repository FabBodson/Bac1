# Constantes
PU_CROISSANT = 0.8
PU_PAIN_AU_CHOCOLAT = 0.9
PU_BAGUETTE = 1.1
PU_PAIN = 2.1
POURCENTAGE_FIDELITE = 0.1


# Acquisition des données
nb_croissants = int(input("Nombre de croissants: "))
nb_pains_au_chocolat = int(input("Nombre de pains au chcolat : "))
nb_baguettes = int(input("Nombre de baguettes : "))
nb_pains = int(input("Nombre de pains: "))



# Traitement des données

# 1. Calculer le montant total des achats
montant_achats = nb_croissants * PU_CROISSANT
montant_achats += nb_pains_au_chocolat * PU_PAIN_AU_CHOCOLAT
montant_achats += nb_baguettes * PU_BAGUETTE
montant_achats += nb_pains * PU_PAIN


# 2. Calculer le montant de fidélité
montant_fidelite = montant_achats * POURCENTAGE_FIDELITE

# Affichage
print(montant_achats)
print(montant_fidelite)
