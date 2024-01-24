
ALIMENTATION = "Installer des ventilateurs d'alimentation"
EXTRACTION = "Installer des ventilateurs d'extraction"
ALIM_EXTRAC = "Installer des ventilateurs d'alimentation et d'extraction"
REPONSE_INCORRECTE = 'Réponse incorrecte !'


def _main():
    pass

if __name__ == '__main__':
    _main()



type_chauffage = str.upper(input("Quel type de chauffage ? (A)ir chaud puisé ? (C)ombustion ? \n"))


if type_chauffage == 'A':
    sol_gaz = str.upper(input("Le sol est-il saturé de gaz ? (OUI/NON) \n"))

    if sol_gaz == 'NON':
        print(EXTRACTION)
    elif sol_gaz == 'OUI':
        print(ALIM_EXTRAC)
    else:
        print(REPONSE_INCORRECTE)


if type_chauffage == 'C':
    humidite = int(input("Quel est le taux d'humidité en % ? \n"))

    if 0 < humidite < 100 :

        if humidite > 70:
            print(ALIM_EXTRAC)

        elif humidite <= 70:
            print(ALIMENTATION)

    else:
        print(REPONSE_INCORRECTE)