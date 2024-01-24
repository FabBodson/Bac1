animaux = ['lapin', 'chat', 'chien', 'chiot', 'dragon', 'ornithorynque']

animaux_domestiques = animaux[:4].copy()

for i in range(len(animaux_domestiques)):

    if animaux[0] == animaux_domestiques[i]:
        animaux.remove(animaux[0])

    else:
        continue

animaux.reverse()

animaux.sort()

animaux.append('troll')

print(f'Animaux: {animaux}')

for i in range(len(animaux)):
    print(len(animaux[i]), end=" ")


print(f'\n\nDomestiques: {animaux_domestiques}')

for l in range(len(animaux_domestiques)):
    print(len(animaux_domestiques[l]), end=" ")

