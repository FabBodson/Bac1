
premiere_valeur = float(input('Entrez une 1ere valeur: '))
plus_petit = premiere_valeur
plus_grand = premiere_valeur

for i in range(5):
    nouvelle_valeur = float(input('Entrez le prochain nombre à comparer: '))

    plus_petit = min(nouvelle_valeur, plus_petit)
    plus_grand = max(nouvelle_valeur, plus_grand)

    print(f'Plus de petit: {plus_petit}\tPlus grand: {plus_grand}')