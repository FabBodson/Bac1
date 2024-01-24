def annee_bissextile(annee)

    if annee % 400 == 0:
        return annee
    elif (annee % 4) and (annee %100 ! 0):
        return annee
    else:
        return False


def jour_dans_mois(mois, annee):

    jours = 31
    if mois < 1 or mois > 12:
        return False

    elif mois == 2:
        if annee_bissextile(annee):
            jours = 29
        else:
            jours = 28

    elif (mois == 4) or (mois == 6) or (mois == 9) or (mois == 11):
        jours = 30

    return jours

def _main():


if __name__ == '__main__':
