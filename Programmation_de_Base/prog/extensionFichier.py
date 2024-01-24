nom_fichier = input("Quel est le nom du fichier ? (Extension comprise)\n")

for caracter in nom_fichier:
    if caracter == '.':
        point = nom_fichier.index(caracter)

extension = nom_fichier[point+1:]

print(extension)