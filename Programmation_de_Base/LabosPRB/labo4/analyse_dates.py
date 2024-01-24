import re

dates = input("Entrez une date : ")



def _main():

    expression = '([0-2][\d]|3[0-1])[/](0[1-9]|1[0-2])[/]([\d]{4})'
    est_valide = re.match(expression, dates)

    groupe1 = est_valide.group(1)
    groupe2 = est_valide.group(2)
    groupe3 = est_valide.group(3)


    print(f"Jour = {groupe1}\n")


    if groupe2 == '01':
        groupe2 = 'Janvier'
        print(f"Mois = {groupe2}\n")

    elif groupe2 == '02':
        groupe2 = 'Février'
        print(f"Mois = {groupe2}\n")

    elif groupe2 == '03':
        groupe2 = 'Mars'
        print(f"Mois = {groupe2}\n")

    elif groupe2 == '04':
        groupe2 = 'Avril'
        print(f"Mois = {groupe2}\n")

    elif groupe2 == '05':
        groupe2 = 'Mai'
        print(f"Mois = {groupe2}\n")

    elif groupe2 == '06':
        groupe2 = 'Juin'
        print(f"Mois = {groupe2}\n")

    elif groupe2 == '07':
        groupe2 = 'Juillet'
        print(f"Mois = {groupe2}\n")

    elif groupe2 == '08':
        groupe2 = 'Aout'
        print(f"Mois = {groupe2}\n")

    elif groupe2 == '09':
        groupe2 = 'Septembre'
        print(f"Mois = {groupe2}\n")

    elif groupe2 == '10':
        groupe2 = 'Octobre'
        print(f"Mois = {groupe2}\n")

    elif groupe2 == '11':
        groupe2 = 'Novembre'
        print(f"Mois = {groupe2}\n")

    elif groupe2 == '12':
        groupe2 = 'Décembre'
        print(f"Mois = {groupe2}\n")


    print(f"Année = {groupe3}\n")


if __name__ == '__main__':
    _main()

