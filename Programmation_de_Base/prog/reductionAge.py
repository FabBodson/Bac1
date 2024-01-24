def reduction(age, prix_billet):

    if (0 <= age <= 12) or (65 <= age):
        montant_reduction = prix_billet * 0.5

    elif 13 <= age <= 18:
        montant_reduction = prix_billet * 0.4

    elif 19 <= age <= 25:
        montant_reduction = prix_billet * 0.3

    else:
        montant_reduction = 0

    return prix_billet - montant_reduction



def _main():
    print(f'Prix du billet: {reduction(30, 30)} €')


if __name__ == '__main__':
    _main()