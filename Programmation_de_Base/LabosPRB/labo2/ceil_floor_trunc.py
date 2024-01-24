import math

#Acquisition

x = float(input("Entrez une valeur pour X : \n"))

#Fonction de la librairie math

valeur = math.ceil(x)

print(f"\nFontion ceil : {valeur}")

valeur = math.floor(x)

print(f"\nFontion floor : {valeur}")

valeur = math.trunc(x)

print(f"\nFontion trunc : {valeur}\n")
