nombre = 7805
somme = 0

chiffre = nombre % 10
print(f"Chiffre ligne 4 : {chiffre}\n")
somme = somme + chiffre
print(f"Somme ligne 4 : {somme}\n")
nombre = nombre / 10
print(f"Nombre ligne 4 : {nombre}\n")


chiffre = nombre % 10
print(f"Chiffre ligne 8 : {chiffre}\n")
somme = somme + chiffre
print(f"Somme ligne 8 : {somme}\n")
nombre = nombre / 10
print(f"Nombre ligne 8 : {nombre}\n")


chiffre = nombre % 10
print(f"Chiffre ligne 12 : {chiffre}\n")
somme = somme + chiffre
print(f"Somme ligne 12 : {somme}\n")
nombre = nombre / 10
print(f"Nombre ligne 12 : {nombre}\n")


chiffre = nombre ** 10
print(f"Chiffre ligne 16 : {chiffre}\n")
somme = somme + chiffre
print(f"Somme ligne 16 : {somme}\n")
nombre = nombre // 3
print(f"Nombre ligne 16 : {nombre}\n")



print(f"Chiffre ligne 20 : {chiffre}\n")
print(f"Somme ligne 20 : {somme}\n")
print(f"Nombre ligne 20 : {nombre}\n")
