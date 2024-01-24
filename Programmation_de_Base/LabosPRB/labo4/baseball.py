
MATCH_JOUE = 'Le match sera joué !'

MATCH_REPORTE = 'Le match sera reporté …'

REPONSE_INCORRECTE = 'Réponse incorrecte !'


def _main():
    pass

if __name__ == '__main__':
    _main()





temps = str.upper(input("Quel temps fait-il ? (E)nsoleillé ? (P)luvieux ? (N)uageux ? \n"))



if temps == 'P':
    print(MATCH_REPORTE)


elif temps == 'E':
    print(MATCH_JOUE)


if temps == 'N':
    humidite = int(input("Quelle est le taux d'humidité en % ? \n"))

    if 0 < humidite < 100 :

        if humidite >= 90:
            print(MATCH_REPORTE)

        elif humidite < 90:
            print(MATCH_JOUE)

else:
    print(REPONSE_INCORRECTE)


