t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre',
      'Décembre']


# Création t3

t3 = []

for i in range(len(t1)):
      t3.append(t2[i])
      t3.append(t1[i])
print(t3)



# Les éléments pars et impairs

liste_pairs = []
liste_impairs = []

for mois in t1:
      if mois % 2 == 0:
            liste_pairs.append(mois)
      else:
            liste_impairs.append(mois)

print(liste_pairs)
print(liste_impairs)



# Calcul du Xe jour de l'année

mois = 'Février'
jour = 12
somme_jours = 0

for i in range(len(t2)):
      if t2[i] == mois:

            for j in range(t1[i]):
                  if j == jour-1:
                        somme_jours += 1
                        break
                  else:
                        somme_jours += 1
            break
      else:
            somme_jours += t1[i]

print(f"Le {jour} {mois} est le {somme_jours}e jour de l'année!")