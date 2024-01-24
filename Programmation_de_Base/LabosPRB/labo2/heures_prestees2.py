
#Definition de fonctions

def lire_heures(hhmm):
    """
    Fonction recuperant un nombre d'heures à partir d'un texte au format "hh:mm"
    :param hhmm: texte au format "hh:mm"
    :return: nombre entier representant un nombre d'heures
    """


    return hhmm[0:2]



def lire_minutes(hhmm):
    """
    Fonction recuperant un nombre de minutes à partir d'un texte au format "hh:mm"
    :param hhmm: texte au format "hh:mm"
    :return: nombre entier representant un nombre de minutes
    """


    return hhmm[3:5]




def convertir_en_minutes(hhmm):
    """
    Fonction calculant le nombre de minutes contenues dans un temps exprimé sous la forme d'un texte au format("hh:mm")
    :param hhmm: texte au format "hh:mm"
    :return: nombre entier representant un nombre de minutes
    """




#Acquisition Lundi

lundi = input("Combien d'heures avez-vous prestés lundi (Format -> hh:mm) ? \n")

#Affichage
lundi = lundi.zfill(5)
lundi = f"{lire_heures(lundi)}:{lire_minutes(lundi)}"


print(f"Vous avez presté {lundi} lundi.")


#Conversion en entier

lundi_heures_int = int(lire_heures(lundi))
lundi_minutes_int = int(lire_minutes(lundi))

#Conversion en secondes

lundi_heures_secondes = lundi_heures_int * 3600

lundi_min_secondes = lundi_minutes_int * 60

lundi_secondes = lundi_heures_secondes + lundi_min_secondes




#Acquisition Mardi

mardi = input("Combien d'heures avez-vous prestés mardi (Format -> hh:mm) ? \n")

#Affichage
mardi = mardi.zfill(5)
mardi = f"{lire_heures(mardi)}:{lire_minutes(mardi)}"

print(f"Vous avez presté {mardi} mardi.")


#Conversion en entier

mardi_heures_int = int(lire_heures(mardi))
mardi_minutes_int = int(lire_minutes(mardi))

#Conversion en secondes

mardi_heures_secondes = mardi_heures_int * 3600

mardi_min_secondes = mardi_minutes_int * 60

mardi_secondes = mardi_heures_secondes + mardi_min_secondes




#Acquisition Mercredi

mercredi = input("Combien d'heures avez-vous prestés mercredi (Format -> hh:mm) ? \n")

#Affichage
mercredi = mercredi.zfill(5)
mercredi = f"{lire_heures(mercredi)}:{lire_minutes(mercredi)}"

print(f"Vous avez presté {mercredi} mercredi.")


#Conversion en entier

mercredi_heures_int = int(lire_heures(mercredi))
mercredi_minutes_int = int(lire_minutes(mercredi))

#Conversion en secondes

mercredi_heures_secondes = mercredi_heures_int * 3600

mercredi_min_secondes = mercredi_minutes_int * 60

mercredi_secondes = mercredi_heures_secondes + mercredi_min_secondes





#Acquisition Jeudi

jeudi = input("Combien d'heures avez-vous prestés jeudi (Format -> hh:mm) ? \n")

#Affichage
jeudi = jeudi.zfill(5)
jeudi = f"{lire_heures(jeudi)}:{lire_minutes(jeudi)}"

print(f"Vous avez presté {jeudi} jeudi.")


#Conversion en entier

jeudi_heures_int = int(lire_heures(jeudi))
jeudi_minutes_int = int(lire_minutes(jeudi))

#Conversion en secondes

jeudi_heures_secondes = jeudi_heures_int * 3600

jeudi_min_secondes = jeudi_minutes_int * 60

jeudi_secondes = jeudi_heures_secondes + jeudi_min_secondes





#Acquisition Vendredi


vendredi = input("Combien d'heures avez-vous prestés vendredi (Format -> hh:mm) ? \n")

#Affichage
vendredi = vendredi.zfill(5)
vendredi = f"{lire_heures(vendredi)}:{lire_minutes(vendredi)}"

print(f"Vous avez presté {vendredi} vendredi.")


#Conversion en entier

vendredi_heures_int = int(lire_heures(vendredi))
vendredi_minutes_int = int(lire_minutes(vendredi))

#Conversion en secondes

vendredi_heures_secondes = vendredi_heures_int * 3600

vendredi_min_secondes = vendredi_minutes_int * 60

vendredi_secondes = vendredi_heures_secondes + vendredi_min_secondes





jour = 0
secondes = lundi_secondes + mardi_secondes + mercredi_secondes + jeudi_secondes + vendredi_secondes

salaire = secondes / 3600 *50

jour = secondes // 86400
reste = secondes % 86400

heures = reste // 3600
reste = reste % 3600

minutes = reste // 60
reste = reste % 60

secondes = reste



print(f"Cette semaine vous avez presté {jour} jour(s) {heures} heures {minutes} minutes ! \nVous avez donc gagner {salaire} € !!\n")
