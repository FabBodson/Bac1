liste = [5, 1, 1, 2, 5, 6, 3, 4, 4, 4, 2]

sans_doublon = []

for element in liste:

    if element in sans_doublon:
        continue
    else:
        sans_doublon.append(element)

print(sans_doublon)