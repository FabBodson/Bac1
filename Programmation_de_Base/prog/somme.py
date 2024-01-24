montant = int(input('Quel montant voulez-vous décomposer ? (Nombre entier)\n'))

nbr_billets200 = montant // 200
reste = montant % 200

nbr_billets100 = reste // 100
reste = reste % 100

nbr_billets50 = reste // 50
reste = reste % 50

nbr_billets20 = reste // 20
reste = reste % 20

nbr_billets10 = reste // 10
reste = reste % 10


print(f'Nombre de billets de 200: {nbr_billets200}')
print(f'Nombre de billets de 100: {nbr_billets100}')
print(f'Nombre de billets de 50: {nbr_billets50}')
print(f'Nombre de billets de 20: {nbr_billets20}')
print(f'Nombre de billets de 10: {nbr_billets10}\n')


print(f'200x{nbr_billets200} = {200 * nbr_billets200}')
print(f'100x{nbr_billets100} = {100 * nbr_billets100}')
print(f'50x{nbr_billets50} = {50 * nbr_billets50}')
print(f'20x{nbr_billets20} = {20 * nbr_billets20}')
print(f'10x{nbr_billets10} = {10 * nbr_billets10}')