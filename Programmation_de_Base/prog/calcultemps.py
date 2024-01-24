# Acquisition des temps

print("Donnez le temps 1 :")
heure_1 = float(input("Nombre d'heures ? "))
minutes_1 = int(input("Nombre de minutes ? "))
secondes_1 = int(input("Nombre de secondes ? "))

print("Donnez le temps 2 :")
heure_2 = int(input("Nombre d'heures ? "))
minutes_2 = int(input("Nombre de minutes ? "))
secondes_2 = int(input("Nombre de secondes ? "))


# Somme des heures, min, sec

jour = 0
somme_h = heure_1 + heure_2
somme_m = minutes_1 + minutes_2
somme_s = secondes_1 + secondes_2


# Calculs des cas où sec/min =  +60 sec et heure = + 24

if somme_s >= 60:
    while somme_s >= 60:
        somme_m += 1
        somme_s -= 60



if somme_m >= 60:
    while somme_m >= 60:
        somme_h += 1
        somme_m -= 60



if somme_h >= 24:
    if somme_h % 24 == 0:
        jour = somme_h // 24
        somme_h = 0
    else:
        while somme_h >= 24:
            jour += 1
            somme_h -= 24


# Affichage

print("Temps total : ")
print(f" {jour} j")
print(f"{somme_h} h")
print(f"{somme_m} min")
print(f"{somme_s} sec")
