#Acquisition Lundi

lundi_heures = input("Combien d'heures avez-vous prestées lundi ? \n")
lundi_min = input("Combien de minutes avez-vous prestées lundi ? \n")

lundi = f"{lundi_heures}:{lundi_min}"
lundi = lundi.zfill(5)

lundi_heures = int(lundi_heures)*3600
lundi_min = int(lundi_min)*60

print(f"Vous avez presté {lundi} lundi.")





#Acquisition Mardi

mardi_heures = input("Combien d'heures avez-vous prestées mardi ? \n")
mardi_min = input("Combien de minutes avez-vous prestées mardi ? \n")

mardi = f"{mardi_heures}:{mardi_min}"
mardi = mardi.zfill(5)

mardi_heures = int(mardi_heures)*3600
mardi_min = int(mardi_min)*60

print(f"Vous avez presté {mardi} mardi.")





#Acquisition Mercredi

mercredi_heures = input("Combien d'heures avez-vous prestées mercredi ? \n")
mercredi_min = input("Combien de minutes avez-vous prestées mercredi ? \n")

mercredi = f"{mercredi_heures}:{mercredi_min}"
mercredi = mercredi.zfill(5)

mercredi_heures = int(mercredi_heures)*3600
mercredi_min = int(mercredi_min)*60

print(f"Vous avez presté {mercredi} mercredi.")





#Acquisition Jeudi

jeudi_heures = input("Combien d'heures avez-vous prestées jeudi ? \n")
jeudi_min = input("Combien de minutes avez-vous prestées jeudi ? \n")

jeudi = f"{jeudi_heures}:{jeudi_min}"
jeudi = jeudi.zfill(5)

jeudi_heures = int(jeudi_heures)*3600
jeudi_min = int(jeudi_min)*60

print(f"Vous avez presté {jeudi} jeudi.")





#Acquisition vendredi

vendredi_heures = input("Combien d'heures avez-vous prestées vendredi ? \n")
vendredi_min = input("Combien de minutes avez-vous prestées vendredi ? \n")

vendredi = f"{vendredi_heures}:{vendredi_min}"
vendredi = vendredi.zfill(5)

vendredi_heures = int(vendredi_heures)*3600
vendredi_min = int(vendredi_min)*60

print(f"Vous avez presté {vendredi} vendredi.")




#Traitement

jour = 0

secondes = lundi_heures + mardi_heures + mercredi_heures + jeudi_heures + vendredi_heures + lundi_min + mardi_min + mercredi_min + jeudi_min + vendredi_min

salaire = ( secondes / 3600 ) * 50

jour = secondes // 86400
reste = secondes % 86400

heures = reste // 3600
reste = reste % 3600

minutes = reste // 60
reste = reste % 60

secondes = reste



print(f"Cette semaine vous avez presté {jour} jour(s) {heures} heures {minutes} minutes ! \nVous avez donc gagner {salaire} € !!\n")
