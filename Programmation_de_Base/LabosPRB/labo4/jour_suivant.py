import re
from _datetime import datetime



date = input("Entrez une date ([j]j/[m]m/aaaa) : ")


def est_bissextile(annee):
    return annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0)


def jours_dans_mois(mois, annee):
    nb_jours = 31

    if mois < 1 or mois > 12:
        nb_jours = 0

    elif mois == 2:

        if est_bissextile(annee) == True:
            nb_jours = 29
        else:
            nb_jours = 28

    elif mois == 4 or mois == 6 or mois == 9 or mois == 11:
        nb_jours = 30

    return nb_jours


def _main():

    expression = '([1-9]|[0-2][\d]|3[0-1])[/](0?[1-9]|1?[0-2])[/]([\d]{4})'
    est_valide = re.match(expression, date)

    jour = int(est_valide.group(1))
    mois = int(est_valide.group(2))
    annee = int(est_valide.group(3))



    date_du_jour = datetime(day=jour, month=mois, year=annee)
    date_lendemain = datetime(day=jour+1, month=mois, year=annee)


    if est_valide:
        print(f'Date du jour : {date_du_jour.strftime("%d/%m/%Y")}')
        print(f'Date de demain : {date_lendemain.strftime("%d/%m/%Y")}')



    else:
        print('Mauvaise saisie !')








if __name__ == '__main__':
    _main()







