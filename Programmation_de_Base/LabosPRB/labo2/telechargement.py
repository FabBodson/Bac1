#Interface

print("Calculons le temps de téléchargement...\n")


#Acquisition

nom = input("Quel est le nom du fichier ?\n")

fichier_giga = int(input("Si votre fichier est en Go, appuyez sur 1\nSi votre fichier est en Mo, appuyez sur 2\n"))

vitesse = float(input("\nQuelle est la vitesse de votre connexion internet en Mbps ?\n"))


#Calculs des données récupérées

if fichier_giga == 1:

    fichier = float(input("Quelle est la taille de votre fichier ?\n"))*1024

    mbits = fichier * 8

    secondes = mbits / vitesse

    jours = secondes // 86400
    reste = secondes % 86400

    heures = reste // 3600
    reste = reste % 3600

    minutes = reste // 60
    reste = reste % 60

    secondes = reste



if fichier_giga == 2:

    fichier = float(input("Quelle est la taille de votre fichier ?\n"))

    mbits = fichier * 8

    secondes = mbits / vitesse

    jours = secondes // 86400
    reste = secondes % 86400

    heures = reste // 3600
    reste = reste % 3600

    minutes = reste // 60
    reste = reste % 60

    secondes = reste



#Affichage

print(f"\nLe téléchargement de votre fichier {nom} prendra exactement :\n")
print(f"{jours} jours {heures} heures {minutes} minutes {secondes} secondes")
