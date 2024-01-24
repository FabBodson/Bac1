entier = int(input('Entrez un entier: '))


# [8: 10[

if 8 <= entier < 10:
    print(f'Il est compris dans [8: 10[')


# ]-∞;-5] U [5;+∞[

elif entier <= -5 or entier >= 5:
    print(f'Il est compris dans ]-∞;-5] U [5;+∞[')

# ]-∞;0] U [5;10[

elif entier <= 0 or 5 <= entier < 10:
    print(f'Il est compris dans ]-∞;0] U [5;10[')


# [-5;15] / {0}

elif (-5 <= entier <= 15) and entier != 0:
    print(f'Il est compris dans [-5;15] != 0')
