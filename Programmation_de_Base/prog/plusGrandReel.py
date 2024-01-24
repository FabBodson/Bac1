reel1 = float(input('Donnez un 1er nombre réel: '))
reel2 = float(input('Donnez un 2nd nombre réel: '))


if reel1 < reel2:
    print(f'{reel2} est le plus grand')

elif reel1 > reel2:
    print(f'{reel1} est le plus grand')

else:
    print('Ils sont égaux')

"""

plus_grand = max(reel1, reel2)

print(f'{plus_grand} est le plus grand')"""