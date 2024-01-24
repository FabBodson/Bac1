chaine1 = 'abc'
chaine2 = 'de'

liste = []

for i in range(len(chaine1)):
    for j in range(len(chaine2)):
        liste.append(chaine1[i]+chaine2[j])

print(liste)