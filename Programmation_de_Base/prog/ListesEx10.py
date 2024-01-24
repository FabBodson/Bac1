nombre = 20
liste = []

for i in range(nombre):
    liste.append(i + 1)
liste.remove(1)


i = 0

while i < len(liste):
    j = i+1

    while j < len(liste):
        if (liste[j]%liste[i]) == 0:
            liste.pop(j)
            j += 1
        else:
            j += 1
    i += 1



print(liste)