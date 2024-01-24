
prenom = input("Votre prénom ? ")

prenom2 = prenom[-1]

prenom = prenom[:-1] + prenom[0]

prenom3 = prenom2 + prenom[1:]


print(f"{prenom3}")
