def calculer_taux_mensuel(taux_annuel):
    """
    Fonction calculant le taux mensuel
    :param taux_annuel: réel representant le taux_annuel
    :return taux_mensuel: réel representant le taux des mensualités

    """
    taux_mensuel = ((1 + taux_annuel) ** (1 / 12)) - 1
    return taux_mensuel

def calculer_mensualite(capital, taux_annuel, N):    

    """
    Fonction calculant le montant des mensualites
    :param capital: capital emprunté par le client
    :param taux_annuel:  réel representant le taux_annuel des interets
    :param N: entier representant le nombre de mensualites
    :return mensualite: entier des mensualites

    """
    mensualites = capital * (calculer_taux_mensuel(taux_annuel) / (1 - (1 + calculer_taux_mensuel(taux_annuel)) ** (-N)))
    return mensualites



def calculer_solde_capital(capital, taux_annuel, N, nb_mensualites_restantes):
    """
    Fonction calculant le solde du capital qu'il reste à payer
    :param capital: capital emprunté par le client
    :param taux_annuel: réel représentant le taux_annuel des interets
    :param N: entier representant le nombre de mensualites
    :param nb_mensualites_restantes: nombre de mensualoites restantes à payer
    :return: solde: solde du capital qu'il reste à payer
    """

    solde = calculer_mensualite(capital, taux_annuel, N) * ((1 - (1 + calculer_taux_mensuel(taux_annuel)) ** -nb_mensualites_restantes) / calculer_taux_mensuel(taux_annuel))
    return solde
