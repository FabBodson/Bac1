intervalle = int(input('Entrez un nombre >= 1: '))

somme = 0

for i in range(intervalle):
    if (i % 3 == 0) or (i % 5 == 0):
        somme += i
    else:
        continue

print(somme)