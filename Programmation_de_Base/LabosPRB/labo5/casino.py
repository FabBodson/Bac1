import random




def _main():
    mise_depart = int(input('Quelle est votre mise de départ ? \n'))
    solde_mise_en_cours = mise_depart - 1
    gain_final = int(input('Quelle sont les gains souhaités ? \n'))
    gain_en_cours = 0

    nb_paris = 0
    paris_gagné = 0
    paris_perdu = 0

    if mise_depart == 0:
        mise_depart = print('Pas de mise, pas de paris ! ')

    else:

        while (0 <= solde_mise_en_cours <= gain_final) or (gain_en_cours < gain_final):

            pari_gagnant = random.random()

            if pari_gagnant < 0.5: #gagné
                gain_en_cours += 1
                solde_mise_en_cours += 1
                paris_gagné += 1


            else : #perdu
                gain_en_cours -= 1
                solde_mise_en_cours -= 1
                paris_perdu += 1

            nb_paris += 1



        print(f'Mise de départ : {mise_depart} EUROS\n')
        print(f'Gain souhaités : {gain_final} EUROS\n')

        print(f'Vous avez gagné {paris_gagné} sur {nb_paris} paris\n')
        print(f'Vous avez gagné : {gain_en_cours} EUROS')


if __name__ == '__main__':
    _main()

