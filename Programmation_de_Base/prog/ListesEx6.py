liste = [8, 3, 12.5, 45, 25.5, 52, 1]

liste_triee = []

while 0 < len(liste):
    liste_triee.append(min(liste))
    liste.remove(min(liste))

print(f'Liste 1: {liste}')
print(f'Liste triée: {liste_triee}')